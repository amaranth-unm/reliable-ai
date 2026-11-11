#!/usr/bin/env python3
"""Record the replies shown on a session page, from a plan file.

Each session that shows recorded replies has a plan at
workshop-drafts/<session>/runs-plan.json. The plan lists conversations
("chains"). Each chain is a fresh headless Claude Code session, and each
turn in it is one message: pasted files, then a prompt taken word for word
from _data/prompts.yml (with its brackets filled as the page says), or a
literal message. Later turns continue the same session with --resume, which
is what the page means by "in the same chat".

    python3 scripts/record-runs.py workshop-drafts/editorial-assistant/runs-plan.json
    python3 scripts/record-runs.py PLAN --only baseline,roles   # some chains
    python3 scripts/record-runs.py PLAN --dry-run               # show messages

Everything goes to workshop-drafts/<session>/_local/runs-<date>/<chain>/:
the exact message sent (NN-<name>.msg.txt), the reply (NN-<name>.md), the
raw JSON, any files the run wrote, and sessions.json. Copy replies into
_data/demos.yml by hand, trimming with […] and saying in the note what was
cut. Never edit a reply's wording.

Plan format:
{
  "session": "editorial-assistant",
  "model": "claude-opus-5-5",
  "inputs": "assets/editorial-assistant/data",   # where pasted/attached files live
  "tools": "",               # default tool list for chains ("" = none, a plain chat)
  "settings": null,          # optional settings JSON string, e.g. a sandbox
  "chains": [
    {"name": "baseline", "tools": "", "turns": [
      {"name": "edit", "paste": ["syllabus-policy.txt"], "prompt": "baseline"},
      {"name": "fix", "text": "Put 'should' back in the first sentence."},
      {"name": "brief", "prompt": "editorial-brief",
       "fill": {"[genre: seminar paper / abstract / syllabus policy / cover letter]": "syllabus policy"}},
      {"name": "read", "attach": ["report.docx"], "prompt": "word-comments"}
    ]}
  ]
}

"paste" puts each file's text above the prompt, separated by a blank line,
as someone would paste it into a chat. "attach" copies the file into the
run's working folder; give the chain the Read tool so it can open it.
"after" names other chains whose last reply should be pasted first, which
is how a comparison prompt receives two readings. "attach_note": true adds a
last line listing the attached files, the way a chat window shows them.

A chain with "continue": "<other chain>" resumes that chain's conversation
and folder, so a later phase can follow up on a reply after you've read it.

Chain options for agent runs: "workdir" (another chain's name, to work in
the same folder, as when a new session opens the same project), "setup"
(files or folders, relative to the repo, copied into the folder first),
"allowed" (tools pre-approved, passed to --allowedTools), "setting_sources"
("" by default; "project" loads the folder's own .claude settings and
agents). A turn with "save": {"path/in/folder": "prompt-id"} writes that
prompt's text to the folder without sending anything, as when the page says
"Save this as instructions/reading.md".

For browser-chat runs, where the reply sets each file out as a filename
followed by a code block, a turn with "extract": true writes those blocks to
the folder, as the participant does by copying them out. "extract_append"
lists files whose new block is added to the end instead (prompts.md).
"save_reply": "baseline.md" saves the whole reply as one file. A chain with
"files_from": "<other chain>" can attach files from that chain's folder,
as when a participant brings their saved files into a new conversation.
"""
import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def load_prompts():
    data = yaml.safe_load((ROOT / "_data" / "prompts.yml").read_text(encoding="utf-8"))
    return {p["id"]: p for p in data}


def build_message(turn, prompts, inputs, outdir):
    parts = []
    for ref in turn.get("after", []):
        replies = sorted((outdir / ref).glob("[0-9][0-9]-*.md"))
        if not replies:
            sys.exit(f"chain '{ref}' has no reply yet; run it first")
        parts.append(replies[-1].read_text(encoding="utf-8").strip())
    for name in turn.get("paste", []):
        parts.append((inputs / name).read_text(encoding="utf-8").strip())
    if "prompt" in turn:
        text = prompts[turn["prompt"]]["text"].strip()
        fills = dict(turn.get("fill", {}))
        for slot, name in turn.get("fill_files", {}).items():
            fills[slot] = (inputs / name).read_text(encoding="utf-8").strip()
        for slot, value in fills.items():
            if slot not in text:
                sys.exit(f"slot {slot!r} not found in prompt {turn['prompt']}")
            text = text.replace(slot, value)
        parts.append(text)
    if "text" in turn:
        parts.append(turn["text"].strip())
    if turn.get("attach_note") and turn.get("attach"):
        parts.append("[Attached: " + ", ".join(turn["attach"]) + "]")
    return "\n\n".join(parts)


FILE_BLOCK = re.compile(r"^[*`]*([\w./-]+\.\w+)[*`]*:?[ \t]*\n+(`{3,})[^\n]*\n(.*?)\n\2[ \t]*$",
                        re.M | re.S)


def extract_files(reply, work, append=()):
    """Write each 'filename' + code block in a reply into the folder."""
    names = []
    for name, _, body in FILE_BLOCK.findall(reply):
        dest = work / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        if name in append and dest.exists():
            body = dest.read_text(encoding="utf-8").rstrip() + "\n\n" + body
        dest.write_text(body.rstrip() + "\n", encoding="utf-8")
        names.append(name)
    return names


def run_chain(chain, plan, prompts, inputs, outdir, dry):
    cdir = outdir / chain["name"]
    cdir.mkdir(parents=True, exist_ok=True)
    session_id = None
    base = chain.get("continue")
    if base:
        prev = json.loads((outdir / base / "sessions.json").read_text(encoding="utf-8"))
        session_id = prev[-1]["session_id"]
    work = outdir / chain.get("workdir", base or chain["name"]) / "work"
    work.mkdir(parents=True, exist_ok=True)
    for item in chain.get("setup", []):
        src = ROOT / item.rstrip("/.")
        dest = work if item.endswith("/.") else work / src.name
        if src.is_dir():
            shutil.copytree(src, dest, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dest)
    tools = chain.get("tools", plan.get("tools", ""))
    settings = chain.get("settings", plan.get("settings"))
    record = []
    for i, turn in enumerate(chain["turns"], 1):
        if "save" in turn:
            for dest, pid in turn["save"].items():
                (work / dest).parent.mkdir(parents=True, exist_ok=True)
                (work / dest).write_text(prompts[pid]["text"], encoding="utf-8")
            print(f"{chain['name']}: saved {', '.join(turn['save'])}")
            continue
        for name in turn.get("attach", []):
            src = inputs / name if (inputs / name).exists() else work / name
            if not src.exists() and chain.get("files_from"):
                src = outdir / chain["files_from"] / "work" / name
            if src != work / name:
                (work / name).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, work / name)
        msg = build_message(turn, prompts, inputs, outdir)
        stem = f"{i:02d}-{turn['name']}"
        (cdir / f"{stem}.msg.txt").write_text(msg + "\n", encoding="utf-8")
        if dry:
            print(f"--- {chain['name']}/{stem} (tools={tools!r})\n{msg}\n")
            continue
        cmd = ["claude", "-p", msg, "--model", plan.get("model", "claude-opus-5-5"),
               "--strict-mcp-config", "--setting-sources", chain.get("setting_sources", ""),
               "--tools", tools,
               "--output-format", "json", "--permission-mode",
               chain.get("permission_mode", "acceptEdits")]
        if settings:
            cmd += ["--settings", settings]
        if chain.get("allowed"):
            cmd += ["--allowedTools", chain["allowed"]]
        if session_id:
            cmd += ["--resume", session_id]
        res = subprocess.run(cmd, cwd=work, capture_output=True, text=True)
        (cdir / f"{stem}.json").write_text(res.stdout, encoding="utf-8")
        if res.stderr:
            (cdir / f"{stem}.err").write_text(res.stderr, encoding="utf-8")
        try:
            out = json.loads(res.stdout)
        except json.JSONDecodeError:
            sys.exit(f"{chain['name']}/{stem}: no JSON reply; see {stem}.err")
        session_id = out.get("session_id", session_id)
        reply = out.get("result", "")
        (cdir / f"{stem}.md").write_text(reply + "\n", encoding="utf-8")
        if turn.get("save_reply"):
            (work / turn["save_reply"]).write_text(reply + "\n", encoding="utf-8")
        if turn.get("extract"):
            saved = extract_files(reply, work, turn.get("extract_append", []))
            print(f"{chain['name']}/{stem}: saved {', '.join(saved) or 'no files'}")
        record.append({"turn": stem, "session_id": session_id,
                       "num_turns": out.get("num_turns"), "is_error": out.get("is_error")})
        print(f"{chain['name']}/{stem}: done ({out.get('num_turns')} turns, error={out.get('is_error')})")
    if not dry:
        (cdir / "sessions.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("plan")
    ap.add_argument("--only", help="comma-separated chain names")
    ap.add_argument("--date", default=dt.date.today().isoformat())
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    plan_path = Path(a.plan).resolve()
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    prompts = load_prompts()
    inputs = ROOT / plan["inputs"]
    outdir = ROOT / "workshop-drafts" / plan["session"] / "_local" / f"runs-{a.date}"
    outdir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(plan_path, outdir / "runs-plan.json")
    only = set(a.only.split(",")) if a.only else None
    for chain in plan["chains"]:
        if only and chain["name"] not in only:
            continue
        run_chain(chain, plan, prompts, inputs, outdir, a.dry_run)


if __name__ == "__main__":
    main()

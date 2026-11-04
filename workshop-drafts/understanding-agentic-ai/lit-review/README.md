# Literature review starter

For the Understanding Agentic AI workshop. The folder holds instructions and
no articles: the agent finds and saves those.

## Run it

The folder is set up for Claude Code. Open a terminal in this folder, run
`claude` and send the prompts from the workshop page in order.

Other agents read a similar instructions file under another name; Codex, for
example, reads `AGENTS.md`. Copy `CLAUDE.md` to that name. The skill and
helper-agent files in `.claude/` are in Claude Code's format. In another tool,
point the agent at them by path, or have the lead agent read every article
itself.

## What's here

- `CLAUDE.md`: the workflow the lead agent follows.
- `brief.md`: the question, scope, limits and when the work is done.
- `progress.md`: where the project stands.
- `.claude/skills/read-article/SKILL.md`: how to read one article.
- `.claude/skills/relate-articles/SKILL.md`: how to relate the notes.
- `.claude/agents/reader.md`: a helper that reads one PDF.
- `.claude/agents/checker.md`: a helper that checks the synthesis.

The `.claude` folder is hidden because its name starts with a dot. On a Mac,
press Cmd+Shift+. in Finder to show it. In Windows File Explorer, choose
View → Show → Hidden items.

## What the agent adds

`sources.md`, `pdfs/`, `notes/`, `synthesis.md`, `synthesis-log.md`,
`history/`, `checks.md` and `leads.md`.

These instructions were written for the workshop on 2026-11-04. Nothing in
the starter folder is a recorded agent output.

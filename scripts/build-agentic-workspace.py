#!/usr/bin/env python3
"""Package the Understanding Agentic AI starter folder.

Source: workshop-drafts/understanding-agentic-ai/lit-review/ (edit files there).
Writes:
  assets/agentic-ai/lit-review-starter.zip   the participant download
  assets/agentic-ai/files/                   plain-text copies linked from the page.
      Jekyll skips the hidden .claude folder, and the github-pages gem renders any
      .md file as a page (consuming its front matter), so each copy is a .txt file
      whose first line names the original.
"""
from pathlib import Path
import shutil
import zipfile

root = Path(__file__).resolve().parents[1]
src = root / 'workshop-drafts/understanding-agentic-ai/lit-review'
out = root / 'assets/agentic-ai'
stamp = (2026, 11, 4, 0, 0, 0)

files = sorted(p for p in src.rglob('*') if p.is_file() and p.name != '.DS_Store')
if not files:
    raise SystemExit(f'No files in {src}')

out.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(out / 'lit-review-starter.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for path in files:
        info = zipfile.ZipInfo('lit-review/' + path.relative_to(src).as_posix(), stamp)
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        z.writestr(info, path.read_bytes())

readable = {
    'CLAUDE.md': 'CLAUDE.txt',
    'brief.md': 'brief.txt',
    '.claude/skills/read-article/SKILL.md': 'read-article-skill.txt',
    '.claude/skills/relate-articles/SKILL.md': 'relate-articles-skill.txt',
    '.claude/agents/reader.md': 'reader-agent.txt',
    '.claude/agents/checker.md': 'checker-agent.txt',
}
copies = out / 'files'
if copies.exists():
    shutil.rmtree(copies)
copies.mkdir()
for source, name in readable.items():
    header = f'File: lit-review/{source}\n\n'
    (copies / name).write_text(header + (src / source).read_text(), encoding='utf-8')

print(f'Zipped {len(files)} files to {out / "lit-review-starter.zip"}; '
      f'copied {len(readable)} readable files to {copies}.')

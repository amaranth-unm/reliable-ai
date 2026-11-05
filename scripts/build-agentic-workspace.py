#!/usr/bin/env python3
"""Package the starting folder for the Understanding Agentic AI session:
the files a participant writes, with none of the agent's outputs.

The brief and the instruction files are the "Save as …" entries in
_data/prompts.yml (those with a `file` key), so the page and the download
always match. CLAUDE.md, progress.md and README.md come from
workshop-drafts/understanding-agentic-ai/lit-review/.

Writes:
  assets/agentic-ai/lit-review-starting-folder.zip   the participant download
  assets/agentic-ai/CLAUDE.txt                    the prepared CLAUDE.md, as plain
      text (the github-pages gem would render a .md copy as a page)
"""
from pathlib import Path
import shutil
import zipfile

import yaml

root = Path(__file__).resolve().parents[1]
drafts = root / 'workshop-drafts/understanding-agentic-ai/lit-review'
out = root / 'assets/agentic-ai'
stamp = (2026, 11, 4, 0, 0, 0)

prompts = yaml.safe_load((root / '_data/prompts.yml').read_text())
files = {
    p['file']: p['text']
    for p in prompts
    if p.get('session') == 'understanding-agentic-ai' and p.get('file')
}
for name in ('CLAUDE.md', 'progress.md', 'README.md'):
    files[name] = (drafts / name).read_text()

if out.exists():
    shutil.rmtree(out)
out.mkdir(parents=True)

with zipfile.ZipFile(out / 'lit-review-starting-folder.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for name in sorted(files):
        info = zipfile.ZipInfo('lit-review/' + name, stamp)
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        z.writestr(info, files[name])
    # Sample PDFs from the brief's backup set, so nobody depends on a
    # download working in the room.
    for pdf in sorted((drafts / 'sample-pdfs').glob('*.pdf')):
        info = zipfile.ZipInfo('lit-review/sample-pdfs/' + pdf.name, stamp)
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        z.writestr(info, pdf.read_bytes())

(out / 'CLAUDE.txt').write_text(files['CLAUDE.md'], encoding='utf-8')
print(f'Wrote {len(files)} files to {out / "lit-review-starting-folder.zip"} and CLAUDE.txt.')

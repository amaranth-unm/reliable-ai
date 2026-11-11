#!/usr/bin/env python3
"""Zip a session's data files for the page's "download all" link.

The files in assets/<folder>/data/ are the inputs attached or pasted in the
recorded runs, with a README.txt giving each one's source. Edit them there,
then run, for example:

    python3 scripts/build-session-data.py editorial-assistant
    python3 scripts/build-session-data.py agentic-ai
    python3 scripts/build-session-data.py audit-trails

The ZIP is written to assets/<folder>/<folder>-data.zip, with every file
inside a folder of the same name.

A second form zips any folder, for downloads such as a finished agent
folder whose Markdown files shouldn't be served as pages:

    python3 scripts/build-session-data.py agentic-ai \
        workshop-drafts/understanding-agentic-ai/lit-review-finished lit-review-finished.zip

That zips the folder's contents into assets/agentic-ai/lit-review-finished.zip. (Mapping with AI has its own script,
build-mapping-data.py, which does the same.)
"""
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if len(sys.argv) not in (2, 4):
    sys.exit(__doc__)
folder = sys.argv[1]
if len(sys.argv) == 4:
    data, out, prefix = ROOT / sys.argv[2], ROOT / "assets" / folder / sys.argv[3], ""
else:
    data = ROOT / "assets" / folder / "data"
    out = ROOT / "assets" / folder / f"{folder}-data.zip"
    prefix = f"{folder}-data/"
files = sorted(p for p in data.rglob("*") if p.is_file() and not p.name.startswith("."))
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for p in files:
        z.write(p, f"{prefix}{p.relative_to(data)}")
size = out.stat().st_size / 1e6
print(f"wrote {out.relative_to(ROOT)} ({len(files)} files, {size:.1f} MB)")

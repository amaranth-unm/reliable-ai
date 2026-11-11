#!/usr/bin/env python3
"""Zip the Mapping with AI data files for the page's "download all" link.

The files in assets/mapping-with-ai/data/ are the inputs attached to the
recorded runs. Edit them there, then run:

    python3 scripts/build-mapping-data.py
"""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "assets" / "mapping-with-ai" / "data"
OUT = ROOT / "assets" / "mapping-with-ai" / "mapping-with-ai-data.zip"

files = sorted(p for p in DATA.iterdir() if p.is_file() and not p.name.startswith("."))
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for p in files:
        z.write(p, f"mapping-with-ai-data/{p.name}")
print(f"wrote {OUT.relative_to(ROOT)} ({len(files)} files)")

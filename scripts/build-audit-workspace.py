#!/usr/bin/env python3
"""Regenerate prepared downloads from the same manifest used by the viewer."""
from pathlib import Path
import json
import zipfile

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / '_data/audit_workspace.json').read_text())
folder = root / 'assets/audit-trails/humanities-ai'
folder.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(folder.parent / 'example-workspace.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
    for entry in manifest['files']:
        relative = Path(entry['path'])
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError('Example filename must stay inside the workspace')
        target = folder / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(entry['content'])
        # Stable ZIP metadata keeps regeneration from changing an unchanged archive.
        info = zipfile.ZipInfo('humanities-ai/' + relative.as_posix(), (2026, 10, 11, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        archive.writestr(info, entry['content'])
print(f"Updated {len(manifest['files'])} prepared files and the ZIP.")

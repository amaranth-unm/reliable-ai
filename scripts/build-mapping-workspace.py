#!/usr/bin/env python3
"""Generate both teaching maps and the participant kit from the saved examples."""
import html
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'workshop-drafts/mapping-with-ai'
OUT = ROOT / 'assets/mapping-with-ai'

def main():
    data = json.loads((ROOT / '_data/mapping_examples.json').read_text())
    OUT.mkdir(parents=True, exist_ok=True)
    template = (SOURCE / 'map-template.html').read_text()
    outputs = []
    for key, name in [('research', 'research'), ('monuments', 'monuments')]:
        collection = data[key]
        ids = [r['id'] for r in collection['records']]
        assert len(ids) == len(set(ids)), 'Duplicate record IDs'
        for r in collection['records']:
            assert (r['lat'] is None) == (r['lon'] is None)
            if r['lat'] is not None:
                assert -90 <= r['lat'] <= 90 and -180 <= r['lon'] <= 180
        for p in collection.get('photographs', []):
            assert p['monument_id'] in ids, 'Unlinked photograph'
        raw = json.dumps(collection, ensure_ascii=False, indent=2)
        substitutions = {'__TITLE__': html.escape(collection['title']), '__STYLE__': (SOURCE / 'map.css').read_text(), '__SCRIPT__': (SOURCE / 'map.js').read_text(), '__DATA__': raw.replace('<', '\\u003c')}
        page = template
        for token, value in substitutions.items():
            page = page.replace(token, value)
        filename = name + '-map.html'
        (OUT / filename).write_text(page)
        outputs.append(filename)
        filename = 'research-reviewed.json' if key == 'research' else 'monuments.json'
        (OUT / filename).write_text(raw + '\n')
        outputs.append(filename)
    for filename in ['practice-texts.txt', 'README.txt']:
        (OUT / filename).write_text((SOURCE / filename).read_text())
        outputs.append(filename)
    with ZipFile(OUT / 'mapping-practice-kit.zip', 'w', ZIP_DEFLATED) as kit:
        for filename in outputs:
            kit.write(OUT / filename, arcname='mapping-practice-kit/' + filename)
    print(f'Built {len(outputs)} files and mapping-practice-kit.zip')

if __name__ == '__main__':
    main()

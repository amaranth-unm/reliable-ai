MAPPING WITH AI — PRACTICE KIT
Reliable AI for Humanists · Amaranth · University of New Mexico
Prepared 28 October 2026

START HERE
Unzip the kit. Open research-map.html or monuments-map.html in a browser.
No installation or mapping account is needed. Internet access is needed for
Leaflet (the map library), OpenStreetMap backgrounds, and NPS photographs.
If those fail, the collection lists and source passages remain available.
The maps contain their data; they do not fetch the adjacent JSON files.
Editing a JSON file therefore does not automatically update a map.

FILES
practice-texts.txt: three fictional letters created for this workshop.
research-reviewed.json: prepared readings of ten references in those letters.
research-map.html: searchable map and list of those references.
monuments.json: two real memorials and three linked photograph records.
monuments-map.html: prepared public browsing interface.

These are prepared examples, not recorded AI replies. The HTML files can be
provided to a coding assistant alongside the data when requesting changes.
For a new map, attach the appropriate JSON file to your AI tool and use the
session's interface prompt. Save the original data before requesting edits.
Download data always exports the full collection, regardless of active filters.

RESEARCH EXAMPLE
The letters, dates, and journeys are fictional. Exact supporting quotations
are kept in the reference records. Interpretations can be disputed. City
coordinates come from the GeoNames record named in each location note,
checked 29 October 2026 and rounded to two decimals (about 1 km). They
represent cities, not archival places of residence. Springfield is
unresolved; the pronoun "there" is intentionally left unlocated pending a
reader's decision. Paris has two references at one point. Unlocated
records stay in the list. No route or historical boundary
is claimed. This example demonstrates a process, not a historical finding.

PUBLIC HISTORY EXAMPLE: SOURCES
The source pages and image credits were reviewed on 28 October 2026.
Historical descriptions are workshop summaries, not quoted inscriptions.

M1: District of Columbia War Memorial. The NPS page supports the dedication
date (11 November 1931), local commemoration, and dual use as a memorial and
performance space:
https://www.nps.gov/nama/planyourvisit/dc-war-memorial.htm
Photo P1 is credited on the following NPS page to Nathan Adams:
https://www.nps.gov/places/000/district-of-columbia-war-memorial.htm

M2: World War I Memorial. NPS describes its national commemorative purpose
and identifies the Pershing statue and Belvedere photographs:
https://www.nps.gov/wwim/index.htm
The dedication date is not supplied in this sample. This is an incomplete
record, not a claim that a date cannot be found.

P1 source image:
https://www.nps.gov/common/uploads/cropped_image/primary/FB09418F-E317-438F-C1BA9F6D19854F78.jpg?mode=crop&quality=90&width=1000
P2 source image (Pershing statue):
https://www.nps.gov/common/uploads/structured_data/CB4DB522-0F64-662E-7F41883E1BEC3066.jpg?maxHeight=800&maxWidth=1200&quality=90
P3 source image (Belvedere):
https://www.nps.gov/common/uploads/structured_data/F758D02B-D733-5F8B-301195968EB96177.jpg?maxHeight=800&maxWidth=1200&quality=90

P2 and P3 are credited NPS Photo. Alt text is written for this workshop.
NPS says NPS-created material is generally public domain unless otherwise
indicated, and cautions that third-party material may have other rights:
https://www.nps.gov/aboutus/disclaimer.htm
Preserve photograph credits and check the item-level source before reuse.
Images are loaded from NPS; they are not packaged as local image files.

POINT LOCATIONS
Monument coordinates were supplied as approximate demonstration site points.
Their exact placement has not been independently verified. They are neither
surveyed coordinates nor directions to entrances. Replace them with checked
locations before using this as a visitor guide. The two selected memorials
cannot support a claim about national patterns or collection completeness.

MAP SOFTWARE
Leaflet 1.9.4, following its official quick-start example:
https://leafletjs.com/examples/quick-start/
Leaflet is loaded from unpkg.com, not bundled in this kit.
Background tiles: https://tile.openstreetmap.org/{z}/{x}/{y}.png
Attribution: © OpenStreetMap contributors
https://www.openstreetmap.org/copyright
For public deployment, review the tile provider's usage policy:
https://operations.osmfoundation.org/policies/tiles/

MAINTAINING THESE MATERIALS
In the reliable-ai repository, edit _data/mapping_examples.json and the
files in workshop-drafts/mapping-with-ai/. Then run:
python3 scripts/build-mapping-workspace.py
This regenerates the maps, data exports, and ZIP under assets/mapping-with-ai/.

# Mapping with AI: presenter guide

50 minutes, beginners, no coding or GIS experience. Session page:
`sessions/mapping-with-ai/index.md`. Materials are prepared teaching examples;
do not describe them as successful live model runs.

## What participants should leave able to do

Turn a familiar source into a checkable place table; catch a wrong or
unsourced coordinate and replace it from a gazetteer; explain a map's claim;
describe a useful interface change in ordinary language and test it.

## Run of show

| Minutes | Action | Visible result |
|---|---|---|
| 0–4 | Open both prepared maps. Click a reference and a monument. Ask what a map might make possible for someone's own collection. | Two concrete outcomes before tool setup. |
| 4–10 | Read the fictional letters together. Participants paste them into chat with the extraction prompt in step 1. | A table they can check against a short, familiar text. |
| 10–16 | Participants check roles and unresolved locations in pairs. Compare Las Vegas, Paris, Springfield, and “there.” Use the follow-up in step 2 only if needed. | At least one explicit correction or decision. |
| 16–25 | Step 3. New chat, bare list (3 min): ask the room which Las Vegas and Springfield they got and how many decimals. Source follow-up and two links (2 min). Look up Las Vegas and a bare Santa Fe in GeoNames on screen; show the gazetteer prompt (4 min). | A coordinate the room has caught, then one row with a record ID. |
| 25–32 | Use the prepared research map. Filter completed/planned travel; find Paris and the unlocated references. Point out the GeoNames IDs in the location notes. | A question prompted by the map and checked in the source. |
| 32–40 | Open the monument map. Show one site with two photos, local/national filtering, and sources. Demonstrate the photograph prompt on P1; distinguish visible form from historical metadata. | A collection structure participants can apply to their photos. |
| 40–47 | Presenter attaches monuments.json and requests the interface in step 6. While it generates, participants describe one change for their own audience. Test the result, or use the prepared version. | An interface request and a concrete test. |
| 47–50 | Ask each person to name their pilot collection and one action the map should support. Revisit the takeaways. | A next step small enough to try. |

## Teaching choices

Research is the hands-on core; public history is the second case and a
presenter demonstration. Building two interfaces live would crowd out time
for participants to use them. With a slow room, skip the second AI follow-up
and the live interface generation. In step 3, keep the bare list and the Las
Vegas lookup; the source follow-up and gazetteer prompt can be shown rather
than run. Preserve the research exploration and photo-to-collection
demonstration.

The research table's ten records represent references, not ten places or ten
journeys. Eight located references share five city points; two references
remain unlocated. Filtering planned travel yields one located and one
unlocated reference. Completed travel yields only the reported Santa Fe visit.
Use the L2 sentence about postponed travel to discuss whether even the planned
Las Vegas journey should appear in a map of completed travel.

“there” probably means Santa Fe. Leaving it unlocated is a deliberate,
debatable editorial choice, not a claim that resolving pronouns is impossible.
A participant who resolves it with a stated reason has made a defensible
interpretation. AI rechecking itself is not an independent source check.

Step 3 shows the failure before the fix, and the room's own replies are the
evidence. The bare list deliberately drops the states the letters supply. Do
not predict on screen what a tool will return; ask what people got. If a
reply flags the ambiguity or declines to guess, that is a good result: ask
what it would have done with three hundred names and no one reading each
row. The source follow-up may return fabricated links or, from a tool with
web search, working ones. Either is useful. A working link makes the choice
checkable, and the person still decides whether it is the right place.

Facts checked 29 October 2026 (GeoNames RDF and the Wikidata API):

- Las Vegas, New Mexico: GeoNames 5475433, 35.59393, −105.2239 (Wikidata
  Q676171). Las Vegas, Nevada: GeoNames 5506956, 36.17497, −115.13722. The
  two points are 895 km apart.
- A bare “Santa Fe” search lists Santa Fe, Argentina first in both GeoNames
  (3836277) and Wikidata (Q44244). New Mexico's capital is GeoNames 5490263.
- Gazetteers place one city differently. Wikidata's Santa Fe point
  (35.6667, −105.9667) is 3.4 km from GeoNames' (35.68698, −105.9378).
  Neither is wrong: a city point is a convention, which is why the record ID
  matters more than the numbers.
- Curated links need opening too. Wikidata's GeoNames link for Paris (Q90)
  points to 2968815, the Paris Department; the city is 2988507. The prepared
  data uses 2988507.
- All five prepared city points are the GeoNames coordinates rounded to two
  decimals. Rounding Paris moved it from 48.86 to 48.85.
- Precision: 0.0001° of latitude is about 11 m; 0.01° is about 1.1 km.

The monuments sample uses two real nearby sites rather than pretending to be
a representative survey. It is a small prototype of an imagined larger photo
collection. Both carry approximate, unverified site points. State this while
showing them. Historical source summaries are checked; exact marker placement
has not been independently checked. Before using this as a public visitor
guide, verify coordinates and entrances, complete the metadata, and check
photo rights at the source. Do not present this prototype as published research.

Do not ask AI to identify the monument by its appearance. Ask what can be
observed, then supply a source page to fill historical fields. If a source
page and photograph disagree, preserve the disagreement for review.

## Rehearsal and fallbacks

- Run `python3 scripts/build-mapping-workspace.py` after changing example data.
- Preview future session bodies with the existing local config:
  `bundle exec jekyll serve --config _config.yml,_config.local.yml`.
- Open both maps at laptop and phone widths. Test search, relationship or
  commemoration filters, unlocated records, reset, source links, data download,
  and keyboard access. Compare exported data with the source JSON.
- Confirm the venue network loads unpkg, OpenStreetMap, and NPS images. The
  maps keep their lists if external services fail, but photos are remote.
- Rehearse the bare coordinate list, image prompt and interface prompt with
  the account you will use. Free-account limits vary; keep the prepared maps
  open throughout.
- If recording an actual response for the site, save exact inputs, output,
  tool, date, source coverage, and context under `_local/`. Add a recorded
  demo only after that run exists; never substitute a prepared example.
- For a text-only AI account, compare the monument card with its source page
  and discuss what cannot be inferred from the overview photograph.

## Scope for the next iteration

The supplied texts are fictional so people can concentrate on the method.
A stronger research case could use a short, openly reusable historical source
that Fred already knows well. Replace the fictional material and prepared
readings together; preserve passage references and explicit uncertain cases.
For the monument case, an actual researcher photo collection would make the
example more personal. Keep original filenames, one monument ID per site,
multiple photograph records, and separate photo dates from dedication dates.

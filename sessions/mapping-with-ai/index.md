---
title: Mapping with AI
presenter: Fred Gibbs
layout: base
position: 5
date: 2026-11-11
time: "12:00–12:50"
location: History Commons (MVH 1104)
kicker: Session 4 · November 11, 2026
summary: "Explore places in research texts and turn photographs of WWI monuments into a public map, using AI to organize the material and help build the interface."
points:
  - title: Explore the geography of a text
    text: Extract place references, return to their passages, and distinguish a place mentioned from a place visited.
  - title: Give a photograph collection a public interface
    text: Browse WWI monuments through a map, photographs, and short descriptions linked to sources.
  - title: Ask for the map you need
    text: Describe filters and other changes in ordinary language, then test what AI builds.
note: "Bring a laptop and access to an AI chat tool. Practice materials provided; no coding or mapping experience needed."
thumbnail: "/assets/images/stradanus-press-1600.jpg"
header-image: "/assets/images/stradanus-press-1600.jpg"
header-tier: section
header-filter: etching
header-position: center right
header-opacity: 0.18
header-title: Mapping with AI
header-subtitle: "Use AI to help turn research materials into maps you can explore and share. Keep the evidence attached as you decide what each point means."
header-caption: "Jan van der Straet (Stradanus), <i>Impressio Librorum</i>, from <i>Nova Reperta</i>, engraved by Joannes Galle. Museum Plantin-Moretus, public domain."
tags: [mapping, research, public history]
workshop_mode: true
---

{% include nav/scrollspy-toc.html %}

Work down this page during the session or return to it later. The practice materials, working maps, and prompts stay together so you can repeat the exercises with your own sources.
{: .lead}

<div class="rule" markdown="1">
**Keep a source and a location decision attached to every point.**
</div>

## Introduction
{: .step #introduction}

### Why your research materials are the place to start

You have letters full of place names, or hundreds of photographs of monuments. A map could help you ask questions of the collection or share it with other people. Getting from those materials to a useful interface can require skills you have never needed to learn.

Today you will try two uses of AI. First, use it to organize place references from texts so you can explore a research question. Then ask it to help build an interface through which visitors can browse photographs of WWI monuments. **Your knowledge of the sources gives you a way to judge both the information and the map.**

### What you're working with

- AI can propose a table of place references from prose. Check its quotations and its reading of what happened in each place (steps 1 and 2).
- AI will supply coordinates for any list of names. Check which place it chose, then take the location from a gazetteer record you can cite (step 3).
- A map lets you filter those references and return to their passages. Use it to ask a question the text alone makes harder to follow (step 4).
- AI can help write an interface's code. Describe what a visitor needs to do and test a proposed change against the collection (steps 5 and 6).

### Before you start

- Bring a laptop with an AI chat tool you can already use. The text exercise needs ordinary chat; the photograph demonstration needs image input.
- Open the [research map]({{ site.baseurl }}/assets/mapping-with-ai/research-map.html) and [monument map]({{ site.baseurl }}/assets/mapping-with-ai/monuments-map.html). Neither requires an account. Map backgrounds and monument photographs need internet access; the lists and source passages remain usable if those services fail.
- Download the [practice kit]({{ site.baseurl }}/assets/mapping-with-ai/mapping-practice-kit.zip) to keep the texts, reviewed data, and both maps. The HTML files open in a browser; nothing needs installing.

<div class="reminder" markdown="1">
Use material you have permission to share, such as your own research or the practice materials provided here.
</div>

### About the examples

The research exercise uses three short **fictional letters written for this workshop**, with a prepared reference table. The monument example uses two real Washington, DC memorials and three credited National Park Service photographs. Its descriptions are prepared summaries linked to NPS pages. Both interfaces are prepared teaching examples, not records of a live AI run. Monument points are approximate site locations, not surveyed positions or visitor directions. See the kit's README for sources and limitations.

## 1. Turn a question into a table
{: .step #step-1}

Open the [practice letters]({{ site.baseurl }}/assets/mapping-with-ai/practice-texts.txt). Read them before asking AI to do anything. Our research question is: **Which places belong to the writer's movements, and which enter through correspondence, plans, or imagination?**

Paste the letters into your chat, then send this request.

{% include prompt.html id="mapping-extract" %}

Look for the distinction between where a letter was written and the other places it names. In L1, the writer puts a journey to Santa Fe in the past but a journey to Las Vegas in the future. In L2, Paris appears through postcards, and the writer explicitly says they have never been there. Mapping all these references as visits would give you a different history.

**Save the table before turning it into a map.** You can revise an interpretation more easily when the original words sit beside it. With your own material, begin with two or three pages whose geography you understand.

## 2. Check what each location means
{: .step #step-2}

Compare each row with its passage. Correct an inaccurate quotation, a missing reference, or a role that overstates the evidence. Then ask AI to explain its unsettled decisions.

{% include prompt.html id="mapping-check" %}

Use these examples to judge the reply:

| Source wording | Prepared reading | Mapping decision |
|---|---|---|
| L1: “Tomorrow I hope to go on to Las Vegas, New Mexico” | Planned travel, explicitly in New Mexico | Use the New Mexico city; keep it separate from completed travel. |
| L2: “I have never been to Paris” | Explicitly not visited | Keep the reference, visibly labeled as not visited. |
| L3: “Your last letter says only Springfield” | Recipient's location is unresolved | Keep it in the list without a point. |
| L3: “I may return there next month” | “There” probably refers to Santa Fe | Mark the link as an interpretation requiring review; leave it unlocated in the prepared map. |

Decide which place a reference means before you ask where it is. A coordinate does not settle a place's identity, and the next step shows how easily one can be attached to the wrong place.

<div class="keypoint" markdown="1">
Keep unresolved references in the collection with their reasons. Leave their coordinates blank until you have evidence for a location.
</div>

## 3. Ask for coordinates, then check them
{: .step #step-3}

Open a new chat and send this request on its own, without the letters.

{% include prompt.html id="mapping-coordinates" %}

Place names often reach a map this way: a column copied from notes or a spreadsheet, with the documents left behind. Check three things in the reply before you look at anything else.

- **Which Las Vegas did it choose?** The letter says New Mexico; the list doesn't. Las Vegas, Nevada, is 895 km to the west, and a point there would look reasonable on a map of the Southwest.
- **What happened to Springfield?** Dozens of places share the name, and L3 asks which one. See whether the reply picked one, and whether it said so.
- **How many decimal places?** Four decimal places locate a point to within about 11 meters, and six to about 10 centimeters. For a city named in a letter, two decimal places (about a kilometer) are already finer than the source; the point stands for the whole city.

Compare your table with a neighbor's, or ask for the same table again. Note whether the same city gets the same numbers.

The tool did what the list asked. A bare name gives it no way to choose among places that share one, so expect the best-known candidate. **The numbers arrive without a record you can open**, which means a plausible coordinate and a checked one look the same. Ask where they came from.

{% include prompt.html id="mapping-coordinates-source" %}

Open two of the links. Does each one lead to a record for the place named, with coordinates close to the ones in the table? A link that fails, or that leads somewhere else, tells you the coordinates had no source behind them. A link that works lets you check the choice; you still have to decide whether it was the right place.

### Take the location from a gazetteer

A gazetteer is an index of places, each with an identifier, its names, and coordinates. A record ID in your table lets anyone see which place you meant and where its point came from. Return to the chat with your letters and checked table, and send this.

{% include prompt.html id="mapping-gazetteer" %}

Then do one lookup yourself. Search [GeoNames](https://www.geonames.org/) or [Wikidata](https://www.wikidata.org/) for **Las Vegas**, choose the record that matches the letter's “Las Vegas, New Mexico,” and copy its ID and coordinates into your table. Round them to the precision you recorded. Search for a bare **Santa Fe** as well: when we checked on 29 October 2026, GeoNames and Wikidata both listed the city in Argentina first.

| Reference | Gazetteer record | Coordinates | Precision | What decides it |
|---|---|---|---|---|
| L1: “Las Vegas, New Mexico” | GeoNames 5475433 | 35.59, −105.22 | Settlement | The letter names the state. |
| L2: “Paris, France” | GeoNames 2988507 | 48.85, 2.35 | Settlement | The letter names the country. |
| L3: “Springfield” | None chosen | Blank | Unknown | The writer asks which state; the letters cannot decide. |

These lookups were checked in GeoNames on 29 October 2026, and the prepared map in step 4 uses them. Use AI for the part it can check against the text in front of it: quoting the words that decide a place and suggesting spellings to search. Take the coordinates from the record. With your own sources, older names need a gazetteer that records them. The [World Historical Gazetteer](https://whgazetteer.org/) lists names with the periods they were in use, and [Pleiades](https://pleiades.stoa.org/) covers the ancient world. A modern gazetteer places a historical name where that name is used today, which may not be where your source meant.

<div class="keypoint" markdown="1">
Copy coordinates from a gazetteer record and keep its ID in the row. Round them to the precision your source supports, and note the words that decided which place it is.
</div>

## 4. Explore the text through a map
{: .step #step-4}

Open the [prepared research map]({{ site.baseurl }}/assets/mapping-with-ai/research-map.html). It uses a reviewed teaching table so everyone can reach this part even if their chat produced a different format. Each located reference names the GeoNames record for its point. Choose a reference in the list to open its source passage. References to the same city share a point; the list preserves each reference separately.

Try the relationship filter. First show completed travel, then planned travel, then all references. Search for **Paris**. Finally, choose **Unlocated only** and read what could not be placed. The result count includes list entries that have no marker.

**What changes when you separate travel from other kinds of geographic attention?** Paris belongs to the writer's world through images rather than a visit. An unresolved Springfield still belongs to the correspondence. A map of confirmed journeys alone would conceal both relationships.

Use these questions with your own collection:

- Which references would you want to read together, and what filter would help you find them?
- Are repeated mentions evidence of importance, or a consequence of which letters survive?
- What would a map of places mentioned reveal that a route map would obscure?

Ask for a next step grounded in the checked table.

{% include prompt.html id="mapping-research-question" %}

No routes are drawn in this example. A line would add a claim about a connection or movement. Add one only when you can explain what it represents and which passage supports it.

## 5. Turn monument photographs into a collection
{: .step #step-5}

Open the [prepared monument map]({{ site.baseurl }}/assets/mapping-with-ai/monuments-map.html). Select a monument to see its photographs and source link. Filter between local and national commemoration. There are two sites, with two photographs attached to the national memorial: a photograph count and a monument count give different answers.

Imagine your collection contains 300 photographs across 80 monuments. **Begin with one record per monument and a separate record for each photograph.** Link photographs to their monument using an ID. Visitors can then see an overview, a detail, and an inscription together without placing three supposed monuments on the map.

For the presenter demonstration, open the DC War Memorial photograph from its card and provide it to an AI tool that accepts images. Use the request below. If image input is unavailable, use the caption and source page to discuss which fields would remain unknown.

{% include prompt.html id="mapping-photo" %}

The overview photograph shows the memorial's form but cannot support a complete transcription of the names around its base. The NPS page supplies historical context. Keep those kinds of evidence distinguishable: what is visible, what a source states, and what you infer.

Compare the public questions with the research questions from step 4. A visitor might ask, “Which memorial commemorates a local community?” or “Where can I see another photograph?” Choose a card and check whether the interface helps answer both. These two sites illustrate browsing; they cannot establish a national pattern of commemoration.

<div class="keypoint" markdown="1">
Give every photograph a monument ID, a credit, and a source. Check image reuse separately from the accuracy of its caption.
</div>

## 6. Ask for an interface change and test it
{: .step #step-6}

Use the monument map's **Download data** button to save its collection, or take `monuments.json` from the kit. Describe one improvement in your own words. The request below is a presenter demonstration; the prepared map remains available while the tool works.

{% include prompt.html id="mapping-interface" %}

If your tool produces a downloadable HTML file or a preview, open it and test it. Otherwise, save its proposed interface description and use the prepared map to decide what you would change. Code generation may need another attempt; you can keep working with the reviewed collection while that happens.

Test the result with specific actions:

1. Select **Local**. Only the DC War Memorial should remain in this collection.
2. Select **National**. The World War I Memorial should show both photographs under one site.
3. Search for a phrase absent from the collection. The interface should explain that no records match.
4. Open a source link and compare the site's name and description. Check that image credits remain visible.
5. Narrow the window and try the controls with the keyboard. The list should provide a way to reach information without clicking a marker.

Then request a change that would serve your audience: larger photographs, a dedication-date filter with an “unknown” option, or a way to read inscriptions alongside images. **You can direct the interface by explaining what someone needs to do.** Ask the tool to preserve data and credits while making that change, and repeat the relevant checks.

To continue with your own collection, make a pilot with five sites or three texts. Save the checked data, source files, map, and unresolved location decisions. Sharing it online is a separate step from opening it in your browser; the downloadable map is a starting point for that conversation.

## What to take with you
{: .step #takeaways}

<div class="takeaways" markdown="1">
Use these habits when you map your own material:

- **Start with a question.** Decide which relationship or visitor action the map should help you explore.
- **Keep the passage or photograph attached.** A point should lead back to its evidence.
- **Separate mention, movement, and inference.** Each makes a different claim about a place.
- **Take coordinates from a gazetteer.** Keep the record ID and round to what the source supports, so anyone can see which place you meant.
- **Keep unknowns visible.** A missing location should remain available in the list.
- **Describe a useful action, then test it.** You can guide an interface through ordinary language and check what it does.
</div>

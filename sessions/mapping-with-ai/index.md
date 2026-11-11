---
title: Mapping with AI
presenter: Fred Gibbs
layout: base
position: 5
date: 2026-11-11
time: "12:00–12:50"
location: History Commons (MVH 1104)
kicker: Session 5 · November 11, 2026
summary: "See how AI turns tables, photographs and census pages into maps, and why the work that matters happens in the data before anything is drawn."
points:
  - title: Ask for a map and see what comes back
    text: Compare a generated picture of a map with a map drawn from data, and find out where each one's locations came from.
  - title: Give AI a table it can map
    text: Turn a list of places, a folder of photographs and a page of census figures into tables with sources and locations you can check.
  - title: Match the map to the evidence
    text: Join figures to the right boundaries, choose rates over counts, and make a figure fit for publication.
note: "A demonstration: bring a laptop if you want to try the prompts. No coding or mapping experience needed."
thumbnail: "/assets/images/hondius-mercator-1613.jpg"
header-image: "/assets/images/hondius-mercator-1613.jpg"
header-tier: section
header-filter: etching
header-position: center right
header-opacity: 0.18
header-title: Mapping with AI
header-subtitle: "AI can draw a map in seconds. Make sure you can see how it got there: which place each name means, where every location comes from and which boundaries your numbers belong to."
header-caption: "Gerard Mercator and Jodocus Hondius, engraved by an anonymous printmaker for Mercator's <i>Atlas</i> (Amsterdam: Jodocus Hondius II, 1613). Rijksmuseum, Amsterdam, CC0."
tags: [mapping, research, census, data]
workshop_mode: true
---

{% comment %}
Authoring references: SESSION-STYLE.md.
Each step: the source, the prompts, what came back, what to check.
Recorded replies go in _data/demos.yml under the mapping-* ids; the page
shows a red slot for any that are still empty. Map screenshots go in
sessions/mapping-with-ai/images/ and replace the matching demo include.
{% endcomment %}

{% include nav/scrollspy-toc.html %}

Work down this page during the session or return to it later. Each step shows a source, the prompts sent to an AI tool, and the map that came back, so you can repeat the process with your own material.
{: .lead}

<div class="rule" markdown="1">
**Make every step behind a map visible: where each location and number came from, and who made each choice about how to draw them.**
</div>

## Introduction
{: .step #introduction}

### Why the data is the place to start

Ask an AI tool for a map and you will get one in seconds. It may even look right. The trouble is that nothing about its appearance tells you whether the towns are where it put them, or whether the shading means what the legend says.

Most of the work in a map that holds up happens before anything is drawn. Someone decides what each row stands for, which place a name refers to, where its coordinates came from and which boundary a number belongs to. AI can help with every one of those decisions, and it can write the code that draws the map, but **it makes those decisions silently unless you make them first.** This session works through five kinds of material, from a list of names to a page of a 1910 census report, and shows where the decisions sit in each.

### What a web map is made of

If you haven't made a map before, these are the parts. Every map on this page is built from them, and each one is a place where someone makes a decision.

{% include images/figure.html
  image-width="100%"
  caption="The ghost-town map from step 2, taken apart. Only the middle layer came from the data."
  alt-text="Three panels of New Mexico at the same scale: a street-style base map alone, colored points alone on a white background, and the two combined."
  image-path="/sessions/mapping-with-ai/images/web-map-layers.jpg"
%}

- **A base map and a data layer.** A web map is layers stacked in a browser. The bottom layer, the base map, shows roads, rivers, borders and place names. Someone else drew it, and it arrives as small square images called tiles; the maps here use OpenStreetMap's. Your data sits on top. Only that layer is yours, and only it can be checked against a source. Some maps have no base map at all: in the county maps of step 4, the county shapes are the map.
- **A location is a pair of numbers.** A point is placed by its latitude, how far north or south (about 35 in central New Mexico), and its longitude, how far east or west (about −106, negative because it is west of Greenwich). Maps use them as decimal degrees: Albuquerque is 35.0845, −106.6511. Some files put latitude first and some put longitude first, and a swapped pair is a common reason a point lands in the wrong place or disappears. The numbers have to come from somewhere: a gazetteer (step 2), a phone's GPS (step 3) or a geocoding service, which looks up an address and returns coordinates. A model's memory is not a source (step 1).
- **Every feature is a shape made of coordinates.** Each thing on the data layer is drawn as one of three kinds of shape, and each shape is nothing more than coordinate pairs. A **point** is a single pair: a town, a photograph. A **line** is a series of pairs joined in order: a road, a river, a railroad. A **polygon** is a series that closes back on its first pair, tracing the border of an area: a county, a state, a lake. A detailed county border can take hundreds or thousands of pairs. A point fits in a table as two columns, which is why steps 2, 3 and 5 start from tables. A polygon doesn't fit in a table cell, so areas come in a **boundary file**: one shape per row, with a few columns that say what each shape is, such as the county's name and ID (step 4). You will meet three formats: CSV for tables, GeoJSON for shapes on the web, and the shapefile, an older format for shapes that is really several files shared together as a ZIP.
- **A join connects a table to shapes.** Census figures arrive as a table with no shapes, and a boundary file has shapes but not your figures. A join matches each row to its shape through an ID both files share, such as a county's FIPS code. A row that fails to match simply goes missing from the map unless you ask for a list (step 4).
- **Shading and classes.** A choropleth shades each area by a value. The values are grouped into classes, the bands in the legend, and where the breaks fall decides what looks high or low. Raw counts mostly show where people live, so shade by a rate (step 4).
- **Projection.** The earth is round and a screen is flat, so every map stretches something; the projection is the rule for how. A map drawn on tiles has to use the tiles' projection, Web Mercator, which keeps streets and coastlines looking right but makes places look larger the farther they are from the equator. That is fine for the point maps in steps 1, 2, 3 and 5. A map that draws its own shapes without tiles can use any projection. The county maps in steps 4 and 6 have no tiles, and each run chose an Albers equal-area conic projection, the usual choice for maps of the United States, because it keeps every county's area true. That matters when color fills the area.
- **The map is a file.** A web map from an AI tool is usually a single HTML page that uses a mapping library, often Leaflet, to fetch the tiles and draw your data. You open it in a browser, and nothing needs installing. A figure for print is a different product: an image made by a script, with no tiles (step 6). Desktop mapping software (GIS) such as [QGIS](https://qgis.org/) does all of this in one program, with more to learn.

When you ask AI for a map without saying how to handle these, it decides them for you. The steps show where.

### About the examples

All the sources are real and public: a Wikipedia list, photographs taken on a phone, current Census Bureau data and the 1910 census report for New Mexico, which is in the public domain. The replies and maps on this page are recorded from actual runs on 11 November 2026, labeled with the tool and date. Notes under each reply say what was attached and what was cut. Models change, so yours may differ. When a step shows a recorded map, the prompts above it are the ones that produced it.

**In most steps, the tool in these runs could read and write files, but it could not run code or search the web.** The exceptions are noted under each reply: step 1's picture came from Gemini, the runs in steps 3 and 6 could also run code, and one reply in step 5 was run with no tools at all. That was how we recorded them, and it shows in the replies. Several say they haven't opened the map they made, and some name details they couldn't check, such as web addresses written from memory. That is the tool being straight about what it couldn't do. We opened every map ourselves, and the screenshots show what we saw.

### Setting up to follow along

You can follow most of this page in an ordinary AI chat in your browser, such as ChatGPT, Claude or Gemini. A few things are worth knowing first.

- **Step 1's picture needs a chat that makes images.** ChatGPT and Gemini do; Claude doesn't. Every other step works in any of them.
- **Two prompts are marked “Needs a tool that runs code”** (steps 2 and 3). Most chat tools can run code on files you upload, but some plans or settings turn it off. If a reply says it can't run code, it will usually hand you a script to run yourself, or, as in step 2, do the work by reading, which is slower and needs more checking. Look for a setting called something like code execution or analysis, or use a coding assistant (Claude Code, GitHub Copilot or Cursor) opened on a folder of your files.
- **Getting a map out of a chat.** Many prompts ask for “a single HTML file”. Depending on the tool, it arrives as a preview beside the chat, a file to download, or code in the reply. If it is code, copy it into a plain text file, save it with a name ending in `.html` and double-click it to open it in your browser. If a preview stays blank, download the file and open it in your browser instead: previews often block the map tiles and boundaries that a map loads from the internet.
- **What “attach” means.** Many prompts begin “I have attached…”. Attaching a file uploads it with your message, so the AI can read it. First download the file from this page to your computer: a chat can't open a link to it for you. Then, in the chat, click the paperclip or **+** button beside the message box and choose the file, or drag the file onto the chat window. Paste the prompt and send both together. Chat tools take files or a ZIP, not a folder, so where a step uses a folder, attach it as a ZIP. In a coding assistant, put the files in the folder it is working in instead.
- **New chat or same chat.** Where it matters, the note above a prompt says whether to start a new chat or continue the last one. A new chat keeps earlier replies from steering the next.

### Data for this session

Every file attached to a prompt on this page is in **[one ZIP]({{ '/assets/mapping-with-ai/mapping-with-ai-data.zip' | relative_url }}) (6.5 MB)**, with a README giving each file's source, so you can repeat any step without first repeating the ones before it. The one file not in it is the Census Bureau's [county boundary file](https://www2.census.gov/geo/tiger/GENZ2023/shp/cb_2023_us_county_500k.zip) (12 MB), used in steps 4 and 6. Each step also links the files it uses, and the maps the runs made are linked under each screenshot.

<details class="more" markdown="1">
<summary>The files one at a time</summary>

| Step | File | What it is |
|---|---|---|
| 2 | [nm-ghost-towns-wikipedia-2026-11-11.tsv]({{ '/assets/mapping-with-ai/data/nm-ghost-towns-wikipedia-2026-11-11.tsv' | relative_url }}) | The Wikipedia table as copied on 11 November 2026, saved as tab-separated text (CC BY-SA 4.0) |
| 2 | [nm-ghost-towns.csv]({{ '/assets/mapping-with-ai/data/nm-ghost-towns.csv' | relative_url }}) | That table as a CSV, from the first prompt |
| 2 | [gnis-nm-populated-places.txt]({{ '/assets/mapping-with-ai/data/gnis-nm-populated-places.txt' | relative_url }}) | GNIS's 1,601 New Mexico populated places; the [full state file](https://prd-tnm.s3.amazonaws.com/StagedProducts/GeographicNames/DomesticNames/DomesticNames_NM_Text.zip) has every feature type |
| 2 | [nm-ghost-towns-gnis.csv]({{ '/assets/mapping-with-ai/data/nm-ghost-towns-gnis.csv' | relative_url }}) | The CSV with GNIS matches, from the second prompt |
| 3 | [marrakech-cats-sample.zip]({{ '/assets/mapping-with-ai/data/marrakech-cats-sample.zip' | relative_url }}) | 20 phone photos by Jonathan Seyfried; all 208 are in his [repository](https://github.com/jeseyfried/cats-of-marrakech/tree/main/assets/images/marrakech-cats) |
| 4, 6 | [nm-county-population-2020-2024.csv]({{ '/assets/mapping-with-ai/data/nm-county-population-2020-2024.csv' | relative_url }}) | New Mexico's rows from the Census Bureau's 2024 county estimates |
| 4 | [us-county-population-2020-2024.csv]({{ '/assets/mapping-with-ai/data/us-county-population-2020-2024.csv' | relative_url }}) | Every county, 2020 and 2024 only; the [full estimates file](https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/counties/totals/co-est2024-alldata.csv) has every year |
| 4, 6 | [cb_2023_us_county_500k.zip](https://www2.census.gov/geo/tiger/GENZ2023/shp/cb_2023_us_county_500k.zip) | Census Bureau county boundaries (12 MB, from the Census Bureau) |
| 5 | [census-1910-nm-cities-table.png]({{ '/assets/mapping-with-ai/data/census-1910-nm-cities-table.png' | relative_url }}) | The table on page 158 of the 1910 report |
| 5 | [nm-cities-1860-1910.csv]({{ '/assets/mapping-with-ai/data/nm-cities-1860-1910.csv' | relative_url }}) | Its transcription, checked against the scan |
| 5 | [nm-city-coordinates-gnis.csv]({{ '/assets/mapping-with-ai/data/nm-city-coordinates-gnis.csv' | relative_url }}) | GNIS coordinates for the four cities |
| 5 | [nm-counties-1900-1910.txt]({{ '/assets/mapping-with-ai/data/nm-counties-1900-1910.txt' | relative_url }}) | County names in the 1900 and 1910 censuses |

Files that came out of a prompt are the recorded replies' files, checked as each step describes.

</details>

## 1. Ask for a map and see what comes back
{: .step #step-1}

Send this to a chat tool that can make images, such as ChatGPT or Gemini.

{% include prompt.html id="mapping-hook-picture" %}

{% include images/figure.html
  image-width="60%"
  caption="The picture that came back, from Gemini on 11 November 2026."
  alt-text="Engraving-style picture of a map titled Nuevo México: Mapa histórico de los pueblos abandonados y rutas antiguas, with mountains, trails, wagons, a compass rose and labeled towns including Shakespeare, Chloride, Kelly, Golden and Pinos Altos."
  image-path="/sessions/mapping-with-ai/images/run-hook-picture.jpg"
%}

Look at the town names and where they sit. Most are real New Mexico ghost towns, but Shakespeare and Steins, both near the Arizona line in the southwest, appear at the top and on the east edge, and Dawson and Colfax, in the northeast, appear in the middle and the southeast. Golden, Kelly and Pinos Altos each appear twice, and one label, Fasnflur, is not a place at all. An image generator draws a picture that resembles maps it has seen. Nothing in the picture can be checked, corrected or updated, because there is no data behind it.

Now ask a chat tool that writes code for the same thing.

{% include prompt.html id="mapping-hook-code" %}

{% include demo.html id="mapping-hook-code" %}

{% include images/figure.html
  image-width="100%"
  caption="The map that came back: 40 towns, each placed at coordinates the tool supplied."
  alt-text="Web map of New Mexico with 40 labeled orange points and a sidebar listing the towns alphabetically with their counties."
  image-path="/sessions/mapping-with-ai/images/run-hook-code-map.jpg"
%}

[Open the map this run made]({{ '/assets/mapping-with-ai/maps/step-1-code-map.html' | relative_url }}){: target="_blank" rel="noopener"}, exactly as the tool wrote it.

This one is a real map. The state outline comes from map tiles, the points sit at coordinates, and you can click them. It looks far more trustworthy. This run admitted, unprompted, that it typed the coordinates from memory. Not every run will say so, so ask.

{% include prompt.html id="mapping-hook-source" %}

{% include demo.html id="mapping-hook-source" %}

**The coordinates came from the same place as the picture: the model's memory.** The code map has the same problem as the image, now hidden behind a display that looks authoritative. Its confidence ratings are also from memory: “fairly sure” describes how well the model recalls a place, not a check. The list itself was a judgment call. It chose 40 towns, including Madrid and Chloride, which still have residents. Wikipedia's list, in the next step, has 66.

None of that is malfunction. You asked for a map without saying which towns, from which source, located how. The rest of this page supplies those answers before asking for anything to be drawn.

<div class="keypoint" markdown="1">
After any AI-made map, ask: “Where did each location come from? Mark any you are unsure of.” If it can't name a source for a point, treat the point as a guess.
</div>

## 2. Map a list of places from a table
{: .step #step-2}

Start with a list someone else has compiled and sourced. Wikipedia's [List of ghost towns in New Mexico](https://en.wikipedia.org/wiki/List_of_ghost_towns_in_New_Mexico) is a table of 66 towns with their county, the years settled and abandoned, and their current status. Only three rows give coordinates. That gap is common in historical lists, and filling it is the main job here.

### Turn the table into data

Open the [List of ghost towns in New Mexico](https://en.wikipedia.org/wiki/List_of_ghost_towns_in_New_Mexico) on Wikipedia. Select the whole table, from the header row down to the last town, copy it and paste it into a new chat. Then paste this prompt below it and send.

The list changes as people edit it. To start from the same table as the run below, use [our copy from 11 November 2026]({{ '/assets/mapping-with-ai/data/nm-ghost-towns-wikipedia-2026-11-11.tsv' | relative_url }}) instead, which is also in the session ZIP: open it in a text editor or spreadsheet, copy everything and paste that.

{% include prompt.html id="mapping-ghost-table" %}

{% include demo.html id="mapping-ghost-table" %}

Check the row count against the page, and spot-check three rows. Here the count was right, and the reply listed the cells it had to make decisions about: dashes treated as blanks, two years in one cell, a county cell that also names a Texas county. Those are the rows to read first. Keep the Wikipedia page's URL and the date you copied it with the file; the list changes.

### Take locations from a gazetteer

A gazetteer is an index of places with an identifier, names and coordinates for each one. For the United States, the [Geographic Names Information System](https://www.usgs.gov/us-board-on-geographic-names/domestic-names) (GNIS) is the official one, and it keeps many abandoned settlements, usually with “(historical)” after the name. Its [New Mexico file](https://prd-tnm.s3.amazonaws.com/StagedProducts/GeographicNames/DomesticNames/DomesticNames_NM_Text.zip) lists every named feature in the state, from towns to springs; other states are on the [GNIS download page](https://www.usgs.gov/us-board-on-geographic-names/download-gnis-data). This run was sent just the [1,601 populated places]({{ '/assets/mapping-with-ai/data/gnis-nm-populated-places.txt' | relative_url }}) with the [ghost-town CSV]({{ '/assets/mapping-with-ai/data/nm-ghost-towns.csv' | relative_url }}). Attach both and send this.

{% include prompt.html id="mapping-ghost-gnis" %}

{% include demo.html id="mapping-ghost-gnis" %}

Read the rows it flagged before you read anything else. Ghost towns are hard to match for predictable reasons, and this run hit most of them. Clairmont is spelled Claremont in GNIS. Santa Barbara matched through its other name, Hatch, which is the modern village rather than the 1850s settlement. Bramlett's only record is filed under a different county, though the tool thought its coordinates sat in the right one. Alamocita has no record at all; it is now under Elephant Butte Reservoir. **The county column is your check:** a match in the wrong county is the wrong place, however close the name. Each flagged row is a decision for you, not the tool.

### Ask for the map

Attach the matched CSV, [nm-ghost-towns-gnis.csv]({{ '/assets/mapping-with-ai/data/nm-ghost-towns-gnis.csv' | relative_url }}) in this run, and send this.

{% include prompt.html id="mapping-ghost-map" %}

{% include demo.html id="mapping-ghost-map" %}

The file it described did not work. Opened in a browser, the map was blank and the page's code spilled out as text.

{% include images/figure.html
  image-width="70%"
  caption="The first file, opened in Chrome."
  alt-text="A web page titled New Mexico Ghost Towns with an empty map area and JavaScript code printed as text below an empty table."
  image-path="/sessions/mapping-with-ai/images/run-ghost-map-broken.jpg"
%}

Describe what you see and ask for a fix. You don't need to know the cause.

{% include prompt.html id="mapping-ghost-map-fix" %}

{% include demo.html id="mapping-ghost-map-fix" %}

{% include images/figure.html
  image-width="100%"
  caption="The fixed map: 46 towns placed from GNIS records, with the 20 unlocated towns listed below it."
  alt-text="Web map of New Mexico with 46 points colored by status, a legend, and the start of a table of towns without coordinates."
  image-path="/sessions/mapping-with-ai/images/run-ghost-map.jpg"
%}

[Open the fixed map]({{ '/assets/mapping-with-ai/maps/step-2-ghost-town-map.html' | relative_url }}){: target="_blank" rel="noopener"} and click the points.

Click a few points and compare the popup with the row in your file. Look at the list of unlocated towns as well. They are part of the collection, and a map that dropped them would quietly claim the list was complete. Notice the gray points too: 20 of the mapped towns have no status because Wikipedia's table gives none, and the legend says so rather than guessing.

<div class="keypoint" markdown="1">
Copy coordinates from a gazetteer record and keep its ID in the row. Have AI match names and flag doubts, then decide the flagged rows yourself.
</div>

## 3. Map photographs by their location data
{: .step #step-3}

A photograph can carry its own coordinates. Phones with location services on write the latitude and longitude into each image file, along with the date and time. That information, the file's EXIF data, is the location. Nobody has to infer it.

In March 2026, [Jonathan Seyfried](https://jonathanseyfried.net/), a PhD candidate in history at UNM, photographed street cats in the Marrakech medina on his phone. To try this step, download a [sample of 20 of his photos]({{ '/assets/mapping-with-ai/data/marrakech-cats-sample.zip' | relative_url }}) (6 MB) and attach the ZIP, or attach a ZIP of your own phone photos. In a coding assistant, unzip it into your folder instead. The run below used the same 20 photos, so your results should match it. All 208 are mapped on Jonathan's own site, [Cats of Marrakech](https://jeseyfried.github.io/cats-of-marrakech/), and the photos are in his [repository](https://github.com/jeseyfried/cats-of-marrakech/tree/main/assets/images/marrakech-cats).

Attach your ZIP and send this.

{% include prompt.html id="mapping-photos-exif" %}

{% include demo.html id="mapping-photos-exif" %}

The reply gives a count, describes both files and explains the one oddity: the last photo's filename is an hour behind its recorded time. A phone stores each photo's local time along with its time zone, written as hours ahead of Greenwich time (UTC), and the last photo, taken on 22 March, says +01:00 where the others say +00:00. The tool's explanation, that Morocco moves its clocks back an hour during Ramadan, is plausible, and it is exactly the kind of claim to check before you use photo times as evidence.

{% include images/figure.html
  image-width="100%"
  caption="The map the run made: 20 photos, with one popup open. Photos by Jonathan Seyfried."
  alt-text="Street map of the Marrakech medina with orange points, and a popup showing two cats asleep in a cardboard box with the filename and the time 2026-03-19 11:34:53 +00:00."
  image-path="/sessions/mapping-with-ai/images/run-photos-map.jpg"
%}

[Open the map]({{ '/assets/mapping-with-ai/maps/step-3-photo-map.html' | relative_url }}){: target="_blank" rel="noopener"}. It is 400 KB because the photos are inside it. You can also download the [CSV]({{ '/assets/mapping-with-ai/maps/marrakech-cats-locations.csv' | relative_url }}).

**Once the locations are clear, the map is the easy part.** One request turned a folder of photos into a working map with a popup for each, in under a minute. Not long ago, someone who didn't code had to learn to pull coordinates out of image files, set up a mapping library and build a page around it, and that was often where a project like this stopped. A quick map now costs almost nothing, so spend your effort on what it rests on: the CSV of photos, coordinates and dates that you can open, correct and reuse. The map is one view of it.

Three things to check with your own photographs:

- **Whether the location survived.** Messaging apps, social media and some export settings remove location data. Ask the tool to list any images it found without coordinates rather than skipping them.
- **How precise it is.** Phone GPS can be off by several meters, and much more indoors or between tall buildings. For a street cat that hardly matters. For field photographs of a building or a grave marker, check the pins before treating them as evidence.
- **What the coordinates record.** They are where the camera was, not where the subject was. A photo of a mountain taken from twenty miles away is mapped at the photographer's feet.

Reading coordinates from a file is different from asking AI to work out where a photo was taken by looking at it. A model will offer a confident guess from architecture, plants or signs. Treat that as a lead to check against something you can cite, never as a location.

<div class="keypoint" markdown="1">
When your locations are clear, a quick map is one request away; it is no longer the hurdle. Ask for the coordinates in a separate data file too, with a list of every image that had none, so you can check, fix and reuse them.
</div>

## 4. Join county figures to county boundaries
{: .step #step-4}

The Census Bureau has been making county maps for well over a century. Its report on the 1910 census of New Mexico shades each county by its inhabitants per square mile, drawn and shaded by hand.

{% include images/figure.html
  image-width="100%"
  caption="“Density of population of New Mexico, by counties: 1910.” *Thirteenth Census of the United States, Volume 3: Population* (1913), page 162. U.S. Census Bureau, public domain. [Scan via IPUMS](https://usa.ipums.org/usa/resources/voliii/pubdocs/1910/Vol3/36894832v3ch2.pdf)."
  alt-text="Two choropleth maps of New Mexico's 26 counties in 1910, shaded by inhabitants per square mile for total and rural population."
  image-path="/sessions/mapping-with-ai/images/census-1910-nm-density-map.png"
%}

This step makes the same kind of map, a choropleth, from today's figures. Steps 2 and 3 mapped points; a county is an area, so it needs a shape from a boundary file. Census figures and county shapes come in different files, so a county map starts with the join described in the introduction, and most of the decisions in this step are about it.

### Two files: the figures and the shapes

**The table** has one row per county and no shapes. These are three rows of the Census Bureau's 2024 county estimates, the [file this run used]({{ '/assets/mapping-with-ai/data/nm-county-population-2020-2024.csv' | relative_url }}), showing four of its columns:

| STATE | COUNTY | CTYNAME | POPESTIMATE2024 |
|---|---|---|---|
| 35 | 001 | Bernalillo County | 671747 |
| 35 | 013 | Doña Ana County | 229366 |
| 35 | 031 | McKinley County | 68945 |

**The boundary file** also has one row per county, but each row carries a shape. These are the same three counties in the Census Bureau's [county boundary file](https://www2.census.gov/geo/tiger/GENZ2023/shp/cb_2023_us_county_500k.zip), which covers the whole country:

| GEOID | NAME | ALAND | geometry |
|---|---|---|---|
| 35001 | Bernalillo | 3007611376 | an outline of 132 coordinate pairs |
| 35013 | Doña Ana | 9863137493 | an outline of 194 coordinate pairs |
| 35031 | McKinley | 14118189399 | an outline of 229 coordinate pairs |

The geometry column is the shape: latitude and longitude pairs traced around the border, ending where they began. This file is simplified for maps of the whole country, so Bernalillo's border takes 132 pairs; a detailed survey boundary can take thousands. The other columns describe each shape. ALAND is the county's land area in square meters, which a per-square-mile rate needs.

The boundary file comes as a **shapefile**, an older format that is still the most common for boundaries, and a shapefile is not one file. Unzip this one and you find seven. The `.shp` file holds the shapes, the `.dbf` file holds the columns, the `.shx` file is an index that connects the two, the `.prj` file says what coordinate system the numbers are in, and the `.cpg` file says how the text is encoded, which is what keeps the ñ in Doña Ana. The rest are documentation. The parts only work together, so keep them in one folder and attach the whole ZIP: a `.shp` on its own is a set of outlines with no names. GeoJSON, the other common format, puts shapes and columns in a single text file.

### Joining the table to the shapes

A join lines up two tables by a column they both have, called the **key**. For each row of the table, the tool looks for the shape with the same key and attaches that row's figures to it. Once every shape has its figure, the map can shade it.

The key has to match exactly, character for character, which is why names make poor keys. The table says “Doña Ana County”, the boundary file says “Doña Ana”, and other sources write “Dona Ana”. Thirty states have a Washington County. So every county has a code, the five-digit **FIPS code**: two digits for the state (35 is New Mexico) and three for the county. The boundary file has it ready as GEOID, 35013. The table splits it into STATE and COUNTY, so the join has to put 35 and 013 together first. Open either file in a spreadsheet and it may quietly turn 013 into 13, and then nothing matches.

**A failed join doesn't announce itself.** A row that finds no shape is simply missing from the map, and a shape that finds no row is left blank or dropped. That is why the prompt asks for both lists of failures before any map is drawn.

You have met joins already. Step 2 joined the ghost-town list to GNIS by name, because the list had no codes, and that is why every match needed checking. Step 5 meets a harder case: a county name that stands for different shapes in different censuses.

Once the figures are joined, the map shades each county by its value, as the 1910 map does by hand.

Download county population figures from the Census Bureau's [county population totals](https://www.census.gov/programs-surveys/popest/data/tables.html), or use any table you have with a county and a number. This run used [New Mexico's rows]({{ '/assets/mapping-with-ai/data/nm-county-population-2020-2024.csv' | relative_url }}) from the 2024 estimates. Attach your table and send this.

{% include prompt.html id="mapping-county-nm" %}

{% include demo.html id="mapping-county-nm" %}

{% include images/figure.html
  image-width="80%"
  caption="The New Mexico map, with its join check printed above it."
  alt-text="Choropleth of New Mexico's 33 counties in red and blue by percent population change, under a panel reporting 33 of 33 counties matched."
  image-path="/sessions/mapping-with-ai/images/run-county-nm-map.jpg"
%}

[Open the New Mexico map]({{ '/assets/mapping-with-ai/maps/step-4-nm-county-map.html' | relative_url }}){: target="_blank" rel="noopener"}. It fetches the county boundaries from the Census Bureau when it opens, which takes a few seconds.

Check the list of unmatched counties first. New Mexico has 33 counties; a choropleth with a blank county usually means a failed join, not missing data. Here all 33 matched, and the tool left out the statewide row without being told to. Note also the decision it reported about the measure: the table has two 2020 figures, an April 1 base and a July 1 estimate, and it chose July. The step 6 run made the same choice and says how much the other one would change.

### Rates, not counts

A map of raw population mostly shows where people live, and so does a map of almost any raw count: churches, newspapers, cases. **Shade by a rate** (per square mile, per thousand residents, percent change) so that large counties don't win by size. The 1910 map at the top of this step does exactly that: inhabitants per square mile, not inhabitants. Look at the classes the tool chose as well. The same figures split into different ranges can make a county look average or extreme. Ask what it chose and why, then decide.

### Change the scale and the base map changes

In the same chat, attach the [national table]({{ '/assets/mapping-with-ai/data/us-county-population-2020-2024.csv' | relative_url }}) and send this.

{% include prompt.html id="mapping-county-us" %}

{% include demo.html id="mapping-county-us" %}

At national scale the decisions change. A flat web map stretches the northern states and makes Alaska enormous, so national county maps use an equal-area projection with Alaska and Hawaii moved into insets. More than 3,000 counties also bring more failed matches. Connecticut replaced its counties with planning regions in 2022, so a boundary file and a data table from different years will not line up there. Ask for the unmatched list again.

Rather than type 3,144 rows into the page by hand, the tool made the page ask for the CSV when it opens. Its join check found exactly the failures the reply predicted: 91 boundaries in Puerto Rico and the island areas, which the estimates file does not cover.

{% include images/figure.html
  image-width="80%"
  caption="The join check on the national map."
  alt-text="A panel reporting 3,144 of 3,144 table rows matched and 91 unmatched boundaries, grouped by territory, with an explanation of the pattern."
  image-path="/sessions/mapping-with-ai/images/run-county-us-join.jpg"
%}

{% include images/figure.html
  image-width="100%"
  caption="The national map, on an equal-area projection with Alaska and Hawaii as insets."
  alt-text="Choropleth of all U.S. counties in red and blue by percent population change from 2020 to 2024, with Alaska and Hawaii inset at lower left."
  image-path="/sessions/mapping-with-ai/images/run-county-us-map.jpg"
%}

[Open the national map]({{ '/assets/mapping-with-ai/maps/step-4-us-county-map.html' | relative_url }}){: target="_blank" rel="noopener"}. Opened from this site, it finds the [national table]({{ '/assets/mapping-with-ai/maps/us-county-population-2020-2024.csv' | relative_url }}) beside it and loads it without asking; a copy saved to your computer asks you to choose the file. It also fetches more than 3,000 county boundaries from the Census Bureau, so give it half a minute. The join check comes first; the map is below it.

Compare the reply with the map's legend. The reply says values run “from about −20% (Garza County, TX) to over +30%”; the map, which computes from the file, says −28.36% to +34.42%. The tool had read 3,144 rows by eye and missed Loving County, Texas, the least populous county in the country. **Trust the numbers the code computed over the numbers the reply describes.**

<div class="keypoint" markdown="1">
Join counties on FIPS codes and ask for a list of rows that didn't match. Shade by a rate, and ask which classes and projection the tool chose before you accept them.
</div>

## 5. Extract historical census figures and map change
{: .step #step-5}

Historical population figures are often only available as scanned printed tables. The [1910 census report for New Mexico](https://usa.ipums.org/usa/resources/voliii/pubdocs/1910/Vol3/36894832v3ch2.pdf) (a 30 MB scan; other states are on the [IPUMS volume list](https://usa.ipums.org/usa/voliii/pubdocs/1910/pubvols1910.shtml)) can't be searched or copied as text: every figure is a picture of print. Turning it into a table is the step AI makes much faster.

### Transcribe a table from the scan

Page 158 compares the territory's four largest cities across every census in which each was counted.

{% include images/figure.html
  image-width="70%"
  caption="Population of cities, 1860–1910. *Thirteenth Census*, Volume 3 (1913), page 158. Public domain."
  alt-text="Scanned table listing the populations of Albuquerque, Raton, Roswell and Santa Fe at each census, with the increase over the preceding census."
  image-path="/sessions/mapping-with-ai/images/census-1910-nm-cities-table.png"
%}

Attach a screenshot of the table, or [download this one]({{ '/assets/mapping-with-ai/data/census-1910-nm-cities-table.png' | relative_url }}), and send this.

{% include prompt.html id="mapping-census-transcribe" %}

{% include demo.html id="mapping-census-transcribe" %}

Check every number against the scan; with a table this small, that takes two minutes. The report gives you a second check: it prints the change from each census to the next, so you can ask the tool to verify each population figure against the printed difference. A digit misread as another will usually break that arithmetic.

This run got every figure right, and its one doubt is worth reading. Albuquerque's 1910 percentage could be read as 70.7 or 76.7. The run saw a 150 dpi crop, but even at 400 dpi the scan is ambiguous. The tool entered 76.7 because the arithmetic gives 76.7. The prompt told it not to calculate or correct anything, so it bent that rule, but **it said that it had used the arithmetic to decide**, so you know which cell to check. The report's own text gives a third check: “Roswell shows the highest rate of increase during the last decade, namely, 201.2 per cent, and Raton the lowest, 28.2 per cent, while Santa Fe shows a decrease of 9.5 per cent.”

Then map it. Four cities need four coordinates; take them from GNIS, as in step 2. This run was sent the [checked transcription]({{ '/assets/mapping-with-ai/data/nm-cities-1860-1910.csv' | relative_url }}) and the [four GNIS records]({{ '/assets/mapping-with-ai/data/nm-city-coordinates-gnis.csv' | relative_url }}).

{% include prompt.html id="mapping-census-cities-map" %}

{% include demo.html id="mapping-census-cities-map" %}

{% include images/figure.html
  image-width="100%"
  caption="The city map at 1910, with a control to step back through earlier censuses."
  alt-text="Web map of New Mexico with orange circles sized by 1910 population at Albuquerque, Santa Fe, Raton and Roswell, a year slider and a circle-size legend."
  image-path="/sessions/mapping-with-ai/images/run-census-cities-map.jpg"
%}

[Open the city map]({{ '/assets/mapping-with-ai/maps/step-5-city-map.html' | relative_url }}){: target="_blank" rel="noopener"} and step through the census years.

The map makes visible what the table only records: the capital was shrinking while Albuquerque, Raton and Roswell grew. The same process scales to the report's Table 1, which lists every precinct, town and village for 1890, 1900 and 1910. It runs to many pages, so extract one county first and check it before attempting the rest.

### Notice when the counties changed

County figures over time raise a problem that town figures don't. On page 159, the report explains why it could compare 1900 and 1910 for only six of its 26 counties.

{% include images/figure.html
  image-width="60%"
  caption="“The following territorial changes have been made in the counties of New Mexico since 1900.” *Thirteenth Census*, Volume 3 (1913), page 159. Public domain."
  alt-text="Scanned paragraph listing eight New Mexico counties formed from parts of others between 1901 and 1909."
  image-path="/sessions/mapping-with-ai/images/census-1910-nm-county-changes.png"
%}

Eight new counties were carved out of others between 1901 and 1909. One of them, Leonard Wood, was renamed Guadalupe in 1905, and the report calls the earlier county “old Guadalupe”, which had a different shape. **A county name is not a stable identifier across censuses.** Join 1900 figures to 1910 shapes by name and Guadalupe gets the wrong population; join either to today's 33 counties and the map is wrong in a way no one will notice from looking at it.

The Census Bureau's answer was to combine counties into units that stayed the same across both censuses. Its map of growth draws those combinations with white dashed lines.

{% include images/figure.html
  image-width="100%"
  caption="“Per cent of increase of population of New Mexico, by counties: 1900–1910.” *Thirteenth Census*, Volume 3 (1913), page 161. Public domain."
  alt-text="Two choropleth maps of New Mexico counties shaded by percent increase in population from 1900 to 1910, with dashed white lines grouping counties formed after 1900."
  image-path="/sessions/mapping-with-ai/images/census-1910-nm-increase-map.png"
%}

You can do the same, or use boundaries drawn for each census year. The Newberry Library's [Atlas of Historical County Boundaries](https://digital.newberry.org/ahcb/) has free boundary files for every state with the dates each shape was in force, and [NHGIS](https://www.nhgis.org/) (free with an account) pairs historical census tables with matching boundaries. Ask AI to find the changes before it maps anything. This run was sent the [county names for each year]({{ '/assets/mapping-with-ai/data/nm-counties-1900-1910.txt' | relative_url }}), pasted above the prompt.

{% include prompt.html id="mapping-census-boundaries" %}

{% include demo.html id="mapping-census-boundaries" %}

Compare its list with the paragraph on page 159. The reply was candid that it worked from memory, and the comparison shows why that matters:

- **Leonard Wood.** The reply says Guadalupe was renamed Leonard Wood and then renamed back. The report says Leonard Wood was a new county made in 1903 from parts of Bernalillo, Valencia and old Guadalupe, and renamed Guadalupe in 1905. The name returned with a different shape.
- **McKinley.** The reply dates it to 1899, warns that it should already appear in the 1900 census, and names only Bernalillo and possibly Valencia as the counties it came from. The report says it was formed in 1901 from parts of Bernalillo, Rio Arriba, San Juan and Valencia, and counts it among the eight new counties. Check the Newberry atlas for which date applies to census day.
- **Torrance.** The reply dates it to 1903 and leaves Bernalillo out of the counties it came from. The report says it was formed in 1905 and includes Bernalillo.
- **Rio Arriba.** The report notes that part of Santa Fe County was annexed to Rio Arriba in 1902. The reply mentions unspecified line changes “around Bernalillo and Santa Fe” but not this one.

Its advice, by contrast, holds up: combine counties that changed, use boundaries from each census year, and check every change against the atlas. That is the same answer the Census Bureau reached in 1913. Anything a reply asserts that the report doesn't mention, check in the Newberry atlas before you accept it.

<div class="keypoint" markdown="1">
Before mapping figures from more than one census, ask: “Which counties were created, renamed or redrawn between these years?” Then use boundaries from the year of each figure.
</div>

## 6. Make a map figure for publication
{: .step #step-6}

The checked tables from steps 2 to 5 can become a web map or a printed figure. A screenshot of a web map makes a poor figure: low resolution, map tiles designed for a screen, attribution requirements for the tiles, and colors that may vanish in grayscale. Ask for a figure instead.

### Ask for the program, not the picture

Every map so far has been a web page: an HTML file that your browser runs each time you open it, fetching map tiles, drawing the points or counties and answering your clicks. That suits exploring. A publication needs something else: a fixed image that looks the same on screen, in a PDF and on paper.

So this step asks for a **script** instead of a map. A script is a short program, a list of instructions a computer carries out in order, and running it produces the figure. This one is written in **Python**, a programming language widely used for working with data. It relies on two free add-ons, called libraries, that other people have written: **geopandas**, which reads tables and boundary files and joins them, and **matplotlib**, which draws charts and figures. In plain terms, the script:

1. reads your CSV and the boundary file;
2. joins them on FIPS codes, as in step 4, and stops if any county fails to match;
3. works out each county's percent change from the figures in the CSV;
4. flattens the map with an equal-area projection and shades each county by its class;
5. adds the names, legend, scale bar and source line;
6. saves the result as a high-resolution PNG and a PDF.

Why go to the trouble of a script, rather than asking for the image itself?

- **Every number comes from your file.** The prompt rules out typing data into the script, so the figure can't drift from the CSV.
- **You can make it again.** Correct a figure in the CSV or change one setting, run the script, and the whole figure updates exactly.
- **The choices are written down.** The projection, the class breaks and the colors are all in the script, so you can see how the figure was made, and so can anyone you share it with.

You don't need to read the code to use it. A tool that can run code, like the one recorded here, runs the script and hands you the finished image. Otherwise it gives you the script and instructions, and you run it on your own computer, which needs Python installed. Either way, keep the script.

This run was sent the [New Mexico county table]({{ '/assets/mapping-with-ai/data/nm-county-population-2020-2024.csv' | relative_url }}) from step 4 and the Census Bureau's [county boundary file](https://www2.census.gov/geo/tiger/GENZ2023/shp/cb_2023_us_county_500k.zip) (12 MB). Attach both, fill in the brackets and send this. In this run, the first bracket described percent change in population in New Mexico counties from 2020 to 2024, and the second gave the source line printed at the foot of the figure.

{% include prompt.html id="mapping-figure" %}

{% include demo.html id="mapping-figure" %}

{% include images/figure.html
  image-width="80%"
  caption="The figure the script produced: 6.5 inches wide at 300 dots per inch (dpi), a usual resolution for print, and also saved as a PDF."
  alt-text="Print-style choropleth of New Mexico counties in oranges for population loss and blues for gain from 2020 to 2024, with county names, a legend giving each class and its number of counties, a scale bar in kilometers and miles, and a source line."
  image-path="/sessions/mapping-with-ai/images/run-figure-nm-pop-change.png"
%}

Open [the PDF]({{ '/assets/mapping-with-ai/maps/nm_population_change_2020_2024.pdf' | relative_url }}){: target="_blank" rel="noopener"} or download [the script]({{ '/assets/mapping-with-ai/maps/nm_pop_change_map.py' | relative_url }}) that made it.

Compare this figure with the web map in step 4. Both measure from the July 1, 2020 estimate, and the figure prints that in its subtitle. The table also has an April 1, 2020 base, which would start every county from a different number. The reply flags this as a decision for you, says how much it moves the results (Catron County goes from +5.2% to +6.0%) and adds an option to switch. **Make sure the measure on the figure is the one your text describes.**

The install and run instructions at the end of the reply are for later, when you want to remake the figure yourself. If you haven't used Python before, ask the tool to walk you through them on your own computer. Look at what the colors say, too. So that the figure reads in grayscale, they darken steadily from the biggest loss to the biggest gain, which makes the five counties that lost the most, such as McKinley and Hidalgo, the palest on the map. They can look like the counties that changed least. The reply describes the colors but not that trade-off. If the figure will be seen in color, ask for both ends of the scale to be dark. Open the PDF at full size. Check that every label is readable at the size it will be printed, that the legend's classes match the data, and that the source line names your sources. Keep the script and the CSV with your manuscript files. When a reviewer or editor asks for a different shading or one more county, you change a line and run it again rather than rebuilding the map.

If you would rather not run code, [Datawrapper](https://www.datawrapper.de/) makes county maps of the United States and of individual states from a pasted table with FIPS codes, and exports images. [QGIS](https://qgis.org/) is free and does everything here, with more to learn.

<div class="keypoint" markdown="1">
Ask for a script that writes the figure from your CSV, not for a picture of the map. Keep the script, data and sources together so the figure can be remade.
</div>

## What to take with you
{: .step #takeaways}

<div class="takeaways" markdown="1">
Use these habits when you map your own material:

- **Know how your map was made.** Keep a note of where the places, the numbers and the choices came from, including the choices the AI made, and keep it with the map.
- **Don't spend your effort on the drawing.** Once you know where things are, a first map takes one request. Spend the time you save checking the information behind it.
- **Ask where each location came from.** A location should come from a source you can open, such as an official list of place names or the photo itself. One the AI supplied from memory is a guess.
- **Show what you couldn't place.** List the places that have no location beside the map, so the map doesn't look more complete than your evidence.
- **Match places by ID number, not by name.** The same place is spelled differently from one source to the next. Ask which ones failed to match, every time.
- **Compare like with like.** Shade by a percentage or a figure per person rather than a raw total, which mostly shows where people live. Ask what color bands the tool chose, and why.
- **Use borders from the same year as your numbers.** Counties were created, renamed and redrawn, and a county's name doesn't tell you which version you have.
- **Keep the code with the figure.** If you can remake a figure from its data, you can fix it when someone finds a mistake.
</div>

---
title: Audit Trails for AI Agents
layout: base
position: 3
date: 2026-10-21
time: "12:00–12:50"
location: History Commons (MVH 1104)
kicker: Session 3 · October 21, 2026
summary: "Read into a topic with an AI agent, map the articles’ ideas and relationships, and keep a record of what you checked and chose to read next."
note: "Bring a laptop and a topic to explore, or use the example we provide."
points:
  - title: Organize sources, prompts, outputs
    text: Set up a project workspace that preserves your research materials, AI instructions, and results.
  - title: Check claims, track corrections
    text: Use AI agents to review each other's work, verify claims against original sources, and record errors and corrections.
  - title: Document decisions and revisions
    text: Keep a concise record of what you accepted, changed, or rejected, and why, so others can follow your research process.
flyer: "audit-trail-flyer-v2.jpeg"
thumbnail: "/assets/images/stradanus-press-1600.jpg"
header-image: "/assets/images/stradanus-press-1600.jpg"
header-tier: section
header-filter: etching
header-position: center right
header-opacity: 0.18
header-title: Audit Trails for AI Agents
header-subtitle: "An agent can help you find your way into a body of writing. Keep the articles, interpretations and reading choices together so you can check and revise the map."
header-caption: "Jan van der Straet (Stradanus), <i>Impressio Librorum</i>, from <i>Nova Reperta</i>, engraved by Joannes Galle. Museum Plantin-Moretus, public domain."
tags: [research, agents, audit trails]
workshop_mode: true
css: audit-workspace.css
redirect_from: /sessions/audit-trails-for-ai-agents.html
---

{% comment %}
Authoring conventions: SESSION-STYLE.md; worked example: sessions/editorial-assistant/index.md.
Prepared examples below are teaching materials, never recorded agent replies.
{% endcomment %}

{% include nav/scrollspy-toc.html %}

Work down this page during the session or return to it later: the prompts, source links and example files stay together so you can repeat the exercise.
{: .lead}

<div class="rule" markdown="1">
**Keep the route from article to interpretation.**
</div>

## Introduction
{: .step #introduction}

### Why reading into a topic is the place to start

Start with a topic you want to understand. Ask an agent to find several
articles, explain their arguments and suggest where to spend your reading
time. That can give you an overview quickly. The useful result is a map you
can question: which ideas belong to which authors, where the articles meet
or pull apart, and what you want to follow next.

**Theoretical arguments and ways of framing a problem are part of what you
are reading for.** A source can matter because it changes your question,
introduces a distinction or gives you another way to interpret AI. Record
what kind of work it does and why that matters to your inquiry.

An audit trail keeps those interpretations available for someone else to
follow. Save the search boundaries, the material actually accessed, the
notes, and the reasons you changed a summary or a reading recommendation.
A saved chat can help, but a colleague should be able to follow one important
connection without reading your whole conversation.

This continues the [editing session's work with a saved style guide]({{ site.baseurl }}/sessions/editorial-assistant/#step-5).
There, you taught the assistant how to read your writing. Here, you give it a
reading procedure and check how it represents other people's arguments.

### What you're working with

- A tool with search and file access can gather articles and keep a source
  register. Check what it can access and save. (Step 2)
- An agent can compare several texts and recommend a reading order. Ask for
  the grounds of each connection and recommendation. (Step 3)
- Another agent can challenge the overview, but its interpretations also need
  checking against the original articles. (Step 4)
- Files keep your corrections and decisions available across conversations.
  The same notes can later feed a visual map or citation manager. (Step 5)

An agent is a way of working: you delegate a bounded task and it chooses
intermediate actions using the tools available. A browser chat can support
that workflow too. Watch what it does and saves. If your assistant cannot
write files, save its outputs yourself using the same filenames.

### Before you start

- **A laptop and an AI assistant**, with web search available. The presenter
  demonstrates a folder and text editor; you can save replies from a browser
  chat into files.
- **A topic you want to explore**, or the question below.
- **A folder for the exercise**, and a text editor that opens `.md` or `.txt`
  files. Everything you need for the main exercise is plain text. Obsidian
  and Zotero appear only in optional presenter demos at the end.

<div class="reminder" markdown="1">
Use sources and research materials you have permission to share, such as the public articles linked below or your own notes.
</div>

### The question we'll use

> How do arts and humanities perspectives help us think about AI?

Choose an interest within that topic: ethical concepts, historical framing,
creative practice, or something from your own field. Keep it in `brief.md`.
It gives you a reason to prefer one reading route over another. You are
getting oriented in a body of writing and deciding what deserves closer
attention.

**About the examples on this page.** The workspace and comparisons are
prepared teaching examples using five sources, checked during authoring on
October 11, 2026. Four source bodies and selected passages from the fifth
were read; the files state that coverage. The first overview deliberately
flattens a difference between authors, and its reading recommendation follows that mistake. These
are not transcripts of an agent run. Keep the tool, date, instructions and
replies from your own live exercise as a separate record.

## 1. Start with an overview you would want to use
{: .step #step-1}

Send the question as a reasonable first request. Save the complete reply as
`baseline.md`, including its citations and the date.

{% include prompt.html id="audit-baseline" %}

**Prepared example:** “The three essays offer the same framework: pluralism,
procedures and participation. Powell repeats Tasioulas, so read her last.”

This gives you an apparent overview and an efficient reading order. Before
you follow it, look at what you would need to check.

- Who actually sets out that framework?
- Does “repeats” describe the relationship between the texts?
- Which passages explain the recommendation to read Powell last?
- Would a different interest change the reading order?

Keep your own first reply too. Choose one connection or recommendation whose
accuracy would change where you spend your reading time.

<div class="keypoint" markdown="1">
Save the first overview. Pick one interpretation or reading recommendation to follow back to the articles.
</div>

## 2. Set the search boundaries and open a workspace
{: .step #step-2}

Write a brief before the agent searches. Choose a date range, source types,
languages and a particular interest within the topic. Say what would make an
article worth including.

{% include prompt.html id="audit-retrieve" %}

Give retrieval eight minutes. Find up to eight candidates and choose five
accessible sources for an initial orientation. If fewer are ready, record
that and use the backup set. A blocked or paywalled source stays in the register as a lead; record what you could access and move on.
The backup set is linked in step 3.

Compare one search choice with another pair. A search for historical framing
may produce a different starting set from a search for ethical concepts.
Restricting source types or languages also changes what you can see.
**Save the choice that shaped the set, as well as the articles it produced.**

### Give each part of the work a home

Download the [example workspace]({{ site.baseurl }}/assets/audit-trails/example-workspace.zip)
and open it in a text editor. The files are small enough to read together.

```text
humanities-ai/
  baseline.md
  brief.md
  sources.md
  reading-protocol.md
  prompts.md
  notes/
    S01-tasioulas.md
    S02-vallor.md
    S03-powell.md
    S04-chander-squirrel-nation.md
    S05-goodlad.md
  synthesis-v1.md
  idea-map-v1.md
  reading-queue-v1.md
  checks.md
  decisions.md
  synthesis-v2.md
  idea-map-v2.md
  reading-queue-v2.md
  methods.md
```

### Keep a short record of each AI step

In `prompts.md`, give each actual step a run ID and save its exact prompt,
input files and source IDs, procedure version, output filenames and unfinished
work. For example, a comparison uses five notes and produces three v1 files;
a check uses those versions and records the passages it actually reviewed.
If both steps happen in one conversation, record the shared context.

With five sources, a later reader needs to see whether all five entered the
comparison, whether a revision used updated notes, and which connections
received a passage check. **A file called “checked” does not say what was checked.**
The prepared run index is a template; fill it with what actually happened.

Use stable IDs such as `S01` to follow an article across the source register,
notes, comparisons and corrections. You can transfer the citations to Zotero
later; collecting them need not interrupt the reading exercise.

{% include audit-workspace.html %}

The browser view shows the same prepared files as the download. Select a
stage, then a file. During the session, open your actual folder beside the
agent and watch which files it creates. The viewer displays saved examples.

<div class="keypoint" markdown="1">
Ask the agent to record the searches it actually ran, its selection reasons and how much of each article it could access.
</div>

## 3. Compare the articles and choose a reading route
{: .step #step-3}

Open the sources before relying on the notes. The five-source backup set
combines three linked essays, a related dialogue and a journal introduction:

- [John Tasioulas: The role of the arts and humanities in thinking about artificial intelligence](https://www.adalovelaceinstitute.org/blog/role-arts-humanities-thinking-artificial-intelligence-ai/).
- [Shannon Vallor: Mobilising the intellectual resources of the arts and humanities](https://www.adalovelaceinstitute.org/blog/mobilising-intellectual-resources-arts-humanities/).
- [Alison Powell: Otherwises, and the contribution of the arts and humanities to ethical AI](https://www.adalovelaceinstitute.org/blog/otherwises-contribution-arts-humanities-ethical-ai/).
- [Sarah Devi Chander and Squirrel Nation: Who gets to write the future?](https://www.adalovelaceinstitute.org/blog/who-write-future/), a dialogue linked from Powell's essay.
- [Lauren M. E. Goodlad: Editor's Introduction: Humanities in the Loop](https://doi.org/10.1215/2834703X-10734016), with an accessible [project-hosted proof PDF](https://criticalai.org/wp-content/uploads/2023/09/CAI112_01Goodlad_1pp-1-1.pdf).

The set gives you both an explicit conversation and connections you can
propose across forms and venues. Record that you used it. Four sources come
from one publisher; a broader search would need other traditions and positions.
The prepared Goodlad note uses selected passages on proof PDF pages 1 and 6,
so its recommendation remains provisional.

Read `reading-protocol.md` and change one rule to suit your discipline. Give
the agent the articles, the brief and the procedure. Ask for short orientation
notes for all five, then read one or two important passages yourself. Keep
the notes brief so comparison and checking fit the hour. Record the passages
you checked and leave the rest as open work.

{% include prompt.html id="audit-read" %}

### Get an overview that preserves differences

Ask the agent to compare the articles from their notes and the original
texts. Save an overview, an idea map and a reading queue as separate files.

{% include prompt.html id="audit-synthesize" %}

**Prepared comparison:**

| Article | A focus to follow | Relationship to check |
|---|---|---|
| S01 · Tasioulas | Choice, plural values and participation | Sets out the three Ps; start at the named section. |
| S02 · Vallor | Historical framing and technological imagination | Responds to S01; read the opening and the paragraph beginning “The desire to keep an ahistorical frame”. |
| S03 · Powell | Creative possibilities and situated practices | Responds to both; “Ethics and practice” reframes procedures as practices. |
| S04 · Chander and Squirrel Nation | Racial justice, lived experience and creative practice in policymaking | S03 links here. Preserve the dialogue's named speakers; compare their participation questions with S01. |
| S05 · Goodlad | Interdisciplinary critical AI and public accountability | Compare the selected proof passages with S04 as our interpretation; a direct response is not established. |

A useful overview carries the distinctions into its prose. It should help
you explain what each author adds. Read the comparison beside the articles:
does it make a useful distinction, or turn a passing example into the
article's central claim?

### Make the connections explainable

Use `idea-map-v1.md` to connect source IDs with themes and with one another.
For each connection, name the relationship and its basis. A direct response
is different from a thematic connection that you infer as a reader.

**Prepared connection:** S03 → S01: reframes “procedures” as “practices”.
The basis is Powell's “Ethics and practice” section. You can go to that
passage and decide whether “reframes” captures the move.

Compare S03's direct hyperlink to S04 with a proposed S05–S04 connection
through public accountability. The first is an observable citation; the
second is our thematic reading. Neither establishes that the authors agree
on everything.

Do the same for a connection in your own set. Keep an uncertain relationship
marked as a question. The map can include an interesting tension without
turning it into a direct disagreement or claiming one author cited another.

### Ask what deserves your next twenty minutes

Use `reading-queue-v1.md` to recommend an order for *your* inquiry. Each entry
should give the reading goal, the relevant passage, why it adds something,
and how much text was available for the recommendation. A rating such as
“9/10 relevance” hides those decisions.

**Prepared reading routes:**

| Your interest | Spend more time on | Why this is a useful next reading |
|---|---|---|
| Ethical concepts | S01, the three Ps section | Follow how the framework separates values, decision processes and participation. |
| Historical framing | S02, the ahistorical-framing passage | Follow how history changes the questions asked about technology. |
| Creative practice | S03, “Ethics and practice”, then S04's dialogue | Compare situated practice with questions about whose lived experience enters policymaking. |
| Racial justice and policymaking | S04, Sarah's participation turn | Question who sets the terms of participation. |
| Interdisciplinary research | S05, proof PDF pages 1 and 6, then the full introduction | Explore a wider critical AI project; this route is provisional because only selected passages were read. |

These recommendations depend on the question you brought. An article can
be worth reading because it complicates the others or takes your interest in
a new direction. Ask the agent how the order would change if you changed
your interest. If it only saw an abstract or selected passages, keep its
recommendation provisional. Give every selected source a next action, even if that action
is to read more before assessing it.

### Keep the procedure in plain text

A short file is enough to specify how to read: state access levels, preserve
the author's argument, give passage locations, and separate interpretation
from what the source says. Bring it into each new conversation and check a
note against it.

A skill can package this procedure for reuse. Start with the text file and
revise the instructions when you see what they miss. Keep its version with
the notes so a later reader can see how you asked the agent to read.

<div class="keypoint" markdown="1">
Ask for the passage and reading goal behind every important connection or recommendation. Check one against the original text.
</div>

## 4. Check a connection and challenge the checker
{: .step #step-4}

Give another agent the original articles, brief, notes, overview, map and
reading queue. Use a fresh conversation where possible. Save its findings
in `checks.md` with the tool and date.

{% include prompt.html id="audit-check" %}

### Follow one correction back to the article

Return to the prepared sentence from step 1. Tasioulas sets out the three Ps.
Powell's “Ethics and practice” section explicitly nuances that framing by
recasting procedures as practices. Describing this as repetition misses a
reason you might want to read her closely.

**Prepared check:**

| Draft wording | Passage to check | Proposed action |
|---|---|---|
| “The three essays offer the same framework” | S01's three Ps section; S03's “Ethics and practice” | Attribute the framework to S01 and preserve S03's reframing. |
| “Powell repeats Tasioulas, so read her last” | S03's distinction between procedures and practices | Change the map connection and explain when S03 is worth closer reading. |

Read the passages before accepting the criticism. Ask whether the proposed
correction preserves the authors' arguments and whether its reading
recommendation fits your interest. An interpretation can be defensible
without being the only possible reading; record what you remain unsure about.

### Check a second kind of error

The prepared first map says Goodlad directly responds to Tasioulas. Its queue
also claims the complete introduction was read. The saved access record says
selected passages, and those passages do not establish that direct response.

Compare `idea-map-v1.md` and `reading-queue-v1.md` with S05's note and the
original proof. Keep a useful thematic comparison if you can explain it,
label it as your interpretation, and correct the access claim. Save this
finding as C04. Full-paper reading remains open.

### Check a criticism you might reject

**Prepared suggestion from a checker:** “These are linked essays in one
series. Merge them into one note and drop the later readings as duplicates.”

Their relationship belongs in the register and the map. It also makes them
useful to read together: the later essays shift the emphasis and develop the
conversation. You might keep separate notes so those moves remain visible.
Record why you accept or reject the suggestion.

Check the records too. Does every cited article have a note? Do access
statuses match what was read? Can you locate the basis for a map connection?
Does the queue silently drop an article because it is difficult to access?

Separate agents can share assumptions. Read at least one important passage
yourself and judge both the overview and the checker's reading against it.

<div class="keypoint" markdown="1">
Check a proposed correction against the article and your reading goal before treating it as a decision.
</div>

## 5. Record your decisions and keep the reading route
{: .step #step-5}

Decide which findings hold up, then add your reasons to `decisions.md`.
Preserve the first overview, map and queue when you create revised versions.

{% include prompt.html id="audit-revise" %}

**Prepared decision record:**

| Decision | Reason | Consequence |
|---|---|---|
| Accept the objection to “same framework” | S03 explicitly reframes S01's procedures | Show distinct contributions in the overview and map. |
| Revise the recommendation to read Powell last | Her discussion fits an interest in creative practice | Name that reading goal and the relevant section in the queue. |
| Reject merging the essays as duplicates | Their different moves are useful to compare | Keep separate notes and record their relationship. |
| Revise S05's direct-response and access claims | The selected passages support our comparison; the whole paper was not read | Label the map link and keep the next reading provisional. |

An agent can prepare this table from your comments. **You supply the
decision.** Proposed changes stay pending until you decide; record who decided
and when.

**Prepared revision:** “The five sources offer several routes into humanities
and AI. Tasioulas sets out an ethical framework; Vallor foregrounds history
and imagination; Powell reframes procedures through situated practice.
The dialogue brings racial justice and lived experience into policymaking.
Goodlad's selected passages frame a wider interdisciplinary critical AI project.”

Open both versions beside `checks.md` and `decisions.md`. The record should
explain changes to your overview, your connections and your reading order.
Append new corrections to the log and keep the current reading route in the
latest files. This follows the CHM project's use of process notes alongside
a separate account of current conclusions and open work.

### Give someone else a few minutes

Exchange folders. Ask a partner to trace one connection to an article,
explain one reading recommendation and identify which passages were checked
from your records alone. Add the passage,
link or reason they needed and could not find.

Keep a short `methods.md` with the actual search choices, sources accessed,
tool and procedure used, checks completed, human decisions and open work.
For peer review, consider how this would help a reader assess an AI-assisted
interpretation. Procedural evidence can make a judgment easier to examine;
the reviewer still needs to judge the reading and argument.

### Optional closing demo: open the notes in Obsidian

The presenter can open the downloaded `humanities-ai` folder as an Obsidian
vault. Start with `idea-map-v2.md`, follow a link into a source note, and open
its local graph. The prepared notes also link to a few idea notes in `ideas/`.
No plugins are needed for this demonstration.

Obsidian's [graph view](https://help.obsidian.md/Plugins/Graph+view) draws
connections from links between notes. **Keep the relationship in the text
beside the link.** The graph shows that you connected two notes; their text
explains whether you mean a direct response, a shared theme or a provisional
interpretation. Click a connection's source note and show its passage location.

{% include prompt.html id="audit-obsidian" %}

The same Markdown files remain usable in a text editor. Participants do not
need to install Obsidian during the workshop.

### Optional closing demo: import the citations into Zotero

The presenter can ask the agent to make `library.ris` from the verified source
register, then demonstrate **File → Import → A file** in Zotero. Compare one
imported item's author, title, date and URL with the original article. Zotero
[accepts RIS and other standard formats](https://www.zotero.org/support/kb/importing_standardized_formats).

{% include prompt.html id="audit-zotero" %}

A [prepared five-item RIS file]({{ site.baseurl }}/assets/audit-trails/humanities-ai/library.ris)
is included in the workspace so the demo can continue if live generation
fails. It imports citation records into a collection. The separate Markdown
files keep the reading notes, connections and decisions; this citation export
does not bundle the article texts or the audit trail.

<div class="keypoint" markdown="1">
Keep the reasons behind a revised interpretation or reading choice. A colleague should be able to follow the change from your files.
</div>

## What to take with you
{: .step #takeaways}

<div class="takeaways" markdown="1">
Use these habits in your next reading project:

- **Save the search choices.** Keep your interest and selection boundaries beside the articles.
- **State what was read.** Distinguish metadata, abstracts, selected passages and full texts; record check coverage separately.
- **Record each AI step.** Save the instructions, inputs, output versions and unfinished work behind your comparisons.
- **Preserve different arguments.** Check what each author adds before combining them into an overview.
- **Explain the connections.** Name the relationship and the passage behind a link in your map.
- **Give a reason to read next.** Tie recommendations to your inquiry and keep uncertainty visible.
- **Keep your corrections.** Save earlier versions and the reasons your interpretation or reading route changed.
</div>

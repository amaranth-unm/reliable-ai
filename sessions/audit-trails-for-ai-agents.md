---
title: Audit Trails for AI Agents
layout: base
position: 3
date: 2026-10-21
time: "12:00–12:50"
location: History Commons (MVH 1104)
kicker: Session 3 · October 21, 2026
summary: "Explore a research question with an AI agent, then trace its claims through sources, reading notes, checks and your decisions."
note: "Bring a laptop and a research question, or use the example on this page."
published: false
thumbnail: "/assets/images/stradanus-press-1600.jpg"
header-image: "/assets/images/stradanus-press-1600.jpg"
header-tier: section
header-filter: etching
header-position: center right
header-opacity: 0.18
header-title: Audit Trails for AI Agents
header-subtitle: "An agent can move quickly from a question to a convincing summary. Keep enough evidence to explain how it got there, what you checked and why you changed it."
header-caption: "Jan van der Straet (Stradanus), <i>Impressio Librorum</i>, from <i>Nova Reperta</i>, engraved by Joannes Galle. Museum Plantin-Moretus, public domain."
tags: [research, agents, audit trails]
workshop_mode: true
css: audit-workspace.css
---

{% comment %}
Authoring conventions: SESSION-STYLE.md; worked example: sessions/editorial-assistant.md.
Prepared examples below are teaching materials, never recorded agent replies.
{% endcomment %}

{% include nav/scrollspy-toc.html %}

Work down this page during the session or return to it later: the prompts, source links and example files stay together so you can repeat the exercise.
{: .lead}

<div class="rule" markdown="1">
**Keep the evidence behind the answer.**
</div>

## Introduction
{: .step #introduction}

### Why a research sprint is the place to start

Start with a topic you want to explore, and ask an agent to find sources and
write a short synthesis. You can get a useful orientation quickly. But reading
the synthesis alone won't tell you whether it used whole articles or abstracts,
why it chose those sources, or which claims you have checked.

**An audit trail makes those choices available for someone else to follow.**
Keep the question and search boundaries, the sources actually accessed, the
reading notes, and the corrections that changed the result. A saved chat can
help, but a reader should be able to trace a consequential claim without
working through your entire conversation.

This continues the [editing session's work with a saved style guide]({{ site.baseurl }}/sessions/editorial-assistant#step-5).
There, you taught the assistant how to read your writing. Here, you give it a
reading procedure and require records that let you check its use of sources.

### What you're working with

- A tool with search and file access can carry out several steps from one
  instruction. Check what your tool can do before delegating the task. (Step 2)
- A source link can lead to metadata, an abstract or a full text. Each gives
  you a different basis for a claim. (Step 3)
- Another agent can challenge the first one's summary. Its criticism also
  needs checking against the original. (Step 4)
- Files can preserve a correction across conversations, including the reason
  you accepted or rejected it. (Step 5)

An agent is a way of working: you delegate a bounded task and it chooses
intermediate actions using the tools available. A browser chat can support
that workflow too. Watch what it does and saves. If your assistant cannot
write files, save its outputs yourself using the same filenames.

### Before you start

- **A laptop and an AI assistant**, with web search available. The presenter
  demonstrates an agent working with a folder and text editor; you can use
  a browser chat and save the replies into files.
- **A narrow research question**, or the question below.
- **A folder for this exercise**, and a text editor that opens `.md` or `.txt`
  files. Zotero is useful for collecting citations, but you can complete the
  exercise with the source register provided here.

<div class="reminder" markdown="1">
Use sources and research materials you have permission to share, such as the public articles linked below or your own notes.
</div>

### The question we'll use

> What do humanities methods contribute to evaluating AI, and what evidence
> supports those contributions?

Keep this question through the whole exercise. It lets you separate proposals
about what the humanities could contribute from studies that demonstrate an
effect. Both can matter, but they support different claims.

**About the examples on this page.** The workspace and before-and-after
synthesis are prepared teaching examples, checked against the linked original
essays on October 11, 2026. The first synthesis deliberately overstates the
evidence. They are not transcripts of an agent run or measurements of its
performance. Your live runs produce a separate record; keep the tool, date,
exact instructions and replies you actually used.

## 1. Start with a summary you would want to use
{: .step #step-1}

Send the question as a reasonable first request. Save the reply as
`baseline.md`, including any citations and the date.

{% include prompt.html id="audit-baseline" %}

**Prepared example:** “Humanities methods improve AI evaluation. Two independent
essays demonstrate that historical and ethical analysis produces fairer
systems.”

The sentence sounds useful, and it appears to have sources. Before you carry
it into a literature review, ask what you would need to check.

- Does “improve” describe a measured result or a proposed contribution?
- What makes the sources independent?
- Did the assistant read the articles, or find descriptions of them?
- Where would you go to verify the sentence?

The later steps return to this sentence. Keep your own first reply too:
choose one consequential claim and see whether the records you make allow
another person to check it.

<div class="keypoint" markdown="1">
Save the first synthesis before you improve the instructions. Pick one claim whose wording would matter if you cited it.
</div>

## 2. Set the search boundaries and open a workspace
{: .step #step-2}

Write a brief before the agent searches. Choose a date range, source types and
languages, then say what makes a source relevant. Keep the question open
enough that a source can complicate your initial expectation.

{% include prompt.html id="audit-retrieve" %}

Give the search eight minutes. Find up to five candidates and choose two
accessible texts to read. A blocked or paywalled source stays in the register
as a lead; record what you could access and move on. **Availability shapes
your corpus, so keep the access limitation alongside the source.**

Compare one search choice with another pair. Restricting the search to
peer-reviewed research may miss useful conceptual essays. Restricting it to
freely accessible English texts may exclude relevant scholarship. Neither
choice is automatically wrong; both limit what you can claim afterwards.

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
  synthesis-v1.md
  checks.md
  decisions.md
  synthesis-v2.md
  methods.md
```

Put citations in Zotero if you already use it. Keep stable IDs such as `S01`
in your notes and claim checks so you can follow the source across files.
Finding a source, saving its citation and reading it are separate events.

{% include audit-workspace.html %}

The browser view shows the same prepared files as the download. Select a
stage, then a file. It is a way to read a saved example, not a live display
of an agent's activity. During the session, open your actual folder beside
the agent and watch which files it creates.

<div class="keypoint" markdown="1">
Ask the agent to record the searches it actually ran, its inclusion decisions and how much of each source it could access.
</div>

## 3. Read two sources with a procedure you can check
{: .step #step-3}

Open the original articles before relying on the notes. The backup pair is
[John Tasioulas's essay](https://www.adalovelaceinstitute.org/blog/role-arts-humanities-thinking-artificial-intelligence-ai/)
and [Shannon Vallor's response](https://www.adalovelaceinstitute.org/blog/mobilising-intellectual-resources-arts-humanities/).
Both are accessible on the Ada Lovelace Institute's website. Record that you
used the backup pair if retrieval brought you here.

Read `reading-protocol.md` and change one rule to suit your discipline. Then
give the agent the original text, the brief and the procedure.

{% include prompt.html id="audit-read" %}

**Prepared note, S01:** The source is a conceptual essay. In the section on
procedures, Tasioulas argues that the process of making an AI-assisted
decision matters alongside its outcome. That supports a claim about what
evaluation should consider; it does not measure whether a humanities
intervention makes a system fairer.

Go to the named section and decide whether the note preserves the author's
argument. On a web page, use a heading and a short identifying phrase. In a
PDF, record the printed page and the PDF page if they differ. A quotation
helps you find the evidence; you still have to judge what it supports.

Read the second note beside the second article. Vallor's opening explicitly
responds to Tasioulas. **Two source records do not establish two independent
lines of evidence.** Add that relationship to the register before writing
the synthesis.

Use the two notes to write a short synthesis of the same question. Save this
as `synthesis-v1.md`, and preserve `baseline.md` as your initial orientation.
The sourced draft is the one you give the checker in step 4. Compare it with
your baseline: which claims changed once you knew what the sources contained?

{% include prompt.html id="audit-synthesize" %}

### Keep the procedure in plain text

A short file is enough to specify how to read: distinguish access levels,
state the source's own argument, identify evidence locations, and separate
interpretation from what the source says. Bring it into each new conversation
and check one note against it.

A skill packages a reusable procedure, usually with a name, instructions
about when to use it, and optional templates or scripts. You can turn this
file into a skill once you know which rules help. Keeping a version of the
procedure with this project's notes lets a later reader see which rules you
used, even if your installed skill changes.

Now use the same procedure on one source for your own question. Check whether
it captures the kind of intervention that matters in your field, rather than
only extracting passages that support your argument.

<div class="keypoint" markdown="1">
Require every note to state what was accessed and give a location for each claim you might carry into the synthesis.
</div>

## 4. Check the claim and challenge the checker
{: .step #step-4}

Give another agent the original sources, reading notes, brief and first
synthesis. Use a fresh conversation where possible and require it to open
the originals. Save its reply as `checks.md` with the tool and date.

{% include prompt.html id="audit-check" %}

### Follow one correction back to the source

Return to the prepared sentence from step 1. The word “demonstrate” would
require evidence these essays do not provide. The articles make arguments
about AI ethics; they do not report a comparative trial of system fairness.
The source relationship also needs correcting: Vallor directly discusses
Tasioulas's essay.

**Prepared check:**

| Draft wording | Evidence to check | Proposed action |
|---|---|---|
| “demonstrate … fairer systems” | The sources' argument and evidence type | Replace the claim of demonstrated effects with a description of proposed contributions. |
| “Two independent essays” | S02's opening response to S01 | Describe the relationship and limit the claim of corroboration. |

Read the actual passages before accepting either criticism. A checker that
says “unsupported” without a location or an explanation leaves you with
another assertion. Ask what evidence would support the stronger wording and
whether the source contains it. Record an unresolved judgment when you
cannot decide.

### Check a criticism you might reject

**Prepared suggestion from a checker:** “Remove the essays because they
contain no experiment.”

The brief permits conceptual essays. They help answer what humanities
methods could contribute, even though they do not establish a measured
effect. Keep them for that purpose and narrow the synthesis. Rejecting the
suggestion is a research decision worth saving: it explains why a source
remained in the corpus after a challenge.

Run this comparison on the claim you selected from your own first reply.
Look for a correction you accept and one that needs more work. The checker
may find an error, overstate its objection, or simply lack context. Give its
claims the same scrutiny as the first agent's claims.

### Check the records as well as the argument

Ask whether each cited source has a note, whether the access statuses agree
with what was read, and whether the synthesis cites the current notes. This
is a different check from asking whether a passage supports a claim. A
missing source note can survive an otherwise careful argument review.

Separate agent conversations can reduce the influence of the first draft's
framing, but they can share assumptions and blind spots. Read at least one
consequential passage yourself. Agent agreement is a reason to look at the
evidence, and your decision follows that reading.

<div class="keypoint" markdown="1">
Require a checker to name the claim, locate the evidence and propose an action. Check those three things before recording its finding as a correction.
</div>

## 5. Record your decision and hand over the folder
{: .step #step-5}

Decide which findings hold up, then add an entry to `decisions.md` before
revising the synthesis. Keep the first draft intact.

{% include prompt.html id="audit-revise" %}

**Prepared decision record:**

| Decision | Reason | Consequence |
|---|---|---|
| Accept the objection to “demonstrate” | Neither essay measures a fairness improvement | Describe proposed contributions in v2. |
| Accept the objection to “independent” | S02 explicitly responds to S01 | State the source relationship. |
| Reject automatic exclusion of conceptual essays | The brief includes arguments about evaluation | Keep both, with their evidence type visible. |

An agent can prepare this table from your comments. **You supply the
decision.** If it proposes a disposition you have not made, label it pending
rather than recording that you accepted it. Include who decided and when in
your own file.

**Prepared revision:** “These linked conceptual essays propose ways humanities
can broaden AI evaluation. They do not establish a measured improvement in
system fairness. Further research is needed to test that effect.”

The revision carries less certainty, but the folder makes its basis easier
to judge. Open v1 and v2 side by side. You can see which words changed, and
`checks.md` and `decisions.md` explain why.

### Keep the history and the current conclusion separate

Append corrections to the chronological record. Put the current conclusion
and open questions in v2 or a short state file. If a later source changes
your view, add the new finding and update the current conclusion; preserve
the earlier entry so someone can follow the change.

This follows the division used in the CHM research project: source notes,
argument checks and a methods log preserved the research process, while a
separate process-state file held the current conclusions and open work.
For today's small exercise, `decisions.md` and `synthesis-v2.md` do those jobs.

### Give someone else five minutes

Exchange folders. Ask your partner to trace one revised claim to the original
source and explain one accepted or rejected correction without asking you
what happened. Note where they get stuck. That tells you which link or
decision your records still need.

Add a short `methods.md` stating the question, search limits, sources read,
tool and procedure used, checks completed, human decisions and unresolved
issues. An exploratory sprint should say how small and selective it was.
Keep raw replies when useful, but make the consequential evidence easy to find.

For peer review, consider what this folder adds to an AI-use disclosure. A
reviewer could follow a claim and assess the correction; they still need to
judge the source and argument. Treat procedural evidence as a proposed way
to support that judgment, rather than a universal publication requirement.

<div class="keypoint" markdown="1">
Give a colleague your files and ask them to explain one revision from the records alone. Add what they needed and could not find.
</div>

## What to take with you
{: .step #takeaways}

<div class="takeaways" markdown="1">
Use these habits in your next research project:

- **Save the research boundaries.** Keep the question, search parameters and inclusion decisions beside the results.
- **Distinguish finding from reading.** Record what you could access before using a source to support a claim.
- **Give notes a procedure.** Preserve the author's argument and the locations that let someone check your interpretation.
- **Check the checker.** Follow consequential criticisms back to the original evidence, including suggestions you reject.
- **Preserve your decisions.** Keep earlier versions and explain why the current conclusion changed.
- **Test the handoff.** Another reader should be able to trace a claim and a correction without your narration.
</div>

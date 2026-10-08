---
layout: reveal-workshop
title: AI as Editorial Assistant
summary: "A 45-minute walkthrough: briefing AI, saving editorial rules, and comparing reader perspectives."
permalink: /presents/editorial-assistant/
tutorial: /sessions/editorial-assistant
---

{::options parse_block_html="true" auto_ids="false" /}

<!-- 20 slides, 44 minutes. The matching full tutorial lives
     at sessions/editorial-assistant.md. Sources and timing are in each note.
     Response labels distinguish illustrations from saved excerpts; provenance is in the notes. -->


<!-- 01 -->
<section id="title" class="workshop-title" data-timing="60" aria-label="AI as editorial assistant">

<header>

Amaranth Brown Bag Series
{: .deck-topic}

# AI as editorial assistant

AI reads. You write.
{: .deck-thesis}

</header>

<div class="deck-summary">

- Brief the reader
- Save your rules and style guide
- Compare different readers

</div>

<div class="deck-decoration" markdown="0"><img class="deck-art" src="{{ '/assets/images/amman-typefounder-1568.jpg' | relative_url }}" alt="" aria-hidden="true"></div>

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**0:00–1:00**

Welcome. Today has the three topics promised on the flyer: teaching the assistant how to read your work, keeping rules and a style guide, and trying different reader perspectives. You can participate by watching and judging the examples. People with a laptop can use the webpage. This is a practice boundary for this session, not a claim that all other uses are wrong.

Cover image: Jost Amman, typefounder, 1568. Existing public-domain workshop image. The Rubric theme and typography follow the Reliable AI site.

</aside>
</section>


<!-- 02 -->
<section id="shared-paragraph" class="workshop-reading" data-timing="120" aria-label="One paragraph we can all judge">

<header>

Shared example
{: .deck-topic}

## One paragraph we can all judge

</header>

<div class="deck-specimen">

Students may use generative AI tools in this course where appropriate, but should not use them to complete assignments for them. Any use of AI should be disclosed. Work that is substantially produced by AI will not receive credit and may be referred as an academic integrity violation. Students are responsible for the accuracy of everything they submit. If you are unsure whether a particular use is permitted, ask before submitting. The goal of this policy is to support learning rather than to prohibit technology, and I expect students to use their judgment.

</div>

What would a student need to know before acting on this?
{: .deck-question}

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**1:00–3:00**

Give the room 30 seconds to read. Ask for one phrase that seems open to interpretation. Do not turn this into a debate over the ideal AI policy. We are examining how an assistant reads a familiar text. The example is invented and makes no claim about university policy. Participants may use their own shareable paragraph instead.

</aside>
</section>


<!-- 03 -->
<section id="baseline" class="workshop-example" data-timing="120" aria-label="Before: a general editing request">

<header>

Teach AI to read like you do
{: .deck-topic}

## Before: a general editing request

</header>

<div class="deck-pair">

<div class="prompt" markdown="0">
  <div class="prompt-head">
    <p class="deck-label">Before · request a clearer policy</p>
    <button class="prompt-copy" type="button" data-prompt-copy aria-label="Copy the displayed prompt"><span class="prompt-copy-text">Copy</span></button>
  </div>
  <pre class="prompt-text"><code>Please edit this syllabus policy for clarity and concision.

Preserve my meaning and tone, and explain any substantive changes.</code></pre>
</div>

<div class="deck-response fragment" data-fragment-index="0">

What this prompt left to the model
{: .deck-label}

<div markdown="0">
<dl class="example-lines">
  <dt>Asked for</dt>
  <dd>Clarity, concision, and my meaning and tone preserved.</dd>
  <dt>Never said</dt>
  <dd>Who has to act on this policy, or which decisions it has to settle for them.</dd>
  <dt>So the model decides</dt>
  <dd>What counts as “appropriate,” and whether disclosure needs a form — the two questions only the author can answer.</dd>
</dl>
</div>

</div>
</div>

Don't ask for subjective decisions.
{: .deck-question .fragment data-fragment-index="0"}

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**3:00–5:00**

Use this as the first half of a before/after prompt comparison. Read the prompt aloud: it is a reasonable editing request that states goals and protects meaning. Then read the right side, which is a reading of the prompt rather than a reply to it — no model output appears on this slide, so there is nothing here to mistake for a transcript.

The point is the third line. A prompt that asks only for clarity and concision has not withheld a decision; it has handed one over. Whatever the model returns, it will have settled what "appropriate" means, because the prompt gave it no way not to. That is the sense in which the request is subjective: not badly worded, but silent on the only questions that matter.

Ask the room which student actions this policy still leaves uncertain, and who ought to be deciding them. Advance to the next slide to make the changed task explicit: ask for a reader diagnosis before requesting an edit. Both slides use the same original policy.

Source prompt: `baseline`. Invented source policy: `practice-texts.md#3-a-syllabus-policy`. Do not pair this prompt with the archived reply to “Edit this.”

</aside>
</section>


<!-- 04 -->
<section id="editorial-brief" class="workshop-example" data-timing="180" aria-label="After: give the reader a specific job">

<header>

Teach AI to read like you do
{: .deck-topic}

## After: give AI a specific job

</header>

<div class="deck-pair">

<div class="prompt" markdown="0">
  <div class="prompt-head">
    <p class="deck-label">After · add audience, concern, and evidence</p>
    <button class="prompt-copy" type="button" data-prompt-copy aria-label="Copy the displayed prompt"><span class="prompt-copy-text">Copy</span></button>
  </div>
  <pre class="prompt-text"><code>This syllabus policy is for first-year students.

Before editing, identify unclear instructions. Focus on disclosure.

Quote the passage, explain what a student cannot do, and name the decision I need to make. Don’t invent a policy.</code></pre>
</div>

<div class="deck-response fragment" data-fragment-index="0">

Illustrative reader report
{: .deck-label}

<div markdown="0">
<dl class="example-lines">
  <dt>Passage</dt>
  <dd>“Any use of AI should be disclosed.”</dd>
  <dt>Reader problem</dt>
  <dd>No location or format for the disclosure is given.</dd>
  <dt>Author’s next step</dt>
  <dd>Choose where the disclosure goes and what it must include; then add that instruction.</dd>
</dl>
</div>

</div>
</div>

The brief produces a passage, a specific problem, and a next step.
{: .deck-question .fragment data-fragment-index="0"}

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**5:00–8:00**

Compare directly with the preceding slide. Point to the three additions on the left: first-year audience, the disclosure concern, and a requested output with a quotation, explanation, and author decision. The task also changes from editing immediately to diagnosing first. Say that explicitly; this is a comparison of workflows, not a controlled experiment in wording alone.

The right side is a prepared illustration, not a transcript or a guarantee about the tool. Its quality gain is visible: the generic uncertainty becomes a located problem with a next action. The assistant can identify the missing procedure without inventing one. Ask the room to supply one possible disclosure arrangement, and note that the author chooses it.

Full prompt ID: `policy-reader-brief`. The longer generic `editorial-brief` prompt and the older `policy-briefed` reply remain in the tutorial. The saved reply is not being presented as a response to this revised prompt.

</aside>
</section>


<!-- 05 -->
<section id="vague-follow-up" class="workshop-example" data-timing="120" aria-label="Before: an open-ended follow-up">

<header>

Teach AI to read like you do
{: .deck-topic}

## Before: an open-ended follow-up

</header>

<div class="deck-pair">

<div class="prompt" markdown="0">
  <div class="prompt-head">
    <p class="deck-label">Before · invite additional advice</p>
    <button class="prompt-copy" type="button" data-prompt-copy aria-label="Copy the displayed prompt"><span class="prompt-copy-text">Copy</span></button>
  </div>
  <pre class="prompt-text"><code>Anything else I should worry about?</code></pre>
</div>

<div class="deck-response fragment" data-fragment-index="0">

Response excerpt
{: .deck-label}

> The tone is generally supportive, but the policy could do more to convey the pedagogical rationale behind these restrictions. Students respond better to guidelines when they understand the reasoning […]

</div>
</div>

This gives teaching advice without establishing a problem in the text.
{: .deck-question .fragment data-fragment-index="0"}

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**8:00–10:00**

This begins a separate before/after pair from the saved policy conversation. It is not a continuation of the illustrated reply on the previous slide. Read the actual open-ended follow-up and its response excerpt. Ask which statement describes the paragraph and which makes a general claim about teaching. The paragraph already says that the policy aims to support learning.

The next slide asks the assistant to identify the textual basis for its comment. Preserve the difference between a useful suggestion and a finding supported by the supplied text.

Source ID: `policy-vague`. The source file attributes this reply to Claude Opus 5 on September 22, 2026, in the workshop-authoring conversation; that attribution has not been independently verified. Earlier discussion of the intended lesson is part of its context. This saved example is not a fresh independent run. The excerpt follows the source order and marks its cut with […]. Full follow-up prompt: `policy-open-followup`.

</aside>
</section>

<!-- 06 -->
<section id="check-the-finding" class="workshop-example" data-timing="180" aria-label="After: require evidence for the comment">

<header>

Teach AI to read like you do
{: .deck-topic}

## After: require evidence for the comment

</header>

<div class="deck-pair">

<div class="prompt" markdown="0">
  <div class="prompt-head">
    <p class="deck-label">After · ask which words support the claim</p>
    <button class="prompt-copy" type="button" data-prompt-copy aria-label="Copy the displayed prompt"><span class="prompt-copy-text">Copy</span></button>
  </div>
  <pre class="prompt-text"><code>Quote the exact words that made you say that. If you can’t point to specific text, say so instead of explaining further.</code></pre>
</div>

<div class="deck-response fragment" data-fragment-index="0">

Response excerpt
{: .deck-label}

> “Students respond better to guidelines when they understand the reasoning” is a general belief about teaching, not something I read in your text.

</div>
</div>

The follow-up separates a finding about the text from general advice.
{: .deck-question .fragment data-fragment-index="0"}

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**10:00–13:00**

This is the actual follow-up to the comment on the preceding slide. Read the two outputs back to back. The response now acknowledges that the teaching claim came from outside the paragraph. The gain is a narrower, more accountable answer, not a longer or more confident one.

A missing feature can still be a legitimate concern; ask what stated purpose or criterion requires it. A quotation also does not automatically make a criticism correct. Ask participants whether they would retain the general advice, reject it, or treat it as a separate question.

Source IDs: `quote-it`, `policy-vague`, `policy-quoted`. The quoted sentence is extracted without rewording from `policy-quoted`; the surrounding reply is omitted. The source attributes the reply to Claude Opus 5 on September 22, 2026, in the workshop-authoring conversation. This attribution has not been independently verified and prior teaching context may have shaped the answer. Dates and provenance are retained here and in `_data/demos.yml`.

</aside>
</section>


<!-- 07 -->
<section id="standing-rules" class="workshop-example" data-timing="180" aria-label="Before: edit the report for clarity">

<header>

Set up rules and style guides
{: .deck-topic}

## Before: edit the report for clarity

</header>

<div class="deck-pair">

<div class="prompt" markdown="0">
  <div class="prompt-head">
    <p class="deck-label">Before · a general prose-editing request</p>
    <button class="prompt-copy" type="button" data-prompt-copy aria-label="Copy the displayed prompt"><span class="prompt-copy-text">Copy</span></button>
  </div>
  <pre class="prompt-text"><code>Edit this community archive report for clarity and concision.

Preserve its meaning and voice. Explain the changes.</code></pre>
</div>

<div class="deck-response fragment" data-fragment-index="0">

Illustrative edit · report paragraph 2
{: .deck-label}

<div markdown="0">
<dl class="example-lines example-lines--tight">
  <dt>What the edit changed</dt>
  <dd class="edit-pair">
    <span class="edit-tag">was</span>
    <span class="edit-was">“The implementation of a common description template has facilitated the comparison of records by contributors.”</span>
    <span class="edit-tag">now</span>
    <span class="edit-now">“A common description template has made it easier for contributors to compare records.”</span>
  </dd>
  <dt>What it left alone, two sentences later</dt>
  <dd class="edit-clash">
    <span>“Final decisions about descriptions are made by the project team.”</span>
    <span>“…community members retain control.”</span>
  </dd>
</dl>
</div>

</div>
</div>

A sentence can become clearer while a claim still needs attention.
{: .deck-question .fragment data-fragment-index="0"}

<footer class="deck-source">

[Report and guide]({{ site.baseurl }}/practice-texts#community-archive)

</footer>

<aside class="notes">

**13:00–16:00**

Introduce the four-paragraph community archive report: a fictional project explaining its pilot to contributors and university colleagues. The complete passage is on the webpage. Everything the room needs for this slide is on it.

Read the top block first. The original sentence is genuinely bad — a noun phrase doing the work of a verb — and the revision is genuinely better: shorter, same actor, same outcome, nothing added. Say that plainly, because the argument of this slide depends on conceding that the broad prompt did something useful.

Then read the bottom block aloud, both clauses, and let the room sit with them. They are two sentences apart in the same paragraph. The project team makes the final call; the contributors are said to retain control. Those can both be true, but only if someone says how, and the report does not. Do not call it a proved contradiction — the author may well be able to explain it.

The point is the gap between the two blocks. A request for clarity and concision operates on sentences, and this one improved a sentence. The thing most worth an editor's attention in that paragraph is not a sentence at all; it is a relationship between two claims, and no amount of tightening prose will surface it. The next slide supplies criteria that do.

This is a prepared teaching comparison, not an AI transcript or a claim that every broad prompt misses the issue. Prompt ID: `archive-general-edit`. Full report and guide: `practice-texts.md#community-archive`.

</aside>
</section>


<!-- 08 -->
<section id="checkable-rules" class="workshop-example" data-timing="120" aria-label="After: define what clarity must preserve">

<header>

Set up rules and style guides
{: .deck-topic}

## After: define what clarity must preserve

</header>

<div class="deck-pair">

<div class="prompt" markdown="0">
  <div class="prompt-head">
    <p class="deck-label">After · apply the report’s style guide</p>
    <button class="prompt-copy" type="button" data-prompt-copy aria-label="Copy the displayed prompt"><span class="prompt-copy-text">Copy</span></button>
  </div>
  <pre class="prompt-text"><code>Use my report guide: preserve evidence and uncertainty; keep access and control distinct; make decision-making clear.

Quote a passage to keep and a claim that needs my decision. Explain which rule applies. Don’t settle the decision for me.</code></pre>
</div>

<div class="deck-response fragment" data-fragment-index="0">

Illustrative review against the guide
{: .deck-label}

<div markdown="0">
<dl class="example-lines">
  <dt>Keep the qualification</dt>
  <dd>“The limited response may reflect…” The evidence cannot yet distinguish the possible causes.</dd>
  <dt>Flag the claim about control</dt>
  <dd>The team has the final say. The author needs to define which decisions contributors control.</dd>
</dl>
</div>

</div>
</div>

The guide gives reasons to preserve wording and question a claim.
{: .deck-question .fragment data-fragment-index="0"}

<footer class="deck-source">

[Report and guide]({{ site.baseurl }}/practice-texts#community-archive)

</footer>

<aside class="notes">

**16:00–18:00**

Compare with the previous slide. The prompt now supplies criteria that go beyond concision: preserve the limits of evidence, distinguish access from control, and identify decision-making authority. The same report supports both observations on the right. Read the full paragraph 3 sentence if needed; it lists several possible reasons for low participation and explicitly says the project cannot yet distinguish them.

The guide changes what counts as a useful edit. Retaining “may reflect” is a positive editorial choice. Replacing “control” with “input” would silently weaken the report's claim; asking the author to define the relationship preserves that choice. The local wording improvement on the previous slide is still acceptable. The gain is clearer criteria, not a demand to find more faults.

The displayed prompt is a shortened version of `archive-style-review`. Both right-hand examples are illustrations prepared for teaching. Full report and five-rule guide: `practice-texts.md#community-archive`. The webpage retains the additional `archive-style-edit` follow-up for making a chosen local edit.

</aside>
</section>


<!-- 09 -->
<section id="campus-history-project" class="workshop-summary" data-timing="120" aria-label="The UNM Campus Histories collection">

<header>

Set up rules and style guides
{: .deck-topic}

## A real collection, still being added to

</header>

<div class="deck-summary">

[amaranth.unm.edu/campus-history](https://amaranth.unm.edu/campus-history/){: target="_blank" rel="noopener"}
{: .deck-url}

- Student-authored essays on the buildings, landscapes, public art, and everyday places of the UNM campus
- Written for a course, published as a public archive, added to each semester
- Every essay is some student's first encounter with the site's conventions

</div>

Open it and pick an essay before we look at twenty.
{: .deck-question}

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**18:00–20:00**

Put the site on screen and browse for a minute rather than describing it. Open one essay — Hodgin Hall or the Duck Pond both work — and scroll it. This is the only part of the session that uses a live public collection rather than a prepared specimen, and it is worth the minute because everything in the next three slides is about a problem the room can see for itself.

Say what the project is: students in a Making History course research a campus place in the archives and publish the essay here, and the collection has grown each semester since. Nobody is editing this for a grade. It is a public archive with the students' names on it.

Then say the editorial situation plainly. Each essay arrives from a different student, written at a different time, with different ideas about headings, images, and citations, and all of them land in one collection that has to read as one thing. Nobody has time to hold twenty separate conversations about heading levels. That is the condition a style guide exists for, and the next slide shows what it looks like when there isn't one.

Link opens in a new tab so the deck keeps its place. Site checked September 23, 2026.

</aside>
</section>


<!-- 10 -->
<section id="collection-variations" class="workshop-example" data-timing="120" aria-label="The same template filled in three different ways">

<header>

Set up rules and style guides
{: .deck-topic}

## One template, three conventions

</header>

<div markdown="0">
<div class="deck-mockups">

  <div>
    <div class="deck-mock">
      <div class="deck-mock-hero">
        <p class="deck-mock-eyebrow">Campus History</p>
        <p class="deck-mock-title">Popejoy Hall</p>
      </div>
      <div class="deck-mock-body">
        <p class="deck-mock-h1">Popejoy Hall</p>
        <span class="deck-mock-line"></span>
        <span class="deck-mock-line"></span>
        <span class="deck-mock-line is-short"></span>
        <span class="deck-mock-gap"></span>
        <p class="deck-mock-bold">Sources</p>
        <p class="deck-mock-run">Nash, “Building the Fine Arts Center,” 1966, https://econtent.unm.edu/…; UNM Archives, Box 4, folder 11.</p>
      </div>
    </div>
    <p class="deck-mock-note">Title repeated under the header; sources run together in one paragraph</p>
  </div>

  <div>
    <div class="deck-mock">
      <div class="deck-mock-hero">
        <p class="deck-mock-eyebrow">Campus History</p>
        <p class="deck-mock-title">Zimmerman Library</p>
      </div>
      <div class="deck-mock-body">
        <span class="deck-mock-img"></span>
        <p class="deck-mock-h2">Early Construction</p>
        <span class="deck-mock-line"></span>
        <span class="deck-mock-line"></span>
        <span class="deck-mock-line"></span>
        <span class="deck-mock-line is-short"></span>
      </div>
    </div>
    <p class="deck-mock-note">Opens on an image, so the reader meets the essay with no orientation</p>
  </div>

  <div>
    <div class="deck-mock">
      <div class="deck-mock-hero">
        <p class="deck-mock-eyebrow">Dormitory</p>
        <p class="deck-mock-title">Mesa Vista Hall</p>
      </div>
      <div class="deck-mock-body">
        <span class="deck-mock-line"></span>
        <span class="deck-mock-line"></span>
        <span class="deck-mock-line is-short"></span>
        <span class="deck-mock-gap"></span>
        <p class="deck-mock-bold">A New Dormitory</p>
        <span class="deck-mock-line"></span>
        <span class="deck-mock-line"></span>
        <span class="deck-mock-line is-short"></span>
      </div>
    </div>
    <p class="deck-mock-note">Bold text standing in for a heading, so it never enters the outline</p>
  </div>

</div>
</div>

Not one of these is a mistake. That is what makes it a style problem.
{: .deck-question}

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**20:00–22:00**

Three student essays from the same collection, built from the same template, each solving the same layout question differently. Say out loud that these are mockups drawn for this slide, not screenshots of anyone's page.

Work left to right and let the room name the differences before you do. The first repeats its title under the header and runs its sources together as prose. The second opens on a photograph, so a reader arrives with no idea what the essay argues. The third uses bold text where a heading belongs, which looks right and is invisible to the table of contents, to search, and to a screen reader. Only the third page has a real category in its eyebrow; the other two fall back to the generic site label.

The point to land before advancing: no student did anything wrong. Each made a reasonable local choice in the absence of a stated one. Twenty essays of reasonable local choices is what a collection looks like without a guide — and it is why the fix is a written rule rather than twenty conversations.

The pages are invented. The inconsistencies are the real ones the Campus History guide was written to settle.

</aside>
</section>


<!-- 11 -->
<section id="guide-file" class="workshop-example workshop-file" data-timing="120" aria-label="The style guide as a plain text file">

<header>

Set up rules and style guides
{: .deck-topic}

## The guide is a file you can read

</header>

<div markdown="0">
<div class="deck-editor">
  <div class="deck-editor-bar">
    <span class="deck-editor-dot"></span>
    <span class="deck-editor-dot"></span>
    <span class="deck-editor-dot"></span>
    <span class="deck-editor-name">ESSAY-STYLE-GUIDE.md — campus-history</span>
  </div>
  <div class="deck-editor-body">
<pre class="deck-editor-gutter">  11
  12
  13
  14
  15
   ⋮
  81
  82
  83
  84
  85
   ⋮
  90
  91
  92
  93
  94
   ⋮
 104</pre>
<pre class="deck-editor-code"><span class="tok-head">## Allowed Changes</span>

<span class="tok-mark">-</span> Fix Markdown formatting.
<span class="tok-mark">-</span> Break up very long paragraphs into shorter units appropriate for online reading, …
<span class="tok-mark">-</span> Normalize heading levels, usually <span class="tok-code">`##`</span> for major sections and <span class="tok-code">`###`</span> for subsections.

<span class="tok-head">## Avoid</span>

<span class="tok-mark">-</span> Do not rewrite thesis statements or major claims.
<span class="tok-mark">-</span> Do not add new evidence, interpretation, or scholarly framing.
<span class="tok-mark">-</span> Do not substantially reorder the argument.

<span class="tok-head">## Flag Or Ask First</span>

Ask before making a change when you encounter a nonstandard, unusual, or ambiguous issue. This includes:

<span class="tok-mark">-</span> A factual claim that seems wrong but is not simply a typo.

When in doubt, preserve the original text and leave a note or ask for direction.</pre>
  </div>
</div>
</div>

Rules you can point at, argue with, and change.
{: .deck-question}

<footer class="deck-source">

[Guide and exercise]({{ site.baseurl }}/examples/campus-history-style-guide/)

</footer>

<aside class="notes">

**22:00–24:00**

This is the real file, open in an editor, with its real line numbers; the trailing ellipses mark lines trimmed to fit this slide, not lines that end there. Nothing here is generated. Someone sat down and wrote it after seeing the pages on the previous slide.

Read the three section headings first, because the shape is the lesson: Allowed Changes, Avoid, Flag Or Ask First. Most people writing a style guide write only the first one. The second is what keeps an assistant from improving a student's argument out from under them, and the third is the one nobody thinks to include — the list of things it must stop and ask about rather than decide.

Then point at the writing itself. It is Markdown in a text file: no app, no account, no format anyone has to be taught. And every line is checkable against an actual page. "Normalize heading levels" and "do not add new evidence" can be held up against an essay and answered yes or no, where "make it professional" cannot. That is the whole craft of writing one of these.

Line 104 is the one to read aloud: when in doubt, preserve the original text and leave a note or ask for direction. That single sentence is what makes the difference between an assistant and a ghostwriter.

Say that the guide grew from the problems, not from a template. That is also the advice for the room: do not open a blank file and try to write a style sheet. Fix three essays, notice what you keep deciding, and write those decisions down.

Excerpt from lines 11–15, 81–85, 90–94, and 104. Source: https://github.com/amaranth-unm/campus-history/blob/master/ESSAY-STYLE-GUIDE.md (public and local versions matched September 23, 2026). Workshop copy: `/assets/documents/campus-history-essay-style-guide.txt`.

</aside>
</section>


<!-- 12 -->
<section id="campus-history-guide" class="workshop-example" data-timing="180" aria-label="One editorial guide across semesters">

<header>

Set up rules and style guides
{: .deck-topic}

## One editorial guide across semesters

</header>

<div class="deck-pair">

<div class="prompt" markdown="0">
  <div class="prompt-head">
    <p class="deck-label">Prompt with the actual collection guide</p>
    <button class="prompt-copy" type="button" data-prompt-copy aria-label="Copy the displayed prompt"><span class="prompt-copy-text">Copy</span></button>
  </div>
  <pre class="prompt-text"><code>Use my Campus History Essay Style Guide on this essay.

Propose formatting and light prose edits. Name the rule behind each change.

Preserve the student’s argument, voice, and uncertainty. Flag missing sources and changes to meaning. Ask if guide rules conflict.</code></pre>
</div>

<div class="deck-response fragment" data-fragment-index="0">

Illustrative edits · one essay, with the rule behind each
{: .deck-label}

<div markdown="0">
<dl class="example-lines example-lines--tight">
  <dt>Headings use heading syntax</dt>
  <dd class="edit-pair">
    <span class="edit-tag">was</span>
    <span class="edit-was"><code>**A New Dormitory**</code></span>
    <span class="edit-tag">now</span>
    <span class="edit-now"><code>## A New Dormitory</code></span>
  </dd>
  <dt>The title belongs in the front matter, not under the header</dt>
  <dd class="edit-pair">
    <span class="edit-tag">was</span>
    <span class="edit-was"><code>&#35; Popejoy Hall</code> as the first line of the essay</span>
    <span class="edit-tag">now</span>
    <span class="edit-now"><code>header-title: Popejoy Hall</code></span>
  </dd>
  <dt>Assignment scaffolding comes out; the voice stays</dt>
  <dd class="edit-pair">
    <span class="edit-tag">was</span>
    <span class="edit-was">“In conclusion, the letters suggest…”</span>
    <span class="edit-tag">now</span>
    <span class="edit-now">“The letters suggest…”</span>
  </dd>
</dl>
</div>

</div>
</div>

Which decisions should carry into the next semester?
{: .deck-question .fragment data-fragment-index="0"}

<footer class="deck-source">

[Guide and exercise]({{ site.baseurl }}/examples/campus-history-style-guide/)

</footer>

<aside class="notes">

**24:00–27:00**

This is the actual Campus History Essay Style Guide, not Amaranth's general language guide. The prompt on the left asks it to name the rule behind each change, and the panel on the right is what that produces: three edits, each traceable to a line in the file we just looked at. The edits are illustrative, written for this slide; the rules behind them are real.

Two of the three should look familiar — they are the first and third mockups from the collection slide, now fixed. Say so. The room has seen the problem, the file, and now the change, and that is the whole argument for writing one of these down.

Note what the third edit does not do. The guide permits cutting "In conclusion," and in the same breath protects meaningful first person and justified uncertainty. A guide that only standardizes would flatten the collection into one voice; this one spends rules preventing that.

Then the maintenance point, which this slide can demonstrate rather than assert. The second edit writes the title into `header-title`, and the guide contradicts itself on that field: one rule says `header-title`, another says `image-title`. An assistant working from this file should stop and ask which is right, not quietly pick one. A style guide is a document with bugs in it like any other. The source guide and essays have not been changed for this workshop.

Source: https://github.com/amaranth-unm/campus-history/blob/master/ESSAY-STYLE-GUIDE.md (public and local versions matched September 23, 2026). Full prompt: `campus-history-normalize`. Workshop copy: `/assets/documents/campus-history-essay-style-guide.txt`.

</aside>
</section>

<!-- 13 -->
<section id="where-the-guide-lives" class="workshop-summary" data-timing="120" aria-label="Where the style guide actually lives">

<header>

Set up rules and style guides
{: .deck-topic}

## Where the guide actually lives

</header>

<div class="deck-summary">

<div markdown="0">
<dl>
  <dt>Paste it at the top</dt>
  <dd>A plain text file, pasted into your first message. Works in every tool, on every free tier, and depends on nothing.</dd>
  <dt>Attach the file</dt>
  <dd>Most tools take a <code>.txt</code> or <code>.md</code> upload. Same guide, less scrolling — but ask it to quote a rule back before you trust that it read one.</dd>
  <dt>Give it a standing place</dt>
  <dd>A Project in Claude, custom instructions or a custom GPT in ChatGPT, a Gem in Gemini: the guide then applies to every conversation inside it.</dd>
</dl>
</div>

</div>

Start with the text file. Upgrade later, or never.
{: .deck-question}

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**27:00–29:00**

The previous slide showed a prompt that begins "Use my Campus History Essay Style Guide" without saying how the assistant ever sees it. This slide answers that, because it is the first thing anyone following along on a laptop will get stuck on.

Lead with the plain file and mean it. A guide pasted into the first message works in every tool, costs nothing, and survives your changing tools next year — which the other two options do not. The standing place is a convenience for people already paying for one, not a prerequisite for anything in this session.

Two cautions worth saying aloud. Attaching a file is not the same as having it read: ask the assistant to quote one rule back before relying on it. And a Project's memory is a liability as well as a convenience — the limits from the start of the session still apply to what you put in one. Other people's unpublished work, student writing with names attached, and anything under embargo or an IRB protocol do not belong in a standing place any more than in a chat window.

The tutorial covers this at greater length under "Where to keep it" and "Keep the draft in a file."

</aside>
</section>

<!-- 14 -->
<section id="cv-formatting" class="workshop-example" data-timing="180" aria-label="A CV audit catches several kinds of inconsistency">

<header>

Set up rules and style guides
{: .deck-topic}

## A CV audit catches several kinds of inconsistency

</header>

<div class="deck-pair">

<div class="prompt" markdown="0">
  <div class="prompt-head">
    <p class="deck-label">Expanded Alexandra Ruiz Word specimen</p>
    <button class="prompt-copy" type="button" data-prompt-copy aria-label="Copy the displayed prompt"><span class="prompt-copy-text">Copy</span></button>
  </div>
  <pre class="prompt-text"><code>Audit this CV before editing it.

Separate formatting inconsistencies, questions for the author, and Word structures you can actually inspect.

Quote examples and explain why they matter. Preserve names, dates, and publication statuses. Propose rules before making changes.</code></pre>
</div>

<div class="deck-response fragment" data-fragment-index="0">

Fictional CV · audit examples
{: .deck-label}

<div markdown="0">
<dl class="example-lines">
  <dt>Visible detail</dt>
  <dd>One date range uses a hyphen; comparable ranges use en dashes.</dd>
  <dt>Hidden structure</dt>
  <dd>Only the oldest talks sit inside a borderless table.</dd>
  <dt>Author decision</dt>
  <dd>One article appears as both “Forthcoming” and “Article in preparation.”</dd>
</dl>
</div>

</div>
</div>

Which finding is a formatting fix, and which needs a decision?
{: .deck-question .fragment data-fragment-index="0"}

<footer class="deck-source">

[Exercise]({{ site.baseurl }}/examples/cv-audit/) · [Download Word CV]({{ site.baseurl }}/assets/documents/alexandra-ruiz-cv-workshop.docx)

</footer>

<aside class="notes">

**29:00–32:00**

The expanded four-page Alexandra Ruiz specimen is designed to look ordinary while containing subtle text inconsistencies and inherited Word structures. These three findings were verified when the document was constructed; they are not claimed as output from a model run. Use the separate audit prompts in workshop-drafts/editorial-assistant/cv-audit/prompts.md. Do not supply the instructor key to the model.

A text-only extraction may expose the date and publication-status issues while missing the table structure. Ask the assistant what it actually inspected. A borderless table is not automatically wrong; the useful finding is that comparable entries behave differently during editing. Preserve facts and ask about the status conflict. The original specimen remains unchanged. Its source is https://xanthan-web.github.io/alexandra-ruiz/cv, expanded with fictional entries for the workshop.

</aside>
</section>


<!-- 15 -->
<section id="student-reader" class="workshop-example" data-timing="120" aria-label="The assignment as a student reads it">

<header>

Role-play as different readers
{: .deck-topic}

## The assignment as a student reads it

</header>

<div class="deck-pair">

<div class="prompt" markdown="0">
  <div class="prompt-head">
    <p class="deck-label">Campus History Part 2; shortened student prompt</p>
    <button class="prompt-copy" type="button" data-prompt-copy aria-label="Copy the displayed prompt"><span class="prompt-copy-text">Copy</span></button>
  </div>
  <pre class="prompt-text"><code>Read this Making History assignment as a first-year student.

What would I do first? What must I submit? How would I check my work?

Quote the instructions. Identify where I would have to guess. Use only the supplied materials. Don’t rewrite the assignment.</code></pre>
</div>

<div class="deck-response fragment" data-fragment-index="0">

Illustrative student reading
{: .deck-label}

<div markdown="0">
<dl class="example-lines">
  <dt>What I can act on</dt>
  <dd>Visit the archive. Write about 800–1000 words with 4–5 images, captions, and sources.</dd>
  <dt>What I would ask</dt>
  <dd>The grading section expects an “AI-Archive Comparison.” Does it belong in the public essay or a separate reflection? Does it count toward the word target?</dd>
</dl>
</div>

</div>
</div>

Which question would you want students to ask before starting?
{: .deck-question .fragment data-fragment-index="0"}

<footer class="deck-source">

[Assignment and prompts]({{ site.baseurl }}/examples/assignment-review/)

</footer>

<aside class="notes">

**32:00–34:00**

Introduce the real assignment: students first critique an AI draft, then visit the Center for Southwest Research and build a Campus History essay from archival evidence. The full assignment is linked, with a stable workshop text copy. Do not put the whole assignment on a slide. The practical question comes from comparing the Requirements list with What I'm looking for. The instructions specify the essay length and images; grading names an AI-Archive Comparison but the requirements do not state its location or relationship to the word target.

This is a prepared reading, not an observed AI response or a claim about what actual students think. Another course document or class discussion may answer the question. Invite students to explain the task back to the instructor rather than treating a simulated reader as a substitute for them.

Source: https://fredgibbs.net/courses/making-history/campus-history-human (checked September 23, 2026). Full prompt: `assignment-student`.

</aside>
</section>


<!-- 16 -->
<section id="outsider-reader" class="workshop-example" data-timing="120" aria-label="The assignment as a designer reads it">

<header>

Role-play as different readers
{: .deck-topic}

## The assignment as a designer reads it

</header>

<div class="deck-pair">

<div class="prompt" markdown="0">
  <div class="prompt-head">
    <p class="deck-label">TILT review; shortened designer prompt</p>
    <button class="prompt-copy" type="button" data-prompt-copy aria-label="Copy the displayed prompt"><span class="prompt-copy-text">Copy</span></button>
  </div>
  <pre class="prompt-text"><code>Use transparent assignment design: purpose, task, and criteria.

Quote what is clear or partly explained. Is each graded component introduced in the instructions?

Recognize strengths. Ask for context. Don’t invent requirements or rewrite.</code></pre>
</div>

<div class="deck-response fragment" data-fragment-index="0">

Illustrative design review
{: .deck-label}

<div markdown="0">
<dl class="example-lines">
  <dt>Purpose</dt>
  <dd>The skills section explains what students practice.</dd>
  <dt>Task</dt>
  <dd>The archive visit and essay requirements give a workable sequence.</dd>
  <dt>Criteria</dt>
  <dd>The grading section describes strong work. The comparison’s place in the submission still needs clarification.</dd>
</dl>
</div>

</div>
</div>

Do the instructions and grading criteria describe the same work?
{: .deck-question .fragment data-fragment-index="0"}

<footer class="deck-source">

[Sources and exercise]({{ site.baseurl }}/examples/assignment-review/)

</footer>

<aside class="notes">

**34:00–36:00**

Use the same complete assignment and supplied context as the student reading, in a separate conversation. The purpose/task/criteria framework comes from TILT. The point is to check whether students can understand the learning purpose, required actions, and characteristics of successful work. Recognize the assignment's existing strengths. It already states skills, gives archive logistics, and distinguishes stronger from weaker submissions. Do not describe it as having no criteria, or treat the absence of a literal Purpose heading as a failure.

The particular alignment issue is that the AI-Archive Comparison appears in grading without a clear location in the submission instructions. Ask the instructor to decide how that work should be submitted. TILT emphasizes students' understanding; AI inspection can suggest questions, but actual student feedback remains necessary.

Assignment: https://fredgibbs.net/courses/making-history/campus-history-human
Framework: https://www.tilthighered.org/resources
Checklist: https://www.tilthighered.com/assets/pdffiles/Checklist%20for%20Designing%20Transparent%20Assignments.pdf
Flexible use and student understanding: https://www.tilthighered.org/faq
Full prompt: `assignment-designer`. This slide contains prepared analysis, not a recorded model reply.

</aside>
</section>


<!-- 17 -->
<section id="compare-readers" class="workshop-example" data-timing="120" aria-label="Compare the questions the two readers raise">

<header>

Role-play as different readers
{: .deck-topic}

## Compare the questions the two readers raise

</header>

<div class="deck-pair">

<div class="prompt" markdown="0">
  <div class="prompt-head">
    <p class="deck-label">Comparison prompt, shortened</p>
    <button class="prompt-copy" type="button" data-prompt-copy aria-label="Copy the displayed prompt"><span class="prompt-copy-text">Copy</span></button>
  </div>
  <pre class="prompt-text"><code>Compare the student and designer readings. Check each claim against the assignment.

Where does a practical uncertainty point to a design issue? Where do the readings differ?

Recommend one clarification, then name the decision the instructor still needs to make.</code></pre>
</div>

<div class="deck-response fragment" data-fragment-index="0">

Illustrative comparison
{: .deck-label}

<div markdown="0">
<dl class="example-lines">
  <dt>Student question</dt>
  <dd>Where does the AI-Archive Comparison go?</dd>
  <dt>Design question</dt>
  <dd>Is every graded component explained in the task instructions?</dd>
  <dt>Instructor decision</dt>
  <dd>Choose its location and relationship to the word target, then clarify the instructions.</dd>
</dl>
</div>

</div>
</div>

Does their agreement identify evidence, or just repeat an assumption?
{: .deck-question .fragment data-fragment-index="0"}

<footer class="deck-source">

[Full exercise]({{ site.baseurl }}/examples/assignment-review/)

</footer>

<aside class="notes">

**36:00–38:00**

Both perspectives point to one actionable clarification. That connection is useful because it links a reader's practical question to a design principle. It is not independent corroboration: two generated roles can share assumptions or copy one another's framing. Preserve the source assignment and inspect the cited passages before acting. Do not make the comparison decide whether the instructor should require a separate reflection; that is a pedagogical choice.

The broader technique is to change the reading lens while holding the material steady, then compare the questions rather than counting votes. The longer tutorial retains the syllabus-policy reader comparisons as another example. Full prompt: `assignment-compare`. Prepared analysis of the Making History assignment; no model transcript is claimed.

</aside>
</section>


<!-- 18 -->
<section id="word-comments" class="workshop-example" data-timing="180" aria-label="Reader comments can stay beside the passage">

<header>

Application in Word
{: .deck-topic}

## Reader comments can stay beside the passage

</header>

<div class="deck-pair">

<div class="prompt" markdown="0">
  <div class="prompt-head">
    <p class="deck-label">Document-comment prompt, shortened</p>
    <button class="prompt-copy" type="button" data-prompt-copy aria-label="Copy the displayed prompt"><span class="prompt-copy-text">Copy</span></button>
  </div>
  <pre class="prompt-text"><code>Read as a student encountering this text.
Add comments at confusing passages.
Explain what is unclear and ask a question.
Keep all text and formatting unchanged.
Return a copy with comments.</code></pre>
</div>

<div class="deck-response fragment" data-fragment-index="0">

Illustrative Word comment
{: .deck-label}

<div markdown="0">
<dl class="example-lines">
  <dt>Passage in the document</dt>
  <dd><p>“Any use of AI should be disclosed.”</p></dd>
  <dt>Reader comment</dt>
  <dd><p>I don’t know how to disclose my use. Should I add a note to the assignment, send an email, or use another method?</p></dd>
</dl>
</div>

</div>
</div>

Does the comment help the author make a decision?
{: .deck-question .fragment data-fragment-index="0"}

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**38:00–41:00**

Explain the requested artifact: a copy of the document whose original text is intact and whose comments attach to exact phrases. The prepared annotation shows the desired form. Do not claim that every assistant or free tier can create native Word comments. Test the intended tool with a non-sensitive copy first. If it can only return text, a passage/comment table preserves the reading workflow. The user should inspect each comment and make their own revision. This slide illustrates a proposed demonstration; it does not document a completed live product run.

### Full prompt

```text
Read the attached document as a first-time student reader. Add comments anchored to the exact passages that confuse you.

Describe the uncertainty and ask a question for the author. Preserve the text and formatting. Return a copy with comments.

If you can’t add Word comments, return a passage/comment table.
```

</aside>
</section>




<!-- 19 -->
<section id="takeaways" class="workshop-summary" data-timing="120" aria-label="Five techniques to take with you">

<header>

Take-home techniques
{: .deck-topic}

## Five techniques to take with you

</header>

<div class="deck-summary">

- **Brief the task.** Name the audience, purpose, and limits.
- **Ask for evidence.** Request a passage and the rule behind a finding.
- **Compare perspectives.** Keep the text fixed; change the reader.
- **Save your decisions.** Turn useful corrections into reusable rules.
- **Work in passes.** Diagnose, choose an edit, then inspect the result.

</div>

Which technique could you use on a real task this week?
{: .deck-question}

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**41:00–43:00**

Connect each technique to a concrete example instead of introducing more theory. The policy brief supplied purpose and limits. The assignment review tied a question to the text and to a design criterion. The student and designer perspectives exposed different kinds of uncertainty. The Campus History guide carried accepted editorial decisions across semesters. The CV separated diagnosis from changes and showed why verification depends on what the tool can inspect.

These techniques transfer to a syllabus, grant abstract, policy, report, or shared collection. Ask each participant to choose one technique and a real task for this week. Their first experiment can be small: one passage, two perspectives, or one reusable rule. The durable outcome is a way to ask and check, not a memorized prompt. Keep a copy of the original and inspect any proposed changes before adopting them.

</aside>
</section>


<!-- 20 -->
<section id="resources" class="workshop-summary" data-timing="60" aria-label="The webpage is the full walkthrough">

<header>

Continue at your own pace
{: .deck-topic}

## The webpage is the full walkthrough

</header>

<div class="deck-summary">

[amaranth.unm.edu/reliable-ai]({{ '/' | relative_url }})
{: .deck-url}

- The complete sequence
- Copyable prompts
- Practice texts
- More rules and reader roles to try

</div>

<div class="deck-question" aria-hidden="true" markdown="0"></div>

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**43:00–44:00**

The webpage is the durable tutorial for people who missed the session or want to go farther. The slide sequence highlights selected prompts and need not reproduce the full tutorial. The linked assignment and Campus History exercises include full prompts and source snapshots. The CV specimen is downloadable from its slide; the presenter guide links the detailed audit and Word-commenting prompts. Prepared examples still need recorded runs in the tool selected for the workshop.

</aside>
</section>



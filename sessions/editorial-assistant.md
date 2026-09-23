---
title: AI as Editorial Assistant
layout: base
position: 1
date: 2026-09-23
kicker: Session 1 · September 23, 2026
summary: "Treat AI as an eager but naive editor: teach it what to look for, tell it whose eyes to read with, and write down the rules so you don't have to repeat yourself."
thumbnail: "/assets/images/amman-typefounder-1568.jpg"
header-image: "/assets/images/amman-typefounder-1568.jpg"
header-tier: section
header-filter: etching
header-title: AI as Editorial Assistant
header-subtitle: "Use AI as a reader whose comments you can check. Give it your editorial rules, then decide which findings deserve a revision."
tags:
  - editing
  - prompting
  - getting started
workshop_mode: true
---

{% include nav/scrollspy-toc.html %}

[View the presentation slides]({{ site.baseurl }}/presents/editorial-assistant/). This page is the complete tutorial, with prompts and additional exercises to work through at your own pace.
{: .lead}

<div class="rule" markdown="1">
**AI reads. You write.**
</div>

## Why editing is the place to start

Most people meet these tools by asking for something they can't check — a summary of a literature they haven't read, a draft in an unfamiliar genre. You can't tell a good answer from a merely plausible one, so you either trust it or you don't.

Editing gives you something concrete to check. **You know what you intended your paragraph to say.** You can compare a comment or proposed edit with the original and decide whether it helps. Start by asking AI to read; choose any revisions after examining its reasons.

## What you're working with

You do not need a theory of how a model works to examine its comments.
Practice four habits with the text in front of you:

- **Supply the context.** Give the current draft, audience, and purpose;
  do not assume the assistant knows which version or instructions to use.
- **Check the evidence.** Fluent criticism still needs a passage you can
  inspect. For an omission, ask what requirement makes it matter.
- **Ask a specific question.** A request to identify an unclear instruction
  gives you more to evaluate than a request for general approval.
- **Compare readings.** Different roles can surface different questions.
  Treat them as possibilities to check, not independent human testimony.

## Before you start

- **A laptop**, and an AI assistant open in a browser tab — Claude, ChatGPT, Gemini, Copilot, any of them, free account is fine.
- **One paragraph of your own writing** — a draft, an abstract, a policy, a grant blurb. Real stakes work better than invented ones. No paragraph? Take one from the [practice texts]({{ site.baseurl }}/practice-texts).
- **One thing to leave out:** other people's unpublished work, student writing with names attached, anything under embargo or an IRB protocol.

## The paragraph we'll use

We begin with the **AI-use policy** from the
[practice texts]({{ site.baseurl }}/practice-texts). It is short enough to read
together and familiar enough to judge. For the style-guide exercise, we move
to a [four-paragraph project report]({{ site.baseurl }}/practice-texts#community-archive),
where wording choices have to hold across a longer argument.

> **Use of AI Tools.** Students may use generative AI tools in this course
> where appropriate, but should not use them to complete assignments for them.
> Any use of AI should be disclosed. Work that is substantially produced by AI
> will not receive credit and may be referred as an academic integrity
> violation. Students are responsible for the accuracy of everything they
> submit. If you are unsure whether a particular use is permitted, ask before
> submitting. The goal of this policy is to support learning rather than to
> prohibit technology, and I expect students to use their judgment.

Read it as the person who wrote it and it is clear enough. The session is about
what happens when you stop reading it that way.

The existing policy replies are **provisional examples**: their source records
the tool and date, but they came from the conversation that developed this
workshop. They need a fresh run without that prior context. Cuts are marked.
The style-guide exercise uses separately labeled prepared examples. Compare
your own results with the text; a different response can be just as useful.

## 1. Try a reasonable editing request
{: .step #step-1}

Paste the syllabus policy, then ask for a conventional edit.

{% include prompt.html id="baseline" %}

This is a reasonable request. It names the document, sets an editing goal, and
asks the assistant to preserve meaning. It may produce useful changes. Read
the reply beside the original and choose one change you would accept and one
you would inspect more closely.

- Did “should,” “may,” and “must” keep their different meanings?
- Did the edit make a sentence clearer, or make a policy decision the writer had left open?
- Does the explanation account for the substantial changes?
- Which questions remain even if every sentence now reads smoothly?

**A smooth edit still needs your judgment.** “Preserve my meaning” is a useful
instruction, but an ambiguous sentence can leave that meaning undecided. If
the assistant keeps an ambiguity or asks you about it, count that as useful
work too. The next step asks it to identify those decisions before rewriting.

**Illustrative edit:** “Students may use AI where appropriate, but not to
complete assignments for them.” The sentence is shorter, yet “appropriate”
still needs examples and the paragraph still gives no disclosure method.
This is a prepared comparison for the slides, not a recorded reply. Your own
run may identify those gaps; keep and examine what actually comes back.

## 2. Teach it to read like you do
{: .step #step-2}

Use the same original policy with a more specific task. Name the reader,
focus the concern, and ask for the evidence behind each observation.

{% include prompt.html id="policy-reader-brief" %}

**Illustrative reader report:** “Any use of AI should be disclosed” gives no
location or format for that disclosure. The instructor needs to choose where
it goes and what it includes, then add that instruction.

The gain is something you can act on: **a passage, a specific problem, and a
next step**. The prompt asks for a diagnosis before editing, so it changes the
task as well as adding detail. This prepared illustration shows what to look
for in the reply; it does not guarantee that any prompt will produce it.

For another document, use the more general brief below. The saved policy
response after it belongs to that earlier, fuller prompt.

A brief needs five things: **what this is**, **who reads it**, **what it's trying to do**, **what you're worried about**, and **what not to touch**. Then the move that changes everything — ask for a reading, not a rewrite.

{% include prompt.html id="editorial-brief" %}

{% include demo.html id="policy-briefed" %}

Compare this kind of response with your first edit. The brief adds a purpose
and a specific concern, and it also changes the requested task from rewriting
to commenting. Look for a useful question the edit alone did not resolve.
If you want to compare prompts directly, use the same starting text and tool
in fresh conversations and keep both replies.

Now the second strategy, which is what keeps the first one honest — and notice
first what the brief already bought you. Every one of those three findings
arrived with the sentence it was about, because the prompt demanded it. That
is not the tool being scrupulous; it is the tool doing what it was told.

The saved conversation also gives us a second before/after comparison.
An open-ended follow-up produced the comment below:

{% include prompt.html id="policy-open-followup" %}

{% include demo.html id="policy-vague" %}

Don't accept it and don't argue with it. Make it point:

{% include prompt.html id="quote-it" %}

{% include demo.html id="policy-quoted" %}

The gain is a more accountable comment: the reply distinguishes a finding
about the supplied text from general teaching advice. **Ask for evidence you
can inspect.** A quotation does not automatically prove the criticism; for
something missing, ask which purpose or rule makes the omission matter.

One more, because it will flatter you by default:

{% include prompt.html id="anti-sycophancy" %}

Never ask *is this good?* A yes-or-no question buys you praise. Ask for a ranking and something has to come last.

### Two of these are permanent, one isn't

Worth stopping on, because it decides where each move lives.

**The brief is per piece.** What this is, who reads it, what it's trying to do
— that changes with every document, so you type it fresh every time. There's
no automating it and no reason to want to: writing the brief is how you find
out what you think the piece is doing.

**The other two aren't about this policy at all.** *Never make a claim about
my text without quoting it* and *never open with praise* are facts about how
you want to be read. They'll be just as true of the next thing you write, and
the one after that. You've just pasted them by hand, which is the right way to
meet them and a silly way to keep them.

So don't keep pasting them. **Those are the first two lines of the rule file**
you'll assemble in step 5 — and you have them already, before writing a single
rule of your own. What step 4 adds is the ones you could only have found by
watching it get your own work wrong.

## 3. Assign reader roles
{: .step #step-3}

Keep the text and brief fixed, then change the reader's role. A student may
ask what to do next; an assignment designer may ask whether the instructions
and grading criteria describe the same work. Neither role needs to rewrite
the assignment to give its author a useful question.

### Read a real assignment in two roles

Open the [Making History assignment exercise]({{ site.baseurl }}/examples/assignment-review/).
It includes the actual Campus History archive-and-essay assignment, a text
copy, and links to its surrounding instructions. Supply the same materials
to both readers in separate conversations.

{% include prompt.html id="assignment-student" %}

{% include prompt.html id="assignment-designer" %}

The designer's framework is **purpose, task, and criteria for success**, from
[TILT](https://www.tilthighered.org/resources). Check what the assignment
already explains as carefully as you check what may be missing.

{% include prompt.html id="assignment-compare" %}

**Prepared observation:** the assignment explains the archive visit, essay
length, images, and qualities of strong work. Its grading section also
expects an “AI-Archive Comparison,” without saying in the requirements where
that comparison belongs or whether it counts toward the word target. That
joins a student's practical question to a designer's alignment question.
It is an observation for discussion, not a transcript of an AI run.

The instructor chooses how to clarify the task. Other course materials or
class discussion may already answer it. Ask actual students to explain the
assignment back to you before treating an AI reading as evidence of their
understanding.

### Try other readers on your own text

You already imagine readers when revising: the reviewer who may object, the
student meeting a term for the first time, or the editor in a hurry. Make
that perspective explicit and inspect what it helps you notice.

Same paragraph, same brief. Change only who's reading. **Run at least two**, and don't let any of them fix anything.

{% include prompt.html id="role-reviewer" %}

{% include prompt.html id="role-outsider" %}

{% include prompt.html id="role-panelist" %}

Then pick the one that fits the work you actually brought:

{% include prompt.html id="role-desk-editor" %}

{% include prompt.html id="role-confused-student" %}

The earlier policy demonstration gives another example of a possible
student reading:

{% include demo.html id="policy-student" %}

{% include prompt.html id="role-outsider" %}

Here is the same paragraph under an outsider-reader prompt:

{% include demo.html id="policy-outsider" %}

### The part that matters

Put the readings side by side. Check the comparison against both replies
and the original text; a fluent summary can misrepresent any of them.

{% include prompt.html id="compare-readers" %}

{% include demo.html id="policy-compare" %}

These are generated perspectives, not independent human reviewers. Agreement
can suggest a place to inspect; it does not verify the criticism.

**Read the comparison for three things.**

**What both readers flagged.** Return to the passage and see whether it
supports the concern. In the assignment, the comparison requirement really
is named in the grading section. Its location remains a question for the
author, not something the assistant should decide.

**What only one reader flagged.** Decide whether the concern matters for the
intended audience. A specialist's request for detail and a newcomer's request
for a definition may both be reasonable in different settings.

**Where the readers disagree.** Ask whether the disagreement exposes an
authorial choice, a mistaken reading, or missing context. In the provisional
policy comparison above, “instruction or enforcement” is presented as a
choice. A policy can reasonably serve both purposes. You can keep the useful
question without accepting that framing.

**Keep the text fixed while changing the perspective.** That lets you inspect
how the requested role changes the questions you receive. Use those questions
to plan a revision or a conversation with real readers.

## 4. Turn corrections into rules
{: .step #step-4}

The first three steps gave you changes and comments to evaluate. Some of your
corrections will apply to more than this policy: preserve a qualification,
keep a defined term, or ask before resolving an ambiguity. Write those down
as rules you can reuse.

This step is about how to write one that holds. Not where to keep it, which is step 5, and not what your rules should say, which is yours to decide. **The difference between a rule that works and one that gets quietly ignored is almost entirely in how it's phrased.**

### Harvest, don't invent

Don't open a blank file and write a style sheet. You'll produce a description
of the writer you would like to be, which is no use as an instruction to
anyone. The raw material already exists: every time you've said *no, put that
back*, you found a candidate.

{% include prompt.html id="rule-harvest" %}

**Twice is a rule.** The first time it flattens a hedge, that's noise. The
second time it's a pattern, and fixing it by hand a third time is unpaid
labour.

### A rule has to be checkable

This is the whole craft, and it's one test: **could someone who doesn't know
you tell whether the rule was followed, looking only at the text?**

"Be more scholarly" fails — there's no way to be wrong about it, so there's
nothing to follow. "Never replace a hedged verb with an unhedged one" passes:
you point at *suggests* becoming *demonstrates*, and the argument is over.
Most first drafts of a rule fail the same way, naming a **quality** (rigorous,
clear, academic) where they need an **action**. A quality is a wish. An action
is a rule.

Two things follow from that, and they're the reason a rule sticks:

- **Say what not to do.** A positive rule licenses everything it doesn't
  forbid — "write clearly" is satisfied by any prose the tool thinks is clear,
  which is to say its prose rather than yours. Pair them: say what you want,
  then fence off the way it usually goes wrong.
- **Rank them, because they will conflict.** "Never remove my hedges" and "cut
  anything that isn't working" will land on the same sentence eventually, and
  if you haven't said which wins, the tool decides differently every time.
  **Five rules you can put in order beat twenty you can't.**

{% include prompt.html id="rule-sharpen" %}

Then try it where it *shouldn't* fire. A rule that catches everything is as
useless as one that catches nothing.

{% include prompt.html id="rule-test" %}

If it fires on a passage where the hedge genuinely should have gone, the rule
is too broad. Add the exception now, while you still remember what it was for.

## 5. Write the rules down
{: .step #step-5}

### Apply a guide to a longer piece

Open the [community archive report and working style guide]({{ site.baseurl }}/practice-texts#community-archive).
Its four paragraphs give you several kinds of editorial work: a wordy sentence
you can simplify, a qualification worth keeping, and a claim about community
control that needs the author's decision. The report and its details are invented.

Read the report first, then try a general edit without the guide.

{% include prompt.html id="archive-general-edit" %}

**Illustrative edit:** “A common description template has made it easier for
contributors to compare records.” This usefully simplifies one sentence.
It leaves a separate question about the paragraph: how does the team's final
decision-making authority fit with the claim that contributors retain control?

Now use the same original report in a fresh conversation. Choose which guide
rules you would keep, supply the guide, and request a reading against it.

{% include prompt.html id="archive-style-review" %}

For each useful comment, check both the quotation and the rule. Does the rule
actually apply? Is the suggested change a matter of wording, or does it decide
what the writer means? The prompt also asks for a passage to leave alone:
a guide should help an editor recognize deliberate choices as well as problems.

The gain is an explicit reason for each editorial choice. In the slide
illustration, the guide protects “may reflect” because the evidence cannot
distinguish several explanations. It also calls attention to who controls
decisions. Compare those observations with your first reply; a broad prompt
may have caught them too.

Now select one local change you agree with.

{% include prompt.html id="archive-style-edit" %}

Compare the proposal with the original. For example, shortening “the
implementation of a common description template” may preserve the point.
Replacing “retain control” with “have a voice” changes the claim and needs
the writer's agreement. The [prepared examples]({{ site.baseurl }}/practice-texts#archive-style-guide)
give you a few comparisons after you have made your own reading.

### Reuse a guide across semesters

The [Campus History style-guide exercise]({{ site.baseurl }}/examples/campus-history-style-guide/)
uses the actual guide for the student essay collection. It carries editorial
decisions across semesters: consistent headings, captions, citations, and
light prose cleanup, while preserving each student's argument and voice.
Download its snapshot and try it on one essay you are authorized to share.

{% include prompt.html id="campus-history-normalize" %}

**Prepared illustration:** removing “In conclusion,” from “In conclusion, the
letters suggest that students may have used the room after hours” follows
the guide's treatment of assignment scaffolding. Keeping “suggest” and “may
have” preserves the limit of the evidence. This sentence is invented for
the exercise, not taken from a student's work.

A saved guide also needs review. The exercise identifies two conflicting
instructions in the current guide. Ask about such conflicts before applying
a rule across a collection, and inspect the rendered page after editing.

### Build a guide from your own writing

The sample guide belongs to that report. For your own work, combine rules from
your corrections with a few passages whose style you want to keep. Ask the
assistant to describe their patterns from evidence:

{% include prompt.html id="style-extract" %}

It will get part of this wrong — it tends to mistake caution for vagueness, and it will miss the habits you'd most like named. **Correcting it is the point.** Ten minutes of arguing with a description of your own prose is how the style sheet stops being its and starts being yours.

Then add the negative rules, which in practice do more work than the positive ones:

{% include prompt.html id="style-never" %}

Finally, put the standing instruction at the top, so the editorial stance doesn't have to be re-established every time:

{% include prompt.html id="standing-instruction" %}

**Where to keep it.** A plain text file you paste at the top of a conversation works completely and depends on nothing. If you want it applied automatically, most tools have somewhere to put it — a Project in Claude, custom instructions or a custom GPT in ChatGPT, a Gem in Gemini. Start with the text file. Upgrade later, or never.

## 6. Move out of the chat window
{: .step #step-6}

Optional, and the shortest step here. Everything above works in a browser tab
with nothing set up. But two things you've built today don't survive the tab:
**your rules scroll away** when the conversation ends, and **your draft isn't
anywhere** — it's spread across forty messages in a tool that owns the
transcript. Same shape, same fix: put them somewhere that persists.

### Give the rules somewhere to live

A **project** holds instructions and applies them to every conversation inside
it — Projects in Claude, projects or custom GPTs in ChatGPT, Gems in Gemini.
Make one per piece of work, not one for everything: "book chapter 3" and
"grant narrative" want different briefs, and a project covering both briefs
for neither.

{% include prompt.html id="project-instructions" %}

Two cautions. A project's memory is a liability as well as a convenience — it
will happily reason from a draft you replaced three weeks ago, which is why
that block tells it to ask rather than assume. And the limits from *Before you
start* still apply: a project is a place you've uploaded things.

### Keep the draft in a file

Write in a plain text file — `.txt`, or `.md` if you want headings to
survive. The reason is ordinary rather than technical: a plain file opens in
anything, outlives whichever assistant you're using this year, and leaves no
question about which version is current. **The conversation is scratch. The
file is the draft.**

Keep the original file as the point of comparison. Ask for a reading of one
part, decide which findings are useful, then make an edit yourself or request
a specific change to a copy. **Inspect what changed before adopting it.** A
change list helps you check the scope as well as the wording.

{% include prompt.html id="working-file" %}

Some tools will edit your files directly rather than making you copy and
paste. That's faster, and it removes friction that was doing useful work for
you — when it takes one sentence to rewrite the whole draft, ask whether you'd
have approved each of those changes had you seen them. So keep the discipline
explicit, and work somewhere you can undo.

{% include prompt.html id="no-silent-edits" %}

## Look at your paragraph again
{: .step #closing-pass}

Return to the paragraph you brought and compare it with the original.
Choose one finding you accepted, rejected, or want to investigate. Point to
the passage and explain your decision.

If you requested an edit, check that its meaning still matches your intent.
If you kept the text, name what the reading helped you understand. **The
useful result is a decision you can explain**, whether or not a sentence
changed. Save one rule that would help with your next piece.

## What to take with you
{: .step #takeaways}

Use these five techniques on a syllabus, report, abstract, CV, or shared
collection. Start with one passage or one recurring problem.

- **Brief the task.** Name the audience, purpose, and limits. Supply the current text and say what must stay intact.
- **Ask for evidence.** Request a passage and the rule behind a finding. Check that the rule applies; a quotation alone does not prove the criticism.
- **Compare perspectives.** Keep the text fixed and change the reader. Use differences to generate questions, then check them against the text and actual readers.
- **Save your decisions.** Turn useful corrections into a short, reusable guide. Include what to preserve and when to ask; revise conflicting or overbroad rules.
- **Work in passes.** Diagnose, choose an edit, then inspect the result. Keep the original and compare both meaning and presentation before accepting changes.

## Take the session with you

- The full [prompt library]({{ site.baseurl }}/prompts) — everything above, in one page, still copy-able.
- The [assignment review]({{ site.baseurl }}/examples/assignment-review/) and [Campus History guide exercise]({{ site.baseurl }}/examples/campus-history-style-guide/) — real teaching materials, full prompts, and prepared observations.
- The [practice texts]({{ site.baseurl }}/practice-texts), if you want to run the whole sequence again on something low-stakes.
- <a href="{{ site.baseurl }}/assets/posters/sept-23-amaranth-ai-brown-bag-flyer.pdf">The session flyer</a> (PDF).

Questions that came up in the room get added here after the session. If something didn't work on your machine or your writing, tell us — that's the most useful thing we can put on this page.

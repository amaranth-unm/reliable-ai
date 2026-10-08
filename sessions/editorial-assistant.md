---
title: AI as Editorial Assistant
layout: base
position: 1
date: 2026-09-23
kicker: Session 1 · September 23, 2026
summary: "Use AI as an eager but inexperienced editor: tell it what to look for and who the reader is, then save your rules so you don't have to repeat them."
thumbnail: "/assets/images/amman-typefounder-1568.jpg"
header-image: "/assets/images/amman-typefounder-1568.jpg"
header-tier: section
header-filter: etching
header-flip: true
header-title: AI as Editorial Assistant
header-subtitle: "Use AI as a reader whose comments you can check against your own text. Tell it your editorial rules, then decide which comments are worth acting on."
tags:
  - editing
  - prompting
  - getting started
workshop_mode: true
---

{% include nav/scrollspy-toc.html %}

This page is the full tutorial, with every prompt and some extra exercises to work through at your own pace. You can also [view the presentation slides]({{ site.baseurl }}/presents/editorial-assistant/).
{: .lead}

<div class="rule" markdown="1">
**Teach AI how to read your work. You stay the writer and the editor.**
</div>

## Why editing is the place to start

Many people first use these tools for something they can't check, like a summary of a literature they haven't read or a draft in an unfamiliar genre. It's hard to tell a good answer from a plausible one there.

Editing is different, because **you know what you meant your paragraph to say.** You can hold any comment or proposed edit up against your own text and decide whether it helps. That makes editing a good place to learn what these tools do well: ask for a reading first, and revise once you've seen its reasons.

## What you're working with

You don't need to know how a model works inside to judge what it tells you. Four habits of these tools come up in the exercises:

- **It edits smoothly, and settles ambiguities without saying so.** A cleaner
  sentence can quietly answer a question you meant to leave open. (Step 1)
- **It answers the question you ask.** An open question like *what am I
  missing?* brings in broad advice, which is often worth having. Asking it to
  quote your text gets findings you can check sentence by sentence. (Step 2)
- **It will read as anyone you name.** A student and a reviewer notice
  different things, but the same model wrote both readings, so they don't
  count as two opinions. (Step 3)
- **It forgets your preferences.** Each new conversation starts from nothing
  unless you save your rules and bring them along. (Steps 4 to 6)

## Before you start

- **A laptop**, with an AI assistant open in a browser tab. Claude, ChatGPT, Gemini, or Copilot all work, and a free account is fine.
- **One paragraph of your own writing**, such as a draft, an abstract, a policy, or a grant blurb. Your own work teaches more than an invented example. No paragraph? Take one from the [practice texts]({{ site.baseurl }}/practice-texts).
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

Read it as the person who wrote it and it seems clear. This session is about
reading it as the students it is addressed to.

**About the replies on this page.** Recorded replies show the tool and date.
They come from the conversation in which this workshop was developed, so the
tool already had some context; re-run them in a fresh conversation before
treating them as typical. […] marks a cut. Examples labeled *prepared* were
written for the slides rather than recorded. Your own replies will differ, and
a different reply can be just as good.

## 1. Try a reasonable editing request
{: .step #step-1}

Paste the syllabus policy, then ask for a conventional edit.

{% include prompt.html id="baseline" %}

Some of what comes back will probably help. Read the reply beside the
original and pick one change you would accept and one you would want to argue
with.

- Did “should,” “may,” and “must” keep their different meanings?
- Did the edit make a sentence clearer, or did it settle a policy question the writer had deliberately left open?
- Did it explain the changes that alter meaning, or only the small ones?
- Which questions are still unanswered now that every sentence reads smoothly?

**A smooth edit still needs your judgment.** “Preserve my meaning” only helps
if a sentence has one meaning to begin with. Where the original is ambiguous,
the tool either picks a reading or asks which you meant, and a question is the
better result. Step 2 gets it to name those decisions before it rewrites
anything.

**Prepared example:** “Students may use AI where appropriate, but not to
complete assignments for them.” The sentence is shorter, but “appropriate”
still needs examples, and the paragraph still doesn't say how to disclose AI
use.

Now send the same request with your own paragraph, and look for a choice the
edit made for you.

## 2. Teach it to read like you do
{: .step #step-2}

Use the same original policy, this time with a specific job. Name the reader,
focus the concern, and ask for the evidence behind each observation.

{% include prompt.html id="policy-reader-brief" %}

**Prepared example:** “Any use of AI should be disclosed” doesn't say where
or how. The instructor needs to decide what disclosure includes and where it
goes, then add that to the policy.

That reply gives you a passage, a problem, and a decision to make, because the
prompt asked for a diagnosis before any editing.

For other documents, use the general brief below. A brief says what the text
is, who reads it, what it's trying to do, what worries you, and what shouldn't
change, and it asks for comments rather than a rewrite. The recorded reply
after it comes from running this brief on the policy.

{% include prompt.html id="editorial-brief" %}

{% include demo.html id="policy-briefed" %}

Compare this with your first edit and look for a question the edit didn't
raise. To compare prompts fairly, use the same text and tool in fresh
conversations and keep both replies.

### Open questions and anchored questions

Both kinds are worth asking. An open question, such as *anything else I should
worry about?* or *what am I missing?*, lets the tool bring in what you didn't
think to ask about: teaching practice, the conventions of a genre, how readers
like yours tend to react. An anchored question ties each answer to a passage,
so you can check it against your text. Ask open questions to widen what you
consider, and anchored ones when you need to know what is on the page.

The two are easy to confuse in a reply. Later in the same conversation, an
open follow-up produced this:

{% include prompt.html id="policy-open-followup" %}

{% include demo.html id="policy-vague" %}

Some of this is good advice. Explaining the reasoning behind a policy and
treating AI use as a skill are both worth considering. But the reply reads
like a diagnosis of the paragraph, and you can't tell which parts are. Ask it
to anchor what it said:

{% include prompt.html id="quote-it" %}

{% include demo.html id="policy-quoted" %}

Now you can sort the reply. One point is about a sentence in the policy, and
you can go and check it. The other two are general advice: decide whether you
agree, but don't treat them as problems with this policy. **When a comment is
about your text, ask for the exact words.** A quotation doesn't prove the
criticism is right, but it gives you somewhere to look, and when the claim is
that something is missing, ask which purpose or rule makes the absence matter.

These tools also tend to open with praise. When you want criticism, ask in a
form where something has to come last:

{% include prompt.html id="anti-sycophancy" %}

### Which instructions to keep

**The brief changes with every document**, so write it fresh each time. That's
worth doing anyway, because writing it is how you work out what the piece is
for.

Two other instructions describe how you want any of your writing read: *quote
the text when you comment on it, and label general advice as general*, and
*don't open with praise*. Type them by hand today, then make them the first
lines of the rule file you build in step 5. Step 4 adds the rules you can only
find by watching the tool get your own work wrong.

## 3. Assign reader roles
{: .step #step-3}

Keep the text and the brief fixed, and change only the reader. A student asks
what to do next. An assignment designer asks whether the instructions and the
grading criteria describe the same piece of work. Neither has to rewrite
anything to give the author a question worth answering.

### Read a real assignment in two roles

Open the [Making History assignment exercise]({{ site.baseurl }}/examples/assignment-review/).
It includes the actual Campus History archive-and-essay assignment, a text
copy, and links to its surrounding instructions. Give the same materials to
both readers in separate conversations.

{% include prompt.html id="assignment-student" %}

{% include prompt.html id="assignment-designer" %}

The designer's framework is **purpose, task, and criteria for success**, from
[TILT](https://www.tilthighered.org/resources). Give what the assignment
already explains as much attention as what may be missing.

{% include prompt.html id="assignment-compare" %}

**Prepared observation**, in TILT's three parts:

- **Purpose.** “Skills you are practicing” explains what students learn and why.
- **Task.** The archive visit and the essay requirements give a workable sequence.
- **Criteria.** “What I'm looking for” describes strong work. But the grading
  also expects an “AI-Archive Comparison” that the requirements never place,
  so students can't tell where it goes or whether it counts toward the word
  target.

A student would ask where to put the comparison, and a designer would ask why
the grading expects something the instructions never assign. Both lead to the
same missing sentence. A recorded run of the designer prompt, on the
[exercise page]({{ site.baseurl }}/examples/assignment-review/), reached the
same point: its alignment table marks the comparison “No. It appears only in
the criteria.”

The instructor decides how to fix it, and other course materials or class
discussion may already cover it. Before you treat an AI reading as evidence of
what students understand, ask some students to explain the assignment back to
you.

### Try other readers on your own text

You already imagine readers when you revise: the reviewer who may object, the
student meeting a term for the first time, the editor in a hurry. Name that
reader in the prompt and see what it helps you notice.

**Run at least two roles on your paragraph**, and ask for comments only, not
fixes.

{% include prompt.html id="role-reviewer" %}

{% include prompt.html id="role-outsider" %}

{% include prompt.html id="role-panelist" %}

Then add the one closest to the work you brought:

{% include prompt.html id="role-desk-editor" %}

{% include prompt.html id="role-confused-student" %}

{% include prompt.html id="role-grader" %}

Here is how the confused-student role read the syllabus policy:

{% include demo.html id="policy-student" %}

And here is the outsider's reading of the same policy:

{% include demo.html id="policy-outsider" %}

### Compare the readings

Put the readings side by side. Then check the comparison against both replies
and the original, since a tidy summary can still misrepresent all three.

{% include prompt.html id="compare-readers" %}

{% include demo.html id="policy-compare" %}

Where the readings agree, you have learned where to look. You have not
learned that the criticism is right.

**Read the comparison for three things.**

**What both readers flagged.** Go back to the passage and see whether it
supports the concern. In the assignment, the comparison requirement really is
named in the grading section. Where it belongs is still the author's call.

**What only one reader flagged.** Decide whether that concern matters for the
audience you actually have. A specialist asking for more detail and a newcomer
asking for a definition can both be right, for different readers.

**Where the readers disagree.** Work out what the disagreement is about: a
choice you made on purpose, a misreading, or context you left out. In the
policy comparison above, the reply offers “instruction or enforcement” as
though you had to pick one. A policy can do both. Keep the question it raises
and drop the either-or.

Use the questions that hold up to plan a revision, or to decide what to ask a
real reader.

## 4. Turn corrections into rules
{: .step #step-4}

The first three steps gave you changes and comments to judge. Some of your
corrections will apply beyond this policy: keep a qualification, keep a
defined term, ask before resolving an ambiguity. Write those down as rules you
can reuse. **Whether a rule gets followed depends mostly on how it's
phrased.**

### Start from your corrections

Don't start with a blank page. A style sheet written from scratch tends to
describe the writer you'd like to be, which doesn't work as an instruction.
Your corrections are better material: each time you said *no, put that back*,
you found a possible rule.

{% include prompt.html id="rule-harvest" %}

**If you've made the same correction twice, make it a rule**, so you don't
have to fix it by hand a third time.

### A rule has to be checkable

Test each rule with one question: **could someone who doesn't know you tell
whether the rule was followed, just by looking at the text?**

"Be more scholarly" fails, because there's no clear way to break it. "Never
replace a hedged verb with an unhedged one" passes: if *suggests* becomes
*demonstrates*, you can point at the change. Most first drafts of a rule name
a quality (rigorous, clear, academic) where they need to name an action you
could find in the text.

Two more things to build in:

- **Say what not to do.** "Write clearly" is satisfied by anything the tool
  considers clear, which usually means its own style. Say what you want, then
  rule out the way it usually goes wrong.
- **Put your rules in order.** "Never remove my hedges" and "cut anything that
  isn't working" will eventually apply to the same sentence. If you haven't
  said which one wins, the tool may decide differently each time. Five rules
  in a clear order work better than twenty with none.

{% include prompt.html id="rule-sharpen" %}

Then test the rule on a passage where it *shouldn't* apply, to make sure it
doesn't fire everywhere.

{% include prompt.html id="rule-test" %}

If it fires on a passage where the hedge should have gone, the rule is too
broad. Add the exception now, while you still remember what it was for.

## 5. Work from a style guide
{: .step #step-5}

### Apply a guide to a longer piece

Open the [community archive report and working style guide]({{ site.baseurl }}/practice-texts#community-archive).
Its four paragraphs give you several kinds of editorial work: a wordy sentence
you can simplify, a qualification worth keeping, and a claim about community
control that needs the author's decision. The report and its details are invented.

Read the report first, then try a general edit without the guide.

{% include prompt.html id="archive-general-edit" %}

**Prepared example:** “A common description template has made it easier for
contributors to compare records.” That simplifies one sentence well. It leaves
a separate question about the paragraph: how does the team's final
decision-making authority fit with the claim that contributors retain control?

In a fresh conversation, give it the same original report and the guide rules
you want to keep, and ask for a reading against them.

{% include prompt.html id="archive-style-review" %}

For each comment, check the quotation and the rule. Does the rule apply here?
Is the change a matter of wording, or does it decide what the writer means?
The prompt also asks for a passage to leave alone, because a guide should
protect deliberate choices as well as catch problems.

Each comment now comes with a reason you can argue with. In the prepared
example on the slides, the guide protects “may reflect” because the evidence
can't tell several explanations apart, and it raises the question of who
controls decisions. Compare that with your first reply.

Then pick one local change you agree with and ask for it.

{% include prompt.html id="archive-style-edit" %}

Compare the proposal with the original. For example, shortening “the
implementation of a common description template” may preserve the point.
Replacing “retain control” with “have a voice” changes the claim and needs
the writer's agreement. The [prepared examples]({{ site.baseurl }}/practice-texts#archive-style-guide)
give you a few comparisons to check once you have made your own.

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
have” preserves the limit of the evidence. (The sentence is invented, not
taken from a student's essay.)

A saved guide needs checking too. This exercise points out two instructions in
the current guide that contradict each other. Look for conflicts like that
before you apply a guide across a whole collection, and read the rendered page
afterwards, not just the file.

### Audit formatting as well as prose

The same approach works on formatting. The [CV audit exercise]({{ site.baseurl }}/examples/cv-audit/)
uses a four-page fictional CV in Word that looks finished but has small
inconsistencies, such as mixed date ranges and an article listed under two
different statuses. Its three prompts audit the CV, check its Word structure,
and draw a style guide from its own patterns. The first asks the tool to say
whether it read the page, the extracted text, or the Word file itself.

### Build a guide from your own writing

The guide in the first exercise belongs to the archive report. For your own work, combine rules from
your corrections with a few passages whose style you want to keep. Ask the
assistant to describe their patterns from evidence:

{% include prompt.html id="style-extract" %}

Expect it to get some of this wrong. It often reads caution as vagueness, and it may miss the habits you most want named. **Saying why its description is wrong is how you find the rules you want.**

Then add rules about what not to do, which tend to change the output more than positive ones:

{% include prompt.html id="style-never" %}

Finally, put the standing instruction at the top, so you don't have to set out your editorial stance again in every new conversation:

{% include prompt.html id="standing-instruction" %}

## 6. Move out of the chat window
{: .step #step-6}

This step is optional. Everything above works in a browser tab with nothing
set up, but two things you made today won't outlast the conversation. Your
rules scroll out of view, and your draft is scattered across dozens of
messages in someone else's tool. **Keep both somewhere more permanent.**

### Give the rules somewhere to live

The simplest home is a plain text file that you paste at the top of a new
conversation. It depends on nothing, and you can move it into a tool later.

If you want the rules applied automatically, use a **project**, which holds
instructions and applies them to every conversation inside it: Projects in
Claude, projects or custom GPTs in ChatGPT, Gems in Gemini. Make one per piece
of work rather than one for everything, since a book chapter and a grant
narrative need different briefs.

{% include prompt.html id="project-instructions" %}

A project remembers everything you have given it, including the draft you
replaced three weeks ago, which is why the instructions above tell it to ask
which version to use. The limits from *Before you start* apply to anything you
upload to a project.

### Keep the draft in a file

Write in a plain text file: `.txt`, or `.md` if you want to keep headings.
A plain file opens in any program, will outlast whichever assistant you use
this year, and makes it obvious which version is current. **Treat the
conversation as scratch paper and the file as the draft.**

Keep the original file to compare against. Ask for a reading of one part,
decide which findings to act on, then either edit it yourself or ask for one
specific change to a copy. **Read what changed before you keep it.** A list of
changes shows you how much was touched, not just how it was worded.

{% include prompt.html id="working-file" %}

Some tools can edit your files directly, without copying and pasting. That's
faster, but copying and pasting was also a chance to look at each change. When
one instruction can rewrite a whole draft, ask for a list of changes and work
somewhere you can undo.

{% include prompt.html id="no-silent-edits" %}

## Look at your paragraph again
{: .step #closing-pass}

Return to the paragraph you brought and compare it with the original. Choose
one finding you accepted, rejected, or want to look into, point to the
passage, and explain your decision.

If you took an edit, check that the sentence still means what you meant. If you
kept your own wording, say what the reading showed you. **You should be able to
explain the decision**, whether or not a sentence changed. Save one rule that
will help with the next piece.

## What to take with you
{: .step #takeaways}

Use these five techniques on a syllabus, report, abstract, CV, or shared
collection. Start with one passage or one recurring problem.

- **Brief the task.** Name the audience, purpose, and limits. Supply the current text and say what must stay intact.
- **Ask open questions, then anchor.** Broad questions bring in advice you didn't think to ask for. When a comment is about your text, ask which passage it refers to and which rule makes it a problem; a quotation on its own doesn't prove the criticism.
- **Compare readers.** Keep the text fixed and change the reader. Turn the differences into questions, then check them against the text and against real readers.
- **Save your decisions.** Turn corrections you keep making into a short, reusable guide. Say what to preserve and when to ask, and rewrite rules that conflict or fire too widely.
- **Work in passes.** Diagnose, choose an edit, then read the result. Keep the original, and check both meaning and formatting before you accept a change.

## Take the session with you

- Every prompt on this page has a copy button, so you can work straight from it.
- The [assignment review]({{ site.baseurl }}/examples/assignment-review/) and [Campus History guide exercise]({{ site.baseurl }}/examples/campus-history-style-guide/): real teaching materials with full prompts and prepared observations.
- The [CV audit]({{ site.baseurl }}/examples/cv-audit/), on a fictional four-page CV in Word.
- The [practice texts]({{ site.baseurl }}/practice-texts), if you want to run the whole sequence again on something low-stakes.
- <a href="{{ site.baseurl }}/assets/posters/sept-23-amaranth-ai-brown-bag-flyer.pdf">The session flyer</a> (PDF).

We add questions from the room here after each session. If something didn't work on your computer or with your writing, please tell us and we'll add it here.

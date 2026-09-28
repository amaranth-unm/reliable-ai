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

This page is the complete tutorial, with prompts and additional exercises to work through at your own pace. You can also [View the presentation slides]({{ site.baseurl }}/presents/editorial-assistant/).
{: .lead}

<div class="rule" markdown="1">
**Teach AI to read like you want it to. Help it make better suggestions. You remain the writer and editor.**
</div>

## Why editing is the place to start

Most people first use these tools to ask for something they can't check, such as a summary of a literature they haven't read or a draft in an unfamiliar genre. You can't tell a good answer from a merely plausible one, so you either trust it or you don't.

Editing gives you something concrete to check. **You know what you intended your paragraph to say.** You can hold a comment or a proposed edit up against the original and decide whether it helps. Ask it to read before it rewrites, and revise only after you have read its reasons.

## What you're working with

You don't need a theory of how a model works to judge its comments.
Practice four habits, all of them on the text in front of you:

- **Supply the context.** Give the current draft, the audience, and the
  purpose. Don't assume the assistant knows which version you mean or which
  instructions still stand.
- **Check the evidence.** A criticism that reads well still has to point at a
  sentence you can go and read. If it says something is missing, ask which
  requirement makes the absence matter.
- **Ask a specific question.** Asking which instruction is unclear gets you
  more to work with than asking whether the draft is any good.
- **Compare readings.** Different reader roles raise different questions.
  Check each question against the text. The same model wrote all of them, so
  they are not second opinions.

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

**About the replies on this page.** The recorded replies to the policy show
the tool and date. They come from the conversation in which this workshop was
developed, so the tool already had some context, and they should be re-run in a
fresh conversation before being treated as typical. Passages marked […] were
cut. Examples labeled *prepared* were written for the slides and are not
recorded replies. Your own results may differ, and a different reply can be
just as useful.

## 1. Try a reasonable editing request
{: .step #step-1}

Paste the syllabus policy, then ask for a conventional edit.

{% include prompt.html id="baseline" %}

This is a reasonable request. It names the document, sets an editing goal, and
asks the assistant to preserve meaning. Some of what comes back will probably
be useful. Read the reply beside the original and pick one change you would
accept and one you would want to argue with.

- Did “should,” “may,” and “must” keep their different meanings?
- Did the edit make a sentence clearer, or did it settle a policy question the writer had deliberately left open?
- Did it explain the changes that alter meaning, or only the small ones?
- Which questions are still unanswered now that every sentence reads smoothly?

**A smooth edit still needs your judgment.** “Preserve my meaning” only helps
if the sentence has one meaning to begin with. Where the original is
ambiguous, there is nothing to preserve, so the tool either picks a reading or
asks you which you meant. If it asks, that is useful work. The next step gets
it to name those decisions before it rewrites anything.

**Prepared example:** “Students may use AI where appropriate, but not to
complete assignments for them.” The sentence is shorter, but “appropriate”
still needs examples, and the paragraph still doesn't say how to disclose AI
use. Your own run may or may not catch those gaps. Read what actually comes
back.

## 2. Teach it to read like you do
{: .step #step-2}

Use the same original policy with a more specific task. Name the reader,
focus the concern, and ask for the evidence behind each observation.

{% include prompt.html id="policy-reader-brief" %}

**Prepared example:** “Any use of AI should be disclosed” doesn't say where
or how to disclose it. The instructor needs to decide what disclosure should
include and where it goes, then add that to the policy.

Now you have something to act on: **a passage, a specific problem, and a next
step**. The prompt got that by asking for a diagnosis before any editing,
which changes the task rather than just adding words to it. The example shows
what a useful reply looks like. No prompt guarantees one.

For other documents, use the general brief below. The recorded reply after it
comes from running this brief on the policy.

A brief covers five things: what the text is, who reads it, what it's trying
to do, what you're worried about, and what shouldn't change. Most important,
it asks the tool to comment rather than rewrite.

{% include prompt.html id="editorial-brief" %}

{% include demo.html id="policy-briefed" %}

Compare this reply with your first edit. Look for a useful question that
the edit alone didn't raise. To compare prompts fairly, use the same text and
tool in fresh conversations and keep both replies.

Each finding in that reply came with the sentence it refers to, and it did
that because the prompt asked for it. Here is what happens when you stop
asking. Later in the same conversation, a loosely worded follow-up produced
this:

{% include prompt.html id="policy-open-followup" %}

{% include demo.html id="policy-vague" %}

Rather than accepting it or arguing with it, ask it to point to the text:

{% include prompt.html id="quote-it" %}

{% include demo.html id="policy-quoted" %}

The reply now separates what it found in the text from general teaching
advice. **Ask for the exact words.** A quotation doesn't prove the criticism
is right, but it gives you somewhere to go and check. When the claim is that
something is missing, ask which purpose or rule makes the absence matter.

One more, because these tools tend to open with praise:

{% include prompt.html id="anti-sycophancy" %}

Avoid asking *is this good?* A yes-or-no question usually gets a yes. If you
ask for a ranking, something has to come last.

### Which instructions to keep

**The brief changes with every document.** What the text is, who reads it,
and what it's trying to do are different each time, so you write the brief
fresh. That's worth doing anyway, because writing it is how you work out what
the piece is for.

The other two instructions, *quote the text for every claim* and *don't open
with praise*, have nothing to do with this particular policy. They describe how
you want any of your writing to be read. Typing them by hand today is a good
way to learn them, but you won't want to keep doing it.

**They become the first two lines of the rule file** you'll build in step 5.
Step 4 adds the rules you can only find by watching the tool get your own work
wrong.

## 3. Assign reader roles
{: .step #step-3}

Keep the text and the brief fixed, and change only the reader. A student asks
what to do next. An assignment designer asks whether the instructions and the
grading criteria describe the same piece of work. Neither one has to rewrite
anything to hand the author a useful question.

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
that comparison belongs or whether it counts toward the word target. That is
the point where a student's practical question and a designer's question about
alignment turn out to be the same question. We wrote this observation for
discussion; it is not a transcript of an AI run.

The instructor decides how to fix it, and other course materials or class
discussion may already cover it. Before you treat an AI reading as evidence of
what students understand, ask some students to explain the assignment back to
you.

### Try other readers on your own text

You already imagine readers when you revise: the reviewer who may object, the
student meeting a term for the first time, the editor in a hurry. Name that
reader in the prompt and see what it helps you notice.

Keep the paragraph and the brief the same, and change only the reader. **Run at least two roles**, and ask for comments only, not fixes.

{% include prompt.html id="role-reviewer" %}

{% include prompt.html id="role-outsider" %}

{% include prompt.html id="role-panelist" %}

Then pick the one that fits the work you actually brought:

{% include prompt.html id="role-desk-editor" %}

{% include prompt.html id="role-confused-student" %}

{% include prompt.html id="role-grader" %}

Here is how the confused-student role read the syllabus policy:

{% include demo.html id="policy-student" %}

And here is the outsider's reading of the same policy:

{% include demo.html id="policy-outsider" %}

### Compare the readings

Put the readings side by side. Then check the comparison against both replies
and against the original, because a summary that reads well can still
misrepresent all three.

{% include prompt.html id="compare-readers" %}

{% include demo.html id="policy-compare" %}

The same model wrote both readings, so they are not two opinions. Where they
agree, you have learned where to look. You have not learned that the criticism
is right.

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

**Change the reader and nothing else.** Then any difference in the questions
you get back came from the reader you named. Use those questions to plan a
revision, or to decide what to ask a real reader.

## 4. Turn corrections into rules
{: .step #step-4}

The first three steps gave you changes and comments to judge. Some of your
corrections will apply to more than this policy: keep a qualification, keep a
defined term, ask before resolving an ambiguity. Write those down as rules you
can reuse.

This step is about wording. Where to keep your rules is step 5, and what
they say is up to you. **Whether a rule gets followed depends mostly on how
it's phrased.**

### Start from your corrections

Don't start with a blank page. A style sheet written from scratch tends to
describe the writer you'd like to be, which doesn't work well as an
instruction. Your corrections are better material: each time you said *no,
put that back*, you found a possible rule.

{% include prompt.html id="rule-harvest" %}

**If you've made the same correction twice, make it a rule.** One flattened
hedge could be chance. Two is a pattern, and you shouldn't have to fix it by
hand a third time.

### A rule has to be checkable

One test does most of the work: **could someone who doesn't know you tell
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

Then test it on a passage where it *shouldn't* apply. A rule that fires
everywhere is no more useful than one that never fires.

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

**Prepared example:** “A common description template has made it easier for
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

Now every comment arrives with a reason you can argue with. In the prepared
example on the slides, the guide protects “may reflect” because the evidence
can't tell several explanations apart. It also raises the question of who
controls decisions. Compare that with your first reply, which may have caught
the same things.

Now select one local change you agree with.

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
have” preserves the limit of the evidence. This sentence is invented for
the exercise, not taken from a student's work.

A saved guide needs checking too. This exercise points out two instructions in
the current guide that contradict each other. Look for conflicts like that
before you apply a guide across a whole collection, and read the rendered page
afterwards, not just the file.

### Build a guide from your own writing

The sample guide belongs to that report. For your own work, combine rules from
your corrections with a few passages whose style you want to keep. Ask the
assistant to describe their patterns from evidence:

{% include prompt.html id="style-extract" %}

Expect it to get some of this wrong. It often reads caution as vagueness, and it may miss the habits you most want named. **Correcting its description is the useful part.** Saying why a description of your prose is wrong is how you find the rule you actually want.

Then add the negative rules. In practice these do more work than the positive ones:

{% include prompt.html id="style-never" %}

Finally, put the standing instruction at the top, so you don't have to set out your editorial stance again in every new conversation:

{% include prompt.html id="standing-instruction" %}

**Where to keep it.** A plain text file you paste at the top of a conversation works, and depends on nothing. If you want it applied automatically, most tools have a place for it: a Project in Claude, custom instructions or a custom GPT in ChatGPT, a Gem in Gemini. Start with the text file. You can move it into a tool later if you want to.

## 6. Move out of the chat window
{: .step #step-6}

This step is optional. Everything above works in a browser tab with nothing
set up, but two things you made today won't outlast the conversation. Your
rules scroll out of view, and your draft is scattered across dozens of
messages in someone else's tool. **Keep both somewhere more permanent.**

### Give the rules somewhere to live

A **project** holds instructions and applies them to every conversation inside
it: Projects in Claude, projects or custom GPTs in ChatGPT, Gems in Gemini.
Make one per piece of work rather than one for everything. A book chapter and
a grant narrative need different briefs, and a project that tries to cover
both won't serve either well.

{% include prompt.html id="project-instructions" %}

Two cautions. A project remembers everything you have given it, including the
draft you replaced three weeks ago, which is why the instructions above tell it
to ask which version to use. And the limits from *Before you start* still
apply, because a project is somewhere you have uploaded other people's
material.

### Keep the draft in a file

Write in a plain text file: `.txt`, or `.md` if you want to keep headings.
A plain file opens in any program, will outlast whichever assistant you use
this year, and makes it obvious which version is current. **Treat the
conversation as scratch paper and the file as the draft.**

Keep the original file to compare against. Ask for a reading of one part,
decide which findings are useful, then either edit it yourself or ask for one
specific change to a copy. **Read what changed before you keep it.** Asking for
a list of changes shows you how much was touched, not just how it was worded.

{% include prompt.html id="working-file" %}

Some tools can edit your files directly, without copying and pasting. That's
faster, but copying and pasting was also a chance to look at each change. When
one instruction can rewrite a whole draft, ask whether you'd have approved each
change if you'd seen it. Ask for a list of changes, and work somewhere you can
undo.

{% include prompt.html id="no-silent-edits" %}

## Look at your paragraph again
{: .step #closing-pass}

Return to the paragraph you brought and compare it with the original.
Choose one finding you accepted, rejected, or want to investigate. Point to
the passage and explain your decision.

If you took an edit, check that the sentence still means what you meant. If you
kept your own wording, say what the reading showed you. **What you should leave
with is a decision you can explain**, whether or not a sentence changed. Save
one rule that will help with the next piece.

## What to take with you
{: .step #takeaways}

Use these five techniques on a syllabus, report, abstract, CV, or shared
collection. Start with one passage or one recurring problem.

- **Brief the task.** Name the audience, purpose, and limits. Supply the current text and say what must stay intact.
- **Ask for evidence.** Ask which passage a finding refers to, and which rule makes it a problem. Check that the rule applies; a quotation on its own doesn't prove the criticism.
- **Compare readers.** Keep the text fixed and change the reader. Turn the differences into questions, then check them against the text and against real readers.
- **Save your decisions.** Turn useful corrections into a short, reusable guide. Say what to preserve and when to ask, and rewrite rules that conflict or fire too widely.
- **Work in passes.** Diagnose, choose an edit, then read the result. Keep the original, and check both meaning and formatting before you accept a change.

## Take the session with you

- Every prompt on this page has a copy button, so you can work straight from it.
- The [assignment review]({{ site.baseurl }}/examples/assignment-review/) and [Campus History guide exercise]({{ site.baseurl }}/examples/campus-history-style-guide/): real teaching materials with full prompts and prepared observations.
- The [practice texts]({{ site.baseurl }}/practice-texts), if you want to run the whole sequence again on something low-stakes.
- <a href="{{ site.baseurl }}/assets/posters/sept-23-amaranth-ai-brown-bag-flyer.pdf">The session flyer</a> (PDF).

We add questions from the room here after each session. If something didn't work on your computer or with your writing, please tell us. It's the most useful thing we can add to this page.

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

Most people first use these tools to ask for something they can't check, such as a summary of a literature they haven't read or a draft in an unfamiliar genre. You can't tell a good answer from a merely plausible one, so you either trust it or you don't.

Editing gives you something concrete to check. **You know what you intended your paragraph to say.** You can compare a comment or proposed edit with the original and decide whether it helps. Ask it to read first, and decide on revisions only after you've looked at its reasons.

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

Read it as the person who wrote it and it is clear enough. The session is about
what happens when you stop reading it that way.

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

**Prepared example:** “Students may use AI where appropriate, but not to
complete assignments for them.” The sentence is shorter, but “appropriate”
still needs examples, and the paragraph still doesn't say how to disclose AI
use. Your own run may catch those gaps. Either way, look closely at what
actually comes back.

## 2. Teach it to read like you do
{: .step #step-2}

Use the same original policy with a more specific task. Name the reader,
focus the concern, and ask for the evidence behind each observation.

{% include prompt.html id="policy-reader-brief" %}

**Prepared example:** “Any use of AI should be disclosed” doesn't say where
or how to disclose it. The instructor needs to decide what disclosure should
include and where it goes, then add that to the policy.

That gives you something to act on: **a passage, a specific problem, and a
next step**. Because the prompt asks for a diagnosis before any editing, it
changes the task as well as adding detail. The example shows what to look for
in the reply. No prompt guarantees it.

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

Notice that each finding in that reply came with the sentence it refers to.
That happened because the prompt asked for it, and it's worth seeing what
happens when you stop asking. Later in the same conversation, a loosely worded
follow-up produced this:

{% include prompt.html id="policy-open-followup" %}

{% include demo.html id="policy-vague" %}

Rather than accepting it or arguing with it, ask it to point to the text:

{% include prompt.html id="quote-it" %}

{% include demo.html id="policy-quoted" %}

The reply now separates what it found in the text from general teaching
advice. **Ask for evidence you
can inspect.** A quotation does not automatically prove the criticism; for
something missing, ask which purpose or rule makes the omission matter.

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

Keep the paragraph and the brief the same, and change only the reader. **Run at least two roles**, and ask for comments only, not fixes.

{% include prompt.html id="role-reviewer" %}

{% include prompt.html id="role-outsider" %}

{% include prompt.html id="role-panelist" %}

Then pick the one that fits the work you actually brought:

{% include prompt.html id="role-desk-editor" %}

{% include prompt.html id="role-confused-student" %}

Here is how the confused-student role read the syllabus policy:

{% include demo.html id="policy-student" %}

And here is the outsider's reading of the same policy:

{% include demo.html id="policy-outsider" %}

### Compare the readings

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
authorial choice, a mistaken reading, or missing context. In the policy
comparison above, “instruction or enforcement” is presented as a
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
*demonstrates*, you can point to the change. Most first drafts of a rule name
a quality (rigorous, clear, academic) when they need an action. Qualities are
hard to check. Actions aren't.

Two more things help a rule hold:

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

What you get is a stated reason for each editorial choice. In the prepared
example on the slides, the guide protects “may reflect” because the evidence cannot
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

Expect it to get some of this wrong. It often mistakes caution for vagueness, and it may miss the habits you most want named. **Correcting its description is the useful part.** Ten minutes spent arguing with an account of your own prose is how the style sheet becomes yours.

Then add the negative rules, which in practice do more work than the positive ones:

{% include prompt.html id="style-never" %}

Finally, put the standing instruction at the top, so the editorial stance doesn't have to be re-established every time:

{% include prompt.html id="standing-instruction" %}

**Where to keep it.** A plain text file you paste at the top of a conversation works completely and depends on nothing. If you want it applied automatically, most tools have a place for it: a Project in Claude, custom instructions or a custom GPT in ChatGPT, a Gem in Gemini. Start with the text file. You can move it into a tool later if you want to.

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

Two cautions. A project remembers what you've given it, which cuts both ways:
it may reason from a draft you replaced three weeks ago, which is why the
instructions above tell it to ask rather than assume. And the limits from
*Before you start* still apply, because a project is a place where you've
uploaded material.

### Keep the draft in a file

Write in a plain text file: `.txt`, or `.md` if you want to keep headings.
A plain file opens in any program, will outlast whichever assistant you use
this year, and makes it obvious which version is current. **Treat the
conversation as scratch paper and the file as the draft.**

Keep the original file as the point of comparison. Ask for a reading of one
part, decide which findings are useful, then make an edit yourself or request
a specific change to a copy. **Inspect what changed before adopting it.** A
change list helps you check the scope as well as the wording.

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

- The [prompt library]({{ site.baseurl }}/prompts): every prompt from this page, ready to copy.
- The [assignment review]({{ site.baseurl }}/examples/assignment-review/) and [Campus History guide exercise]({{ site.baseurl }}/examples/campus-history-style-guide/): real teaching materials with full prompts and prepared observations.
- The [practice texts]({{ site.baseurl }}/practice-texts), if you want to run the whole sequence again on something low-stakes.
- <a href="{{ site.baseurl }}/assets/posters/sept-23-amaranth-ai-brown-bag-flyer.pdf">The session flyer</a> (PDF).

We add questions from the room here after each session. If something didn't work on your computer or with your writing, please tell us. It's the most useful thing we can add to this page.

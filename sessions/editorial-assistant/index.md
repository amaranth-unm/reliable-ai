---
title: AI as Editorial Assistant
presenter: Fred Gibbs
layout: base
position: 1
date: 2026-09-23
kicker: Session 1 · September 23, 2026
summary: "Use AI as an eager but inexperienced editor: tell it what to look for and who the reader is, then save your rules so you don't have to repeat them."
points:
  - title: Teach AI to read like you do
    text: Treat AI like an eager but naive student who needs guidance about what to look for and what to suggest.
  - title: Create rules and style guides
    text: Gain more control over the kind of thinking and suggestions from AI tools.
  - title: Assign reader roles
    text: Learn techniques for having AI read as different kinds of readers and improving its focus.
flyer: "Brown Bag Flyer.jpeg"
time: "12:00–12:50"
location: History Commons
thumbnail: "/assets/images/amman-typefounder-1568.jpg"
header-image: "/assets/images/amman-typefounder-1568.jpg"
header-tier: section
header-filter: etching
header-flip: true
header-title: AI as Editorial Assistant
header-subtitle: "Use AI as a reader whose comments you can check against your own text. Tell it your editorial rules, then decide which comments are worth acting on."
header-caption: "Jost Amman, <i>Der Schrifftgiesser</i> (the typefounder), from <i>Eygentliche Beschreibung aller Stände auff Erden</i>, Frankfurt, 1568. Shown mirrored. Public domain, via Wikimedia Commons."
tags:
  - editing
  - prompting
  - getting started
workshop_mode: true
redirect_from: /sessions/editorial-assistant.html
---

{% comment %}
Authoring references: SESSION-STYLE.md. Each step: the text, the prompt,
what came back, what to check. Recorded replies are in _data/demos.yml and
were made with scripts/record-runs.py from
workshop-drafts/editorial-assistant/runs-plan.json; see MAINTAINING.md to
re-record them.
{% endcomment %}

{% include nav/scrollspy-toc.html %}

Work down this page during the session or return to it later. Each step shows a text, the prompt sent to an AI tool and the reply that came back, so you can repeat the process with your own writing.
{: .lead}

<div class="rule" markdown="1">
**Teach AI how to read your work. You stay the writer and the editor.**
</div>

## Introduction
{: .step #introduction}

### Why editing is the place to start

Many people first use these tools for something they can't check, like a summary of a literature they haven't read or a draft in an unfamiliar genre. It's hard to tell a good answer from a plausible one there.

Editing is different, because **you know what you meant your paragraph to say.** You can hold any comment or proposed edit up against your own text and decide whether it helps. That makes editing a good place to learn what these tools do well: ask for a reading first, and revise once you've seen its reasons.

### What you're working with

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

### About the examples

The texts are invented practice material, apart from one real course assignment in step 3. The replies on this page were recorded on 11 November 2026 with Claude Opus 5.5, each in a new conversation with nothing set up beforehand. **Except in step 6, the tool could not search the web, open files or run code**, so it behaved like an ordinary chat window with text pasted into it. In step 6 it could also run commands, which is how it returned a Word file. The note under each reply says what was pasted in and what was cut; cuts are marked […]. Models change, so your replies will differ, and a different reply can be just as good.

### Setting up to follow along

- **Any chat assistant works:** Claude, ChatGPT, Gemini or Copilot, in a browser tab, on a free account. Step 6's Word comments need a tool that can send a file back to you; the step says more.
- **Paste the text, then the prompt, in one message.** Most prompts here say “paste the policy, then send this”. Copy the text from this page or from the data files below, paste it into the message box, press Shift+Enter for a blank line, paste the prompt below it and send.
- **New chat or same chat.** Where it matters, the note above a prompt says whether to start a new chat or continue the last one. A new chat keeps earlier replies from steering the next one, which matters most when you compare two readings.
- **Fill in the brackets.** Some prompts have slots like `[genre: seminar paper / abstract]`. Replace the whole bracket with your choice before sending.

### Data for this session

Every text pasted or attached on this page is in **[one ZIP]({{ '/assets/editorial-assistant/editorial-assistant-data.zip' | relative_url }}) (0.1 MB)**, with a README saying where each file came from. The practice texts are also on the [practice texts page]({{ site.baseurl }}/sessions/editorial-assistant/practice-texts).

<details class="more" markdown="1">
<summary>The files one at a time</summary>

| Step | File | What it is |
|---|---|---|
| 1–4 | [syllabus-policy.txt]({{ '/assets/editorial-assistant/data/syllabus-policy.txt' | relative_url }}) | The AI-use policy used as the running example |
| 3, 5 | [seminar-paragraph.txt]({{ '/assets/editorial-assistant/data/seminar-paragraph.txt' | relative_url }}) | A seminar paper paragraph, for the peer-reviewer reader |
| 3, 5 | [abstract.txt]({{ '/assets/editorial-assistant/data/abstract.txt' | relative_url }}) | An abstract, for the grant-panelist reader |
| 2, 5, 6 | [archive-report.txt]({{ '/assets/editorial-assistant/data/archive-report.txt' | relative_url }}) | A four-paragraph community archive report |
| 5 | [archive-style-guide.txt]({{ '/assets/editorial-assistant/data/archive-style-guide.txt' | relative_url }}) | The working style guide for that report |
| 3 | [making-history-campus-history-assignment.txt]({{ '/assets/editorial-assistant/data/making-history-campus-history-assignment.txt' | relative_url }}) | A real course assignment, for the two-reader exercise |
| 5 | [campus-history-essay-style-guide.txt]({{ '/assets/editorial-assistant/data/campus-history-essay-style-guide.txt' | relative_url }}) | A real collection's style guide |
| 5 | [alexandra-ruiz-cv-workshop.docx]({{ '/assets/editorial-assistant/data/alexandra-ruiz-cv-workshop.docx' | relative_url }}) | A fictional CV in Word, for the CV audit |
| 6 | [machiavelli-study-guide.docx]({{ '/assets/editorial-assistant/data/machiavelli-study-guide.docx' | relative_url }}) | An AI-written study guide in Word, without comments |
| 6 | [machiavelli-study-guide-with-comments.docx]({{ '/assets/editorial-assistant/data/machiavelli-study-guide-with-comments.docx' | relative_url }}) | The same guide with the comments step 6 added |

</details>

### Before you start

- **A laptop**, with an AI assistant open in a browser tab. Claude, ChatGPT, Gemini, or Copilot all work, and a free account is fine.
- **One paragraph of your own writing**, such as a draft, an abstract, a policy, or a grant blurb. Your own work teaches more than an invented example. No paragraph? Take one from the [practice texts]({{ site.baseurl }}/sessions/editorial-assistant/practice-texts).

<div class="reminder" markdown="1">
Use texts you have permission to share, such as your own writing or the practice texts.
</div>

### The paragraph we'll use

We begin with this **AI-use policy** from the practice texts. It is short
enough to read together and familiar enough to judge. For the style-guide
exercise, we move to a four-paragraph project report, where wording choices
have to hold across a longer argument.

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

## 1. Try a reasonable editing request
{: .step #step-1}

Paste the syllabus policy into a new chat, then ask for a conventional edit.

{% include prompt.html id="baseline" %}

{% include demo.html id="policy-baseline" %}

Some of this helps, and the closing suggestion to give examples of acceptable
use is a good one. Now read the edit beside the original.

- Did “should,” “may,” and “must” keep their different meanings?
- Did the edit make a sentence clearer, or did it settle a policy question the writer had deliberately left open?
- Did it explain the changes that alter meaning, or only the small ones?
- Which questions are still unanswered now that every sentence reads smoothly?

Here, “Any use of AI should be disclosed” became “Disclose any use of AI.”
That turns a recommendation into a command, and the reply lists it under
**small trims**. “Preserve my meaning” only helps if a sentence has one
meaning to begin with. Where the original is ambiguous, the tool either picks
a reading or asks which you meant, and a question is the better result. Step
2 gets it to name those decisions before it rewrites anything.

<div class="keypoint" markdown="1">
Add one line to any editing request: “If a sentence could mean more than one thing, ask me which I meant before you change it.”
</div>

Now send the same request with your own paragraph, and look for a choice the
edit made for you.

## 2. Teach it to read like you do
{: .step #step-2}

Use the same original policy in a new chat, this time with a specific job.
Name the reader, focus the concern, and ask for the evidence behind each
observation.

{% include prompt.html id="policy-reader-brief" %}

{% include demo.html id="policy-reader-brief-run" %}

That reply gives you passages, problems and decisions to make, because the
prompt asked for a diagnosis before any editing. Item 2 is the “should” that
step 1's edit quietly changed, now raised as a question for you.

For other documents, use the general brief below. A brief says what the text
is, who reads it, what it's trying to do, what worries you, and what shouldn't
change, and it asks for comments rather than a rewrite.

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

The two are easy to confuse in a reply. In the same chat, an open follow-up
produced this:

{% include prompt.html id="policy-open-followup" %}

{% include demo.html id="policy-vague" %}

Some of this is good advice. Saying how you will decide a case, and naming
fabricated citations as the accuracy risk in a history course, are both worth
considering. But the reply reads like a diagnosis of the paragraph, and you
can't tell which parts are. Ask it to anchor what it said:

{% include prompt.html id="quote-it" %}

{% include demo.html id="policy-quoted" %}

Now you can sort the reply. One point comes from the policy's wording, and you
can go and check it. The rest are inferences about students and courses:
decide whether you agree, but don't treat them as problems with this policy.

<div class="keypoint" markdown="1">
Ask open questions when you want ideas, and ask for the exact words when you want to know what's on the page. A comment that can't point to a passage is general advice, which may still be worth taking.
</div>

A quotation doesn't prove the criticism is right, but it gives you somewhere to
look. When the claim is that something is missing, ask which purpose or rule
makes the absence matter.

These tools also tend to open with praise. When you want criticism, ask in a
form where something has to come last. This needs more than one paragraph, so
the recorded run used the four-paragraph archive report.

{% include prompt.html id="anti-sycophancy" %}

{% include demo.html id="archive-rank" %}

The ranking forced a weakest paragraph, and the reason it gives can be
checked: paragraph 2 says contributors “retain control” two sentences after
saying the team makes final decisions. Step 5 comes back to that sentence.

### Which instructions to keep

**The brief changes with every document**, so write it fresh each time. That's
worth doing anyway, because writing it is how you work out what the piece is
for.

Two other instructions describe how you want any of your writing read: *quote
the text when you comment on it, and label general advice as general*, and
*don't open with praise*. Type them by hand today, then make them the first
lines of the style sheet you build in step 5. Step 4 adds the rules you can
only find by watching the tool get your own work wrong.

## 3. Assign reader roles
{: .step #step-3}

Keep the text and the brief fixed, and change only the reader. A student asks
what to do next. A reviewer asks what the claim rests on. Neither has to
rewrite anything to give the author a question worth answering.

### Read the policy as two different readers

Start a new chat for each reader and paste the policy above the prompt.

{% include prompt.html id="role-confused-student" %}

{% include demo.html id="policy-student" %}

{% include prompt.html id="role-outsider" %}

{% include demo.html id="policy-outsider" %}

### Compare the readings

Put the readings side by side in a new chat, with the policy. Then check the
comparison against both replies and the original, since a tidy summary can
still misrepresent all three.

{% include prompt.html id="compare-readers" %}

{% include demo.html id="policy-compare" %}

Where the readings agree, you have learned where to look. You have not
learned that the criticism is right.

**Read the comparison for three things.**

**What both readers flagged.** Go back to the passage and see whether it
supports the concern. Both readers stopped at “substantially” and at whether
disclosing protects the student, and the policy really doesn't say.

**What only one reader flagged.** Decide whether that concern matters for the
audience you actually have. Only the careful outsider worried about which
tools count; the student at 11pm barely noticed.

**Where the readers disagree.** Work out what the disagreement is about: a
choice you made on purpose, a misreading, or context you left out. Here the
comparison turns the disagreement into decisions the policy hasn't made, such
as whether it protects students' thinking or the authorship of the text. Keep
the questions that hold up and drop any that force a false choice.

<div class="keypoint" markdown="1">
Give each imagined reader its own conversation and ask for questions, not fixes. Check the concerns they share against the passage, and the ones that matter against a real reader.
</div>

### Try other readers on other texts

You already imagine readers when you revise: the reviewer who may object, the
panelist in a hurry. Name that reader in the prompt and see what it helps you
notice. These two used other practice texts, each pasted above the prompt in
a new chat.

{% include prompt.html id="role-reviewer" %}

{% include demo.html id="seminar-reviewer" %}

The reviewer makes specific historical claims about territorial legislation
and upstream diversions. They are the tool's claims, and a real reviewer's
would need checking just the same. The useful part is the question at the
end, which tells the writer what the paragraph has to show.

{% include prompt.html id="role-panelist" %}

{% include demo.html id="abstract-panelist" %}

<details class="more" markdown="1">
<summary>Two more readers that need your own materials</summary>

These ask for things only you have, a journal's aims and scope or an
assignment's rubric, so there is no recorded reply. Use them the same way:
one reader per chat, comments only.

{% include prompt.html id="role-desk-editor" %}

{% include prompt.html id="role-grader" %}

</details>

### Read a real assignment in two roles

The [Making History assignment exercise]({{ site.baseurl }}/examples/assignment-review/)
runs the same idea on a real course assignment, with a student reader and an
assignment designer who uses the purpose, task and criteria framework from
[TILT](https://www.tilthighered.org/resources). Its three prompts and their
recorded replies are on that page. The comparison found that the grading
expects an “AI-Archive Comparison” the requirements never ask students to
produce, so a student can't tell how to meet a criterion the task never names.
It also flagged claims in both readings that the assignment doesn't support.
Before you treat an AI reading as evidence of what students understand, ask
some students to explain the assignment back to you.

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

In the recorded run, we went back to the chat from step 1 and sent three
corrections to its edit, one at a time:

1. “Put "should" back in both places. "Disclose any use of AI" turns a recommendation into a command, and I haven't decided yet whether disclosure is required.”
2. “Move the goal statement back to the end. I want students to meet the rules first and the reason last. Please don't move sentences without asking.”
3. “Change "you" back to "students". The rest of my syllabus is in the third person.”

The reply to the third correction is worth reading closely:

{% include demo.html id="policy-correction-3" %}

The first edit had also dropped “in this course” and “If you are” without
listing either change. The tool found them only when it restored the
original. Then, in the same chat:

{% include prompt.html id="rule-harvest" %}

{% include demo.html id="rule-harvest-run" %}

Each rule quotes the exchange it came from, so you can check it against what
you actually said. **If you've made the same correction twice, make it a
rule**, so you don't have to fix it by hand a third time.

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

The recorded run tried a typical first draft in a new chat.

{% include prompt.html id="rule-sharpen" %}

{% include demo.html id="rule-sharpen-run" %}

Then test the rule on a passage where it *shouldn't* apply, to make sure it
doesn't fire everywhere. The run used the first harvested rule and three
sentences from the practice texts.

{% include prompt.html id="rule-test" %}

{% include demo.html id="rule-test-run" %}

The rule fired on passage 2 because the word “may” appears, though that “may”
is a hedge about evidence, not a permission. If a rule fires where it
shouldn't, it is too broad. Add the exception now, while you still remember
what it was for: here, split it into one rule for obligation and one for
hedges.

<div class="keypoint" markdown="1">
When you make the same correction twice, write it as a rule someone else could check by looking at the text, then test it on a passage where it shouldn't apply.
</div>

## 5. Work from a style guide
{: .step #step-5}

### Apply a guide to a longer piece

Open the [community archive report and working style guide]({{ site.baseurl }}/sessions/editorial-assistant/practice-texts#community-archive),
or download [archive-report.txt]({{ '/assets/editorial-assistant/data/archive-report.txt' | relative_url }})
and [archive-style-guide.txt]({{ '/assets/editorial-assistant/data/archive-style-guide.txt' | relative_url }}).
The report's four paragraphs give you several kinds of editorial work: a
wordy sentence you can simplify, a qualification worth keeping, and a claim
about community control that needs the author's decision. The report and its
details are invented.

Read the report first, then try a general edit without the guide, pasting
the report above the prompt in a new chat.

{% include prompt.html id="archive-general-edit" %}

{% include demo.html id="archive-general-run" %}

The edit is careful and flags its two meaning changes, which is better than
step 1's. But both are decisions: “retain control” became “a real say”, and
“shows” became “suggests … can strengthen”. The reply made them and asked you
to check afterwards.

In a fresh conversation, give it the same original report and the guide rules
you want to keep, and ask for a reading against them.

{% include prompt.html id="archive-style-review" %}

{% include demo.html id="archive-guide-run" %}

For each comment, check the quotation and the rule. Does the rule apply here?
Is the change a matter of wording, or does it decide what the writer means?
The prompt also asks for a passage to leave alone, because a guide should
protect deliberate choices as well as catch problems. Each comment now comes
with a reason you can argue with, and the two questions about control and
ownership come back to you as decisions instead of arriving as edits.

Then pick one local change you agree with and ask for it in the same chat.
The run chose the template sentence from finding 5.

{% include prompt.html id="archive-style-edit" %}

{% include demo.html id="archive-guide-edit-run" %}

Compare the proposal with the original. Shortening “the implementation of a
common description template” keeps the point. The reply then asks which of two
meanings you intended instead of picking one, which is what the prompt asked
it to do.

<div class="keypoint" markdown="1">
Ask for a reading against your guide before any edits, with each comment quoting the passage and naming its rule. Then ask for one small change at a time, and for a question whenever a change would need your decision.
</div>

### Reuse a guide, or audit a document

Two exercise pages take the same approach further, each with its own prompts
and recorded replies:

- The [Campus History style-guide exercise]({{ site.baseurl }}/examples/campus-history-style-guide/)
  uses the actual guide for a collection of student essays. It carries
  editorial decisions across semesters while preserving each student's
  argument and voice, and it points out two instructions in the guide that
  contradict each other.
- The [CV audit exercise]({{ site.baseurl }}/examples/cv-audit/) uses a
  four-page fictional CV in Word that looks finished but has small
  inconsistencies. Its prompts audit the CV, check its Word structure, and
  draw a style guide from its own patterns.

### Build a guide from your own writing

For your own work, combine rules from your corrections with a few passages
whose style you want to keep. Ask the assistant to describe their patterns
from evidence. The recorded run had no writing of ours to use, so it was sent
three practice texts, pasted above the prompt.

{% include prompt.html id="style-extract" %}

{% include demo.html id="style-extract-run" %}

Its first move was the right one: it noticed the three passages weren't by one
writer and said which it had based the rules on. With your own passages, expect
it to get some of your habits wrong. It often reads caution as vagueness, and
it may miss the habits you most want named. **Saying why its description is
wrong is how you find the rules you want.**

Then add rules about what not to do, which tend to change the output more than
positive ones. In the same chat:

{% include prompt.html id="style-never" %}

{% include demo.html id="style-never-run" %}

It also found three of its own earlier rules that the new list contradicted,
and rewrote them. Read revisions like these before you keep them: a style
sheet that disagrees with itself will be applied differently each time.

Finally, put a standing instruction at the top, so you don't have to set out
your editorial stance again in every new conversation. This one is a file to
keep, not a prompt with a reply.

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
narrative need different briefs. This is another block to paste into a
settings field, not a prompt with a reply.

{% include prompt.html id="project-instructions" %}

A project remembers everything you have given it, including the draft you
replaced three weeks ago, which is why the instructions above tell it to ask
which version to use. As with anything you paste, upload texts you have
permission to share.

### Keep the draft in a file

Write in a plain text file: `.txt`, or `.md` (Markdown, plain text with a few
marks such as `#` for headings) if you want to keep headings. A plain file
opens in any program, will outlast whichever assistant you use this year, and
makes it obvious which version is current. **Treat the conversation as scratch
paper and the file as the draft.**

Keep the original file to compare against. Ask for a reading of one part,
decide which findings to act on, then either edit it yourself or ask for one
specific change to a copy. The recorded run pasted the whole archive report
and named its third paragraph.

{% include prompt.html id="working-file" %}

{% include demo.html id="working-file-run" %}

**Read what changed before you keep it.** A list of changes shows you how much
was touched, not just how it was worded. In the same chat:

{% include prompt.html id="no-silent-edits" %}

{% include demo.html id="no-silent-edits-run" %}

Change 3 leaves a bracket for a fact only you know, instead of inventing one.
Change 2 would put a new admission into your report; whether to make it is
your call. Some tools can edit your files directly, without copying and
pasting. That's faster, but copying and pasting was also a chance to look at
each change. When one instruction can rewrite a whole draft, ask for a list of
changes like this one and work somewhere you can undo.

### Ask for comments instead of changes

Some tools can return a copy of your Word file with comments attached to the
passages they're about, the way a colleague marks up a draft. Nothing in your
text changes. You read each comment beside its passage and decide what to do
with it. This needs a tool that can work with files and send one back, such
as ChatGPT or Claude with file creation turned on; a plain chat can only
describe the comments.

The recorded run attached [machiavelli-study-guide.docx]({{ '/assets/editorial-assistant/data/machiavelli-study-guide.docx' | relative_url }}),
a study guide to Machiavelli's political thought written by a small model
(Gemma 4) running on a laptop, and chose “a specialist in the field” as the
reader.

{% include prompt.html id="word-comments" %}

{% include demo.html id="word-comments-run" %}

[Download the commented file]({{ '/assets/editorial-assistant/data/machiavelli-study-guide-with-comments.docx' | relative_url }})
and open it in Word. Here are three of its comments, with the passages they're
attached to:

{% include demo.html id="machiavelli-comments" %}

Each comment names a chapter to check, and the reply says plainly that it took
the chapter references from memory. That is the right instruction to follow:
look up a few in an edition before you rely on any of them. If your tool can't
return a Word file with comments, the last line of the prompt asks for a table
of passages and comments instead.

<div class="keypoint" markdown="1">
Keep the draft and your rules in files you control, and bring them to each new conversation. Ask for a list of changes, or for comments instead of changes, so you read each one before it reaches your draft.
</div>

## What to take with you
{: .step #takeaways}

<div class="takeaways" markdown="1">
Use these five techniques on a syllabus, report, abstract, CV, or shared
collection. Start with one passage or one recurring problem.

- **Brief the task.** Name the audience, purpose, and limits. Supply the current text and say what must stay intact.
- **Ask open questions, then anchor.** Broad questions bring in advice you didn't think to ask for. When a comment is about your text, ask which passage it refers to and which rule makes it a problem; a quotation on its own doesn't prove the criticism.
- **Compare readers.** Keep the text fixed and change the reader. Turn the differences into questions, then check them against the text and against real readers.
- **Save your decisions.** Turn corrections you keep making into a short, reusable guide. Say what to preserve and when to ask, and rewrite rules that conflict or fire too widely.
- **Work in passes.** Diagnose, choose an edit, then read the result. Keep the original, and check both meaning and formatting before you accept a change.
</div>

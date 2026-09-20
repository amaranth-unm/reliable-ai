---
title: AI as Editorial Assistant
layout: base
position: 1
date: 2026-09-23
kicker: Session 1 · September 23, 2026
summary: "Treat AI as an eager but naive editor: teach it what to look for, tell it whose eyes to read with, and write down the rules so you don't have to repeat yourself."
thumbnail: "/assets/images/aldine-colophon-1502.jpg"
header-image: "/assets/images/aldine-colophon-1502.jpg"
header-tier: section
header-filter: etching
header-title: AI as Editorial Assistant
tags:
  - editing
  - prompting
  - getting started
workshop_mode: true
---

**In the room?** Work down the page. Each step has a prompt you can copy with one click. **Reading this afterwards?** Same steps — the timings are the only thing you can ignore.
{: .lead}

<div class="rule" markdown="1">
**AI reads. You write.**
</div>

Everything below is a way of teaching a reader what to look for. None of it is a way of getting something written. That distinction is the whole session, and it's also what makes this work defensible when a journal, a department, or a student asks what the machine did.

## Why editing is the place to start

Most people meet these tools by asking for something they can't check — a summary of a literature they haven't read, a draft in a genre they're still learning. There's no way to tell a good answer from a merely plausible one, so you either trust it or you don't, and neither is a skill.

Editing is different. **You are the expert on your own paragraph.** When the machine tells you your third sentence is confusing, you know whether it's right. That makes editing the one place where the feedback loop actually closes — where you can build calibrated judgment about what these tools are good for before you rely on them for anything you can't verify.

It also inverts the thing most people are worried about. The fear is that AI writes for you. Used as an editor, it doesn't write anything at all.

## Before you start

- **A laptop**, and an AI assistant open in a browser tab. Claude, ChatGPT, Gemini, Copilot — any of them. Everything here works on a free account.
- **One paragraph of your own writing.** A draft, an abstract, a syllabus policy, a grant blurb, a cover letter. Something with real stakes reads better than something invented for practice. No paragraph? Take one from the [practice texts]({{ site.baseurl }}/practice-texts).
- **One thing to leave out:** other people's unpublished work, student writing with names attached, anything under embargo or covered by an IRB protocol. When in doubt, use a paragraph of your own instead.

<h2 class="step" id="step-1"><span class="step-clock">0:05 — 8 minutes</span><br>1. Start with the bad version</h2>

Paste your paragraph, then send this and nothing else.

{% include prompt.html id="baseline" %}

Now look hard at what came back, because this is the baseline everything else improves on. Most people find some version of the following:

- It **rewrote** rather than commented — so you're now proofreading its prose instead of writing yours.
- It **flattened the hedges**. "Suggests" became "demonstrates." The qualification you put there on purpose is gone.
- It **swapped your terminology** for more common synonyms, including the term of art you chose deliberately.
- It **added connective tissue** — *Moreover*, *Furthermore* — that papers over a gap instead of naming it.
- It **complimented you first**, which tells you nothing.

None of that is malfunction. You asked an eager, well-read, thoroughly naive assistant to edit an unlabelled paragraph, so it guessed at your genre, your audience, and your purpose, and filled the gaps with an average of everything it has read. **Everything that follows is a way of not making it guess.**

<h2 class="step" id="step-2"><span class="step-clock">0:13 — 12 minutes</span><br>2. Teach it to read like you do</h2>

Think of it as a bright first-year TA on day one. Capable, genuinely well read, no idea what matters in your field or what this particular piece is trying to do. You wouldn't hand that person a paragraph and say "edit this." You'd brief them.

A brief needs five things: **what this is**, **who reads it**, **what it's trying to do**, **what you're worried about**, and **what not to touch**. Then the move that changes everything — ask for a reading, not a rewrite.

{% include prompt.html id="editorial-brief" %}

Compare it against your baseline. The comments usually get specific, and — more importantly — it stops handing you replacement prose.

When a comment sounds plausible but vague, don't accept it and don't argue with it. Make it point:

{% include prompt.html id="quote-it" %}

This is the single most transferable habit in the session. **No quotation, no finding.** A tool that can't show you the text it's talking about is generating something that sounds like criticism, and you've just caught it — without needing to know anything about how the model works.

One more, because it will flatter you by default:

{% include prompt.html id="anti-sycophancy" %}

Never ask *is this good?* A yes-or-no question buys you praise. Ask for a ranking and something has to come last.

<h2 class="step" id="step-3"><span class="step-clock">0:25 — 12 minutes</span><br>3. Assign reader roles</h2>

You already do this. When you revise, you imagine someone reading — the reviewer who'll object, the student who'll misread, the editor who's in a hurry. You can hand that imagined reader over explicitly, and get a different reading each time.

Same paragraph, same brief. Change only who's reading. **Run at least two**, and don't let any of them fix anything.

{% include prompt.html id="role-reviewer" %}

{% include prompt.html id="role-outsider" %}

{% include prompt.html id="role-panelist" %}

Then pick the one that fits the work you actually brought:

{% include prompt.html id="role-desk-editor" %}

{% include prompt.html id="role-confused-student" %}

{% include prompt.html id="role-grader" %}

### The part that matters

Now put the readings side by side.

{% include prompt.html id="compare-readers" %}

Two things come out of this, and the second one is why it's here.

The practical payoff: disagreement between readers usually marks a decision you haven't made. If the specialist wants more evidence and the outsider wants less detail, you haven't settled who this paragraph is for — and no amount of editing fixes that, because it isn't a sentence problem.

The bigger payoff: **you just watched the output change because you changed the framing, not because the text changed.** What comes back isn't the answer, it's an answer, contingent on what you asked and who you said was asking. That's the most useful thing to understand about these tools, and it's why comparing beats accepting — in editing, and in everything else you'll use them for.

<h2 class="step" id="step-4"><span class="step-clock">0:37 — 8 minutes</span><br>4. Write the rules down</h2>

If you've typed the same instruction twice, it should be a file. This is the step that turns chatting into a workflow, and it's the one thing to leave with today.

Start by having it describe your style back to you, from evidence:

{% include prompt.html id="style-extract" %}

It will get part of this wrong — it tends to mistake caution for vagueness, and it will miss the habits you'd most like named. **Correcting it is the point.** Ten minutes of arguing with a description of your own prose is how the style sheet stops being its and starts being yours.

Then add the negative rules, which in practice do more work than the positive ones:

{% include prompt.html id="style-never" %}

Finally, put the standing instruction at the top, so the editorial stance doesn't have to be re-established every time:

{% include prompt.html id="standing-instruction" %}

**Where to keep it.** A plain text file you paste at the top of a conversation works completely and depends on nothing. If you want it applied automatically, most tools have somewhere to put it — a Project in Claude, custom instructions or a custom GPT in ChatGPT, a Gem in Gemini. Start with the text file. Upgrade later, or never.

<h2 class="step" id="takeaways"><span class="step-clock">0:45 — the last five minutes</span><br>What to take with you</h2>

Everything above was editing. None of these are:

- **Context beats cleverness.** There are no magic words. There is saying what this is, who it's for, and what counts as good — which is information only you have.
- **Ask for diagnosis before you ask for a cure.** "Tell me what you notice" keeps you making the decisions. "Fix this" hands them over.
- **Make it quote.** If it can't point to the text, the finding isn't real. This is how you check a tool you don't understand, using only knowledge you already have.
- **Change the frame and compare.** One answer looks like the answer. Two answers show you it was contingent all along, and the gap between them is where the real problem lives.
- **Write down what works.** A prompt you've used twice belongs in a file.
- **Never ask whether it's good.** Ask what's weakest. Yes-or-no questions get you flattered.
- **You keep the pen.** Not a rule about integrity — a rule about quality. The judgment is the part you can't delegate, and it's the part that was always the work.

## Take the session with you

- The full [prompt library]({{ site.baseurl }}/prompts) — everything above, in one page, still copy-able.
- The [practice texts]({{ site.baseurl }}/practice-texts), if you want to run the whole sequence again on something low-stakes.
- <a href="{{ site.baseurl }}/assets/posters/sept-23-amaranth-ai-brown-bag-flyer.pdf">The session flyer</a> (PDF).

Questions that came up in the room get added here after the session. If something didn't work on your machine or your writing, tell us — that's the most useful thing we can put on this page.

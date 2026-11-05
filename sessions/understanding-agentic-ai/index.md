---
title: Understanding Agentic AI
layout: base
position: 4
kicker: Workshop draft
summary: "Build a small literature review with an AI agent, one step at a time, so that what it produces takes less time to check."
note: "Bring a laptop. The presenter runs the agent; if you already use one, you can build the same review alongside."
published: false
thumbnail: "/assets/images/stradanus-press-1600.jpg"
header-image: "/assets/images/stradanus-press-1600.jpg"
header-tier: section
header-filter: etching
header-position: center right
header-opacity: 0.18
header-title: Understanding Agentic AI
header-subtitle: "An AI can write a literature review in a minute, and checking it can take hours. Use an agent to build the review in steps whose results are each quick to check."
header-caption: "Jan van der Straet (Stradanus), <i>Impressio Librorum</i>, from <i>Nova Reperta</i>, engraved by Joannes Galle. Museum Plantin-Moretus, public domain."
tags: [agents, research, literature review]
workshop_mode: true
redirect_from: /sessions/understanding-agentic-ai.html
---

{% comment %}
Authoring references: SESSION-STYLE.md and sessions/audit-trails-for-ai-agents/index.md.
Separate introductory workshop; no meeting date assigned.
The "Save as …" prompts are the instruction files. scripts/build-agentic-workspace.py
packages them, with the prepared CLAUDE.md, into the download in step 6.
{% endcomment %}

{% include nav/scrollspy-toc.html %}

Work down this page during the workshop or return to it later. The presenter builds the review live, one file at a time, and you can build the same folder alongside.
{: .lead}

<div class="rule" markdown="1">
**Build the review so that every claim leads back to a saved PDF and a page.**
</div>

## Introduction
{: .step #introduction}

### Why a literature review is the place to start

A literature review is a task most researchers know well and one of the
most tempting to hand to AI. It is also one where you can judge the result:
you know whether a summary represents an article, and whether two authors
have been blurred together.

This session builds a small review with an AI agent, one step at a time.
Each step starts from a problem you would run into checking an ordinary AI
review and adds one thing that makes the result quicker to check. Along the
way you will see what makes a system agentic, and how to direct one.

### Before you start

- **A laptop** to follow the page and open the files the agent writes.
- **A way to read the folder.** [Obsidian](https://obsidian.md/) is free on
  Mac and Windows. Choose **Open folder as vault** and pick your
  `lit-review` folder. It shows files as the agent writes them, displays the
  notes formatted and can open a PDF beside a note, which helps when you
  check an idea against its page. A code editor such as
  [Visual Studio Code](https://code.visualstudio.com/) works too.
- **An AI chat assistant** such as Claude, ChatGPT, Gemini or Copilot, for
  the first exercise.
- **An agent that works in a folder, if you already use one**, such as
  Claude Code or Codex. You don't need one: the presenter runs every step.

If you would rather not write the files as you go, step 6 has a
[download of the starting folder](#step-6): every file you write during the
session, ready for the agent. Open each file as it comes up.

<div class="reminder" markdown="1">
Give an AI service only PDFs you have permission to share, such as open-access articles like the ones in this session's brief.
</div>

## What makes AI agentic
{: .step #what-agentic-means}

**In this workshop, an agent is a system that can choose intermediate
actions, use tools and respond to what those actions return while pursuing
your goal.** That is a working definition; definitions vary. A plan written
in a reply is useful, but you need to see actions and results to know what
was carried out.

A browser window does not tell you how agentic a system is. A chat
interface can front a system with tools, and a desktop agent can be used for
a single reply. Look at how the work proceeds.

| Way of working | What to look for | When it helps |
|---|---|---|
| Question and answer | You ask, receive text and decide the next move. | Discussing an idea, interpreting a passage or choosing a direction. |
| A fixed workflow | A specified sequence runs, such as extract, summarize, format. | Repeating a task with stable steps and requirements. |
| An agent working toward a goal | The system chooses some intermediate actions and changes course using tool results. | Work whose next useful step depends on what it finds. |

The review in this session uses all three. You decide the stages, and
within each one the agent chooses its actions.

<details class="more" markdown="1">
<summary>How the idea of an agent has developed</summary>

Agent systems have a history long before today's language models. These
selected milestones show how ideas about planning, choosing and carrying out
actions changed. They are not a claim about who first used the phrase
“agentic AI”.

| Period | What happened | Why it matters for today's agents |
|---|---|---|
| 1966–1972 | Researchers at SRI built Shakey, a wheeled robot given tasks in simple English. It looked at its surroundings with a camera, planned a sequence of moves, such as pushing a box into another room, and carried them out. [SRI's account](https://www.sri.com/case-study/the-man-the-myth-the-legend-meet-shakey-the-robot-the-worlds-first-ai-based-robot/) | Giving a system a goal and letting it work out the steps came decades before chatbots. |
| 1995 | Michael Wooldridge and Nicholas Jennings surveyed research on “intelligent agents.” Their minimal definition named four properties: the system acts without step-by-step direction, responds to changes around it, takes initiative toward its goals and interacts with people or other agents. [Their account of agency](https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/ker95/subsubsectionstar3_1_1_1.html) | The four properties still work as a checklist. “Agent” has long covered systems with very different designs and degrees of independence. |
| 2022–2023 | Two research papers connected language models to actions. ReAct had a model alternate between writing out its reasoning and taking an action, such as a search, then use what came back to choose the next step. Toolformer taught a model when to call outside tools, such as a calculator or a search engine, and how to use the results. [ReAct](https://arxiv.org/abs/2210.03629), [Toolformer](https://arxiv.org/abs/2302.04761) | A language model could now be one part of a loop: act, read the result, act again. You watch that loop in step 1. |
| 2024 | Anthropic's guide to building agents separated *workflows*, where the steps are fixed in advance by the people who build them, from *agents*, where the model decides how to proceed and which tools to use. It called both “agentic systems” and advised starting with the simplest arrangement that works. [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Ask who picks the next step: you, a fixed script or the model. This session's review fixes the stages and lets the agent choose its actions within each. |
| Current tools, checked October 11, 2026 | Agent tools now work in a folder of files, keep notes on a project between sessions and run long tasks in repeated cycles of working, checking and revising. Some can also operate a web browser. OpenAI documents this for Codex and for ChatGPT's browser. [Codex's task loop](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex), [browser capabilities](https://learn.chatgpt.com/docs/browser) | The review in this session runs in this kind of environment. You watch the agent search, save and read files and revise them, and you can steer it between steps. |

For a researcher, the practical change is connecting a natural-language task
to a flexible sequence of work across files and software. You describe the
result you want, let the system choose some intermediate steps and steer it
using what it creates. The model, tools and environment work together, and
what a system can do depends on that combination.

The adjective *agentic* now often emphasizes delegated action in systems
built around language models, and its scope varies across researchers and
products. In current tools it is partly a practical question of which
decisions and permissions you hand over. None of these uses establishes
human-like intentions or understanding.

</details>

## The verification tax
{: .step #verification-tax}

Send this to any chat assistant, the way you might on an ordinary day.

{% include prompt.html id="agentic-baseline" %}

In under a minute you have a review: five sources, what each argues and how
they relate. It reads well. **Before you could rely on it, you would have to
check:**

- that each source exists, and the citation leads to it;
- whether the assistant read each one, and how much of it;
- that each claim about an article is in the article;
- that each author's ideas are kept separate;
- that the connections between articles are ones the articles support;
- that the set isn't missing something obvious or leaning on one author.

None of this assumes the AI is bad at reviews. You would check a new
research assistant's review the same way, and how much checking is enough
depends on your field, what you will use the review for and your own
standards. Call it the verification tax. For five sources it can take longer than
reading them yourself, which leaves you wondering what the review saved
you. The rest of this session reduces the tax. Each step adds something
that moves part of the checking into the work itself, and ends with the
smaller, quicker checks that remain. Which of them you do, and how
thoroughly, is up to you. An agent can do this where a single reply can't,
because the work takes several steps, each depending on what the last one
returned.

## 1. Give the agent a bounded set of readings
{: .step #step-1}

The review in the chat drew on sources you can't see. **A review built from
four PDFs saved in your folder can be checked against those four PDFs.** So
the first job is to get the readings.

Before the agent can search, it needs to know what it is looking for and
when to stop. A **brief** is a short file that says so: the question, what
counts as a relevant source, and limits such as how many sources and how
many searches. It does the job a one-line prompt leaves to the agent's
guesswork. **The limits also bound what you will have to check**: four
sources, not however many the agent decides to find. And because the brief
is a file, the agent can reread it at every step, and so can you.

Make a folder called `lit-review` on your desktop and save this in it as
`brief.md`.

{% include prompt.html id="agentic-brief" %}

The prompt below asks the agent to give each source an **ID**: S01, S02
and so on, in the order it saves them. Titles are long and author names
repeat, so the agent uses the ID everywhere it refers to a source: the PDF's
filename, its note, every citation in the synthesis and every finding the
checker writes. **When every file uses the same ID, you can follow one
source through the whole folder**, and so can a new session that has never
seen this conversation. The same idea applies to anything the agent will
need to refer back to later; step 3 gives each point in the synthesis an ID
too.

Start your agent in the folder. In Claude Code, open a terminal in
`lit-review` and type `claude`. Then send this.

{% include prompt.html id="agentic-search" %}

Watch for one cycle: an action, the result it returns and a next action
chosen because of that result. A search turns up a promising article, the
download returns a login page instead of a PDF, and the agent deletes the
file, records the article as a lead and searches again. **That choice of a
next step, made from what the last step returned, is what the definition
above describes.**

Your folder now holds:

```text
lit-review/
  brief.md
  sources.md     every search, then one entry per source
  pdfs/          S01-surname.pdf … S04-surname.pdf
```

<div class="tax" markdown="1">
These are the checks you'd give a research assistant who fetched articles for you. How many you do depends on what you'll use the review for.

- Open each PDF. Is it the article its entry in `sources.md` names?
- Does the set fit the brief: two sources about teaching, no more than two
  by one author?
- Do the searches in `sources.md` match the ones you watched it run?
</div>

<div class="keypoint" markdown="1">
Have the agent save the readings in your folder before it writes anything about them. Whether the sources exist is then off your list, and what's left is a quicker check: is each PDF the article it names?
</div>

## 2. Tell it how to read, then get one note per source
{: .step #step-2}

You have the readings. Will the agent read them the way you would? A note
that summarizes without page numbers sends you back to reread the whole
article to check one claim. **Written instructions decide what every note
contains**, including the page behind each idea.

Make a folder called `instructions` inside `lit-review`. It will hold all
the instructions you write today. Save this in it as `reading.md`.

{% include prompt.html id="agentic-reading" %}

Change one rule to fit how your field reads. A historian might ask what
evidence each author uses. A literary scholar might want key phrases quoted
exactly. Someone planning a course might ask whether the article addresses
students directly. Then send this. Start with two sources; step 4 explains
why.

{% include prompt.html id="agentic-read-two" %}

```text
lit-review/
  instructions/
    reading.md
  notes/         S01-surname.md, S02-surname.md
```

<div class="tax" markdown="1">
You'd ask the same of anyone's notes, your own included. One idea per note may be enough for getting oriented; a review you'll publish deserves more.

- Pick one key idea in each note and go to the page it gives. Is the passage
  there, and does it say that?
- Does each note say which pages were read?
- Is “the argument in its own terms” the author's emphasis, or has it been
  tilted toward our question?
- Did the note follow the rule you changed?
</div>

<div class="keypoint" markdown="1">
Require a page for every key idea, so that checking a claim means opening one page. If notes keep missing something, change the instructions rather than correcting each note.
</div>

## 3. Relate the notes in a synthesis
{: .step #step-3}

The most expensive checks in the chat review were the connections. “These
two authors agree” means reading both articles to find out whether they do,
and whether either one says so. **Ask for every connection to name the claim
at stake, give pages in both sources and say who made the connection**: the
authors, by citing or responding to each other, or the agent.

The instructions also give each point in the synthesis its own ID, such as
P03, which it keeps through every revision. The log can then say “P03
weakened” and the checker can say which point it disputes, without quoting
paragraphs at you.

Save this in the `instructions` folder as `synthesis.md`.

{% include prompt.html id="agentic-synthesis" %}

{% include prompt.html id="agentic-synthesize" %}

```text
lit-review/
  synthesis.md       version 1, from two notes
  synthesis-log.md
```

<div class="tax" markdown="1">
These are the questions you'd put to a colleague's synthesis. How far you take them depends on what's riding on it.

- Does each overlap give pages in both notes?
- Which connections are labeled as the agent's, and which as the authors'?
  Check one the authors are said to make.
- Is any author recruited to a position the note doesn't support?
</div>

With only two sources, “what only one offers” is easy to get right. The
next step puts it to the test.

<div class="keypoint" markdown="1">
Ask for the claim, both pages and who drew each connection. Treat a connection the agent drew as a question to read yourself.
</div>

## 4. Add the rest and revise as you go
{: .step #step-4}

Researchers don't read everything and then write. They read a few things,
form a picture and revise it as each new reading changes it. The synthesis
instructions ask the agent to do the same: save the old version, revise and
log what changed. **When the synthesis changes, you check the change, not
the whole synthesis again.**

This time each article goes to a separate helper agent. A helper starts
fresh with one PDF and the reading instructions. It hasn't seen the other
notes or the synthesis, so it can't bend a new article to fit the picture
so far, and two helpers can run at once.

{% include prompt.html id="agentic-continue" %}

Watch the transcript. You see each helper start and finish with a short
report, but not every page it reads. Handing work off puts less of it in
view, so the note is what you check.

```text
lit-review/
  notes/         … S03-surname.md, S04-surname.md
  synthesis.md   version 2
  history/
    synthesis-v1.md
```

<div class="tax" markdown="1">
Revising in steps shrinks these checks to what changed. How closely you read the log is your call.

- Read the new entry in `synthesis-log.md`. Does each change name a point
  ID and trace to S03 or S04?
- Did a claim that only one source offers something survive the new notes?
- Check one key idea in a helper's note against its page.
</div>

The earlier version stays in `history/` in case you ever want to go back to
it. With more sources, the agent repeats this loop: two notes, a revision, a
log entry.

<div class="keypoint" markdown="1">
Have the agent keep the old version and log each revision, so the log tells you where to look. Check what changed instead of rereading the whole synthesis.
</div>

## 5. Have one agent check another
{: .step #step-5}

You still can't check every claim yourself. A checker that didn't write the
synthesis can do a first pass, going back to the PDFs rather than the
notes. **You then check its findings, which is a much shorter list.**

Save this in the `instructions` folder as `checker.md`.

{% include prompt.html id="agentic-checker" %}

{% include prompt.html id="agentic-check" %}

```text
lit-review/
  instructions/
    checker.md
  checks.md
```

<div class="tax" markdown="1">
A checker's findings are a second opinion. Which ones you follow up, and how far, is your decision.

- Open one finding and go to the page it names. Is the checker right?
- Its coverage section says what it checked and what it couldn't. What is
  still unchecked?
- Decide which findings to accept. The agent was told not to apply them.
</div>

The checker is the same model with different instructions, and it can be
wrong too. Keep one agent on the synthesis itself: two revising it at once
would overwrite each other, and the order of revisions is what the log
records.

<div class="keypoint" markdown="1">
Add a separate helper when it solves a problem you can name, such as a check that doesn't rely on the agent's account of its own work. Check its findings against the page before you accept them.
</div>

## 6. Write the workflow down and pick up later
{: .step #step-6}

Everything about the order of the work lives in this conversation. Next
time you would type it all again. Ask the agent to write it down in a file
it reads at the start of every session.

{% include prompt.html id="agentic-workflow" %}

Compare its `CLAUDE.md` with what you did, and with the
[prepared version]({{ site.baseurl }}/assets/agentic-ai/CLAUDE.txt). Then
quit the agent, start a new session in the same folder and send this.

{% include prompt.html id="agentic-resume" %}

The new session has none of the earlier conversation. The files carry the
project forward, and the agent still has to read them.

<div class="tax" markdown="1">
Read a workflow file the way you'd read a colleague's methods note: once, carefully, and again when the work changes.

- Does `CLAUDE.md` describe what you actually did, in the order you did it?
- Does the new session's account match `progress.md` and the files?
- Does it name the right next action?
</div>

Here is the whole folder:

```text
lit-review/
  CLAUDE.md          the workflow, read at the start of every session
  progress.md        what exists and what's next
  brief.md
  instructions/
    reading.md
    synthesis.md
    checker.md
  sources.md
  pdfs/
  notes/
  synthesis.md
  synthesis-log.md
  history/
  checks.md
```

[Download the starting folder]({{ site.baseurl }}/assets/agentic-ai/lit-review-starting-folder.zip).
It holds the files you write during the session: `brief.md`, the three files
in `instructions/`, a prepared `CLAUDE.md` and an empty `progress.md`. It has
no articles, notes or synthesis; the agent creates those when it runs. Start
an agent in the folder and ask it to run stage 1 in `CLAUDE.md`. In Claude Code, the files in `instructions/` can also be
packaged as skills and helper-agent definitions, which load on their own and
can be limited to particular tools. Plain files work in any agent and are
easier to read.

With a partner, choose one task from your own work that you could build the
same way. What would bound the materials? What would the instructions
require, so that checking takes less time? What would you still check
yourself?

<div class="keypoint" markdown="1">
Ask the agent to write the workflow and current state into files, so the next session doesn't depend on this conversation. Start a new session and check that it can continue from them.
</div>

## What to take with you
{: .step #takeaways}

| Step | What it takes off your list | What you still check |
|---|---|---|
| Bounded readings | Whether sources exist; getting hold of them | Each PDF is the article it names |
| Reading instructions | Rereading a whole article to check one claim | One key idea per note, at its page |
| Synthesis instructions | Guessing who made a connection | Connections attributed to the authors |
| Revising in pairs | Rereading the whole synthesis | What the log says changed |
| A separate checker | A first pass against the PDFs | Its findings, at their pages |
| A written workflow | Retyping the process | That a new session's account matches the files |

<div class="takeaways" markdown="1">
Use these habits when you hand research work to an agent:

- **Bound the materials.** Have the agent save what it will work from in your folder, so you can check against it.
- **Put instructions in files.** How to read, how to relate and how to check, written once and changed when the results miss something.
- **Give everything an ID.** Sources, points and findings each get a short label used in every file, so you can follow one through the folder.
- **Ask for the page behind every claim.** A claim with a page takes a minute to check; one without takes an article.
- **Check the changes.** Keep earlier versions and a log, and read what changed.
- **Add a helper agent for a reason you can name**, such as reading without the running picture or checking without the agent's own account.
- **Ask who chooses the next step.** Look for what the agent decided, what it acted on and what you still decide.
</div>

---
title: Understanding Agentic AI
layout: base
position: 4
kicker: Workshop draft
summary: "Watch an AI agent carry out a small literature review, from finding articles to revising a synthesis, and see how instructions, skills and helper agents shape what it does."
note: "Bring a laptop. The presenter runs the agent; if you already use one, download the starter folder and run the same review."
published: false
thumbnail: "/assets/images/stradanus-press-1600.jpg"
header-image: "/assets/images/stradanus-press-1600.jpg"
header-tier: section
header-filter: etching
header-position: center right
header-opacity: 0.18
header-title: Understanding Agentic AI
header-subtitle: "An agent chooses its next step from what the last one returned. Give it a result to reach and instructions it can read, then check what it leaves in the folder."
header-caption: "Jan van der Straet (Stradanus), <i>Impressio Librorum</i>, from <i>Nova Reperta</i>, engraved by Joannes Galle. Museum Plantin-Moretus, public domain."
tags: [agents, research, literature review]
workshop_mode: true
redirect_from: /sessions/understanding-agentic-ai.html
---

{% comment %}
Authoring references: SESSION-STYLE.md and sessions/audit-trails-for-ai-agents/index.md.
Separate introductory workshop; no meeting date assigned.
Starter folder source: workshop-drafts/understanding-agentic-ai/lit-review/; run scripts/build-agentic-workspace.py after editing it.
{% endcomment %}

{% include nav/scrollspy-toc.html %}

Work down this page during the workshop or return to it later. The presenter runs the review live. The starter folder and prompts let you run the same review with an agent you already use.
{: .lead}

<div class="rule" markdown="1">
**Give the agent a result to reach, instructions it can read and a way for you to check its work.**
</div>

## Introduction
{: .step #introduction}

### Why a literature review is the place to start

Ask a chat assistant for a literature review and you will have a few
paragraphs and a list of citations in under a minute. The work a review
involves is missing from that reply: searching, finding that an article is
paywalled and choosing another, saving the PDFs, reading each one and
revising your sense of the field as each new article changes it. **Each of
those steps depends on what the one before it returned**, and that is the
kind of work an agent can take on.

It is also work you know how to judge. You can tell whether a note
represents an article, whether two authors have been blurred together, and
whether a claim that only one article makes something survives reading the
others. That makes a review a good place to see what an agent does and where
your judgment still comes in.

The review uses a real question:

> How are the humanities relevant to using and teaching AI?

The practical question for the hour is how much of a task you want a system
to handle. A good delegation leaves it room to choose an approach while
making the result, boundaries and stopping point clear.

### What you're working with

- A chat reply can describe a literature review. An agent working in a
  folder can carry one out. Compare what exists afterwards. (Step 1)
- The agent reads its instructions from files in the folder, so you change
  how it works by editing a file. (Step 2)
- It chooses its next action from what the last one returned, such as a
  download that turns out to be a login page. (Step 3)
- A skill shapes how it reads, and you can check a note against the PDF.
  (Step 4)
- It can hand work to helper agents that start fresh, and revise a synthesis
  as their notes arrive. (Step 5)
- A new session can pick up the project from the files alone. (Step 6)

### Before you start

- **A laptop** to follow the page and open the files the agent writes.
- **An AI chat assistant** such as Claude, ChatGPT, Gemini or Copilot, for
  step 1.
- **An agent that works in a folder, if you already use one.** The starter
  folder is set up for Claude Code. You don't need one: the presenter runs
  every step.

<div class="reminder" markdown="1">
Give an AI service only PDFs you have permission to share, such as open-access articles like the ones in the backup set in step 3.
</div>

## What makes AI agentic
{: .step #what-agentic-means}

**In this workshop, an agent is a system that can choose intermediate actions,
use tools and respond to what those actions return while pursuing your goal.**
That is a working definition for the exercise. Definitions vary; the history
below explains some of that variation. A plan written in a reply is useful,
but you need to see actions and results to know what was carried out.

### How the concept has changed

Agent systems have a history before today's language models. These selected
milestones show changes in how actions are planned, chosen and connected to
the world. They are not a claim about who first coined “agentic AI”.

| Period | A development to notice | Connection to today's exercise |
|---|---|---|
| 1966–1972 | SRI's Shakey combined perception, planning and actions to carry out tasks in a physical environment. [SRI's account](https://www.sri.com/case-study/the-man-the-myth-the-legend-meet-shakey-the-robot-the-worlds-first-ai-based-robot/) | Giving a goal and letting a system work out actions predates conversational AI. |
| 1995 | Wooldridge and Jennings surveyed agents through autonomy, responsiveness to an environment, initiative and interaction with others. [Their account of agency](https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/ker95/subsubsectionstar3_1_1_1.html) | “Agent” already covered several architectures and degrees of autonomy. |
| 2022–2023 | ReAct studied language models that interleave planning-related text and actions informed by external results; Toolformer studied learning when and how to call APIs. [ReAct](https://arxiv.org/abs/2210.03629), [Toolformer](https://arxiv.org/abs/2302.04761) | Language models could participate in a tool-and-feedback process, beyond producing a final passage of text. |
| 2024 | Anthropic distinguished fixed workflows from agents whose models choose how to proceed, while using “agentic systems” as a broader category. [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Ask who selects the next step. A fixed sequence and an adaptive process can both be useful. |
| Current tools, checked October 11, 2026 | Agent environments combine tools, saved project state and repeated work/check/revise cycles. OpenAI documents this in Codex and browser control. [Codex's task loop](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex), [browser capabilities](https://learn.chatgpt.com/docs/browser) | Today's review lets you watch an agent search, save and read files and revise them, and steer the work between steps. |

### What's distinctive now

For a researcher, the practical change is connecting a natural-language task
to a flexible sequence of work across files and software. You can describe
the result you want, let the system choose some intermediate steps and steer
it using the artifact it creates. The model, tools and environment work
together; capabilities depend on that combination.

The adjective *agentic* now often emphasizes delegated action in systems
built around language models. Its scope varies across researchers and
products. In the older account, autonomy could describe control over actions
and state; in current tool systems it is also a practical question of which
decisions and permissions the user delegates. These uses do not establish
human-like intentions or understanding.

### Does “agent versus browser chat” still hold?

**A browser window does not tell you how agentic the system is.** A chat
interface can front a system with tools; a desktop application can also be
used for a single text reply. Compare what the current session can do and
how the work proceeds. Tool access, file access and permissions vary.

| Way of working | What to look for | When it helps |
|---|---|---|
| Question and answer | You ask, receive text and decide the next move. | Discussing an idea, interpreting a passage or choosing a direction. |
| A fixed workflow | A specified sequence runs, such as extract, summarize, format. | Repeating a task with stable steps and requirements. |
| An agent working toward a goal | The system chooses some intermediate actions and changes course using tool results. | Work whose next useful step depends on what it finds. |

These can occur inside the same product or project. A system may use a fixed
procedure for part of a task and choose its next action elsewhere. More
autonomy adds value when it saves you from coordinating useful intermediate
work; it can also spend time on an approach you would have rejected.

**Try this with a partner:** an assistant writes a plan; a script runs the
same report nightly; a system reads a folder and repairs a broken link after
testing it. Which example shows adaptive action? What additional information
would you need about the others?

## Set up the workspace
{: .step #workspace}

Download and extract the [starter folder]({{ site.baseurl }}/assets/agentic-ai/lit-review-starter.zip).
It holds instructions and no articles; the agent finds those in step 3.

A **workspace** is the place where a project keeps its materials,
instructions and results. Here it is an ordinary folder. The agent reads its
instructions from files in the folder at the start of every session, so
**you change how it works by editing a file**, and the change applies to
every task that follows.

```text
lit-review/
  CLAUDE.md                     the workflow the lead agent follows
  brief.md                      question, scope, limits, when it's done
  progress.md                   where the project stands
  .claude/
    skills/
      read-article/SKILL.md     how to read one article
      relate-articles/SKILL.md  how to relate the notes
    agents/
      reader.md                 a helper that reads one PDF
      checker.md                a helper that checks the synthesis
```

By the end of the session the agent has added:

```text
  sources.md          the articles it chose and how it found them
  pdfs/               S01-surname.pdf … S05-surname.pdf
  notes/              one note per PDF, with the same name
  synthesis.md        how the articles relate, revised as notes arrive
  synthesis-log.md    what each revision changed, and why
  history/            earlier versions of the synthesis
  checks.md           the checker's findings
  leads.md            works the articles cite, to consider next
```

The `.claude` folder is hidden because its name starts with a dot. To see
it, press **Cmd+Shift+.** in a Finder window on a Mac, or choose **View →
Show → Hidden items** in Windows File Explorer. A code editor such as
[Visual Studio Code](https://code.visualstudio.com/) lists it in the
sidebar. Every file is plain text, and you can also read them on this site:
[CLAUDE.md]({{ site.baseurl }}/assets/agentic-ai/files/CLAUDE.txt),
[the brief]({{ site.baseurl }}/assets/agentic-ai/files/brief.txt),
[the reading skill]({{ site.baseurl }}/assets/agentic-ai/files/read-article-skill.txt),
[the relating skill]({{ site.baseurl }}/assets/agentic-ai/files/relate-articles-skill.txt),
[the reader]({{ site.baseurl }}/assets/agentic-ai/files/reader-agent.txt) and
[the checker]({{ site.baseurl }}/assets/agentic-ai/files/checker-agent.txt).

**To follow along,** open a terminal in the folder and start Claude Code
with `claude`. Other agents read a similar instructions file under another
name (Codex reads `AGENTS.md`), so copy `CLAUDE.md` to that name. The skill
and helper-agent files are in Claude Code's format. In another tool, point
the agent at them by path, or let the lead agent read every article itself
in step 5.

**About the examples.** The starter folder's instructions were written for
this workshop on November 4, 2026. The articles are real open-access
publications, chosen by the agent during the run. This page shows no
recorded agent output. What you see is the presenter's live run, or your
own.

### See a workflow across the files

A **workflow** is how a task moves through stages. Here the search produces
`sources.md` and the PDFs, the PDFs produce notes, the notes produce the
synthesis, and the checker reads the synthesis against the PDFs. Each result
feeds the next stage and stays in the folder where you can open it.

The stages themselves are fixed: `CLAUDE.md` lists them in order. Within
each stage the agent chooses its actions: which search to run, what to do
when a download fails, which pages to go back to. **This review combines a
fixed workflow with an agent's choices**, the second and third rows of the
table above, as many useful agent setups do.

## 1. Ask for a review and look at what comes back
{: .step #step-1}

Send this to any chat assistant, the way you might on an ordinary day.

{% include prompt.html id="agentic-baseline" %}

Now look at what exists after the reply. You have text: a summary and
perhaps a list of citations. Ask of it:

- Did it search, or answer from what it already knew? Does it say which?
- Does each citation open, and does it lead to the work it names?
- Could you tell which ideas belong to which author?
- If you wanted to read one of the articles, where is it?

A request for a review returns text shaped like a review, which is what you
asked for. The rest of the session asks for the steps behind a review
instead, so that each one leaves something in the folder you can open.

<div class="keypoint" markdown="1">
Ask what exists after a reply: text, files, or something you can open and check. A reply shaped like a review still needs the steps behind one.
</div>

## 2. Write the brief and the reading skill
{: .step #step-2}

Open `brief.md`. It names the question, the scope, the limits (five
sources, at least two about teaching, no more than five searches) and what
counts as done. Then open the reading skill,
`.claude/skills/read-article/SKILL.md`. It sets out what every note
contains: the argument in the author's own terms, key ideas with page
numbers, what the author says is new, and what the article offers people
who use AI and people who teach with it.

Change one rule in the skill to fit how your field reads. A historian might
ask what evidence each author uses. A literary scholar might want key
phrases quoted exactly. Someone planning a course might ask whether the
article addresses students directly. The presenter makes one such change
live.

Then start the agent in the folder and send this. It asks the agent to say
what it can do before it does anything.

{% include prompt.html id="agentic-plan" %}

Check its answer against the folder. Did it read the brief and both skills?
Does it name the tools it has for searching, downloading, reading PDFs,
writing files and starting helper agents? **A confident plan does not mean
the tools to carry it out are available.**

### Skills, tools and the parts around the model

A **skill** is a set of instructions with a description of when to use them.
The agent reads the description at the start of a session and loads the
full instructions when a task matches. The reading skill doesn't let the
agent read a PDF; its tools do that. The skill says how to read, and editing
it changes every note written afterwards. That is why it carries a date.

| Part | In this review |
|---|---|
| The model | Produces text and chooses next actions from the task and what it can see. |
| The brief | The question, scope, limits and when the work is done. |
| Standing instructions | `CLAUDE.md`: the stages, file names and rules, read at the start of every session. |
| Skills | How to read one article, and how to relate the notes. |
| Tools | Searching the web, downloading, reading PDFs, writing files and starting helper agents. |
| Saved project state | `progress.md` and the files written so far. |
| The agent environment | The software that connects the model with tools, files and permissions and decides when it stops; here, Claude Code. |

Your brief guides the work; it does not grant a tool that the environment
lacks. You may see *agent harness* used for the last row.

<div class="keypoint" markdown="1">
Put the result, limits and stopping point in a brief and how to read in a skill. Ask the agent which tools it has before it starts.
</div>

## 3. Let the agent find and save the sources
{: .step #step-3}

Send this, and keep the transcript and the folder side by side.

{% include prompt.html id="agentic-search" %}

Watch for one cycle: an action, the result it returns and a next action
chosen because of that result. A search turns up a promising title, the
download returns a login page instead of a PDF, and the agent deletes the
file, records the article as a lead and searches again. **That choice of a
next step, made from what the last step returned, is what the definition
above describes.** A chat reply can say it searched; here you watch which
searches ran and which files arrived.

Open `sources.md` while it works. Each entry should say which search found
the article and why it fits the brief. Then open one PDF in `pdfs/` and
compare its first page with its entry. Is it the right title and author?

If the search stalls, the brief lists five backups. Each link is the PDF
itself, checked on November 4, 2026.

- Lauren M. E. Goodlad, [“Editor's Introduction: Humanities in the Loop”](https://criticalai.org/wp-content/uploads/2023/09/CAI112_01Goodlad_1pp-1-1.pdf), *Critical AI* (2023).
- Seth Perlow, [“Generative Theories, Pretrained Responses: Large AI Models and the Humanities”](https://doi.org/10.1632/S0030812924000518), *PMLA* (2024).
- Fabian Offert and Ranjodh Singh Dhaliwal, [“The Method of Critical AI Studies, A Propaedeutic”](https://arxiv.org/pdf/2411.18833), arXiv (2024).
- Lauren M. E. Goodlad and Sharon Stoerger, [“Teaching Critical AI Literacy: Advice for the New Semester”](https://otear.rutgers.edu/wp-content/uploads/2024/10/TEACHING-CRITICAL-AI-LITERACY.pdf), Rutgers University.
- Clara Nobile et al., [“Beyond STEM: An Educational Framework Proposal for AI Literacy in Humanities Higher Education”](https://ceur-ws.org/Vol-4305/4_paper.pdf), CEUR Workshop Proceedings (2026).

Two of these are by Lauren Goodlad. A synthesis built on them should say
so, and the relating skill in step 5 asks for exactly that.

<div class="keypoint" markdown="1">
Watch for a next action that responds to a result. Open one saved PDF and check that it is the article the register names.
</div>

## 4. Read one article with the skill
{: .step #step-4}

Ask the lead agent to read the first article itself, following the skill.

{% include prompt.html id="agentic-read-one" %}

In the transcript, watch it open the PDF and work through the pages. Then
open the note in `notes/` beside the PDF.

- Does the note have every section the skill asks for, including the rule
  you changed in step 2?
- Pick one key idea and go to the page it gives. Is the passage there, and
  does it say that?
- Is “the argument in its own terms” the author's emphasis, or has it been
  tilted toward our question?
- Does “what the author says is new” name what the article argues against?

The skill shapes the note, and the note is still the agent's reading.
**Check it the way you would check a research assistant's notes: against
the page.** If notes keep missing something you need, change the skill
rather than correcting each note.

<div class="keypoint" markdown="1">
Check one key idea in a note against the page it cites. When notes keep missing something, change the skill.
</div>

## 5. Hand the reading to helper agents and revise as notes arrive
{: .step #step-5}

Now the lead agent hands the other four articles to reader agents, two at a
time, and revises the synthesis after each pair.

{% include prompt.html id="agentic-delegate" %}

### What the helpers do

A **reader** is a separate agent, defined in `.claude/agents/reader.md`. It
starts fresh, with one PDF and the reading skill. It hasn't seen the
conversation so far or the other notes. It can read files and write its
note, and it can't search the web. The lead agent starts two readers at
once and waits for both notes.

Watch the transcript. You see each reader start and finish with a short
report, but not every page it reads, as you did in step 4. **Handing work
off puts less of it in view**, so the note in `notes/` is what you check.

### Watch the synthesis change

After each pair, the lead agent saves the current synthesis in `history/`,
revises `synthesis.md` with the relating skill and adds an entry to
`synthesis-log.md`. The relating skill is where overlap and uniqueness are
worked out: where the articles agree, where they differ, what only one of
them offers and what none of them addresses.

Open `synthesis-log.md` after the second revision.

- What did the second pair change? Look for a point of agreement that
  became a tension, a claim that only one article says something that a
  later article also says, or a gap that a teaching article filled.
- Does each overlap say whether the authors make the connection themselves,
  by citing or responding to each other, or whether the agent drew it?
- Does it say that two articles share an author?

Then compare `history/synthesis-v1.md` with the current `synthesis.md`. The
first version is an account of three articles; the log tells you which of
its claims held once two more arrived. The reader records what an author
says is new, but **whether a contribution is unique is a judgment across
all the notes**, which is why it belongs to the relating skill.

### When several agents help, and when they don't

Splitting the work helps where:

- **Separate readers keep authors separate.** A reader that sees one article
  can't blend it with the one before. Keeping whole PDFs out of the lead
  agent's working context also lets a review grow to twenty articles without
  the lead losing track.
- **A narrow job needs narrow permissions.** The reader can read and write
  files; it can't search the web or change the synthesis.
- **A checker that didn't write the work** reads it with fresh eyes, as in
  step 6.
- **Independent work can run at once.** Two readers finish in about the time
  one takes.

Keep the work with one agent where:

- **The running picture needs one author, revising in order.** Two agents
  revising the synthesis at once would overwrite each other, and the order
  of revisions is part of what the log records.
- **A judgment needs the whole picture.** Whether a source fits the brief,
  or a lead deserves a search, stays with the lead agent and with you.

Helper agents are the same model with different instructions and less
context. More of them does not add expertise. Add one when it solves a
problem you can name.

<div class="keypoint" markdown="1">
Give a helper agent one bounded job and only the files it needs. Keep the running picture with one agent, and read its log of what changed.
</div>

## 6. Check the work and pick up where it left off
{: .step #step-6}

Ask the lead agent to send the synthesis to the checker and compile the
leads.

{% include prompt.html id="agentic-check" %}

The checker is another helper. It starts with only the folder and checks
the synthesis against the PDFs, not the notes. It looks hardest at claims of
overlap and uniqueness: to show that only one article makes a point, it has
to read the others. Its findings go in `checks.md`, and the agent doesn't
apply them. Open one finding and go to the page it names. Deciding which
findings hold up is your job.

`leads.md` lists works the articles cite, with any work cited by two or more
of them marked first. The agent is told to list leads, not to follow them.
**Whether the review grows is your decision.**

### Continue in a fresh session

Quit the agent, start a new session in the same folder and send this.

{% include prompt.html id="agentic-resume" %}

The new session has none of the earlier conversation. Does its account
match `progress.md` and the files? Does it name the next unfinished action?
The files carry the project forward, and the agent still has to read them.

### Choose a task from your own work

With a partner, choose one task you could delegate next. Write down the
result you want, the materials, what the agent may do, how you will check
the result and which decisions you will keep.

| Task | Work an agent might carry through | What you check or keep |
|---|---|---|
| Read into a new topic | Find and save articles, write a note on each and keep a synthesis current. | One key idea against its page; which leads to follow. |
| Prepare a course reading packet | Find open-access readings on a theme and write a short headnote for each. | Whether each headnote represents its reading; the final selection. |
| Clean collection metadata | Compare fields, propose a consistent format and write a cleaned copy. | Record counts and sample changes; ambiguous identifications. |
| Build a research aid | Turn notes into a local search page or timeline. | Try an intended use; judge the categories. |

<div class="keypoint" markdown="1">
Keep the project's state in files a new session can read. Decide yourself which checker findings and leads to act on.
</div>

## What to take with you
{: .step #takeaways}

<div class="takeaways" markdown="1">
Use these questions when someone calls a tool “agentic”:

- **Who chooses the next step?** Look for the decisions delegated to the system and where your input is needed.
- **What can it act on?** Check the actual tools, files and permissions in the session.
- **Where do its instructions live?** A brief, standing instructions and skills kept in files can be read, changed and dated.
- **What result exists?** Open the files and check one against its source.
- **When does a helper agent help?** When it keeps work separate, needs fewer permissions or checks with fresh eyes. Keep the running picture with one agent.
- **What carries forward?** Keep current instructions and project state where the next session can read them.
- **When is delegation worthwhile?** Compare the useful work completed with the time you spend directing and checking it.
</div>

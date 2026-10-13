---
title: Understanding Agentic AI
layout: base
position: 4
kicker: Workshop draft
summary: "Follow an AI agent from a task brief to a working research guide, then steer a revision and see how it uses tools, feedback and saved context."
note: "Bring a laptop and an AI assistant. The presenter demonstrates file and browser tools; no coding or new software setup is required."
published: false
thumbnail: "/assets/images/stradanus-press-1600.jpg"
header-image: "/assets/images/stradanus-press-1600.jpg"
header-tier: section
header-filter: etching
header-position: center right
header-opacity: 0.18
header-title: Understanding Agentic AI
header-subtitle: "Give AI a task whose result you can examine. Watch how it chooses actions, uses tools and responds to feedback, then decide how much work to delegate."
header-caption: "Jan van der Straet (Stradanus), <i>Impressio Librorum</i>, from <i>Nova Reperta</i>, engraved by Joannes Galle. Museum Plantin-Moretus, public domain."
tags: [agents, getting started, research]
workshop_mode: true
redirect_from: /sessions/understanding-agentic-ai.html
---

{% comment %}
Authoring references: SESSION-STYLE.md and sessions/editorial-assistant/index.md.
Separate introductory workshop; no meeting date assigned.
{% endcomment %}

{% include nav/scrollspy-toc.html %}

Work down this page during the workshop or return to it later. The short history, prompts and practice folder let you repeat the task and examine what your assistant actually does.
{: .lead}

<div class="rule" markdown="1">
**Give the agent a clear result to reach, room to choose its steps and a way to check its work.**
</div>

## Introduction
{: .step #introduction}

### Why a small research task is the place to start

Ask an assistant how to organize research materials and it can offer useful
advice. Give an agent access to a folder and a concrete goal, and it may also
read the files, create an inventory, build a guide and test it. The task helps
you see where conversation turns into delegated work.

**In this workshop, an agent is a system that can choose intermediate actions,
use tools and respond to what those actions return while pursuing your goal.**
That is a working definition for the exercise. Definitions vary; the history
below explains some of that variation. A plan written in a reply is useful,
but you need to see actions and results to know what was carried out.

The practical question is how much of a task you want the system to handle.
A good delegation leaves it room to choose an approach while making the
result, boundaries and stopping point clear.

### What you'll learn to do

- **Prepare a workspace:** locate the source materials, task instructions and place for new files. (Step 1)
- **Delegate a useful result:** describe what a reader should be able to do, what the agent may change and when it should stop. (Step 2)
- **Follow the work:** distinguish a proposed action from a tool action and the result it returns. (Step 3)
- **Steer a revision:** try the artifact, give concrete feedback and decide whether the change helps. (Step 4)
- **Continue the project:** use saved instructions and current files to pick up the next task in a fresh conversation. (Step 5)

Everyone uses the same small task. You can make these decisions and try the
presenter's result even if your assistant cannot operate on local files.
If you already use agents, add one useful check or compare two organizing
choices after the shared exercise.

### Before you start

- **A laptop and an AI assistant.** The presenter uses an agent with file access and a browser. You can still work through the brief and comparisons in a chat.
- **The practice folder**, linked below, and a text editor. The materials are short enough to read yourself.
- **A small task from your own work** to consider at the end. No programming knowledge, API key, connector installation or citation manager is needed for this exercise.

Where your tool cannot open a folder, attach the [combined practice text]({{ site.baseurl }}/assets/agentic-ai/starter/practice-pack.md) or paste it. Save replies yourself and compare them with the presenter's file actions. Record which actions your tool could actually perform; use the same task throughout.

<div class="reminder" markdown="1">
Use materials you have permission to share, such as your own notes or the fictional practice materials below.
</div>

### Start with a workspace

Download and extract the [City Memory practice folder]({{ site.baseurl }}/assets/agentic-ai/city-memory-starter.zip). It contains five fictional source files: an exhibition note, an interview excerpt, a photograph label, a research note and a small poster register. There are uncertain dates and different kinds of material to preserve.

A **workspace** is the place where a project keeps its materials,
instructions and results. Here it is an ordinary folder. The assistant
needs access to the relevant files, and you still need to check which ones
it actually read. The `.md` files are plain text; any text editor can open
them.

```text
city-memory/
  sources/       the five original materials
  brief.md       the result you want and its boundaries
  procedure.md   directions to reuse across tasks
  output/        new files the agent will create
```

The download also includes a README and the combined practice text for
attachment or pasting. `output/` is created during the exercise. The sources
supply material to work with; the brief and procedure supply instructions.

**Before prompting:** open one source and `brief.md`. Point to the place
where new files will go. In a chat without folder access, make the same
choices about what to attach and where you will save its replies.

The goal is a **local browsable guide to the folder**, with a searchable index,
links to originals and a short list of unresolved questions. You choose
whether organizing by theme or by source type better serves a first-time
reader. The agent can choose how to implement that choice.

**About the examples.** The practice materials and reference guide were
prepared for teaching on October 11, 2026. They are invented materials, not
historical records or transcripts of a workshop agent run. The reference
shows a possible result. Use your own run's actions and outputs to judge
performance.

### See a workflow across the files

A **workflow** is how a task moves through stages. In this exercise, reading
the sources produces an inventory; the inventory helps create the guide;
trying the guide produces feedback for a revision. Each result helps the
next stage. You can keep the same workspace as the task develops.

The brief names the result and useful checks. The agent chooses some of the
actions needed to get there and responds to what they return. A workflow
can also use fixed steps; its length alone does not establish agency.

**Your first choice:** would this audience find materials more easily by
theme or source type? Start with the supplied brief and change that one
field. Keep the technical implementation with the agent.

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
| Current tools, checked October 11, 2026 | Agent environments combine tools, saved project state and repeated work/check/revise cycles. OpenAI documents this in Codex and browser control. [Codex's task loop](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex), [browser capabilities](https://learn.chatgpt.com/docs/browser) | Our demo lets you watch files and browser results change, and steer the work between steps. |

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

## 1. Ask for advice and examine the result
{: .step #step-1}

Open the workspace and locate a source, the brief and the place for new
files. Give the assistant the five sources, then ask for a sensible first
approach. Save its reply as `baseline.md`.

{% include prompt.html id="agentic-baseline" %}

**Prepared comparison:** an assistant might suggest “Make a chronological
index and add themes to each entry.” That gives you an organizing idea.
You still need to decide how uncertain dates fit and whether the files have
actually been read. Open I03: its date is “c. 1975”, rather than a precise year.

Look at your reply. Did it propose an approach, supply finished content or
actually create anything you can open? Each can help, but they leave you with
different work to do. Pick one suggestion worth carrying into the brief.

<div class="keypoint" markdown="1">
Compare the advice with what exists after the reply. Name the next piece of work you still need done.
</div>

## 2. Turn the idea into a task you can delegate
{: .step #step-2}

Open `brief.md` and choose an organizing priority. State what the finished
guide should let a reader do. Then ask what tools are available and request
a short plan before file changes.

{% include prompt.html id="agentic-plan" %}

Check one promised capability. Can the assistant list the five filenames?
Can it write in the output folder? Does it have a browser it can operate,
or can it only return code for you to open? A tool description or confident
reply needs to be matched with what is available in this session.

**Prepared brief:** “Help a new researcher find materials by theme. Create a
local guide with all five sources, a search box and links to the originals.
Preserve uncertain dates. Put generated files in `output/`. The work is done
when the guide opens, a search finds the intended item and all five links
reach the right files.”

The goal names the outcome. The boundaries say where it can act. The
completion conditions say how you will know it got there. **Leave it room to
choose an implementation you can examine.** You can choose a table instead
of cards without specifying every line of code.

### Recognize the parts around the model

| Part | What it contributes in this task |
|---|---|
| The model | Produces text and proposes next actions based on the task and available context. |
| Your task brief | The audience, goal, boundaries and completion conditions. |
| Tools | Actions such as reading files, writing files or operating a browser. |
| Working context | The materials and instructions the current conversation can access. |
| Saved project state | Files describing what exists, what was decided and what remains. |
| The agent environment | The software that connects the model with tools, context, permissions and stopping rules. |

Your brief guides the work; it does not grant a tool that the environment
lacks. A saved file only helps when the assistant can read it. You may see
*agent harness* used for this surrounding environment; the practical point
is to recognize which parts your task needs.

<div class="keypoint" markdown="1">
Delegate a result with clear boundaries and completion conditions. Check that the tools can carry out the proposed plan.
</div>

## 3. Let it create a result you can use
{: .step #step-3}

Choose the plan, then let the agent work within the practice folder. Keep the
folder and editor open so you can see what changes.

{% include prompt.html id="agentic-build" %}

Watch one cycle: it chooses an action, a tool returns a result, and it chooses
what to do next. A useful cycle might be reading a label, noticing an uncertain
date and adjusting the inventory field. Another might be opening the guide,
seeing a bad source link and changing the path.

Read visible tool actions and results. You do not need access to hidden
reasoning to examine what the system did. Ask it to explain a particular
choice, then judge the explanation against the artifact.

### Open the result

A possible output folder is:

```text
output/
  inventory.csv
  questions.md
  index.html
  handoff.md
```

Open `index.html`, follow a source link and look at the inventory. Can you
find all five inputs? Does the guide preserve “c. 1975” and unknown dates?
Do its summaries help a reader decide what to open?

The [prepared reference guide]({{ site.baseurl }}/examples/understanding-agentic-ai/)
lets you try a working search and theme filter. It shows the kind of artifact
the task requests, while your live folder shows what your agent produced.

**Prepared comparison:** selecting “Public memory” in the reference shows
I01, I02 and I03. Searching for “poster” shows I04 and I05. A reader can open
the originals from those results. Check those same actions in your guide.

### What is the advantage here?

The advantage is carrying connected work through to an artifact you can
use: read the folder, organize its contents, make the page and check whether
it works. A tool-enabled chat may accomplish that too. Compare the work
completed, your coordination effort and the quality of the result.

For a discussion of an interpretation, a direct conversation may be all you
need. Use delegated action where the intermediate work is worth handing over.

<div class="keypoint" markdown="1">
Open the artifact and try one intended use. A report of success should match a result you can examine.
</div>

## 4. Change the requirement and watch it adapt
{: .step #step-4}

Give the agent one concrete change. For example, a collaborator wants a
source-type filter as well as themes, with date uncertainty more visible.

{% include prompt.html id="agentic-revise" %}

Watch how it uses what is already there. Does it read the existing page and
inventory, change the relevant files and check the new behavior? Does it
repair something discovered by a check, or merely announce that it checked?

**Prepared feedback:** “When I select Interviews, I want just I02. If I also
search for poster, there should be no results and a useful message. Clearing
the search should restore I02 without resetting the filter.” This gives the
agent a sequence you and it can try.

If a check fails, ask it to make a focused repair and try that check again.
Stop after two repair attempts during the exercise; leave remaining problems
in `handoff.md`. That is enough to see how feedback shapes the next action.
The [OpenAI repair-loop example](https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex)
uses the same general pattern of producing an artifact, testing it and using
the result for the next pass.

A working filter can be checked directly. Whether the themes make useful
intellectual distinctions still needs your judgment. Automatic checks and
interpretive decisions do different work.

<div class="keypoint" markdown="1">
Give feedback as a concrete use to try. Watch whether the next action responds to its result.
</div>

## 5. Carry the work forward and choose your next delegation
{: .step #step-5}

Ask for a short handoff, then start a fresh conversation with the folder or
attach its current files. See what it can understand without the whole chat.

{% include prompt.html id="agentic-handoff" %}

**Prepared handoff shape:** “Five source files; generated guide in
`output/index.html`; theme search tested; source-type filter requested;
I02 date remains unknown; next action is to test Interviews plus poster.”
Replace every statement with what actually happened in your run.

Use this in the fresh conversation:

{% include prompt.html id="agentic-resume" %}

Check its account of the current state before it acts again. Does it point
to an existing file and distinguish finished work from the next task?
External files can carry project state across conversations; the assistant
still needs to read them. Calling something “memory” does not guarantee it
is complete or current.

### Optional presenter demo: a plain procedure and a skill

Open `procedure.md`. It tells the assistant to preserve source IDs and date
uncertainty, label interpretation and test the generated guide. Change one
rule and show how you would bring the revised file into the next task.

A skill packages reusable instructions with a description of when to use
them and, where needed, supporting resources or scripts. It guides available
tools; installing an instructions-only skill does not give an assistant file
or browser access. [OpenAI's skill documentation](https://developers.openai.com/plugins/build/skills)
describes these separate roles. Other systems have their own packaging.

Start with a plain text procedure for this workshop. Once you have a useful
repeated task, packaging it as a skill can make it easier to reuse. No skill
installation is required today.

### Choose a task from your own work

With a partner, choose one task you could try next. Write its result,
available materials, allowed actions, completion check and the decision you
want to retain.

| Task | Work an agent might carry through | A useful check or retained decision |
|---|---|---|
| Explore five articles | Open accessible texts, make notes and a linked reading guide. | Check an important interpretation; choose what deserves closer reading. |
| Clean collection metadata | Compare fields, propose a consistent format and write a cleaned copy. | Compare record counts and sample changes; retain ambiguous identifications. |
| Review a document | Read its instructions, mark passages and prepare changes. | Judge comments against the text and choose substantive revisions. |
| Build a research aid | Turn notes into a local search page, timeline or comparison tool. | Try an intended use and judge the categories. |

Several agents can divide work, but a single agent is enough to demonstrate
this process. Multiple replies do not automatically constitute independent
expertise. Choose extra coordination when it solves a problem you can name.

<div class="keypoint" markdown="1">
Carry forward the current files and a short account of unfinished work. Choose your next delegation by its useful result and how you will judge it.
</div>

## What to take with you
{: .step #takeaways}

<div class="takeaways" markdown="1">
Use these questions when someone calls a tool “agentic”:

- **Who chooses the next step?** Look for the decisions delegated to the system and where your input is needed.
- **What can it act on?** Check the actual tools, accessible materials and permission boundaries.
- **What result exists?** Open the artifact and compare it with the requested outcome.
- **What feedback changes its actions?** Give it a concrete check or correction and watch the response.
- **What carries forward?** Keep current instructions and project state where the next session can read them.
- **When is delegation worthwhile?** Compare useful work completed with the time you spend directing and checking it.
</div>

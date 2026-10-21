---
title: Audit Trails for AI Agents
layout: base
position: 3
date: 2026-10-21
time: "12:00–12:50"
location: History Commons (MVH 1104)
kicker: Session 3 · October 21, 2026
summary: "Read into a topic with an AI agent, map the articles’ ideas and relationships, and keep a record of what you checked and chose to read next."
note: "Bring a laptop and a topic to explore, or use the example we provide."
points:
  - title: Organize sources, prompts, outputs
    text: Set up a project workspace that preserves your research materials, AI instructions, and results.
  - title: Check claims, track corrections
    text: Use AI agents to review each other's work, verify claims against original sources, and record errors and corrections.
  - title: Document decisions and revisions
    text: Keep a concise record of what you accepted, changed, or rejected, and why, so others can follow your research process.
flyer: "audit-trail-flyer-v2.jpeg"
thumbnail: "/assets/images/stradanus-press-1600.jpg"
header-image: "/assets/images/stradanus-press-1600.jpg"
header-tier: section
header-filter: etching
header-position: center right
header-opacity: 0.18
header-title: Audit Trails for AI Agents
header-subtitle: "An agent can help you find your way into a body of writing. Keep the articles, interpretations and reading choices together so you can check and revise the map."
header-caption: "Jan van der Straet (Stradanus), <i>Impressio Librorum</i>, from <i>Nova Reperta</i>, engraved by Joannes Galle. Museum Plantin-Moretus, public domain."
tags: [research, agents, audit trails]
workshop_mode: true
redirect_from: /sessions/audit-trails-for-ai-agents.html
---

{% comment %}
Authoring conventions: SESSION-STYLE.md; worked example: sessions/editorial-assistant/index.md.
The presenter's demo files in assets/audit-trails/ are prepared teaching materials, never a recorded agent run.
{% endcomment %}

{% include nav/scrollspy-toc.html %}

Work down this page during the session or return to it later: the prompts, source links and example files stay together so you can repeat the exercise.
{: .lead}


## Introduction
{: .step #introduction}

### Why historians keep an audit trail

Historians have always had to show their work. A footnote lets a skeptical
reader walk back from a claim to the archive box, page or passage behind
it, and historical argument depends on the assumption that readers could
check (even if few of them ever do). We expect to be able to say where
everything came from, how we arrived at our interpretations, what we
verified carefully and what we took on trust, and how someone else could
retrace our steps and test the conclusions against their own reading.

**None of these expectations change when an AI agent assists with research. But imagine you have to peer review AI-assisted work. What would you want to see to trust it was used carefully?**

Imagine AI as a very capable but very new and naive research assistant. You simply don't know if you can trust it, so you want to see the thinking process that led to conclusions. In real life, that would be face to face conversations.

In the AI-assistant world, the answer to building trust is to keep the trail as you go, in files rather than in the scroll of a chat window: the searches you asked for, the material the agent
could actually open, your notes, and your reasons for changing a summary or
a reading recommendation. A saved chat can help, of course, but no
colleague wants to read your entire conversation to check one claim.

Reproducibility works differently here, too. Send the same request twice
and the reply will usually come back worded differently, so the goal is not
identical output. The goal is that someone else can run the same searches,
open the same articles, read the same passages and decide for themselves
whether your interpretation holds up.

### Why reading into a topic is the place to start

Getting oriented in an unfamiliar body of writing is one of the most
tempting jobs to hand to an agent, and one of the riskiest. Ask it to find
several articles on a topic, explain their arguments and suggest where to
spend your reading time, and you will have a tidy overview in a few
minutes. What you want from that overview, though, is something closer to
a map you can argue with: which ideas belong to which authors, where the
articles agree or pull apart, and what seems worth following up. **This is
also where an audit trail matters most.** When you don't yet know the
articles well, you are in no position to notice when a summary quietly
blurs two authors' positions, which is one of the first things you will
check for in this session.

Nor are you reading only for facts. Theoretical arguments and ways of
framing a problem matter just as much; a source can be valuable because it
changes your question, introduces a useful distinction or offers another
way to think about AI altogether. Part of what the trail records, then, is
what kind of work each source does for your inquiry, and why you think so.

This session picks up where the [editing session's work with a saved style guide]({{ site.baseurl }}/sessions/editorial-assistant/#step-5)
left off. There you taught an assistant how to read your own writing; here
you give it a reading procedure and check how well it represents other
people's arguments.

### How this session works

The session has two halves. In the first, you work in an ordinary browser
chat: you send a prompt, copy each file out of the reply and save it in
your folder yourself. By the end you will have built the whole trail by
hand, from the first overview and the source register through the reading
notes, the comparison, the check and your decisions. That is slower than it
needs to be, but it shows you what each file is for and what goes missing
when you skip one. Most people reach step 4 in the hour. Finish steps 5
and 6 afterwards from your folder and this page.

In the second half, the presenter runs the same work with an agent. An
agent works toward a goal over several steps before it reports back,
**choosing some of those steps itself** and changing course based on what
they return. Asked for three accessible articles, it might run a search,
find that one result is paywalled, search again and save notes on the three
it could open. The demonstration uses Claude Code, which works in a folder
on the presenter's computer and writes the files and its own run record as
it goes.

A browser chat with web search turned on already does some of this: it
searches and opens pages you don't see. **Its account of that work is a
claim to check.** “I searched three databases and read five articles”
describes steps you mostly did not watch, so treat it the way you treat its
summary of an article. Both halves of the session build a record that lets
you check it: the searches it ran, what it could open, which passages
someone read and what you decided.

### What you're working with

- A browser chat with web search can find articles and report what it
  searched and opened. Open two of its links yourself. (Step 2)
- Given your reading instructions, it can write a short note on each
  article. Ask it to say how much of each one it could open. (Step 3)
- It can compare several texts and recommend a reading order. Ask for the
  passage behind each connection and recommendation. (Step 4)
- A new conversation sees only the files you give it, which makes it a fair
  test of your trail. (Step 5)
- An agent working in a folder writes the files and its own run record. Its
  account still needs the same checks. (Step 7)

### Before you start

- **A laptop** with a web browser.
- **An account with an AI assistant**, such as Claude, ChatGPT, Gemini or
  Copilot. Sign in before you start.
- **A topic you want to explore**, or use the question below.

The only thing worth installing is a code editor (setup step 3), and even
that is optional. The agent, Obsidian and Zotero appear only in the
presenter's demonstration at the end. Setting up takes about five minutes,
or ten if you install an editor.

**1. Make a folder for today's work.** On your desktop, create a folder named
`my-reading-trail`. Every file you save today goes in it.

- Mac: click the desktop, choose **File → New Folder** and type the name.
- Windows: right-click the desktop, choose **New → Folder** and type the name.

**2. Turn on file extensions,** so you can see that a file is called
`baseline.md` and not `baseline.md.txt`.

- Mac: in Finder, choose **Finder → Settings → Advanced** (**Preferences** on
  older systems) and tick **Show all filename extensions**.
- Windows 11: in File Explorer, choose **View → Show → File name extensions**.
  On Windows 10, open the **View** tab and tick **File name extensions**.

**3. Open a text editor, ideally one that shows the whole folder.** TextEdit
on a Mac or Notepad on Windows is enough for today. A code editor is better:
it lists every file in the folder in a sidebar, so you can watch the trail
grow, and it saves each file under exactly the name you type. It is also
the kind of tool you will want for any longer project kept in plain text.
Avoid Word and Google Docs: they save files in their own formats, and this
exercise uses plain text.

- **A code editor (recommended).** [Visual Studio Code](https://code.visualstudio.com/)
  is free. [Sublime Text](https://www.sublimetext.com/) is smaller and
  quicker to install, but now and then it asks you to buy a license. Install
  one, then open `my-reading-trail` as a folder with **File → Open Folder**
  (in Sublime on a Mac, **File → Open** and choose the folder). If VS Code
  asks whether you trust the authors of the files in this folder, choose
  **Yes**: they are your files.
- **TextEdit** on a Mac: choose **File → New**, then **Format → Make Plain
  Text**.
- **Notepad** on Windows: open it from the Start menu.

If your laptop won't let you install software, use TextEdit or Notepad and
keep the folder open beside it.

The files you save today end in `.md`, for Markdown: plain text with a few
marks for structure. A line starting with `#` is a heading, `**words**` are
bold and a line starting with `-` is a list item. Any text editor can open
it, and AI assistants read and write it easily. You don't need to learn the
marks, because the assistant writes them. In an editor they show up exactly
as typed, which is what you want. VS Code can also show the formatted
version: press **Cmd+Shift+V** on a Mac or **Ctrl+Shift+V** on Windows.

**4. Open your AI assistant** in a browser tab and start a new conversation.
Put the browser on one half of the screen and your folder and editor on the
other.

- Mac: hold the pointer over the green button at the top left of a window and
  choose the left or right half.
- Windows: press the Windows key and the left or right arrow.

**5. Tell the assistant how you will save files.** A browser chat can't put
files in your folder. Some offer a download link, depending on the tool and
plan; if yours does, download each file and move it into
`my-reading-trail`. Copying each file out of the reply works everywhere, so
the steps below use that. This prompt asks the assistant to set files out
so they are easy to copy.

{% include prompt.html id="audit-setup-files" %}

If your assistant can already work in a folder on your computer, give it
access to `my-reading-trail` only and skip this prompt.

**6. Check that it can search the web.**

{% include prompt.html id="audit-setup-search" %}

If it says it can't search the web, look for a search or web option near the
message box and turn it on.

<div class="reminder" markdown="1">
Use sources and research materials you have permission to share, such as the public articles linked below or your own notes.
</div>

### The question we'll use

> How do arts and humanities perspectives help us think about AI?

Choose an interest within that topic: ethical concepts, historical framing,
creative practice, or something from your own field. You will give it to
the assistant when it searches in step 2, and it decides which reading route
suits you in step 4. You are getting oriented in a body of writing and
deciding what deserves closer attention.


## 1. Start with an overview you would want to use
{: .step #step-1}

Send the question as a reasonable first request, the way you might on any
other day.

{% include prompt.html id="audit-baseline" %}

Save the complete reply, citations included. You will save every result
today the same way.

- Click the copy button under the reply, usually two overlapping squares.
  When the assistant shows a file in its own box, use that box's copy button.
- In your editor, start a new file. Type the assistant's name and today's
  date on the first line, then paste the reply below it.
- Save it in `my-reading-trail` as `baseline.md`. In a code editor, choose
  **File → Save** and type the name; the file appears in the sidebar. In
  TextEdit, if it asks which extension to use, choose **Use .md**. In
  Notepad, choose **File → Save as**, set **Save as type** to **All files**
  and type `baseline.md`.
- Check the name in the sidebar or the folder. You should see `baseline.md`,
  not `baseline.md.txt` or `baseline.rtf`. If the name is wrong, rename the
  file.

Now read the overview before you do anything with it. You don't need to
know the articles yet to ask useful questions of it.

- Which ideas does it give to which author? Does any idea float free of an
  author?
- Where does it say two articles agree, repeat or respond to each other?
  What would you need to read to know whether that is true?
- Why does it recommend the reading order it gives? Would a different
  interest change it?
- Does each citation open, and does it lead to the work it names?

Choose one connection or recommendation whose accuracy would change where
you spend your reading time, and write it at the top of `baseline.md`, under
the date, as something to check. You will come back to it in step 5.

<div class="keypoint" markdown="1">
Save the first overview with the assistant's name and the date. Pick one interpretation or reading recommendation to follow back to the articles.
</div>

## 2. Search within limits you set
{: .step #step-2}

Replace the bracket with your interest, then send this. Change the scope
if you want other dates, languages or kinds of writing. The assistant
records your choices and the searches it says it ran at the
top of `sources.md`, followed by the register of what it found.

{% include prompt.html id="audit-retrieve" %}

Give the search five minutes. If fewer than three sources are ready by
then, record that in `sources.md` and use the backup set below. A blocked or
paywalled source stays in the register as a lead; record what you could
access and move on.

Open two of the links yourself and check that each one leads to the article
it names. The register is also an account of what the assistant did, and a
link that goes nowhere tells you something about the rest of it.

Compare one search choice with a neighbor's. A search for historical
framing may produce a different starting set from a search for ethical
concepts, and restricting source types or languages changes what you can
see. **Save the choices that shaped the set, as well as the articles it
produced.**

If the search stalls, use these three instead: two essays from one series
and a journal introduction.

- [John Tasioulas: The role of the arts and humanities in thinking about artificial intelligence](https://www.adalovelaceinstitute.org/blog/role-arts-humanities-thinking-artificial-intelligence-ai/).
- [Alison Powell: Otherwises, and the contribution of the arts and humanities to ethical AI](https://www.adalovelaceinstitute.org/blog/otherwises-contribution-arts-humanities-ethical-ai/).
- [Lauren M. E. Goodlad: Editor's Introduction: Humanities in the Loop](https://doi.org/10.1215/2834703X-10734016), with an accessible [project-hosted proof PDF](https://criticalai.org/wp-content/uploads/2023/09/CAI112_01Goodlad_1pp-1-1.pdf).

Record that you used this backup set, and that two of its three sources come
from one publisher. A broader search would need other traditions and positions.

<div class="keypoint" markdown="1">
Ask the assistant to list the searches it says it ran and how much of each article it could open. Then open two of its links yourself.
</div>

## 3. Read the articles with your own instructions
{: .step #step-3}

### Write your reading instructions

Make a new file in `my-reading-trail` called `reading-protocol.md` and copy
these rules into it. They tell the assistant how to read, and you can bring
the same file into any later conversation.

{% include prompt.html id="audit-reading-protocol" %}

Change one rule to fit how your field reads. A historian might ask for the
kind of evidence each author uses. A literary scholar might want the key
phrase quoted exactly. Then put today's date on the first line.

### Get a note on each article

Send this in the same conversation, with your edited `reading-protocol.md`
pasted below the prompt. The assistant already has `sources.md` from step 2;
if you started a new conversation, paste that in too. You don't need to read the articles first. In
step 5 you will open one or two passages to check what the assistant said
about them.

{% include prompt.html id="audit-read" %}

Save the reply as `notes.md`, with a section for each source ID. Check that
each section says how much of the article the assistant could open: step 5
relies on that record. Keep the notes short so there is time to compare and
check them.

Use the source IDs (`S01` to `S03`) everywhere from now on: in the notes,
the comparison, the checks and your decisions. They let you, or anyone
reading your folder later, follow one article through the whole trail.

<div class="keypoint" markdown="1">
Keep your reading instructions in a file and give it to the assistant with every reading request.
</div>

## 4. Compare the articles and choose a reading route
{: .step #step-4}

### Get an overview that preserves differences

Send this in the same conversation, which already has `sources.md` and
`notes.md`. Save the three files it returns as `synthesis.md`, `idea-map.md` and
`reading-queue.md`.

{% include prompt.html id="audit-synthesize" %}

A useful overview carries the distinctions into its prose. Read
`synthesis.md` with these questions:

- From the overview alone, could you say what each author adds? If two
  authors blur together, which sentence did it?
- Does it give each article's central claim, or promote a passing example
  to the center?
- Are its interpretations labeled as interpretations?

### Make the connections explainable

Open `idea-map.md`. Every connection should name its relationship and
its basis. For each one, ask:

- Is this an explicit response or citation you could find in the text, or a
  theme the assistant inferred?
- Does it point to a passage? Could you go there and decide whether the
  label fits?
- Does it claim more agreement or disagreement than the articles may
  support?

Pick the connection you find most interesting and keep it marked as a
question until you have read its passage. The map can hold an interesting
tension without turning it into a direct disagreement or claiming one author
cited another.

### Ask what deserves your next twenty minutes

Open `reading-queue.md`. Each entry should give a reading goal, the
passage to start with, why it adds something and how much text the
recommendation rests on. A rating such as “9/10 relevance” hides those
decisions.

- Does each recommendation follow from your interest, or would it be the
  same for anyone?
- Is any article dropped or pushed to the end because it was hard to open?
- Which recommendations rest only on an abstract or selected passages?

Then ask the assistant how the order would change if you changed your
interest. The difference between the two routes shows you how much the
recommendation depends on the question you brought. Give every source a next
action, even if that action is to read more before assessing it.

### Keep a record of what you asked

Before you leave this conversation, ask for the run record: a short entry
for each request you sent, saying what you asked, what you gave the
assistant and what it produced. The chat already holds all of this, but a
colleague can't see your chat, and neither can the new conversation in
step 5.

{% include prompt.html id="audit-run-record" %}

Save the reply as `prompts.md`. Then check one entry against the chat
above it: does it give your request as you sent it, and does it say what
the assistant couldn't open? The record is the assistant's account of its
own work, and it can be wrong.

<div class="keypoint" markdown="1">
Ask for the passage and reading goal behind every important connection or recommendation. Check one against the original text.
</div>

## 5. Check a connection in a new conversation
{: .step #step-5}

Start a new conversation for the check. In a browser chat, that means the
**New chat** button. The new conversation does not remember the first one,
and a different assistant works too. **A new conversation sees only what you
give it, the way a colleague opening your folder would.** Where it gets lost,
a later reader would too.

Send the file-saving prompt from **Before you start** first. Then drag your
files into the message box, or paste their text if your assistant limits
uploads: `sources.md`, `notes.md`, `synthesis.md`, `idea-map.md`,
`reading-queue.md` and `prompts.md`. The article links and your interest
are already in `sources.md`. Save the reply as `checks.md` with the tool
and date.

{% include prompt.html id="audit-check" %}

### Follow one finding back to the article

Pick the finding in `checks.md` that matters most to your reading route,
ideally the connection you noted in step 1. Open the passage it names and
read it yourself.

- Does the passage say what the checker says it says?
- Does the proposed correction keep each author's argument distinct?
- Does the corrected reading recommendation still fit your interest?

An interpretation can be defensible without being the only possible reading;
record what you remain unsure about.

### Look for a criticism you might reject

A checker can be wrong too. Look for a suggestion that would make your trail
tidier but lose something, such as merging two articles because they belong
to one series, or dropping a source because it was hard to open. Ask what
the change would erase, and record why you accept or reject it.

### Check the records

- Does every article in `sources.md` have a section in `notes.md`?
- Do the access statuses match what the assistant could actually open?
- Can you find the basis for each connection in the map?
- Do the entries in `prompts.md` match what you sent and saved?

Separate conversations, even with different assistants, can share
assumptions. Read at least one important passage yourself and judge both
the overview and the checker's reading against it.

<div class="keypoint" markdown="1">
Check a proposed correction against the article and your reading goal before treating it as a decision.
</div>

## 6. Record your decisions and keep the reading route
{: .step #step-6}

Decide which findings hold up, write your decisions into the prompt below
and send it in the checking conversation. Save `decisions.md`, then save
the updated overview, map and queue over the old files. `decisions.md`
records what changed and why.

{% include prompt.html id="audit-revise" %}

For each finding, write accept, revise, reject or unresolved into the
prompt, with a reason. The assistant can lay your decisions out as a table.
**You supply the decision.** Proposed changes stay pending until you decide;
record who decided and when.

Then read the list of changes in `decisions.md` against `checks.md` and the
updated files.

- Can you trace each change to one of your decisions?
- Did anything change that you didn't decide? With the old files gone, you
  are relying on the assistant's list of changes, which is one reason a
  longer project keeps earlier versions.
- Could a colleague, reading only your folder, explain why your reading
  route changed?

Before you finish, send the run-record prompt from step 4 once more and
add the new entries to the end of `prompts.md`.

Append new corrections to the log and keep the current reading route in the
latest files. This follows the CHM project's use of process notes alongside
a separate account of current conclusions and open work.

<div class="keypoint" markdown="1">
Keep the reasons behind a revised interpretation or reading choice. A colleague should be able to follow the change from your files.
</div>

## 7. Watch an agent keep the same trail
{: .step #step-7}

**Presenter demonstration.** Watch this one; you don't need to install
anything.

The presenter runs the same reading sprint in Claude Code, an agent that
works in a folder on the computer. Instead of a reply for you to copy, it
searches, opens pages and writes `sources.md`, a note per article and the
comparison files into the folder, adding to the run record as it goes. A
`CLAUDE.md` file in the folder holds the standing instructions (the stages,
the rules for each file and the format of the run record), and the agent
reads it at the start of every session, so nobody pastes the instructions
into each conversation. Other agents that work in a folder use a similar
file. The prompt is short because the instructions are already in the
folder, next to the brief and the reading protocol.

{% include prompt.html id="audit-agent-sprint" %}

Watch for what changes, and for what doesn't.

- Each search, page and file the agent opens or writes appears in its
  transcript as it happens. In the browser chat you had only its account of
  what it searched.
- The run record is written while the work happens, not reconstructed at
  the end as you did in the browser. Read one entry against the transcript
  and the files: does it say what actually happened?
- The files appear and change in the folder. Open `sources.md` and a note
  while it works and watch the access statuses fill in.
- The check goes to a separate checker with its own instructions. It
  starts with only the files in the folder, not the first agent's account
  of its work: the same test you ran with a new chat in step 5.

**A visible record of actions does not make the notes accurate.** The
transcript shows that the agent opened a page; it doesn't show that its note
represents the argument fairly. Steps 4 to 6 still apply: follow one
connection to its passage, and record the decision yourself.

### The workspace it builds

The folder starts with the standing instructions, the brief, the reading
protocol, an empty run record and the checker's instructions. By the end of
the sprint the agent has added the rest:

```text
humanities-ai/
  CLAUDE.md               standing instructions
  brief.md                question, interest and limits
  reading-protocol.md     how to read each source
  prompts.md              run record, one entry per stage
  .claude/agents/
    source-checker.md     the checker's instructions
  sources.md
  notes/
    S01-author.md … S03-author.md
  synthesis.md
  idea-map.md
  reading-queue.md
  ideas/                  one note per shared concept
  checks.md
  library.ris
```

It keeps more than you did by hand: one note per article, a separate file
for each stage, the checker's findings and a citation file. There is no
`decisions.md`: the checker's corrections stay pending, because the
decisions are yours, as they were in step 6.

With three sources, a later reader needs to see whether all three entered the
comparison, which connections the checker followed to a passage and which
sources it couldn't open. The run record answers those questions only if it
is specific. **A file called “checked” does not say what was checked.**

### Optional: open the notes in Obsidian

The presenter can open the agent's `humanities-ai` folder as an Obsidian
vault. Start with `idea-map.md`, follow a link into a source note, and open
its local graph. The idea notes in `ideas/` link back to the sources that use
each concept. No plugins are needed for this demonstration.

Obsidian's [graph view](https://help.obsidian.md/Plugins/Graph+view) draws
connections from links between notes. **Keep the relationship in the text
beside the link.** The graph shows that you connected two notes; their text
explains whether you mean a direct response, a shared theme or a provisional
interpretation. Click a connection's source note and show its passage location.

The same Markdown files remain usable in a text editor.

### Optional: import the citations into Zotero

The sprint's last stage writes `library.ris` from the source register. The
presenter can then demonstrate **File → Import → A file** in Zotero. Compare
one imported item's author, title, date and URL with the original article.
Zotero [accepts RIS and other standard formats](https://www.zotero.org/support/kb/importing_standardized_formats).

A [prepared five-item RIS file]({{ site.baseurl }}/assets/audit-trails/humanities-ai/library.ris)
is a fallback if the live run doesn't get that far. It imports citation
records into a collection. The separate Markdown files keep the reading
notes, connections and decisions; this citation export does not bundle the
article texts or the audit trail.

<div class="keypoint" markdown="1">
Put standing instructions in a file the agent reads at the start of each session. Read its run record against the files and links it left.
</div>

## What to take with you
{: .step #takeaways}

Use these habits in your next reading project.

<div class="takeaways" markdown="1">
### Keep the trail in files

- **Give the project one folder.** Keep the sources, reading instructions, notes and outputs together as plain text files.
- **Save each result as a file.** Put the tool and date at the top.
- **Keep a run record.** At the end of each conversation, ask for an entry per request: what you asked, what you gave the assistant and what it produced. Check one entry against the chat before you keep it.
- **Give each source a stable ID.** Use it across the source list, notes, map and corrections so you can follow one article through the work. In a longer project, give each source its own note file named by that ID.
- **End with a short methods note.** Say what actually happened: the question and interest, the searches, what was opened, the instructions used, the checks done, your decisions and what is unfinished. Don't call a reading sprint a systematic review.
- **Keep earlier versions.** Today you saved revisions over the old files. In a longer project, save a revision as a new file (`synthesis-v2.md`) and number each version of your reading instructions, so you can see what changed without relying on the assistant's account and tell which instructions produced which notes.
</div>

<div class="takeaways" markdown="1">
### Give the AI instructions

- **Record the search choices.** Save your interest, scope and the searches it says it ran before any summary.
- **Keep reading instructions in a file.** Adapt them to your field, date them and bring them into every new conversation.
- **Ask for the passage behind each claim.** Every connection and reading recommendation should point to a place in an article and to your interest.
</div>

<div class="takeaways" markdown="1">
### Check the work

- **Treat the AI's report as a claim.** Compare what it says it searched, read and saved with the files and links it left.
- **Match claims to what was read.** An abstract or a few selected passages cannot support a claim about a whole article. Note which passages a person checked.
- **Follow one connection back to the article.** Read the passage yourself, check that the overview keeps each author's argument distinct, and test a checker's corrections the same way.
- **Record your decisions.** Save what you accepted, changed or rejected and why, so someone else can follow how your reading route changed.
</div>

<div class="takeaways" markdown="1">
### What an agent adds

- **Standing instructions in the folder.** A file such as `CLAUDE.md` gives every session the same reading rules without pasting them in.
- **Actions you can see.** Its searches, pages and file writes appear as they happen. Read the run record against them.
- **The same checks.** A record of actions shows what the agent opened, not whether it read fairly.
</div>

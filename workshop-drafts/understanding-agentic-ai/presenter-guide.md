# Understanding Agentic AI · presenter guide

Authoring references: ../../SESSION-STYLE.md and ../../sessions/audit-trails-for-ai-agents/index.md.
Session: ../../sessions/understanding-agentic-ai/index.md. Separate unlisted workshop draft, with no meeting date assigned. The instruction files are the "Save as …" entries in _data/prompts.yml; the prepared CLAUDE.md, progress.md and README.md are in lit-review/ here. Run scripts/build-agentic-workspace.py after editing either. Put rehearsal runs in _local/.

## The hour's purpose

The session is a piece of problem solving. An AI review is quick to get and slow to check; each step adds one thing that moves part of the checking into the work and leaves a smaller check for the person. Participants should leave able to say what makes a system agentic and to apply the same moves to their own work: bound the materials, put instructions in files, require pages, revise in steps with a log, add a helper for a named reason, write the workflow down.

It is a stand-alone workshop. The audit trail session covers recording and verification as a practice; here verification is the motivation for each design choice, and the emphasis is on how the agent works.

Most of the room watches. Participants who already use an agent build the same folder alongside. Everyone can send the baseline prompt in a chat and answer the "Remaining tax liability" questions from the presenter's screen.

## Reveal the folder gradually

Start in an empty lit-review folder. Each step adds one or two files, and the page shows only those. Don't open the finished folder or the download until step 6. Keep the file browser or editor sidebar visible so the room sees the folder grow.

## A 60-minute route

- 0–4: introduction. Why a literature review.
- 4–9: what makes AI agentic. The working definition and the three-row table. Open the history box only if there is a question about where the idea comes from. Optional partner question: an assistant writes a plan; a script runs the same report nightly; a system reads a folder and repairs a broken link after testing it. Which shows adaptive action?
- 9–15: the verification tax. Participants send the baseline prompt. Ask the room what they would have to check, then show the list.
- 15–23: step 1. Save the brief, start the agent, search and save. Narrate one action, result and next-action cycle as it happens. Open one PDF.
- 23–31: step 2. Save the reading instructions and change one rule from a suggestion in the room. Notes on S01 and S02. Check one key idea against its page with the room.
- 31–38: step 3. Synthesis instructions; version 1. Find one connection labeled as the authors' and check it.
- 38–46: step 4. Two helpers, revision, log. Read the log entry aloud and check one change against its note.
- 46–52: step 5. Checker instructions and checks.md. Open one finding.
- 52–58: step 6. Workflow file, fresh session, the whole folder and the download. Partner question about their own work.
- 58–60: takeaways table.

Steps 1 and 4 take the most live time. While the agent works, talk through the "Remaining tax liability" box for that step.

## Before teaching

- Participants are pointed to Obsidian for reading the folder (Open folder as vault). It adds a hidden .obsidian settings folder to lit-review; that's harmless, and the agent should ignore it. Run the agent yourself in the Claude desktop app's Code tab, with Obsidian open beside it, so the room sees the transcript and the folder filling in. The page tells participants to use the desktop apps, not a terminal.

- In the invitation, ask anyone who wants to follow along to install Obsidian (or have VS Code) beforehand, and, if they will run an agent, to check that the Claude Code tab or the ChatGPT desktop app opens a folder on their plan. Don't wait for installs in the room. The page cues Obsidian twice: opening the folder as a vault in step 1, and a note beside its PDF in step 2. Some managed university laptops block installs; those participants watch the presenter's screen.
- Rehearse at least once in an empty folder in _local/rehearsal/, with the prompts from the page in order. Time each step and keep the transcript and the finished folder.
- Check that Claude Code is signed in, that web search and PDF downloads work on the venue network, and that the backup PDFs in the brief open.
- Grant permissions in advance where you can, so approval prompts don't interrupt the room. Keep the session inside the lit-review folder.
- Platform notes, to recheck before teaching: Claude Code reads CLAUDE.md at the start of every session; its general-purpose helper agents (subagents) start with only the prompt the lead gives them and can run in parallel; subagents can't start their own subagents. The instruction files are plain files in a visible folder, so other agents can use them, at the cost of Claude Code's automatic skill loading and per-helper tool limits. Mention that packaging in step 6 only.
- Plans and apps, checked 2026-11-05 (recheck before teaching):
  - Claude: the desktop app's Code tab is Claude Code, so CLAUDE.md and helper agents work as the page describes. It needs a paid plan (Pro or above); the pricing page marks Claude Code "No" for Free. Cowork was merged into the main Claude conversation from September 16, 2026 (https://claude.com/blog/cowork-is-now-claude), so participants may not see a Cowork option. On paid plans the merged Claude can also work in a local folder, but Cowork's help page never mentioned CLAUDE.md (it used its own folder instructions), so send participants to the Code tab, where step 6 behaves as described.
  - ChatGPT: the desktop app opens a local folder and runs Codex. Free and Go include "Limited Codex access"; OpenAI gives no number. Codex reads AGENTS.md, not CLAUDE.md, so in step 6 ChatGPT users ask for AGENTS.md (the prompt's note says so). Codex runs helper agents in parallel by default. Its web search uses a cached index by default; check before teaching whether it asks for approval before downloading PDFs.
  - Free accounts: Claude Free can do the baseline exercise but not the folder steps. ChatGPT Free can try the folder steps but may hit its limit partway through.
  - Sources: https://claude.com/pricing, https://support.claude.com/en/articles/13345190-get-started-with-cowork, https://code.claude.com/docs/en/desktop, https://learn.chatgpt.com/docs/pricing, https://learn.chatgpt.com/docs/app, https://learn.chatgpt.com/docs/agent-configuration/agents-md, https://learn.chatgpt.com/codex/agent-configuration/subagents, https://learn.chatgpt.com/codex/web-search

## If the live run stalls

Keep the rehearsal folder open in a second window. If the search runs long, tell the agent to use the backup set in brief.md. If a step fails, switch to the rehearsal folder and say so: it is a run from an earlier date, not this one. Don't present rehearsal files as live output, and don't stage a failure in a run that worked.

## Points to make, and claims to avoid

- A visible tool action shows what the agent opened, not whether it read fairly. That is why every step ends with a check against a page.
- Helper agents are the same model with different instructions and less context. Several replies do not amount to independent expertise.
- The reading instructions record what an author claims is new; the synthesis decides what is distinctive in the set. A reader that can see the running synthesis tends to recruit each new source to it, which is the most common failure in the CHM chapter's reading protocol and the reason helpers read without it.
- Don't claim anything about model internals. Point to actions, files and results.

## Historical and current references

- SRI's Shakey retrospective: https://www.sri.com/case-study/the-man-the-myth-the-legend-meet-shakey-the-robot-the-worlds-first-ai-based-robot/
- Wooldridge and Jennings, Intelligent Agents: Theory and Practice (1995), weak notion of agency: https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/ker95/subsubsectionstar3_1_1_1.html
- ReAct (2022 preprint; 2023 ICLR camera-ready): https://arxiv.org/abs/2210.03629
- Toolformer (2023): https://arxiv.org/abs/2302.04761
- Anthropic's 2024 workflow/agent distinction (historical framing; not a current product inventory): https://www.anthropic.com/engineering/building-effective-agents
- Current OpenAI documentation checked 2026-10-11: https://developers.openai.com/blog/run-long-horizon-tasks-with-codex and https://learn.chatgpt.com/docs/browser

This is a selected conceptual history, not an etymology of "agentic" or a claim that one paper invented agents. Recheck current product capabilities before teaching.

## Backup set

The five PDFs in the brief were downloaded and their first pages checked on 2026-11-04. Perlow (PMLA) is published by Cambridge with an author copyright line; Nobile et al. is CC BY 4.0; the Goodlad proof and the Rutgers guide are hosted by their own projects; Offert and Dhaliwal is an arXiv preprint. A chapter by Alexa Alice Joubin on teaching Shakespeare with generative AI was left out because its PDF is a Springer chapter under exclusive license. Two of the five are by Lauren Goodlad, which gives the synthesis's over-representation rule something to catch.

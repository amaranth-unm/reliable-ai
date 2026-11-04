# Understanding Agentic AI · presenter guide

Authoring references: ../../SESSION-STYLE.md and ../../sessions/audit-trails-for-ai-agents/index.md.
Session: ../../sessions/understanding-agentic-ai/index.md. Separate unlisted workshop draft, with no meeting date assigned. The starter folder's source is lit-review/ here; run scripts/build-agentic-workspace.py after editing it. Put rehearsal runs in _local/.

## The hour's purpose

Participants should leave able to say what makes a system agentic (it chooses intermediate actions, uses tools and responds to what they return), and to recognize the parts that shape an agent's work: a brief, standing instructions, skills, tools, saved state and helper agents. The vehicle is a small literature review on how the humanities are relevant to using and teaching AI. It is a stand-alone workshop. The audit trail session covers recording and verification; here the emphasis is on how the agent works and how you direct it.

Most of the room watches. Participants who already use an agent can download the starter folder and run the same prompts. Everyone can do step 1 in a browser chat and answer the observation questions in steps 3 to 6.

## What the demonstration should make visible

| Step | Concept | What to point at on screen |
|---|---|---|
| 1 | A reply versus actions | What exists after a chat reply: text, no files. |
| 2 | Brief, standing instructions, skills, tools | Edit one rule in the reading skill live. The agent's account of its tools before it acts. |
| 3 | Choosing the next step from a result | A failed or wrong download, and what the agent does next. sources.md filling in. |
| 4 | A skill shaping work | The agent reading page by page; the note's sections; one key idea checked against its page. |
| 5 | Helper agents, parallel work, a running synthesis | Two readers starting at once; the lead revising synthesis.md; the log entry after the second pair. |
| 6 | A fresh checker; state carried in files | One checker finding against its page; a new session's account from progress.md. |

## A 50-minute route

- 0–6: introduction and what makes AI agentic. Use three landmarks from the history table (Shakey, ReAct/Toolformer, current task environments) and the "try this with a partner" examples. Keep the rest for later reading.
- 6–9: open the starter folder. Show the hidden .claude folder and say what each file is for.
- 9–13: step 1. Participants send the baseline prompt in their own chat; ask the room what exists afterwards.
- 13–19: step 2. Edit one rule in read-article/SKILL.md (suggestion from the room). Start Claude Code and send the plan prompt.
- 19–27: step 3. Search and save. Narrate one action/result/next-action cycle as it happens. Open one PDF.
- 27–32: step 4. The lead reads S01. Check one key idea against its page with the room.
- 32–43: step 5. Readers in pairs, synthesis revisions. While readers work, talk through "When several agents help, and when they don't". Read the second log entry aloud.
- 43–48: step 6. Checker and leads; open one finding. If time is short, skip the fresh-session prompt and describe it.
- 48–50: takeaways.

Steps 3 and 5 take the most live time. If the run is slow, move on and come back to the files.

## Before teaching

- Rehearse at least once with a fresh copy of the starter zip in _local/rehearsal/. Time each stage and save the transcript and the finished folder.
- Check that Claude Code is signed in, that web search and downloads work on the venue network, and that the four article PDFs it is likely to choose open.
- Know the platform details: in Claude Code, helper agents (subagents) are defined in .claude/agents/, skills in .claude/skills/<name>/SKILL.md, and standing instructions in CLAUDE.md. Subagents cannot start their own subagents, which is why the lead is the main session. The lead can start two readers in one turn so they run in parallel. Recheck these before teaching; agent products change.
- Grant permissions before the session where you can, so approval prompts don't interrupt the room. Restrict the session to the lit-review folder.

## If the live run stalls

Keep the rehearsal folder open in a second window. If the search runs long, tell the agent to use the backup set in brief.md. If a stage fails, switch to the rehearsal folder and say so: it is a recorded run from an earlier date, not this one. Don't present rehearsal files as live output, and don't stage a failure in a run that worked.

## Points to make, and claims to avoid

- A chat interface can front a tool-using system, and a desktop agent can be used for one reply. Describe what the session can do, not the product category.
- A visible tool action shows what the agent opened, not whether it read fairly. That is why each step has a check against a page.
- Helper agents are the same model with different instructions and less context. Several replies do not amount to independent expertise.
- Don't claim anything about model internals. Point to actions, files and results.
- Uniqueness and overlap are cross-note judgments. The reader skill records what an author claims is new; the relating skill decides what is distinctive in the set. The split comes from the CHM chapter's reading protocol, which found that a reader who can see the running synthesis tends to recruit each new source to it.

## Historical and current references

- SRI's Shakey retrospective: https://www.sri.com/case-study/the-man-the-myth-the-legend-meet-shakey-the-robot-the-worlds-first-ai-based-robot/
- Wooldridge and Jennings, Intelligent Agents: Theory and Practice (1995), weak notion of agency: https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/ker95/subsubsectionstar3_1_1_1.html
- ReAct (2022 preprint; 2023 ICLR camera-ready): https://arxiv.org/abs/2210.03629
- Toolformer (2023): https://arxiv.org/abs/2302.04761
- Anthropic's 2024 workflow/agent distinction (historical framing; not a current product inventory): https://www.anthropic.com/engineering/building-effective-agents
- Current OpenAI documentation checked 2026-10-11: https://developers.openai.com/blog/run-long-horizon-tasks-with-codex and https://learn.chatgpt.com/docs/browser

This is a selected conceptual history, not an etymology of "agentic" or a claim that one paper invented agents. Recheck current product capabilities before teaching.

## Backup set

The five PDFs in brief.md were downloaded and their first pages checked on 2026-11-04. Perlow (PMLA) is published by Cambridge with an author copyright line; Nobile et al. is CC BY 4.0; the Goodlad proof and the Rutgers guide are hosted by their own projects; Offert and Dhaliwal is an arXiv preprint. A chapter by Alexa Alice Joubin on teaching Shakespeare with generative AI was left out because its PDF is a Springer chapter under exclusive license. Two of the five are by Lauren Goodlad, which gives the relating skill's representativeness rule something to catch.

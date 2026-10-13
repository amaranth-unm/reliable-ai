# Understanding Agentic AI · presenter guide

Authoring references: ../../SESSION-STYLE.md and ../../sessions/editorial-assistant/index.md.
Session: ../../sessions/understanding-agentic-ai/index.md. Separate unlisted workshop draft, with no meeting date assigned. All development and rehearsal files belong in this repo; put local runs in _local/.

## The hour's purpose

Participants should be able to explain an agent through its goal, available tools, intermediate choices, feedback and saved state, and choose a useful task to delegate. The payoff is a working research aid and a steered revision. Documentation supports continuity; it is not the center of this introductory workshop.

Compare question-and-answer interaction, a fixed workflow and an adaptive tool process. “Browser chat” is an interface description, not a reliable capability boundary. Avoid saying all browser assistants only return prose or that installing a desktop app guarantees autonomous work. A long response, a written plan or generated code does not establish that tools were used.

## Teach five practical skills

Assume participants know how to ask for a reply but have little experience with an ongoing AI project. Introduce each concept by pointing to something they can use, then have them make a small choice.

| Skill | Concept to introduce | What participants should do |
|---|---|---|
| Prepare the workspace | Materials, instructions and results live together; access does not establish that a file was read. | Locate one source, brief.md and the destination for new files. |
| Delegate a result | An outcome, boundaries and completion conditions give the agent room to choose actions. | Edit the organizing priority in the supplied brief and choose a plan. |
| Follow the work | A proposed step, tool action and returned result are different. Outputs connect the stages of a workflow. | Name one action actually carried out and the file or result it produced. |
| Steer and judge | Feedback can change the next action; useful categories still need human judgment. | Predict a filter result, try it and give one specific change request. |
| Continue and reuse | Saved project state and reusable directions help carry work between conversations when the files are read. | Check a fresh conversation's account of the current files and next task. |

Success means participants can make these choices and explain their purpose. Producing a polished page in a particular app is not the threshold. Use the folder and visible actions to make the vocabulary concrete. Introduce model, tools, workspace and workflow as they appear; leave harness, orchestration and multi-agent architectures for questions.

## A 60-minute route

- 0–5: show the ordinary practice folder. Open a source and the brief, point to the output destination and describe the useful result. Participants locate those three parts; explain how outputs will connect the stages.
- 5–8: selected history and working definition. Use goals/actions before LLMs, language-model tool use and today's accessible task environments as three landmarks. Keep the fuller table for later reading.
- 8–14: give the five practice sources to the assistant and save baseline advice (step 1). Read I03's uncertain date together and classify advice, a fixed sequence and adaptive action.
- 14–22: edit one field in the supplied brief, check tools and choose a plan (step 2). Ask participants to name the requested result and one completion check.
- 22–35: let the agent build for at most five minutes, then open its files and guide. Observe one action/tool-result/next-action cycle. Everyone tries the guide or predicts a search result before you run it (step 3).
- 35–47: request the source-type filter; predict and try Interviews, poster, clear-search; watch a focused repair if a check fails (step 4). Do not manufacture a failure in a live run that worked.
- 47–54: write a short handoff and read it in a fresh conversation (step 5). Optional two-minute plain-procedure/skill explanation comes here.
- 54–60: partners specify one task from their own work and what they will judge. Compare useful work completed with directing/checking effort.

For 50 minutes, use 4 minutes of workspace orientation, 2 history, 5 baseline, 7 briefing/tools, 12 build/open, 10 revision, 5 handoff and 5 transfer. Keep at least one build-and-check cycle. If time is short, omit the skills demo and use the prepared guide rather than troubleshooting software.

## One exercise, different levels of participation

Everyone makes the organizing choice, predicts or tries a result and gives feedback. Browser-chat participants can use the combined text, save replies and inspect the presenter's guide. File-agent participants can generate their own outputs. Pair people for choices and checks rather than requiring everyone to install the same environment.

For beginners, supply the brief and procedure; ask them to change one field and one requirement. Have them point to a file after each important stage. They should see that a workspace carries the materials and results forward, while a workflow connects the work done with them.

For experienced participants, keep the same task but invite one additional check, a second organizing approach or a comparison of the files changed during revision. Have them judge whether extra delegation reduced coordination effort. Keep extensions off the room's critical path.

Use quick observations to check understanding: “Which file did it read?”, “What exists now?”, “What will this filter show?” and “What would the next conversation need?” Give participants time to answer before the presenter demonstrates. This keeps a demo participatory even when tools differ.

## Before teaching

The assumed access is mixed. Use an already configured file-access agent and browser as presenter. Participants with those tools can perform the actions; others can use practice-pack.md, save replies and compare the presenter's actions against the same brief. No API keys, installing a coding environment, connectors or paid plan promises during the workshop. Check account capabilities before the session.

Download city-memory-starter.zip and rehearse with a fresh extracted copy. For presenter rehearsals keep that copy in workshop-drafts/understanding-agentic-ai/_local/rehearsal/. Save exact prompts, observed actions and outputs from real runs there. Prepared data and the reference guide are teaching constructions; never introduce them as recorded agent replies.

The practice sources are fictional. Five files vary in format and epistemic status: a planning note, named-speaker interview excerpt, uncertain photograph label, an interpretive research note and a poster CSV with ambiguous venue/date fields. The inventory has one row per file, not one row per internal CSV record. I03's date stays c. 1975; I02 stays date unknown. Themes are curatorial decisions, not facts discovered by counting.

Open the folder and editor beside the agent. Teach from the long page; a slide deck is optional and unnecessary for the file/action demonstration. Keep a prepared reference guide available at /examples/understanding-agentic-ai/ so generation delays do not consume the workshop. The reference already includes the source-type filter; reveal it after participants specify the change.

## Show the choices, not every technical detail

Pause once after a meaningful action. For example, the agent sees an uncertain date and chooses a text field, or a browser result reveals a filter interaction and it repairs the relevant code. Distinguish a visible plan/explanation from hidden reasoning. You can inspect a tool action, output or changed file without requesting private reasoning traces.

If the assistant lacks a tool, let it name the limit and produce the parts it can. Keep the same task and compare the remaining manual work. A browser-only session may still create downloadable files or use tools; describe observed capabilities, not product categories.

If live generation fails, show the prepared guide and try the acceptance checks together. Label the fallback. If everything works, change a real requirement rather than inventing a transcript of failure.

## Handoff and optional skills

A fresh conversation should read the current files and report the next unfinished action before edits. Saved files carry state; a name like “memory” does not establish that a feature retained the right information. Ask what context it read.

Use procedure.md to explain reusable instructions. A skill adds packaging and activation guidance, with optional resources; tools supply actions. Do not require installing or creating a skill in the hour. A new procedure does not grant new capabilities.

Multiple agents, scheduled runs and connected services can be mentioned as extensions. They are not prerequisites or evidence of quality on their own. No email, account actions or live shared-data changes are needed for this workshop.

## Historical and current references

- SRI's Shakey retrospective: https://www.sri.com/case-study/the-man-the-myth-the-legend-meet-shakey-the-robot-the-worlds-first-ai-based-robot/
- Wooldridge and Jennings, Intelligent Agents: Theory and Practice (1995), weak notion of agency: https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/ker95/subsubsectionstar3_1_1_1.html
- ReAct (2022 preprint; 2023 ICLR camera-ready): https://arxiv.org/abs/2210.03629
- Toolformer (2023): https://arxiv.org/abs/2302.04761
- Anthropic's 2024 workflow/agent distinction (historical framing; not a current product inventory): https://www.anthropic.com/engineering/building-effective-agents
- Current OpenAI documentation checked 2026-10-11: https://developers.openai.com/blog/run-long-horizon-tasks-with-codex and https://learn.chatgpt.com/docs/browser
- Skills: https://developers.openai.com/plugins/build/skills

This is a selected conceptual history, not an etymology of “agentic” or a claim that one paper invented agents. Recheck current product capabilities before teaching. Research-paper summaries on the page rely on their abstracts; the historical agency discussion uses the named section, not a full literature survey.

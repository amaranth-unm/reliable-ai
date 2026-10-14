# Small supervisor interventions: transcribing handwriting with AI

Prepared October 13, 2026 for the October 14 Reliable AI session. Authoring reference: ../../SESSION-STYLE.md. These are optional supervisor cues and proposed prompts, not a replacement presentation. No student slides or public session text have been edited.

## What the additions should accomplish

The presentation already introduces tools, a Transkribus demo, harder scripts, second-model checking and batches. Add the small actions that connect those topics: specify the kind of transcription, examine a difficult word, compare readings against the image and save a usable result. Carry one short passage through these actions. About eight minutes total is enough; use only the first and third intervention if time is tight.

## Separate slides

The standalone browser deck is at /sessions/transcribing-handwritten-documents/supplemental-slides/. Its opening slide links to four independent topics. Use these links or All slides to switch to an example, then return to the student's presentation. The deck has eight slides and is unlisted.

## Have this ready

- One image and a four-to-eight-line passage you can read yourself. Use the student's existing English example if it is manageable. A downloaded fallback is in _local/lincoln-to-bedell.jpg; source links and a prepared comparison are in prepared-comparison.md.
- The prompts in prompts.txt, open for copying.
- An image viewer that can enlarge the passage, and a text editor beside it. Enlarging the original is enough; keep the full page available when a letter comparison needs context.
- If using live assistants, two fresh conversations with the same image and conventions. Obtain the second reading before showing it the first. Keep both original replies. Record the actual tool/model label, date and prompt if you save them in _local/.
- The prepared comparison as a fallback. It is a deliberately constructed teaching contrast, not an AI run. Introduce it that way.

## 1. A two-minute prompt clinic

Insert after the slide “Train a model, or try a commercial LLM” (#llms), or after the first transcription demo.

Supervisor transition: “Let's make the next move concrete. What should we tell an assistant before it reads this page?”

Ask the room to choose the purpose: faithful transcription for checking, or a modern reading aid. For this exercise, choose faithful transcription. Show Prompt 1. Point to three decisions: original spelling stays; line breaks give locations to check; uncertain readings remain visible. Our bracket notation is an exercise convention, not a universal standard.

Send it with the image, or show the prepared reference. Have attendees find the same line in the image and text. If the assistant changes spelling or expands an abbreviation, identify it as a change to correct. A prompt specifies the desired behavior; it does not establish that the assistant followed it.

The Smithsonian's transcription instructions also preserve original spelling, grammar and abbreviations, while marking uncertainty. Projects differ in layout and notation rules, so pick a convention explicitly. [Smithsonian guide](https://transcription.si.edu/instructions/transcribe).

## 2. A three-minute “one difficult word” exercise

Insert after any transcription result. Use one word you genuinely cannot immediately resolve. In the fallback passage, ask the room to look at “affectation” before revealing the reference reading; the prepared comparison offers “affection” as a deliberately altered alternative.

Supervisor transition: “The useful next prompt can be much smaller than ‘do the whole page again.’ Let's investigate this word.”

Enlarge the passage, keeping neighboring words visible. Give attendees 20 seconds to suggest a reading. Then use Prompt 2: ask for possible readings, visible letters and a comparison with the same hand elsewhere on the page. Judge those observations against the image. An explanation about letter shapes can itself be mistaken.

Accept an unresolved result when the image does not settle it. If the scan is inadequate, the next action is a better image or another reader. Do not force the model to choose a word merely to finish the transcript.

## 3. A two-minute second-reader demonstration

Insert at “Have a second model check the first” (#llm-checking).

Supervisor transition: “The second reader needs the original image too. Let's use it to locate disagreements we can inspect.”

For a live run, reuse Prompt 1 in a fresh conversation with the image. Obtain its own reading first. Then supply both readings and use Prompt 3. If time is short, compare two saved real replies; if none are available, use the labeled prepared contrast.

Show one row: location, reading A, reading B, what the image supports, and your decision. Include omissions and line ordering, not only spelling. Keep unresolved alternatives visible. Agreement is not verification: inspect at least one agreed passage as well. Before quoting a passage or extracting a name, date or number for research, check that material directly against the image. This demonstration is a proposed checking procedure, not a claim about a measured accuracy improvement.

Use the separate supplemental slide to make the image requirement explicit; supplying another model's text alone allows comparison of texts, not a visual check of the handwriting. Keep each original reading and create a separate checked version.

## 4. A one-minute “what you take home” example

Insert at the batch slide (#example-of-aca-batching), or use it to close.

Show an ordinary project folder:

```text
one-document/
  original.jpg
  instructions.txt
  draft-a.txt
  draft-b.txt
  checked-transcription.txt
  review-notes.csv
```

Point to the distinction between an AI draft and the version a researcher has checked. In a saved run, review-notes.csv records only actual decisions. Use the supplied blank template, not invented results. An unresolved word can remain unresolved in the checked transcription; describe the extent of review accurately.

Finish with a task-sized next step: “Try one page, choose your transcription conventions, check a few consequential readings, then decide whether this is worth scaling.” For a quotation, check the complete quoted passage. For a search aid, keep clear that it is a draft index and verify passages found through it. These are different levels of intended use.

## A few brief clarifications to have ready

- **Batching and agents:** batching is processing several files; it does not itself require an agent. Transkribus already lets users select multiple pages or documents for recognition. An agent can help coordinate additional steps such as organizing outputs and revisiting flagged pages. [Transkribus recognition instructions](https://help.transkribus.org/automatically-transcribing-your-documents).
- **HTR and LLMs:** an HTR recognition engine is not automatically a general chatbot. Transkribus documents PyLaia recognition models and separate transformer Super Models. The slide notes' “PyLaia eyes / LLM brain” description should not be used as a general explanation of its architecture. [Choosing a model](https://help.transkribus.org/choosing-a-model), [Super Models](https://help.transkribus.org/super-models).
- **Ranks and confidence:** use the same passage to show the task and its checks. Do not turn one successful run, a confident explanation or this prepared example into a general model ranking. The existing state-of-field report is AI-generated and calls for source checking; this supplement does not validate all of its comparative claims.

## Rehearse once

Make sure the image is readable on the projector. Try the first-pass prompt and one-word follow-up; save the exact replies if you will show them. Choose one result for the audience to judge, which can be correct, uncertain or wrong. Keep the reference reading out of the assistant's input during the initial read. The Lincoln document is famous and may already be familiar to a model: it illustrates a procedure, not performance on an unseen manuscript.

The downloaded image is an unaltered Library of Congress exhibition facsimile of an 1860 letter. Its content is public domain; the exhibition identifies the lender as the Benjamin Shapell Family Manuscript Foundation. Keep the source credit with it. The exhibition transcript linked in prepared-comparison.md covers only the final substantive paragraph, not the whole letter. All material here remains in the reliable-ai repo; local images and rehearsal runs are in its ignored _local/ folder.

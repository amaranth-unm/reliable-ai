# Literature review: how the humanities are relevant to using and teaching AI

This folder holds a small literature review run in stages. Each stage has its own instruction file and produces its own files. Read `progress.md` to see where the work stands.

## Read first, in this order

1. `progress.md`: what exists, what's unfinished, and the next action.
2. `brief.md`: the question, scope, limits, and backup set.
3. `instructions/`. Follow the file for the stage you're working on, and only that file:
   - `reading.md`: reading an article and writing its note.
   - `synthesis.md`: writing and revising the synthesis.
   - `checker.md`: checking the synthesis.
4. `synthesis.md`, then the latest entry in `synthesis-log.md`.
5. `checks.md`, if the next action concerns the check findings.

Open the notes in `notes/` and the PDFs in `pdfs/` only when the current stage needs them.

## Stages, in the order they were run

1. **Search and choose sources.**
   - Ran five searches within the brief's limits and recorded each one in `sources.md`, worded exactly.
   - Downloaded each chosen PDF into `pdfs/` as `S0N-surname.pdf` and confirmed the title and author on its first page.
   - Failed downloads and unusable files were deleted and listed as leads at the end of `sources.md`.
   - The searches yielded three sources, so S04 came from the brief's backup set. `sources.md` says so.
2. **Read S01 and S02** (main session), following `instructions/reading.md`. Wrote `notes/S01-tadimalla.md` and `notes/S02-klein.md`.
3. **Synthesis version 1** (main session), following `instructions/synthesis.md`, using the S01 and S02 notes only. Started `synthesis-log.md`.
4. **Read S03 and S04** with two helper agents running at the same time, one per PDF. Each was given only its PDF's path and `instructions/reading.md`, and was told not to open other files. They wrote `notes/S03-adisa.md` and `notes/S04-perlow.md`.
5. **Synthesis version 2** (main session).
   - Copied version 1 to `history/synthesis-v1.md`.
   - Revised `synthesis.md` to cover all four notes, after checking the authors' citations of one another and spot-checking quotations against the PDFs.
   - Appended the version 2 entry to `synthesis-log.md`.
6. **Check** with one helper agent, given only the instruction to follow `instructions/checker.md`. Its findings (C01–C22) were saved word for word in `checks.md` under the date 2026-11-11. **None has been applied.**

## When to use a separate helper agent

Use a helper only where its independence matters, and give it only what the instructions name:
- **Reading a source**, so the note isn't shaped by the other notes or the synthesis. Give it the PDF's path and `instructions/reading.md`, and tell it not to open other files. Run several helpers at the same time when there are several PDFs.
- **Checking the synthesis.** Give it only the instruction to follow `instructions/checker.md`. Save what it returns word for word in `checks.md` under that day's date, and don't apply anything without the user's decision.

Do everything else in the main session: searching, synthesis, revisions, the log and progress updates. Don't start helpers unless the user asks.

## Files

| File | What it is |
|---|---|
| `brief.md` | The brief. Do not edit. |
| `instructions/reading.md`, `synthesis.md`, `checker.md` | Instructions for each stage. Do not edit. |
| `sources.md` | The searches, word for word, then sources S01–S04 (citation, date, URL, filename, why it fits), then leads. |
| `pdfs/S01-tadimalla.pdf` … `S04-perlow.pdf` | The source PDFs. Do not rename, replace, or delete them. |
| `sample-pdfs/` | Backup copies supplied with the brief. Do not edit. |
| `notes/S0N-surname.md` | One note per PDF, with the same name as the PDF. |
| `synthesis.md` | The current synthesis. It has a version number, lists the notes it includes, and has points P01, P02 … |
| `history/synthesis-vN.md` | Earlier versions of the synthesis. Never edit them. |
| `synthesis-log.md` | Append-only log of each version: the notes added, and the point IDs added, changed, weakened, or removed, with reasons. |
| `checks.md` | Checker findings, word for word, with the date. Append new rounds; don't edit earlier ones. |
| `progress.md` | Current state and next action. Update it at the end of each stage. |

## What not to change

- `brief.md`, `instructions/`, `pdfs/`, `sample-pdfs/`, and `history/`.
- Point IDs. A point keeps its ID through every revision. A new point takes the next unused number, and a removed point's number is never reused (P01–P18 are used so far). Never drop a point silently.
- Earlier entries in `synthesis-log.md` and `checks.md`. Only append to them.
- The checker's findings. Don't apply them, or edit `synthesis.md` in response, until the user has decided which to accept.
- Don't search for or add sources beyond S01–S04. The brief allows four.
- Don't commit to git; the user hasn't asked for commits.

## Working notes from this review

- **Page counts:** the `file` command misreported S01 and S02 as 8 pages; they have 23 and 24. Count pages by counting form feeds in `pdftotext` output.
- **Page numbers:** cite PDF page numbers.
  - For S01–S03 these match the printed page numbers.
  - For S04, PDF pp. 1–5 are journal pp. 548–552.
- **Reading pages:** the Read tool can open PDF pages as images using `pages`. `pdftotext -f N -l N` gives the text of a single page. `pdfinfo` and `pdftoppm` required permission in this environment.
- **Text-layer quirks:** S01's text layer prints "usage" as "U.S.A.ge" and "refusal" as "RefU.S.A.l". Quote with care.
- **Links between authors:**
  - No source cites another source in the set.
  - S02 mentions the MLA-CCCC task force and its working papers in general (ref. [13]), not S03.
  - S02 cites Kirschenbaum and Raley's *PMLA* essay (ref. [106]), the piece S04 responds to, not S04.
  - Connections between sources are therefore marked "Read alongside …".

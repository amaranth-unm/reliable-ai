# Alexandra Ruiz CV audit key

Presenter copy. Do not attach this file when running the audit. The `_instructor` directory is omitted from the normal Jekyll site build; this is organizational separation, not access control for the repository itself.

## The specimen

File: `assets/documents/alexandra-ruiz-cv-workshop.docx`.

Four Letter-size pages: education and experience; publications and projects; presentations and workshops; teaching, awards, service, and tools. The document has 46 dated or cited records, two short descriptions of research in progress, and a professional membership without dates. Overlapping entries are deliberate; the count is not a claim of 49 distinct accomplishments.

The base is the [Alexandra Ruiz sample CV](https://xanthan-web.github.io/alexandra-ruiz/cv), retrieved September 23, 2026. The core education, three original positions, two publications, three presentations, three awards, and original service activities were retained or condensed. New entries are fictional extensions in digital public history, community archives, and teaching. Contact details were replaced with placeholders. No personal facts from the presenter's CV were inserted.

The document contains 20 audit targets below. Some are definite inconsistencies; others are questions or maintenance concerns. This is a deliberately constructed specimen, not a blind test of model performance. No model audit has yet been recorded.

## A short demonstration

For the existing three-minute CV slot, show the first page briefly and ask what looks wrong. Run or show a previously recorded first-pass audit. Examine one citation inconsistency and the publication-status conflict. Then show the separate structure prompt and reveal the borderless table containing only the oldest talks. Close by asking which findings justify a change and which need an answer from the author.

Keep the full list for the self-guided tutorial. Trying to uncover all 20 items in the presentation would crowd out the lesson about evaluating findings.

Before the workshop, run the prompts in a fresh conversation with the intended tool and only the specimen attached. Save the exact prompts, full output, tool, date, and any limitations. A missed item is part of the demonstration; do not substitute this key and present it as the tool's output. The second prompt gives explicit categories to inspect, so it is a guided follow-up, not an independent discovery test.

## Text and visual consistency

| No. | Location | Evidence | Appropriate response |
| --- | --- | --- | --- |
| 1 | Page 1, professional experience | `2019-2020` uses a hyphen; comparable year ranges use en dashes. | Suggest a consistent range mark without changing dates. |
| 2 | Page 1, project coordinator | `2024–Present` capitalizes Present; other ongoing entries use `present`. | Identify the local difference and propose the prevailing form. |
| 3 | Page 2, Teaching with Unfinished Collections | `Ruiz, A.` contrasts with `Ruiz, Alexandra` elsewhere. | Flag the author-name form; confirm the identity before expanding initials. |
| 4 | Page 2, Listening at Scale | `Public Humanities Methods` is upright; other journal names are italic. | Point to the comparable journal-title treatment. Text extraction alone may lose this distinction. |
| 5 | Page 2, Digitizing the Borderlands | `45-62` uses a hyphen; other page ranges use en dashes. | Propose a punctuation-only change. |
| 6 | Page 3, Augmented Reality in Teaching Regional History | Straight double quotation marks instead of the curly quotation marks used for other conference titles. | Treat as a minor consistency issue. |
| 7 | Page 3, Teaching Students to Read a Digital Exhibit | A 2024 item appears after the 2023 Virtual Museums presentation in a predominantly descending list. | Ask whether to restore date order; preserve the dates themselves. |
| 8 | Page 2, A Small Museum’s Digital Field Notes | This citation has an explicit 10.5-point override; comparable citations inherit 11 points. | Confirm the property rather than judging from appearance alone. |
| 9 | Same citation | Hanging-indent width is 0.25 inch; the citation style uses 0.22 inch. | Identify the local override. It is only apparent if the entry wraps; it can still affect later editing. |

## Questions for the author

| No. | Location | Evidence | Appropriate response |
| --- | --- | --- | --- |
| 10 | Page 2, publications and research in progress | Small Archives, Shared Stewardship is both `Forthcoming` and `Article in preparation`. | Ask which status is current and whether these are the same work. Do not promote or demote it automatically. |
| 11 | Page 3, conferences and invited workshops | The same Virtual Museums title, conference, year, and city appear in both sections. | Flag a possible duplicate or an unexplained difference in role. A talk and a workshop at one event can be distinct. |
| 12 | Page 2, Reimagining the Museum chapter | The chapter citation has no page range. This absence was retained from the source CV. | Request pages if the chosen citation convention requires them; never fabricate them. |
| 13 | Page 4, professional membership | The Digital Public History Working Group membership has no dates, while surrounding service entries do. | Ask whether dates should be supplied or memberships separated from dated service. An undated membership is not inherently wrong. |

## Word structure and inherited formatting

| No. | Location | What is actually in the file | Why it is useful to discuss |
| --- | --- | --- | --- |
| 14 | Page 1, Professional Experience | A Normal paragraph with direct bold and 12.5-point formatting. Other peer headings use Heading 1. | It looks correct but is absent from the heading hierarchy used for navigation and global style changes. |
| 15 | Page 1 contact block and page 3 oldest talks | Two real borderless tables: one row by two cells for contact details, and four rows for the 2022–2020 talks plus an empty row. Newer talks are ordinary paragraphs with tab stops. | Similar-looking content is built differently. Table detection is useful; deleting all tables is not automatically an improvement. |
| 16 | Page 3, after the 2020 talk | The last row of the talks table is empty and merged across both columns. | A small inherited spacer that can complicate later insertion, selection, and conversion. |
| 17 | Page 4, DH Praxis Workshop | The paragraph uses `CV Entry 2019` with 5-point after-spacing; peers use `CV Entry` with 6 points. | Nearly identical styles can drift apart during later global edits. |
| 18 | Page 3, The Work after Launch | The paragraph and runs explicitly use `en-GB` proofing language. Other ordinary entries inherit the default `en-US`. | A visually undetectable setting that can change proofreading behavior. |
| 19 | Page 2, Migration Stories Online | A hidden run reads `[2023 draft note: replace temporary collection link before circulation.]`. The run has Word's hidden-text property; normal display and hidden-text printing are disabled. | The note is absent from the normal rendered pages but still exists in the file. An extractor may expose or omit it. Its embedded date is part of the fictional exercise, not evidence of an actual editing history. |
| 20 | Page 1, website link | Display text is `alexandra-ruiz.example`; the actual destination is `https://alexandra-ruiz.example/archive/2022`. | Ask whether the archived destination is intended. A short label pointing to a deeper path is not itself a broken link. This is a fictional placeholder, not a website availability test. |

## Things a good audit should leave alone or qualify

The same teaching assistantship appears under both experience and teaching. That can be useful cross-listing. Ongoing service precedes completed service; that is a defensible ordering rule. The awards list follows starting years, so a multi-year award need not be moved merely because it ended later. Two ongoing roles can overlap. The Ph.D. remains in progress. The presentation titles and fictional publication claims should not be verified as if they described a real applicant.

The body uses tab stops for a date column. That is a valid layout choice. Borderless contact tables, manual page starts, and a page-number field can also be intentional. The task is to explain their behavior and maintenance implications, not to insist that every CV adopt one template.

## How to verify

For textual findings, compare the quoted entries directly. For the hidden structures, use Word's table gridlines, Styles pane, navigation headings, formatting controls, language settings, hidden-text display, and hyperlink editing controls. Exact menu locations depend on the version of Word. The Show/Hide paragraph-mark control alone may not reveal every kind of hidden text, depending on display settings.

A tool with access only to extracted text cannot reliably verify border settings, precise typography, style inheritance, proofing language, or link relationships. It should report that limitation. An assistant with document-inspection tools can check these properties, but actual findings must be verified in the returned evidence.

The specimen was checked both as a four-page render and as a Word file. The intended hidden run, two tables, merged empty row, direct formatting, alternate style, language override, and hyperlink target were verified in the file structure. The original DOCX was retained; the render was not saved back over it.

## Relation to the reference CVs

The local comparison used `cv 2026.docx` (September 2026), `gibbs-cv-2pg.docx` (May 2026), and `gibbs-cv-admin-tech.docx` (November 2024). This was a focused comparison of document structure and representative formatting, not a comprehensive factual audit of the presenter's career.

The September file contains two tables, including contact and education layouts, plus several local indentation values. The May file contains a borderless nine-row table for older talks and four sections. The November file has four sections and no tables. All three use different combinations of paragraph styles and direct formatting. These are observed differences; their names or structure do not prove how or when they were introduced.

The specifically named `gibbs-cv-sep2026.docx` and its PDF were zero-byte local files during this review, so that named revision could not be compared. No original CV was modified.

# Checks

## 2026-11-11 — check of synthesis.md version 2

The findings below are recorded as the checker helper returned them. None has been applied.

---

I checked the synthesis (version 2, points P01 to P18) against the four PDFs and found 22 problems, listed below as C01 to C22. Two kinds stand out. Several "only one source" and "all four" claims fail against the PDFs, and four overlaps join sources whose passages answer different questions. No file was edited. The text I pulled from the PDFs for checking is in the scratchpad (for example […]). Every proposed change waits on a person's decision.

## Claims that only one source offers something, or that none does

**C01.** P04: "S01 now stands alone" in routing the humanities through ethics.
- **Source:** S03 p. 17 says institutions that "foreground the crucial role of humanities disciplines, such as … philosophy and ethics, history, and cultural studies" help STEM students understand "why ethics and integrity … are so important."
- **What's wrong:** S03 also routes the humanities through ethics, in its institutional section, so S01 is not alone.
- **Proposed change:** Add S03 p. 17 to P04. Say S03 routes the humanities through rhetoric and literacy for teaching and through ethics for institutions. Drop "S01 now stands alone." Revisit the Interpretation sentence, which depends on it.

**C02.** P07: "Only S01 offers the four-pillar framework and its civic framing."
- **Source:** S03 p. 17 (heading "Citizenship, Ethics, and Integrity as Institutions"; students "develop as global citizens"; "preparing GAI-literate citizens") and p. 21 ("prosocial and prodemocratic goals").
- **What's wrong:** S03 also frames AI ethics in civic terms, though much more briefly than S01's pp. 13–15.
- **Proposed change:** Keep S01's developed civic pedagogy as unique, but note that S03 gestures at the civic frame.

**C03.** P08 and the v2 log: "histories of capitalism applied to compute" was removed from S02's unique list "because S04 also places these costs in history."
- **Sources:** S02 p. 12 draws on histories of capitalism, data colonialism (Couldry and Mejias) and colonial labor. S04 p. 4 only compares AI's labor to "microtask and moderation labor economies" and its energy use to blockchain.
- **What's wrong:** S04 makes a contemporary comparison, not a historical analysis of capitalism. The removal is not supported.
- **Proposed change:** Restore the item to P08, and correct the log entry.

**C04.** P15, and P08's reason for removing consent: P15 lists S02, S04 and S03 on training-data consent and says nothing about S01.
- **Source:** S01 p. 15 says students must analyze "the ethical ramifications of using public data—often without explicit public consent—to train proprietary models."
- **What's wrong:** S01 addresses training-data consent and is left out.
- **Proposed change:** Add S01 p. 15 to P15, on the consent side, without a developed position.

**C05.** P09 Interpretation, repeated in P11: the set "still offers nothing on everyday research uses such as reading, transcription or translation at scale."
- **Sources:**
  - S02 p. 9: a fine-tuned model "to transcribe and transliterate one hundred years of scans of Malay-language newspapers."
  - S01 p. 12: translation tools in a humanities course, and AI-assisted source finding.
  - S03 p. 7: brainstorming and "summarizing an unfamiliar source."
  - S03 p. 19: automated translation compared with language departments.
- **What's wrong:** Several sources touch these uses, though none develops a workflow for them.
- **Proposed change:** Reword to "touches transcription, translation and summarizing only in passing (S02 p. 9; S01 p. 12; S03 pp. 7, 19); no source gives guidance on everyday research workflows."

**C06.** P11 and P12: "History and the arts appear only through S02's examples"; "philosophy appears mainly as S02's foil."
- **Sources:** S03 p. 17 names philosophy, ethics and history. S04 is largely about poetry, art, aesthetics and image generators (pp. 1–5). S01 p. 5 mentions "creative disciplines like arts and architecture."
- **What's wrong:** The claim understates what the other sources say.
- **Proposed change:** Reword to: history, philosophy and the arts are named but not treated as disciplines with their own methods, except literary and aesthetic criticism in S04.

**C07.** P11: "Agentic or multi-step AI tools (per the S03 note)."
- **What's wrong:** The claim is right. I searched the text of all four PDFs and found no mention of agentic tools or AI agents. But the synthesis sources a set-wide claim to one note's Interpretation.
- **Proposed change:** Cite it as checked against all four sources, not "per the S03 note."

## Overlaps that join passages on different questions

**C08.** P03: "all four warn against mistaking fluent output for knowledge."
- **Source:** In S04, "imply (wrongly) that LLMs have mental states" (p. 2) is about prompting effects. "Fabricates evidence and behaves unpredictably" (p. 3) is Perlow describing what media theorists consider. S04's own emphasis on p. 3 runs the other way: "The greater mistake is not to see machine-written texts as expressive of consciousness." On p. 1 it also criticizes humanists' defensive reflex.
- **What's wrong:** S04 does not take up the question of output as knowledge.
- **Proposed change:** Make it "S01, S02 and S03." Move S04 to a note that it mentions unreliability only in passing and puts its emphasis elsewhere (P13).

**C09.** P06: "S02 and S04 put their emphasis on taking part on better terms," citing S04's "hack, pirate, and otherwise mess with" (p. 5).
- **Source:** The S04 sentence closes its argument on copyright and the "enclosure of the language commons" (p. 5). It is not about whether to use AI.
- **What's wrong:** It is a different question.
- **Proposed change:** Remove S04 from P06, or say plainly that S04 does not address non-use.

**C10.** P16: S01 is placed in a "real disagreement" about whether environmental costs are a distinctive objection.
- **Source:** S01 p. 5 gives a single energy estimate (IEA) and says "many of the concerns are real." It does not discuss whether these costs are specific to AI.
- **What's wrong:** S01 is not on either side of the question at stake.
- **Proposed change:** Record S01 as mentioning energy costs without taking a side on distinctiveness, and keep the disagreement to S02 and S04.

**C11.** P16: "S04 argues against Bender et al., whom S02 cites approvingly (S02 ref. [20])."
- **Source:** S02 cites [20] only on p. 5 (communicative intent, which S02 then supplements) and p. 7 (cultural harms). It never cites [20] on energy or labor. Its p. 12 cost passage cites other works ([188], [189]).
- **What's wrong:** As written, it suggests the two sources share a reference on this question. They do not.
- **Proposed change:** Delete the sentence, or say [20] is cited by S02 on other questions.

## Connections presented as the authors' own

**C12.** P14: "the same claim, made independently (neither cites the other)."
- **What's wrong:** It is true that neither cites the other, and S04's prompting passage cites Kojima, Zou and Welsh, not Kirschenbaum and Raley. But P12 itself flags one network: Kirschenbaum is an S03 author, and his prompt essay with Raley is what S04 answers. "Independently" overstates it.
- **Proposed change:** "made without citing each other, though within the network noted in P12."

**C13.** P12: "S02 cites him twice (refs. [105], [106])."
- **Source:** S02 ref. [13] (the task force page) also lists Kirschenbaum. It lists Byrd, Flores, Green, Hassel, S. Z. Johnson, Lockett, Losh and Mills too, all of whom are S03 authors (S03 p. 2).
- **What's wrong:** S02 cites him three times, and its link to S03's authors is closer than the synthesis says. The synthesis is still right that S02 does not cite S03 itself.
- **Proposed change:** Correct the count and add the overlap in authors. This strengthens P12.

**C14.** The opening section and P12: Kirschenbaum and Raley's essay "is the prompt S04 responds to (S04 p. 3)."
- **Source:** The phrase "In their prompt for this PMLA special feature" is on S04 PDF p. 2.
- **Proposed change:** Correct the page to p. 2, in both places.

## Wrong source or wrong page, and dropped qualifications

**C15.** P14: the claim that prompting is rhetoric, "which humanists already know how to do," with S01 as the dissenter.
- **Sources:** S03 p. 8 itself warns that "technology-specific strategies for prompting LLMs are likely to change" (citing Mollick). S04 p. 2 hedges ("may feel more familiar to literary critics") and expects prompting to be "formalized and regularized through automated prompt transformation."
- **What's wrong:** Both qualifications point toward S01's worry that prompting skills will become obsolete, and both are dropped. The title also overstates S04.
- **Proposed change:** Add both qualifications. Soften the title for S04. Note that S01's dissent is partly shared within S03 and S04.

**C16.** P15: S04's position on copyright.
- **Source:** S04 p. 5 also says "we should respond with better ways to value creative work" and "support public datasets." "New copyright fundamentalism" is Kirschenbaum and Raley's phrase, which S04 quotes (p. 4).
- **What's wrong:** A dropped qualification and a missing attribution. S04 accepts that creative work needs to be valued, which narrows the disagreement with S02's "fairly compensated" (S02 p. 11).
- **Proposed change:** Add the qualification and attribute the phrase.

**C17.** P10: S04 says defining "better" is "a genuine intellectual task."
- **Source:** S04 p. 3: "As Kirschenbaum and Raley suggest, to define 'better' … is a genuine intellectual task."
- **Proposed change:** Attribute the point to Kirschenbaum and Raley, as quoted by S04.

**C18.** P18: "LLMs as empirical confirmation of theory" is listed as something only S04 offers.
- **Source:** S04 p. 3 presents this as Ted Underwood's argument. Perlow's own move is the sentence that follows, about subjectivity.
- **Proposed change:** Write "S04's uptake of Underwood's argument …".

**C19.** P02: S03 says institutions should recognize "AI research happens across the humanities."
- **Source:** S03 p. 17 says research occurs "across campus, including in writing programs, libraries, and language departments … not the sole domain of STEM fields." Its most direct claim about the humanities, in the passage cited in C01, is missing from P02.
- **Proposed change:** Quote S03's own wording, and add p. 17.

**C20.** P04: S03 defines literacy "as critical, rhetorical and ethical judgment (pp. 5, 21 n1)."
- **Source:** Note 1 (p. 21) lists "functional, rhetorical, and critical literacies." Ethics comes from p. 5 ("question the ethics").
- **Proposed change:** Cite the two sources of the wording separately, and add "functional."

**C21.** Page errors in S03 citations:
- P16: "labor frameworks" is on p. 10, not p. 9.
- P17: the caution on AI in hiring and admissions is on pp. 18–19; p. 20 is efficiency.
- **Proposed change:** Correct the pages.

**C22.** P01: "S03 and S04 do not address this question directly."
- **Source:** S03 p. 17 speaks of "ethics and integrity in the conceptual and developmental phases of these technologies." S03 p. 5 says systems "inevitably reproduce the biases or gaps" in their training data.
- **What's wrong:** This is a borderline case. S03 touches the question of design values but does not argue it.
- **Proposed change:** Add a sentence recording S03 p. 17 as a brief statement that was considered and not joined, rather than "not addressed."

## Claims about a whole article read in part

None. All four notes say every page was read. The synthesis makes no claim about a whole article that rests on a partial reading.

## What I checked, and what I couldn't

**Checked against the PDFs:**
- S04: the full text, pp. 1–5.
- S03: the full text, pp. 1–23.
- S01: pp. 1–16, the body and conclusion.
- S02: pp. 1–15, the body and conclusion, plus refs. [13], [17], [20], [105]–[107], [188] and [189].
- The author-link claims: I searched S01 and S03 for Klein, Perlow, Kirschenbaum, Raley and MLA, and S02 for every citation of [20].
- The set-wide search for "agentic" and "AI agent."
- Page numbers, using the page breaks in the PDF text.

**Not checked:**
- The figures and tables (S01 Fig. 1, Fig. 2 and Tables 1–2; S02 Table 1). Their text came through garbled, so the cell-level content is unverified, though the Table 1 next steps I could read matched.
- The reference lists beyond spot checks (S01 pp. 16–23, S02 pp. 16–24).
- Whether S02 ref. [106] is the same essay as S04's "prompt for this PMLA special feature." Both are in *PMLA* 139.3, but S04 doesn't name the essay's title.
- S02's v1 date; the sources.md details on searches, URLs and the byte-identical S04 file; the files in sample-pdfs/.

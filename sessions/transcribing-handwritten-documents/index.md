---
title: Transcribing Handwritten Documents
layout: base
position: 2
date: 2026-10-14
time: "12:00–12:50"
location: History Commons (MVH 1104)
kicker: Session 2 · October 14, 2026
summary: "Another task where you can check the work, because the page is right in front of you. We try AI on handwritten sources, compare its readings with the originals, and look closely at where it goes wrong."
note: "Bring a photo or scan of a handwritten document you'd like to read. No laptop? Just show up."
thumbnail: "/assets/images/weigel-scribe-1698.jpg"
header-image: "/assets/images/weigel-scribe-1698.jpg"
header-tier: section
header-filter: etching
header-position: center right
header-title: Transcribing Handwritten Documents
header-subtitle: "AI can now read many historical hands, and you can check every word it gives you against the page. Choose the tool by the script and the size of the job, and have a second model check the first."
header-caption: "Christoph Weigel, <i>Der Schreiber</i>, from <i>Abbildung der Gemein-Nützlichen Haupt-Stände</i>, Regensburg, 1698. National Library of Poland (Polona), public domain."
tags: [transcription, archives, research]
workshop_mode: true
redirect_from: /sessions/transcribing-handwritten-documents.html
---

{% include nav/scrollspy-toc.html %}

This page contains all the links from the presentation and supplementary information. You can also [view the presentation slides]({{ site.baseurl }}/sessions/transcribing-handwritten-documents/slides/).
{: .lead}

## Introduction
{: .step #introduction}

This presentation covers the use of [Transkribus](https://www.transkribus.org/), an AI-powered webapp for handwritten text recognition. But it also explains when to use a commercial large language model, such as Gemini or Claude, for transcribing handwritten documents.

<div class="keypoint" markdown="1">
In the last few years, several strong options have emerged for using AI to transcribe documents.
</div>

### Before you start

- **A photo or scan of a handwritten document** you'd like to read. No document? Use one the example in step 2.
- **A laptop**, if you have one. No laptop? Just show up.

<div class="reminder" markdown="1">
Use images you have permission to share, such as your own photos or the examples on this page, and check an archive's rules before you upload its images to a commercial AI service.
</div>

## 1. Choose the tool that's right for your project
{: .step #step-1}

Try Transkribus first because if it has a trained model for your script then this is the most accurate and cost-effective option. You also will have more data sovereignty with Transkribus versus commercial LLMs. For an excellent overall guide to options for automated text recognition (ATR), see the 2026 ebook by Michael Schonhardt et al, *Automated Text Recognition: Theory, Platforms, Best-Practices*, available at [UNM Libraries](https://unm.on.worldcat.org/oclc/1612800957).

<div class="keypoint" markdown="1">
Transkribus works best when there is already a trained model for your script.
</div>

When working with scripts that do not have pre-existing models in Transkribus, then a commercial AI chatbot might end up working very successfully for transcribing handwritten documents. As you evaluate outputs for non-Latinate scripts, beware of the legacy of colonially mediated training data. 

## 2. Try it on three kinds of handwriting
{: .step #step-2}

### Example 1: Drop an image into Transkribus

Find any image of a handwritten document and drag it to the window on Transkribus.

- **For transcribing documents one at a time, this might be ideal.** [Link to Transkribus](https://www.transkribus.org/)
- **For less common scripts, training your own model might be worth the time.** Model training on Transkribus works well for large batches of document images that have a lot of consistency.
- **Transkribus can handle complex layouts.** For example, if you have a large dataset of digitized government documents with consistent labels, Transkribus excels at producing transcriptions in an Excel document with each label as a column.
- **Nineteenth-century handwritten script usually works nicely on Transkribus.** For an example, try out a page from [William Andrew Mauney's Civil War diary](https://www.digitalnc.org/blog/civil-war-diary-added-to-digitalnc/).

### Example 2: Gothic secretarial hand, with Gemini and Claude

- **Automated transcription accuracy greatly increased when using one LLM to check the work of another.** In this example, which can be viewed on Jonathan Seyfried's [website](https://jonathanseyfried.net/htr-episodes), Claude checked the work of Gemini. Although far from perfect each time and not suitable for critical editions, the transcriptions were good enough to use for research purposes. 
- **The large language models (LLMs) have been shown to perform better than Transkribus.** [Mark Humphries](https://generativehistory.substack.com) provides the best resource for understanding the conditions in which LLMs outperform Transkribus.

### Example 3: A challenging classical Japanese document

- **The language, classical Japanese, and the multi-directional layout, presents a large transcription challenge.** The [full chat transcript](https://claude.ai/share/50647f1c-3dab-48ee-8d40-714c7ed36d39) and [a report](https://claude.ai/artifact/7yTFsYxL9KxUdtVcRKFDdP#ccdb996d-540e) from Claude are accessible with a login to Anthropic. Alternatively, here is are PDF copies of the [full chat transcript](sessions/transcribing-handwritten-documents/claude-fable-5.1-santa-fe-yosegaki-chat-transcript-sept30.pdf) and the [report](sessions/transcribing-handwritten-documents/claude-fable-5.1-transcription-notes-santa-fe-yosegaki.pdf).
- **Claude Fable 5.1 generated some transcription.** The transcription carried out by Anthropic's most capable model (as of October 2026) successfully identified many of the characters but also substituted a blank circle when it found the script unreadable. For some difficult-to-read parts of this document the AI refused to guess or confabulate. The LLM correctly identified the material as silk.

## 3. Process documents in batches
{: .step #step-3}

- **Batch processing in the LLMs require agentic AI.** [Jonathan Seyfried](https://jonathanseyfried.net/aca-csv-files) has tested this out with Gemini and Claude for digitized documents from the Archive of the Crown of Aragon. The initial testing of this process took place in March 2026 and since then the usage costs have increased dramatically.
- **Transkribus offers batch processing, but this often requires the purchase of usage credits.** At a price of about $110 per year, Transkribus is much less expensive for batch processing.



## 4. Read a state-of-the-field report written by Claude
{: .step #step-4}

*The following report was generated by Claude when prompted to generate a state of the field for HTR in October 2026. Here is the prompt, followed by what Claude generated.*

{% include prompt.html id="htr-state-of-field" %}

### Handwritten Text Recognition Tools: State of the Field, October 2026

October 10, 2026

### Summary

As of October 2026, no single tool is best: Gemini leads for zero-shot transcription of post-1700 English and other well-resourced hands, Transkribus leads as an end-to-end platform for Latin-script archives, and eScriptorium/kraken leads for non-Latin, right-to-left and medieval material that needs trained models.

- **Gemini (Google)** reached about 0.7% meaningful character error on 18th–19th-century English, comparable to a professional typist, at about one cent per page. It still normalizes spelling, slips on names and numbers, and fails unpredictably on medieval abbreviated Latin.
- **Claude (Anthropic)** is a clear second on English hands and the most useful cross-checking partner for Gemini. It is strong on dates and numbers in forms but weaker overall and sometimes declines very hard material.
- **ChatGPT (OpenAI)** trails on running handwriting but has the lowest hallucination rate on structured forms.
- **Transkribus** shipped Text Titan II in June 2026 (about 47% fewer character errors than its predecessor) and is adding LLM integration, NER and one-step table extraction. It remains the best choice for German Kurrent, Dutch and large institutional projects that need line-aligned, exportable output.
- **eScriptorium/kraken** added multilingual base models in August 2026 and remains the strongest option for Arabic, Hebrew, Syriac and medieval manuscripts, where fine-tuning on your own ground truth is still required.
- **The emerging best practice is hybrid:** a specialist model or a frontier LLM for the first pass, a second model family to flag disagreements, and a human reviewing only the flagged words.

### How to read the accuracy numbers

Error rates from different studies are not directly comparable, so treat every figure below as indicative of a tool on a particular test set, not as a universal ranking.

- **CER and WER.** Character Error Rate counts character edits needed to reach the ground truth; Word Error Rate counts whole words. WER is usually about double CER, because one wrong comma or letter spoils the whole word ([Humphries 2025](https://generativehistory.substack.com/p/gemini-3-solves-handwriting-recognition)).
- **What a CER means in practice.** Humphries estimates a 3% CER at roughly 3–4 errors per sentence (a rough draft), 1% at about one per sentence, and 0.5% at one or two characters per page (copy-editing territory).
- **Strict versus normalized scoring.** Many LLM "errors" are capitalization, punctuation or silently corrected spelling. Gemini 3 Pro scored 1.67% CER strict but 0.69% once those were excluded, on the same test.
- **Diplomatic versus expanded transcription.** For medieval material, whether ground truth keeps abbreviations or expands them changes scores dramatically. Off-the-shelf medieval models scored 29–47% CER on English plea rolls largely because of convention mismatch and script ([Zhang et al. 2026](https://arxiv.org/abs/2605.00977)).
- **Who built the benchmark.** Vendor benchmarks (Transkribus's 2,016-page internal set) reflect platform material; independent benchmarks often avoid public datasets because LLMs may have seen them in training ([Crosilla, Klic & Colavizza 2025](https://arxiv.org/abs/2503.15195)).
- **The kind of error matters as much as the rate.** An unreadable word sends you back to the manuscript; a fluent, grammatical but wrong word does not. LLMs and transformer HTR models make more of the second kind (see the LLM section).

### Transkribus

Transkribus remains the most complete HTR *platform*: it is the safest institutional choice for Latin-script archives, especially German Kurrent and large multi-hand collections, but it is no longer the clear accuracy leader on easy English hands.

**What changed in 2026.** On 25 June 2026 READ-COOP released [Text Titan II](https://blog.transkribus.org/en/introducing-text-titan-ii), a single multilingual "Super Model" for print and handwriting across Latin scripts, trained on more than 250 million words. On an internal 2,016-page benchmark (81% handwriting; 34% German, 13% English, 12% Dutch, 10% French) it cut CER by about 47% against Text Titan I and beat the older language-specific Super Models. READ-COOP still advises dedicated models for specialised scripts and hands. The [2026 roadmap](https://blog.transkribus.org/en/community-ai-the-transkribus-vision-for-2026) adds versioned Datasets, Projects, Named Entity Recognition, "Smart Extract" models (DAN/DONUT architectures that read a register and output a table in one step), and opt-in connections to commercial LLMs; a Gemini integration was demonstrated at the September 2026 [user conference](https://tuc.transkribus.org/programme/workshops/workshop-read-coop-1).

**Strengths**

- End-to-end workflow: layout analysis, line segmentation, tables and fields, a line-aligned editor, PAGE XML/ALTO export, and Transkribus Sites for publishing.
- Custom model training on your own ground truth, plus hundreds of public community models (Kurrent, Sütterlin, Neo-Latin, medieval Latin charters, Dutch, Scandinavian).
- Text stays mapped to image coordinates, which LLM chat transcription does not give you.
- EU-hosted, GDPR-compliant, run by a cooperative of archives and universities; external LLM use is opt-in.

**Weaknesses**

- Raw out-of-the-box accuracy on English trails frontier LLMs: Humphries reports about 8% CER / 20% WER for Transkribus on raw English documents, falling to around 3% CER once a model is fine-tuned on dozens of pages ([Humphries 2025](https://generativehistory.substack.com/p/gemini-3-solves-handwriting-recognition)).
- Independent tests are mixed: Crosilla et al. found LLMs matched Transkribus on English historical hands and beat it on modern and Italian hands, while Transkribus won on German and multilingual sets ([Crosilla, Klic & Colavizza 2025](https://arxiv.org/abs/2503.15195)).
- Cloud-only and credit-metered: 1 credit per page for text recognition. The free tier gives 50 credits a month; Text Titan II requires Scholar (€99/year, 900 credits) or Team (about €450/year, 1,500 credits, 5 seats); API jobs cost half ([pricing](https://www.transkribus.org/pricing)).
- Text Titan II covers Latin scripts only; non-Latin scripts still depend on community or custom models.
- Training good custom models still takes real ground-truth labour and some technical patience.

### eScriptorium and kraken

eScriptorium is the strongest choice for non-Latin and right-to-left scripts, for medieval manuscripts with open ground truth, and for anyone who needs to own, share and publish their models.

eScriptorium is the open-source web interface; [kraken](https://github.com/mittagessen/kraken) is the engine underneath. Kraken was designed with connected and right-to-left scripts in mind, which is why OpenITI adopted it for Arabic-script OCR and HTR ([OpenITI case study](https://arxiv.org/pdf/2402.10943); [UT Austin overview](https://texlibris.lib.utexas.edu/?p=12779)). The medieval Latin-script ecosystem around it is unusually rich: CATMuS Medieval offers more than 160,000 lines in 10 languages from the 8th to the 16th century under shared transcription guidelines ([CATMuS](https://chartes.psl.eu/recherche/centre-jean-mabillon/publications-des-chercheurs/catmus-medieval-multilingual-large-scale-cross-century-dataset-latin-script-handwritten)), and it underpins the [ICDAR 2026 competition on multilingual medieval HTR](https://zenodo.org/records/18270331).

**What changed in 2026.** Kraken 7.0 (April 2026) reworked training and inference, added GPU batching (about 80% faster even on CPU) and a plugin system for outside layout and recognition models. Kraken 7.1 (5 August 2026) added pretrained multilingual base models built on a PP-OCRv6 architecture and trained on essentially all openly available historical HTR/OCR data ([release notes](https://github.com/mittagessen/kraken/releases)). Reported CER for the medium base model ranges from about 1.6% on German and 2.1% on Catalan to 6.5% on Latin, 9.4% on Arabic and 12.3% on Russian; the developer warns that coverage outside Western European languages, Hebrew and Arabic is uneven.

**Strengths**

- Free and open source; models are portable files you can download, cite and share (HTR-United, Zenodo).
- Best-in-class handling of right-to-left, connected and diacritic-heavy scripts; a Heidelberg comparison found kraken handled diacritics and complex layouts better than Transkribus ([Heidelberg talk](https://backend.uni-heidelberg.de/de/dokumente/ocr-technologien-im-vergleich-von-handschriften-und-altdrucken-zu-datenbankenstrukturen-und-htr-0/download)).
- Strong fine-tuning results: for 8th-century Syriac Estrangelo, manually corrected segmentation in eScriptorium reached about 6% CER, versus 21.7% (Transkribus) and 28.1% (kraken) out of the box ([Benabdellah, March 2026](https://www.dhhumanist.org/volume/39/375/)).
- IIIF import, PAGE XML/ALTO export, and line-level image–text alignment suitable for editions.

**Weaknesses**

- You need an instance: self-hosting takes server and Linux skills, so most users depend on an institutional or national-infrastructure server ([Kansai University comparison](https://kansai-u.repo.nii.ac.jp/records/22599)).
- Less polished interface and documentation than Transkribus; no all-purpose "Super Model" equivalent for handwriting until the 7.1 base models, which still need fine-tuning.
- General medieval models still transfer poorly to new documentary hands: on Catalan notarial charters (13th–15th c., Latin with Catalan) and on English plea rolls, off-the-shelf CATMuS/TRIDIS models were "far from" usable until fine-tuned ([Coll Ardanuy et al., ICDAR 2025](https://dataverse.bsc.es/dataverse/computational_archival_history); [Zhang et al. 2026](https://arxiv.org/abs/2605.00977)).

### Other prominent HTR tools

Beyond the two big platforms, the field has split into national-archive pipelines, institutional document factories, crowdsourcing front-ends that now wrap LLMs, and specialist models for single traditions.

| Tool | Type | Best for | Main limitation |
| --- | --- | --- | --- |
| [Loghi](https://di.huc.knaw.nl/home-en.html) (KNAW Humanities Cluster / Nationaal Archief) | Open-source pipeline | Early modern Dutch at scale; the Voices project has transcribed 500,000+ colonial pages including VOC records and built an early modern Portuguese model ([DH2025 report](https://voices.iisg.nl/?p=239)) | Command-line tooling; needs GPU and technical staff |
| Riksarkivet models + HTRflow (Swedish National Archives) | Open-source TrOCR models and pipeline | Swedish and Nordic historical hands ([model card](https://huggingface.co/Riksarkivet/trocr-base-handwritten-hist-swe-2)) | Narrow language focus |
| [Arkindex / Callico](https://teklia.com/solutions/arkindex) (Teklia, Paris) | Open-source and proprietary; cloud or on-premise | Institutional mass processing: French census (SOCFACE), ICRC prisoner lists; Latin, old French, Arabic; now orchestrates LLMs too | Built for projects with budgets and staff, not individual scholars |
| OCR4all (Würzburg) | Open source | Early printed books; some manuscripts | Expert installation ([Kansai comparison](https://kansai-u.repo.nii.ac.jp/records/22599)) |
| [FromThePage](https://content.fromthepage.com/?p=3156) | Crowdsourcing platform | Volunteer correction of Gemini 3 "AI drafts" (added November 2025) | No text-to-image bounding boxes for LLM drafts |
| [Glyph Machina](https://arxiv.org/abs/2605.00977) | Specialist web portal | English plea rolls in abbreviated legal Latin (1272–1461): kraken segmentation, CNN-LSTM recognition, optional Gemini correction | Latin legal rolls only |
| [CHURRO](https://arxiv.org/pdf/2509.19768) (Stanford, EMNLP 2025) | Open-weight 3B vision-language model | Broad historical coverage: 155 corpora, 46 language clusters; beat Gemini 2.5 Pro on its benchmark at about 1/15 the cost | Trails 2026 frontier models on English; small-model errors |
| Calfa Vision | Commercial/academic | Arabic Maghribī and Armenian; under 5% error with about 10 transcribed pages ([Lucas et al.](https://arxiv.org/abs/2211.16147v1)) | Narrow script focus |
| miwo / RURI (CODH, Japan) | Free app and models | Japanese *kuzushiji*; LLM post-correction further cuts errors ([Clanuwat et al. 2024](https://ipsj.ixsq.nii.ac.jp/records/241512)) | Printed books better covered than documents |

Genealogy users should also know that FamilySearch and Ancestry now run their own AI transcription and full-text search over record images ([Language Hat](https://languagehat.com/ai-and-handwriting-recognition/)); these are useful for finding records but not for producing citable transcriptions.

### Multimodal LLMs: Gemini, ChatGPT, Claude and open-weight models

For clear-to-moderate English (and, increasingly, other major Western European) hands from roughly 1700 onward, Google's Gemini is now the most accurate zero-shot transcriber available, ahead of Claude and well ahead of ChatGPT; for medieval, heavily abbreviated or non-Latin scripts, no general LLM is yet reliable on its own.

The best-controlled comparison is [Mark Humphries and Lianne Leddy's](https://www-tandfonline-com.libproxy.unm.edu/doi/full/10.1080/01615440.2025.2500309) benchmark of 50 unseen English documents (10,000 words, 18th–19th centuries), each run ten times. Its numbers, below, are the reference point for the model-by-model notes that follow.


{% include images/figure.html
  image-width="90%"
  caption="Data from Humphries and Leddy re-formatted by Claude."
  alt-text="Table of data from Humprhies and Leddy."
  image-path="/sessions/transcribing-handwritten-documents/slides/images/humphries-and-leddy-claude-data.png"
%}



On this set, model choice matters more than anything else you can tune: ChatGPT's error rate was roughly ten times Gemini's, and cross-checking against a second model family cut Gemini's meaningful errors by about two-thirds.

### Gemini (Google)

- **Accuracy.** Gemini 3 Pro reached 1.67% CER / 4.42% WER strict, and 0.69% / 1.33% once capitalization and punctuation were excluded: about one early-career professional typist, with no hallucinated text in 100,000 transcribed words ([Humphries, Nov 2025](https://generativehistory.substack.com/p/gemini-3-solves-handwriting-recognition)). Gemini 3.5 Flash (May 2026) scored 2.99% / 1.28% CER (strict / modified), just behind 3 Pro and ahead of Claude ([Humphries reply, May 2026](https://generativehistory.substack.com/p/where-do-stochastic-parrots-go-when/comments)). Gemini 3.1 Pro also had the lowest free-text error rates among 17 models on messy handwritten medical forms ([Pather et al. 2026](https://arxiv.org/abs/2604.16504)).
- **Breadth.** Library staff testing 15 documents spanning 600 years ranked Gemini most accurate of four assistants ([UVA Library, 2026](https://library-drupal.internal.lib.virginia.edu/news/2026/gamechanger-can-ai-accurately-transcribe-primary-source-documents)). One practitioner reports that no other model matches it on Polish handwriting ([comment on Humphries, May 2026](https://generativehistory.substack.com/p/when-models-disagree-transcription)); another found it can read mid-20th-century Yiddish, though not yet at human level ([Generative Lives](https://generativelives.substack.com/p/mid-c20th-yiddish-htr)).
- **Cost and settings.** About US$0.01 per page via the API. Humphries got the best results at temperature 0, high media resolution and *minimal* thinking; the consumer Gemini app behaves differently from AI Studio/API.
- **Weaknesses.** 61% of its errors are "corrections" toward modern spelling, capitalization and punctuation; names and numbers are the next risk. On English plea rolls in abbreviated Latin, Gemini 3 Pro gave usable output on only 3 of 20 cases, returned nothing on 2 and hallucinated lines on 9 ([Zhang et al. 2026](https://arxiv.org/abs/2605.00977)). Users also report skipped lines and weak handling of marginalia, and preview models are retired without notice (3 Pro Preview has already been withdrawn).

### Claude (Anthropic)

- **Accuracy.** Claude 3.5 Sonnet was the best zero-shot model in Crosilla et al.'s four-language benchmark. On Humphries's set, Claude Opus 4.5 scored 4.28% / 2.53% CER (strict / modified): a large jump from Sonnet 3.7 (10.45% / 7.47%) but well behind Gemini 3. Opus 4.7 is now used as a cross-checking model alongside Gemini because its errors fall in different places ([Humphries, May 2026](https://generativehistory.substack.com/p/when-models-disagree-transcription)).
- **Strengths.** Claude Sonnet 4.6 had the best character-level accuracy on synthetic forms and the best accuracy on dates and numbers in real ones ([Pather et al.](https://arxiv.org/abs/2604.16504)); in 18th-century Russian print, older Claude models inserted fewer anachronistic letters than GPT or Gemini ([Levchenko 2025](https://arxiv.org/abs/2510.06743)). It is in production use for 18th-century American records ([Papers of the War Department](https://wardepartmentpapers.org/transcription-methodology/)).
- **Weaknesses.** Overall accuracy on messy real-world forms was about 10 points behind Gemini and GPT, and very large images were rejected. Claude Sonnet 4.5 declined to attempt medieval plea rolls, and a March 2026 Syriac assessment judged GPT and Claude unsuitable because of invented content ([Benabdellah](https://www.dhhumanist.org/volume/39/375/)). Published tests of the newest Claude models on historical handwriting are still sparse.

### ChatGPT (OpenAI)

- **Accuracy.** GPT-4o was the first model that could read historical documents at all, but OpenAI has lagged since: on Humphries's set its late-2025 model scored 16.81% CER / 23.51% WER strict. GPT-5.1 refused or hallucinated on medieval plea rolls in December 2025.
- **Strengths.** On handwritten forms, GPT-5.4 was a close second to Gemini 3.1 Pro overall, had the lowest hallucination rate (6%) and was best on messy dates ([Pather et al.](https://arxiv.org/abs/2604.16504)). That makes it a reasonable choice for structured records (registers, census-style tables) more than for running prose.
- **Weaknesses.** GPT-4o "over-historicized" 18th-century Russian, inserting pre-Petrine letters in 59% of files ([Levchenko](https://arxiv.org/abs/2510.06743)); a customized GPT-4o misread 12% of dates, 27% of names and 36% of places in a 1930s register ([Taylor & Fillmore blog](https://edspace.american.edu/taylorandfillmore/gemini-as-transcriber-artificial-intelligence-and-documentary-editing/)).

### Open-weight vision-language models

Open models matter for privacy, cost and longevity, because closed models change or disappear. Fine-tuned small models are competitive on their target material: CHURRO (3B) beat Gemini 2.5 Pro on a 46-language historical benchmark ([Stanford, EMNLP 2025](https://arxiv.org/pdf/2509.19768)), and fine-tuned Qwen2.5-VL reached about 8% CER on handwritten classical Chinese in the EvaHan 2026 shared task ([LT4HALA 2026](https://aclanthology.org/2026.lt4hala-1.30/)). Out of the box, however, small open models trail frontier ones badly on difficult hands.

### Failure modes common to all LLMs

- **Fluent wrong readings.** A semantically plausible wrong word gives no signal that it is wrong. On one plea-roll case, Gemini correction cut errors from 24 to 10, but in the four lines examined closely three of its four remaining errors were misleading, including one where the raw HTR model had been right ([Zhang et al.](https://arxiv.org/abs/2605.00977)).
- **Normalization.** Models silently modernize spelling and expand or "fix" abbreviations unless told otherwise, and sometimes even when told.
- **Self-correction no longer helps.** Feeding one frontier model's transcription to another for correction now introduces about as many errors as it fixes ([Humphries, May 2026](https://generativehistory.substack.com/p/when-models-disagree-transcription); [Levchenko](https://arxiv.org/abs/2510.06743)).
- **No coordinates.** Chat transcription does not tie each word to its place on the image, which editions, search interfaces and crowdsourcing tools need.
- **Data governance.** Sending archival images to commercial APIs may conflict with archive licences or privacy rules.

### What is new since October 2025

The year's biggest shift is that general LLMs crossed expert-human accuracy on English hands, and the specialist platforms responded by shipping stronger general models and wiring LLMs into their workflows.

| Date | Development | Why it matters |
| --- | --- | --- |
| Sept 2026 | Transkribus User Conference (Passau) demonstrates NER, Smart Extract, Datasets, Projects and a [Gemini integration](https://tuc.transkribus.org/programme/workshops/workshop-read-coop-1) | LLM reading inside a line-aligned, exportable platform |
| 5 Aug 2026 | [kraken 7.1](https://github.com/mittagessen/kraken/releases) multilingual base models covering 40+ languages and scripts | First broad open "starter" model to fine-tune from |
| 25 Jun 2026 | [Text Titan II](https://blog.transkribus.org/en/introducing-text-titan-ii) | About 47% lower CER than Text Titan I on Latin-script material |
| 8 Jun 2026 | [MUDIDI benchmark](https://www.emergentmind.com/papers/2606.09435) of scanned multilingual dictionaries | LLMs beat conventional OCR across most writing systems, including Syriac and Georgian |
| 27 May 2026 | [Cross-model verification and ArchivePearl](https://generativehistory.substack.com/p/when-models-disagree-transcription) | Flags 76% of remaining errors for human review of only 4% of the text |
| May 2026 | Gemini 3.5 Flash; [Glyph Machina](https://arxiv.org/abs/2605.00977) for English plea rolls; [EvaHan 2026](https://aclanthology.org/2026.lt4hala-1.30/) classical Chinese task | Cheap near-top LLM; specialist pipelines still win on abbreviated Latin and fine-tuned VLMs on Chinese |
| Apr 2026 | kraken 7.0; [GlotOCR Bench](https://www.alphaxiv.org/abs/2604.12978) (100+ scripts); [handwritten-forms benchmark](https://arxiv.org/abs/2604.16504) | GlotOCR finds every OCR/VLM model collapses on low-resource scripts and invents characters from familiar ones |
| Mar 2026 | [Syriac HTR assessment](https://www.dhhumanist.org/volume/39/375/) | Fine-tuned eScriptorium about 6% CER; LLMs judged unsuitable |
| 18 Feb 2026 | [Transkribus 2026 roadmap](https://blog.transkribus.org/en/community-ai-the-transkribus-vision-for-2026) | Opt-in LLMs, versioned datasets, one-step table extraction |
| Jan 2026 | [ICDAR 2026 multilingual medieval HTR competition](https://zenodo.org/records/18270331) dataset (CATMuS) | Shared benchmark for medieval Latin-script hands |
| Dec 2025 | [AMSMB model](https://dataverse.bsc.es/dataverse/computational_archival_history) for medieval Catalan notarial charters | Fine-tuned TRIDIS model for Latin/Catalan documentary hands |
| Nov 2025 | Gemini 3 Pro released; [Humphries benchmark](https://generativehistory.substack.com/p/gemini-3-solves-handwriting-recognition); [FromThePage](https://content.fromthepage.com/?p=3156) adds Gemini drafts | Zero-shot LLM HTR reaches expert-typist accuracy on English |

No Reddit thread met the bar of academic discussion in my searches; the most substantive practitioner debate is in the comment threads of Humphries's *Generative History* posts and on [Language Hat](https://languagehat.com/ai-and-handwriting-recognition/).

### Best tools by script and language
*Generated by Claude as part of its report of October 10, 2026*

The older, more abbreviated, more non-Latin or more structured the material, the more the advantage shifts from general LLMs back to trained specialist models.

| Material | Best first choice | Also strong | Use with caution |
| --- | --- | --- | --- |
| English handwriting, c. 1700–1950 | Gemini 3 Pro / 3.5 Flash via API, cross-checked with Claude Opus | Claude Opus 4.x; Transkribus Text Titan II when you need line-aligned output | ChatGPT for running prose |
| English secretary hand, 16th–17th c. | Test Gemini against a Transkribus model on 5–10 pages | Fine-tuned Transkribus or kraken model | Any single zero-shot result (little published evidence) |
| German Kurrent and Sütterlin; Dutch; Scandinavian | Transkribus (Text Titan II, Kurrent models) | Loghi (Dutch at scale); Riksarkivet models (Swedish); Gemini on clear hands | LLMs on hard German hands, where Transkribus still wins |
| French, Italian, Spanish, Portuguese, Polish (early modern–modern) | Gemini on clear hands; Text Titan II for hard hands and volume | Loghi early modern Portuguese model; kraken 7.1 base models fine-tuned | Older Claude/GPT on non-English cursive |
| Medieval Latin book hands (Caroline, textualis) | eScriptorium with CATMuS models, fine-tuned | Transkribus medieval Latin models | Zero-shot LLMs, which expand or invent abbreviations |
| Medieval documentary hands (notarial, chancery, court) incl. Latin–Catalan charters | Fine-tuned specialist model (Glyph Machina; AMSMB; custom Transkribus/kraken) | LLM post-correction, compared against the raw output | Zero-shot LLMs: blanks and hallucinated lines |
| Greek (ancient, Byzantine) | Custom Transkribus or eScriptorium model | kraken 7.1 Ancient Greek base model (7.2% CER) as a fine-tuning start | LLMs on minuscule with ligatures |
| Cyrillic (Church Slavonic, Russian, Ukrainian) | Transkribus or eScriptorium generic Cyrillic models | Gemini for 18th–19th c. print and clear hands | LLM "over-historicization" (anachronistic letters) |
| Arabic, Persian, Ottoman, Urdu | eScriptorium/kraken (OpenITI ecosystem) | Calfa Vision (Maghribī) | LLMs on manuscripts |
| Hebrew, Yiddish, Syriac, Armenian, Ge'ez | eScriptorium/kraken, fine-tuned | Gemini as a draft for 20th-c. Yiddish | GPT/Claude on Syriac (invented text) |
| Classical Chinese; Japanese *kuzushiji* | Fine-tuned VLMs (Qwen2.5-VL); miwo/RURI with LLM correction | CHURRO | Zero-shot general LLMs |
| Registers, census forms, tables | Transkribus table/field models and Smart Extract; Arkindex | Gemini 3.1 Pro or GPT-5.4 with a fixed output schema | Free-text fields, where even the best model had 31% CER on medical forms |

### Recommendations
*Generated by Claude as part of its report of October 10, 2026*

Choose by testing on your own pages and by what the transcription is for, not by headline benchmarks.

1. **Pilot first.** Transcribe 5–10 representative pages by hand under your own conventions (diplomatic or expanded), then score two or three candidate tools against them. Published CERs rarely transfer to a new hand.
2. **Match the tool to the purpose.** For discovery and full-text search, a zero-shot LLM draft is often enough. For editions, quotation or data extraction, you need line-aligned output, a documented model and human review.
3. **Run LLMs as research instruments.** Use the API or AI Studio rather than consumer chat apps; set temperature to 0, image resolution high and thinking low; tell the model to keep original spelling, capitalization and abbreviations; and record the exact model version, date and prompt.
4. **Verify by disagreement.** Run two model families (for example Gemini plus Claude) and review only where they differ, as Humphries's ArchivePearl workflow does.
5. **Keep the raw output.** Never replace a specialist HTR transcription with an LLM "corrected" one without keeping both: corrections can turn visible errors into invisible ones.
6. **For medieval, non-Latin and low-resource scripts, invest in ground truth.** Start from Text Titan II, CATMuS or the kraken 7.1 base models and fine-tune; share the ground truth (HTR-United, Zenodo) so the next project starts further ahead.
7. **Manage platform risk.** Export PAGE XML or ALTO, keep an open-source fallback, and check archive licences and privacy rules before sending images to commercial APIs.

### Sources

**Scholarly articles, proceedings and preprints**
*Generated by Claude as part of its report of October 10, 2026*

- Crosilla, G., Klic, L. & Colavizza, G. (2025). "Benchmarking large language models for handwritten text recognition." *Journal of Documentation* 81(7). [Emerald](https://www.emerald.com/jd/article/81/7/334/1275080/Benchmarking-large-language-models-for-handwritten) · [arXiv](https://arxiv.org/abs/2503.15195)
- Humphries, M., Leddy, L. C. et al. (2024–25). "Unlocking the Archives." [arXiv 2411.03340](https://arxiv.org/abs/2411.03340v1); published version in *Historical Methods* ([Taylor & Francis](https://www.tandfonline.com/doi/abs/10.1080/01615440.2025.2500309))
- Zhang, M., Wang, E., Whatley, C., Strickland, S. & Bannon, D. (2026). "Democratizing the medieval English legal tradition." [arXiv 2605.00977](https://arxiv.org/abs/2605.00977)
- Pather, N., Fouché, J. et al. (2026). "From Handwriting to Structured Data: Benchmarking AI Digitisation of Handwritten Forms." [arXiv 2604.16504](https://arxiv.org/abs/2604.16504)
- Levchenko, M. (2025). "Evaluating LLMs for Historical Document OCR." [arXiv 2510.06743](https://arxiv.org/abs/2510.06743)
- Clérice, T. et al. (2024). "CATMuS Medieval." ICDAR 2024. [École des chartes](https://chartes.psl.eu/recherche/centre-jean-mabillon/publications-des-chercheurs/catmus-medieval-multilingual-large-scale-cross-century-dataset-latin-script-handwritten)
- Coll Ardanuy, M., Berganzo-Besga, I., Sarobe, R. & Cuadrada, C. (2025). "Evaluating HTR in Medieval Notarial Manuscripts." ICDAR 2025; dataset and model on [BSC Dataverse](https://dataverse.bsc.es/dataverse/computational_archival_history)
- CHURRO: open-weight VLM for historical text recognition (EMNLP 2025). [arXiv 2509.19768](https://arxiv.org/pdf/2509.19768)
- GlotOCR Bench (2026). [arXiv 2604.12978](https://www.alphaxiv.org/abs/2604.12978)
- MUDIDI multilingual dictionary benchmark (2026). [arXiv 2606.09435](https://www.emergentmind.com/papers/2606.09435)
- Xia, T. et al. (2026). LVLM optimization for ancient Chinese, LT4HALA @ LREC 2026. [ACL Anthology](https://aclanthology.org/2026.lt4hala-1.30/)
- OpenITI team. "Advances and Limitations in Open Source Arabic-Script OCR." [arXiv 2402.10943](https://arxiv.org/pdf/2402.10943)
- Lucas, N. et al. "New Results for the Text Recognition of Arabic Maghribī Manuscripts." [arXiv 2211.16147](https://arxiv.org/abs/2211.16147v1)
- Clanuwat, T. et al. (2024). "Beyond OCR: Enhancing Classical Japanese Transcription with LLMs." [IPSJ](https://ipsj.ixsq.nii.ac.jp/records/241512)
- Comparison of Transkribus, eScriptorium/Kraken and OCR4all. [Kansai University repository](https://kansai-u.repo.nii.ac.jp/records/22599)

**Blogs, Substack posts and practitioner reports**
*Generated by Claude as part of its report of October 10, 2026*

- Humphries, M. *Generative History*: ["Gemini 3 Solves Handwriting Recognition"](https://generativehistory.substack.com/p/gemini-3-solves-handwriting-recognition) (25 Nov 2025); ["When Models Disagree"](https://generativehistory.substack.com/p/when-models-disagree-transcription) (27 May 2026); [Gemini 3.5 Flash results in comments](https://generativehistory.substack.com/p/where-do-stochastic-parrots-go-when/comments) (May 2026)
- Transkribus blog: [2026 vision](https://blog.transkribus.org/en/community-ai-the-transkribus-vision-for-2026) (18 Feb 2026); [Text Titan II](https://blog.transkribus.org/en/introducing-text-titan-ii) (25 Jun 2026); [pricing](https://www.transkribus.org/pricing); [TUC 2026 workshop](https://tuc.transkribus.org/programme/workshops/workshop-read-coop-1)
- Kiessling, B. [kraken release notes 7.0–7.1](https://github.com/mittagessen/kraken/releases) (Apr–Aug 2026)
- Benabdellah, M. H. "HTR for Syriac manuscripts" (Mar 2026), via [Humanist 39.375](https://www.dhhumanist.org/volume/39/375/)
- ["Gemini as Transcriber?"](https://edspace.american.edu/taylorandfillmore/gemini-as-transcriber-artificial-intelligence-and-documentary-editing/), Papers of Zachary Taylor and Millard Fillmore blog (2026)
- ["Gamechanger: Can AI accurately transcribe primary source documents?"](https://library-drupal.internal.lib.virginia.edu/news/2026/gamechanger-can-ai-accurately-transcribe-primary-source-documents), UVA Library (2026)
- ["Mid-C20th Yiddish HTR"](https://generativelives.substack.com/p/mid-c20th-yiddish-htr), *Generative Lives* Substack
- ["Introducing Gemini 3.0 Support in FromThePage"](https://content.fromthepage.com/?p=3156), FromThePage blog
- ["AI and Handwriting Recognition"](https://languagehat.com/ai-and-handwriting-recognition/), Language Hat
- [Voices project DH2025 report on Loghi](https://voices.iisg.nl/?p=239); [KNAW Humanities Cluster](https://di.huc.knaw.nl/home-en.html)
- [Riksarkivet TrOCR model card](https://huggingface.co/Riksarkivet/trocr-base-handwritten-hist-swe-2); [Teklia Arkindex](https://teklia.com/solutions/arkindex)
- [Papers of the War Department transcription methodology](https://wardepartmentpapers.org/transcription-methodology/)
- [Transkribus vs eScriptorium/kraken](https://backend.uni-heidelberg.de/de/dokumente/ocr-technologien-im-vergleich-von-handschriften-und-altdrucken-zu-datenbankenstrukturen-und-htr-0/download), Heidelberg Forum Digital Humanities talk; [eScriptorium for non-Roman scripts](https://texlibris.lib.utexas.edu/?p=12779), UT Austin TexLibris
- [ICDAR 2026 Multilingual Medieval HTR competition data](https://zenodo.org/records/18270331), Zenodo

## What to take with you
{: .step #takeaways}

<div class="takeaways" markdown="1">
Use these on the next handwritten source you need to read, whether it is one letter or a whole collection.

- **Try Transkribus first if your script has a model.** It is the most accurate and cost-effective option there, and your images stay out of commercial chatbots.
- **Pilot before you commit.** Run around ten representative pages through each tool you are considering, and compare what comes back with the page.
- **Have a second model check the first.** Paste one model's transcription into another and ask it to revise, then read the two against each other where they differ.
- **Budget for verification.** Checking takes real time, and image recognition uses up credits quickly.
- **Treat batch output as a draft.** Batching changes how many pages you can process, not how accurate each one is, so every row still needs checking.
</div>

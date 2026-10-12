---
layout: reveal-workshop
title: Transcribing Handwritten Documents with AI
summary: "A 45-minute workshop on using AI to transcribe handwritten documents."
permalink: /presents/transcribing-handwritten-documents/
tutorial: /sessions/transcribing-handwritten-documents
---

{::options parse_block_html="true" auto_ids="false" /}

<!-- 11 slides, 19 minutes so far. The matching full tutorial lives
     at sessions/transcribing-handwritten-documents.md. Sources and timing are in each note.
     Response labels distinguish illustrations from saved excerpts; provenance is in the notes. -->


<!-- 01 -->
<section id="title" class="workshop-title" data-timing="60" aria-label="Using AI to Transcribe Handwritten Documents">

<header>

Amaranth Brown Bag Series
{: .deck-topic}

# Using AI to Transcribe Handwritten Documents

Tips and Recommendations
{: .deck-thesis}

</header>

<div class="deck-summary">

- Choose your tool based on your project needs
- Use one LLM to check the work of another
- Preview of agentic processing

</div>

<div class="deck-decoration" markdown="0"><img class="deck-art" src="{{ '/assets/images/amman-typefounder-1568.jpg' | relative_url }}" alt="" aria-hidden="true"></div>

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**0:00–1:00**

Welcome. Summarize the session goals.

Cover image: Jost Amman, typefounder, 1568. Existing public-domain workshop image. The Rubric theme and typography follow the Reliable AI site.

</aside>
</section>

<!-- 02 -->
<section id="active-scholars" class="workshop-summary" data-timing="90" aria-label="Scholars already working on AI transcription">

<header>

Existing scholarship on HTR and AI
{: .deck-topic}

## Several scholars are already working on this

</header>

<div class="deck-summary">

- &#9642; For the general Digital Humanities response to AI for transcription, a 2026 monograph by  David Joseph Wrisely and Estelle Guéville, *Medieval Manuscripts and the Computational Humanities*, ebook at [UNM Libraries](https://unm.on.worldcat.org/oclc/1590924317)
- &#9642; For a easy-to-understand guide to all the options for Automated Text Recognition (ATR), see the ebook by Michael Schonhardt et al, *Automated Text Recognition : Theory, Platforms, Best-Practices*, available at [UNM Libraries](https://unm.on.worldcat.org/oclc/1612800957)
- &#9642; For studies that compare LLMs' transcription accuracy to Transkribus, see Mark Humphries, [generativehistory.substack.com](https://generativehistory.substack.com)
- &#9642; For examples of full chats when using AI for transcribing handwriting, see Jonathan Seyfried,[jonathanseyfried.net](https://jonathanseyfried.net/htr-episodes)

</div>

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**1:00–2:30**

See the 'Sources' section of the workshop webpage for a more extensive list of scholarship.

</aside>
</section>

<!-- 03 -->
<section id="choosing-the-tool" class="workshop-summary" data-timing="120" aria-label="Four criteria for choosing a transcription tool">

<header>

Choosing the right tool
{: .deck-topic}

## Match the tool to the needs of the project

</header>

<div class="deck-summary">

- &#9642; First, the language, age, rarity, and style of the handwriting.
- &#9642; Second, the quality of the scan or photo, and its layout.
- &#9642; Third, the number of documents you need transcribed.
- &#9642; Fourth, the budget, time, and tech comfort you can bring to the project.

</div>

Then choose around 10 document images for a pilot test
{: .deck-question}

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**2:30–4:30**

Walk the list in order on purpose: script constraints come first because they decide whether a tool can read the document at all, no matter how much time or budget you throw at it. Everything after that is a tradeoff a project can actually make. A one-off family letter and a thousand-page institutional archive call for different tools even if the handwriting is identical. Also, beware that scholars have observed training data for some scripts as colonially-mediated, for example David Joseph Wrisley noticed that Transkribus had a very colonially-mediated training set for Arabic script.

</aside>
</section>

<!-- 04 -->
<section id="demo-transkribus" class="workshop-summary" data-timing="120" aria-label="Live demo: dropping an image into Transkribus">

<header>

Choosing the right tool
{: .deck-topic}

## Try Transkribus live

</header>

<div class="deck-summary">

[transkribus.org](https://www.transkribus.org/){: target="_blank" rel="noopener"}
{: .deck-url}

- Choose a single image of a handwritten document with text in horizontal lines
- Drag the image into the box on the Transkribus home page
- Watch how it performs, with no additional setup required

</div>

Drag in an image and see what comes back.
{: .deck-question}

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**4:30–6:30**

Do this live rather than describing it. Transkribus's home page accepts a dropped image and runs its general model with no account setup, so the room can watch an untrained first pass happen in real time. Pick a document with plain horizontal lines for this first try; harder layouts come later. Transkribus uses PyLaia to interact with a LLM. When doing HTR, PyLaia functions as the eyes and the LLM as the brain.

</aside>
</section>

<!-- 05 -->
<section id="debrief-the-demo" class="workshop-summary" data-timing="90" aria-label="Coverage varies wildly by script">

<header>

Choosing the right tool
{: .deck-topic}

## The usefulness of Transkribus depends on the script

</header>

<div class="deck-summary">

If you have a document in Precalit Sanskrit or Old Nubian, you're in luck! Someone else has created models for those.

For a Catalan document in late fourteenth-century Gothic Secretarial Hand, you are not lucky.

That said, a lot of scripts have existing models; almost all Latinate scripts from the nineteenth century will work on Transkribus.

</div>

Transkribus can be trained for a variety of [layouts](https://www.transkribus.org/document-layout-analysis)
{: .deck-question}

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**6:30–8:00**

Coverage on Transkribus is a function of who has already trained a model on that script, not of how hard the script is to read. Rare doesn't mean uncovered — a handful of specialists have built models for scripts you'd assume nobody touched — and common doesn't guarantee coverage either, if the specific hand or period falls between existing models. Click on 'layouts' to explain what is meant by that term on Transkribus.

</aside>
</section>

<!-- 06 -->
<section id="llms" class="workshop-summary" data-timing="120" aria-label="A commercial LLM as the alternative to training a model">

<header>

Commercial LLMs
{: .deck-topic}


</header>

<div class="deck-summary deck-summary-row">

<div class="deck-summary-text">

If you have a script that is not yet available on Transkribus, you can train a new model

However, training a Transkribus model might not be worth the time, so instead you can try a commercial large language model

Generally, the AI chatbots will also work for Latinate scripts after 1900

</div>

<figure class="deck-figure" markdown="0">
<img src="{{ '/assets/images/humphries-and-leddy-claude-data.png' | relative_url }}" alt="Table comparing transcription error rates for Gemini, Claude, and ChatGPT.">
<figcaption>Humphries and Leddy's error-rate comparison, reformatted by Claude</figcaption>
</figure>

</div>

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**8:00–10:00**

Training is the right call for a standing collection that will keep producing pages in the same hand. For a one-off batch, it's usually faster to point a frontier chatbot at the images directly. The comparison data here is Mark Humphries's, reformatted by Claude rather than copied as a screenshot.

</aside>
</section>

<!-- 07 -->

<section class="image-slide bleed"
 data-background-image="assets/images/humphries-and-leddy-claude-data.png"
 data-background-size="contain"
 data-background-color="#0d1412" markdown="1">


Table comparing transcription error rates for Gemini, Claude, and ChatGPT.
{: .bleed-alt}

</section>

<!-- 08 -->

<section class="image-slide bleed"
 data-background-image="assets/images/japanese-santa-fe-signatures.jpg"
 data-background-size="contain"
 data-background-color="#0d1412" markdown="1">


Table comparing transcription error rates for Gemini, Claude, and ChatGPT.
{: .bleed-alt}

</section>


<!-- 09 -->
<section id="japanese-example" class="workshop-summary" data-timing="60" aria-label="A striking LLM transcription of classical Japanese handwriting">

<header>

An example using Claude Fable 5.1
{: .deck-topic}

## An unexpected success

</header>

<div class="deck-summary">

Sometimes the LLM produces quite impressive results, as with this classical Japanese handwriting on a silk handkerchief from the 1940s.

<figure class="deck-figure" markdown="0">
<img src="{{ '/assets/images/japanese-santa-fe-signatures.jpg' | relative_url }}" alt="Photograph of classical Japanese handwriting on a silk handkerchief from the 1940s.">
<figcaption>Classical Japanese handwriting, silk handkerchief, 1940s</figcaption>
</figure>

</div>

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**10:00–11:00**

Don't expect every run to be this good, but don't assume a hard, unfamiliar script is automatically out of reach either.

</aside>
</section>

<!-- 10 -->
<section id="llm-checking" class="workshop-example" data-timing="150" aria-label="Using a second model to check the first transcription">

<header>

Checking the transcription
{: .deck-topic}

## Have a second model check the first

</header>

<div class="deck-pair">

<div class="prompt" markdown="0">
  <div class="prompt-head">
    <p class="deck-label">Prompt for the second LLM</p>
    <button class="prompt-copy" type="button" data-prompt-copy aria-label="Copy the displayed prompt"><span class="prompt-copy-text">Copy</span></button>
  </div>
  <pre class="prompt-text"><code>I am going to paste a transcription of the same image done by another LLM. Please look it over and use it to consider parts of the transcription that were ambiguous or difficult for you. Then make adjustments to your transcription and provide it again in full. Here is the transcription...</code></pre>
</div>

<div class="deck-response fragment" data-fragment-index="0">

Current recommendation
{: .deck-label}

<div markdown="0">
<dl class="example-lines">
  <dt>Use Gemini as the first LLM</dt>
  <dd>Gemini currently leads in performance for image recognition.</dd>
  <dt>Prompt Gemini</dt>
  <dd>Upload the image file and specify the year and the script</dd>
  <dt>Then go to Claude</dt>
  <dd>Paste Gemini's output into a prompt for Claude</dd>
</dl>
</div>

</div>
</div>

It will take some time to check the end result for each document
{: .deck-question .fragment data-fragment-index="0"}

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**11:00–13:30**

Sometimes, this only works as a check if you actually read the two transcriptions against each other, not just accept whichever one finishes second. Other times, I found that the output from Claude was obviously superior with so much of the text that it wasn't worth the time to check to see if Gemini had done better. I also prompted Claude to explain when it overrode Gemini in a significant way.

### Sample checking prompt

```text
I am going to paste a transcription of the same image done by another LLM. Please look it over and use it to consider parts of the transcription that were ambiguous or difficult for you. Then make adjustments to your transcription and provide it again in full. Here is the transcription...
```

</aside>
</section>

<!-- 11 -->
<section id="agents" class="workshop-summary" data-timing="120" aria-label="What agentic AI means and why it's safer now">

<header>

Agentic AI
{: .deck-topic}

## What agentic AI changes

</header>

<div class="deck-summary">

- Agentic AI means letting an AI application edit files directly on your computer
- OpenClaw, the first popular agentic AI app, contained significant security vulnerabilities
- Today's frontier agentic tools, such as Claude Cowork, are considerably safer
- The October 21 Reliable AI Brown Bag goes into agentic AI in more detail

</div>

<footer class="deck-source">

[Audit Trails for AI Agents]({{ site.baseurl }}/sessions/audit-trails-for-ai-agents)

</footer>

<aside class="notes">

**13:30–15:30**

Flag this as a change in kind, not just a faster chatbot: once an AI application can write to your filesystem, the security and review questions are different from anything else in this session. The next Brown Bag session is where those questions actually get worked through; here it's enough to know the category exists and that the safety picture has improved since the first wave of tools.

</aside>
</section>

<!-- 12 -->
<section id="example-of-aca-batching" class="workshop-summary" data-timing="120" aria-label="Batch transcription with agentic AI, Archive of the Crown of Aragon">

<header>

Agentic AI
{: .deck-topic}

## Batches instead of one by one

</header>

<div class="deck-summary">

- Agentic AI can transcribe a whole batch of images instead of you uploading them one at a time
- Tried on document images from the Archive of the Crown of Aragon, with varying levels of success
- Batch output can go straight into a CSV, ready to open in Excel or upload as a database on a website

</div>

Two examples of CSV files are available on Jonathan Seyfried's [website](https://jonathanseyfried.net/aca-csv-files)
{: .deck-question}

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**15:30–17:30**

"Varying levels of success" is doing real work in that sentence: batching changes the scale of the task, not the accuracy of any single transcription, so the same per-document checking from the last two slides still applies to every row in the resulting file.

</aside>
</section>

<!-- 13 -->
<section id="cautionary-notes" class="workshop-summary" data-timing="90" aria-label="What to expect before you start transcribing">

<header>

Cautionary notes
{: .deck-topic}

## Keep these points in mind going forward

</header>

<div class="deck-summary">

Image recognition drains usage credits quickly

There is a substantial time commitment for perfect transcriptions, increasingly viewed as a 'verification tax'

Consider the use of AI for transcription as more of an axe than a scalpel

At the same time, be ready for the AI to surprise you with moments of high accuracy

</div>


<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**17:30–19:00**

This will be an iterative process as you figure out which tool to use and how to organize your workflow.

</aside>
</section>

<!-- 14 -->
<section id="resources" class="workshop-summary" data-timing="60" aria-label="The webpage has more resources">

<header>

More resources for HTR using AI
{: .deck-topic}

## The webpage on the Reliable AI site contains more guidance and information

</header>

<div class="deck-summary">

[amaranth.unm.edu/reliable-ai]({{ '/' | relative_url }})
{: .deck-url}

- The presentation slides
- Links to all the examples covered in the presentation
- A report on 2026 HTR developments generated by Claude
- Citations of current scholarship


</div>

<div class="deck-question" aria-hidden="true" markdown="0"></div>

<footer class="deck-source" aria-hidden="true"></footer>

<aside class="notes">

**43:00–44:00**

Conclusion

</aside>
</section>
---
title: Audit a CV before editing it
layout: base
header-image: "/assets/images/amman-typefounder-1568.jpg"
header-filter: etching
header-tier: banner
header-title: Audit a CV before editing it
summary: "Ask AI to audit a fictional four-page CV in Word, then sort its findings into formatting fixes and questions only the author can answer."
permalink: /examples/cv-audit/
---

A CV can look finished and still be inconsistent in ways that matter the next time you edit it. Have AI audit one before changing anything, then decide which findings are formatting fixes and which need the author.
{: .lead}

## The CV

[Download the workshop CV]({{ '/assets/documents/alexandra-ruiz-cv-workshop.docx' | relative_url }}) (Word, four pages). It expands the fictional [Alexandra Ruiz sample CV](https://xanthan-web.github.io/alexandra-ruiz/cv) with invented publications, positions, and institutions. It is practice material, not a record of anyone's qualifications.

It is built to look ordinary at first glance. It contains small inconsistencies in the text and some older Word structures that you can't see on the page.

Before you run anything, read the first page yourself and note what you would ask its author. You'll want something to compare the tool's findings against.

## First pass: a broad audit

Attach the Word file to a fresh conversation.

{% include prompt.html id="cv-audit-first" %}

Here is a recorded reply:

{% include demo.html id="cv-audit-first-run" %}

Start with what it says it examined. This run read only the text Claude extracted from the file, and said so before anything else. That text still showed the table in the conference list and many of the inconsistencies, but not fonts, spacing, or Word's heading styles, so the reply marks anything about those as something to verify in Word. Then check two or three of its findings against the document yourself.

## Second pass: the Word structure

{% include prompt.html id="cv-audit-structure" %}

This prompt names the things to look for, so it is a guided check rather than a second independent audit. Keep its findings separate from what the first pass noticed on its own.

In the recorded run, Claude said it couldn't inspect the Word structure, listed the checks it couldn't do, and pointed to places worth verifying in Word. It also corrected two details of its own first reply.

<details markdown="1">
<summary>The recorded reply</summary>

{% include demo.html id="cv-audit-structure-run" %}

</details>

A structure isn't wrong just because it's unusual. A borderless table, for example, is a common way to line up text. The question is whether comparable entries behave differently when you edit them.

## Decide on rules

{% include prompt.html id="cv-audit-rules" %}

Approve the guide before anything changes. Formatting decisions are yours to make, but a conflict about a fact, such as a publication's status, needs the author's answer. When the new Word file comes back, open it and look at it as well as reading the change list.

The recorded guide keeps nine questions for the author apart from its formatting rules. It also says it hasn't confirmed it can edit the Word file with its styles intact, and offers a change list you could apply yourself.

<details markdown="1">
<summary>The recorded reply</summary>

{% include demo.html id="cv-audit-rules-run" %}

</details>

<details markdown="1">
<summary>Three findings to check yours against</summary>

These were confirmed in the document when it was built. They are not output from an AI run, and the CV contains more than these three. The recorded reply above found all three, though from the text alone it could tell only that the talks sit in a table, not that the table has no borders.

**A visible detail.** One date range uses a hyphen, while comparable ranges use en dashes. A formatting fix: make the ranges consistent without changing the dates.

**A hidden structure.** Only the oldest talks sit inside a borderless table. It looks the same as the rest of the list on the page, but those entries won't behave like their neighbors when you edit or restyle them.

**An author decision.** One article appears as both “Forthcoming” and “Article in preparation.” The tool shouldn't pick one. Only the author knows which is true.

Catching every small inconsistency matters less than noticing a conflict like the last one and leaving the decision with the author.

</details>

Return to the [style-guide step]({{ site.baseurl }}/sessions/editorial-assistant#step-5) or the [presentation]({{ site.baseurl }}/presents/editorial-assistant/#/cv-formatting).

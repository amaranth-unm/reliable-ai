---
title: A style guide that works across semesters
layout: base
header-image: "/assets/images/amman-typefounder-1568.jpg"
header-filter: etching
header-tier: banner
header-title: A style guide that works across semesters
summary: "Use the Campus History Essay Style Guide to normalize a collection while preserving student authorship."
permalink: /examples/campus-history-style-guide/
---

The Campus History Essay Style Guide carries the editor's decisions from one essay and semester to the next. It gives AI a defined scope for making a varied collection easier to read.
{: .lead}

## The actual guide

This example uses the [Campus History Essay Style Guide](https://github.com/amaranth-unm/campus-history/blob/master/ESSAY-STYLE-GUIDE.md), which accompanies the [UNM Campus History site](https://amaranth.unm.edu/campus-history/). The [workshop snapshot]({{ '/assets/documents/campus-history-essay-style-guide.txt' | relative_url }}) is a complete text copy from September 23, 2026, matching the public repository at the time of preparation.

Its scope is concrete:

- Normalize paragraph breaks, heading levels, citation presentation, captions, and recurring page elements.
- Make light prose edits when the meaning is clear, including removing unnecessary assignment scaffolding.
- Preserve student arguments, distinctive phrasing, meaningful first person, and uncertainty supported by the evidence.
- Flag missing sources, unclear claims, and changes that would alter interpretation.

This makes consistency a matter of shared editorial decisions. It does not require identical prose from every contributor.

## Try it on one essay

Attach the guide and an essay you have permission to share. Use a copy and inspect the proposed scope before editing a collection.

{% include prompt.html id="campus-history-normalize" %}

Compare the original and revised text, then inspect the page as a reader sees it. A clean-looking change can still alter a claim; a text-only check can miss a broken image or misplaced caption.

## A small illustration

The following sentence is invented for teaching; it is not taken from a student's essay or an AI transcript.

**Original:** In conclusion, the letters suggest that students may have used the room after hours.

**Proposed edit:** The letters suggest that students may have used the room after hours.

The guide permits removing unnecessary concluding scaffolding. It also gives a reason to keep “suggest” and “may have” when the historical record is incomplete. Whether this sentence makes a good conclusion would still depend on its surrounding paragraph.

For a more substantial change, ask for the rule and inspect the evidence. If a citation is incomplete, flag it. If a paragraph needs a new interpretation to become coherent, return it to the editor. Save corrections to the guide so the next essay benefits from what you learned.

## Check the guide too

A saved guide can accumulate inconsistencies. This snapshot refers to both `header-title` and `image-title` for an essay's displayed title; the current student publishing guide uses `header-title`. It also mixes an instruction to add an opening heading with the later rule that a lead paragraph should precede section headings. An assistant should surface such conflicts for the editor to resolve before applying changes across many essays.

The workshop preserves the source guide as a snapshot. The editorial example is a chance to make its boundaries visible and test them on one page.

Return to the [style-guide exercise]({{ site.baseurl }}/sessions/editorial-assistant#step-5) or [presentation]({{ site.baseurl }}/presents/editorial-assistant/#/campus-history-guide).

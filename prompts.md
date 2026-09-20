---
title: Prompt library
layout: base
header-image: "/assets/images/press.webp"
header-tier: banner
header-filter: etching
header-title: Prompt library
summary: "Every prompt from the series in one place, grouped by session and ready to copy."
---

Everything we've used, in one place. Copy, then change the parts in brackets — these are scaffolds, not incantations, and the specifics you add are what makes them work.
{: .lead}

A note on how to read these: none of them are magic words. Each one is a way of supplying information the tool doesn't have (what this is, who it's for, what counts as good) or of constraining what it's allowed to hand back. That's all prompting is.

## Session 1 — AI as Editorial Assistant

See the [full session]({{ site.baseurl }}/sessions/editorial-assistant) for what each of these is doing and why.

### Starting out

{% assign step1 = site.data.prompts | where: "session", "editorial-assistant" | where: "step", 1 %}
{% for p in step1 %}{% include prompt.html id=p.id %}{% endfor %}

### Teaching it to read like you do

{% assign step2 = site.data.prompts | where: "session", "editorial-assistant" | where: "step", 2 %}
{% for p in step2 %}{% include prompt.html id=p.id %}{% endfor %}

### Reader roles

{% assign step3 = site.data.prompts | where: "session", "editorial-assistant" | where: "step", 3 %}
{% for p in step3 %}{% include prompt.html id=p.id %}{% endfor %}

### Rules and style sheets

{% assign step4 = site.data.prompts | where: "session", "editorial-assistant" | where: "step", 4 %}
{% for p in step4 %}{% include prompt.html id=p.id %}{% endfor %}

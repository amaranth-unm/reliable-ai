---
title: Prompt library
layout: base
header-image: "/assets/images/press.webp"
header-tier: banner
header-filter: etching
header-title: Prompt library
summary: "Every prompt from the series in one place, grouped by session and ready to copy."
---

Every prompt from the series, grouped by session. Copy one, then fill in the parts in brackets. The details you add are what make a prompt work.
{: .lead}

None of these are magic words. Each one either gives the tool information it doesn't have (what the text is, who it's for, what counts as good) or limits what it's allowed to send back. That covers most of what prompting is.

## Session 1: AI as Editorial Assistant

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

### Making rules

{% assign step4 = site.data.prompts | where: "session", "editorial-assistant" | where: "step", 4 %}
{% for p in step4 %}{% include prompt.html id=p.id %}{% endfor %}

### Rules and style sheets

{% assign step5 = site.data.prompts | where: "session", "editorial-assistant" | where: "step", 5 %}
{% for p in step5 %}{% include prompt.html id=p.id %}{% endfor %}

### Working in files

{% assign step6 = site.data.prompts | where: "session", "editorial-assistant" | where: "step", 6 %}
{% for p in step6 %}{% include prompt.html id=p.id %}{% endfor %}

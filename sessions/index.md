---
title: Sessions
layout: base
header-image: "/assets/images/stradanus-press-1600.jpg"
header-tier: section
header-filter: etching
header-position: center right
header-title: Sessions
header-subtitle: "A printing house around 1600: compositors set the type, a corrector reads the proof, pressmen work the press. The sessions divide the work the same way. The tool can help with the setting, but the proofreading is yours."
header-caption: "Jan van der Straet (Stradanus), <i>Impressio Librorum</i>, from <i>Nova Reperta</i>, engraved by Joannes Galle. Museum Plantin-Moretus, public domain." 
summary: "Every session in the Reliable AI for Humanists brown bag series, with the full materials from each."
---

Each session is about an hour of hands-on work: a short introduction, three or four exercises on your own writing, and a set of prompts to keep. The pages stay up afterwards, so you can repeat the exercises or catch up on a session you missed.
{: .lead}

{% assign session_pages = site.pages | where_exp: "p", "p.path contains 'sessions/'" | where_exp: "p", "p.path != 'sessions/index.md'" %}
{% include cards/card-toc.html rows=session_pages %}

## Coming up

{% comment %}
  Mirrors the lookup in index.md — see the comment there for why this can't
  be shared via an include.
{% endcomment %}
{% assign today = site.time | date: "%Y-%m-%d" %}
{% assign upcoming_sessions = "" | split: "," %}
{% for s in session_pages %}
  {% assign s_date = s.date | date: "%Y-%m-%d" %}
  {% if s_date > today %}
    {% assign upcoming_sessions = upcoming_sessions | push: s %}
  {% endif %}
{% endfor %}
{% assign upcoming_sessions = upcoming_sessions | sort: "date" %}
{% assign next_session = upcoming_sessions | first %}

{% if next_session %}
**Next: {{ next_session.title }}**, {{ next_session.date | date: "%A, %B %-d" }}{% if next_session.time %}, {{ next_session.time }}{% endif %}{% if next_session.location %}, {{ next_session.location }}{% endif %}.{% if next_session.note %} {{ next_session.note }}{% endif %}
{% endif %}

### Later this semester

{% include schedule-list.html %}

Later sessions take the same approach: try the tools on work you already know how to judge. Topics for the TBA dates are still being decided — some we're considering:

- **Reading and note-taking.** Ask AI about a text you know well, and see what that tells you about asking it about one you don't.
- **AI in the classroom.** Design assignments that assume students have these tools.
- **Research assistance and its limits.** Where fabricated citations come from, and habits that catch them.

Have a request? [Tell us](https://amaranth.unm.edu) and we'll add it to the list.

---
title: Sessions
layout: base
header-image: "/assets/images/stradanus-press-1600.jpg"
header-tier: section
header-filter: etching
header-position: center right
header-title: Sessions
header-subtitle: "A printing house around 1600: people at work, a boy watching, a man in a fur robe talking it over with the pressman. The sessions run the same way: watch, work along on your own laptop, or stop us to ask about anything, as often as you like."
header-caption: "Jan van der Straet (Stradanus), <i>Impressio Librorum</i>, from <i>Nova Reperta</i>, engraved by Joannes Galle. Museum Plantin-Moretus, public domain." 
summary: "Every session in the Reliable AI for Humanists brown bag series, with the full materials from each."
---

We work through a few exercises on screen and talk about what the tool is doing as we go. Follow along on your own laptop or just watch. Ask questions constantly or never say a word. Skeptics, critics, the curious and the enthusiastic all have a place here, and we're hoping to learn from each other.
{: .lead}

## What to bring

- **Lunch.** It's a brown bag series.
- **A laptop, if you want to follow along**, with Claude, ChatGPT, Gemini or Copilot open in a browser tab. A free account is enough. No laptop is fine; you can watch.
- **Something of your own to try it on.** Each session's page says what, such as a paragraph of your writing or a photo of a handwritten page. If you don't have anything suitable, use the [practice texts]({{ site.baseurl }}/practice-texts).
- **Nothing you shouldn't share.** Leave out other people's unpublished work, student writing with names attached, and anything under embargo or an IRB protocol.

{% comment %}
  Same next/past lookup as index.md. See the comment there for why it's
  repeated here instead of shared through an include.
{% endcomment %}
{% assign today = site.time | date: "%Y-%m-%d" %}
{% assign session_pages = site.pages | where_exp: "p", "p.path contains 'sessions/'" | where_exp: "p", "p.path != 'sessions/index.md'" %}
{% assign session_pages = session_pages | sort: "date" %}
{% assign upcoming_sessions = "" | split: "," %}
{% assign past_sessions = "" | split: "," %}
{% for s in session_pages %}
  {% assign s_date = s.date | date: "%Y-%m-%d" %}
  {% if s_date > today %}
    {% assign upcoming_sessions = upcoming_sessions | push: s %}
  {% else %}
    {% assign past_sessions = past_sessions | push: s %}
  {% endif %}
{% endfor %}
{% assign next_session = upcoming_sessions | first %}

{% if next_session %}
{% include next-session.html session=next_session %}
{% endif %}

{% if past_sessions.size > 0 %}
## Past sessions

Each session's page keeps the exercises, the prompts and the replies we got, so you can try them again later or catch up on one you missed.

{% include cards/card-toc.html rows=past_sessions %}
{% endif %}

## Later this semester

{% include schedule-list.html %}

Later sessions take the same approach: try the tools on work you already know how to judge. Topics for the TBA dates are still being decided. Some we're considering:

- **Reading and note-taking.** Ask AI about a text you know well, and see what that tells you about asking it about one you don't.
- **AI in the classroom.** Design assignments that assume students have these tools.
- **Research assistance and its limits.** Where fabricated citations come from, and habits that catch them.

Have a request? [Tell us](https://amaranth.unm.edu) and we'll add it to the list.

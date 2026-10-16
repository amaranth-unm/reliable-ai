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
- **Something of your own to try it on.** Each session's page says what, such as a paragraph of your writing or a photo of a handwritten page. If you don't have anything suitable, the session page has examples you can use instead.
- **Nothing you shouldn't share.** Leave out other people's unpublished work, student writing with names attached, and anything under embargo or an IRB protocol.

{% comment %}
  Every session in date order, past and upcoming together, as one compact
  line each (cards/session-list.html): a reference list that links to the
  session pages. The home page is the display, with the next session's
  points, note and flyer. The lookup is repeated from index.md; see the
  comment there for why.
{% endcomment %}
{% assign today = site.time | date: "%Y-%m-%d" %}
{% assign session_pages = site.pages | where_exp: "p", "p.path contains 'sessions/'" | where_exp: "p", "p.path != 'sessions/index.md'" | where: "layout", "base" | where: "name", "index.md" | where_exp: "p", "p.published != false" | sort: "date" %}

## All sessions

Each session's page keeps the exercises, the prompts and the replies we got, so you can try them again later or catch up on one you missed.

{% include cards/session-list.html rows=session_pages today=today %}

Have a topic request? [Tell us](https://amaranth.unm.edu) and we'll add it to the list.

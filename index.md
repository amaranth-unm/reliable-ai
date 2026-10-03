---
title: Reliable AI for Humanists
layout: base
header-image: "/assets/images/aldine-colophon-1521.jpg"
header-tier: hero
header-position: center center
header-filter: botanical
header-caption: "Festina lente: the closing leaves of the Aldine <i>Terence</i>, Venice, June 1521 — the imprint, and the anchor-and-dolphin mark. John Carter Brown Library."
header-eyebrow: Amaranth Brown Bag Series
header-title: Reliable AI for Humanists
header-divider: bring lunch and a laptop
header-subtitle: Hands-on sessions on getting useful, checkable results from generative AI, using work you already know how to judge.
summary: "A brown bag series on using generative AI well in humanities research and teaching. All skill levels welcome."
---

A lunchtime series from Amaranth for people at UNM who are curious about generative AI but skeptical if not unconvinced by most of what they have heard about it. Each session takes a routine task or process common in the humanaities and explores how AI can augment or speed up the process in reliable ways.
{: .lead}

There are many reasons to be skeptical about AI. Much of what gets claimed for these tools is overstated, and the failures are the ones that matter most in our work: invented sources, confident misreadings, prose that flattens significant nuance. 

But that doesn't mean AI is hopeless for the humanities. And often, unhelpful AI output comes from unrefined prompting and cursory use, rather than sustained engagement with a complex tool that takes significant practice to harness. 


## How the sessions work

Our meetings aim for a deliberate combination of demonstration and discussion. We go through some use cases that can help you augment your work. You can follow along with our sample prompts and texts, or you can work with your own writing or sources so it's easier to tell whether a tool helped or whether it merely sounded fluent.

This is not about outsourcing thinking or writing. This is about using a powerful tool to help and augment what you're already doing.

Everything runs on free accounts, and we try to showcase a variety of tools and workflows, since everyone has different ways of working. 

These are not AI propaganda sessions. These are not anti-AI communions. We try to be balanaced about what AI tools can do now, how they have changed, and where they are headed. Read more on the [About]({{ site.baseurl }}/about) page.

{% comment %}
  Next/past sessions are read from the sessions/ folder's own front matter
  (date, time, location, summary, note) instead of being typed here — add a
  session's file and this picks it up. sessions/index.md repeats this same
  lookup for its own "Coming up" line: Liquid's include tag scopes assigned
  variables to the include, so this can't be worked out once and shared across pages.
  Keep the two in sync if the lookup logic changes.
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
{% assign recent_sessions = past_sessions | reverse %}

{% if next_session %}
{% include next-session.html session=next_session %}
{% endif %}

## Later this semester

{% include schedule-list.html %}

{% if recent_sessions.size > 0 %}
## Past sessions

{% include cards/session-row.html rows=recent_sessions limit=3 %}
{% endif %}

<p>
  <a href="{{ site.baseurl }}/sessions/" class="btn-primary">See all sessions →</a>
</p>

*Hosted by [Amaranth](https://amaranth.unm.edu), a digital humanities and public scholarship studio at UNM.*

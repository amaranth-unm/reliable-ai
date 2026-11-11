---
title: Reliable AI
layout: base
header-image: "/assets/images/aldine-colophon-1521.jpg"
header-tier: hero
header-position: center center
header-filter: botanical
header-caption: "Festina lente: the closing leaves of the Aldine <i>Terence</i>, Venice, June 1521, showing the imprint and the anchor-and-dolphin mark. John Carter Brown Library."
header-eyebrow: Amaranth Brown Bag Series
header-title: Reliable AI
header-divider: bring lunch and a laptop
header-subtitle: Hands-on sessions that build the skills and the confidence to use generative AI well, starting from the humanities habits you already have.
summary: "A brown bag series that builds skill and confidence with generative AI in research and teaching. No technical background needed."
---

A lunchtime series from Amaranth for people at UNM who want to get good at using generative AI, whether you are curious, skeptical or somewhere in between. Each session takes a routine task in research or teaching, often one from the humanities, and works through it step by step, so you leave able to do it on your own.
{: .lead}

## What you build

- **Skills you can use the next day.** Every session ends with prompts, files and habits you can take back to your own work.
- **Comfort with the technology.** Files and folders, attaching a document, starting a new chat, letting an agent work in a folder: each session explains what it uses as it comes up, and assumes no technical background.
- **Confidence that comes from checking.** You learn to hold what a tool gives you up against a source, a page or your own text, so you know when to rely on it and when not to.
- **Humanities habits as the core skill.** Close reading, source criticism, attention to context and careful citation are what make AI output usable. The sessions treat them as the expertise you bring, and build on them.

There are good reasons to be skeptical about AI. Much of what gets claimed for these tools is overstated, and the failures are the ones that matter most in our work: invented sources, confident misreadings, prose that flattens significant nuance. But unhelpful output often comes from cursory use rather than practice with a complex tool, and practice is what these sessions are for.

## How the sessions work

Each meeting combines demonstration and discussion around one task. You can follow along with our sample prompts and texts, or work with your own writing or sources, which makes it easier to tell whether a tool helped or only sounded fluent.

Every session page stands on its own afterwards: the prompts, the replies they produced and the files they used, with an explanation of each new term. Work through it at your own pace, or come back to it when you need it.

This is not about outsourcing thinking or writing. It is about using a powerful tool to help with what you're already doing.

You can follow almost everything on a free account; when a session needs a paid tool, the presenter demonstrates it. We try to showcase a variety of tools and workflows, since everyone has different ways of working. 

These are not AI propaganda sessions. These are not anti-AI communions. We try to be balanced about what AI tools can do now, how they have changed, and where they are headed. Read more on the [About]({{ site.baseurl }}/about) page.

{% comment %}
  Upcoming/past sessions are read from the sessions/ folder's own front matter
  (date, time, location, summary, note) instead of being typed here. Add a
  session's file and this picks it up. sessions/index.md repeats this same
  lookup for its reference list: Liquid's include tag scopes assigned
  variables to the include, so this can't be worked out once and shared across pages.
  Keep the two in sync if the lookup logic changes.

  A session stays upcoming through its own date (>=), and moves to past
  sessions the night after, when .github/workflows/nightly-rebuild.yml
  rebuilds the site. site.time is the build time, so without that rebuild
  the page would keep announcing a session until the next push.
{% endcomment %}
{% assign today = site.time | date: "%Y-%m-%d" %}
{% assign session_pages = site.pages | where_exp: "p", "p.path contains 'sessions/'" | where_exp: "p", "p.path != 'sessions/index.md'" | where: "layout", "base" | where: "name", "index.md" | where_exp: "p", "p.published != false" %}
{% assign session_pages = session_pages | sort: "date" %}
{% assign upcoming_sessions = "" | split: "," %}
{% assign past_sessions = "" | split: "," %}
{% for s in session_pages %}
  {% assign s_date = s.date | date: "%Y-%m-%d" %}
  {% if s_date >= today %}
    {% assign upcoming_sessions = upcoming_sessions | push: s %}
  {% else %}
    {% assign past_sessions = past_sessions | push: s %}
  {% endif %}
{% endfor %}
{% comment %}
  Upcoming sessions are set as a program (cards/session-program.html): the
  next one opens out with its points, later ones are agenda rows, each
  labelled with how many weeks away it is. Past sessions run oldest first,
  two to a row, so the semester fills in as a grid in the order it happened.
{% endcomment %}
## Upcoming sessions
{: .sessions-heading}

{% if upcoming_sessions.size > 0 %}
{% include cards/session-program.html rows=upcoming_sessions today=today %}
{% endif %}

{% include schedule-list.html tba_only=true %}

{% if past_sessions.size > 0 %}
## Past sessions

{% include cards/session-row.html rows=past_sessions limit=20 pairs=true %}
{% endif %}

<p>
  <a href="{{ site.baseurl }}/sessions/" class="btn-primary">All sessions at a glance →</a>
</p>

*Hosted by [Amaranth](https://amaranth.unm.edu), a digital humanities and public scholarship studio at UNM.*

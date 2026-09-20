---
title: Sessions
layout: base
header-image: "/assets/images/letterforms.webp"
header-tier: banner
header-filter: etching
header-title: Sessions
summary: "Every session in the Reliable AI for Humanists brown bag series, with the full materials from each."
---

Each session is a working hour: a short framing, three or four exercises you do on your own writing, and a set of prompts you keep. Pages stay up afterwards with everything we covered, so you can run the sequence again — or catch a session you missed.
{: .lead}

{% assign session_pages = site.pages | where_exp: "p", "p.path contains 'sessions/'" | where_exp: "p", "p.path != 'sessions/index.md'" %}
{% include cards/card-grid.html cards=session_pages %}

## Coming up

Later sessions in the series build on the same principle — that you learn what these tools are good for by using them on work you already know how to judge. Topics under consideration:

- **Reading and note-taking** — what happens when you ask AI about a text you know well, and what that teaches you about asking it for one you don't.
- **AI in the classroom** — designing assignments for a world where students have these tools, rather than around it.
- **Research assistance and its limits** — where fabricated citations come from, and the habits that catch them.

Have a request? Tell us and we'll put it on the list.

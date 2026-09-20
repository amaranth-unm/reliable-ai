---
title: Reliable AI for Humanists
layout: base
header-image: "/assets/images/amaranth-flower-etch.jpg"
header-tier: hero
header-filter: botanical
header-eyebrow: Amaranth Brown Bag Series
header-title: Reliable AI for Humanists
header-divider: see examples · try it out · ask questions
header-subtitle: Techniques, habits, and workflows for getting more useful results from generative AI — the kind that complement expertise and human judgment instead of substituting for them.
summary: "A brown bag series on using generative AI well in humanities research and teaching. All skill levels welcome."
---

We can't think clearly about AI — in our research, in our classrooms, or in the arguments happening around us — without knowing something about how it actually behaves. That means using it, carefully, on work we know well enough to judge.
{: .lead}

These are working sessions, not demonstrations. Bring a laptop and something you're actually writing. Every session leaves you with prompts you can reuse and a habit you can take back to your own desk. All skill levels welcome, and "I've never opened one of these things" is a perfectly good starting point.

## Next session

<div class="rule" markdown="1">
**AI as Editorial Assistant** · Wednesday, September 23, 12:00–12:50 · History Common Room
</div>

Editing is the best place to start, because it's the one task where you already know the right answer. You are the expert on your own paragraph. That makes it the only safe place to learn the skill that actually matters — judging what the machine hands back.

**Before you come:** bring a laptop and **one paragraph of your own writing** — a draft, an abstract, a syllabus policy, a cover letter, anything. If you'd rather not bring your own, we have [practice texts]({{ site.baseurl }}/practice-texts) ready to go. Arrive with an AI tool already open in a browser tab and you'll save yourself five minutes.

<p><a href="{{ site.baseurl }}/sessions/editorial-assistant" class="btn-primary">Follow along →</a></p>

## Sessions

{% assign session_pages = site.pages | where_exp: "p", "p.path contains 'sessions/'" | where_exp: "p", "p.path != 'sessions/index.md'" %}
{% include cards/card-grid.html cards=session_pages %}

## What every session assumes

- **You keep the pen.** These sessions are about getting AI to read, question, and check — not to write for you. Every technique here is designed to leave the words yours.
- **Nothing you learn depends on a subscription.** Everything we do works on free tiers. We don't endorse a particular tool, and we'll name more than one.
- **Bring real work.** Generic exercises teach generic lessons. The point is to find out how these tools behave on the writing you actually care about.
- **Skepticism is welcome.** Several of us are unconvinced, and that's a better starting position than enthusiasm. Knowing what these tools do badly is most of the skill.

*Hosted by [Amaranth](https://amaranth.unm.edu), UNM's digital humanities and public scholarship studio.*

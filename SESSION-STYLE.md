# Session Page Style

How to write a session page for the Reliable AI brown bag series. Read this
before starting one. `sessions/editorial-assistant.md` is the worked example
and every rule below is drawn from it — when the two disagree, the page is
probably right and this file needs updating.

Contributor notes only; excluded from the build in `_config.yml`.

## What a session page is for

**Three audiences, one page, no branches.** Someone doing the exercises live,
someone watching the screen, and someone who missed it and is reading a month
later. They all work down the same page in order. Say so at the top and then
never mention the distinction again — no "if you're following along" asides,
no separate handout track.

The test for anything you're about to add: **does it survive the session?** A
page that only makes sense with you talking over it is a slide deck, and it
will be dead by Friday. The page is the artefact; the hour is the occasion.

## Front matter

```yaml
---
title: AI as Editorial Assistant          # site-wide, appears in cards and <title>
layout: base
position: 1                               # order in the session card grid
date: 2026-09-23
kicker: Session 1 · September 23, 2026    # line above the title in the sessions list
summary: "Treat AI as an eager but naive editor: …"   # the card blurb
thumbnail: "/assets/images/amman-typefounder-1568.jpg"
header-image: "/assets/images/amman-typefounder-1568.jpg"
header-tier: section
header-filter: etching
header-title: AI as Editorial Assistant
header-subtitle: "Everything below is a way of teaching a reader…"
tags: [editing, prompting, getting started]
workshop_mode: true
---
```

**`summary` is for the list, `header-subtitle` is for the page.** They are
different jobs and should not be the same sentence. The summary sells the
session to someone scanning `sessions/`; the subtitle tells someone who has
already arrived what the session is arguing.

**`sessions/index.md` lists past sessions as `cards/card-toc.html` rows**,
under the same next-session bar as the home page, not as a card grid — a series index is a table of contents, and a full-width row with
the session number, the title and one sentence reads as one at a glance. The
row takes `kicker`, `title` and `summary`, so all three have to carry their
weight on their own: there is no thumbnail to do the work. Keep `summary` to a
single sentence that says what the session *does*.

**`time` and `location` are optional, and only matter before the session
happens.** The home page and `sessions/index.md` both scan the sessions
folder for whichever page has the soonest future `date` and announce it
automatically — see the lookup in `index.md` — so these two fields are what
that announcement shows (alongside `summary`, reused as the announcement's
blurb, and `note` for a logistics line like what to bring). Announcing a
session is adding its file with these fields filled in and a short
placeholder body; nothing on the home page is hand-typed per announcement.
Once a session is in the past, nothing reads `time` or `location` any more —
`editorial-assistant.md` doesn't carry them, and a session you're writing up
after the fact doesn't need to either.

**`workshop_mode: true` is not decoration.** It loads the bullet-highlighting
script (`_includes/html/html-js.html`), which is what lets you walk the room
through a list without a cursor. Every session page needs it.

**`header-tier: section`** for every page but one. Sessions, the sessions
index, about and practice texts all use it, so the header is the same 60vh
band wherever you land. `hero` is the series home alone, and it is the only
place 100vh is worth the scroll. Don't reach for it on a session: opening at
full height makes people scroll before they can start.

`banner` (22vh) is no longer used. About and practice texts were on it, and at
that height the header read as a nameplate rather than part of the page. If
you bring it back, know that the tier renders a title and nothing else: no
subtitle, which is where a page's argument goes.

**Header images are early modern prints, and they carry a `header-caption`.**
The series is about a division of labour between machine and judgment, so the
images are printing-house images — Stradanus's *Impressio Librorum* on the
sessions index, Amman's typefounder on session 1, the Aldine device on the
home page. Source them at 2000px on the long edge, public domain, and credit
maker, title, holding institution and licence in `header-caption`. Fetch at
the command line rather than saving from a browser:

```sh
curl -sL -H 'User-Agent: your-name (your-email)' \
  'https://commons.wikimedia.org/wiki/Special:FilePath/<FILE>?width=2400' -o raw.jpg
magick raw.jpg -crop <plate area> +repage -resize 2000x2000\> -quality 84 out.jpg
```

Crop to the engraved area and drop the letterpress caption and sheet margins —
they read as grubby edges at header size, and the identification belongs in
`header-caption` anyway.

**`header-flip: true` mirrors the background image.** The `section` tier sets
its text in a column on the left, so a print whose figure also works on the
left puts the two on top of each other. Session 1 uses it: Amman's typefounder
sits at his bench on the left of the block, and flipping moves him clear of
the subtitle. It mirrors the image layer only, so the title and caption stay
the right way round. Two things to know: a mirrored print is a reversed
historical document, so don't use it where the image contains legible type or
a device that reads as a signature (the Aldine anchor, a maker's monogram);
and `header-position` applies to the unflipped image, so `right` shows what
ends up on the left.

## The header carries the argument

**Put the session's thesis in `header-subtitle`, not in the body.** It is the
one claim the whole hour turns on, and it belongs where someone landing on the
page reads it before anything else — above the table of contents, above the
housekeeping. From the worked example:

> Everything below is a way of teaching a reader what to look for. None of it
> is a way of getting something written. That distinction is the whole
> session, and it's also what makes this work defensible when a journal, a
> department, or a student asks what the machine did.

Three sentences is the ceiling. It renders in `--page-header-ink` — the text
ink warmed toward the ochre shadow, so it belongs to the printed image it sits
on — in a 58%-wide content box (see `assets/css/page-header.css`), which holds
about that much before it starts crowding the image.

**The palette is `assets/css/themes/rubric.css`**, sampled from a printed
antiphonal: black ink and vermilion on parchment. Red is the rubric — it marks
what the reader should notice and is never decoration, so use `--accent-primary`
for the one thing on a page that matters and let ink carry everything else.
The standing exception is the `.step` band on each main division, which is
what a rubric originally was: a heading written in red.

**Pick a header image that is line art**, and use `header-filter: etching` —
the filter is tuned for marks on paper and renders them as dark brown ink.
Photographs go through `photo`. If the header text stops reading against a
busy image, lower `header-opacity` on that page rather than changing the
filter for everyone.

## The shape of a page

The spine is fixed. Sessions differ in their steps, not their skeleton.

Items 4 to 6, and a `### The paragraph we'll use` for the session's running
example if it has one, sit under a single `## Introduction`, marked
`{: .step #introduction}` like the steps so it gets the same band. The table of
contents lists `##` headings, so it shows the introduction, the numbered steps
and the takeaways, and nothing else.

1. **`{% include nav/scrollspy-toc.html %}`** — first line of the body.
2. **The orientation line**, with `{: .lead}`. Who the page is for and how to
   use it. One sentence.
3. **A `.rule` callout** carrying the session in four words — "AI reads. You
   write." This is the thing people repeat afterwards. Write it last, once you
   know what the session turned out to be about.
4. **`### Why <this> is the place to start`** — why this topic and not a more
   obvious one. This is where you argue that the exercise is worth the hour.
5. **`### What you're working with`** — three or four tool behaviours the
   session will demonstrate, each one pointing at the step where it shows up.
   Behaviours only: nothing about how the model works inside, because that is
   not checkable from a browser tab and the whole series rests on the reader
   being able to check. Keep it to about 150 words — it is a map, not a
   lecture, and a long one re-creates the problem the session exists to avoid.
6. **`### Before you start`** — what to bring, and, as its own bullet, **what
   to leave out**. Unpublished work, student writing with names, anything
   under embargo or IRB. Never skip the second half.
7. **Numbered steps** — see below.
8. **`## What to take with you`**, marked `{: .step #takeaways}` — the last
   section. The session compressed to a bulleted list of principles, each one
   bolded and then explained in a clause. These should read as portable rules,
   not as a recap of what was clicked.

There is no separate closing pass or links section. Send readers back to the
thing they brought inside the steps instead: a line at the end of an early
step ("Now send the same request with your own paragraph") does the work a
closing section used to, while the exercise is still fresh. Link each worked
example from the step that uses it, so nothing depends on a list at the end.

**Watch the proportions, and measure them.** The failure mode of a session
like this is that it quietly becomes a prompting lesson: the steps that
configure the tool crowd out the steps where something happens to the
reader's own work. `editorial-assistant` drifted this way — rule craft and
file hygiene reached 60% of the page while the reader-comparison payoff, the
one move that is hard to get any other way, had 163 words. **Aim for at least
a third of the page on what the reader sees in their own writing**, and give
the strongest demonstration more room than any setup step. Word-count the `##`
sections if you are not sure; the instinct that something is off is usually
right and is always checkable.

## Steps

```markdown
## 3. Turn corrections into rules
{: .step #step-3}
```

**Number them and make the heading a verb phrase.** "Start with the bad
version", "Teach it to read like you do", "Move out of the chat window". The
reader should be able to tell from the table of contents what they will *do*,
not what topic is covered.

`.step` sets the heading as a vermilion band (`assets/css/prompt.css`), so the
page's main divisions stand apart from the `###` headings inside them, and sets
`scroll-margin-top` so a `#step-3` link doesn't land under the navbar. The id is what the scrollspy and
any cross-page link point at, so keep the `#step-N` form.

**Sub-steps are plain `###`**, no `.step`. Use them when a step has genuinely
separate moves — step 3 has five, each one a rule about writing rules.

**Open each step with the move, not with context.** "Paste your paragraph,
then send this and nothing else." The explanation goes after the prompt, once
they have a result in front of them to look at.

**Every step earns its place by producing something the next step uses.** Step
1 produces the baseline; step 2 beats the baseline; step 3 harvests rules from
what step 2 corrected. If a step could be cut without breaking the chain, cut
it.

## Show what came back

**A session page that shows no output is a recipe, not a demonstration.** The
first version of `editorial-assistant` had twenty prompts and zero replies on
it: it told the reader that briefing produces sharper comments, that a vague
finding collapses when you make it quote, that a policy falls apart when a
student reads it — and showed none of it. A reader who wasn't in the room had
no way to tell whether any of it worked, which is the difference between a
session that carries weight and one that reads as a prompting exercise.

**Carry one text the whole way down.** Pick a specimen that looks finished —
`editorial-assistant` uses the AI-use policy from the practice texts — and
show the same paragraph at every turn. The reader is then watching one thing
change, not collecting techniques.

**Pair every strategy with a `demo.html` block.** Prompts live in
`_data/prompts.yml`, replies in `_data/demos.yml`, and the two render as
deliberately different components: a prompt is dark, mono and copyable; a demo
is paper, prose and read-only, with the tool and date in its header. An entry
with empty `text` renders as a loud red unfilled slot, so a half-finished
demonstration cannot ship looking finished.

**Never write a demo's `text` from memory or imagination.** This is the one
rule on this page that has no exceptions. The entire series rests on the claim
that the reader can check everything, and a plausible invented transcript
destroys that for every other page too. Trimming a long reply is fine — mark
the cut with […]. Reordering, tidying the grammar, or merging two runs is not.

**Date every demo, and re-run them before you teach the session again.**
Models drift. A transcript that was true in September and is quietly false in
March is worse than no transcript, because it still looks like evidence. When
a re-run comes back materially different, replace it and move the date — and
consider saying so on the page, because "we re-ran this and it no longer
flatters us" is itself one of the most useful things the series can show.

## Prompts

**Prompts live in `_data/prompts.yml`, never inline in the page.**

```liquid
{% include prompt.html id="rule-harvest" %}
```

Each entry carries `id`, `session`, `step`, `label`, `note`, `text`. Fill in
`session` and `step` so it's clear which exercise an entry belongs to.

**Render every prompt inside the session that teaches it.** There is no
standalone prompt library, and adding one back would undo the argument the
series makes: a prompt lifted away from the exercise it came out of is exactly
the "magic words" reading these sessions exist to break. If a prompt seems to
have nowhere to go, that means the page is missing the step that earns it, not
that the site needs a list.

**The `note` is instructions for the person pasting it** — what to fill in,
what to keep, what to watch for. The body text around the prompt is the
argument; the note is the operating manual. Don't duplicate one in the other.

**Write prompts to be pasted whole.** Bracketed slots (`[genre: seminar paper
/ abstract]`) with real options in them, not `[your genre here]`. Someone who
doesn't know the vocabulary of the field should be able to pick one.

## Voice

**Second person, imperative, present tense.** "Paste your paragraph." "Look
hard at what came back." The reader is doing something, not being told about
it.

**Bold the load-bearing claim, once per paragraph at most.** The bolding is a
skim layer — someone reading only the bold should get the argument. Two bolds
in a paragraph means neither is the point.

**Write like a colleague explaining something, not like a slogan.** Earlier
drafts leaned on patterns that read as machine-written once they pile up, and
a September 2026 copy pass took most of them out. Watch for:

- **Aphorisms and punchy closers.** "Twice is a rule." "That's all prompting
  is." "Correcting it is the point." One memorable line per step at most, and
  only if it compresses a move the reader just made. Otherwise say it plainly.
- **Sentences that rate their own importance.** "That is the whole method."
  "This is the whole workshop in one block." "That retraction is the
  demonstration." The sentence stops to tell the reader that what they just
  read was the important part. If the point landed, the label adds nothing; if
  it didn't, the label won't rescue it. Cut it and let the claim stand, or
  write a better claim. Watch for "that is the whole X", "X is the point",
  and "that is what this is really about".
- **"Not X, but Y" contrasts.** "Working sessions, not demonstrations."
  "Scaffolds, not incantations." Say what the thing is.
- **Em-dashes as all-purpose joints.** Use a period, comma, colon or
  parentheses. The session page has none now; keep it that way.
- **Triplets by reflex.** Three examples, three clauses, three nouns. Use as
  many as the point needs.
- **Bold lead-ins on every bullet.** Fine for a list of distinct items people
  scan (what to bring, the takeaways). Elsewhere, write the list plainly or
  make it a paragraph.
- **Drafting notes left on the page.** Provenance belongs in one clear note
  near the top ("About the replies on this page") and in the demo headers,
  not repeated in hedges after every example.
- **Clinical verbs standing in for ordinary ones.** "Inspect the result,"
  "examine its comments," "evaluate the reply," "surface different questions."
  A September 2026 pass took ten uses of "inspect" off the session page, where
  it had come to mean read, reread, check and test on different lines. Write
  the verb you mean: read it, check it against the original, go and look at
  the sentence, test the rule where it shouldn't fire.
- **Nominalizations that hide who acts.** "A request to identify an unclear
  instruction gives you more to evaluate." "The useful result is a decision you
  can explain." Find the buried verb and give it back its subject: "Asking
  which instruction is unclear gets you more to work with."
- **Hedges stacked on hedges.** "Agreement can suggest a place to inspect."
  One hedge is honest, two is evasive. Say what the reader learns and what they
  don't: "Where the readings agree, you have learned where to look. You have
  not learned that the criticism is right."


**Explain failure as behaviour, not malfunction.** "None of that is
malfunction. You asked an eager, well-read, thoroughly naive assistant to edit
an unlabelled paragraph." The reader should leave able to predict the tool,
not resenting it.

**No hype, no doom, and no claims about how the model works internally.**
Everything on the page should be verifiable by someone sitting in front of a
chat window with their own paragraph. If a sentence requires the reader to
trust you about model internals, cut it. The reader has to be able to check
everything here, or the series has no standing to ask them to check anything.

**Never promise a specific tool's behaviour.** "Claude, ChatGPT, Gemini,
Copilot, any of them" — the exercises work across tools, and naming versions
dates the page.

## Before publishing

- Every prompt on the page resolves — a bad `id` renders nothing and fails
  silently.
- `position` doesn't collide with an existing session.
- The step ids run `#step-1`…`#step-N` with no gaps, and `#takeaways` closes.
- The header subtitle is three sentences or fewer and reads against the image.
- The "what to leave out" bullet is present in **Before you start**.
- `bundle exec jekyll serve` and walk the page at phone width. The section
  header grows to fit its subtitle under 768px rather than clipping it, so a
  long one pushes the table of contents down the page — check it still opens
  on something other than the header.

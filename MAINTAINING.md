# Maintaining the Reliable AI for Humanists site

Notes for whoever edits the site. Workshop participants don't need any of
this; the [README](README.md) sends them to the site.

This is the site for Amaranth's AI brown bag series. Built with [Xanthan](https://xanthan-web.github.io)
(class-project template), published to GitHub Pages at
<https://amaranth.unm.edu/reliable-ai/>.

The site does two jobs: people follow along on it during a session, and it's
where the material lives afterwards.

## Running it locally

```bash
bundle install     # first time only
bundle exec jekyll serve
```

Then <http://localhost:4000/reliable-ai/>. The `baseurl` in `_config.yml` means
the path is required — plain `localhost:4000` will 404.

## Writing a session

**Read `SESSION-STYLE.md` before starting or editing a session page.** It is
the source of truth for front matter, the fixed page skeleton, how steps and
prompts are written, and the voice. `sessions/editorial-assistant.md` is the
worked example.

Keep all session work in this repo, including presenter notes, drafts and
local verification. Use `workshop-drafts/<session>/` for private planning and
its ignored `_local/` subfolder for rehearsal runs, source checks and local
preview artifacts. Build directly into the repo's ignored `_site/`; avoid
parallel authoring copies in other project folders. `SESSION-STYLE.md`
documents the convention.

## How it's put together

```
_data/prompts.yml           every prompt in the series, keyed by id
_includes/prompt.html       renders one prompt as a copyable block
assets/css/prompt.css       prompt blocks, step headings, the .rule callout
assets/js/prompt-copy.js    the copy buttons
index.md                    series home
sessions/                   one page per session; the session lists build themselves
practice-texts.md           invented paragraphs for people who didn't bring one
```

### Prompts

Prompts are written once in `_data/prompts.yml` and pulled in wherever they're
needed:

```liquid
{% include prompt.html id="editorial-brief" %}
```

That's why the same prompt can appear in a session's exercise and again in its
recap without the two versions drifting apart. Each entry takes `id`, `session`,
`step`, `label`, `text`, and an optional `note`. If an `id` doesn't match
anything, the page shows a visible warning rather than failing silently.

Prompts are only ever rendered inside the session that teaches them. There is
deliberately no standalone prompt library: a prompt separated from the exercise
it came out of is the thing this series argues against, and a single page
accumulating every prompt in the series would get long enough to be useless
anyway. `session` and `step` stay on each entry because they order the prompts
within a session page and make it clear which session an entry belongs to.

### Adding a session

1. Add `sessions/your-session.md` with front matter: `title`, `position`
   (controls card order), `kicker`, `summary`, `thumbnail`, and
   `workshop_mode: true`.
2. Add that session's prompts to `_data/prompts.yml` with a new `session:` value,
   and render each one with `prompt.html` at the point in the page it's taught.

The home page and `/sessions` pick the page up automatically; nothing to
register. Add its date and slug to `_data/schedule.yml` for the semester list.

### Unlisted previews

Set `published: false` in a page's front matter to build a preview that is
accessible at its usual URL and omitted from site listings, navigation,
search and the sitemap. `_config.yml` keeps `unpublished: true` so GitHub
Pages builds those files too; no custom plugin is needed. A robots tag asks
search engines not to index the preview. This is visibility, not access control.

Remove the flag or set `published: true` when the page is ready to be listed.
Existing pages without the flag retain their normal behavior. Do not add
manual links to a preview from another page. The schedule shows “Topic TBA”
when its session points to an unlisted page.

### Audit-trails example files

Edit `_data/audit_workspace.json`, then run
`python3 scripts/build-audit-workspace.py`. The browser viewer reads that data
and the script regenerates `assets/audit-trails/humanities-ai/` and its ZIP.
These are prepared teaching materials, not recorded agent replies. The
presenter guide is in `workshop-drafts/audit-trails/presenter-guide.md`;
`workshop-drafts/` is excluded from the public build.

### Understanding Agentic AI example files

Edit `_data/agentic_example.json`, then run
`python3 scripts/build-agentic-workspace.py`. It generates the fictional
starter files, ZIP and reference inventory in `assets/agentic-ai/`. The
unlisted reference guide at `examples/understanding-agentic-ai/` reads the
same data. Keep prepared examples distinct from observed agent runs. The
presenter guide is in `workshop-drafts/understanding-agentic-ai/`; save local
rehearsal and verification work in its ignored `_local/` subfolder.

### Presenting

The editorial-assistant slide deck is at
[`presents/editorial-assistant/`](slides/editorial-assistant/index.md).
It uses Reveal.js with the site's Rubric colors and typography. Edit its
Markdown sections directly; each section includes timing and speaker notes.

- **Space / arrow keys:** advance. On demonstration slides, the next advance
  reveals the response and discussion question.
- **Esc / All slides:** overview. **S:** speaker notes and timer.
- **Copy:** copy the displayed prompt. **Full tutorial:** return to the longer
  workshop page.
- Add `?print-pdf` to the deck URL, then print from the browser to export slides
  with all responses visible.

The shared layout is `_layouts/reveal-workshop.html`, with styles in
`assets/css/reveal-workshop.css` and initialization in
`assets/js/reveal-workshop.js`. Reveal.js 5.2.1 is bundled under
`assets/vendor/`; the runtime does not depend on a CDN. The upstream license
and distribution details are included there.

Session pages set `workshop_mode: true`, which turns on Xanthan's presentation
helper: press <kbd>w</kbd>, then <kbd>space</kbd> or the arrow keys to
step-highlight through list items one at a time. Press <kbd>w</kbd> again to
turn it off.

## Conventions

Same as the main Amaranth site: lowercase hyphenated filenames, images in
`assets/images/`, clarity over cleverness in the writing. Keep the prompts
copy-pasteable — people are pasting them into a chat window while someone talks
at the front of the room.

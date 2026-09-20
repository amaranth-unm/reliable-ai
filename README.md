# Reliable AI for Humanists

Site for Amaranth's AI brown bag series. Built with [Xanthan](https://xanthan-web.github.io)
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

## How it's put together

```
_data/prompts.yml           every prompt in the series, keyed by id
_includes/prompt.html       renders one prompt as a copyable block
assets/css/prompt.css       prompt blocks, step headings, the .rule callout
assets/js/prompt-copy.js    the copy buttons
index.md                    series home
sessions/                   one page per session; the card grid builds itself
prompts.md                  the whole prompt library, grouped by session
practice-texts.md           invented paragraphs for people who didn't bring one
```

### Prompts

Prompts are written once in `_data/prompts.yml` and pulled in wherever they're
needed:

```liquid
{% include prompt.html id="editorial-brief" %}
```

That's why a prompt can appear on a session page and in the library without the
two versions drifting apart. Each entry takes `id`, `session`, `step`, `label`,
`text`, and an optional `note`. If an `id` doesn't match anything, the page
shows a visible warning rather than failing silently.

### Adding a session

1. Add `sessions/your-session.md` with front matter: `title`, `position`
   (controls card order), `kicker`, `summary`, `thumbnail`, and
   `workshop_mode: true`.
2. Add that session's prompts to `_data/prompts.yml` with a new `session:` value.
3. Add a section to `prompts.md` that filters on it.

The card grids on the home page and `/sessions` pick the page up automatically —
nothing to register.

### Presenting

Session pages set `workshop_mode: true`, which turns on Xanthan's presentation
helper: press <kbd>w</kbd>, then <kbd>space</kbd> or the arrow keys to
step-highlight through list items one at a time. Press <kbd>w</kbd> again to
turn it off.

## Conventions

Same as the main Amaranth site: lowercase hyphenated filenames, images in
`assets/images/`, clarity over cleverness in the writing. Keep the prompts
copy-pasteable — people are pasting them into a chat window while someone talks
at the front of the room.

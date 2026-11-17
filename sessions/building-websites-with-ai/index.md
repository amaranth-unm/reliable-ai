---
title: Building Websites with AI
presenter: Allie Love
layout: base
position: 6
date: 2026-11-18
time: "12:00–12:50"
location: History Commons (MVH 1104)
kicker: Session 6 · November 18, 2026
# Draft summary and points; confirm with the presenter. Before the session is
# announced, also add flyer, note (what to bring) and header-subtitle (the
# session's thesis). See SESSION-STYLE.md.
summary: "Start from a free website template, ask AI for changes in plain language, and learn to read what it changed so the site stays yours."
points:
  - title: "Start from a working template"
    text: "Set up a free site on GitHub Pages, made of plain-text files you own and can keep for years."
  - title: "Direct AI in plain language"
    text: "Describe the change you want, from a warmer palette to a new page type, and let AI handle the code."
  - title: "Understand what AI built"
    text: "Ask AI to explain each edit so you can check it, undo it, and make the next change yourself."
thumbnail: "/assets/images/stradanus-press-1600.jpg"
header-image: "/assets/images/stradanus-press-1600.jpg"
header-tier: section
header-filter: etching
header-position: center right
header-opacity: 0.18
header-title: Building Websites with AI
header-subtitle: "Start from a working template and ask AI for changes in plain language. Then have it explain each change, so the site stays yours."
header-caption: "Jan van der Straet (Stradanus), <i>Impressio Librorum</i>, from <i>Nova Reperta</i>, engraved by Joannes Galle. Museum Plantin-Moretus, public domain."
tags: [websites, publishing]
workshop_mode: true
---

{% comment %}
Draft body, written from the presenter's outline. Until 2026-11-18 only the
front matter is public (a "Coming soon" card); the body goes live on the day.
"Prepared example" blocks are written for this page, not recorded runs; keep
them out of _data/demos.yml (see SESSION-STYLE.md).
Authoring conventions: SESSION-STYLE.md; worked example: sessions/editorial-assistant/index.md.
{% endcomment %}

{% include nav/scrollspy-toc.html %}

Work down this page during the session or return to it later: the prompts, examples and links stay together so you can repeat the exercise.
{: .lead}

<div class="rule" markdown="1">
**Start from a working template, and make AI change it one request at a time. You stay the editor.**
</div>

## Introduction
{: .step #introduction}

### Why start from a template

You can ask a chat tool for a whole website from nothing, and it will give you one. Try it if you're curious:

{% include prompt.html id="websites-whole-site" %}

The result is often impressive for about ten minutes. The trouble comes later. The site is in a structure the AI invented, which you didn't choose and can't read. To change something large, such as adding a new kind of page, you have to go back to the chat. The chat doesn't remember the choices it made before, so each request adds another layer, and after a dozen requests the pieces disagree with each other. If you go down this road, you have to do everything through AI from then on.

Starting from a **template** (a small, working site that someone else has built) is the alternative. [Xanthan](https://xanthan-web.github.io/) is a free template made for scholars and students, and it is built to be edited. Its files are plain text and its parts have clear names. Colors and fonts live in one place, content lives in another, and reusable pieces have documented options. That makes it legible to you, and legible to AI, which does better work on a site whose structure is clear.

You can still check every result in seconds: save the change, reload the page and look. You don't have to trust a description of what AI did. This session starts from a Xanthan portfolio you already have, published with GitHub Pages, which is also free. Your site is plain text files you own. You can move them to another host, keep them for years and read them yourself.

### What you're working with

- **A chat tool can write and revise code from a plain-language request** (steps 3 to 6). You describe the look or the feature, and it returns the lines to change.
- **A chat tool only knows the files you give it.** It doesn't know your site unless it can read it or you hand it over. When it guesses, it invents file names and settings that don't exist (steps 2 and 7).
- **It tends to add things rather than reuse them.** Left alone, it will write a new stylesheet or a new layout when your site already has one (step 8).
- **It will explain its own work if you ask**, and that is how you learn enough to take over (step 7).
- **An agentic tool removes the copying and pasting.** It reads and edits your whole site and takes bigger requests, so the habits you build in a browser chat matter more, not less (step 9).

### What a website is made of

Every word below turns up in the steps. You don't need to memorize them. Knowing the names is what lets you ask for the right change.

- **HTML** is the page itself: headings, paragraphs, images and links, marked up so a browser can display them.
- **Markdown** is a shorthand for writing HTML. `## A heading` and `*emphasis*` are Markdown. In Xanthan, you write your content in Markdown files.
- **CSS** is the style: colors, fonts, spacing, layout. It lives in separate files from your words. That separation is the most useful idea in this session: you can change how a whole site looks without touching what it says.
- **Front matter** is a few lines at the top of a page, between two rows of dashes, that give the page its title, description and image.
- **An include** is a reusable piece of a page, such as a card, a figure or a pull quote. You write it once and use it in many places, passing in the words and picture each time.
- **A repository** (repo) is the folder that holds your site, kept on GitHub. **GitHub Pages** turns that folder into a live website.
- **Jekyll** is the program GitHub Pages uses to assemble your pages from the Markdown, includes and styles.

### About the examples

This page shows prompts you can copy, and for the typography and color steps it also shows what a reply looks like. Those replies are labeled **Prepared example**. They were written for this page, not recorded from a chat tool, so they show the form of a good reply and not how any particular tool performed. Yours will differ with the model, the day and the files you give it. What stays the same is how you check them: open the page, look, and ask AI to explain anything you can't read.

The examples use a Xanthan portfolio whose colors and fonts live in a theme file. In these examples that file is `simple-theme.css`, the plain starter theme that comes with Xanthan. Yours may have a different name; the idea is the same. Xanthan also includes finished themes you can switch to, and a whole theme is just one text file, which is why AI can write one (step 3 shows how to ask). The example site you borrow from is a real portfolio, chosen because its fonts and colors are published in its stylesheet, and step 3 shows how to find your own. The examples assume an ordinary browser chat tool such as ChatGPT, Claude or Gemini. Steps 1 to 8 use one. Agentic tools such as GitHub Copilot are step 9.

### Setting up to follow along

- **You need your Xanthan site's GitHub repository.** If you don't have a portfolio yet, [Xanthan's Getting Started guide](https://xanthan-web.github.io/xanthan/docs/getting-started/) takes about 15 minutes.
- **You can do all of this in your browser.** Open your repository and press the `.` (period) key to open GitHub's built-in editor, or use the pencil icon on any file. Use a chat tool in a second tab.
- **A browser chat tool is limited.** ChatGPT and Claude work from what you put in the conversation. They can't change your repository, and they don't know what else is in it unless you show them. Step 2 covers three ways to show them.
- **Work a page at a time.** For a small change, give the chat one file, or a few. That is enough for most changes and keeps the replies short.
- **One change per message.** Several small requests are easier to check, and to undo, than one big one.
- **Start a new chat for a new job.** A long conversation drifts. If answers get strange, begin again and give it the current version of your files.

### Before you start

- **A Xanthan portfolio on GitHub Pages**, already set up, and the GitHub account that owns it.
- **A chat tool open in your browser**, such as ChatGPT, Claude or Gemini.
- **A few things for your site**: your name, a short description of yourself or a project, and two or three images you have the right to use.
- **A site you admire**, for steps 3 and 4. Any site whose fonts or colors you like will do.

## 1. Start from your Xanthan portfolio
{: .step #step-1}

This session assumes you already have a portfolio built from Xanthan. If you want to see what one looks like, the example is at **[xanthan-web.github.io](https://xanthan-web.github.io/)**. Open yours, and look at what it does before you change anything. Xanthan also has [class project](https://xanthan-web.github.io/class-project-template) and [ScrollStory](https://xanthan-web.github.io/scrollstory-template) templates, and everything below applies to them too.

1. Open your live site in one browser tab and your repository on GitHub in another.
2. Pick one thing on the live page, such as a heading, and find the line in the repository that produces it.
3. Press `.` on the repository page to open GitHub's editor, change a few words, and commit the change with the **Commit & Push** button.
4. Reload the live site. GitHub Pages takes a minute or so to rebuild.

<div class="keypoint" markdown="1">
Make one small edit yourself before you ask AI for anything. Then you know your site works, and you have a baseline to return to.
</div>

A template does two jobs for AI-assisted work. It teaches you the basic parts, so you know what to ask for. And it gives you a baseline: when AI changes something and the site breaks, you can compare against the version that worked.

## 2. Look at the files, and show AI your site
{: .step #step-2}

Open your repository on GitHub and click through the folders. You are looking for three kinds of file:

- **Content**: Markdown files such as `index.md`. This is where your words go.
- **Style**: CSS files, mostly in `assets/css`. In the example portfolio, the colors and fonts live in a theme file, `assets/css/themes/simple-theme.css`. Look in `assets/css/themes/` of yours to find the equivalent; the `theme_css:` line in `_config.yml` names the one in use.
- **Pieces**: files in an `_includes` folder, the reusable parts.

A chat tool can only help with files it has seen. There are three ways to show it your site, from easiest to most reliable.

### Give it a link

Your repository is public, so anyone, including an AI tool, can read it. Paste the address of your repository, or of one file, into the chat and ask about it. Some tools can open the link and some can't, and the ones that can sometimes read only part of a page or an old copy. If the answer mentions files you don't have, or the tool says it can't open the link, move on to the next way. A link to a single file's raw text (the **Raw** button at the top of the file on GitHub) works better than a link to the whole repository.

### Paste the text

Open a file on GitHub, click the copy icon at the top of the file, and paste it into the chat after your request. This works with every tool. It is practical for short files and for the part of a long file you want changed.

### Download the file, and upload it

This is the best route for real changes, because the chat gives you a finished file back instead of lines to paste.

1. Open the file on GitHub and click the download icon at the top of the file view.
2. In the chat, click the paperclip or **+** button and choose that file. You can attach several.
3. Ask for the change, and ask for the **complete changed file** back as a download.
4. Download the result. Open the folder on GitHub, click **Add file**, then **Upload files**, drop it in with *the same name*, and commit. A matching name replaces the old file, and a different name adds a second one.

Work a page at a time. For a small change, one or two files are enough, and the reply is easier to check. If a change needs three or four files (a new page, say, and the stylesheet it uses), send those together and say how they relate.

Try it now: pick one content file and send it with this prompt.

{% include prompt.html id="websites-read-file" %}

Try the same with the theme file. You will see that the two are separate: the Markdown holds what the page says, and the CSS holds how it looks. Xanthan keeps them apart on purpose, and the rest of the session depends on it.

<div class="keypoint" markdown="1">
Ask AI to define every technical term the first time it uses one. By the end of the hour you will know the words that let you describe a change precisely.
</div>

## 3. Copy the typography of a site you like
{: .step #step-3}

The quickest change that makes a site feel like yours is its type. Instead of choosing fonts from a list, point AI at a site whose text you like and ask it to work out what makes that text feel the way it does.

### Find a site to borrow from

You don't need a famous example. Any site whose text you enjoy reading will do. To find one:

- **Browse portfolios in your field.** Search for “[your field] portfolio”, or look through a list such as [Bethany Works' portfolio roundup](https://bethanyworks.com/portfolio/). Keep a note of two or three you like.
- **Look at what's on the page.** Ask yourself what you like: the headings, the spacing, the way links look.
- **Let AI identify the fonts.** Paste the address into the chat and ask “What fonts and colors does this site use?” If it can't open the page, right-click on a heading, choose **Inspect**, and look for `font-family` in the panel that opens. Or take a screenshot and attach it.

### Try it

In the example, the theme uses Xanthan's default fonts: Space Grotesk for headings and Source Sans 3 for body text, a clean, modern, all-sans look. The goal is to move it toward one portfolio found this way ([Meg Kendall's](https://www.megkendall.com/)), which pairs a light, elegant serif for headings with a clean sans-serif for body text. Here is the prompt, with the brackets filled in.

{% include prompt.html id="websites-copy-typography-example" %}

<details class="more" markdown="1" open>
<summary>Prepared example: the kind of reply that comes back</summary>

Meg Kendall's site pairs a light, high-contrast serif for headings (Cormorant Garamond) with a geometric sans-serif for body text (Poppins), and uses an italic serif for small accents. Headings are lightly letter-spaced, and body text sits at about 17px with generous line spacing. Your theme already sets a sans-serif body, so the main change is the heading font.

All changes are in `assets/css/themes/simple-theme.css`.

**1. Load the fonts.** Add this line at the very top of the file. Both fonts are free on Google Fonts, under the SIL Open Font License.

```css
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Poppins:wght@400;500;600&display=swap');
```

**2. Point the theme at them.** Your file has two commented-out font lines near the bottom of the `:root` block. Remove the `/*` and `*/` around them and change them to:

```css
--font-heading: 'Cormorant Garamond', Georgia, serif;
--font-body: 'Poppins', 'Helvetica Neue', Arial, sans-serif;
```

**3. Space the headings.** Add this rule at the bottom of the file:

```css
h1, h2, h3, h4 { letter-spacing: 0.02em; }
```

Cormorant Garamond looks smaller than Space Grotesk at the same size, so if the headings feel small, raise them by about 10%. To undo everything, delete the three additions and comment the font lines out again.
</details>

*Prepared example, written for this page. It is not a recorded run. The fonts and spacing described come from the stylesheet Meg Kendall's site publishes, and the file layout comes from Xanthan's `simple-theme.css`.*

Make the three edits, commit, and reload the live site. If the result isn't what you pictured, say so in plain words, as you would to a designer.

### Applying a reply to your site

The reply above is a list of steps, which is the most common shape, but it's the slowest to apply. A reply can arrive in three shapes, and you can ask for the one you want. Whichever you use, the routine is the same: **open the file on GitHub, make the change, commit, reload your live site.** If the page looks wrong, open the file's **History**, click the earlier version, and restore it.

| The reply gives you... | Do this |
|---|---|
| **A list of steps** with small snippets | On GitHub, open the file named in each step, click the pencil icon, find the lines it describes and replace them. Commit once at the end. |
| **One block to paste** | Open the file, scroll to the very bottom, paste the block, commit. |
| **A finished file to download** | Download it, then upload it to the same folder on GitHub with the *same name*. Commit. |

You can ask for the second or third shape by adding a sentence to any request.

{% include prompt.html id="websites-paste-block" %}

<details class="more" markdown="1" open>
<summary>Prepared example: a reply that is one block to paste</summary>

Nothing needs to be removed. Open `assets/css/themes/simple-theme.css`, scroll to the very bottom of the file, and paste this block under everything else:

```css
/* Typography: serif headings, sans-serif body */
:root {
  --font-heading: 'Cormorant Garamond', Georgia, serif;
  --font-body: 'Poppins', 'Helvetica Neue', Arial, sans-serif;
}

h1, h2, h3, h4 { letter-spacing: 0.02em; }
```

The fonts also have to be loaded. Paste this one line at the very top of the same file, above everything else:

```css
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Poppins:wght@400;500;600&display=swap');
```

(A browser only accepts an `@import` line at the top of a stylesheet, which is why it is a separate paste.)
</details>

*Prepared example, written for this page, not recorded. A block at the bottom works because later CSS rules win over earlier ones, so you never have to find the old lines. To undo it, delete the block and the line.*

For a bigger change, ask for the whole file.

{% include prompt.html id="websites-whole-file" %}

<details class="more" markdown="1" open>
<summary>Prepared example: a reply that is a downloadable file</summary>

I've changed the heading and body fonts and the heading letter spacing, and left everything else as it was. Download it here: **simple-theme.css**.

To use it: in your repository, open `assets/css/themes/`, choose **Add file**, then **Upload files**, and drop in the downloaded `simple-theme.css`. Because the name matches, GitHub replaces the old file. Commit it.
</details>

*Prepared example, written for this page, not recorded. The wording and the download link will look different in each tool. Before you upload, open the downloaded file and make sure it is complete and has the same name as the one it replaces. A file called `simple-theme (1).css` would be added next to the old one and change nothing.*

The same trick makes a whole theme: describe the feel, attach your current theme as a model, and ask for a new one as a downloadable file. Upload it to `assets/css/themes/`, then set `theme_css:` in `_config.yml` to its name, without `.css`. A mistake is easy to undo, since the old theme file is still there, and you can switch back by changing that one line.

<details class="more" markdown="1" open>
<summary>Prepared example: a follow-up</summary>

**You:** The headings look too thin now. Make them bolder, but keep the same font.

**Follow-up reply:** In the `h1, h2, h3, h4` rule you added, put `font-weight: 600;` inside the braces. Cormorant Garamond is already loaded at weight 600, so nothing else needs to change. For a middle ground, use `500`.
</details>

Notice what the prompt asks for and what it rules out. It asks for the *feel*, which is fonts, sizes, spacing and link style, and it rules out the other site's content, images and layout. Copying someone's design wholesale isn't the goal, and fonts are licensed, so ask for free ones and ask how to load them.

<div class="keypoint" markdown="1">
Name a site, and describe the type in your own words too (“tall, narrow headings; generous space between lines”). Each one helps the AI where the other is vague.
</div>

## 4. Change the colors and the overall mood
{: .step #step-4}

Colors work the same way: say the feeling you want, and give AI the file that holds them. A few ways to say it:

- **Palette.** “Warm and a little old-fashioned.” “Cool, clinical, lots of white.” “High contrast, black and one bright accent.”
- **Vibe.** “Like a museum label.” “Like a field notebook.” “Like a zine.” Or point at a site you found: “serene and a little luxurious, like a boutique retreat's website.”
- **Density.** “More white space around everything.” “Tighter, more like a newspaper.”
- **Exact colors.** If you already know them, give the hex codes (six characters after a `#`, like `#D7D0C5`) and let AI place them.

Two jobs for color pull against each other, and it helps to say which you want where. **Readable** colors are for the text people read for minutes: they need strong contrast against the background. **Eye-catching** colors are for the few things you want noticed, such as links and buttons, and they should be rare. If everything is eye-catching, nothing is. Ask AI to check the contrast and tell you the ratios. A ratio of 4.5 to 1 is the usual minimum for body text, and 3 to 1 for large headings.

Xanthan keeps its colors in one place, as named variables, so a palette change is a few lines, not a hunt through the whole site.

{% include prompt.html id="websites-palette-example" %}

<details class="more" markdown="1" open>
<summary>Prepared example: the kind of reply that comes back</summary>

**Palette 1: Stone and olive** (the palette Meg Kendall's site publishes)

| Role | Color | Contrast |
|---|---|---|
| Background | `#D7D0C5` | |
| Card background | `#EFEADF` | |
| Body text | `#3B3A26` | 7.5 to 1 on the background |
| Headings, links and buttons | `#554B32` | 5.6 to 1 on the background |
| Link hover | `#773E18` | 5.5 to 1 |
| Olive | `#676637` | 3.9 to 1. Fine for large decoration, too faint for small text, so not used for links |

**Palette 2: Sage and cream** (my own)

| Role | Color | Contrast |
|---|---|---|
| Background | `#F3EFE6` | |
| Card background | `#E7E1D3` | |
| Body text | `#26332B` | 11.5 to 1 |
| Headings, links and buttons | `#2F5D45` | 6.6 to 1 |
| Link hover | `#9A3F17` | 5.9 to 1. Terracotta, so hovering stands out against green |

**Palette 1 edit, in `assets/css/themes/simple-theme.css`.** Your theme defines six base colors at the top of `:root` and points everything else at them, so you only change those six values:

```css
--ocean-blue: #554B32;
--sky-blue: #773E18;
--cloud-white: #D7D0C5;
--pearl: #EFEADF;
--charcoal: #3B3A26;
--slate: #57573D;
```

That recolors the page, the cards, the navigation bar, links and hover states. The variable names are now misleading: `--ocean-blue` holds a dark brown. It works, but if that bothers you, I can rename them everywhere in the file. **To switch to palette 2**, use these six instead: `--ocean-blue: #2F5D45; --sky-blue: #9A3F17; --cloud-white: #F3EFE6; --pearl: #E7E1D3; --charcoal: #26332B; --slate: #5A665E;`.
</details>

*Prepared example, written for this page, not recorded. Palette 1 is the published palette of Meg Kendall's site, and the contrast ratios were calculated for this page. The variable names are from Xanthan's `simple-theme.css`.*

Two things to notice in that reply. It found the one place the colors live, so the change is six lines, not a hunt through the site. And it did the contrast check without being asked twice: the olive that looks good in decoration would be hard to read as a link, so it chose a darker color for links. If your tool skips this, ask.

<div class="keypoint" markdown="1">
Ask for options, not one answer, and ask for the contrast ratios. Choosing between two palettes is faster than describing one perfectly, and the numbers tell you which text your readers will struggle with.
</div>

## 5. Add something that moves
{: .step #step-5}

Sites can also have animated and interactive parts: text that fades in as you scroll, an image carousel, a before-and-after slider, a map. Xanthan already includes several, and the example portfolio has them in `_includes/images/` and `_includes/maps/`:

- **A carousel** (`images/carousel.html`) for a set of images the reader clicks through.
- **A juxtapose slider** (`images/juxtapose.html`) that compares two images, such as a map then and now, as the reader drags a handle.
- **Maps and scroll stories** (`maps/` and `scrollybox/`), where the picture changes as the reader scrolls the text.

Look through the [component reference](https://xanthan-web.github.io/xanthan/docs/reference/) first, and ask for a component by name: “Add a before-and-after slider to my Research page comparing these two images.” Using an existing component is more reliable than asking AI to write one from scratch, because it already works with your styles.

When what you want doesn't exist, ask for something new, but keep it small and give it limits. A fade-in on scroll is a good first one.

{% include prompt.html id="websites-motion" %}

The limits in that prompt are the useful part. “Switch off for readers who prefer reduced motion” and “the page must still work without the script” are the kinds of thing AI leaves out unless asked. After the change, scroll the page, then turn on your computer's reduced-motion setting and check that the effect goes away.

<div class="keypoint" markdown="1">
One effect per request, and say what it must never do. A short list of limits prevents most of the bad surprises.
</div>

## 6. Keep titles, descriptions and images apart, and build with includes
{: .step #step-6}

Look at how a page appears on your home page: a card with a title, a short description and an image. Those three things are *content*. How they are arranged and styled is *design*. In the example portfolio, they are written separately, in each page's front matter:

```yaml
---
title: Research
summary: One or two sentences about the work.
thumbnail: assets/images/my-image.jpg
---
```

The home page doesn't contain a copy of that text. It reads it from each page and draws a card, using an include (`cards/card-grid.html`). Change the summary on the Research page and the card on the home page changes with it. That is the point of keeping content and design apart: to change one, you edit one place.

When you want a piece the template doesn't have, ask AI to make a new include, and have it reuse your existing styles.

{% include prompt.html id="websites-new-include" %}

Once you have a card you can reuse, you can make bigger things from it. A scrolling row of projects is a good first one.

{% include prompt.html id="websites-scroll-projects" %}

Check the result by adding a second and a third card using only the three pieces of content. If a card needs more than a title, a description and an image, the include isn't finished.

<div class="keypoint" markdown="1">
Tell AI to keep content in the page and looks in the stylesheet. A new feature built on that rule can be edited by hand later.
</div>

## 7. Make AI tell you what it did, and how to edit it
{: .step #step-7}

Every answer from AI is a change to your site. Before you paste one in, ask for an account of it.

{% include prompt.html id="websites-explain-change" %}

This turns each request into a small lesson. In the typography example, an account of the change would say that the `@import` line loads the fonts, that the three `--font-` lines tell the theme which to use, and that changing `font-weight` in one rule makes every heading bolder. After a few rounds you'll recognize the file names, the CSS properties and the includes, and you can make small edits yourself. Changing a color code by hand is often faster than writing a request, and it spends no tokens or money.

You should also check what AI built, not only trust the account. Open the page, resize the window to phone width, tab through the links with your keyboard, and read the code it changed, even if you only understand part of it. If you don't understand a line, ask what it does.

GitHub also helps you check. After you commit, the file's **History** shows exactly which lines changed, in red and green, and lets you go back to any earlier version. That makes every experiment safe.

<div class="keypoint" markdown="1">
End any request with: “Tell me which files you changed, what each change does, and how to undo it.” You get the edit and an explanation of it in one reply.
</div>

## 8. Stay consistent, and see why the template matters
{: .step #step-8}

You could skip the template, as the introduction describes. This is the bitter lesson of using AI for this job: once the site exists only because AI wrote it, every change has to go through AI, and it doesn't remember your earlier choices. Suppose you ask for a new Teaching page. A chat tool with no view of your site will write a fresh page with its own fonts, its own colors and its own stylesheet. It looks fine alone. Next to your other pages it has a different heading size and a different blue. Do that a few times and the site is a pile of pieces that disagree, and it is hard for anyone, human or AI, to change one thing without breaking another.

A template prevents that by giving the site a structure. Understanding it also helps you in three ways:

- **You prompt better.** You can say “change the accent color variable” rather than “make it less blue.” Knowing the words (include, front matter, theme, variable) is most of the skill.
- **You can edit by hand.** For small changes, such as a color code, a heading or a link, it's quicker, cheaper and more reliable than a request. Save AI for the changes that need it.
- **You stay consistent.** A new page uses the layouts, includes and styles already there, instead of a new set.

{% include prompt.html id="websites-stay-consistent" %}

### For a shared project

The same rule applies when a group builds a site together, such as a class archive. Xanthan's [class project template](https://xanthan-web.github.io/class-project-template) gives every contributor the same layouts, so ten people's pages look like one site. The [campus history](https://amaranth.unm.edu/campus-history/) site is an example. AI can help with the design here too: ask it to write **instructions for contributors** and **page templates** that follow your site's own conventions, so that new pages match without anyone having to police them. Step 9 shows the same idea written for an AI agent.

<div class="keypoint" markdown="1">
Before asking for a new page or feature, tell AI to reuse what the site already has and to ask you before adding anything new.
</div>

## 9. Go further with an agentic tool
{: .step #step-9}

Everything so far worked in a browser chat, with you moving files back and forth. That has limits: the chat sees only what you give it, it can't change your repository, and it can't look at the result.

An **agentic** tool removes those limits. Instead of answering in a chat window and leaving you to apply the answer, it works directly on your site's files: it reads them, edits them and runs things on your computer, and it reports back. “Agentic” just means that it does the work itself, in steps, rather than telling you how.

You've already used the chat kind. Two common agentic tools are:

- **GitHub Copilot in Visual Studio Code.** VS Code is a free code editor you install on your computer. Copilot appears in a side panel, and you open your site's folder and type requests there, as you would in a chat.
- **The GitHub Copilot app,** a desktop app that opens your repository and works in it, with a chat on one side and your files and a preview on the other.

Both need your site copied to your computer first (the instructions for either tool cover this, and it is called cloning the repository). Other agentic tools work the same way. This isn't a different skill. It is the same habits (small requests, ask what changed, reuse what exists) with more power behind them, so you can start with the browser steps and come here when copy-and-paste starts to feel slow.

### What changes

- **It reads the whole site.** It knows which stylesheet loads which, which includes exist and where the colors are set, so it stops inventing files. That is the specific knowledge of how your site operates that makes its edits better.
- **It makes larger changes.** Ask it to add a Projects section: a page per project, a listing page of cards, new navigation links, and a stylesheet change, in one request. In a browser chat that would be five files and a lot of pasting.
- **It can change a structure, not just a file.** Reorganizing your navigation, renaming pages and updating every link to them, or moving from one layout to another, are all within reach.
- **It can run your site and look at it.** It can start a local copy and tell you the address, so you can see the change before anything goes live.

{% include prompt.html id="websites-agent-restructure" %}

### Write down the rules once

An agent that can change anything can also change the wrong thing. Maybe you've found yourself typing the same reminders into every chat: “keep the colors in the theme file,” “don't add new styles.” An agent lets you write those reminders down **once**, in a plain text file stored in your site's folder, and it reads that file at the start of every request. It's like handing a new assistant a sheet of house rules on their first day.

The file has three parts:

1. **What this site is,** in a sentence or two.
2. **Where things live,** so it doesn't have to guess.
3. **Do and don't lists.** What you want it to do, and what you never want it to touch.

GitHub Copilot looks for a file named `.github/copilot-instructions.md`. Several other tools look for `AGENTS.md`. It is an ordinary Markdown file, so you can edit it yourself at any time.

You don't have to write it from scratch. Ask the agent to draft it from your files, then read it and edit it until it says what you mean.

{% include prompt.html id="websites-agent-instructions" %}

<details class="more" markdown="1" open>
<summary>Prepared example: what such a file might say</summary>

```markdown
# Instructions for editing this site

This is a Xanthan portfolio built with Jekyll and published on GitHub Pages.

## Where things live
- Page content: the .md files in the root folder, for example index.md and research.md
- Colors and fonts: assets/css/themes/simple-theme.css (the active theme)
- Reusable pieces: _includes/
- Navigation: _data/nav-top.yml
- Documentation: docs/ (reference only)

## Do
- Change colors and fonts only in the theme file, using the existing variables.
- Reuse the existing includes and CSS classes before making new ones.
- Put a page's title, summary and thumbnail in its front matter.
- Explain every change in plain language and say how to undo it.

## Don't
- Don't add inline styles or a new stylesheet without asking me first.
- Don't edit anything in docs/.
- Don't change the navigation unless I ask.
- Don't delete or rename pages without asking me first.
```
</details>

*Prepared example, written for this page. The file locations are from the example portfolio. Your agent's draft will differ, and you should read it.*

Notice that the file says both what to do and what not to do. The “don't” list is the safety net: it's where you write down the things that went wrong before.

### Look at it before you commit

The word “commit” has a precise meaning. Until you commit and push, nothing an agent did has reached your live site. The changes are only on your computer. That gap is your chance to look, and it is the biggest advantage over a browser chat, where you could only look after you'd uploaded.

To look, run a local copy of your site. This means your computer builds the site for itself, and you view it in your browser at an address that only you can open.

1. **Ask the agent to start it.** “Run this site on my computer so I can look at it, and tell me the address to open.” It will install what's missing, run Jekyll (the program that builds the site), and tell you an address that looks like `http://localhost:4000`.
2. **Open that address in your browser.** You'll see your site with the agent's changes. Click through it. Check a phone-width window, too.
3. **Ask for fixes while you look.** “The cards are too close together. Add more space between them.” Reload to see the result.
4. **When you're happy, ask it to commit,** or use the Commit button in the tool. If you're not, say so, or ask it to undo everything it did.

For extra safety, ask the agent to work on a **branch**. A branch is a separate copy of your site's files that doesn't affect the live one. You can try a large change there, and if you don't like the result, you delete the branch and your live site is exactly as it was. If you do, you merge the branch into the main one, and the live site updates.

<div class="keypoint" markdown="1">
Write your do's and don'ts once, in a file the agent reads. Ask for a plan before it edits. Look at the result on your own computer before you commit.
</div>

## What to take with you
{: .step #takeaways}

<div class="takeaways" markdown="1">
Short rules to carry into your next site:

- **Start from a template.** AI can build a whole site, but a site it invented is hard to change. A template gives you something legible, and a baseline to compare AI's changes against.
- **Keep content and style separate.** Words in the Markdown, looks in the CSS, reusable parts in includes.
- **Say the feeling, then check the facts.** Describe the vibe and name a site you like, and ask for hex codes and contrast ratios so the result is readable as well as eye-catching.
- **Ask for one change at a time**, and say what the change must not do.
- **Ask what it did and how to undo it.** Every answer should teach you something you can do yourself.
- **Learn the vocabulary.** Knowing the names of the parts lets you prompt precisely and edit small things by hand, which costs nothing.
- **Reuse before adding.** Tell AI to use the stylesheet, layouts and includes that already exist, so the site stays consistent.
- **Write down the rules for agents.** An instructions file, a plan before edits and a local preview let you take on larger changes safely.
- **Keep the files.** The site is plain text you own, so you can change tools, hosts and AI whenever you like.
</div>

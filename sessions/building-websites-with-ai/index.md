---
title: Building Websites with AI
presenter: Allie Love
layout: base
position: 6
date: 2026-11-17
time: "12:00–12:50"
location: History Commons (MVH 1104)
kicker: Session 6 · November 18, 2026
# Draft summary and points; confirm with the presenter. Before the session is
# announced, also add flyer, note (what to bring) and header-subtitle (the
# session's thesis). See SESSION-STYLE.md.
summary: "Start from a free website starter site, ask AI for changes in plain language, and learn to read what it changed so the site stays yours."
points:
  - title: "Start from a working starter site"
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

Work down this page during the session or return to it later: the prompts and examples stay together so you can repeat the exercise.
{: .lead}

<div class="rule" markdown="1">
**Start from a starter site you can read, and let AI do the tedious parts. You stay in charge of your site.**
</div>

## Introduction
{: .step #introduction}

### Why not let AI build the whole site

You can ask a chat tool for a complete website, and in a minute you will have one. Try it if you're curious:

{% include prompt.html id="websites-whole-site" %}

The result usually looks good. The trouble starts when you want to change it. The AI chose the structure, and you can't read it. A large change, such as a new kind of page, means going back to the chat, which doesn't remember its earlier choices, so each request gets layered on the last. After a dozen of them the pieces no longer agree with each other. Even with AI doing the work, keeping a site like that up to date is slow and limited.

### Why start from a starter site

<<<<<<< HEAD
[Xanthan](https://xanthan-web.github.io/) is a free starter site made for scholars and students. You already have a portfolio built from it, so this session starts there. Its pages are plain text files with clear names, and you can edit them by hand without knowing how to code. Change a few words, save, reload, and the site is different. Your words live in one place and your colors and fonts in another. The files are yours to keep, and you can move them to any host.
=======
[Xanthan](https://xanthan-web.github.io/) is a free template made for scholars and students. This session starts from a portfolio built with it, and step 1 shows how to make one. Its pages are plain text files with clear names, and you can edit them by hand without knowing how to code. Change a few words, save, reload, and the site is different. Your words live in one place and your colors and fonts in another. The files are yours to keep, and you can move them to any host.
>>>>>>> c62d25b0f49978958cf59c12a20350da0c6761c8

### Why add AI to a starter site

Editing by hand gets tedious. Changing every color, adding a new kind of page or building a row of project cards takes a lot of careful typing. This is where AI helps, and a starter site makes it work better:

- You stay in control, because you can look at the files and see what the AI changed.
- AI does the jobs you don't want to do, and you decide how it does them.
- New pieces match the old ones, because the AI works inside a structure that already exists.

The session builds up to this in three stages. You start by copying and pasting between a chat and your site, which is slow but shows you exactly what is happening. Then you connect the chat to your site so the AI makes the edits itself. Last, you give it a short set of house rules and review its work before anything goes live.

### What a website is made of

You only need a handful of words. Knowing them lets you ask for the right change.

- **Pages** are text files written in Markdown, a simple way of marking up headings and paragraphs. This is where your words go.
- **The theme** is a file of colors, fonts and spacing, kept apart from your words. You can change how the whole site looks without touching what it says.
- **Front matter** is the few lines at the top of a page that give it a title, a short description and an image.
- **An include** is a reusable piece of a page, such as a project card. You build it once and use it in many places.
- **A repository** (repo) is the folder that holds your site on GitHub. **GitHub Pages** turns that folder into a live website.

### About the examples

The typography example in step 3 is a real ChatGPT conversation, shortened. The other replies are labeled **Prepared example**. I wrote them for this page to show the kind of reply an AI gives when it can edit your repository. Yours will differ with the tool, the day and the files it sees. How you check them stays the same: open the page, look, and ask the AI to explain anything you can't follow.

### Setting up to follow along

- **You need your Xanthan site's GitHub repository.** If you don't have one yet, step 1 shows how to make one.
- **You can do all of it in a browser.** Open your repository and press the `.` key to use GitHub's built-in editor, or use the pencil icon on any file.
- **Steps 4 to 6 need a ChatGPT account** with GitHub connected. Which plans include that changes over time, so check the current instructions linked in step 4.
- **Make one change per message**, so each one is easy to check and to undo.
- **Start a new chat for a new job.** A long conversation drifts.

### Before you start

- **A Xanthan portfolio on GitHub Pages** and the GitHub account that owns it.
- **A chat tool open in your browser**, such as ChatGPT, Claude or Gemini.
- **A site you admire**, for the typography and color steps.

## 1. Set up a starter site
{: .step #step-1}

If you don't have a Xanthan site yet, you can make one in about 10 minutes. Everything happens in your browser, and you don't need to install anything. The full walkthrough is in Xanthan's [Choose a Starter Site](https://xanthan-web.github.io/docs/getting-started/templates) guide. Here is the short version.

1. **Open the [starter site guide](https://xanthan-web.github.io/docs/getting-started/templates).** It describes five starter sites. For a personal site, choose **Portfolio**, which is the one used in this session. You can look at the live example and the clean starter before you decide.
2. **Click “Start with this one.”** It takes you to a step-by-step guide for the starter site you picked.
3. **Make a free GitHub account** if you don't have one. GitHub stores your site files and hosts the site for free.
4. **Click “Use this template,”** the green button on the starter site's GitHub page, then choose **Create a new repository** and name it. This copies a complete working site into your own account.
5. **Tell the site where it lives.** In your new repository, open `_config.yml` and set the `baseurl` line to match your repository's name, with a slash in front, such as `/my-portfolio`. If you named the repository `your-username.github.io`, leave it empty. A mismatch is the most common setup mistake.
6. **Publish it.** Go to **Settings**, then **Pages**. Set the branch to **main** and click **Save**. After a minute or two your site is live at the address shown there.

Bookmark two addresses: your repository on GitHub, where you edit, and your live site, which is what everyone else sees. The rest of this session starts from that site. If you already have a Xanthan portfolio, skip to step 2.

## 2. Make small first edits
{: .step #step-2}

Before you ask AI for anything, change a few things yourself. The point isn't the edits. It's learning how your starter site works, so you know what you're asking AI to change later.

1. Open your live site in one tab and your repository on GitHub in another.
2. Pick a heading on the live page and find where it is written in the repository. Notice that each page is a plain text file.
3. Click the pencil icon on that file, change a few words, and commit.
4. Reload the live site. GitHub Pages takes a minute or so to rebuild.
5. Try one more: change a link, a title or a color. Look around the repository to see where each kind of change lives.

By the end you'll know that your words and your colors are kept in different places, which is the idea the rest of the session builds on. You also have a working version to compare with if an AI change goes wrong later. Small edits like these are often faster by hand than by asking, and they cost nothing.

## 3. Start by copying and pasting
{: .step #step-3}

The first way to use AI on your site is the plainest: ask a chat tool for a change, read its answer, and copy it into your site yourself. It is slower than what comes later, and that is the reason to start here. You see exactly what the AI hands back, which teaches you what the parts of your site are called and where they live. It also teaches you the words to use in future prompts.

### Show the chat your site

A chat tool only knows what you show it, so give it your site first.

Your repository is public, so you can paste its link, such as `https://github.com/your-name/your-name.github.io`, into the chat. The chat can then read the whole site. Also name the one file you want it to work on, either by its path or by attaching it. It will use your real file names and settings instead of guessing.

If a tool can't open the link, copy the text of a file and paste it into the chat, or download the file from GitHub and attach it with the paperclip. Work on one page, or a few, at a time. It keeps the replies short and easy to check.

### Find a site to borrow from

The quickest change that makes a site feel like yours is its text. Find a site whose text you like to read. Search for “[your field] portfolio”, or browse a list such as [Bethany Works' portfolio roundup](https://bethanyworks.com/portfolio/). Look at what you like: the headings, the spacing, the way links look. Keep a note of two or three.

### Try it

The example theme uses Xanthan's default fonts, which give it a clean, modern, all-sans look. The goal is to move it toward [the example site](https://www.megkendall.com/), which pairs an elegant serif for headings with a plain sans-serif for the body text. Attach your theme file, `assets/css/themes/simple-theme.css`, and send this:

{% include prompt.html id="websites-copy-typography-example" %}

### Why the prompt is written this way

Each sentence does a job. If you write your own, keep the jobs and change the words.

- **It names a site and says what you like about it.** Saying “the text” keeps the AI looking at type and not at the whole design.
- **It says what not to copy.** You want a similar feel, not someone else's content or layout.
- **It attaches your theme file.** The AI can only edit what it has seen, and without the file it makes up names.
- **It asks for reasons.** That is how you learn, and it lets you disagree with a choice.
- **It asks for only the lines that change, with a file name on each.** You get small pieces with a destination.
- **It asks for free fonts and how to load them.** Many fonts are licensed, and loading a font is the step beginners forget.

### What came back

This is a real conversation. The prompt above was sent to ChatGPT on November 17, 2026, with `simple-theme.css` attached. This is a shortened version of its first reply.

<details class="more" markdown="1" open>
<summary>Real example: ChatGPT's first reply, shortened</summary>

I would give the Xanthan portfolio a more **editorial, typography-led feel**: refined headings, softer and more readable body text, generous spacing, and understated links. I would borrow the typographic character of the reference, not reproduce its design.

One limitation: I couldn't reliably retrieve the live CSS from megkendall.com, so I can't confirm its exact fonts or measurements. What follows is my proposed interpretation of the qualities you've described, not a claim about the site's actual typefaces.

**Fonts.** Two free Google Fonts: **Instrument Serif** for headings, a distinctive serif with a refined, literary quality, and **DM Sans** for body text, a contemporary sans-serif that keeps descriptions and navigation crisp. Headings are large and light, from about 40 to 88px depending on the level. Body text is 17px with a line height of 1.7, which makes it comfortable to read.

**Links.** Normal text-colored links with a thin underline, a little distance between the underline and the text, and a subtle hover change. Keeping the underline visible avoids relying on color alone.

**Code.** Add this line at the top of `assets/css/themes/simple-theme.css` to load the fonts:

```css
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap');
```

Then these font variables inside `:root`:

```css
--font-heading: 'Instrument Serif', Georgia, serif;
--font-body: 'DM Sans', sans-serif;
--font-mono: 'Courier New', monospace;
```

It also proposed rules for body text, headings, paragraph spacing, links, navigation, captions and small screens.
</details>

*From a real ChatGPT conversation, shortened. The wording is ChatGPT's own.*

Two things are worth noticing. The chat was honest that it couldn't read the other site's styles, so the fonts are its interpretation of “elegant and editorial,” not the site's actual fonts. For most projects that is fine, because you want the feel. If you want a closer match, attach a screenshot and ask again. The reply also comes in pieces: a line for the top of the file, lines for the middle, and rules it didn't write out. You would have to work out where each one goes.

### Ask for the whole file

So the next message asked for everything in one piece.

{% include prompt.html id="websites-complete-file" %}

Because the chat already knows what you want, a short message is enough. A complete file removes the guesswork about where each piece goes. To use it:

1. Open your theme file on GitHub's in browser code editor. 
2. Click inside the file, select everything (`Ctrl+A`, or `Cmd+A` on a Mac) and paste the chat's file over it.
3. Check that your colors are still there. The chat only kept them because it had your current file.
4. Commit, wait a minute, and reload your site with `Ctrl+Shift+R` to skip the page your browser saved.
5. If you don't like the result, open the file's **History**, pick the earlier version and restore it.

You may find a few spots that didn't change, such as card titles. The site's own more specific styles can win over a general one. Tell the chat which text didn't change and ask it to fix that part.

<div class="keypoint" markdown="1">
Name a site, and also describe the type in your own words, such as “tall, narrow headings; generous space between lines.” Each helps where the other is vague.
</div>

## 4. Let the AI make the edits itself
{: .step #step-4}

Copying and pasting works, but you are the one carrying every change from the chat to your site. The next stage removes that. You connect the chat to your repository, and the AI makes the changes itself and shows them to you for approval.

### Connect GitHub to ChatGPT

In ChatGPT's left bar, click on the option for Plugins. OpenAI's page on [connecting GitHub to ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt) has the current steps, which change from time to time. Once it is connected, you don't paste links or attach files. ChatGPT reads your whole site on its own.

### Let it make the change

1. You describe the change in plain language.
2. The AI makes it in a separate copy of your site, called a **branch**. Your live site is not touched.
3. It opens a **pull request**. That is a page on GitHub that shows what it changed, line by line, next to what was there before.
4. You read it, ask for corrections, and then accept it (called **merging**) or close it.

Nothing reaches your live site until you merge. That makes this safer than pasting, where every paste changes your site at once.

Add this to the end of any request, so each edit comes with a lesson:

{% include prompt.html id="websites-explain-change" %}

## 5. Change the colors and the mood
{: .step #step-5}

Colors work the way typography did. Say the feeling you want, and let the AI find where the colors live. A few ways to say it:

- **A palette:** “warm and a little old-fashioned,” “cool, clinical, lots of white,” “black with one bright accent.”
- **A vibe:** “like a museum label,” “like a field notebook,” or point to a site you found.
- **Exact colors:** if you know them, give the hex codes, which are six characters after a `#`, like `#D7D0C5`.

Say which colors should be readable and which should catch the eye. Readable colors are for the text people read for minutes, and they need strong contrast against the background. Eye-catching colors are for the few things you want noticed, such as links and buttons. If everything stands out, nothing does. Ask the AI to check the contrast and tell you the numbers. Body text should be at least 4.5 to 1.

{% include prompt.html id="websites-palette-example" %}

<details class="more" markdown="1" open>
<summary>Prepared example: what the AI says when it can edit your site</summary>

I've made the change on a new branch called `warm-earthy-palette` and opened a pull request for you to review.

**What I changed.** One file: your theme. I updated the six base colors, and everything else follows from them: the page, the cards, the navigation bar, the links and the hover states. I didn't touch anything else.

**Palette 1, stone and olive** (the one I applied, taken from the site you named)

| Role | Color | Contrast |
|---|---|---|
| Background | `#D7D0C5` | |
| Cards | `#EFEADF` | |
| Body text | `#3B3A26` | 7.5 to 1 |
| Headings and links | `#554B32` | 5.6 to 1 |
| Link hover | `#773E18` | 5.5 to 1 |

The olive from that site is `#676637`. It is only 3.9 to 1 against the background, which is fine for decoration but too faint for small text, so I didn't use it for links.

**Palette 2, sage and cream** is ready if you'd like to compare. Its body text is `#26332B` on `#F3EFE6` (11.5 to 1), with links in `#2F5D45` and a terracotta hover `#9A3F17`. Tell me and I'll switch the branch over.

**To undo this,** close the pull request. Your live site hasn't changed.
</details>


Notice what the reply does. It tells you which file it changed and that it touched nothing else, it checks contrast without being asked twice, and it says how to undo the change. If your tool skips any of these, ask.

<div class="keypoint" markdown="1">
Ask for two options, not one answer. Choosing between two palettes is easier than describing one perfectly.
</div>

## 6. Add something new
{: .step #step-6}

The same approach works for new features. Two ideas to try.

### A reusable project card

A card on your home page has three parts: a title, a short description and an image. Those are your content. How the card looks is the design. In Xanthan the two are kept apart: the words live in your page and the look lives in the theme. A reusable piece such as a card is called an **include**. You don't need to write one. Ask for it in plain words, and tell the AI to reuse what your site already has.

{% include prompt.html id="websites-new-include" %}

<details class="more" markdown="1" open>
<summary>Prepared example: what the AI says when it can edit your site</summary>

I've opened a pull request that adds a project card to your site. I checked your existing pieces first. You have a card for your home page, but nothing shaped like a project, so I added one new piece and reused everything else.

**What I changed.**
- Created one new reusable piece for the project card.
- Added its look to your theme, using your existing colors and fonts, so it matches the rest of your site.
- Added three placeholder cards to your Research page, so you can see it working.

**What I didn't change.** Your other pages, your navigation and your colors.

**How to edit it.** Each card's title, description and image are written on your Research page, in `research.md`. To change a card, change the words there. To add a fourth, copy one of the three and edit it. To change what every card looks like, ask me, or look for the project card section in your theme file.

**How to undo it.** Close the pull request, and none of this reaches your live site.
</details>


Once you have a card, you can build on it. A row of projects that scrolls sideways is a good next step:

{% include prompt.html id="websites-scroll-projects" %}

### Something that moves

Xanthan already includes carousels for sets of images, a slider that compares two images, and maps and scroll stories where the picture changes as you read. Look through the [component reference](https://xanthan-web.github.io/xanthan/docs/reference/) and ask for one by name. Using a piece that exists is more reliable than asking AI to invent one, because it already works with your styles.

When you want something new, such as text that fades in as you scroll, ask for one effect and say what it must never do:

{% include prompt.html id="websites-motion" %}

The limits are the important part. “Switch off for readers who prefer reduced motion” is the sort of thing the AI leaves out unless you ask.

## 7. Write down the rules once
{: .step #step-7}

An AI that can change your whole site can also change the wrong thing. You may find yourself typing the same reminders into every chat: “keep the colors in the theme,” “don't add new styles.” Instead, you can write them down once, in a short text file in your site's folder. The AI reads it at the start of every job, like a sheet of house rules for a new assistant.

Many tools look for a file named `AGENTS.md`, including Codex and GitHub Copilot. It is an ordinary text file that you can edit yourself at any time. The example portfolio will include one. It covers three things:

- **What the site is**, in a sentence or two.
- **Where things live**, so the AI doesn't have to guess.
- **What to do and what not to do.** The “don't” list is your safety net. It's the place to write down whatever has gone wrong before.

You don't have to write it from scratch. Ask the AI to draft it from your files, then read it and change it until it says what you mean.

{% include prompt.html id="websites-agent-instructions" %}

<details class="more" markdown="1" open>
<summary>Prepared example: what such a file might say</summary>

**What this site is.** A Xanthan portfolio, published on GitHub Pages.

**Where things live.** Page text is in the `.md` files in the top folder. Colors and fonts are in the theme file. Reusable pieces are in `_includes`. Navigation is in `_data/nav-top.yml`.

**Do.**
- Change colors and fonts only in the theme file, using the variables that are there.
- Reuse existing pieces and styles before making new ones.
- Keep a page's title, description and image at the top of the page.
- Tell me in plain words what you changed and how to undo it.

**Don't.**
- Don't add a new stylesheet or write styles inside a page without asking me first.
- Don't edit the `docs` folder.
- Don't change the navigation unless I ask.
- Don't delete or rename pages without asking me first.
</details>


With the file in place, you can ask for bigger changes and expect them to follow your rules. Ask for a plan before it does anything:

{% include prompt.html id="websites-agent-restructure" %}

## 8. Look before you accept
{: .step #step-8}

Whatever the AI produces, check it before it reaches your live site. Three ways to look, from simplest to most thorough:

1. **Ask what you can't tell.** “Which pages will look different after this?” “Is anything here something I didn't ask for?”
2. **See it on your own computer.** The desktop version of GitHub Copilot, or Copilot inside the free editor Visual Studio Code, can start a private copy of your site that only you can open. You click through it, check a phone-sized window, and ask for fixes while you look. Nothing is public until you accept the changes.

If you aren't happy, say so in plain words, as you would to a designer, or close the pull request. Your live site is exactly as it was. After you merge, the file's **History** on GitHub still lets you go back to any earlier version, so every experiment is safe.

<div class="keypoint" markdown="1">
Ask for a plan before the AI starts, read the pull request before you merge, and keep your do's and don'ts in a file the AI reads.
</div>

## 9. Divide the work between you and the AI
{: .step #step-9}

A site you built yourself has two kinds of work. Some changes are quicker by hand: a color code, a heading, a link. Doing those yourself is faster than writing a request, and it costs nothing. The rest is the repetitive work that AI is good at, such as recoloring a whole site, building a card, or adding a page that matches the others.

Knowing the words from this session makes both easier. You can ask for “the accent color” and not “something less blue,” and you can edit small things without asking.

This is also where the starter site pays off. Suppose you ask for a new Teaching page. A chat that can't see your site will write a fresh page with its own fonts, colors and stylesheet. It looks fine alone, but beside your other pages it has a different heading size and a different blue. Do that a few times and the site is a pile of pieces that disagree. Because a starter site gives the AI a structure to follow, new pages reuse the layouts and styles you already have.

{% include prompt.html id="websites-stay-consistent" %}

The same idea helps when a group builds a site together, such as a class archive. Xanthan's [class project starter site](https://xanthan-web.github.io/class-project-template) gives every contributor the same layouts, so ten people's pages look like one site. The [campus history](https://amaranth.unm.edu/campus-history/) site is an example. AI can help with the design here, too. Ask it to write instructions for contributors and page templates that follow your site's conventions, so new pages match without anyone having to police them.

## What to take with you
{: .step #takeaways}

<div class="takeaways" markdown="1">
Short rules to carry into your next site:

- **Start from a starter site.** AI can build a whole site, but a site it invented is hard to change. A starter site gives you something you can read and edit yourself.
- **Begin by copying and pasting.** You see exactly what the AI does, and you learn the names of your site's parts.
- **Then let the AI make the edits.** It does the tedious work, and you decide how it does it.
- **Say the feeling, then check the facts.** Describe a vibe, name a site you like, and ask for contrast numbers.
- **Change one thing at a time**, and say what the change must not do.
- **Ask what it did and how to undo it.** Every answer should teach you something.
- **Write the rules down once**, in a file the AI reads.
- **Look before you accept.** Read the pull request, and preview large changes.
- **Do the small edits yourself.** It's faster, and it's yours.
</div>

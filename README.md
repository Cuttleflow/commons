# Cuttleflow Commons — Meridian financial-lines wordings

An open library of Australian insurance policy wordings, published by Cuttleflow
Systems Pty Ltd. Read the wordings, use and adapt them under **CC BY 4.0**, and
suggest changes.

This repository is also the website: it is served by **GitHub Pages** from the
files here. `index.html` is the hub; `wordings/*.html` are the readable wordings;
`wordings/downloads/*.docx` are the branded Word originals.

> **Draft status.** Every wording here is a working draft, marked *DRAFT — SUBJECT
> TO LEGAL REVIEW — NOT FOR USE*. Nothing may be issued, quoted from, or bound
> until Wording Partner sign-off. The wordings are source material, not advice, and
> carry no warranty.

## How people take part

There are two routes, deliberately kept separate:

1. **Comment on a wording** — each wording page carries a comment thread, backed by
   GitHub Discussions. Sign in with a **GitHub account** and comment inline.
2. **Propose a change to the text** — the structured route, for those who want to
   redline exact wording, using **GitHub Issues and Pull Requests**. See
   `CONTRIBUTING.md`.

Comments and proposals never change a published wording on their own. A change is
published only after review and sign-off, and is then released as a new tagged
version.

## Identity

Both routes are GitHub-backed for now: a free **GitHub account** to comment inline or to
submit the form. That is a real barrier for some readers, and it is accepted
deliberately — it is the only identity Cuttleflow has standing today, and the
alternative (a self-hosted comment engine wired to platform SSO) is not on the critical
path to launch. Anyone who will not create an account can email a point in for a
maintainer to file on their behalf. `SETUP.md` records what adding a second path would
involve; it does not require changing the wording pages.

## Styling

The site uses the Cuttleflow estate stylesheet, `assets/meridian.css` — a verbatim copy
of `site/assets/meridian.css` in the website repository, so the Commons and
cuttleflow.com stay visually identical. Commons-only components (wording cards, the
article body, the comment block) live in `assets/commons.css`. Update the shared file by
re-copying it, never by editing it here. Fonts are self-hosted: drop the six woff2 files
into `assets/fonts/` (see that folder's README) — there are no external font requests.

## Licence

Wording text is licensed **CC BY 4.0** (`LICENSE.txt`). Attribution and trade-mark
terms are in `NOTICE.txt`. The Cuttleflow and Meridian names and brand assets are not
licensed.

## Setup

`DEPLOY-COMMONS.md` is the step-by-step runbook: publish to GitHub Pages, attach
`commons.cuttleflow.com`, turn on comments, and the three changes to make on launch day
(2 September 2026). `SETUP.md` explains why it is built this way.

The published wordings carry no change logs — version history lives in releases and
commit history.

# Standing up the Commons — commons.cuttleflow.com

Written to be followed in order. Parts 1–3 can be done today; Part 4 happens
on 2 September.

`SETUP.md` explains the reasoning behind these choices. This file is the steps.

---

## How people take part

Two routes, both landing in the same GitHub repository. No other identity
system is set up yet, and nothing here depends on one.

| Route | Needs a GitHub account? | Use it for |
| --- | --- | --- |
| **Comment inline** — the comment area under each wording | Yes | Discussion, questions, general remarks |
| **The form** — *Suggest a change* / *Raise a point* | Yes to submit | Proposing specific wording, reporting a defect |

Both are GitHub-backed. If someone will not create an account, the honest
answer for now is: email it in and you file it on their behalf. Cuttleflow
platform sign-in and an email path can be added later without changing these
pages — see the note at the end of `SETUP.md`.

---

## Before you start: what "public" means here

GitHub Pages on the free plan only serves from a **public** repository. From
the moment you push, anyone with the URL can read the eight wordings, and
anyone can fork them.

That is fine — they are CC BY 4.0 and meant to be public — but it is not the
same as being *launched*. Two things keep them quiet until 2 September:

- `robots.txt` says `Disallow: /`
- every page carries `<meta name="robots" content="noindex, nofollow">`

Readable by anyone you send the link to, invisible to search. That is the
right state for a draft that will change several times before launch. If even
that is too open, Pages works on private repos on a paid GitHub plan — say so
and I will adjust.

---

# Part 1 — Publish the site

1. Create a **public** repository called `commons` under the `cuttleflow`
   organisation. Do not add a README, licence or `.gitignore` — the files
   already have them.
2. Push the contents of the `commons/` folder to `main`. The folder
   **contents** go at the root of the new repo — `index.html` must be at the
   top level, not inside a `commons/` subfolder.
3. **Settings → Pages → Build and deployment → Source: Deploy from a
   branch**. Choose `main` and `/ (root)`. Save.
4. Wait two or three minutes, then open
   `https://cuttleflow.github.io/commons/`. You should see the index with
   eight wordings listed and the type rendering in the Meridian faces.

If the page loads as unstyled text, `assets/` did not upload. If it 404s,
Pages is still building — check the **Actions** tab.

---

# Part 2 — Point the domain at it

The `CNAME` file already contains `commons.cuttleflow.com`, so GitHub picks
the domain up on its own. You need the DNS record.

1. At your DNS provider, add a **CNAME** record:
   - **Name / host**: `commons`
   - **Value / target**: `cuttleflow.github.io`
2. Back in **Settings → Pages**, the custom domain box should already read
   `commons.cuttleflow.com`. Wait for the check to go green — usually
   minutes, occasionally an hour.
3. Tick **Enforce HTTPS** once it becomes available. It is greyed out until
   the certificate is issued; that can take up to a day.

Do this early. DNS is the one step that cannot be hurried on launch day.

---

# Part 3 — Turn on comments

Comments are GitHub Discussions, displayed on the page by giscus. Nothing to
host, nothing to pay for, no server to keep alive.

1. **Settings → General → Features** and tick **Discussions**.
2. In the Discussions tab, create a category called **Wordings**. Set its
   format to **Announcement** — that way only maintainers start threads and
   comments attach to the right wording.
3. Install the giscus app: <https://github.com/apps/giscus> → Install →
   select only the `commons` repository.
4. Go to <https://giscus.app>, enter `cuttleflow/commons`, choose **Discussion
   title contains page pathname** and the **Wordings** category. It will show
   you a `data-repo-id` and a `data-category-id`.
5. Paste those two values into `assets/comments.js` (the two empty strings at
   the top). Commit.
6. Open a wording and post a test comment. It should appear as a Discussion in
   the repo.

Until step 5 is done the comment area stays empty and logs one line to the
console. Nothing breaks, and the form route works from day one.

---

# Part 4 — Launch day, 2 September

Three changes, about five minutes.

1. Replace `robots.txt` with the contents of `robots.LAUNCH.txt`, then delete
   `robots.LAUNCH.txt`.
2. Delete the `<meta name="robots" content="noindex, nofollow">` line from all
   nine pages. Each is marked
   `<!-- PRELAUNCH: delete this line on 2 September -->` — search the repo for
   `PRELAUNCH`.
3. Commit. Pages rebuilds in about a minute.

Then check `https://commons.cuttleflow.com/robots.txt` reads `Allow: /`, and
view-source on one wording to confirm the noindex line is gone.

---

# Keeping wordings current

When a wording changes: update the `.docx` in `wordings/downloads/`,
regenerate `wordings/<slug>.html`, bump the version, tag a release. One
authoritative file per version.

Between now and 2 September this will happen several times. Because the site
is `noindex`, none of those intermediate drafts will be picked up by search
engines — only the state on launch day matters.

The eight published pages carry no change logs. Version history belongs in
the repo — in releases and commit history — not in the wording itself.

---

# If something goes wrong

| What you see | What it usually is |
| --- | --- |
| Page loads as unstyled text | `assets/` did not upload, or Pages source is set to the wrong folder. |
| 404 at the github.io address | Pages still building, or `index.html` is one folder too deep. |
| Custom domain stuck on "checking" | DNS. Wait an hour and retry. |
| "Enforce HTTPS" greyed out | Certificate not issued yet. Can take a day. Nothing to fix. |
| Comment area never appears | The two ids in `assets/comments.js` are still empty, or Discussions is off. |
| "giscus is not installed" in the comment box | The app is not installed on this repo, or the category name does not match. |
| Comments load but sign-in fails | The repo is private. giscus needs it public. |

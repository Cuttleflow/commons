# Standing up the Commons site — why it is built this way

`DEPLOY-COMMONS.md` has the steps. This file has the reasoning, and what to
revisit later.

Placeholders to change if anything moves: GitHub org/repo (`cuttleflow/commons`),
the two giscus ids in `assets/comments.js`, and the custom domain in `CNAME`.

## 1. Hosting: GitHub Pages, not Azure

The main estate is an Azure Static Web App. The Commons deliberately is not.
The wordings *are* the repository — the readable HTML, the `.docx` downloads, the
issue history and the pull requests are one artefact. Hosting the site from the
same repo that holds the source means there is no publish step that can drift,
and no version of a wording that exists on the site but not in git.

Consequence to accept: Pages on the free plan requires a **public** repo. That
suits CC BY 4.0 material, but it means drafts are readable from first push. The
`noindex` meta and `Disallow: /` robots keep them out of search until launch.

## 2. Participation: GitHub account, or the form

Two routes, both GitHub-backed:

- **Comment inline** — giscus, which stores comments as GitHub Discussions.
- **The form** — *Suggest a change* / *Raise a point*, which files an issue from
  a template in `.github/ISSUE_TEMPLATE/`.

Both need a GitHub account. That is a real barrier for brokers and lawyers, and
we are accepting it for now because it is the only identity we actually have
standing. The alternative — a self-hosted comment engine wired to Cuttleflow
platform SSO — needs a container, a domain, a certificate and an OIDC client
registration, none of which exist yet, and none of which should be on the
critical path to 2 September.

Practical mitigation until then: anyone who will not create an account emails
their point in, and a maintainer files it on their behalf, quoting them.

**Why giscus rather than a hosted engine:** nothing to run, nothing to pay for,
and comments end up in the same place as the change proposals. A wording
discussion and the pull request that acts on it sit side by side.

**Why Announcement format for the Discussions category:** only maintainers can
open threads, so each wording gets exactly one, mapped by pathname. Without it,
anyone can create competing threads for the same page.

## 3. Enable the change/proposal workflow

1. **Settings → General → Features** — enable **Issues** and **Discussions**.
2. Issue and pull-request templates are in `.github/` and load automatically.
3. Turn on **branch protection** for `main` (**Settings → Branches**) so nothing
   merges without review. Do this before you publicise the URL, not after.

## 4. No change logs in the published wordings

The eight pages carry no revision history, no audit-finding counts and no
references to companion change registers. Those are internal drafting artefacts:
they date the document, invite questions about findings a reader cannot see, and
duplicate what git already records precisely.

Version history lives in **releases and commit history**. When a wording
changes: update the `.docx` in `wordings/downloads/`, regenerate
`wordings/<slug>.html` (the originals were produced with `pandoc`), bump the
version, tag a release.

The DRAFT / not-for-use warnings stay on the pages — those are about the
document's status, not its history, and they matter to a reader.

## 5. When there is another identity path

Adding Cuttleflow platform sign-in later does not touch the wording pages. The
comment area is a single `<div class="giscus">` and one loader script. Swapping
in a different engine means rewriting `assets/comments.js` and nothing else —
the eight pages, the CSS and the sign-in note are already generic about *which*
account you use.

If you go that way, the shape is: a small self-hosted engine (Remark42 or
Comentario) on a cheap host behind HTTPS at `comments.cuttleflow.com`, with two
auth paths — a custom OIDC provider pointed at the platform identity, and GitHub
retained for contributors who want the pull-request route. Budget half a day,
plus a domain and certificate.

# Wording source

The wordings in this library are built from the files in this folder. The pages in
`wordings/` and the Word files in `wordings/downloads/` are build outputs: do not edit
them by hand. Edit the source, then run the build.

## Layout

```
source/<class>/
  base.yaml                 the base wording: title, version, document reference, clause order
  clauses/<id>.md           one file per clause (base clauses and profession clauses)
  professions/<slug>.yaml   one file per profession wording (added in later releases)
  changes/<wording>-<version>.md   the "Changes From" note for a release
  disclosure/<slug>.md      a Product Disclosure Statement template (Part A) for a retail wording;
                            its header pins the wording it describes, and its [[ref:...]] links must resolve in it
records/<wording>/<version>.json   build record: every clause ID with a content hash
tools/wordings/build.py     checks and build
```

## Clauses

Each clause file starts with a header:

```yaml
---
id: pi.excl.financial-services     # permanent; never reused; describes the topic, not the position
type: exclusion                    # definition | cover | extension | exclusion | payment | obligation | condition | section | preamble | claims | library | notice
heading: Financial Services         # the heading the reader sees; unique within its type in any wording
legacy_number: '3.5'               # the number the clause had in numbered versions (v1.2.0 and earlier), for tracing old references
since: 1.0.0
changed: 1.3.0
status: draft                      # draft | legal-reviewed | approved | withdrawn
---
```

The body is plain text with a small Markdown subset: paragraphs, `- ` lists, `1. ` lists,
pipe tables, `**bold**` and `*italic*`.

## Cross-references

Clauses have no numbers. To refer to another clause, write its ID:

- `[[ref:pi.excl.financial-services]]` prints "the Financial Services exclusion"
- `[[ref:pi.def.claim]]` prints "the definition of Claim"
- `[[ref:pi.cover.claims-against-you|heading]]` prints the heading only

The build takes the heading from the clause file, so renaming a heading updates every
reference. In the web page and the Word file each reference is a link to the clause.
Never type "Section 3.5", "clause 4" or a quoted heading: the checks reject clause numbers.

## Profession wordings

A profession wording is a file in `professions/` that pins an exact base version and lists
changes to it:

```yaml
id: pi-architects-engineers
title: Architects and Engineers Professional Indemnity Insurance
base: pi-base@1.3.0-DRAFT
version: 1.0.0-DRAFT
overrides:
  - op: replace           # replace a base clause with a profession clause
    target: pi.def.professional-services
    with: pi.arch.def.professional-services
  - op: add               # add a profession clause after a named clause
    clause: pi.arch.excl.cladding
    after: pi.excl.asbestos
  - op: delete            # remove a base clause that does not apply
    target: pi.ext.joint-ventures
```

The build produces the integrated profession wording from this file. Every clause the
profession does not override comes from the base, so a base change reaches every
profession wording on the next build.

## Endorsement triggers

Every endorsement (a clause of type `endorsement`) states when the platform uses it, in a
`trigger` block in its header. The platform imports these rules from the build record.

```yaml
trigger:
  questions: [qs.pi.activities.mining_pct]          # platform questions, defined in source/<class>/questions.yaml
  rules:                                  # default rules; the first rule that matches applies
    - when: qs.pi.activities.mining_pct > 10
      action: refer
    - when: qs.pi.activities.mining_pct > 0
      action: suggest
  restrictions:                           # optional; legal limits that always apply and always refer
    - when: "'VIC' in qs.pi.practice_states"
      action: refer
      note: Why the restriction exists.
  reason: Applies because {qs.pi.activities.mining_pct}% of your fees come from services to the mining industry.
  responses: [Attach, Attach with amended sub-limit, Do not attach]   # optional; what the underwriter may do on a referral or suggestion
```

`responses` lists what an underwriter may do when the endorsement is referred or suggested.
Each must be one of: Attach; Attach with amended sub-limit; Attach with special excess;
Attach with premium loading; Do not attach; Decline risk. If it is left out, the platform
offers all six.

Actions:

| Action | Platform behaviour when the rule matches |
|---|---|
| `apply` | The endorsement is attached automatically and the reason is shown to the broker before binding |
| `refer` | The quote is held for an underwriter, with the endorsement pre-selected |
| `suggest` | The underwriter sees the endorsement recommended; the quote is not held |
| `broker_option` | For endorsements that add cover: offered to the broker as a priced option |

The rules here are Cuttleflow's defaults. Each agency sets its own actions and thresholds in
its platform configuration and may choose any action. Restrictions are legal limits and are
not configurable: when one matches, the quote is referred.

The web page shows the trigger as a wording note under the endorsement. The Word file does
not include it, because the Word file is the policy document.

## Checks

`python3 tools/wordings/build.py check` stops the build when:

- a reference points to a clause that is not in the wording;
- two clauses of the same type in one wording have the same heading;
- a clause body contains a clause number ("Section 3.5", "clause 4");
- an override targets a clause that is not in the pinned base, or adds a clause that does not exist;
- a profession wording pins a base version other than the current one;
- a clause marked draft appears in a wording not marked draft;
- an endorsement has no trigger, a trigger names a question that is not in `questions.yaml`,
  a rule uses an action other than the four above, a restriction does not refer, or an
  underwriter response is not one of the six above.

The same checks run on every pull request (`.github/workflows/wordings.yml`), which also
fails if the committed pages or build records do not match the source.

## Building

```
pip install pyyaml python-docx
python3 tools/wordings/build.py build
```

This writes `wordings/<slug>.html`, `wordings/downloads/<file>_v<version>.docx` and
`records/<wording>/<version>.json`. Earlier versions of the Word file stay in
`wordings/downloads/`; one file per version.

## Versions

- The base wording and each profession wording have their own semantic version.
- A patch release of the base (typing or formatting only) flows into every profession wording.
- A minor release flows into profession wordings after the base is signed off; a profession that
  overrides a changed clause is reviewed separately.
- A major release (clauses removed or merged, structure changed) is migrated profession by profession.
- A policy is governed by the version stated in its schedule at inception. The build record for
  that version is the reference copy.

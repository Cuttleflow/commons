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

## Checks

`python3 tools/wordings/build.py check` stops the build when:

- a reference points to a clause that is not in the wording;
- two clauses of the same type in one wording have the same heading;
- a clause body contains a clause number ("Section 3.5", "clause 4");
- an override targets a clause that is not in the pinned base, or adds a clause that does not exist;
- a profession wording pins a base version other than the current one;
- a clause marked draft appears in a wording not marked draft.

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

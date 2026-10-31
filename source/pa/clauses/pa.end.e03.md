---
id: pa.end.e03
type: endorsement
heading: E03 Occupational Cover Only
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pa.cover.scope
  rules:
  - when: qs.pa.cover.scope == occupational
    action: apply
  reason: Applied because cover while working only was selected.
  responses:
  - Attach
  - Do not attach
---

The scope of cover is occupational only, as defined in [[ref:pa.def.scope-of-cover]]. [[ref:pa.cover.weekly-sickness]] is not affected.

Schedule variables: none.

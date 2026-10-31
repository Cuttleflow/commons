---
id: pa.end.e04
type: endorsement
heading: E04 Non-Occupational Cover Only
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pa.cover.scope
  rules:
  - when: qs.pa.cover.scope == non_occupational
    action: apply
  reason: Applied because cover outside work only was selected.
  responses:
  - Attach
  - Do not attach
---

The scope of cover is non-occupational only, as defined in [[ref:pa.def.scope-of-cover]]. [[ref:pa.cover.weekly-sickness]] is not affected.

Schedule variables: none.

---
id: pa.end.e11
type: endorsement
heading: E11 Capital Benefits Only
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pa.cover.weekly_cover
  rules:
  - when: qs.pa.cover.weekly_cover == no
    action: apply
  reason: Applied because only capital benefits were selected.
  responses:
  - Attach
  - Do not attach
---

[[ref:pa.cover.weekly-injury]], [[ref:pa.cover.weekly-sickness]], [[ref:pa.ext.rehabilitation]] and [[ref:pa.ext.escalation]] do not apply.

Schedule variables: none.

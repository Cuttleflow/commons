---
id: gtr.end.e09
type: endorsement
heading: E09 Domestic Travel Only
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gtr.cover.territory
  rules:
  - when: qs.gtr.cover.territory == australia_only
    action: apply
  reason: Applied because the policyholder chose cover for trips within Australia only.
  responses:
  - Attach
  - Do not attach
---

This policy covers trips within Australia only. The territory is Australia, and [[ref:gtr.cover.medical]] does not cover medical expenses for a Medicare-eligible insured person, as [[ref:gtr.pay.medicare]] provides.

Schedule variables: none.

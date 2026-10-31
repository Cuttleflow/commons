---
id: gtr.end.e07
type: endorsement
heading: E07 Increased Personal Accident Benefits
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gtr.limit.pa_capital
  rules:
  - when: qs.gtr.limit.pa_capital > 500000
    action: apply
  reason: Applied because a capital sum above the standard amount was chosen.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

The capital sum for the insured persons or categories named in the schedule for this endorsement is the amount shown for them, in place of the capital sum shown for the personal accident section, up to $2,000,000 for each insured person. The accumulation limit in [[ref:gtr.pay.accumulation]] continues to apply unless the schedule shows a higher one.

Schedule variables: insured persons or categories and their capital sums; accumulation limit.

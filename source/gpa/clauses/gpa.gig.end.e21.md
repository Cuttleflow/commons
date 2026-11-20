---
id: gpa.gig.end.e21
type: endorsement
heading: E21 Superannuation Contribution Benefit
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.gig.super_benefit
  rules:
  - when: qs.gpa.gig.super_benefit == yes
    action: apply
  reason: Applied because the platform buys a superannuation contribution benefit.
  responses:
  - Attach
  - Do not attach
---

For each week we pay you a weekly benefit, we also pay the percentage of the weekly benefit shown in the schedule (default 12%) into the complying superannuation fund you nominate. This contribution is in addition to the weekly benefit, and the percentage-of-income limit in [[ref:gpa.pay.weekly-benefit-amount]] does not apply to it.

Schedule variables: contribution percentage.

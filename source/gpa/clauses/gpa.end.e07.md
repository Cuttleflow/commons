---
id: gpa.end.e07
type: endorsement
heading: E07 Extended Benefit Period
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.policy.extended_benefit_period
  rules:
  - when: qs.gpa.policy.extended_benefit_period == yes
    action: refer
  reason: Offered because a benefit period longer than 104 weeks was requested.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

For the category named in the schedule for this endorsement, the benefit period is the period shown for this endorsement, which may be 260 weeks or to age 65, in place of the benefit period shown for the category.

Schedule variables: category; benefit period.

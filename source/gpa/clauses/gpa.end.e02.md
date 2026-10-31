---
id: gpa.end.e02
type: endorsement
heading: E02 Journey Cover
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.policy.journey_only
  rules:
  - when: qs.gpa.policy.journey_only == yes
    action: refer
  reason: Offered because journey-only cover was requested; it is outside the standard target market.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

For the category named in the schedule for this endorsement, the scope of cover is journeys only: while you are travelling directly between your home and your place of work, by a reasonably direct route, without interruption for any private purpose. [[ref:gpa.cover.weekly-sickness]] does not apply to that category.

Schedule variables: category.

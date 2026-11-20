---
id: trv.amt.end.e17
type: endorsement
heading: E17 Screened Medical Conditions
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trv.amt.screening_outcome
  rules:
  - when: qs.trv.amt.screening_outcome != none and qs.trv.amt.screening_outcome != decline
    action: apply
  reason: Applied because medical screening accepted one or more declared conditions.
  responses:
  - Attach
  - Attach with premium loading
---

[[ref:trv.excl.pre-existing-conditions]] does not apply to the conditions shown in the schedule for this endorsement, for the insured persons named. We accepted each of them after medical screening, at no extra premium or for the additional premium shown. A condition we accepted stays accepted for the rest of the policy period for every trip, unless it changes and a further trip is booked after the change without telling us.

Schedule variables: insured persons; accepted conditions; additional premium for each.

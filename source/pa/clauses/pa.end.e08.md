---
id: pa.end.e08
type: endorsement
heading: E08 Accepted Pre-existing Condition
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pa.medical.conditions_5yr
  - qs.pa.medical.condition_details
  rules:
  - when: qs.pa.medical.conditions_5yr == yes
    action: suggest
  reason: 'Suggested where the underwriter accepts the disclosed condition: {qs.pa.medical.condition_details}.'
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

The condition named in the schedule for this endorsement is not a pre-existing condition. [[ref:pa.excl.pre-existing-conditions]] does not apply to it.

Schedule variables: named condition.

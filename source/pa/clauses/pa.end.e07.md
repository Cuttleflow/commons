---
id: pa.end.e07
type: endorsement
heading: E07 Specific Condition Exclusion
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pa.medical.conditions_5yr
  - qs.pa.medical.condition_details
  rules:
  - when: qs.pa.medical.conditions_5yr == yes
    action: refer
  reason: 'Offered because the insured person disclosed a medical condition in the last 5 years: {qs.pa.medical.condition_details}.'
  responses:
  - Attach
  - Do not attach
  - Decline risk
---

We do not pay any benefit for disablement or an event caused by, or contributed to by, the condition named in the schedule for this endorsement, or by any complication of it.

Schedule variables: named condition; any period after which this endorsement stops applying.

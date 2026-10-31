---
id: trv.end.e01
type: endorsement
heading: E01 Pre-existing Medical Conditions
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trv.medical.preexisting
  rules:
  - when: qs.trv.medical.preexisting == yes
    action: refer
  reason: Offered because a traveller declared a pre-existing condition; acceptance needs medical assessment.
  responses:
  - Attach
  - Attach with premium loading
  - Attach with special excess
  - Do not attach
---

[[ref:trv.excl.pre-existing-conditions]] does not apply to the conditions shown in the schedule for this endorsement, for the insured persons named, after our medical assessment. We may accept a condition at no extra premium, for an additional premium, or with a higher excess for claims arising from it.

Schedule variables: insured persons and accepted conditions; any additional excess.

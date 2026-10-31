---
id: gtr.end.e01
type: endorsement
heading: E01 Pre-existing Medical Conditions
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gtr.medical.preexisting_declared
  rules:
  - when: qs.gtr.medical.preexisting_declared == yes
    action: refer
  reason: Offered because the policyholder declared a traveller's pre-existing condition; acceptance needs medical underwriting.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

[[ref:gtr.excl.pre-existing-conditions]] does not apply to the conditions of the insured persons named in the schedule for this endorsement, to the extent the schedule shows, provided the insured person had not been advised to avoid travel and was not travelling to obtain treatment.

Schedule variables: insured persons and accepted conditions; any limit for claims arising from each accepted condition.

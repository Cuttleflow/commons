---
id: cpo.end.e11
type: endorsement
heading: E11 Under-insurance Waiver
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.cpo.condition.valuation_current
  rules:
  - when: qs.cpo.condition.valuation_current == yes
    action: broker_option
  reason: A current valuation of the building is held.
  responses:
  - Attach
  - Do not attach
---

[[ref:cpo.pay.average]] does not apply, provided the building sum insured is at least the reinstatement value shown in a valuation of the building made by a qualified valuer within 3 years before the start of the policy period, and you have given us that valuation.

Schedule variables: valuation date and valuer.

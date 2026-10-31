---
id: bpk.end.e06
type: endorsement
heading: E06 Increased Property in Physical or Legal Control
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.bpk.liability.property_in_care_value
  rules:
  - when: qs.bpk.liability.property_in_care_value > 1000000
    action: refer
  - when: qs.bpk.liability.property_in_care_value > 250000
    action: suggest
  reason: Considered because you hold others' property worth up to ${qs.bpk.liability.property_in_care_value}.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

The property in physical or legal control sub-limit in [[ref:bpk.liability.additional-benefits]] is increased to the amount shown in the Schedule.

Schedule variables: property in control sub-limit; special excess (optional).

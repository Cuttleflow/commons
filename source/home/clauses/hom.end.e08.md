---
id: hom.end.e08
type: endorsement
heading: E08 Agreed Value
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.hom.cover.building_sum_insured
  rules:
  - when: qs.hom.cover.building_sum_insured > 2500000
    action: refer
  reason: Referred because the building sum insured is ${qs.hom.cover.building_sum_insured}, above the Go limit.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The building is insured for the agreed value shown in the schedule for this endorsement. If the building is destroyed, we pay the agreed value, whatever the cost of rebuilding, and the safety net in [[ref:hom.pay.building-settlement]] does not apply. For partial damage, [[ref:hom.pay.building-settlement]] applies up to the agreed value.

Schedule variables: agreed value (no default); date of valuation.

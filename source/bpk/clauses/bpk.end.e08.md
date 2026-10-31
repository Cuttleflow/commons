---
id: bpk.end.e08
type: endorsement
heading: E08 Minor Contract Works
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.bpk.situation.works_contract_value
  rules:
  - when: qs.bpk.situation.works_contract_value > 250000
    action: refer
  - when: qs.bpk.situation.works_contract_value > 0
    action: suggest
  reason: Considered because building works worth ${qs.bpk.situation.works_contract_value} are under way at a Situation.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:bpk.pd.exclusions]] does not exclude Damage to property under construction at a Situation where the contract value is no more than the amount shown in the Schedule for this Endorsement.

Schedule variables: Situations; maximum contract value.

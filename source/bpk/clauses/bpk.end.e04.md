---
id: bpk.end.e04
type: endorsement
heading: E04 Equipment Damage Consequential Loss
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.bpk.equipment.breakdown_bi_wanted
  rules:
  - when: qs.bpk.equipment.breakdown_bi_wanted == yes
    action: broker_option
  reason: Offered because you asked for loss of profit cover after equipment breakdown.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

[[ref:bpk.section.equipment]] is extended to loss of gross profit and increased cost of working following Breakdown covered under [[ref:bpk.equipment.cover]], for the indemnity period and up to the sub-limit shown in the Schedule. [[ref:bpk.excl.consequential-loss]] does not apply to this cover.

Schedule variables: indemnity period; sub-limit.

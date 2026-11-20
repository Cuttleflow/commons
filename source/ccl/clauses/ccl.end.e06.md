---
id: ccl.end.e06
type: endorsement
heading: E06 Increased Accumulation
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.ccl.operations.depot_max_value
  rules:
  - when: qs.ccl.operations.depot_max_value > 1000000
    action: refer
  reason: Applies because the most you hold at one depot is ${qs.ccl.operations.depot_max_value}.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The accumulation limit at the depot named in the schedule is the amount shown in the schedule for this endorsement, instead of the amount [[ref:ccl.ext.accumulation]] sets. The depot must be locked and alarmed, or attended, whenever goods are held there.

Schedule variables: the depot; the accumulation limit there.

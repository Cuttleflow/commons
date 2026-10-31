---
id: ppl.end.e13
type: endorsement
heading: E13 Vibration and Removal of Support
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.ppl.ops.excavation_depth_m
  - qs.ppl.ops.demolition
  rules:
  - when: qs.ppl.ops.excavation_depth_m > 3 or qs.ppl.ops.demolition == yes
    action: refer
  - when: qs.ppl.ops.excavation_depth_m > 0
    action: broker_option
  reason: Offered because you excavate to {qs.ppl.ops.excavation_depth_m} metres.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

[[ref:ppl.excl.vibration-and-support]] does not apply, if before the work started you:

- had a dilapidation survey made of buildings and structures within the zone of influence of the work, where a prudent contractor would; and
- followed the design and any monitoring required by a qualified engineer for excavation deeper than the depth shown in the schedule for this endorsement.

The sub-limit and special excess shown for this endorsement apply. We do not cover cosmetic cracking of less than 2 millimetres in width that does not affect the structural integrity of the building.

Schedule variables: sub-limit (any one occurrence and aggregate); special excess; excavation depth threshold (default 3 metres).

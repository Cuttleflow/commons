---
id: trd.end.e03
type: endorsement
heading: E03 Excavation Depth
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trd.ops.excavation
  - qs.trd.ops.max_depth_m
  rules:
  - when: qs.trd.ops.max_depth_m > 3
    action: refer
  - when: qs.trd.ops.excavation == yes
    action: apply
  reason: Applies because you excavate, trench or bore. Work deeper than 3 metres is referred to an underwriter.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Decline risk
---

[[ref:trd.section.liability|heading]] does not cover liability arising from excavation, trenching, boring, piling or tunnelling deeper than the depth limit shown for this endorsement below the natural ground level.

Schedule variables: depth limit (default: 3 metres).

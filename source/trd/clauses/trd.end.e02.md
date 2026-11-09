---
id: trd.end.e02
type: endorsement
heading: E02 Work at Height
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trd.ops.max_height_m
  rules:
  - when: qs.trd.ops.max_height_m > 15
    action: refer
  - when: qs.trd.ops.max_height_m >= 0
    action: apply
  reason: Applies to every trade at the height limit shown. Work above 15 metres is referred to an underwriter.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Decline risk
---

[[ref:trd.section.liability|heading]] does not cover liability arising from work you carry out at a height above the height limit shown for this endorsement, measured from the ground or floor below to the place where the work is done.

This endorsement does not apply to personal injury or property damage caused by a tool or material that falls from a height at or below the height limit.

Schedule variables: height limit (default: 15 metres).

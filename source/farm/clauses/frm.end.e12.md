---
id: frm.end.e12
type: endorsement
heading: E12 Farm Gate Sales and Markets
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.frm.ops.direct_sales
  rules:
  - when: qs.frm.ops.direct_sales == yes
    action: apply
  reason: Applies because the farm business sells produce direct to the public.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

When you sell farm produce direct to the public, at the farm gate, at markets or at shows and field days, you must hold any registration or licence that the food safety law of the state or territory requires for the produce you sell, and label it as that law requires.

The special excess applies to each claim for personal injury caused by produce you sold direct to the public. If a condition of this endorsement was not met, [[ref:frm.cond.insurance-contracts-act]] applies.

Schedule variables: special excess (default: $1,000).

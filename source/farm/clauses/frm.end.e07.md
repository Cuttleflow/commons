---
id: frm.end.e07
type: endorsement
heading: E07 Hay and Fodder Storage
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.frm.produce.hay_stored
  rules:
  - when: qs.frm.produce.hay_stored == yes
    action: apply
  reason: Applies because the farm business stores hay or fodder.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

When you store hay, silage, straw or fodder at the farm location:

- bale hay only when it is dry enough for its type, and monitor the temperature of stacks of new-season hay regularly for the first six weeks after baling;
- keep each stack in the open at least the stack separation distance from farm buildings, other stacks, fuel stores and power lines; and
- keep a firebreak around each stack in the open during the fire danger season.

The special excess applies to each claim for spontaneous combustion of farm produce. If a condition of this endorsement was not met, [[ref:frm.cond.insurance-contracts-act]] applies.

Schedule variables: stack separation distance (default: 20 metres); special excess (default: $2,500).

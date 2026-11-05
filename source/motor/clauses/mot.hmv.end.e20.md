---
id: mot.hmv.end.e20
type: endorsement
heading: E20 Tipping Operations
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.hmv.vehicles.tipper
  rules:
  - when: qs.hmv.vehicles.tipper == true
    action: apply
  reason: Applies because you told us a vehicle is a tipper or has a body that is raised to unload.
  responses:
  - Attach
  - Attach with special excess
  - Do not attach
---

This Endorsement applies to each Insured vehicle shown in the Schedule as a tipper, or fitted with a hook-lift, roll-on roll-off or other body that is raised to unload. For those vehicles, the tipping excess in [[ref:mot.hmv.cond.excess]] is the amount shown for this Endorsement in the Schedule. Liability arising from tipping at a work site remains excluded as use of the vehicle as a Tool of trade.

Schedule variables: vehicles; tipping excess.

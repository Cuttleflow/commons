---
id: mpc.end.e08
type: endorsement
heading: E08 Extended Navigation Limits
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.mpc.navigation.area
  rules:
  - when: qs.mpc.navigation.area == offshore_beyond
    action: refer
  reason: Referred because the boat will be taken beyond the standard navigation limits.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The navigation limits are extended to the waters shown in the schedule for this endorsement, for the period shown, provided the boat carries the crew and safety equipment shown. The suspension of cover when the boat clears Australian customs in [[ref:mpc.excl.navigation]] does not apply to a passage to a destination shown.

Schedule variables: extended waters and destinations; period; crew and safety equipment.

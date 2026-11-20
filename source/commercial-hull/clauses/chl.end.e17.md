---
id: chl.end.e17
type: endorsement
heading: E17 High-Speed Vessels
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.chl.vessel.max_speed
  rules:
  - when: qs.chl.vessel.max_speed > 35
    action: refer
  reason: Applies because the vessel can travel at more than 35 knots.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Decline risk
---

For a vessel capable of more than 35 knots:

- the master must hold any high-speed endorsement or training the national law requires for the vessel;
- passengers must be seated, and briefed on holding on and on the vessel's motion, whenever it travels faster than 25 knots; and
- the special excess shown in the schedule applies to each claim under [[ref:chl.section.pi|heading]] for a passenger.

[[ref:chl.cond.insurance-contracts-act]] applies to these conditions.

Schedule variables: special excess (default $10,000).

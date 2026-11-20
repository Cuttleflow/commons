---
id: chl.end.e06
type: endorsement
heading: E06 Overnight Passengers
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.chl.operations.overnight_passengers
  rules:
  - when: qs.chl.operations.overnight_passengers == true
    action: refer
  reason: Applies because passengers sleep on board.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Decline risk
---

Where passengers sleep on board:

- the vessel may carry no more passengers overnight than its certificate of operation allows for berthed passengers;
- the smoke and fire detection and alarm systems the national law requires must be working; and
- a crew member must be awake and on watch throughout the night while the vessel is under way or at anchor.

[[ref:chl.cond.insurance-contracts-act]] applies to these conditions.

Schedule variables: maximum berthed passengers.

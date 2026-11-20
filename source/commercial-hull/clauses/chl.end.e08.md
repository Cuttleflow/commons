---
id: chl.end.e08
type: endorsement
heading: E08 Swing Mooring
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.chl.vessel.mooring
  rules:
  - when: qs.chl.vessel.mooring == SWING_MOORING
    action: apply
  reason: Applies because the vessel is kept on a swing mooring.
---

Where the vessel is kept on a swing mooring:

- the mooring must be approved by the authority that manages the mooring area for a vessel of the vessel's size and weight; and
- the mooring must be inspected and serviced by a competent person at least once every 12 months, and you must keep the record of each inspection.

[[ref:chl.cond.insurance-contracts-act]] applies to these conditions.

Schedule variables: mooring location and authority.

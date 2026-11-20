---
id: mpc.end.e05
type: endorsement
heading: E05 Swing Mooring in Northern Waters
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.mpc.storage.method
  - qs.mpc.storage.zone
  rules:
  - when: qs.mpc.storage.method == swing_mooring and qs.mpc.storage.zone == northern
    action: refer
  reason: Referred because the boat is kept on a swing mooring in northern waters during the cyclone season.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The exclusion of damage by a named cyclone to a boat on a swing mooring in northern waters during the cyclone season, in [[ref:mpc.excl.moorings-and-rigging]], does not apply, provided the mooring meets the specification shown in the schedule for this endorsement and was inspected by a qualified mooring contractor within the period shown. The named cyclone excess under [[ref:mpc.end.e04]] applies.

Schedule variables: mooring specification; inspection period (default 12 months).

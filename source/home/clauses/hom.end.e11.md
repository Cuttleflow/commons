---
id: hom.end.e11
type: endorsement
heading: E11 Unoccupied Home
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.hom.occupancy.unoccupied_over_60_days
  rules:
  - when: qs.hom.occupancy.unoccupied_over_60_days == yes
    action: refer
  reason: Referred because the home has been, or will be, unoccupied for more than 60 days.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

[[ref:hom.excl.unoccupied]] does not apply until the date shown in the schedule for this endorsement, provided someone inspects the home at least every 14 days and keeps it secure.

Schedule variables: date cover for unoccupancy ends (no default).

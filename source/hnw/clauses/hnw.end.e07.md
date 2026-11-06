---
id: hnw.end.e07
type: endorsement
heading: E07 Unoccupied Home
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.hnw.occupancy.unoccupied_over_100_days
  rules:
  - when: qs.hnw.occupancy.unoccupied_over_100_days == yes
    action: refer
  reason: Referred because the home has been, or will be, unoccupied for more than 100 days.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

[[ref:hnw.excl.unoccupied]] does not apply until the date shown in the schedule for this endorsement, provided someone inspects the home at least every 14 days, the alarm is set and monitored, and the home is kept secure.

Schedule variables: date cover for unoccupancy ends (no default).

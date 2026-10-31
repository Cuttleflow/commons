---
id: str.end.e10
type: endorsement
heading: E10 Unoccupied Building
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.str.occupancy.unoccupied
  rules:
  - when: qs.str.occupancy.unoccupied == yes
    action: refer
  reason: Referred because the building is unoccupied.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:str.excl.unoccupied-building]] does not apply for the period shown in the schedule for this endorsement, if you inspect the building at least every 14 days, keep it secured, and turn off the water supply where it is safe to do so. [[ref:str.cond.insurance-contracts-act]] applies to these steps.

Schedule variables: unoccupied period; special excess.

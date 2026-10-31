---
id: mot.end.e17
type: endorsement
heading: E17 Courtesy Vehicle Fleets
since: 3.0.0
status: draft
trigger:
  questions:
  - qs.mot.use.courtesy_fleet
  rules:
  - when: qs.mot.use.courtesy_fleet == true
    action: refer
  reason: Referred because lending vehicles to customers is part of your business.
  responses:
  - Attach
  - Attach with special excess
  - Do not attach
---

Where lending vehicles is part of your business, [[ref:mot.fleet.courtesy-vehicles]] applies to the number of courtesy vehicles shown in the Schedule, and a customer driving one with your permission is an Insured person. You must check and copy each customer's licence before lending a vehicle.

Schedule variables: maximum number of courtesy vehicles; additional excess.

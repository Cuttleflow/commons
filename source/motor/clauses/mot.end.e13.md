---
id: mot.end.e13
type: endorsement
heading: E13 Interstate Long-Haul
since: 3.0.0
status: draft
trigger:
  questions:
  - qs.mot.use.radius
  rules:
  - when: qs.mot.use.radius == 'interstate'
    action: apply
  reason: Applies because vehicles operate interstate.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

For Insured vehicles used on interstate long-haul routes, we also pay, after loss or damage covered by [[ref:mot.section.vehicle-cover]] more than 500 km from the vehicle's garaging address, the reasonable cost of roadside assistance, the driver's accommodation and return travel, and a relief driver to complete the trip, up to the amount shown in the Schedule for each Occurrence.

Schedule variables: limit each Occurrence.

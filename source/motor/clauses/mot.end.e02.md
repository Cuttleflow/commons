---
id: mot.end.e02
type: endorsement
heading: E02 Refrigerated Vehicles
since: 3.0.0
status: draft
trigger:
  questions:
  - qs.mot.vehicles.refrigerated_count
  rules:
  - when: qs.mot.vehicles.refrigerated_count > 0
    action: broker_option
  reason: Offered because {qs.mot.vehicles.refrigerated_count} vehicle(s) are refrigerated.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

For each Insured vehicle shown in the Schedule as refrigerated, we pay for the spoilage of goods carried in it caused by the failure of its refrigeration unit following loss or damage covered by [[ref:mot.section.vehicle-cover]], or following a mechanical or electrical breakdown of the refrigeration unit, up to the amount shown in the Schedule for each Occurrence. We do not pay for spoilage caused by the unit being switched off, a failure to maintain it, or a delay in delivery alone.

Schedule variables: vehicles covered; spoilage limit each Occurrence; spoilage excess.

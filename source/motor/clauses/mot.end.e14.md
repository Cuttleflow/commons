---
id: mot.end.e14
type: endorsement
heading: E14 Electric and Hybrid Vehicles
since: 3.0.0
status: draft
trigger:
  questions:
  - qs.mot.vehicles.ev_count
  rules:
  - when: qs.mot.vehicles.ev_count > 0
    action: apply
  reason: Applies because {qs.mot.vehicles.ev_count} vehicle(s) are electric or hybrid.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

For each Insured vehicle that is electric or hybrid, [[ref:mot.section.vehicle-cover]] includes Accidental loss or damage to its traction battery, and to charging equipment you own at the garaging address and portable charging cables, up to the amount shown in the Schedule; and [[ref:mot.cover.third-party-property-damage]] extends to liability arising from charging the vehicle. We do not pay for loss of battery capacity through age or use.

Schedule variables: charging equipment limit.

---
id: isr.end.lion
type: endorsement
heading: LION Lithium-ion Batteries and Energy Storage
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.risk.lithium
  rules:
  - when: qs.isr.risk.lithium == 'storage_system_over_threshold'
    action: refer
  - when: qs.isr.risk.lithium == 'charging_or_storage'
    action: suggest
  reason: Suggested because lithium-ion batteries are charged or stored at a Situation.
---

Where lithium-ion batteries are charged or stored at a Situation:

- keep charging areas for forklifts, e-bikes, scooters and power tools clear of combustible materials for the distance shown in the Schedule, or separate them by fire-rated construction;
- remove or isolate damaged, faulty or recalled batteries promptly; and
- install any battery energy storage system larger than the capacity shown in the Schedule as its manufacturer and AS/NZS 5139 require, and declare it to us.

If the Schedule shows a battery deductible, it applies to Damage caused by a fire that starts in a battery or its charging equipment.

Schedule variables: clearance distance; storage system capacity threshold (kWh); battery deductible (optional).

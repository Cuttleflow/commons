---
id: mot.end.e09
type: endorsement
heading: E09 Large Fleet Excess Layer
since: 3.0.0
status: draft
trigger:
  questions:
  - qs.mot.fleet.vehicle_count
  rules:
  - when: qs.mot.fleet.vehicle_count >= 50
    action: suggest
  reason: Suggested because the fleet has {qs.mot.fleet.vehicle_count} vehicles.
  responses:
  - Attach
  - Attach with special excess
  - Do not attach
---

For claims under [[ref:mot.section.vehicle-cover]], you bear each claim up to the self-insured amount shown in the Schedule, in place of the basic excess, and we pay the amount above it. Where the Schedule shows an aggregate, once the self-insured amounts you have borne in the Period of Insurance reach the aggregate, the basic excess applies to later claims instead.

Schedule variables: self-insured amount each claim; annual aggregate.

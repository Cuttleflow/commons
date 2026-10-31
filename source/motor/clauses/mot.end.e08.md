---
id: mot.end.e08
type: endorsement
heading: E08 Novated Lease Vehicles
since: 3.0.0
status: draft
trigger:
  questions:
  - qs.mot.vehicles.novated_count
  rules:
  - when: qs.mot.vehicles.novated_count > 0
    action: apply
  reason: Applies because {qs.mot.vehicles.novated_count} vehicle(s) are held under a novated lease.
  responses:
  - Attach
  - Do not attach
---

For each Insured vehicle shown in the Schedule as held under a novated lease, the employee named for it is an Insured person and the vehicle's Permitted use includes their private use. The lessor named is an interested party under [[ref:mot.cond.subrogation-and-interested-parties]]. Where the employee leaves your employment, cover for the vehicle continues until the end of the Period of Insurance or until the lease is assigned, whichever is earlier.

Schedule variables: vehicles covered; employee; lessor.

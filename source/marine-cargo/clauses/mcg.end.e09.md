---
id: mcg.end.e09
type: endorsement
heading: E09 Storage in Transit
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.mcg.ops.storage_over_7_days
  rules:
  - when: qs.mcg.ops.storage_over_7_days == yes
    action: refer
  reason: Referred because goods are stored for more than 7 days in the course of inland transits.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

For inland transits, storage of the goods in the course of transit at the places shown in the schedule for this endorsement is insured for up to the number of days shown, despite the 7 day limit in [[ref:mcg.cover.duration]].

The limit any one conveyance applies to each place of storage. It is a condition of this cover that each place of storage is a closed building, locked when unattended.

Schedule variables: places of storage; maximum number of days (default 30); limit at each place.

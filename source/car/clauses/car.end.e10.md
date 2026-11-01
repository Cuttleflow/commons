---
id: car.end.e10
type: endorsement
heading: E10 Increased Offsite Storage and Transit
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.car.s1.offsite_transit_limit
  rules:
  - when: qs.car.s1.offsite_transit_limit > 2000000
    action: refer
  - when: qs.car.s1.offsite_transit_limit > 500000
    action: broker_option
  reason: Considered because offsite storage or transit above $500,000 was asked for.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

The limit in [[ref:car.ext.offsite-and-transit]] is replaced by the amounts shown in the schedule for this endorsement, for any one location and any one conveyance.

Schedule variables: limit for any one location; limit for any one conveyance.

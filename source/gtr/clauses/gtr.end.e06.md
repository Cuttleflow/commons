---
id: gtr.end.e06
type: endorsement
heading: E06 Long-Term Assignment
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gtr.trips.max_duration
  rules:
  - when: qs.gtr.trips.max_duration == over_90
    action: refer
  reason: Offered because a trip will be longer than the maximum trip duration.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

The maximum trip duration in [[ref:gtr.cover.trip]] is extended, for the insured persons named in the schedule for this endorsement, to the period shown for each of them. While on that assignment, the place they live is not their home for the purposes of this policy.

Schedule variables: insured persons, destinations and assignment periods (up to 12 months).

---
id: trv.end.e04
type: endorsement
heading: E04 Annual Multi-Trip
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trv.trip.type
  rules:
  - when: qs.trv.trip.type == annual
    action: refer
  reason: Offered because annual multi-trip cover was chosen.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

This policy covers every trip that starts during the 12-month period shown in the schedule, each for no longer than the maximum trip length shown for this endorsement. The limits apply to each trip, except the cancellation limit, which applies to each trip and to the period in total as the schedule shows. [[ref:trv.cond.cancellation]] refunds the premium in proportion to the unexpired period.

Schedule variables: period; maximum trip length (30, 45, 60 or 90 days).

---
id: trv.end.e06
type: endorsement
heading: E06 One-Way Trip or Working Holiday
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trv.trip.one_way
  rules:
  - when: qs.trv.trip.one_way == yes
    action: refer
  reason: Offered because the trip does not return to Australia.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

The trip need not end in Australia. Cover ends when you arrive at your final destination shown in the schedule, or on the return date shown, whichever is earlier. [[ref:trv.excl.business-travel]] does not apply to casual work in hospitality, retail, tourism or office work on a working holiday visa.

Schedule variables: final destination; whether working holiday applies.

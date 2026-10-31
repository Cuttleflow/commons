---
id: pa.end.e10
type: endorsement
heading: E10 Extended Overseas Cover
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pa.overseas.days_abroad
  rules:
  - when: qs.pa.overseas.days_abroad > 90
    action: refer
  reason: Offered because a trip of {qs.pa.overseas.days_abroad} days outside Australia is planned.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

In [[ref:pa.obl.residence-and-travel]], the number of days shown in the schedule for this endorsement replaces 90 days, for travel to the countries named.

Schedule variables: number of days; countries named, or worldwide.

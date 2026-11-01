---
id: me.end.e07
type: endorsement
heading: E07 Increased Sub-limits
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.me.cover.sublimit_increase
  rules:
  - when: qs.me.cover.sublimit_increase == yes
    action: broker_option
  reason: Offered because you asked for higher sub-limits.
---

One or more of the sub-limits in [[ref:me.pay.sub-limits]] are increased to the amounts shown in the schedule.

Schedule variables: sub-limits and amounts.

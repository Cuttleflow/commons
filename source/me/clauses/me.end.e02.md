---
id: me.end.e02
type: endorsement
heading: E02 Defence Costs in Addition
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.me.cover.defence_costs_in_addition
  rules:
  - when: qs.me.cover.defence_costs_in_addition == yes
    action: broker_option
  reason: Offered because you asked for defence costs in addition to the limit.
---

[[ref:me.pay.defence-costs]] is amended so that defence costs are payable in addition to the limit of liability, up to the separate defence costs limit shown in the schedule.

Schedule variables: defence costs limit.

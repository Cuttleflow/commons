---
id: xol.end.e04
type: endorsement
heading: E04 Defence Costs in Addition to the Limit
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.xol.underlying.defence_costs_basis
  rules:
  - when: qs.xol.underlying.defence_costs_basis == 'within'
    action: broker_option
  reason: Offered because the followed policy pays defence costs within its limit.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

Where the followed policy pays defence costs within its limit, we will pay defence costs in addition to the limit of liability, in the proportion that our payment of loss bears to the total loss, up to the defence costs sub-limit shown in the schedule for this endorsement. If no sub-limit is shown, the sub-limit is equal to the limit of liability. The attachment point is still reached only as [[ref:xol.cover.attachment-and-exhaustion]] provides.

Schedule variables: the defence costs sub-limit.

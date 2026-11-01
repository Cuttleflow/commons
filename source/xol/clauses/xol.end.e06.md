---
id: xol.end.e06
type: endorsement
heading: E06 Multi-year Underlying
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.xol.underlying.multi_year
  rules:
  - when: qs.xol.underlying.multi_year == true
    action: suggest
  reason: Suggested because the followed policy has a period longer than twelve months.
  responses:
  - Attach
  - Do not attach
---

Where the followed policy has a period longer than the policy period, this policy follows the followed policy as it was at its own inception, as shown in the schedule, for the whole of the policy period. A single aggregate underlying limit that runs across more than one policy period of this policy is counted towards the attachment point in each policy period only for loss paid in that policy period, unless [[ref:xol.end.e03]] applies.

Schedule variables: the followed policy's period and inception date.

---
id: xol.end.e07
type: endorsement
heading: E07 USA and Canada
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.xol.exposure.usa_canada
  rules:
  - when: qs.xol.exposure.usa_canada == true
    action: refer
  reason: Referred because you have exposure to claims brought in the USA or Canada.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

Where the followed policy covers claims brought in the USA or Canada, or claims to enforce a judgment made there, this policy follows that cover, subject to the separate attachment point, if any, and the sub-limit shown in the schedule for this endorsement, which is part of and not in addition to the limit of liability. Without this endorsement, this policy does not cover any such claim.

Schedule variables: the USA and Canada attachment point, if different; the sub-limit.

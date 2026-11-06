---
id: hnw.end.e08
type: endorsement
heading: E08 Short-Stay Letting
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.hnw.occupancy.short_stay
  rules:
  - when: qs.hnw.occupancy.short_stay == yes
    action: refer
  reason: Referred because the home is let for short stays.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

You may let the home, or part of it, for stays of less than three months while your household is away, for up to the number of nights a year shown in the schedule for this endorsement. Theft and malicious damage by a guest are covered, subject to the special excess shown in the schedule for this endorsement, and [[ref:hnw.excl.liability-business]] does not apply to that letting. Valuables are not covered while a guest is staying, unless they are kept in a locked safe or a vault.

Schedule variables: nights a year (default 60); special excess (default $5,000).

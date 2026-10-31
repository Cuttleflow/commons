---
id: hom.end.e05
type: endorsement
heading: E05 Short-Stay Letting
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.hom.occupancy.short_stay
  rules:
  - when: qs.hom.occupancy.short_stay == yes
    action: refer
  reason: Referred because the home is let for short stays.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

You may let the home, or part of it, for stays of less than three months while your household is away, for up to the number of nights a year shown in the schedule for this endorsement. Theft and malicious damage by a guest are covered, subject to the special excess shown in the schedule for this endorsement, and [[ref:hom.excl.liability-business]] does not apply to that letting.

Schedule variables: nights a year (default 60); special excess (default $1,000).

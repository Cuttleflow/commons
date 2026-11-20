---
id: ccl.end.e09
type: endorsement
heading: E09 Extended Storage
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.ccl.operations.storage_over_30_days
  rules:
  - when: qs.ccl.operations.storage_over_30_days == true
    action: refer
  reason: Applies because you hold goods at a depot for more than 30 days.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

Goods held at a depot named in the schedule are covered for up to the number of days shown in the schedule for this endorsement, instead of 30 days, on the terms of the sections that apply. The depot must be locked and alarmed, or attended, whenever goods are held there.

Schedule variables: the depot; the number of days (default 90).

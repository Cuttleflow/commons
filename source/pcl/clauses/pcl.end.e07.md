---
id: pcl.end.e07
type: endorsement
heading: E07 Unoccupied Premises
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pcl.premises.unoccupied_over_60_days
  rules:
  - when: qs.pcl.premises.unoccupied_over_60_days == yes
    action: refer
  reason: Referred because the premises are, or will be, unoccupied for more than 60 days.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:pcl.excl.unoccupied]] does not apply for the period shown in the schedule for this endorsement, if during that period:

- the premises are inspected inside and outside by you or a person you choose at least once in every number of days shown in the schedule for this endorsement; and
- any alarm shown in the schedule is switched on whenever the premises are empty.

Schedule variables: period; inspection interval in days (default 7).

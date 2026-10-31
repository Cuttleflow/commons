---
id: gpa.end.e16
type: endorsement
heading: E16 Specific Condition Exclusion
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.history.condition_exclusions
  rules:
  - when: qs.gpa.history.condition_exclusions == yes
    action: refer
  reason: Offered because a covered person needs benefits above the free cover limit and has disclosed a medical condition.
  responses:
  - Attach
  - Do not attach
---

We do not pay any benefit to the covered person named in the schedule for this endorsement for disablement or an event caused by, or contributed to by, the condition named, or by any complication of it.

Schedule variables: covered person; named condition; any period after which this endorsement stops applying.

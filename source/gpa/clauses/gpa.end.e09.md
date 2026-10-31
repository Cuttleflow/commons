---
id: gpa.end.e09
type: endorsement
heading: E09 Weekly Benefits to Age 70
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.policy.weekly_over_65
  rules:
  - when: qs.gpa.policy.weekly_over_65 == yes
    action: refer
  reason: Offered because weekly benefits are needed for covered persons aged 65 or older.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

For the category named in the schedule for this endorsement, in [[ref:gpa.pay.age-limits]], 70th birthday replaces 65th birthday for weekly benefits.

Schedule variables: category.

---
id: pa.end.e09
type: endorsement
heading: E09 Weekly Benefits to Age 70
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pa.cover.weekly_to_age_70
  - qs.pa.insured.age
  rules:
  - when: qs.pa.cover.weekly_to_age_70 == yes or qs.pa.insured.age >= 65
    action: refer
  reason: Offered because weekly benefits are needed after age 65.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

In [[ref:pa.pay.age-limits]], 70th birthday replaces 65th birthday for weekly benefits.

Schedule variables: none.

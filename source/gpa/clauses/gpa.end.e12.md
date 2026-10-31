---
id: gpa.end.e12
type: endorsement
heading: E12 Key Person Top-Up
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.policy.key_persons
  rules:
  - when: qs.gpa.policy.key_persons > 0
    action: refer
  reason: Offered because {qs.gpa.policy.key_persons} key persons need higher benefits than their category.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

For the covered persons named in the schedule for this endorsement, the capital sum and weekly benefit shown for each of them replace those of their category. We must accept each named person in writing.

Schedule variables: named persons; capital sum and weekly benefit for each.

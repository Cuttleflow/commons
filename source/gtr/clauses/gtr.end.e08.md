---
id: gtr.end.e08
type: endorsement
heading: E08 Non-Employee Travellers
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gtr.persons.non_employees
  rules:
  - when: qs.gtr.persons.non_employees == yes
    action: apply
  reason: Applied because people other than employees and named contractors will travel at the policyholder's cost.
  responses:
  - Attach
  - Do not attach
---

Consultants, board advisers and guests travelling on your business, at your cost and with your authority, are insured persons, for the categories shown in the schedule for this endorsement. Weekly benefits under [[ref:gtr.cover.personal-accident]] do not apply to them.

Schedule variables: categories of non-employee travellers; maximum number on any one trip.

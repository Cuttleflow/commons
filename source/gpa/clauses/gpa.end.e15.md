---
id: gpa.end.e15
type: endorsement
heading: E15 Students
since: 1.0.0
changed: 1.1.0
status: draft
trigger:
  questions:
  - qs.gpa.pertype.students
  rules:
  - when: qs.gpa.pertype.students > 0
    action: apply
  reason: Applied because the policyholder covers {qs.gpa.pertype.students} enrolled students.
  responses:
  - Attach
  - Do not attach
---

The category named in the schedule for this endorsement covers enrolled students of the policyholder. For them:

- the scope of cover is the scope shown for this endorsement: 24 hours a day, or school activities only (while at the school, at activities it organises, and while travelling directly to and from them);
- weekly sickness benefits do not apply, and weekly injury benefits do not apply unless the schedule shows them; and
- the capital sum for a student under 18 is the reduced amount shown for this endorsement.

The premium for this category is a rate per enrolled student.

Schedule variables: number of enrolled students (or the declaration basis); scope; capital sum; reduced capital sum for those under 18 (default $50,000).

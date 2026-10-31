---
id: pi.et.end.increased-reassessment
type: endorsement
heading: Increased Re-assessment Sub-limit
profession: education-training
since: 1.0.0
status: draft
note: Adds cover.
trigger:
  questions:
  - qs.pi.et.enrolments
  rules:
  - when: qs.pi.et.enrolments > 1000
    action: broker_option
  reason: Offered because large enrolments raise the cost of re-assessing students.
---

The sub-limit for [[ref:pi.et.ext.reassessment-costs]] is increased to the amount shown in the schedule for this endorsement.

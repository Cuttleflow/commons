---
id: gpa.end.e11
type: endorsement
heading: E11 Workers Compensation Top-Up
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.policy.wc_top_up
  rules:
  - when: qs.gpa.policy.wc_top_up == yes
    action: apply
  reason: Applied because weekly benefits are to top up workers compensation.
  responses:
  - Attach
  - Do not attach
---

For the categories named in the schedule for this endorsement, while you are entitled to weekly payments under a workers compensation law for an injury, the weekly benefit for that injury is the amount by which the lower of the weekly benefit and the percentage of income in [[ref:gpa.pay.weekly-benefit-amount]] exceeds those payments. Outside working hours, and once workers compensation payments stop, the weekly benefit applies in full.

Schedule variables: categories.

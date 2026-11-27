---
id: nur.end.e04
type: endorsement
heading: E04 Deterioration of Stock Conditions
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.nur.cover.deterioration
  rules:
  - when: qs.nur.cover.deterioration == yes
    action: apply
  reason: Applies because you chose Deterioration of Stock cover.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

This endorsement sets conditions for [[ref:nur.section.deterioration|heading]].

- Where a climate control system has an alarm that warns of a failure, a loss of power or a temperature outside its set range, keep the alarm switched on and set to alert you or an employee who can respond, and test it at least every 3 months.
- Where the schedule shows backup power, keep the generator or other backup power maintained, and test it under load at least every 3 months.
- Have each climate control system serviced as its maker recommends, and at least once a year, and keep the service records.

If a condition of this endorsement was not met, [[ref:nur.cond.insurance-contracts-act]] applies.

Schedule variables: backup power (default: not shown).

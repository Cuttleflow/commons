---
id: isr.end.mony
type: endorsement
heading: MONY Money
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.risk.cash_handling
  rules:
  - when: '''MONY'' in qs.isr.cover.options_requested'
    action: broker_option
  - when: qs.isr.risk.cash_handling == yes
    action: suggest
  reason: Suggested because the business handles cash.
---

We cover loss of Money, as the Base Wording defines it, up to the sub-limits shown in the Schedule for each of these: in transit; at a Situation during business hours; in a locked safe or strongroom at a Situation outside business hours; and at the home of an authorised employee. We do not pay for shortages caused by error or omission; loss from an unattended vehicle; loss caused by the dishonesty of an employee; or electronic funds and digital currency. Keep a record of Money in transit and in safes, and remove safe keys from the Situation outside business hours.

Schedule variables: sub-limit for each location type.

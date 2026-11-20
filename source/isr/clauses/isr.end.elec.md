---
id: isr.end.elec
type: endorsement
heading: ELEC Electronic Equipment Breakdown
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  rules:
  - when: '''ELEC'' in qs.isr.cover.options_requested'
    action: broker_option
  reason: Offered as an option for electronic equipment breakdown.
---

We cover sudden and unforeseen physical Damage to computers, servers, process control systems, telecommunications and other electronic equipment at a Situation, caused by electrical or electronic breakdown, including power surge, up to the sub-limit shown in the Schedule. We do not pay for faults in software or data (see CYBX and DATA); wear and tear; consumable parts; or costs a maintenance contract should meet.

Schedule variables: sub-limit; deductible.

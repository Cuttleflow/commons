---
id: isr.end.incd
type: endorsement
heading: INCD Incidents at the Premises
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.risk.anzsic_division
  rules:
  - when: '''INCD'' in qs.isr.cover.options_requested'
    action: broker_option
  - when: qs.isr.risk.anzsic_division in ['H', 'P', 'Q']
    action: suggest
  reason: Suggested for hospitality, education and health care businesses.
---

We cover Business Interruption loss from the closure or restriction of a Situation, ordered by a competent authority because of:

- murder, suicide or serious assault at the Situation;
- food or drink poisoning caused by food or drink provided at the Situation; or
- vermin, pests or defective sanitation at the Situation.

We do not cover loss arising from a disease that is the subject of an order or declaration applying generally to a region, a state or territory, or Australia. Cover is limited to the sub-limit and the maximum period shown in the Schedule, and the sub-limit is the most we pay in the aggregate for the Period of Insurance.

Schedule variables: aggregate sub-limit; maximum period; waiting period.

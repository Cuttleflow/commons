---
id: isr.end.escl
type: endorsement
heading: ESCL Escalation of Declared Values
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.values.oldest_valuation_years
  rules:
  - when: '''ESCL'' in qs.isr.cover.options_requested'
    action: broker_option
  - when: qs.isr.values.oldest_valuation_years > 1
    action: suggest
  reason: Suggested because a Situation's valuation is more than 12 months old.
---

For the co-insurance test, the Declared Value for each Situation increases each day of the Period of Insurance by a daily proportion of the escalation percentage shown in the Schedule. If the Schedule says so, the Limit of Liability increases in the same way. We do not charge additional premium for escalation during the Period of Insurance.

Schedule variables: escalation percentage a year; whether it applies to the Limit of Liability.

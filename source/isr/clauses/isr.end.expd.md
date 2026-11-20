---
id: isr.end.expd
type: endorsement
heading: EXPD Expediting Expenses and Temporary Repairs
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.bi.insured
  rules:
  - when: '''EXPD'' in qs.isr.cover.options_requested'
    action: broker_option
  - when: qs.isr.bi.insured == no
    action: suggest
  reason: Suggested because business interruption is not insured.
---

We pay the reasonable extra cost of making temporary repairs to Damaged property, and of speeding up its permanent repair or replacement, including overtime, night and weekend work, and express or air freight, up to the sub-limit shown in the Schedule. We do not pay the same cost twice under this endorsement and the Business Interruption cover.

Schedule variables: sub-limit.

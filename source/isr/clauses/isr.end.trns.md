---
id: isr.end.trns
type: endorsement
heading: TRNS Transit within Australia
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.risk.transit_over_threshold
  rules:
  - when: qs.isr.risk.transit_over_threshold == yes
    action: refer
  - when: '''TRNS'' in qs.isr.cover.options_requested'
    action: broker_option
  reason: Offered because the business moves goods within Australia.
---

The Material Damage cover extends to insured property, other than Money, while in transit within Australia by road, rail, inland waterway, coastal shipping between Australian ports, or air, including loading, unloading and incidental storage for up to the period shown in the Schedule. The most we pay for any one conveyance is the sub-limit shown. We do not pay for Damage caused by insufficient packing by you or your employees; delay or loss of market; ordinary leakage or shrinkage; or theft from an unattended vehicle unless it was locked and the theft followed forcible entry.

Schedule variables: sub-limit per conveyance; incidental storage period (default 7 days).

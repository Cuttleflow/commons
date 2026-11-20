---
id: isr.end.biip
type: endorsement
heading: BIIP Indemnity Periods by Situation and Item
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.bi.indemnity_periods_differ
  rules:
  - when: qs.isr.bi.indemnity_periods_differ == yes
    action: apply
  reason: Applies because indemnity periods differ between Situations or items.
---

The indemnity period for Business Interruption loss resulting from Damage at a Situation is the period shown in the Schedule for that Situation and insured item, starting when the Damage occurs. Where the Schedule shows an extended indemnity period for named plant, that period applies to loss resulting from Damage to that plant. Where an extension has its own indemnity period in the Schedule, that period applies to the extension if it is shorter.

Schedule variables: indemnity period per Situation and item; extended period and named plant (optional).

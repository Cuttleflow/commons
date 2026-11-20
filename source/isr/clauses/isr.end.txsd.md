---
id: isr.end.txsd
type: endorsement
heading: TXSD Time Excess (Deducted)
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.bi.time_excess_basis
  rules:
  - when: qs.isr.bi.time_excess_basis == 'deducted'
    action: apply
  reason: Applies because the agency deducts the time excess rather than using a threshold.
---

This endorsement replaces any provision of the Base Wording under which a waiting period, once passed, allows loss to be measured from the start of the interruption. For each interruption we do not pay Business Interruption loss arising in the time excess shown in the Schedule, measured from the Damage or other event that triggers the cover. We pay the loss after that time. The time excess applies to each Event at each Situation.

Schedule variables: time excess (hours or days) for the main cover and each extension.

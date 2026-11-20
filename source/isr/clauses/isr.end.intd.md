---
id: isr.end.intd
type: endorsement
heading: INTD Interdependency between Situations
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.policy.situation_count
  - qs.isr.bi.insured
  rules:
  - when: qs.isr.policy.situation_count > 1 and qs.isr.bi.insured == yes
    action: apply
  reason: Applies because business interruption is insured at more than one Situation.
---

Where Damage at one Situation interrupts the business at another Situation, the Business Interruption loss at every affected Situation is covered as if the Damage had happened at each of them. The indemnity period for each affected Situation applies.

Schedule variables: none.

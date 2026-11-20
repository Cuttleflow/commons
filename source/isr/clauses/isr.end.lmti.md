---
id: isr.end.lmti
type: endorsement
heading: LMTI How Limits and Sub-limits Interact
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.policy.base_wording
  rules:
  - when: qs.isr.policy.base_wording != 'meridian'
    action: apply
  reason: Applies because the base wording does not have the Meridian rules on how limits interact.
---

- Where more than one limit or sub-limit could apply to the same Damage or loss, the higher one applies, not their total. A sub-limit that the Schedule marks "most we pay" applies instead, whatever other provision might apply.
- A sub-limit stated "per Event" applies once to all Damage and loss from one Event. A sub-limit stated "in the aggregate" is the most we pay for all such Damage and loss during the Period of Insurance.
- A sub-limit stated "in addition" is paid on top of the Limit of Liability. Every other sub-limit is part of it.
- Where more than one Deductible could apply to Damage from one Event at one Situation, only the highest applies.

Schedule variables: for each sub-limit, its basis (per Event, in the aggregate, in addition, most we pay).

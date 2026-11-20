---
id: isr.end.eqke
type: endorsement
heading: 'EQKE Earthquake: 72-Hour Event and Deductible'
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.policy.situation_count
  rules:
  - when: qs.isr.policy.situation_count >= 1
    action: apply
  reason: Applies to every policy to add earthquake cover with the 72-hour rule and an earthquake deductible.
---

We cover Damage caused by earthquake, subterranean fire or volcanic eruption, and fire or explosion resulting from them, and Business Interruption loss resulting from that Damage. Any earth movement exclusion in the Base Wording does not apply to that Damage; it continues to apply to subsidence, settlement and landslip.

- All such Damage within any 72 consecutive hours is one Event. You may choose when each 72-hour period starts, but no two periods may overlap.
- The earthquake deductible shown in the Schedule applies to each Situation for each Event, instead of any other Deductible. It may be a fixed amount, or a percentage of the Declared Value of the Situation with a minimum and a maximum.

Schedule variables: earthquake deductible (amount, or percentage with minimum and maximum).

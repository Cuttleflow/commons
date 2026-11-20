---
id: isr.end.aggp
type: endorsement
heading: AGGP Annual Aggregates for Specified Perils
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.binder.aggregate_required
  - qs.isr.peril.multi_situation_high_hazard
  rules:
  - when: qs.isr.binder.aggregate_required == yes
    action: apply
  - when: qs.isr.peril.multi_situation_high_hazard == yes
    action: suggest
  reason: Suggested because more than one Situation is in a high-hazard zone for the same peril, or required by the binder.
---

For each peril named in the Schedule for this endorsement (for example flood, earthquake, named cyclone or bushfire), the aggregate shown is the most we pay for all Damage and all Business Interruption loss caused by that peril during the Period of Insurance, at all Situations combined. Each payment reduces the remaining aggregate. AREI does not restore these aggregates unless the Schedule says so.

Schedule variables: perils and aggregate amounts.

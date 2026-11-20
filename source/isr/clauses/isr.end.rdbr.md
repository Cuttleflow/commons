---
id: isr.end.rdbr
type: endorsement
heading: 'RDBR Removal of Debris: Increased Limit'
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.risk.pre_1990_building
  - qs.isr.risk.hazardous_goods
  rules:
  - when: '''RDBR'' in qs.isr.cover.options_requested'
    action: broker_option
  - when: qs.isr.risk.pre_1990_building == yes
    action: suggest
  - when: qs.isr.risk.hazardous_goods == yes
    action: suggest
  reason: Suggested because a building pre-dates 1990 or hazardous goods are stored, which raises debris costs.
---

The sub-limit for removal of debris under the Base Wording is increased to the amount shown in the Schedule. Removal of debris costs are the reasonable costs you incur, following Damage covered by this Policy, to demolish, dismantle, shore up or prop up the Damaged property; to remove, store and dispose of its debris; and to clean up pollutants or contaminants at the Situation released by that Damage. We do not pay to clean up pollutants or contaminants beyond the boundary of the Situation, or costs an authority requires where there is no Damage covered by this Policy. Asbestos-containing debris is dealt with under ASBS.

Schedule variables: sub-limit; whether it is in addition to the Limit of Liability.

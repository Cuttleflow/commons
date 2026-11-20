---
id: isr.end.cnwk
type: endorsement
heading: CNWK Alterations, Additions and Contract Works
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.risk.works_over_limit
  - qs.isr.risk.works_contract_value
  rules:
  - when: qs.isr.risk.works_over_limit == yes
    action: refer
  - when: qs.isr.risk.works_contract_value > 0
    action: apply
  reason: Applies because building works are planned or under way at a Situation.
---

The Material Damage cover extends to Damage to alterations, additions, renovations and repairs being carried out at a Situation, including materials on site for them, where the total contract value of the project is not more than the contract works limit shown in the Schedule. Any provision of the Base Wording that excludes property in the course of construction does not apply to these works. We do not cover contractors' plant and equipment that you do not own; liquidated damages or penalties for delay; or works insured under a separate contract works policy. If the contract requires it, your contractor's interest in the works is noted.

Schedule variables: contract works limit per project.

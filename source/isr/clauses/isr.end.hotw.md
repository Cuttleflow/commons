---
id: isr.end.hotw
type: endorsement
heading: HOTW Hot Work
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.risk.combustible_panel_pct
  - qs.isr.risk.works_contract_value
  - qs.isr.risk.anzsic_division
  rules:
  - when: qs.isr.risk.combustible_panel_pct > 0
    action: apply
  - when: qs.isr.risk.works_contract_value > 0
    action: apply
  - when: qs.isr.risk.anzsic_division in ['C', 'I']
    action: suggest
  reason: Applies because building works are planned or a building has combustible core panels; suggested for manufacturing and warehousing.
---

**Hot work** means welding, cutting, grinding, brazing, soldering, use of open flame, or other work that produces sparks or heat capable of igniting materials. Hot work at a Situation, by you or your contractors, outside an area designed for it, must be done under a written permit that requires:

- combustible materials within the distance shown in the Schedule to be removed or protected;
- suitable fire extinguishers at hand;
- a fire watch during the work and for the period shown after it ends; and
- a final check of the area before it is left.

If the Schedule shows a hot work deductible, it applies to Damage caused by hot work done without such a permit.

Schedule variables: clearance distance (default 10 metres); fire watch period after work (default 60 minutes); hot work deductible (optional).

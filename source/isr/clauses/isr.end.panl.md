---
id: isr.end.panl
type: endorsement
heading: PANL Combustible Core Panels
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.risk.combustible_panel_pct
  rules:
  - when: qs.isr.risk.combustible_panel_pct > 0
    action: refer
  reason: Referred because a building has combustible core panels.
---

In this endorsement, a **combustible core panel** is an insulated sandwich panel or other composite panel with a core of expanded or extruded polystyrene, polyurethane, polyisocyanurate or another combustible material, unless the panel is certified to the fire performance standard shown in the Schedule.

For Damage by fire at a Situation where combustible core panels make up more than the percentage shown in the Schedule of the walls, ceilings or roof of the building in which the fire starts or to which it spreads:

- the panel deductible shown applies instead of the standard Deductible; and
- if the Schedule shows a panel sub-limit, it is the most we pay for that Situation.

This endorsement does not apply at a Situation the Schedule shows as protected by automatic sprinklers, while they are in working order.

Schedule variables: fire performance standard (for example FM 4880 or LPS 1181); panel percentage threshold; panel deductible; panel sub-limit (optional); sprinkler exemption (yes or no).

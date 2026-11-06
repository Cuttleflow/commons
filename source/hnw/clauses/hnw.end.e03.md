---
id: hnw.end.e03
type: endorsement
heading: E03 Bushfire-Prone Home
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.hnw.property.bushfire_attack_level
  rules:
  - when: qs.hnw.property.bushfire_attack_level == bal_40 or qs.hnw.property.bushfire_attack_level == bal_fz
    action: refer
  reason: Referred because the home is on land with a bushfire attack level of BAL-40 or BAL-FZ.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The home is on land with the bushfire attack level shown in the schedule for this endorsement. For damage caused by bushfire, the special excess shown in the schedule for this endorsement applies in place of the basic excess.

Keep gutters clear of leaves, and keep the land within 20 metres of the building clear of dead vegetation and stored fuel, as the bushfire authority for the area recommends. This is not a condition of cover: [[ref:hnw.cond.insurance-contracts-act]] applies, and we may reduce a claim only to the extent that not doing so caused or added to the damage.

Schedule variables: bushfire attack level; bushfire excess (no default).

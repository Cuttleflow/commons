---
id: mcg.end.e01
type: endorsement
heading: E01 Temperature-Controlled Goods
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.mcg.goods.temperature_controlled
  rules:
  - when: qs.mcg.goods.temperature_controlled == yes
    action: refer
  reason: Referred because the goods include temperature-controlled goods; the underwriter sets the terms for refrigeration breakdown.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

This endorsement applies to goods that must be kept within a temperature range during transit, as described in the schedule for this endorsement.

We cover loss of or damage to those goods caused by a change in temperature that results from the breakdown of the refrigerating machinery or the insulation of the conveyance or container, where the breakdown lasts for at least the period shown in the schedule for this endorsement. This cover applies whatever the cover level shown in the schedule, and despite the exclusions in the Institute Clauses for inherent vice and for delay, to the extent of the change in temperature only.

It is a condition of this cover that:

- the goods are in sound condition and at the required temperature when the transit starts;
- the refrigerating machinery is set to the required temperature, and you keep, or ask the carrier to keep, a temperature record for the transit; and
- the goods are carried by a professional carrier, or in your own vehicle fitted with a working temperature alarm.

We do not cover loss or damage caused by the goods being packed or loaded at the wrong temperature, by the machinery being switched off or set wrongly by you or your employees, or by a failure to supply power that lasts less than the period shown.

Schedule variables: goods and temperature range; minimum breakdown period (default 24 hours); special excess.

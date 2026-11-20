---
id: isr.end.dtst
type: endorsement
heading: DTST Deterioration of Stock
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.risk.temperature_controlled_stock
  rules:
  - when: '''DTST'' in qs.isr.cover.options_requested'
    action: broker_option
  - when: qs.isr.risk.temperature_controlled_stock == yes
    action: suggest
  reason: Suggested because the business keeps temperature-controlled stock.
---

We cover deterioration, putrefaction or spoilage of stock kept in a temperature-controlled environment at a Situation, up to the sub-limit shown in the Schedule, caused by:

- a rise or fall in temperature resulting from Damage covered by this Policy, or from breakdown of the refrigeration or control plant, whether or not MBRK applies;
- the failure of the public electricity supply, other than a deliberate act of the supply authority, unless the Schedule includes deliberate acts; or
- contamination by refrigerant escaping from the plant.

We do not pay where the temperature change lasts less than the time excess shown; for stock past its use-by date; or for incorrect temperature settings. Keep the refrigeration and control plant maintained as its manufacturer recommends, with a working temperature alarm. The Insurance Contracts Act 1984 (Cth), including its section 54, applies to this condition.

Schedule variables: sub-limit; time excess (hours); deliberate acts of supply authority included (yes or no).

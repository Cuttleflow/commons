---
id: isr.end.glas
type: endorsement
heading: GLAS Glass
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.risk.anzsic_division
  rules:
  - when: '''GLAS'' in qs.isr.cover.options_requested'
    action: broker_option
  - when: qs.isr.risk.anzsic_division == 'G'
    action: suggest
  reason: Suggested because the business is a retailer with shopfront glass.
---

For accidental breakage of fixed glass, mirrors, glass signs and glass shopfronts at a Situation, the glass deductible shown in the Schedule applies instead of the standard Deductible. We also pay the reasonable cost of temporary boarding up, removing and refixing fittings, and replacing lettering or decoration on the broken glass, up to the sub-limit shown. We do not pay for glass that was cracked or defective at the start of the Period of Insurance, or breakage during alteration, repair or removal.

Schedule variables: glass deductible; sub-limit for associated costs.

---
id: isr.end.attr
type: endorsement
heading: ATTR Loss of Attraction
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.risk.in_shopping_centre
  rules:
  - when: '''ATTR'' in qs.isr.cover.options_requested'
    action: broker_option
  - when: qs.isr.risk.in_shopping_centre == yes
    action: suggest
  reason: Suggested because a Situation is in a shopping centre.
---

We cover Business Interruption loss when Damage, by a cause this Policy would cover, to property within the radius shown in the Schedule, or to an attraction named in the Schedule (for example the anchor tenant of a shopping centre), reduces the number of customers coming to the Situation, even though the Situation is not damaged and access to it is not prevented. Cover is limited to the sub-limit and maximum period shown.

Schedule variables: radius or named attractions; sub-limit; maximum period; waiting period.

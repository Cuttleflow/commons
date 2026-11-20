---
id: isr.end.xcor
type: endorsement
heading: 'XCOR Extra Cost of Reinstatement: Increased Limit'
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.risk.building_over_20_years
  - qs.isr.risk.combustible_cladding
  rules:
  - when: '''XCOR'' in qs.isr.cover.options_requested'
    action: broker_option
  - when: qs.isr.risk.combustible_cladding == yes
    action: suggest
  - when: qs.isr.risk.building_over_20_years == yes
    action: suggest
  reason: Suggested because a building is more than 20 years old or has combustible cladding.
---

The sub-limit for the extra cost of reinstatement is increased to the amount shown in the Schedule. Extra cost of reinstatement is the additional cost of reinstating Damaged property to comply with laws, regulations, building codes and the requirements of any authority in force when the reinstatement is carried out. It includes work on undamaged parts of a Damaged building where that work is needed for the reinstated building to comply. We do not pay for a requirement you were notified of before the Damage; fines or penalties; or any cost if the property is not reinstated, unless reinstatement is prevented by law.

Schedule variables: sub-limit.

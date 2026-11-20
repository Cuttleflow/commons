---
id: isr.end.fusn
type: endorsement
heading: FUSN Fusion
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.risk.refrigeration_or_pumping
  rules:
  - when: '''FUSN'' in qs.isr.cover.options_requested'
    action: broker_option
  - when: qs.isr.risk.refrigeration_or_pumping == yes
    action: suggest
  reason: Suggested because the business relies on refrigeration or pumping motors.
---

We cover Damage to electric motors, generators, transformers and other electrical apparatus, including their windings, caused by their own burning out, short-circuit or electrical overload, up to the sub-limit shown in the Schedule for any one item. We do not pay for wear and tear or routine maintenance.

Schedule variables: sub-limit per item; deductible.

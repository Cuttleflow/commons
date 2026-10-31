---
id: hom.end.e06
type: endorsement
heading: E06 Specified Valuables
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.hom.cover.specified_valuables
  rules:
  - when: qs.hom.cover.specified_valuables > 25000
    action: refer
  - when: qs.hom.cover.specified_valuables > 0
    action: apply
  reason: Applies because valuables of ${qs.hom.cover.specified_valuables} are to be specified.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

Each item listed in the schedule for this endorsement is covered for its stated value, in place of the limits in [[ref:hom.pay.contents-limits]], for loss or damage by any sudden and accidental cause, anywhere in the world. We may replace the item, or pay its stated value or the cost of replacement, whichever is less.

Schedule variables: each item, its description and its stated value.

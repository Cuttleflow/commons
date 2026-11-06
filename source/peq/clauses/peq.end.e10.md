---
id: peq.end.e10
type: endorsement
heading: 'E10 Unspecified Plant: Increased Item Limit'
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.peq.cover.unspecified_item_max
  rules:
  - when: qs.peq.cover.unspecified_item_max > 100000
    action: refer
  - when: qs.peq.cover.unspecified_item_max > 25000
    action: apply
  reason: Applies because unspecified plant items of up to {qs.peq.cover.unspecified_item_max} each are to be insured; referred above $100,000.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

The most we pay for any one item of unspecified plant, in [[ref:peq.def.unspecified-plant]] and [[ref:peq.ext.unspecified-plant]], is increased to the amount shown in the schedule for this endorsement. The unspecified plant sum insured is not increased.

[[ref:peq.excl.unattended-theft]] continues to apply.

Schedule variables: most we pay for any one item of unspecified plant (default $50,000).

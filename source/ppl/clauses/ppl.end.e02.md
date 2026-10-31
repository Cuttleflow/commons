---
id: ppl.end.e02
type: endorsement
heading: E02 Increased Property in Your Care
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.ppl.ops.ccc_max_value
  rules:
  - when: qs.ppl.ops.ccc_max_value > 1000000
    action: refer
  - when: qs.ppl.ops.ccc_max_value > 250000
    action: broker_option
  reason: Offered because you hold up to {qs.ppl.ops.ccc_max_value} of other people's property.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

The default sub-limit in [[ref:ppl.ext.property-in-your-care]] is replaced by the sub-limit shown in the schedule for this endorsement. If the schedule shows a special excess for this endorsement, it applies to each occurrence under that extension.

Schedule variables: care, custody or control sub-limit (any one occurrence); special excess (optional).

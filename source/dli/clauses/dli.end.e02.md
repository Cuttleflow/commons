---
id: dli.end.e02
type: endorsement
heading: E02 Waterproofing in Lots
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.dli.cover.lot_waterproofing
  rules:
  - when: qs.dli.cover.lot_waterproofing == yes
    action: apply
  - when: qs.dli.cover.lot_waterproofing == no
    action: broker_option
  reason: Offered because waterproofing in lots is the most common defect in NSW apartments and may not be common property; applies when the developer chooses it.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

[[ref:dli.cover.relevant-defects]] also covers a relevant defect in the waterproofing of a wet area, balcony or planter box within a lot, whether or not that waterproofing forms part of the common property.

[[ref:dli.excl.lot-property]] does not apply to that waterproofing. We pay the rectification costs to the lot owner or, where the owners corporation arranges the rectification, to the owners corporation.

Schedule variables: limit for each lot (default $100,000), within the sum insured.

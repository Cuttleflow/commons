---
id: ppl.end.e06
type: endorsement
heading: E06 Therapeutic Goods and Medical Devices
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.ppl.products.tga_regulated
  rules:
  - when: qs.ppl.products.tga_regulated == yes
    action: refer
  reason: Referred because you supply therapeutic goods or medical devices.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The therapeutic goods part of [[ref:ppl.excl.high-hazard-products]] does not apply to the products shown in the schedule for this endorsement, if they are included in the Australian Register of Therapeutic Goods (or are exempt from inclusion) and you comply with the Therapeutic Goods Act 1989 (Cth) and any recall procedure required under it. We do not cover liability arising from a product the Therapeutic Goods Administration has cancelled, suspended or ordered to be recalled before the occurrence. The sub-limit and any special excess shown for this endorsement apply.

Schedule variables: products and ARTG numbers; sub-limit (aggregate); special excess (optional).

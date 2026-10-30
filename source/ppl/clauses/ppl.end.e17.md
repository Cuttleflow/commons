---
id: ppl.end.e17
type: endorsement
heading: E17 Product Errors and Omissions
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.ppl.products.components_pct
  - qs.ppl.products.role
  rules:
  - when: qs.ppl.products.components_pct > 50
    action: refer
  - when: qs.ppl.products.role includes manufacturer or qs.ppl.products.role includes own_brand
    action: broker_option
  reason: Offered because you manufacture or brand products.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Do not attach
---

We will pay the compensation you become legally liable to pay because your products fail to perform their intended function or to meet the level of performance, quality or fitness you warranted or represented, if:

- the claim is first made against you during the policy period and you tell us about it during the policy period; and
- the products were supplied after the retroactive date shown in the schedule for this endorsement.

[[ref:ppl.excl.product-performance]] and [[ref:ppl.excl.economic-loss]] do not apply to compensation covered by this endorsement. We do not pay the cost of repairing, replacing or refunding the products themselves, or any claim arising from a circumstance you knew of before the policy period. The most we will pay for all claims in the policy period, including defence costs, is the aggregate sub-limit shown for this endorsement. The special excess shown applies to each claim.

Schedule variables: aggregate sub-limit; retroactive date; special excess.

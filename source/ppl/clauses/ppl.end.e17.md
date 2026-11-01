---
id: ppl.end.e17
type: endorsement
heading: E17 Product Errors and Omissions
since: 2.0.0
changed: 2.1.0
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

- the claim is first made against you during the policy period and you tell us about it as set out in [[ref:ppl.cond.claims-made-endorsements]]; and
- the products were supplied after the retroactive date shown in the schedule for this endorsement.

This endorsement applies despite the words "happens during the policy period" in the covers. For compensation covered by this endorsement, the following do not apply:

- [[ref:ppl.excl.product-performance]];
- [[ref:ppl.excl.economic-loss]];
- [[ref:ppl.excl.contractual-liability]], to the extent the liability is for breach of a warranty or representation about the performance, quality or fitness of your products; and
- the fourth point of [[ref:ppl.excl.your-products-and-work]] (loss of use of tangible property that has not been physically damaged).

We do not pay the cost of repairing, replacing or refunding the products themselves, or any claim arising from a circumstance that a member of your control group knew of before the policy period. The most we will pay for all claims in the policy period, including defence costs, is the aggregate sub-limit shown for this endorsement. The special excess shown applies to each claim.

Schedule variables: aggregate sub-limit; retroactive date; special excess.

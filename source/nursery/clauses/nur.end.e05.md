---
id: nur.end.e05
type: endorsement
heading: E05 Biosecurity Destruction
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.nur.business.biosecurity_order
  rules:
  - when: qs.nur.business.biosecurity_order == yes
    action: refer
  - when: qs.nur.business.biosecurity_order == no
    action: broker_option
  reason: Offered as a priced option because this policy otherwise excludes plant stock destroyed by order under a biosecurity law. Referred if an order or direction is in force for the situation now.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

[[ref:nur.excl.government-orders]] is changed so that we pay for plant stock that is destroyed, or that you must destroy, by an order or direction under a biosecurity law made during the policy period to eradicate or contain a pest, disease or weed.

We value the plant stock as [[ref:nur.prp.plant-stock]] sets out, and deduct any compensation or reimbursement for it that you receive or are entitled to receive from a government, an industry body or a response arrangement. The most we pay in the policy period is the biosecurity sub-limit, and the special excess applies to each claim.

We do not pay where the pest, disease or weed had been found at the situation, or an order or direction about it was in force for the situation, before this endorsement was first attached. [[ref:nur.cond.insurance-contracts-act]] applies to this endorsement.

[WP REVIEW: confirm how this cover interacts with owner reimbursement costs under the Emergency Plant Pest Response Deed and with state compensation schemes, and that the deduction of compensation is enforceable as drafted.]

Schedule variables: biosecurity sub-limit (default: $50,000); special excess (default: $2,500).

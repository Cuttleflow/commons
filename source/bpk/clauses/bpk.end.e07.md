---
id: bpk.end.e07
type: endorsement
heading: E07 Product Recall Costs
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.bpk.liability.products_supplied
  rules:
  - when: qs.bpk.liability.products_supplied == manufacture_or_import
    action: broker_option
  reason: Offered because you manufacture or import the products you sell.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

[[ref:bpk.liability.excl.product-recall]] does not apply to the reasonable costs of recalling Your products following a defect that could cause Personal injury or Property damage, up to the recall sub-limit shown in the Schedule, which is an aggregate for the Period of Insurance.

Schedule variables: recall sub-limit (aggregate).

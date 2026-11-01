---
id: bpk.end.e07
type: endorsement
heading: E07 Product Recall Costs
since: 2.1.0
changed: 2.2.0
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

We pay the reasonable costs you incur, with our written agreement, to recall Your products from the market or from your customers, where you or a government authority decide during the Period of Insurance that a fault in Your products is likely to cause Personal injury or Property damage. Recall costs are the costs of notifying people of the recall, collecting and transporting the products, storing and destroying them, and the extra staff and advertising the recall needs. We pay up to the recall sub-limit shown in the Schedule, which is an aggregate for the Period of Insurance and is part of the limit of [[ref:bpk.section.liability]]. The Excess applies.

We do not pay for repairing, replacing or refunding the price of Your products, for your lost profit or loss of reputation, or for a recall that a fault a member of the Control group knew about before the Period of Insurance caused. [[ref:bpk.liability.excl.product-recall]] does not apply to the recall costs this Endorsement covers, and continues to apply to all other costs of recalling, repairing or replacing Your products.

Schedule variables: recall sub-limit (aggregate).

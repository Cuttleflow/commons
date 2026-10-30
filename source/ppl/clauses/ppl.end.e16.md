---
id: ppl.end.e16
type: endorsement
heading: E16 Product Recall Expenses
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.ppl.products.recalls_5yrs
  - qs.ppl.products.food_beverage
  - qs.ppl.products.recall_plan
  rules:
  - when: qs.ppl.products.recalls_5yrs > 0
    action: refer
  - when: qs.ppl.products.food_beverage == yes and qs.ppl.products.recall_plan == yes
    action: broker_option
  reason: Offered because you supply food or beverages and have a recall plan.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

We will pay the recall expenses you incur in recalling your products from the market, if:

- the recall is required by law, or is necessary because you or a regulator first discover during the policy period that the use of your products has caused or could cause personal injury or property damage; and
- you tell us in writing within 7 days of deciding to recall.

Recall expenses means the reasonable costs of communicating the recall, transporting, storing and destroying recalled products, and extra staff costs, incurred within 12 months of the recall decision. [[ref:ppl.excl.your-products-and-work]] does not apply to recall expenses covered by this endorsement.

We do not pay: the cost of repairing, replacing or refunding the products; loss of profit, market share or goodwill; recalls caused by the products reaching the end of their shelf life, by deterioration in normal use, or by a defect you knew of before the policy period; or recalls of products that are prohibited from sale. The most we will pay for all recalls in the policy period is the aggregate sub-limit shown for this endorsement, which is $500,000 if none is shown. The special excess shown for this endorsement applies to each recall.

Schedule variables: aggregate sub-limit (default $500,000); special excess.

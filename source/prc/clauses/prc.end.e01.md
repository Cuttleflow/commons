---
id: prc.end.e01
type: endorsement
heading: E01 Third-party Recall Costs
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.prc.products.role
  rules:
  - when: qs.prc.products.role in ['contract_manufacturer', 'ingredient_supplier']
    action: suggest
  reason: Suggested because you make products or ingredients for other brand owners, who may recover their recall costs from you.
---

We will also pay the recall costs and replacement costs that your customers incur because of an insured event in an insured product you supplied to them, to the extent you are legally liable to reimburse them, whether under contract or otherwise, up to the sub-limit shown in the schedule for this endorsement. [[ref:prc.excl.bodily-injury-and-property-damage-claims]] still applies.

Schedule variables: the sub-limit; any named customers.

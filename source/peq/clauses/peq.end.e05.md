---
id: peq.end.e05
type: endorsement
heading: 'E05 Agreed Value: All Items'
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.peq.plant.agreed_value_all
  - qs.peq.plant.valuation_held
  rules:
  - when: qs.peq.plant.agreed_value_all == yes and qs.peq.plant.valuation_held == no
    action: refer
  - when: qs.peq.plant.agreed_value_all == yes
    action: apply
  reason: Applies because all items are to be insured for an agreed value; referred where a written valuation is not held for every item.
  responses:
  - Attach
  - Do not attach
---

Every item of specified plant is insured for its agreed value, and [[ref:peq.pay.basis-of-settlement]] settles each item on that basis.

The agreed value of each item is the value in a written valuation by a licensed valuer, or a dealer's written replacement quotation for an item less than 12 months old, dated no more than 12 months before the start of the policy period, unless we agree otherwise. The agreed value is fixed for the policy period and does not change because the schedule is reissued for another reason. [[ref:peq.ext.appreciation]] does not apply.

Schedule variables: none.

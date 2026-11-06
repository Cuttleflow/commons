---
id: hnw.end.e11
type: endorsement
heading: E11 Jewellery Kept in a Safe
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.hnw.valuables.jewellery_watches_sum_insured
  rules:
  - when: qs.hnw.valuables.jewellery_watches_sum_insured > 250000
    action: apply
  reason: Applies because jewellery and watches kept at the home are insured for ${qs.hnw.valuables.jewellery_watches_sum_insured}.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

When it is not being worn, and no member of your household is at the home, keep each item of jewellery and each watch with a value of more than the amount shown in the schedule for this endorsement in a locked safe at the home or in a vault. This is not a condition of cover: [[ref:hnw.cond.insurance-contracts-act]] applies, and we may reduce a claim for theft only to the extent that the item not being in a safe or vault caused or added to the loss.

Schedule variables: value above which an item is kept in a safe (default $25,000).

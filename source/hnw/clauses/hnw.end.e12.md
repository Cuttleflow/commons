---
id: hnw.end.e12
type: endorsement
heading: E12 Item Valuations to Follow
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.hnw.valuables.valuations_outstanding
  - qs.hnw.valuables.highest_item_value
  rules:
  - when: qs.hnw.valuables.valuations_outstanding == yes and qs.hnw.valuables.highest_item_value > 50000
    action: refer
  - when: qs.hnw.valuables.valuations_outstanding == yes
    action: apply
  reason: Applies because some items worth $10,000 or more have no valuation or receipt less than three years old; above $50,000 an item it is referred.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
  - Decline risk
---

For each specified item listed in the schedule for this endorsement, you have not yet given us a professional valuation or a receipt dated within the last three years. Until you do, the most we pay for that item is the lower of its agreed value and the amount shown in the schedule for this endorsement.

Give us the valuation or receipt within the number of days after this policy starts shown in the schedule for this endorsement. When you do, this endorsement stops applying to that item.

Schedule variables: items; amount payable until valuation (default $10,000); days to give the valuation (default 60).

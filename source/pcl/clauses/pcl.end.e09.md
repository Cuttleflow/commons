---
id: pcl.end.e09
type: endorsement
heading: E09 Valuations to Follow
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pcl.collection.valuations_outstanding
  - qs.pcl.collection.highest_item_value
  rules:
  - when: qs.pcl.collection.valuations_outstanding == yes and qs.pcl.collection.highest_item_value > 50000
    action: refer
  - when: qs.pcl.collection.valuations_outstanding == yes
    action: apply
  reason: Applies because valuations for some specified items are still to be given to us.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
  - Decline risk
---

For each specified item shown in the schedule for this endorsement, give us a professional valuation, or a receipt from the seller dated within the last three years, within the number of days shown in the schedule for this endorsement (default 30) from the start of the policy period.

Until we receive it, the most we pay for that item is its agreed value or the cost to replace it with an item of the same kind and quality, whichever is less. Once we receive it, the item is covered for its agreed value, or for the value we then agree with you.

Schedule variables: items affected; days to provide the valuation (default 30).

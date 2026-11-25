---
id: pcl.end.e06
type: endorsement
heading: E06 Exhibition and Loan
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pcl.collection.loans_and_exhibitions
  rules:
  - when: qs.pcl.collection.loans_and_exhibitions == yes
    action: refer
  reason: Referred because an item is to be lent to a gallery, museum or exhibition.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The items shown in the schedule for this endorsement are covered while on loan to the gallery, museum or exhibition named in the schedule, from the time they leave the premises until they are returned to it, including while being packed, moved and hung.

If the borrower provides insurance or an indemnity for an item that covers the same damage, this policy pays only the amount that the borrower's insurance or indemnity does not pay.

Schedule variables: items lent; borrower; loan period.

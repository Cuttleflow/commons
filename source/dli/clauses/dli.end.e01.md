---
id: dli.end.e01
type: endorsement
heading: E01 Alternative Accommodation
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.dli.cover.alt_accommodation
  rules:
  - when: qs.dli.cover.alt_accommodation == yes
    action: apply
  - when: qs.dli.cover.alt_accommodation == no
    action: broker_option
  reason: Offered because a relevant defect can make lots uninhabitable while it is rectified; applies when the developer chooses it.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

Where a lot cannot be lived in while a relevant defect is being rectified, we pay the reasonable cost of alternative accommodation of a similar standard for the occupiers of that lot, and the reasonable cost of moving and storing their contents, until the lot can be lived in again.

We pay up to the limit for each lot and the aggregate limit shown in the schedule, within the sum insured. We pay the lot owner, or the occupiers where the lot owner asks us to.

Where the lot is let, we pay the lot owner's loss of rent instead of the occupiers' accommodation costs, up to the same limits.

Schedule variables: limit for each lot (default $50,000); aggregate limit (default 10% of the sum insured).

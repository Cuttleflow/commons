---
id: xol.end.e03
type: endorsement
heading: E03 Drop-down for Underlying Aggregate Exhaustion
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.xol.endorsements.dropdown_aggregate_requested
  - qs.xol.underlying.aggregate_eroded
  rules:
  - when: qs.xol.endorsements.dropdown_aggregate_requested == true
    action: refer
  reason: Referred because you asked for this layer to drop down when an aggregate underlying limit is reduced by paid loss.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

Where an aggregate underlying limit is reduced or exhausted by payment of covered loss during the policy period, the attachment point is reduced by the amount of that payment, and [[ref:xol.cover.no-drop-down]] does not apply to that extent. Where the aggregate underlying limit is exhausted, this policy responds as the first layer of insurance for that cover, subject to the deductible or excess of the followed policy, which you bear.

The most we will pay for loss in the part of the tower that this endorsement brings into cover is the drop-down sub-limit shown in the schedule, which is part of and not in addition to the limit of liability. This endorsement does not apply to a reduction caused by loss paid before the start of the policy period, unless the schedule says so.

Schedule variables: the underlying policies to which it applies; the drop-down sub-limit; whether prior-period erosion counts.

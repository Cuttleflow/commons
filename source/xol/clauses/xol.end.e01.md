---
id: xol.end.e01
type: endorsement
heading: E01 Difference in Conditions
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.xol.endorsements.dic_requested
  rules:
  - when: qs.xol.endorsements.dic_requested == true
    action: refer
  reason: Referred because you asked for cover for differences between the followed policy and other underlying insurance.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

For the differences in cover specified in the schedule for this endorsement only, [[ref:xol.cover.difference-in-conditions]] does not apply, and this policy covers loss that the other underlying insurance named in the schedule covers but the followed policy does not.

For loss covered only because of this endorsement, the attachment point is reached when the underlying limit of the policy that covers the loss has been paid as [[ref:xol.cover.attachment-and-exhaustion]] provides, and we pay no more than the sub-limit shown for this endorsement, which is part of and not in addition to the limit of liability.

Schedule variables: the specified differences; the underlying policy that covers them; the sub-limit.

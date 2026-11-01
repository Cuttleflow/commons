---
id: xol.end.e08
type: endorsement
heading: E08 Specified Exclusion Changes
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.xol.endorsements.exclusion_changes_requested
  rules:
  - when: qs.xol.endorsements.exclusion_changes_requested == true
    action: refer
  reason: Referred because you asked for changes to the exclusions of the followed policy for this layer.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

The exclusions of the followed policy named in the schedule for this endorsement apply to this policy as changed in the schedule, or do not apply, as the schedule states. A change made by this endorsement does not change the attachment point: a loss covered only because of it reaches the attachment point only if the underlying limits are paid by you or on your behalf as [[ref:xol.cover.attachment-and-exhaustion]] provides.

Schedule variables: each exclusion named; the change to it; any sub-limit.

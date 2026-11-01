---
id: xol.end.e05
type: endorsement
heading: E05 Self-insured Retention
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.xol.endorsements.sir_requested
  rules:
  - when: qs.xol.endorsements.sir_requested == true
    action: refer
  reason: Referred because you asked to retain part of the tower yourself in place of underlying insurance.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

For the cover named in the schedule for this endorsement, there is no underlying insurance in the layer shown, and you retain that layer yourself as a self-insured retention. The self-insured retention counts towards the attachment point only when you have paid it in full, or it has been paid on your behalf, in loss that would have been covered by the followed policy. You must not insure the self-insured retention without our consent.

Schedule variables: the cover; the self-insured retention amount and layer; any aggregate for the retention.

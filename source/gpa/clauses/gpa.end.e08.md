---
id: gpa.end.e08
type: endorsement
heading: E08 Corporate Travel Interface
since: 1.0.0
changed: 1.1.0
status: draft
trigger:
  questions:
  - qs.gpa.policy.corporate_travel
  rules:
  - when: qs.gpa.policy.corporate_travel == yes
    action: suggest
  reason: Suggested because the policyholder also holds a corporate travel policy.
  responses:
  - Attach
  - Do not attach
---

Where an injury to a covered person while travelling on the policyholder's business is also covered by the corporate travel policy named in the schedule for this endorsement, that policy is a specified underlying policy for the purposes of [[ref:gpa.pay.other-insurance]]. This policy pays its capital benefits in full, and pays its weekly benefits and additional benefits only for the amount that the corporate travel policy does not pay for the same benefit.

Schedule variables: the corporate travel policy number and insurer.

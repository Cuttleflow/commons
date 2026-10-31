---
id: gpa.end.e08
type: endorsement
heading: E08 Corporate Travel Interface
since: 1.0.0
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

Where an injury to a covered person while travelling on the policyholder's business is also covered by a corporate travel policy issued to the policyholder, this policy pays its capital benefits in full, and pays its weekly benefits and additional benefits only to the extent the travel policy does not pay the same benefit. Nothing in this endorsement reduces a benefit below what this policy would pay alone.

Schedule variables: the corporate travel policy number and insurer.

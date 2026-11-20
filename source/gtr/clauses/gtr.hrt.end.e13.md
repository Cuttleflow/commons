---
id: gtr.hrt.end.e13
type: endorsement
heading: E13 Security Evacuation Limit Increase
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gtr.hrt.evacuation_increase
  rules:
  - when: qs.gtr.hrt.evacuation_increase == yes
    action: refer
  reason: Referred because a higher security evacuation limit was requested.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
---

In [[ref:gtr.cover.security-evacuation]], the sub-limit for each insured person is increased to the amount shown in the schedule for this endorsement (default $250,000), and the most we pay for all insured persons in one evacuation is the event limit shown (default $1,000,000).

Schedule variables: limit for each insured person; event limit.

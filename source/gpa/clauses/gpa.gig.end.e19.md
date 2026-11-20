---
id: gpa.gig.end.e19
type: endorsement
heading: E19 Cover Across Several Platforms
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.gig.multi_platform
  rules:
  - when: qs.gpa.gig.multi_platform == yes
    action: apply
  reason: Applied because the platform buys cover for its workers' time on other platforms.
  responses:
  - Attach
  - Do not attach
---

A covered person is also covered during engaged time on platform work through the other platforms named in the schedule, as if each were the platform, and their earnings from those platforms count as income. We do not pay twice for the same injury: where another policy covers the same injury for another platform, [[ref:gpa.pay.other-insurance]] applies.

Schedule variables: other platforms.

---
id: trv.end.e15
type: endorsement
heading: E15 Senior Traveller
since: 1.0.0
changed: 1.1.0
status: draft
trigger:
  questions:
  - qs.trv.traveller.oldest_age
  rules:
  - when: qs.trv.traveller.oldest_age > 80
    action: refer
  reason: Offered because a traveller is older than 80.
  responses:
  - Attach
  - Attach with premium loading
  - Attach with amended sub-limit
  - Decline risk
---

In [[ref:trv.cover.who-is-covered]], the maximum age is 85. The overseas medical limit for an insured person aged 81 to 85 is the amount shown for this endorsement.

Schedule variables: overseas medical limit for travellers aged 81 to 85 (default $500,000).

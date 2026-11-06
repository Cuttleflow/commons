---
id: env.end.e07
type: endorsement
heading: E07 Business Interruption
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.env.site.bi_requested
  rules:
  - when: qs.env.site.bi_requested == true
    action: refer
  reason: Referred because you asked for business interruption cover at your sites.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

We will pay your loss of gross profit, and reasonable extra expense, while a covered location is wholly or partly closed because clean-up costs covered under [[ref:env.cover.site-pollution-legal-liability]] are being incurred, after the waiting period shown in the schedule and for no longer than the indemnity period shown. Once the waiting period is exceeded, loss is paid from the start of the closure. The most we will pay under this endorsement is the sub-limit shown in the schedule for it, which is part of and not in addition to the limit of liability.

Schedule variables: the covered locations; the sub-limit; the waiting period; the indemnity period.

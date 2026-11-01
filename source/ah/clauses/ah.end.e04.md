---
id: ah.end.e04
type: endorsement
heading: E04 Increased Inquiry Costs Sub-limit
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.ah.cover.inquiry_sublimit_increase
  rules:
  - when: qs.ah.cover.inquiry_sublimit_increase == yes
    action: broker_option
  reason: Offered because you asked for a higher inquiry costs sub-limit.
---

The sub-limit for [[ref:ah.ext.inquiry-costs]] is increased to the amount stated in the schedule. The sub-limit remains part of, and not in addition to, the limit of liability.

Schedule variables: inquiry costs sub-limit.

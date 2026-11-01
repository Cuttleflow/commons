---
id: tl.end.e03
type: endorsement
heading: E03 Increased Sub-limits
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.tl.cover.options_requested
  rules:
  - when: '''E03'' in qs.tl.cover.options_requested'
    action: broker_option
  reason: Offered because you asked for higher sub-limits on named covers.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

The sub-limit shown in the schedule for this endorsement replaces the standard sub-limit for each cover or extension the schedule names. The standard sub-limit applies to every cover or extension the schedule does not name.

A sub-limit increased by this endorsement is part of, and not in addition to, the limit of liability and the aggregate limit, as stated in [[ref:tl.pay.limits-of-liability]]. The retention for the cover or extension is unchanged unless the schedule shows a different retention for this endorsement.

Schedule variables: covers or extensions increased; increased sub-limit for each; retention (if different).

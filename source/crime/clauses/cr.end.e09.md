---
id: cr.end.e09
type: endorsement
heading: "E09 Financial Institution: Fiduciary Funds"
since: 2.0.0
changed: 2.1.0
status: draft
trigger:
  questions:
  - qs.cr.cover.options_requested
  rules:
  - when: "'E09' in qs.cr.cover.options_requested"
    action: broker_option
  reason: Offered because you hold client money in trust.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Do not attach
---

[[ref:cr.ext.clients-property]] is extended to cover money and securities that you hold in trust for clients in the course of your business as a fiduciary, where the loss is caused by an act covered under [[ref:cr.cover.employee-dishonesty]] or [[ref:cr.cover.funds-transfer-fraud]] and you are legally liable for it.

This endorsement does not cover loss from investment decisions, shortfalls in a trust account that cannot be traced to a specific criminal act, or loss that a regulatory compensation scheme or the trust's own insurance covers.

The sub-limit and excess shown in the schedule for this endorsement apply. The sub-limit is part of, and not in addition to, the limit of liability of the clauses it extends.

Schedule variables: sub-limit; excess; named trust accounts.

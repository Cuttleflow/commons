---
id: cr.end.e03
type: endorsement
heading: "E03 Client Property: Increased Sub-limit"
since: 2.0.0
changed: 2.1.0
status: draft
trigger:
  questions:
  - qs.cr.cover.options_requested
  rules:
  - when: "'E03' in qs.cr.cover.options_requested"
    action: broker_option
  reason: Offered because you hold property of your clients.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Do not attach
---

The sub-limit in [[ref:cr.ext.clients-property]] is increased to the amount shown in the schedule for this endorsement. The increased sub-limit is part of, and not in addition to, the limit of liability of the clause it extends.

The extension continues to apply only to property of a client that is in your care, custody or control, and only where you are legally liable for the loss.

Schedule variables: sub-limit; excess.

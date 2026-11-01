---
id: cr.end.e10
type: endorsement
heading: E10 Invoice Manipulation Fraud
since: 2.0.0
changed: 2.1.0
status: draft
trigger:
  questions:
  - qs.cr.cover.options_requested
  rules:
  - when: "'E10' in qs.cr.cover.options_requested"
    action: broker_option
  reason: Offered because you pay supplier invoices by electronic transfer.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Do not attach
---

[[ref:cr.cover.social-engineering-fraud]] is extended to cover your direct financial loss from paying a supplier invoice, in good faith, where a third party fraudulently altered the invoice or the payment details on it, or created a false invoice that purported to come from a supplier with whom you have an established business relationship.

The sub-limit shown for this endorsement applies to a payment only if, before you paid, you followed the verification procedure shown in the schedule. Where you did not, cover for that payment is not removed: it applies at the social engineering sub-limit that would apply without this endorsement. Verification therefore limits only the increase. It is not a condition of cover.

The excess shown in the schedule for this endorsement applies. The sub-limit is part of, and not in addition to, the limit of liability of [[ref:cr.cover.social-engineering-fraud]].

Schedule variables: sub-limit; excess; verification procedure.

---
id: cr.end.e10
type: endorsement
heading: E10 Invoice Manipulation Fraud
since: 2.0.0
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

The [[ref:cr.cover.social-engineering-fraud]] clause is extended to cover your direct financial loss from paying a supplier invoice, in good faith, where a third party fraudulently altered the invoice or the payment details on it, or created a false invoice that purported to come from a supplier with whom you have an established business relationship.

Cover under this endorsement is not conditional on the verification procedure shown in the schedule. Where you did not follow it and that failure caused or contributed to the loss, we may reduce our payment to the extent the failure caused or contributed to it, as s.54 of the Insurance Contracts Act 1984 (Cth) allows.

The sub-limit and excess shown in the schedule for this endorsement apply. The sub-limit is part of, and not in addition to, the limit of liability of the social engineering clause.

Schedule variables: sub-limit; excess; verification procedure.

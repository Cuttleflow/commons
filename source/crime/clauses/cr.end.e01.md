---
id: cr.end.e01
type: endorsement
heading: E01 Increased Social Engineering Sub-limit
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.cr.cover.options_requested
  rules:
  - when: "'E01' in qs.cr.cover.options_requested"
    action: broker_option
  reason: Offered because you asked for a higher limit for payments made after a fraudulent instruction.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Do not attach
---

The social engineering sub-limit for the [[ref:cr.cover.social-engineering-fraud]] clause is increased to the amount shown in the schedule for this endorsement. The increased sub-limit is part of, and not in addition to, the limit of liability of that clause and of any overall aggregate.

All losses arising from one impersonation, or from a series of related impersonations by the same person or group, are one loss. The social engineering excess shown in the schedule for this endorsement applies to each loss.

This endorsement applies only while the verification procedure shown in the schedule for this endorsement is in use. Where it was not followed and that failure caused or contributed to the loss, we may reduce our payment to the extent the failure caused or contributed to it, as s.54 of the Insurance Contracts Act 1984 (Cth) allows.

Schedule variables: social engineering sub-limit; social engineering excess; verification procedure.

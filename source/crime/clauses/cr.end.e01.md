---
id: cr.end.e01
type: endorsement
heading: E01 Increased Social Engineering Sub-limit
since: 2.0.0
changed: 2.1.0
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

The social engineering sub-limit in [[ref:cr.cover.social-engineering-fraud]] is increased to the amount shown in the schedule for this endorsement. The increased sub-limit is part of, and not in addition to, the limit of liability of that clause and of any overall aggregate.

All losses arising from one impersonation, or from a series of related impersonations by the same person or group, are one loss. The social engineering excess shown in the schedule for this endorsement applies to each loss.

The increased sub-limit applies to a payment only if, before you acted on the instruction, you followed the verification procedure shown in the schedule for this endorsement. Where you did not, cover for that payment is not removed: it applies at the sub-limit that would apply without this endorsement. Verification therefore limits only the increase. It is not a condition of cover.

Schedule variables: social engineering sub-limit; social engineering excess; verification procedure.

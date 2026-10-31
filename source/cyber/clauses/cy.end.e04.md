---
id: cy.end.e04
type: endorsement
heading: E04 Increased Social Engineering Fraud Sub-limit
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.cy.cover.options_requested
  rules:
  - when: '''E04'' in qs.cy.cover.options_requested'
    action: broker_option
  reason: Offered because you asked for a higher limit for payments made after a fraudulent instruction.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Do not attach
---

The funds transfer and social engineering sub-limit in [[ref:cy.cover.social-engineering]] is increased to the amount shown in the schedule for this endorsement, for loss under that clause.

The increased sub-limit applies to a transfer only if, before acting on the instruction to transfer funds or change payment details, you verified the instruction with the requesting party using contact details you held independently of the instruction (call-back verification), or followed the other verification procedure shown in the schedule. Where verification was not performed, cover for that transfer is not removed: it applies at the sub-limit that would apply without this endorsement.

Schedule variables: increased sub-limit; verification procedure (call-back unless the schedule states otherwise).

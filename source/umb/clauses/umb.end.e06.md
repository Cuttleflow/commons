---
id: umb.end.e06
type: endorsement
heading: E06 Increased Self-insured Retention
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.umb.history.uninsured_loss_5y
  rules:
  - when: qs.umb.history.uninsured_loss_5y == true
    action: apply
  reason: Applies because you have had a loss in the last five years that your primary liability insurance did not cover.
---

The self-insured retention for each occurrence under [[ref:umb.cover.coverage-b]] is the amount shown in the schedule for this endorsement instead of the amount shown for the policy. If no amount is shown, it is four times the self-insured retention shown for the policy.

Schedule variables: the increased self-insured retention (default four times the policy self-insured retention).

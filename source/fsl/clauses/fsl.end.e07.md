---
id: fsl.end.e07
type: endorsement
heading: E07 Release Fraud Sub-limit
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.fsl.operations.special_cargo_pct
  rules:
  - when: qs.fsl.operations.special_cargo_pct > 10
    action: suggest
  reason: Suggested because high-value goods are a frequent target of fictitious pick-up and release fraud.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

The most we pay under [[ref:fsl.cover.cargo-liability|heading]] for loss of goods released to a person who obtained them by deception is the sub-limit shown in the schedule for this endorsement, for any one occurrence and for all occurrences in the policy period. Deception includes impersonating a customer, carrier or driver, using false or altered documents or release instructions, and using a computer system or electronic communication to deceive you or a subcontractor.

The sub-limit does not apply if, before the goods were released, you or your subcontractor followed the verification procedure shown in the schedule for this endorsement. If no procedure is shown, the sub-limit applies to every such loss.

Schedule variables: sub-limit any one occurrence and in the aggregate; verification procedure.

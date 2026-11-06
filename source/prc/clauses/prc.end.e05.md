---
id: prc.end.e05
type: endorsement
heading: E05 Allergen Retention
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.prc.controls.allergen_shared_lines
  rules:
  - when: qs.prc.controls.allergen_shared_lines == true
    action: apply
  reason: Applies because allergen-containing products are made on shared lines without validated cleaning.
---

For an insured event caused by an allergen that is not declared on the label of the insured product, you bear the retention shown in the schedule for this endorsement instead of the policy retention. If no amount is shown, it is twice the policy retention.

Schedule variables: the allergen retention (default twice the policy retention).

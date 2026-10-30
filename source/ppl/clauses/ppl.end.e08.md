---
id: ppl.end.e08
type: endorsement
heading: E08 Incidental Professional Services
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.ppl.ops.advice_for_fee
  - qs.ppl.ops.advice_fee_pct
  rules:
  - when: qs.ppl.ops.advice_fee_pct > 20
    action: refer
  - when: qs.ppl.ops.advice_for_fee == yes
    action: suggest
  reason: Considered because you charge separately for advice, design or inspection.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

[[ref:ppl.excl.professional-services]] does not apply to personal injury or property damage arising from advice, design, specification or inspection given by you for a fee in connection with the sale, installation or servicing of your products or the business, if the fee is incidental to the business. This endorsement does not cover financial loss without personal injury or property damage. The aggregate sub-limit shown in the schedule for this endorsement applies.

Schedule variables: aggregate sub-limit.

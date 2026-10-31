---
id: ppl.end.e14
type: endorsement
heading: E14 Shoring and Underpinning
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.ppl.ops.underpinning
  - qs.ppl.ops.engineer_design
  rules:
  - when: qs.ppl.ops.underpinning == yes and qs.ppl.ops.engineer_design == no
    action: refer
  - when: qs.ppl.ops.underpinning == yes
    action: broker_option
  reason: Offered because you do shoring or underpinning work.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Do not attach
  - Decline risk
---

[[ref:ppl.excl.shoring-and-underpinning]] does not apply, if the shoring, underpinning or temporary support was designed by a qualified structural or geotechnical engineer and carried out in accordance with that design and any required permits. The sub-limit and special excess shown for this endorsement apply.

Schedule variables: sub-limit (any one occurrence); special excess.

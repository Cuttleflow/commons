---
id: trd.end.e15
type: endorsement
heading: E15 Residential Building Work
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trd.ops.residential_work
  - qs.trd.ops.statutory_cover_held
  rules:
  - when: qs.trd.ops.residential_work == yes and qs.trd.ops.statutory_cover_held == no
    action: refer
  - when: qs.trd.ops.residential_work == yes
    action: apply
  reason: Applies because you do residential building work for which the law requires statutory insurance. Work without that insurance is referred to an underwriter.
  responses:
  - Attach
  - Decline risk
---

You carry out residential building work for which the law of a state or territory requires statutory insurance, such as home warranty insurance, home building compensation, domestic building insurance or cover under a statutory scheme.

This policy is not that statutory insurance, and nothing we issue is a certificate of it. This policy does not pay amounts that statutory insurance pays, such as the cost of completing or rectifying work for a homeowner after you die, disappear or become insolvent. You must hold the statutory insurance the law requires for each contract.

This endorsement does not change the cover in [[ref:trd.section.liability|heading]] for your liability for personal injury or property damage arising from that work.

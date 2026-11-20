---
id: fsl.end.e04
type: endorsement
heading: E04 Licence Defence Costs Sub-limit
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.fsl.operations.customs_licence
  rules:
  - when: qs.fsl.operations.customs_licence == true
    action: apply
  reason: Applies because you, or your nominee, hold a customs broker licence.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

The sub-limit for [[ref:fsl.ext.licence-defence-costs]] is the amount shown in the schedule for this endorsement, instead of $50,000. It remains part of, and reduces, the [[ref:fsl.cover.fines-and-penalties|heading]] limit.

Schedule variables: sub-limit (default $100,000).

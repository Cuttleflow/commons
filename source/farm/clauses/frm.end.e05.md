---
id: frm.end.e05
type: endorsement
heading: E05 Incidental Contracting
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.frm.ops.contracting_pct
  rules:
  - when: qs.frm.ops.contracting_pct > 20
    action: refer
  - when: qs.frm.ops.contracting_pct > 0
    action: apply
  reason: Applies because the farm business does contracting for others. More than 20% of gross farm turnover from contracting is referred to an underwriter.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

Incidental contracting is work that brings in no more than the contracting share of the farm business's gross farm turnover in the policy period. [[ref:frm.section.liability|heading]] covers your liability arising from incidental contracting, including property damage to the land, crops and livestock you are working on, up to the worked-on property sub-limit for one occurrence, which is part of, and not in addition to, the liability limit.

This endorsement does not cover aerial spraying, earthmoving deeper than 3 metres, work on a public road other than crossing it, or work that is not agricultural.

Schedule variables: contracting share (default: 20%); worked-on property sub-limit (default: $250,000).

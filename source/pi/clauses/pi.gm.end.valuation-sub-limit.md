---
id: pi.gm.end.valuation-sub-limit
type: endorsement
heading: Mineral Asset Valuation Sub-limit
profession: geoscience-mineral
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.gm.valmin_pct
  rules:
  - when: qs.pi.gm.valmin_pct > 10
    action: suggest
  reason: Applies because {qs.pi.gm.valmin_pct}% of your fees come from mineral asset valuations.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

For all claims arising from the valuation of mineral assets, the most we will pay in total, including defence costs, is the sub-limit shown in the schedule for this endorsement. The sub-limit is part of, and not in addition to, the limit of liability.

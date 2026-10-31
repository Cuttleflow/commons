---
id: pi.acct.end.valuations
type: endorsement
heading: Valuations Sub-limit
profession: accountants
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.ac.valuation_pct
  rules:
  - when: qs.pi.ac.valuation_pct > 20
    action: suggest
  reason: Applies because {qs.pi.ac.valuation_pct}% of your fees come from valuations.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

For all claims arising from business, share or asset valuations, the most we will pay in total, including defence costs, is the sub-limit shown in the schedule for this endorsement. The sub-limit is part of, and not in addition to, the limit of liability.

---
id: fs.fa.end.geared-investments
type: endorsement
heading: Geared Investment Advice Sub-limit
profession: financial-advisers
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.fs.fa.geared_pct
  rules:
  - when: qs.fs.fa.geared_pct > 10
    action: suggest
  reason: Applies because {qs.fs.fa.geared_pct}% of your clients have geared investment strategies.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

For all claims arising from advice to borrow to invest, including margin lending and geared investment strategies, the most we will pay in total, including defence costs, is the sub-limit shown in the schedule for this endorsement. The sub-limit is part of, and not in addition to, the limit of liability.

---
id: ppl.end.e03
type: endorsement
heading: E03 Defence Costs Within the Limit
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.ppl.cover.limit
  rules:
  - when: qs.ppl.cover.limit > 20000000
    action: suggest
  reason: Considered because you asked for a limit of {qs.ppl.cover.limit}; defence costs would reduce the limit.
  responses:
  - Attach
  - Do not attach
---

[[ref:ppl.pay.defence-costs-and-the-limit]] is replaced by the following. Defence costs are part of, and not in addition to, the limit of liability for every claim. Each payment of defence costs reduces the limit of liability available for compensation. Supplementary payments remain in addition to the limit of liability.

Schedule variables: none.

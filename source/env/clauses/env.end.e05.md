---
id: env.end.e05
type: endorsement
heading: E05 Asbestos Abatement
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.env.ops.asbestos_pct
  rules:
  - when: qs.env.ops.asbestos_pct > 0
    action: refer
  reason: Referred because {qs.env.ops.asbestos_pct}% of your turnover comes from asbestos removal or abatement.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:env.excl.asbestos]] does not apply to property damage, natural resource damage or clean-up costs arising from the release of asbestos fibres during asbestos removal or abatement work that you carry out as covered operations, under a licence required by work health and safety law, at a job site. It still applies to personal injury. The most we will pay under this endorsement is the sub-limit shown in the schedule for it, which is part of and not in addition to the limit of liability.

Schedule variables: the sub-limit; the licence class held.

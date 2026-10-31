---
id: pi.rl.end.high-risk-placements
type: endorsement
heading: High-Risk Placements Exclusion
profession: recruitment-labour-hire
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.rl.high_risk_pct
  rules:
  - when: qs.pi.rl.high_risk_pct > 20
    action: refer
  reason: Applies because {qs.pi.rl.high_risk_pct}% of your placements are in high-risk roles.
---

We do not cover any claim, loss or liability arising from the placement or supply of workers into roles in mining, construction, heavy industry, aviation, maritime, healthcare or security, or into any other role shown in the schedule for this endorsement.

This endorsement does not apply to a claim that a placed worker did not hold a licence or qualification that you represented they held.

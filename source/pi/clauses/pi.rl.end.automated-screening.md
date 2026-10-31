---
id: pi.rl.end.automated-screening
type: endorsement
heading: Automated Screening Exclusion
profession: recruitment-labour-hire
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.rl.ai_screening
  rules:
  - when: qs.pi.rl.ai_screening = yes
    action: suggest
  reason: Applies because you use automated tools to screen candidates.
---

We do not cover any claim, loss or liability arising from a decision about a candidate that was made by an automated system, including an artificial intelligence tool, without review by a person before the decision was communicated.

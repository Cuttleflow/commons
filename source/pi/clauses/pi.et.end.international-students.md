---
id: pi.et.end.international-students
type: endorsement
heading: International Students Sub-limit
profession: education-training
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.et.international_pct
  rules:
  - when: qs.pi.et.international_pct > 30
    action: suggest
  reason: Applies because {qs.pi.et.international_pct}% of your students are international students.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

For all claims arising from services to international students, including services as an education agent, the most we will pay in total, including defence costs, is the sub-limit shown in the schedule for this endorsement. The sub-limit is part of, and not in addition to, the limit of liability.

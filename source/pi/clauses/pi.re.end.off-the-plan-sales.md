---
id: pi.re.end.off-the-plan-sales
type: endorsement
heading: Off-the-Plan Sales Sub-limit
profession: real-estate-strata
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.re.off_the_plan_pct
  - qs.pi.practice_states
  rules:
  - when: qs.pi.re.off_the_plan_pct > 25
    action: refer
  restrictions:
  - when: '''NSW'' in qs.pi.practice_states and sub-limit < 1000000'
    action: refer
    note: The Property and Stock Agents Regulation 2022 (NSW) requires at least $1 million for any one claim.
  reason: Applies because {qs.pi.re.off_the_plan_pct}% of your sales are off the plan.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

For all claims arising from the sale of property off the plan, the most we will pay in total, including defence costs, is the sub-limit shown in the schedule for this endorsement. The sub-limit is part of, and not in addition to, the limit of liability.

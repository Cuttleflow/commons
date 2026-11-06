---
id: env.end.e04
type: endorsement
heading: E04 Project Term
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.env.exposure.largest_contract_pct
  - qs.env.contracts.project_cover_required
  rules:
  - when: qs.env.contracts.project_cover_required == true
    action: broker_option
  - when: qs.env.exposure.largest_contract_pct > 25
    action: broker_option
  reason: Offered because a single project is a large share of your turnover, or a contract requires project-specific cover.
---

For the project named in the schedule for this endorsement, [[ref:env.cover.contractors-pollution-liability]] applies with its own limit of liability, aggregate and policy period, as shown for the project, and claims arising from the project do not reduce the limits for your other covered operations. The project's policy period ends on the earlier of the date shown for it and three years after its start.

Schedule variables: the project and job site; the project limit and aggregate; the project policy period; the project premium.

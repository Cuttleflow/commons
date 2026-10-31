---
id: gpa.end.e10
type: endorsement
heading: E10 Passive War and Political Risk Zones
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.policy.high_risk_countries
  rules:
  - when: qs.gpa.policy.high_risk_countries == yes
    action: refer
  reason: Offered because covered persons travel to countries with a war or political risk.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:gpa.excl.war]] does not apply to a covered person who is injured as a result of war, civil war or unrest in a country named in the schedule for this endorsement while they are there for the policyholder's business and are not taking part in it, for up to 14 days after it begins, or for the period shown.

Schedule variables: countries; period.

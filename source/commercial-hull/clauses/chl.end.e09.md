---
id: chl.end.e09
type: endorsement
heading: E09 Lay-up and Port Risks
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.chl.operations.lay_up_months
  rules:
  - when: qs.chl.operations.lay_up_months > 0
    action: refer
  reason: Applies because the vessel is laid up for part of the year.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

During each lay-up shown in the schedule, the Institute Time Clauses Hulls Port Risks CL311 20/7/87, or, where the schedule says so, the Institute Time Clauses Hulls Port Risks including Limited Navigation CL312 20/7/87, apply to the vessel instead of the Institute clauses for its conditions, within the port limits shown in the schedule. [[ref:chl.cover.australian-amendments]] applies to them.

For each complete period of 30 consecutive days of lay-up, we return the percentage of the Hull and Machinery premium shown in the schedule, when the lay-up ends.

The vessel must not carry passengers or cargo during a lay-up. [[ref:chl.cond.insurance-contracts-act]] applies to this condition.

Schedule variables: lay-up place and period; port limits; clause (CL311 or CL312); return for each 30 days (default 50% of one month's premium).

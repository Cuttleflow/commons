---
id: isr.end.vacn
type: endorsement
heading: VACN Unoccupied Buildings
since: 1.1.0
status: draft
note: Contains 1 WP REVIEW tag for the Wording Partner.
trigger:
  questions:
  - qs.isr.risk.vacant_building
  rules:
  - when: qs.isr.risk.vacant_building == yes
    action: apply
  reason: Applies because a building is vacant or partly vacant.
---

A building is **unoccupied** when it, or more than the share of its floor area shown in the Schedule, is not used for the business or by a tenant. A building used only for storage is occupied if you or your agent inspect it at least once every 7 days.

If a building at a Situation has been unoccupied for more than the number of consecutive days shown in the Schedule, the unoccupancy deductible shown applies to Damage to that building caused by malicious damage, theft or escape of water or other liquid, unless you told us before that period ended and we agreed other terms in writing. [WP REVIEW: vacancy as an "omission" under section 54.]

Schedule variables: floor area share (default 50%); days (default 60); unoccupancy deductible.

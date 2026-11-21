---
id: frm.end.e06
type: endorsement
heading: E06 Ground Spraying Conditions
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.frm.ops.ground_spraying
  rules:
  - when: qs.frm.ops.ground_spraying == yes
    action: apply
  reason: Applies because the farm business sprays chemicals by ground equipment.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

When you or an employee spray a chemical by ground equipment for the farm business or in incidental contracting:

- the person spraying must hold any chemical user's accreditation or licence that the law of the state or territory requires;
- the chemical must be used as its label and any permit direct, including the wind speed, droplet size and buffer zone requirements; and
- you must keep the spray records that the law requires, and give them to us with any claim.

The special excess applies to each claim for property damage caused by spray drift. If a condition of this endorsement was not met, [[ref:frm.cond.insurance-contracts-act]] applies.

Schedule variables: special excess (default: $2,500).

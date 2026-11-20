---
id: mpc.end.e02
type: endorsement
heading: E02 Lay-Up Period
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.mpc.cover.lay_up_months
  rules:
  - when: "qs.mpc.cover.lay_up_months > 0"
    action: apply
  reason: "Applies because a lay-up period of {qs.mpc.cover.lay_up_months} months was chosen."
  responses:
  - Attach
  - Do not attach
---

During the lay-up period shown in the schedule for this endorsement, [[ref:mpc.section.boat]] covers the boat only while it is out of the water at the storage address shown in the schedule, and while it is being moved by road to or from a place of repair. It does not cover the boat while it is afloat. [[ref:mpc.section.liability]] continues to apply.

If you want to use the boat during the lay-up period, tell us before you do. We will end the lay-up period from that date and you pay the difference in premium for the rest of the policy period, on a pro-rata basis.

Schedule variables: lay-up period (start and end dates); storage address.

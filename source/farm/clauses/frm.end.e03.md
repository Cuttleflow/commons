---
id: frm.end.e03
type: endorsement
heading: E03 Farm Stays and Paying Guests
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.frm.ops.farm_stay
  rules:
  - when: qs.frm.ops.farm_stay == yes
    action: refer
  reason: Referred because the farm business has paying guests, which the underwriter assesses before cover is given.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:frm.li.excl-guests]] does not apply to liability arising from accommodation, meals and farm tours you provide to paying guests at the farm location, for no more than the maximum number of guests at any one time.

You must hold every approval your local council and state or territory law require for the accommodation, keep the smoke alarms, fire safety and escape routes those approvals require, and keep a register of guests. This endorsement does not cover horse riding, motorcycles, all-terrain vehicles, shooting, swimming in dams or rivers, or other adventure activities, unless the schedule also shows [[ref:frm.end.e04]] for horse riding.

Schedule variables: maximum number of guests (default: 12).

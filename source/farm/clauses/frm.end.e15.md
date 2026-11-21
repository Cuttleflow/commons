---
id: frm.end.e15
type: endorsement
heading: E15 Firefighting Equipment
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.frm.fire.firefighting_unit
  rules:
  - when: qs.frm.fire.firefighting_unit == yes
    action: apply
  reason: Applies because you keep a firefighting unit at the farm location, which earns a premium credit.
  responses:
  - Attach
  - Do not attach
---

You have told us that during the fire danger season you keep at the farm location a firefighting unit with a pump and a tank holding at least the minimum tank capacity of water, in working order and ready to use. We have set your premium on that basis. Keep the unit in working order and ready to use during the fire danger season. If you do not, [[ref:frm.cond.insurance-contracts-act]] applies.

Schedule variables: minimum tank capacity (default: 400 litres).

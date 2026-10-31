---
id: mot.end.e16
type: endorsement
heading: E16 Tow Trucks and Recovery Vehicles
since: 3.0.0
status: draft
trigger:
  questions:
  - qs.mot.use.tow_recovery
  rules:
  - when: qs.mot.use.tow_recovery == true
    action: refer
  reason: Referred because vehicles are used for towing or recovery.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Decline risk
---

For Insured vehicles used as tow trucks or recovery vehicles, we pay for loss of or damage to a vehicle being towed, carried or recovered by them, for which you are legally liable, up to the amount shown in the Schedule for each Occurrence. [[ref:mot.excl.liability]] does not apply to that property to that extent. The driver must hold any tow truck licence or authority the law requires.

Schedule variables: goods in care limit; excess.

---
id: mot.hmv.end.e21
type: endorsement
heading: E21 Specialist Transport Operations
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.hmv.operations.specialist
  rules:
  - when: qs.hmv.operations.specialist != 'none'
    action: refer
  reason: Referred because you told us vehicles are used for {qs.hmv.operations.specialist} work.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Decline risk
---

The specialist operations shown in the Schedule, such as car carrying, logging, concrete agitating or pumping, crane or lifting work, oversize or heavy haulage, or waste collection, are Permitted use for the Insured vehicles shown for them. For those vehicles, the specialist operations excess shown in the Schedule applies in addition to the basic excess. Liability arising from the use of a vehicle or its equipment as a Tool of trade remains excluded.

Schedule variables: operations; vehicles; specialist operations excess.

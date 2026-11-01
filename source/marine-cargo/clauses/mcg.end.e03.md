---
id: mcg.end.e03
type: endorsement
heading: E03 Own Vehicle Carriage
since: 1.0.0
changed: 1.1.0
status: draft
trigger:
  questions:
  - qs.mcg.ops.own_vehicle_pct
  rules:
  - when: qs.mcg.ops.own_vehicle_pct > 0
    action: apply
  reason: Applies because {qs.mcg.ops.own_vehicle_pct}% of your inland sendings travel in your own vehicles.
---

For goods carried in your own vehicle:

- we do not cover theft of goods from a vehicle left unattended, unless the vehicle is locked with all windows and doors closed and the goods are in a closed, locked compartment or under a locked cover, or the vehicle is in a locked building or a locked and fenced compound;
- we do not cover theft from a vehicle left unattended overnight in the open, unless the schedule for this endorsement says otherwise;
- goods must be secured against movement during the transit; and
- the driver must hold a current licence for the vehicle.

These requirements are not warranties. If you do not meet one, we may refuse only the part of the claim that the failure caused or contributed to, as [[ref:mcg.cond.insurance-contracts-act]] sets out.

The excess shown in the schedule for this endorsement applies to each claim for goods carried in your own vehicle.

Schedule variables: special excess (default the excess shown in the schedule); whether overnight parking in the open is allowed.

---
id: peq.end.e02
type: endorsement
heading: E02 Cranes
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.peq.plant.crane_count
  - qs.peq.plant.crane_over_25t
  - qs.peq.plant.dual_lifts
  rules:
  - when: qs.peq.plant.crane_over_25t == yes or qs.peq.plant.dual_lifts == yes
    action: refer
  - when: qs.peq.plant.crane_count > 0
    action: apply
  reason: Applies because {qs.peq.plant.crane_count} crane(s) are insured; referred where a crane is rated above 25 tonnes or makes dual or tandem lifts.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

This endorsement applies to every crane that is insured plant, and to any item of plant used to lift a suspended load.

**Lifting conditions.** Each lift must be:

- made by an operator who holds the high risk work licence that the law requires for that crane;
- planned by a competent person using the crane's load chart for the radius, configuration and ground conditions; and
- made with outriggers or stabilisers deployed on ground or mats assessed as able to bear the load, and within the wind limits set by the crane's manufacturer.

A dual or tandem lift, in which more than one item of plant shares a load, must also follow a written lift plan approved by a competent person before the lift.

[[ref:peq.cond.insurance-contracts-act]] governs our response where a lift did not meet these conditions.

**Overturning.** Accidental loss or damage to a crane caused by its overturning, or by the collapse of its boom or jib, is covered under [[ref:peq.cover.material-damage|heading]], and the crane excess shown in the schedule applies to it.

**Goods lifted.** The limit in [[ref:peq.ext.goods-lifted]] is increased to the amount shown in the schedule for this endorsement.

Schedule variables: cranes covered, with their rated capacity; crane excess (default twice the item's excess); goods lifted limit (default $1,000,000 for any one occurrence).

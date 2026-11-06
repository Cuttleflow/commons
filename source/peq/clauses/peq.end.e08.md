---
id: peq.end.e08
type: endorsement
heading: E08 Electric Plant
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.peq.plant.electric_count
  rules:
  - when: qs.peq.plant.electric_count > 0
    action: apply
  reason: Applies because {qs.peq.plant.electric_count} item(s) of insured plant are battery electric or hybrid.
  responses:
  - Attach
  - Attach with special excess
  - Do not attach
---

This endorsement applies to each item of insured plant that is battery electric or hybrid.

**Battery and charger.** The traction battery and the charger supplied with an item are part of the item and its sum insured. Accidental loss or damage to the battery, the charger or the item caused by a fire, explosion or thermal runaway during charging is covered under [[ref:peq.cover.material-damage|heading]].

**Charging conditions.** The item must be charged with a charger approved by its manufacturer, in an area clear of combustible materials.

**Not covered.** We do not pay for the gradual loss of a battery's capacity, or for a battery that fails without external accidental damage, unless [[ref:peq.section.breakdown|heading]] applies to the item.

The battery excess shown in the schedule applies to loss or damage confined to the battery, instead of the item's excess, where it is higher.

Schedule variables: items covered; battery excess (default the item's excess).

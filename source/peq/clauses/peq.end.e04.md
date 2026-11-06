---
id: peq.end.e04
type: endorsement
heading: E04 Demolition Plant
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.peq.ops.demolition
  rules:
  - when: qs.peq.ops.demolition == yes
    action: refer
  reason: Referred because insured plant is used for demolition.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

This endorsement applies to insured plant while it is used for demolition.

**Demolition conditions.** The demolition must follow a written demolition plan or safe work method statement prepared by a competent person. Plant working within reach of falling material must be fitted with a falling object protective structure and with guarding for its windows and hydraulic lines.

We do not pay for loss or damage caused by falling material to an item of plant that was not fitted with that protection.

The demolition excess shown in the schedule applies to loss or damage that happens during demolition, instead of the item's excess, where it is higher.

Schedule variables: items covered; demolition excess (default twice the item's excess).

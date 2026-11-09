---
id: trd.end.e08
type: endorsement
heading: E08 Tree Work Limit
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trd.ops.tree_work
  rules:
  - when: qs.trd.ops.tree_work == yes
    action: apply
  reason: Applies because you fell, lop or remove trees.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
  - Decline risk
---

[[ref:trd.section.liability|heading]] does not cover liability arising from felling, lopping or removing a tree taller than the height limit shown for this endorsement, or from tree work within 3 metres of an overhead power line, unless the work is done by a person who holds a Certificate III in Arboriculture or a higher qualification.

Schedule variables: tree height limit (default: 6 metres).

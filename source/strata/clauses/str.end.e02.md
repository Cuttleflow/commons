---
id: str.end.e02
type: endorsement
heading: E02 Known Defect
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.str.risk.known_defects
  - qs.str.risk.defect_orders
  rules:
  - when: qs.str.risk.defect_orders == yes
    action: refer
  - when: qs.str.risk.known_defects == yes
    action: refer
  reason: Referred because the body corporate has told us about a known defect or a defect order. Known defects are common; the underwriter decides the terms.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The schedule names a known defect in the building and the part of the building it affects.

- The cost of fixing the named defect is not covered, as [[ref:str.excl.defects-and-gradual-causes]] provides.
- Damage to other parts of the building that results suddenly and accidentally from the named defect is covered, subject to the special excess shown in the schedule for this endorsement.
- If the schedule says so, damage to the affected part of the building caused by the named defect is not covered until the defect is fixed. Tell us when it is fixed, and we will remove that restriction.

Liability arising from the named defect is covered under [[ref:str.section.liability]] as usual.

Schedule variables: description of the defect and the affected part; special excess (default: the basic excess); whether damage to the affected part is excluded until rectification.

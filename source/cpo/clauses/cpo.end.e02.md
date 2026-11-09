---
id: cpo.end.e02
type: endorsement
heading: E02 Known Defect
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.cpo.condition.known_defects
  rules:
  - when: qs.cpo.condition.known_defects == yes
    action: refer
  reason: A known defect in the building was disclosed.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The defect described in the schedule for this endorsement is known to you and to us. [[ref:cpo.excl.defects-and-gradual-causes]] applies to it as modified here: we pay for sudden and accidental damage that results from the described defect, subject to the special excess shown for this endorsement, but not for the cost of fixing the defect itself. You agree to carry out the remedial work shown in the schedule by the date shown, and to tell us when it is done.

Schedule variables: description of the defect; remedial work and completion date; special excess (default: the basic excess).

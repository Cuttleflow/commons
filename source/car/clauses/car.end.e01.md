---
id: car.end.e01
type: endorsement
heading: E01 Existing Structures and Principal's Contents
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.car.s1.existing_structures_si
  - qs.car.s1.principals_contents_si
  rules:
  - when: qs.car.s1.existing_structures_si > 2000000
    action: refer
  - when: qs.car.s1.existing_structures_si > 0 or qs.car.s1.principals_contents_si > 0
    action: broker_option
  reason: Considered because existing structures worth ${qs.car.s1.existing_structures_si} are part of, or next to, the project.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

The existing structures and principal's contents named in the schedule for this endorsement are part of the contract works, for the sums insured shown.

**Dilapidation survey.** Before work starts, a dilapidation survey of the existing structures is carried out and kept. We do not pay for damage that the survey records as existing before work started.

**Vibration and removal of support.** We pay for damage to the existing structures caused by vibration or by the removal or weakening of support only if [[ref:car.cond.vibration-and-services]] has been met.

**Primary insurance.** Where the construction contract requires the principal's own property insurance to respond first, this endorsement pays the amount by which the loss exceeds what that insurance pays.

The existing structures excess shown in the schedule applies.

Schedule variables: existing structures described; existing structures sum insured; principal's contents sum insured; existing structures excess (default $25,000).

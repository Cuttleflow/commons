---
id: ah.end.e10
type: endorsement
heading: E10 Animal-assisted Therapy Program
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.ah.practice.therapy_animal_program
  rules:
  - when: qs.ah.practice.therapy_animal_program == yes
    action: suggest
  reason: Suggested because you run a structured animal-assisted therapy program.
---

[[ref:ah.ext.therapy-animals]] is extended to the structured animal-assisted therapy program described in the schedule, including the additional therapy animals, handlers and program locations named there. The insured must hold current veterinary health certification and a temperament assessment for each therapy animal, and maintain a documented animal-welfare and infection-control protocol.

Schedule variables: program description; animals, handlers and locations; sub-limit (optional).

---
id: gtr.exp.end.e14
type: endorsement
heading: E14 Routine Dental and Optical
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gtr.exp.dental
  rules:
  - when: qs.gtr.exp.dental == yes
    action: apply
  reason: Applied because routine dental and optical cover was chosen.
  responses:
  - Attach
  - Attach with amended sub-limit
---

Under the Standard plan, we pay for routine dental treatment (examinations, cleaning, fillings and extractions) and for eye examinations, glasses and contact lenses, up to the amount shown in the schedule for each insured person in each policy period (default $1,500), after a qualifying period of 3 months of cover.

Schedule variables: annual limit.

---
id: pi.rl.end.labour-hire-licences
type: endorsement
heading: Labour Hire Licence Condition
profession: recruitment-labour-hire
since: 1.0.0
status: draft
note: Records the licences on which the base Licences, Registrations and Accreditations condition depends. Counsel to confirm which states currently require a licence.
trigger:
  questions:
  - qs.pi.rl.labour_hire_states
  - qs.pi.rl.licence_numbers
  rules:
  - when: qs.pi.rl.labour_hire_states is not empty
    action: apply
  reason: Applies because you provide labour hire in a state or territory that requires a licence.
---

Labour hire services in a state or territory are professional services under this policy only while you hold the labour hire licence that the law of that state or territory requires. The licence numbers are shown in the schedule.

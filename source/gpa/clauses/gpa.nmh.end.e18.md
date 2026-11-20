---
id: gpa.nmh.end.e18
type: endorsement
heading: E18 Dental Injury Enhancement
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.nmh.dental
  rules:
  - when: qs.gpa.nmh.dental == yes
    action: apply
  reason: Applied because the policyholder buys the dental injury enhancement.
  responses:
  - Attach
  - Do not attach
---

For dental treatment of an injury to sound natural teeth, the limit for each injury in [[ref:gpa.xmed.cover.medical-expenses]] is increased by the amount shown in the schedule (default $1,000), and the treatment may be given up to 104 weeks after the accident if a dentist certifies that it could not reasonably be given sooner.

Schedule variables: additional dental limit.

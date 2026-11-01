---
id: ah.end.e09
type: endorsement
heading: E09 Telehealth to Overseas Patients
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.ah.practice.overseas_telehealth
  rules:
  - when: qs.ah.practice.overseas_telehealth == yes
    action: refer
  reason: Referred because you provide telehealth to patients outside Australia.
---

[[ref:ah.ext.telehealth]] is extended to professional services provided by telehealth from Australia to patients or clients located in the countries stated in the schedule, provided the insured complies with the registration, licensing and privacy laws of both Australia and the patient's location. [[ref:ah.excl.usa-canada]] continues to apply absolutely.

Schedule variables: countries.

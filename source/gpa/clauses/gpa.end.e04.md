---
id: gpa.end.e04
type: endorsement
heading: E04 Overseas Secondment
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.policy.overseas_secondment
  rules:
  - when: qs.gpa.policy.overseas_secondment == yes
    action: refer
  reason: Offered because covered persons are seconded to work outside Australia.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

For the covered persons named in the schedule for this endorsement, [[ref:gpa.obl.residence-and-travel]] does not limit cover while they are seconded by the policyholder to work outside Australia in the countries named, for the period shown. We also pay the reasonable cost of emergency medical evacuation to the nearest place where adequate treatment is available, and of returning the covered person to Australia, up to the limit shown.

Schedule variables: covered persons or category; countries; secondment period; evacuation and repatriation limit (default $100,000).

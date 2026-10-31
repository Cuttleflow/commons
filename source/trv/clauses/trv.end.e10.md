---
id: trv.end.e10
type: endorsement
heading: E10 Epidemic and Pandemic Disruption
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trv.cover.pandemic
  rules:
  - when: qs.trv.cover.pandemic == yes
    action: apply
  reason: Applied because epidemic and pandemic disruption cover was chosen.
  responses:
  - Attach
  - Do not attach
---

[[ref:trv.excl.epidemic-pandemic]] does not apply where you or your travel companion are diagnosed with the disease, or you are denied boarding or placed in mandatory quarantine because you are suspected of having it. It does not cover border closures, travel bans, quarantine of a whole population, or a change in DFAT advice because of the epidemic or pandemic.

Schedule variables: sub-limit (default the cancellation limit for your plan).

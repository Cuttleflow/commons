---
id: bpk.end.e12
type: endorsement
heading: E12 Specified Occupations
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.bpk.situation.hazards
  rules:
  - when: '''deep_frying'' in qs.bpk.situation.hazards or ''spray_painting'' in qs.bpk.situation.hazards or ''woodworking'' in qs.bpk.situation.hazards'
    action: refer
  - when: '''flammable_liquids'' in qs.bpk.situation.hazards'
    action: suggest
  reason: 'Considered because of the hazards at a Situation: {qs.bpk.situation.hazards}.'
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Decline risk
---

For the occupation shown in the Schedule, the conditions listed in the Schedule apply to the sections listed beside them. [[ref:bpk.cond.insurance-contracts-act]] applies to each condition.

Schedule variables: occupation; conditions; sections to which each condition applies.

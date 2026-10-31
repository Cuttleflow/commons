---
id: bpk.end.e01
type: endorsement
heading: E01 Accidental Damage
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.bpk.situation.accidental_damage_wanted
  rules:
  - when: qs.bpk.situation.accidental_damage_wanted == yes
    action: broker_option
  reason: Offered because you asked for accidental damage cover at a Situation.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

[[ref:bpk.pd.insured-events]] is extended to include accidental Damage not otherwise excluded, up to the accidental damage sub-limit and Excess shown in the Schedule.

Schedule variables: Situations; accidental damage sub-limit; Excess.

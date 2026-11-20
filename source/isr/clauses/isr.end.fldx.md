---
id: isr.end.fldx
type: endorsement
heading: FLDX Flood Exclusion for Specified Situations
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.peril.binder_excluded_postcode
  - qs.isr.peril.flood_score_max
  rules:
  - when: qs.isr.peril.binder_excluded_postcode == yes
    action: apply
  - when: qs.isr.peril.flood_score_max == 'high'
    action: suggest
  reason: Applies because a Situation is in a postcode the binder excludes for flood, or suggested because a Situation has a high flood score.
---

We do not pay for Damage by Flood, or Business Interruption loss resulting from it, at the Situations or postcodes listed in the Schedule for this endorsement. Flood has the meaning given in FLOD. This exclusion does not apply to Damage by fire or explosion that results from Flood.

Schedule variables: excluded Situations or postcodes.

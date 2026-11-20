---
id: isr.end.flod
type: endorsement
heading: FLOD Flood Cover
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.peril.flood_score_max
  - qs.isr.peril.binder_excluded_postcode
  rules:
  - when: qs.isr.peril.flood_score_max == 'high'
    action: refer
  - when: qs.isr.peril.flood_score_max == 'medium'
    action: suggest
  - when: qs.isr.peril.flood_score_max == 'low'
    action: apply
  restrictions:
  - when: qs.isr.peril.binder_excluded_postcode == yes
    action: refer
    note: A Situation is in a postcode the binder excludes for flood.
  reason: Applies from the flood score of each geocoded Situation; the highest score among the Situations decides the action.
---

In this endorsement, **Flood** means the covering of normally dry land by water that has escaped or been released from the normal confines of a lake, river, creek or other natural watercourse (whether or not it has been altered or modified), or of a reservoir, canal or dam. It includes water from any of those sources that reaches the land, or enters a building, through a stormwater drain, sewer or other pipe. It does not include action of the sea, storm surge or tsunami.

- For each Situation, we cover Damage by Flood, and Business Interruption loss resulting from it, up to the flood limit shown in the Schedule for that Situation. The Schedule may set the flood limit by tiers of Situation value.
- The flood deductible shown applies to each Situation for each Event. All Flood within any 72 consecutive hours is one Event.
- There is no cover for Flood at a Situation or postcode that the Schedule lists as excluded.
- We do not cover Flood that happens within 72 hours after this endorsement first starts, unless it starts at the same time as cover that replaces flood cover held without a break.
- This endorsement replaces any flood exclusion and flood definition in the Base Wording for the Situations to which it applies. Rainwater and stormwater that has not escaped from one of the sources above is not Flood; the Base Wording's cover for storm and water applies to it.

Schedule variables: flood limit per Situation or per value tier; flood deductible; excluded Situations or postcodes.

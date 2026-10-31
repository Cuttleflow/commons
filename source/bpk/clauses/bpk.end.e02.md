---
id: bpk.end.e02
type: endorsement
heading: E02 Flood
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.bpk.situation.flood_history
  rules:
  - when: qs.bpk.situation.flood_history == yes
    action: refer
  reason: Considered because a Situation has flooded in the last 10 years or is in a flood-prone area.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Do not attach
  - Decline risk
---

Flood is removed from the storm and flood event in [[ref:bpk.pd.insured-events]], or limited to the flood sub-limit shown in the Schedule, as the Schedule states.

In this Endorsement, flood means the covering of normally dry land by water escaping or released from the normal confines of a lake, river, creek or other natural watercourse, reservoir, canal or dam.

Schedule variables: Situations; removed or limited; flood sub-limit.

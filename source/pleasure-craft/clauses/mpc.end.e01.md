---
id: mpc.end.e01
type: endorsement
heading: E01 Racing
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.mpc.cover.racing
  rules:
  - when: qs.mpc.cover.racing == beyond_150nm
    action: refer
  - when: qs.mpc.cover.racing == to_150nm
    action: apply
  reason: Applies because racing cover was chosen; racing beyond 150 nautical miles is referred to the underwriter.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The boat is covered while racing in a race organised by a recognised yacht club, sailing association or racing authority, within the racing limit shown in the schedule for this endorsement (default 150 nautical miles from the start). [[ref:mpc.excl.racing-and-speed]] does not apply to that racing, but it still applies to a powered boat or personal watercraft.

The restriction on damage to sails, spars and rigging while racing, in [[ref:mpc.excl.boat-other|heading]], still applies. While racing, the racing excess shown in the schedule for this endorsement (default twice the basic excess) applies in place of the basic excess.

Schedule variables: racing limit (default 150 nautical miles); racing excess (default twice the basic excess).

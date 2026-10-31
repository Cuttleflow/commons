---
id: pi.mm.end.live-broadcast
type: endorsement
heading: Live Broadcast Exclusion
profession: marketing-media
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.mm.live_broadcast
  - qs.pi.mm.delay_system
  rules:
  - when: qs.pi.mm.live_broadcast = yes and qs.pi.mm.delay_system = no
    action: refer
  reason: Applies because you broadcast or stream live without a delay system.
---

We do not cover any claim, loss or liability arising from material broadcast or streamed live without a delay system that allows the material to be stopped before it reaches the audience.

---
id: pi.mm.end.user-content
type: endorsement
heading: User Content Exclusion
profession: marketing-media
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.mm.ugc_platforms
  - qs.pi.mm.moderation
  rules:
  - when: qs.pi.mm.ugc_platforms = yes and qs.pi.mm.moderation = no
    action: apply
  reason: Applies because you host user content without moderation.
---

We do not cover any claim, loss or liability arising from material posted by a person other than you, or your employees or contractors, on a website, platform or channel that you operate or moderate for yourself or a client.

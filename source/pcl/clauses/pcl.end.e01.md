---
id: pcl.end.e01
type: endorsement
heading: E01 Worldwide Cover
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pcl.cover.worldwide_all_categories
  rules:
  - when: qs.pcl.cover.worldwide_all_categories == yes
    action: apply
  reason: Applies because worldwide cover for every category was chosen.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

Every category is covered anywhere in the world, in place of the table in [[ref:pcl.cover.where-covered]]. An item of fine art, antiques and decorative arts, collectables, wine or musical instruments is covered outside Australia for up to the number of consecutive days shown in the schedule for this endorsement on any one trip.

[[ref:pcl.excl.breakage-in-transit]] continues to apply.

Schedule variables: days on any one trip (default 90).

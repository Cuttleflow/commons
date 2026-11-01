---
id: hom.end.e04
type: endorsement
heading: E04 Home Business
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.hom.occupancy.home_business
  rules:
  - when: qs.hom.occupancy.home_business == yes
    action: refer
  reason: Referred because a business is carried on at the home.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

A member of your household carries on the business described in the schedule for this endorsement at the home. Business equipment and stock at the home are contents, up to the business contents limit shown in the schedule for this endorsement. [[ref:hom.excl.liability-business]] does not apply to liability arising from that business at the home, other than liability for professional advice or for products sold.

Schedule variables: business description; business contents limit (default $10,000).

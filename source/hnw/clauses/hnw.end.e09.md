---
id: hnw.end.e09
type: endorsement
heading: E09 Building Valuation to Follow
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.hnw.cover.building_sum_insured
  - qs.hnw.cover.building_valuation_current
  rules:
  - when: qs.hnw.cover.building_sum_insured > 2500000 and qs.hnw.cover.building_valuation_current == no
    action: refer
  - when: qs.hnw.cover.building_valuation_current == no
    action: apply
  reason: Applies because the building sum insured of ${qs.hnw.cover.building_sum_insured} has no professional valuation less than three years old; above $2.5m it is referred.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

You have not given us a professional valuation of the rebuilding cost of the building dated within the three years before this policy started. Until you do, [[ref:hnw.pay.extended-replacement]] applies with an extended replacement percentage of 10%.

Give us a professional valuation within the number of days after this policy starts shown in the schedule for this endorsement. When you do, the extended replacement percentage shown in the schedule applies from the date of the valuation, and we will adjust the building sum insured and the premium if the valuation shows a different rebuilding cost.

Schedule variables: days to give the valuation (default 90).

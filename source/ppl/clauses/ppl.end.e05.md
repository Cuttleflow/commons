---
id: ppl.end.e05
type: endorsement
heading: E05 Gradual Pollution
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.ppl.ops.gradual_pollution_requested
  - qs.ppl.ops.hazardous_substances
  rules:
  - when: qs.ppl.ops.gradual_pollution_requested == yes and qs.ppl.ops.hazardous_substances == yes
    action: refer
  - when: qs.ppl.ops.gradual_pollution_requested == yes
    action: broker_option
  reason: Offered because you asked for gradual pollution cover.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

[[ref:ppl.excl.pollution]] does not apply to personal injury or property damage caused by a gradual discharge, dispersal, release, seepage or escape of a pollutant from premises or a site where you work in Australia, if:

- the discharge began after the retroactive date shown in the schedule for this endorsement;
- it was first discovered by you during the policy period; and
- you told us about it in writing within 30 days of discovery and during the policy period.

We do not cover the cost of testing, monitoring, cleaning up, removing, containing or neutralising pollutants on premises you own, lease or occupy, or any fine or penalty. The most we will pay under this endorsement for all occurrences in the policy period, including defence costs, is the aggregate sub-limit shown in the schedule.

Schedule variables: aggregate sub-limit; retroactive date; special excess (optional).

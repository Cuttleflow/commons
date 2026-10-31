---
id: pa.end.e05
type: endorsement
heading: E05 Named Hazardous Pursuit
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pa.hazard.scuba_over_30m
  - qs.pa.hazard.air_sports
  - qs.pa.hazard.motor_racing
  - qs.pa.hazard.private_pilot
  - qs.pa.hazard.mountaineering
  rules:
  - when: qs.pa.hazard.scuba_over_30m == yes or qs.pa.hazard.air_sports == yes or qs.pa.hazard.motor_racing == yes or qs.pa.hazard.private_pilot == yes or qs.pa.hazard.mountaineering == yes
    action: refer
  reason: Offered because the insured person takes part in a pursuit the base wording excludes.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:pa.excl.hazardous-pursuits]] and [[ref:pa.excl.flying]] do not apply to the pursuits named in the schedule for this endorsement, while you take part in them as an amateur, under the rules of the governing body for the pursuit where there is one, and holding any licence or qualification it requires.

Schedule variables: named pursuits; conditions for each pursuit (for example, maximum depth or minimum licence); any capital sum limit for injury during the pursuit.

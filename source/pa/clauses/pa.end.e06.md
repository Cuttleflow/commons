---
id: pa.end.e06
type: endorsement
heading: E06 Named Pursuit Exclusion
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pa.hazard.motorcycle_offroad
  - qs.pa.hazard.climbing
  - qs.pa.hazard.contact_sports
  - qs.pa.hazard.equestrian
  rules:
  - when: qs.pa.hazard.motorcycle_offroad == yes or qs.pa.hazard.climbing == yes or qs.pa.hazard.contact_sports == yes or qs.pa.hazard.equestrian == yes
    action: suggest
  reason: Suggested as an alternative to a premium loading for a pursuit the insured person takes part in.
  responses:
  - Attach
  - Do not attach
---

We do not pay any benefit for an injury that happens while you are taking part in the pursuits named in the schedule for this endorsement.

Schedule variables: named pursuits.

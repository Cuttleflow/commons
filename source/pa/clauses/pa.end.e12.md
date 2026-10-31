---
id: pa.end.e12
type: endorsement
heading: E12 Increased Additional Benefits
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pa.cover.increased_additional
  rules:
  - when: qs.pa.cover.increased_additional == yes
    action: broker_option
  reason: Offered as an option because higher funeral and rehabilitation limits were requested.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

The limits shown in the schedule for this endorsement replace the default limits in [[ref:pa.ext.funeral-expenses]] and [[ref:pa.ext.rehabilitation]].

Schedule variables: funeral expenses limit (default $30,000); rehabilitation limit (default $25,000).

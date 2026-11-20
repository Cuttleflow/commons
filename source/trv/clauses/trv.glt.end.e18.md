---
id: trv.glt.end.e18
type: endorsement
heading: E18 Host Family Liability
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trv.glt.host_family
  rules:
  - when: qs.trv.glt.host_family == yes
    action: apply
  reason: Applied because group members will stay with host families.
  responses:
  - Attach
  - Do not attach
---

In [[ref:trv.cover.liability]], the exclusion of property of a close relative or travel companion does not apply to loss of or damage to the property of a host family with whom a group member stays as part of the itinerary, up to the limit shown in the schedule (default $5,000 for each event). The other terms of that section apply.

Schedule variables: host family property limit.

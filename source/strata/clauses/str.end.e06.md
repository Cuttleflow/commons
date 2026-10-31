---
id: str.end.e06
type: endorsement
heading: E06 Short-Term Letting
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.str.occupancy.short_term_pct
  rules:
  - when: qs.str.occupancy.short_term_pct > 25
    action: refer
  - when: qs.str.occupancy.short_term_pct > 0
    action: apply
  reason: Applies because {qs.str.occupancy.short_term_pct}% of the lots are let for short stays.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

Cover is not affected because lots are let for stays of less than three months. Malicious damage to the common property by a short-stay guest is covered, subject to the special excess shown in the schedule for this endorsement.

Schedule variables: share of lots let for short stays; special excess (default: the basic excess).

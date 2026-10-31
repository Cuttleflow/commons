---
id: str.end.e01
type: endorsement
heading: E01 Flood Cover
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.str.cover.flood_requested
  rules:
  - when: qs.str.cover.flood_requested == yes
    action: refer
  reason: Referred because flood cover was requested; the underwriter prices it from the flood risk at the address.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

[[ref:str.excl.flood]] does not apply. We cover damage to the building and common contents caused by flood under [[ref:str.section.property]], subject to the flood excess shown in the schedule for this endorsement.

All damage by flood within any 72 hour period is one event. We do not pay for damage by flood in the first 72 hours after this endorsement starts, unless it starts at the same time as a policy that replaces one with flood cover without a break.

Schedule variables: flood excess (default $5,000).

---
id: cpo.end.e01
type: endorsement
heading: E01 Flood Cover
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.cpo.cover.flood_requested
  rules:
  - when: qs.cpo.cover.flood_requested == yes
    action: refer
  reason: Flood cover was requested; flood is priced by the underwriter for the address.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

[[ref:cpo.excl.flood]] does not apply. Damage caused by flood is covered under [[ref:cpo.section.property]] and [[ref:cpo.section.loss-of-rent]], subject to the flood excess and the flood limit shown in the schedule for this endorsement.

This endorsement does not apply to damage caused by flood that happens within 72 hours of the start of the first policy period in which it is shown, unless this policy replaced another policy that covered flood without a break.

Schedule variables: flood excess (default: $10,000); flood limit (default: the building sum insured).

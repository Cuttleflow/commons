---
id: prc.end.e04
type: endorsement
heading: E04 USA and Canada
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.prc.products.usa_canada_export
  rules:
  - when: qs.prc.products.usa_canada_export == true
    action: refer
  reason: Referred because you sell insured products in the USA or Canada.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:prc.excl.usa-canada]] does not apply, and the geographical limits include the USA and Canada, up to the sub-limit shown in the schedule for this endorsement for loss from insured products sold or distributed there.

Schedule variables: the sub-limit; any retention that applies instead of the policy retention.

---
id: umb.end.e01
type: endorsement
heading: E01 USA and Canada
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.umb.exposure.usa_canada_pct
  rules:
  - when: qs.umb.exposure.usa_canada_pct > 10
    action: refer
  - when: qs.umb.exposure.usa_canada_pct > 0
    action: suggest
  reason: Applies because {qs.umb.exposure.usa_canada_pct}% of your turnover comes from products exported to, or work in, the USA and Canada.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:umb.excl.usa-canada]] does not apply to the extent that the underlying insurance covers claims brought in the USA and Canada, or arising from products exported there. This policy follows that cover under [[ref:umb.cover.coverage-a]] only, up to the sub-limit shown in the schedule for this endorsement, which is part of and not in addition to the limit of liability. Defence costs for these claims are part of, and reduce, that sub-limit.

Schedule variables: the sub-limit; whether exported products only, or also work carried out in the USA and Canada.

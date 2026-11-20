---
id: eqf.end.e01
type: endorsement
heading: E01 Open Site Storage
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.eqf.security.open_site_overnight
  rules:
  - when: qs.eqf.security.open_site_overnight == true
    action: refer
  reason: Applies because you leave equipment on site in the open overnight.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

[[ref:eqf.excl.portable-equipment]] does not exclude theft of insured property left in the open overnight on a construction or work site, where the site is fenced and locked, or the property is chained or locked to a fixed structure. The special excess shown in the schedule applies to each such claim.

Schedule variables: special excess (default $1,000).

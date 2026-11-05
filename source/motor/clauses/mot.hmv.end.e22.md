---
id: mot.hmv.end.e22
type: endorsement
heading: E22 Restricted Sites
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.hmv.operations.restricted_sites
  rules:
  - when: qs.hmv.operations.restricted_sites == true
    action: refer
  reason: Referred because you told us vehicles operate on mine sites, ports or airport airside areas.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Decline risk
---

This Endorsement applies to an Occurrence on a restricted site shown in the Schedule, such as a mine site, port or airport airside area. For that Occurrence:

- the restricted site excess shown in the Schedule applies in addition to the basic excess; and
- the most we pay under [[ref:mot.section.liability|heading]] for damage to property of the site operator, or of anyone working on the site, is the restricted site sub-limit shown in the Schedule. The sub-limit is part of, not in addition to, the third party property damage limit.

Schedule variables: restricted sites; restricted site excess; restricted site sub-limit.

---
id: imi.end.e01
type: endorsement
heading: E01 US and Canada Jurisdiction Extension
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.imi.exposure.us_ca_pct
  - qs.imi.cover.options_requested
  rules:
  - when: qs.imi.exposure.us_ca_pct > 0
    action: refer
  - when: '''E01 US and Canada Jurisdiction Extension'' in qs.imi.cover.options_requested'
    action: refer
  reason: Considered because {qs.imi.exposure.us_ca_pct}% of your investors or funds are in the United States or Canada, or because you asked for it.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:imi.excl.us-canada-jurisdiction]] does not apply to claims brought or maintained in the United States of America or Canada, but only for the sections and subsidiaries shown in the schedule for this endorsement, and only for wrongful acts committed on or after the retroactive date.

Defence costs for those claims are included within the limit of liability and reduce it, unless Endorsement E07 is operative. Any sub-limit shown in the schedule for this endorsement is the most we will pay for all claims brought or maintained in the United States of America or Canada. It forms part of, and is not in addition to, the limit of liability for the section. Any additional excess shown in the schedule applies to those claims in place of the excess otherwise shown.

This endorsement does not cover fines, penalties, or punitive, exemplary or multiplied damages that are not insurable at law. [WP REVIEW: whether punitive and exemplary damages awarded in the United States should be excluded outright or only to the extent uninsurable in the jurisdiction of the award]

Schedule variables: sections and subsidiaries; sub-limit (optional); additional excess (optional).

---
id: cy.end.e05
type: endorsement
heading: E05 Increased Dependent Business Interruption Sub-limit
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.cy.cover.options_requested
  rules:
  - when: '''E05'' in qs.cy.cover.options_requested'
    action: broker_option
  reason: Offered because you rely on outside IT providers and asked for a higher limit for their outages.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

The sub-limit for [[ref:cy.ext.dependent-business-interruption]] is increased to the amount shown in the schedule for this endorsement.

Where the schedule names service providers for this endorsement, the increased sub-limit applies only to interruptions arising from dependent events affecting those named providers; the original sub-limit continues to apply to all other providers.

The waiting period applies on a threshold basis, as [[ref:cy.cover.business-interruption]] sets out.

Schedule variables: increased sub-limit; named providers (optional).

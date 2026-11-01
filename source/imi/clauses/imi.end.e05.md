---
id: imi.end.e05
type: endorsement
heading: E05 Custodian Failure — Enhanced
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.imi.governance.custodian_arrangement
  - qs.imi.governance.custodian_written_contract
  - qs.imi.cover.options_requested
  rules:
  - when: qs.imi.governance.custodian_arrangement = 'I hold the assets of at least one fund myself'
    action: refer
  - when: qs.imi.governance.custodian_written_contract = 'No'
    action: refer
  - when: '''E05 Custodian Failure — Enhanced'' in qs.imi.cover.options_requested'
    action: refer
  reason: Considered because of how the assets of your funds are held, or because you asked for it.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The last paragraph of [[ref:imi.ext.fund-assets-third-party-service-provider-failure]] is amended so that it does not exclude a claim made against you arising from the insolvency of a custodian shown in the schedule for this endorsement, or from the commingling by that custodian of fund assets with its own assets or the assets of its other clients. We will pay the amounts described in [[ref:imi.cover.financial-services-liability]] for that claim, up to the sub-limit shown in the schedule for this endorsement.

This endorsement applies only if the custodian is engaged under a written contract and you exercised reasonable care in selecting, appointing, and monitoring the custodian. It does not cover the loss of fund assets as such. That loss is covered only to the extent [[ref:imi.section.crime]] applies.

The sub-limit forms part of, and is not in addition to, the limit of liability for the section.

Schedule variables: custodians covered; sub-limit; additional excess (optional).

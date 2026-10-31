---
id: cy.end.e16
type: endorsement
heading: E16 Ransomware Exclusion
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.cy.security.mfa
  - qs.cy.security.offline_backups_tested
  rules:
  - when: qs.cy.security.mfa == no or qs.cy.security.offline_backups_tested == no
    action: refer
  reason: Applies because multi-factor authentication or tested offline backups are not in place, which are the controls that most reduce ransomware loss.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Do not attach
  - Decline risk
---

This endorsement applies where the schedule shows it, and is the default where multi-factor authentication for remote access and email, or offline backups tested in the last 12 months, are not in place.

For this policy:

- [[ref:cy.cover.cyber-extortion]] does not apply; and
- we do not pay any insured loss under [[ref:cy.cover.business-interruption]], [[ref:cy.cover.data-restoration]], [[ref:cy.ext.dependent-business-interruption]] or [[ref:cy.ext.bricking]] arising from ransomware, unless the schedule shows a ransomware sub-limit for this endorsement, in which case the most we will pay for all such insured loss is that sub-limit.

This endorsement does not affect [[ref:cy.cover.incident-response]] or any cover in [[ref:cy.section.third-party]]: we still pay incident response costs, and claims against you, arising from ransomware.

If you tell us during the policy period that the missing controls are now in place, and we agree, we will remove this endorsement from the date we agree, for any ransomware first occurring after that date.

Schedule variables: ransomware sub-limit (default none).

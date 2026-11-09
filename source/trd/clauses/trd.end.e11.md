---
id: trd.end.e11
type: endorsement
heading: E11 Subcontractors
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trd.business.subcontractor_pct
  rules:
  - when: qs.trd.business.subcontractor_pct > 60
    action: refer
  - when: qs.trd.business.subcontractor_pct > 0
    action: apply
  reason: Applies because you pay subcontractors. More than 60% of turnover paid to subcontractors is referred to an underwriter.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Decline risk
---

Before a subcontractor starts work for you, you must obtain a certificate of currency showing that the subcontractor holds public liability insurance with a limit of at least the amount shown for this endorsement, and keep it for 7 years.

[[ref:trd.section.liability|heading]] covers your liability arising from work your subcontractors do. It does not insure a subcontractor for its own liability.

If an occurrence arises from a subcontractor's work and you did not obtain the certificate, the special excess shown for this endorsement applies to that occurrence. We do not refuse the claim only because you did not obtain the certificate.

Schedule variables: minimum subcontractor limit (default: $5,000,000); special excess (default: $10,000).

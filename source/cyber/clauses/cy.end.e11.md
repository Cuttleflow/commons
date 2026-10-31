---
id: cy.end.e11
type: endorsement
heading: E11 United States and Canada Jurisdiction
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.cy.exposure.us_revenue_pct
  rules:
  - when: qs.cy.exposure.us_revenue_pct > 0
    action: refer
  reason: Considered because {qs.cy.exposure.us_revenue_pct}% of your revenue comes from customers in the United States or Canada.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:cy.cond.territory-and-jurisdiction]] does not exclude claims brought within, or judgments entered or enforced from, a court of the United States of America or Canada or their territories, and the covers in [[ref:cy.section.third-party]] apply to those claims.

For claims within the scope of this endorsement: (a) we will not pay punitive, exemplary, or multiple damages, or any fine or penalty; (b) defence costs are within the limit of liability, whatever [[ref:cy.end.e02]] provides; and (c) the most we will pay is the sub-limit shown in the schedule for this endorsement, if one is shown.

You must not admit liability, settle, or incur defence costs for any claim within the scope of this endorsement without our prior written consent, which we will not unreasonably withhold, and we may appoint counsel of our choosing.

Schedule variables: sub-limit (if any); additional premium.

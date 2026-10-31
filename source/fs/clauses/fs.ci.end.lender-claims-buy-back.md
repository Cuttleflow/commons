---
id: fs.ci.end.lender-claims-buy-back
type: endorsement
heading: Lender Claims Buy-back
profession: credit-intermediaries
since: 1.0.0
status: draft
note: Adds cover.
trigger:
  questions:
  - qs.fs.ci.aggregator
  - qs.fs.ci.lender_claims
  rules:
  - when: qs.fs.ci.lender_claims = yes
    action: refer
  - when: qs.fs.ci.lender_claims = no
    action: broker_option
  reason: Offered because lenders and aggregators may claim against you for errors in loan applications.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

Paragraph (a) of [[ref:fs.ci.excl.lender-claims]] does not apply. Paragraph (b), for commission clawback, continues to apply.

For claims by a credit provider, lender, mortgage manager or aggregator, the most we will pay in total, including defence costs, is the sub-limit shown in the schedule for this endorsement, which is part of the limit of liability.

---
id: ppl.end.e10
type: endorsement
heading: E10 USA and Canada
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.ppl.products.usa_canada_pct
  rules:
  - when: qs.ppl.products.usa_canada_pct > 0
    action: refer
  reason: Referred because {qs.ppl.products.usa_canada_pct}% of your products turnover goes to the USA or Canada.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:ppl.excl.usa-canada]] does not apply to the exposures shown in the schedule for this endorsement (for example, products exported to the USA and Canada directly or indirectly, or work performed there). The geographical limits include the USA and Canada for those exposures. For claims brought in a court in the USA and Canada, or to enforce a judgment or award of such a court:

- defence costs are part of, and not in addition to, the limit of liability;
- the sub-limit and excess shown for this endorsement apply; and
- we do not pay punitive, exemplary or aggravated damages, or the multiple part of any multiplied damages award.

Schedule variables: exposures covered; sub-limit (aggregate); excess.

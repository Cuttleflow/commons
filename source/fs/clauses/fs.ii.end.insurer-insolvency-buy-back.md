---
id: fs.ii.end.insurer-insolvency-buy-back
type: endorsement
heading: Insurer Insolvency Buy-back
profession: insurance-intermediaries
since: 1.0.0
status: draft
note: Adds cover.
trigger:
  questions:
  - qs.fs.ii.unrated_placements
  rules:
  - when: qs.fs.ii.unrated_placements = no
    action: broker_option
  - when: qs.fs.ii.unrated_placements = yes
    action: refer
  reason: Offered because you place business with insurers and want cover if one becomes insolvent.
---

We will not apply [[ref:fs.ii.excl.insurer-insolvency]] where, when you placed the business, the insurer or reinsurer was authorised by APRA, or held a financial strength rating of at least A- from S&P Global Ratings or an equivalent rating from another recognised agency.

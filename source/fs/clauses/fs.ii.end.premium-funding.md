---
id: fs.ii.end.premium-funding
type: endorsement
heading: Premium Funding
profession: insurance-intermediaries
since: 1.0.0
status: draft
note: Adds cover.
trigger:
  questions:
  - qs.fs.ii.premium_funding
  rules:
  - when: qs.fs.ii.premium_funding = yes
    action: broker_option
  reason: Offered because you arrange premium funding for clients.
---

Arranging premium funding for your clients, including as an introducer or agent of a premium funder, is a professional service under this policy, to the extent that you are authorised to provide it under your licence or any credit licence or exemption that applies.

This endorsement does not affect [[ref:fs.ii.excl.insurer-insolvency]], which continues to apply to the insolvency of a premium funder.

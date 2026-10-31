---
id: fs.ci.end.unregulated-commercial-finance
type: endorsement
heading: Unregulated Commercial Finance
profession: credit-intermediaries
since: 1.0.0
status: draft
note: Adds cover.
trigger:
  questions:
  - qs.fs.ci.commercial_pct
  rules:
  - when: qs.fs.ci.commercial_pct > 0
    action: broker_option
  reason: Offered because {qs.fs.ci.commercial_pct}% of your settlements are for unregulated commercial finance.
---

Arranging finance that is not regulated by the National Consumer Credit Protection Act 2009 (Cth), for borrowers who use it wholly or mainly for business or investment purposes, is a professional service under this policy.

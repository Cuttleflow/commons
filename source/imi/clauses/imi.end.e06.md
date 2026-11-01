---
id: imi.end.e06
type: endorsement
heading: E06 ESG and Greenwashing
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.imi.exposure.esg_labelled
  rules:
  - when: qs.imi.exposure.esg_labelled = 'Yes'
    action: suggest
  reason: Considered because one or more of your funds describes itself as ESG, sustainable, green or climate-focused.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

[[ref:imi.cover.financial-services-liability]] extends to any actual or alleged misleading or deceptive conduct, or negligent misstatement, in a statement or disclosure about the sustainability, environmental, social, governance or climate-related characteristics of a fund shown in the schedule for this endorsement, including a statement in a product disclosure statement, an investor communication, or marketing material.

[[ref:imi.cover.defence-of-regulatory-proceedings]] applies to an ASIC investigation or proceeding about a statement or disclosure of that kind.

This endorsement does not cover a fine or civil penalty that is not insurable at law. [[ref:imi.excl.dishonesty-and-fraud]] continues to apply. [WP REVIEW: whether civil penalty proceedings for greenwashing are insurable beyond defence costs]

Schedule variables: funds covered; sub-limit (optional).

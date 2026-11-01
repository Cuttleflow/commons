---
id: imi.end.e03
type: endorsement
heading: E03 Responsible Entity — Enhanced
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.imi.licence.roles
  - qs.imi.exposure.related_party_dealings
  rules:
  - when: '''Responsible entity'' in qs.imi.licence.roles and qs.imi.exposure.related_party_dealings = ''Yes'''
    action: suggest
  reason: Considered because you act as a responsible entity and a fund you operate deals with you or a related party of yours.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

[[ref:imi.cover.financial-services-liability]] extends to any actual or alleged breach by you, as responsible entity of a registered scheme shown in the schedule for this endorsement, of:

(a) the duties of a responsible entity under Chapter 5C of the Corporations Act 2001 (Cth), including the duty to act in the best interests of members and to give priority to the interests of members over your own;

(b) the scheme's constitution and compliance plan;

(c) the continuous disclosure obligations that apply to a scheme that is a disclosing entity; and

(d) the requirements that apply to a financial benefit given to you or to a related party of yours from scheme assets.

This endorsement does not cover the return or restitution of any financial benefit that you or a related party received. [[ref:imi.excl.personal-profit]] continues to apply.

Schedule variables: registered schemes covered; sub-limit (optional).

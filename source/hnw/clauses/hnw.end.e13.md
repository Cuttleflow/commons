---
id: hnw.end.e13
type: endorsement
heading: E13 Company or Trust as Insured
since: 1.0.0
status: draft
note: Contains 1 WP REVIEW tag for the Wording Partner.
trigger:
  questions:
  - qs.hnw.insured.entity_type
  rules:
  - when: qs.hnw.insured.entity_type == family_trust or qs.hnw.insured.entity_type == company
    action: apply
  reason: Applies because the home is owned by a company or the trustee of a trust.
  responses:
  - Attach
  - Do not attach
---

You are a company, or the trustee of a trust, that owns the home. The people named in the schedule for this endorsement live in the home, and they and their households are the household for this policy. They are insured for their own contents, valuables and personal liability as if each of them were named as an insured, and [[ref:hnw.cond.joint-insureds]] applies to them.

[WP REVIEW: confirm whether a policy issued to a company or a trustee for a home lived in by individuals is a retail product under s.761G(5) of the Corporations Act 2001 (Cth), and whether the occupants' cover makes it one in any case.]

Schedule variables: names of the people who live in the home.

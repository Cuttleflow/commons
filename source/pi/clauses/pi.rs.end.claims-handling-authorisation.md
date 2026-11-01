---
id: pi.rs.end.claims-handling-authorisation
type: endorsement
heading: Claims Handling Authorisation
profession: risk-safety-claims
since: 1.0.0
changed: 1.1.0
status: draft
note: Adds cover where scheduled. A claims manager whose main business is deciding claims under an insurer's authority is better placed on the Insurance Intermediaries wording.
trigger:
  questions:
  - qs.pi.rs.claims_decisions
  - qs.pi.rs.afsl_or_ar
  rules:
  - when: qs.pi.rs.claims_decisions = yes and qs.pi.rs.afsl_or_ar = yes
    action: apply
  - when: qs.pi.rs.claims_decisions = yes and qs.pi.rs.afsl_or_ar = no
    action: refer
  reason: Applies because you decide insurance claims on behalf of insurers.
---

Deciding and settling insurance claims on behalf of an insurer is a professional service under this policy while you are authorised to provide it under the Australian financial services licence, or as an authorised representative of the licensee, shown in the schedule.

For a claim arising from that service, [[ref:pi.excl.financial-services]] does not apply.

[WP REVIEW: confirm whether any compensation arrangement requirement under ASIC RG 126 applies to an insured who decides or settles claims under an Australian financial services licence, and whether this cover meets it.]

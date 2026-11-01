---
id: imi.end.e02
type: endorsement
heading: E02 Superannuation Trustee — Enhanced
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.imi.licence.roles
  - qs.imi.licence.rse_fum
  rules:
  - when: '''RSE licensee'' in qs.imi.licence.roles'
    action: refer
  - when: qs.imi.licence.rse_fum > 0
    action: refer
  reason: Considered because you act as a registrable superannuation entity licensee, managing {qs.imi.licence.rse_fum} $ million.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

This endorsement applies only if the schedule shows an RSE licence number. [[ref:imi.cover.financial-services-liability]] extends to any actual or alleged breach by you, as trustee of a registrable superannuation entity shown in the schedule, of:

(a) the best financial interests duty, the sole purpose test, and the other covenants and duties that apply to a trustee under the Superannuation Industry (Supervision) Act 1993 (Cth);

(b) the obligations that apply to a MySuper product, including the annual assessment of outcomes for members and the performance test;

(c) the obligations that apply to a choice product, including the obligations to compare and report on its performance; and

(d) the obligations that apply on the transfer of a stapled member's account.

Cover under this endorsement is for loss that is not paid or reimbursed from the assets of the fund. This endorsement does not cover any amount that a trustee is prohibited by law from paying or being reimbursed from the assets of a fund, or any fine or civil penalty that is not insurable at law. [WP REVIEW: the trustee indemnity and insurance restrictions in the Superannuation Industry (Supervision) Act 1993 (Cth), and whether the cover should be limited to defence costs for any civil penalty proceeding]

Schedule variables: RSE licence number; registrable superannuation entities and MySuper products covered; sub-limit (optional).

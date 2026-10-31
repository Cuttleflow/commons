---
id: pi.vt.end.pre-purchase-examinations
type: endorsement
heading: Pre-purchase Examinations Sub-limit
profession: veterinary
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.vt.prepurchase_count
  rules:
  - when: qs.pi.vt.prepurchase_count > 50
    action: suggest
  reason: Applies because you perform {qs.pi.vt.prepurchase_count} pre-purchase examinations a year.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

For all claims arising from pre-purchase or soundness examinations, the most we will pay in total, including defence costs, is the sub-limit shown in the schedule for this endorsement. The sub-limit is part of, and not in addition to, the limit of liability.

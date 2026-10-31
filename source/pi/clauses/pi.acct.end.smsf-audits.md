---
id: pi.acct.end.smsf-audits
type: endorsement
heading: SMSF Audits Sub-limit
profession: accountants
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.ac.smsf_audits_count
  rules:
  - when: qs.pi.ac.smsf_audits_count > 500
    action: suggest
  restrictions:
  - when: sub-limit < 500000
    action: refer
    note: ASIC registration conditions for approved SMSF auditors require cover of at least $500,000 (or the level set by a professional standards scheme).
  reason: Applies because you audit {qs.pi.ac.smsf_audits_count} self-managed superannuation funds a year.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

For all claims arising from audits of self-managed superannuation funds, the most we will pay in total, including defence costs, is the sub-limit shown in the schedule for this endorsement. The sub-limit is part of, and not in addition to, the limit of liability.

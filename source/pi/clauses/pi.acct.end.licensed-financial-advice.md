---
id: pi.acct.end.licensed-financial-advice
type: endorsement
heading: Licensed Financial Advice
profession: accountants
since: 1.0.0
status: draft
note: Adds cover. Records the scheduled licence that the base Financial Services exclusion carve-back requires.
trigger:
  questions:
  - qs.pi.ac.limited_afsl
  - qs.pi.ac.tfa_condition
  rules:
  - when: qs.pi.ac.limited_afsl = yes
    action: broker_option
  restrictions:
  - when: qs.pi.ac.limited_afsl = yes and limit of liability < the minimum under ASIC RG 126
    action: refer
    note: The limit must meet the ASIC RG 126 minimum for retail clients, which is higher than the Tax Practitioners Board minimum.
  reason: Offered because you give financial product advice under a limited AFS licence or as an authorised representative.
---

Financial product advice that you provide under a limited Australian financial services licence, or as an authorised representative of the holder of such a licence, is a professional service under this policy. The licence or authorisation is shown in the schedule.

For a claim arising from that advice, [[ref:pi.excl.financial-services]] does not apply.

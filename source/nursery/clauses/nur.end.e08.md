---
id: nur.end.e08
type: endorsement
heading: E08 Chemical Application for Others
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.nur.business.contract_spray_pct
  rules:
  - when: qs.nur.business.contract_spray_pct > 20
    action: refer
  - when: qs.nur.business.contract_spray_pct > 0
    action: apply
  reason: Applies because {qs.nur.business.contract_spray_pct}% of your turnover comes from applying chemicals for others.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:nur.li.excl-contracting]] is changed so that [[ref:nur.section.liability|heading]] covers your liability arising from applying chemicals by ground equipment for others for reward, where the income from it is no more than the share of turnover shown in the schedule.

- The person applying the chemical must hold any chemical user's accreditation or licence, and any commercial spraying or pest management licence, that the law requires for the work.
- The chemical must be used as its label and any permit direct, including the wind speed, droplet size and buffer zone requirements.
- You must keep the spray records the law requires, and give them to us with any claim.

The special excess applies to each claim for property damage caused by spray drift or to plants or turf you treated. We do not pay for the failure of a treatment to work. If a condition of this endorsement was not met, [[ref:nur.cond.insurance-contracts-act]] applies.

Schedule variables: share of turnover (default: 20%); special excess (default: $2,500).

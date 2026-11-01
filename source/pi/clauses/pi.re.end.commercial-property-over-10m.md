---
id: pi.re.end.commercial-property-over-10m
type: endorsement
heading: Commercial Property Value Exclusion
profession: real-estate-strata
since: 1.0.0
changed: 1.1.0
status: draft
note: The Property and Stock Agents Regulation 2022 (NSW) permits professional indemnity insurance to exclude work on commercial property above this value.
trigger:
  questions:
  - qs.pi.re.commercial_over_10m_pct
  rules:
  - when: qs.pi.re.commercial_over_10m_pct > 0
    action: suggest
  reason: Applies because some of your commercial work involves property worth more than $10 million.
---

We do not cover any claim, loss or liability arising from services for a commercial or industrial property, or a portfolio of such properties in one transaction, with a value of more than the amount shown in the schedule for this endorsement (or $10,000,000 if no amount is shown).

This endorsement does not apply to the extent that the law requiring you to hold this insurance permits an exclusion of this kind only above a higher amount, or does not permit it.

[WP REVIEW: confirm whether the NSW regulation prescribes the permitted threshold, so that the amount shown in the schedule cannot be lower.]

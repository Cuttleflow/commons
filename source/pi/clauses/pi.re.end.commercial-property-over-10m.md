---
id: pi.re.end.commercial-property-over-10m
type: endorsement
heading: Commercial Property over $10 Million Exclusion
profession: real-estate-strata
since: 1.0.0
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

We do not cover any claim, loss or liability arising from services for a commercial or industrial property, or a portfolio of such properties in one transaction, with a value of more than $10,000,000.

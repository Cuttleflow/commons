---
id: pi.acct.end.listed-entity-audits
type: endorsement
heading: Listed Entity Audits Exclusion
profession: accountants
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.ac.listed_audit_clients
  rules:
  - when: qs.pi.ac.listed_audit_clients > 0
    action: refer
  reason: Applies because you audit listed or APRA-regulated entities.
---

We do not cover any claim, loss or liability arising from an audit or review of the financial report of an entity listed on a securities exchange, or of an entity regulated by APRA.

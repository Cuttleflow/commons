---
id: trv.end.e07
type: endorsement
heading: E07 Business Meetings and Conferences
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trv.cover.business
  rules:
  - when: qs.trv.cover.business == yes
    action: broker_option
  reason: Offered as an option because a traveller will attend meetings or conferences.
  responses:
  - Attach
  - Do not attach
---

[[ref:trv.excl.business-travel]] does not apply to attending meetings, conferences and trade shows. Your business equipment is covered as portable electronics under [[ref:trv.cover.luggage]].

Schedule variables: none.

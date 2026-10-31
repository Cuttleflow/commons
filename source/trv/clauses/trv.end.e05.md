---
id: trv.end.e05
type: endorsement
heading: E05 Travel Within Australia
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trv.trip.region
  rules:
  - when: qs.trv.trip.region == domestic
    action: apply
  reason: Applied because the trip is within Australia.
  responses:
  - Attach
  - Do not attach
---

A trip within Australia is covered if it is more than 250 kilometres from your home or includes a flight or overnight accommodation. For such a trip, [[ref:trv.cover.medical]] covers only emergency transport home that is not a Medicare benefit, as [[ref:trv.pay.medicare]] provides, and the other sections apply as written.

Schedule variables: none.

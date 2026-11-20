---
id: gpa.spt.end.e19
type: endorsement
heading: E19 Personal Top-Up Cover
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.spt.top_up
  rules:
  - when: qs.gpa.spt.top_up == yes
    action: refer
  reason: Referred because individual top-up cover is a retail product that needs its own disclosure documents.
  responses:
  - Attach
  - Do not attach
---

A covered person who buys top-up cover from us, and whose name and top-up amounts are shown in the schedule or in a certificate we issue, has the higher capital sum and weekly benefit shown for them instead of their category's.

Schedule variables: top-up capital sum; top-up weekly benefit.

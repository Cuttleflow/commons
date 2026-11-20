---
id: ccl.end.e07
type: endorsement
heading: E07 Nominated Clients
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.ccl.cover.nominated_clients
  rules:
  - when: qs.ccl.cover.nominated_clients == true
    action: apply
  reason: Applies because you chose accidental damage cover for nominated clients.
---

The nominated clients and commodities for [[ref:ccl.section.nominated-clients|heading]] are those shown in the schedule for this endorsement. The special excess shown for a nominated client applies to each claim for goods carried for that client.

Schedule variables: nominated clients and commodities; special excess for each (default: the policy excess).

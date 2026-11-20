---
id: gpa.spt.end.e18
type: endorsement
heading: E18 Concussion Assessment Benefit
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.spt.concussion
  rules:
  - when: qs.gpa.spt.concussion == yes
    action: apply
  reason: Applied because the policyholder buys the concussion assessment benefit.
  responses:
  - Attach
  - Do not attach
---

If a covered person suffers a suspected concussion while taking part in a sporting activity, we will pay the reasonable cost of an assessment by a medical practitioner, and of any tests the medical practitioner orders, up to the amount shown in the schedule (default $500) for each incident. We pay this whether or not a concussion is diagnosed, but only to the extent the costs are non-Medicare medical expenses.

Schedule variables: limit for each incident.

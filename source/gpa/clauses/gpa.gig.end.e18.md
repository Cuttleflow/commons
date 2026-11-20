---
id: gpa.gig.end.e18
type: endorsement
heading: E18 Parcel and Last-Mile Delivery
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.gig.parcel
  rules:
  - when: qs.gpa.gig.parcel == yes
    action: refer
  reason: Referred because the platform asks for cover for parcel or last-mile delivery.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

Platform work includes the delivery of parcels and other goods through the platform, in a vehicle with a gross vehicle mass no more than the amount shown in the schedule (default 4.5 tonnes). The premium for parcel and last-mile delivery is charged at the rate shown in the schedule.

Schedule variables: kinds of goods; maximum gross vehicle mass; rate for each engaged hour.

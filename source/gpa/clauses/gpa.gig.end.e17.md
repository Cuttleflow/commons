---
id: gpa.gig.end.e17
type: endorsement
heading: E17 Passenger Transport
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.gig.rideshare
  rules:
  - when: qs.gpa.gig.rideshare == yes
    action: refer
  reason: Referred because the platform asks for cover for passenger transport.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

Platform work includes carrying passengers for reward through the platform, in a vehicle that meets the requirements of the law of the state or territory where the trip happens. For passenger transport, engaged time ends 15 minutes after the last passenger leaves the vehicle, unless you accept another request first. The premium for passenger transport is charged at the rate shown in the schedule.

Schedule variables: passenger transport services covered; rate for each engaged hour.

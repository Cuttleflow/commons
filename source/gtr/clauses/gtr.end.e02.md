---
id: gtr.end.e02
type: endorsement
heading: E02 Leisure Extension
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gtr.cover.leisure_days
  - qs.gtr.cover.directors_leisure
  rules:
  - when: qs.gtr.cover.directors_leisure == yes
    action: broker_option
  - when: qs.gtr.cover.leisure_days > 7
    action: broker_option
  reason: Offered because the policyholder asked for more leisure travel than the base wording allows.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

Leisure travel by an insured person immediately before or after a business trip is part of the trip for up to the number of days shown in the schedule for this endorsement, in place of the number in [[ref:gtr.cover.trip]], and the leisure part may be longer than the business part. Directors and officers named in the schedule for this endorsement are also covered on leisure trips with no business purpose.

Schedule variables: leisure days for each trip (7 to 21, default 14); directors and officers covered for leisure-only trips.

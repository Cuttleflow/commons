---
id: mot.end.e06
type: endorsement
heading: E06 Increased Windscreen Cover
since: 3.0.0
status: draft
trigger:
  questions:
  - qs.mot.cover.windscreen_increased
  rules:
  - when: qs.mot.cover.windscreen_increased == true
    action: broker_option
  reason: Offered as an option to increase the windscreen benefit.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

The windscreen and window glass additional benefit is increased to the amount shown in the Schedule for each Occurrence, and includes the recalibration of cameras and sensors mounted on the glass.

Schedule variables: windscreen limit each Occurrence.

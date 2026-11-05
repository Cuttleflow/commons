---
id: pcl.end.e04
type: endorsement
heading: E04 Wine Temperature Failure
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pcl.collection.wine_temperature
  rules:
  - when: qs.pcl.collection.wine_temperature == yes
    action: apply
  reason: Applies because cover for wine temperature failure was chosen.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Do not attach
---

We cover wine in your collection that is spoiled by a sudden failure of the temperature or humidity control of the cellar or wine storage unit at the premises, despite [[ref:pcl.excl.temperature]].

We do not pay for spoilage caused by a failure that you knew of and did not take reasonable steps to fix, or that lasted less than the number of consecutive hours shown in the schedule for this endorsement. The most we pay for any one event is the amount shown in the schedule for this endorsement.

Schedule variables: minimum hours of failure (default 24); limit any one event (default 25% of the wine category sum insured).

---
id: ccl.end.e05
type: endorsement
heading: E05 Sea Leg to Tasmania and Islands
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.ccl.operations.sea_leg
  rules:
  - when: qs.ccl.operations.sea_leg == true
    action: apply
  reason: Applies because your transits include a sea leg to Tasmania or an island.
---

Goods are covered while the conveying vehicle, or the goods, cross Bass Strait or travel by sea to Kangaroo Island, the Whitsunday islands or another Australian island named in the schedule, as part of an insured transit. During the sea leg, [[ref:ccl.cover.basic-load|heading]] covers the sea events listed in it, and [[ref:ccl.ext.general-average]] applies. The goods must be stowed in or on the conveying vehicle, or in a container, and not on deck unless the vehicle itself is carried on deck.

Schedule variables: the islands named.

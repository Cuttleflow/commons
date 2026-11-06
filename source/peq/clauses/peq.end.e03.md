---
id: peq.end.e03
type: endorsement
heading: E03 Piling and Foundation Rigs
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.peq.plant.piling_rig
  rules:
  - when: qs.peq.plant.piling_rig == yes
    action: refer
  reason: Referred because a piling or foundation rig is to be insured.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

This endorsement applies to each piling rig, drilling rig and other foundation rig that is insured plant.

**Working platform.** A rig must work only on a working platform designed by a competent person for the rig's bearing pressures, with a working platform certificate in place before the rig moves onto it. We do not pay for loss or damage caused by the rig overturning, or by the platform failing, where no working platform certificate was in place.

**Tools in the ground.** We do not pay for the loss of augers, casings, drill strings, hammers or other tools left in the ground, or the cost of recovering them, unless the schedule shows a limit for this endorsement.

The rig excess shown in the schedule applies instead of the item's excess, where it is higher.

Schedule variables: rigs covered; rig excess (default 10% of the loss, minimum $10,000); tools in the ground limit (default nil).

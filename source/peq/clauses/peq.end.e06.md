---
id: peq.end.e06
type: endorsement
heading: 'E06 Hired-Out Plant: Plant Hire Businesses'
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.peq.ops.dry_hire
  - qs.peq.ops.damage_waiver
  rules:
  - when: qs.peq.ops.dry_hire == yes or qs.peq.ops.damage_waiver == yes
    action: refer
  reason: Referred because plant is hired out on dry hire, or hirers are offered a damage waiver.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

This endorsement applies where the named insured hires plant out as a business.

**Standard hire terms.** [[ref:peq.cond.hired-out-plant]] is met for dry hire if the named insured hires out under the standard hire agreement it has given us, or one that is no less protective of its rights. It must tell us before it changes those terms.

**Damage waiver.** Where the named insured offers hirers a damage waiver on terms it has told us about, cover continues while the plant is on hire under the waiver, and we do not seek to recover from the hirer to the extent of the waiver. The damage waiver excess shown in the schedule applies to loss or damage while the plant is on hire under a waiver.

**Conversion by a hirer.** We pay for the loss of an item of insured plant that a hirer fails to return and keeps or sells as its own, up to the conversion limit shown in the schedule for any one event, if before the hire the named insured verified the hirer's identity with photographic identification and a business or residential address it confirmed.

**Not covered.** We do not pay for loss or damage to plant while on hire for use outside the geographical limits.

Schedule variables: standard hire agreement reference; damage waiver terms; damage waiver excess (default twice the item's excess); conversion limit (default $100,000 for any one event).

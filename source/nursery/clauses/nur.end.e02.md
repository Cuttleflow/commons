---
id: nur.end.e02
type: endorsement
heading: E02 Glasshouse Glazing
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.nur.property.glasshouses
  rules:
  - when: qs.nur.property.glasshouses == yes
    action: apply
  reason: Applies because your property includes glasshouses or polytunnels.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:nur.section.property|heading]] is changed so that it also covers the accidental breakage of the glass, polycarbonate or acrylic glazing of a glasshouse, and the accidental tearing of its plastic film covering, where an insured event did not cause it.

The most we pay for accidental breakage and tearing that an insured event did not cause is the glazing sub-limit for one event. The special excess applies to each claim for damage to glazing or coverings by hail, and to each claim for accidental breakage or tearing. We do not pay for breakage or tearing during the installation, removal or repair of the glazing or covering, or for scratching or discolouration.

Schedule variables: glazing sub-limit (default: $25,000); special excess (default: $2,500).

---
id: frm.end.e01
type: endorsement
heading: E01 Flood Cover
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.frm.cover.flood_buyback
  rules:
  - when: qs.frm.cover.flood_buyback == yes
    action: refer
  reason: Referred because you asked for flood cover, which the underwriter prices for the farm location's flood exposure.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:frm.fp.exclusions]], [[ref:frm.fi.exclusions]] and [[ref:frm.fp.insured-events]] are changed so that flood is an insured event under [[ref:frm.section.farm-property|heading]], a cause of death covered under [[ref:frm.section.livestock|heading]], and a cause of interruption covered under [[ref:frm.section.farm-interruption|heading]].

The most we pay for all damage and loss caused by flood in the policy period is the flood sub-limit. The flood excess applies to each flood event instead of the section's excess. We do not pay for damage by flood caused during the first 72 hours after this endorsement is first attached, unless it replaces, without a break, cover for flood for the same property.

Schedule variables: flood sub-limit (default: the farm property sum insured); flood excess (default: $5,000).

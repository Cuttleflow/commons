---
id: frm.end.e02
type: endorsement
heading: E02 Fabric Structures
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.frm.property.fabric_shelters
  rules:
  - when: qs.frm.property.fabric_shelters == yes
    action: apply
  reason: Applies because farm property includes fabric structures, such as hay covers, poly tunnels or fabric sheds.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:frm.fp.exclusions]] is changed so that storm damage to a fabric structure, and to property inside it, is covered under [[ref:frm.section.farm-property|heading]].

The most we pay for all damage to fabric structures by storm in one event is the fabric structures sub-limit, and the special excess applies to each such claim. We pay for the fabric covering at its market value, allowing for its age, if it is more than 5 years old.

Schedule variables: fabric structures sub-limit (default: $50,000); special excess (default: $2,500).

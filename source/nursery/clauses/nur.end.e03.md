---
id: nur.end.e03
type: endorsement
heading: E03 Plants in the Open
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.nur.property.plants_in_open
  rules:
  - when: qs.nur.property.plants_in_open == yes
    action: apply
  reason: Applies because plant stock is grown or held in the open at the situation.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:nur.prp.exclusions]] is changed so that storm, wind, rain and hail damage to plants in the open is covered under [[ref:nur.section.property|heading]].

The most we pay for all storm, wind, rain and hail damage to plants in the open in one event is the plants in the open sub-limit, and the special excess applies to each such claim. Where the schedule shows that hail netting covers plants in the open, keep the netting in a reasonable state of repair and close it when hail is forecast where it is designed to be closed. [[ref:nur.cond.insurance-contracts-act]] applies to these requirements.

Schedule variables: plants in the open sub-limit (default: the plants in the open share of the property sum insured); special excess (default: $2,500); hail netting (default: not shown).

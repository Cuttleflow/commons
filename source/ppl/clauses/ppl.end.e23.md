---
id: ppl.end.e23
type: endorsement
heading: E23 Communicable Disease Write-back
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.ppl.ops.public_contact_premises
  - qs.ppl.ops.infection_control_plan
  rules:
  - when: qs.ppl.ops.public_contact_premises == yes and qs.ppl.ops.infection_control_plan == yes
    action: refer
  reason: Referred because members of the public gather in close contact at your premises.
  responses:
  - Attach with amended sub-limit
  - Attach with special excess
  - Do not attach
---

[[ref:ppl.excl.communicable-disease]] does not apply to personal injury to a member of the public arising from the transmission of a communicable disease at your premises, if at the time you complied with any public health order and with the infection control measures you told us about in your proposal. We do not cover any claim arising from a pandemic or epidemic declared by the World Health Organization or by an Australian government. The aggregate sub-limit and special excess shown for this endorsement apply.

Schedule variables: aggregate sub-limit; special excess; infection control measures relied on.

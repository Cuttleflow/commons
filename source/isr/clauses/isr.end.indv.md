---
id: isr.end.indv
type: endorsement
heading: INDV Indemnity Value for Specified Property
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.values.indemnity_items
  rules:
  - when: qs.isr.values.indemnity_items == yes
    action: suggest
  reason: Suggested because some property is vacant, obsolete or awaiting demolition.
---

For the property listed in the Schedule for this endorsement, we pay indemnity value instead of the cost of reinstatement or replacement. Indemnity value is the cost of reinstating the property at the time of the Damage, less an allowance for wear, tear, depreciation and obsolescence, and not more than its market value immediately before the Damage. The Declared Value of that property must be stated on the same basis for the co-insurance test.

Schedule variables: property or buildings to which indemnity value applies.

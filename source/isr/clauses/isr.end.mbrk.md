---
id: isr.end.mbrk
type: endorsement
heading: MBRK Machinery Breakdown
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.risk.pressure_vessels
  - qs.isr.bi.breakdown_bi_requested
  rules:
  - when: qs.isr.risk.pressure_vessels == yes
    action: refer
  - when: qs.isr.bi.breakdown_bi_requested == yes
    action: refer
  - when: '''MBRK'' in qs.isr.cover.options_requested'
    action: broker_option
  reason: Offered as an option for machinery breakdown; referred for boilers, pressure vessels or turbines, or business interruption after breakdown.
---

Any breakdown exclusion in the Base Wording does not apply to the plant and machinery listed in the Schedule, or to all plant and machinery at a Situation if the Schedule says so. We cover sudden and unforeseen physical Damage to that plant caused by mechanical or electrical breakdown, including Damage to the machine in which the breakdown starts, while it is working, at rest, or being cleaned, overhauled or moved within the Situation.

- We do not pay for wear and tear or gradual deterioration; routine maintenance; parts that need periodic replacement (such as tools, dies, belts, chains, tyres, filters, refractory linings and fuses); breakdown for which a manufacturer or supplier is responsible under contract or law; or tests, experiments or deliberate overloading.
- Business Interruption loss resulting from breakdown is covered only if the Schedule says so, and then with the time excess shown.
- Keep the plant maintained as its manufacturer recommends. The Insurance Contracts Act 1984 (Cth), including its section 54, applies to this condition.

Schedule variables: plant list or "all plant"; sub-limit; deductible; business interruption following breakdown (yes or no) and time excess.

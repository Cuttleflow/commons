---
id: isr.end.accs
type: endorsement
heading: ACCS Prevention of Access
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.bi.evacuation_option_high_hazard
  rules:
  - when: qs.isr.bi.evacuation_option_high_hazard == yes
    action: refer
  - when: '''ACCS'' in qs.isr.cover.options_requested'
    action: broker_option
  reason: Offered as an option for prevention of access, including non-damage cover.
---

We cover Business Interruption loss when access to or use of a Situation is prevented or hindered by:

- Damage, by a cause that this Policy would cover, to property within the radius shown in the Schedule, whether or not the property is yours; or
- the action of a lawful authority, because of a danger or emergency within the radius shown, whether or not there is Damage.

If the Schedule says so, the second limb includes evacuation orders for bushfire, flood or cyclone. We do not cover an order relating to a communicable disease (see COMX and COMB), or an order made because you breached a law or licence. Cover starts after the waiting period, lasts no longer than the maximum period, and is limited to the sub-limit, each as shown in the Schedule.

Schedule variables: radius (default 1 kilometre); natural peril evacuation orders included (yes or no); waiting period; maximum period; sub-limit.

---
id: isr.end.util
type: endorsement
heading: 'UTIL Public Utilities: Extended'
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.bi.utilities_any_cause
  rules:
  - when: qs.isr.bi.utilities_any_cause == yes
    action: refer
  - when: '''UTIL'' in qs.isr.cover.options_requested'
    action: broker_option
  reason: Offered as an option to extend public utilities cover.
---

We cover Business Interruption loss caused by failure of the utilities listed in the Schedule (electricity, gas, water, sewerage or telecommunications) to supply the Situation. The Schedule states whether the failure must be caused by Damage to the supplier's property or may arise from any accidental cause, and whether the supplier's property is covered up to the Situation's terminal point or only at named facilities. We do not cover rationing or load-shedding by a supply authority, unless it follows Damage to its network; drought or lack of supply capacity; strikes; or a cyber event (see CYBX). Cover starts after the waiting period and is limited to the sub-limit shown.

Schedule variables: utilities; trigger (damage or any accidental cause); network extent; waiting period; sub-limit.

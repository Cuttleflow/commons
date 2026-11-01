---
id: do.end.e08
type: endorsement
heading: E08 Side A Standalone / Excess DIC
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.do.cover.options_requested
  rules:
  - when: "'E08' in qs.do.cover.options_requested"
    action: broker_option
  reason: Offered because you asked for a Side A difference-in-conditions layer for the insured persons.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

It converts Side A into a standalone excess and difference-in-conditions layer, with drop-down triggers.

**Excess Function**

Side A of this policy operates as an excess layer above the primary D&O insurance identified in the schedule as the “Primary D&O Policy.” Side A responds when the insured person's non-indemnifiable loss exceeds the limit of the Primary D&O Policy.

**DIC Drop-Down**

Side A will drop down and respond from the ground up (or from a self-insured retention specified in the schedule) for non-indemnifiable loss if the Primary D&O Policy fails to respond because of: (a) insolvency of the primary insurer; (b) aggregate exhaustion of the Primary D&O Policy; (c) avoidance of the Primary D&O Policy on grounds of non-disclosure or misrepresentation (but not where the insured person seeking cover personally caused that avoidance); (d) coverage denial based on a breach of condition by the company (not the insured person); (e) an exclusion in the Primary D&O Policy that does not appear in this policy; or (f) cancellation or non-renewal of the Primary D&O Policy (other than by the company for non-payment).

**Non-Avoidance**

Side A under this endorsement is non-avoidable on the terms of [[ref:do.cond.non-avoidance-side-a]].

**Independent Limits**

The Side A limit under this endorsement is separate from and in addition to the limits available under Side B and Side C.

Schedule variables: Primary D&O policy; Side A limit; self-insured retention.

---
id: do.end.e08
type: endorsement
heading: E08 Side A Standalone / Excess DIC
since: 1.3.0
changed: 1.4.0
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

Side A of this policy operates as an excess layer above the primary D&O insurance identified in the schedule as the “Primary D&O Policy”. Side A responds when the insured person's non-indemnifiable loss exceeds the limit of the Primary D&O Policy. This policy is excess of that specified policy for the purposes of [[ref:do.pay.other-insurance]].

**DIC Drop-Down**

Side A will drop down and respond from the ground up (or from the DIC retention shown in the schedule) for non-indemnifiable loss if the Primary D&O Policy fails to respond because of: (a) insolvency of the primary insurer; (b) aggregate exhaustion of the Primary D&O Policy; (c) avoidance of the Primary D&O Policy on grounds of non-disclosure or misrepresentation (but not where the insured person seeking cover personally caused that avoidance); (d) coverage denial based on a breach of condition by the company (not the insured person); (e) an exclusion in the Primary D&O Policy that does not appear in this policy; or (f) cancellation or non-renewal of the Primary D&O Policy (other than by the company for non-payment).

The DIC retention applies only to loss paid under this drop-down. It does not apply to loss above the limit of the Primary D&O Policy.

**Presumptive Indemnification**

When deciding whether loss is non-indemnifiable loss, we presume that the company will indemnify the insured person to the extent the law permits and the company is financially able. The presumption does not apply if the company is insolvent, or has refused or failed to indemnify. Uncertainty about whether the company will indemnify does not entitle us to withhold or delay advancement of defence costs once this endorsement responds. [WP REVIEW: confirm that this presumption, and its limits, are workable and consistent with the Non-indemnifiable loss definition.]

**Maintenance of the Primary D&O Policy**

The company must keep the Primary D&O Policy in force, on the terms and limits shown in the schedule, for the policy period, and tell us promptly if it is cancelled, not renewed, or its limits or terms are reduced. If it is not kept in force, drop-down under paragraphs (a) to (f) above is available only to the extent the Primary D&O Policy would have responded had it been maintained, and only as section 54 of the Insurance Contracts Act 1984 (Cth) allows (see [[ref:do.cond.insurance-contracts-act-1984-cth]]).

**Non-Avoidance**

Side A under this endorsement is non-avoidable on the terms of [[ref:do.cond.non-avoidance-side-a]].

**Limits**

The Side A limit under this endorsement is the Side A limit shown in Items 3(a) and 3(b) of the schedule. It is part of, not in addition to, the Overall Aggregate in Item 3(g). Payments under Side A rank first under [[ref:do.pay.priority-of-payment]].

Schedule variables: Primary D&O policy; DIC retention.

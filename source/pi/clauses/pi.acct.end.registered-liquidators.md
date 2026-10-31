---
id: pi.acct.end.registered-liquidators
type: endorsement
heading: Registered Liquidators
profession: accountants
since: 1.0.0
status: draft
note: Adds cover. ASIC RG 258 requires registered liquidators to hold adequate and appropriate professional indemnity and fidelity insurance, and ASIC asks whether cover includes run-off if the firm becomes
  insolvent.
trigger:
  questions:
  - qs.pi.ac.registered_liquidator
  rules:
  - when: qs.pi.ac.registered_liquidator = yes
    action: apply
  restrictions:
  - when: qs.pi.ac.registered_liquidator = yes and this endorsement is not attached
    action: refer
    note: ASIC RG 258 requires fidelity cover, and asks about run-off cover, for registered liquidators. The quote cannot proceed without this endorsement unless an underwriter confirms that the liquidator
      holds this cover elsewhere.
  reason: Applies because a principal is a registered liquidator.
---

This endorsement applies to you while you, or an insured person, are registered as a liquidator under the Corporations Act 2001 (Cth).

**Appointment money.** Despite [[ref:pi.excl.deliberate-and-dishonest-acts]], we will pay the loss of money or property that you hold as an external administrator, liquidator, receiver or trustee, caused by the dishonest or fraudulent conduct of an employee or of a person you engage to assist with the appointment. The most we will pay for all such losses in the policy period is the sub-limit shown in the schedule for this endorsement, which is part of the limit of liability.

**Run-off.** If you cease to practise as a registered liquidator, or the company becomes insolvent, during the policy period, [[ref:pi.ext.run-off-cover]] continues for claims arising from your appointments for the period shown in the schedule for this endorsement, of up to seven years after the end of the policy period, on payment of the premium shown in the schedule.

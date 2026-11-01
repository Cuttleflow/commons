---
id: sa.end.e04
type: endorsement
heading: E04 Difference in Conditions
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.sa.cover.options_requested
  rules:
  - when: "'E04' in qs.sa.cover.options_requested"
    action: broker_option
  reason: Offered because you asked for drop-down cover for the insured persons if the underlying D&O insurance does not pay.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

This endorsement applies only where the schedule shows that it applies.

Where it applies, we will also pay an insured person's non-indemnifiable loss, in excess of the DIC retention shown in the schedule, where the underlying D&O insurance does not pay that loss for any of the reasons below. The loss must be loss that [[ref:sa.cover.side-a-excess-cover]] would cover if the underlying D&O insurance had responded and the attachment point had been exhausted, and that [[ref:sa.section.exclusions]] does not exclude.

(a) the underlying insurer is insolvent, is placed into liquidation, or is otherwise unable to pay;

(b) the underlying insurer denies cover for the claim, or avoids or cancels the underlying D&O insurance, because of: (i) a breach of the duty of disclosure or a misrepresentation in the application for the underlying D&O insurance, made without the knowledge of the insured person seeking cover; (ii) a failure by the company (not the insured person) to comply with a condition of the underlying D&O insurance; (iii) an exclusion in the underlying D&O insurance that is not in [[ref:sa.section.exclusions]]; or (iv) a provision of the underlying D&O insurance that attributes the knowledge or conduct of one insured person to another, innocent insured person; or

(c) the underlying D&O insurance is cancelled or not renewed (other than by the company for non-payment of premium), and the company has been unable to obtain replacement cover on substantially similar terms. For this purpose, the company must have asked at least two insurers, through its broker and in writing, for replacement cover with a limit no lower than the expiring limit and no exclusion or restriction that the expiring cover did not have, and must give us copies of the requests and the replies. Replacement cover is substantially similar if it meets that test.

For cover under this endorsement, [[ref:sa.cover.no-drop-down]] does not apply, and this policy does not follow the exclusions of the underlying D&O insurance; only the exclusions in [[ref:sa.section.exclusions]] apply.

This endorsement does not apply where: (a) the insured person seeking cover personally participated in the conduct that caused the underlying insurer to deny or avoid cover; or (b) the company voluntarily cancelled the underlying D&O insurance and the insured person knew of the cancellation but did not tell us.

Payments under this endorsement reduce the limit of liability. They are part of it, not in addition to it.

When we pay under this endorsement, we also take over the insured person's rights against the underlying insurer, under [[ref:sa.cond.subrogation-and-recovery]].

Schedule variables: DIC retention.

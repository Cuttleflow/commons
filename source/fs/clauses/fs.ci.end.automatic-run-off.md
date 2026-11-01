---
id: fs.ci.end.automatic-run-off
type: endorsement
heading: 12-Month Automatic Run-off
profession: credit-intermediaries
since: 1.0.0
changed: 1.1.0
status: draft
note: Adds cover. ASIC RG 210 requires credit licensees to make reasonable efforts to obtain at least 12 months of automatic run-off cover.
trigger:
  questions:
  - qs.fs.ci.ceasing
  rules:
  - when: qs.fs.ci.ceasing = yes
    action: apply
  restrictions:
  - when: qs.fs.ci.ceasing = yes and this endorsement is not attached
    action: refer
    note: ASIC RG 210 requires reasonable efforts to obtain 12 months automatic run-off. The platform records that it was offered and why it was not attached.
  reason: Applies because you intend to cease credit activities, and ASIC expects you to have 12 months of run-off cover.
---

If you cease to hold your Australian credit licence, or cease to be a credit representative, during the policy period, this policy continues, without additional premium, for claims first made against you and notified to us within 12 months after the end of the policy period, arising from professional services provided before you ceased.

All other terms of this policy, including the limit of liability, continue to apply to those claims.

This endorsement works with [[ref:fs.ext.run-off-cover]] as follows:

- ceasing to hold your Australian credit licence, or ceasing to be a credit representative, is ceasing to practise for the purposes of [[ref:fs.ext.run-off-cover]];
- the 12-month period in this endorsement applies despite the statement in [[ref:fs.ext.run-off-cover]] that automatic cover ends at the end of the policy period; and
- if an extension under [[ref:fs.ext.run-off-cover]] also applies, the longer period applies, and the limit of liability is not increased.

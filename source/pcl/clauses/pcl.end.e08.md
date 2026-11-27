---
id: pcl.end.e08
type: endorsement
heading: E08 Self-Managed Superannuation Fund
since: 1.0.0
status: draft
note: Contains a WP REVIEW tag for the Wording Partner.
trigger:
  questions:
  - qs.pcl.insured.owner_type
  - qs.pcl.insured.smsf_related_party_storage
  rules:
  - when: qs.pcl.insured.owner_type == smsf
    action: apply
  restrictions:
  - when: qs.pcl.insured.owner_type == smsf and qs.pcl.insured.smsf_related_party_storage == yes
    action: refer
    note: Superannuation law does not allow a fund's collectables to be kept at a related party's private residence. The underwriter must see the arrangement before cover is offered.
  reason: Applies because the collection is owned by a self-managed superannuation fund.
  responses:
  - Attach
  - Do not attach
  - Decline risk
---

The insured is the trustee of the self-managed superannuation fund named in the schedule, in that capacity only. We pay any claim to the trustee for the fund.

The collection must not be kept in, or used at, the private residence of a member of the fund or of a related party of the fund. If it is, [[ref:pcl.cond.insurance-contracts-act]] applies.

[WP REVIEW: confirm that this endorsement is consistent with reg 13.18AA of the Superannuation Industry (Supervision) Regulations 1994 on the storage and insurance of collectables and personal use assets, including the requirement that the insurance be in the fund's name within 7 days of acquisition.]

Schedule variables: fund name; trustee.

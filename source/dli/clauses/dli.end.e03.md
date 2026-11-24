---
id: dli.end.e03
type: endorsement
heading: E03 Outstanding Defects at Completion
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.dli.tis.final_report_defects
  rules:
  - when: qs.dli.tis.final_report_defects == outstanding_listed
    action: apply
  reason: Applies because the final technical inspection report lists defects that were outstanding at completion.
  responses:
  - Attach
  - Attach with special excess
  - Do not attach
  - Decline risk
---

The defects listed as outstanding in the final technical inspection report are set out in the schedule for this endorsement. The developer must arrange for the builder to rectify them, and the technical inspector must confirm in writing that each has been rectified.

For each listed defect, [[ref:dli.cover.relevant-defects]] applies from the earlier of:

- the date the technical inspector confirms that it has been rectified; and
- the cover start date for listed defects shown in the schedule.

From that date, a listed defect that is a relevant defect is covered in the same way as any other relevant defect. This endorsement does not affect the cover for any defect that is not listed.

Schedule variables: the listed defects; cover start date for listed defects (default six months after the occupation certificate).

[WP REVIEW: confirm that deferring cover for defects listed as outstanding at completion, for at most the period shown, is consistent with s.211AA and acceptable to the Secretary.]

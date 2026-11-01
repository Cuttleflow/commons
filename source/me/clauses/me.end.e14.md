---
id: me.end.e14
type: endorsement
heading: E14 Day Surgery and Procedure Centre
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.me.ops.facility_categories
  - qs.me.ops.overnight_stays
  rules:
  - when: '''day_surgery'' in qs.me.ops.facility_categories and qs.me.ops.overnight_stays == yes'
    action: refer
  - when: '''day_surgery'' in qs.me.ops.facility_categories'
    action: apply
  reason: Applies because you operate a day surgery or procedure centre.
---

This endorsement applies where the company operates one or more facilities shown in the schedule in the category day surgery or procedure centre: facilities licensed for same-day surgical or procedural care, including endoscopy centres, ophthalmic and dermatological surgery centres, and other day procedure centres. [[ref:me.excl.medical-practitioners]] continues to apply.

**Additional obligations.** These are added to [[ref:me.section.obligations]] and operate on the same basis:

- (a) Hospital transfer plan. The company must maintain, and review at least annually, a documented hospital transfer plan for the management of patient deterioration and unexpected complications at each facility, including escalation and resuscitation protocols, arrangements with a receiving hospital capable of accepting the facility's patients within a reasonable transfer time, and ambulance and transfer logistics, and provide evidence of the current plan and its last review to us on request.
- (b) Infection control and reprocessing. The company must comply with AS/NZS 4187:2014 (Reprocessing of Reusable Medical Devices in Health Service Organisations), or its successor standard as applicable to the facility. Current accreditation under the National Safety and Quality Health Service (NSQHS) Standards is accepted as evidence of compliance.
- (c) State and territory licensing. The company must hold and maintain a current licence, approval or registration to operate each facility as a day surgery or day procedure centre under the applicable health facility legislation, including the Private Health Facilities Act 2007 (NSW), the Health Services Act 1988 (Vic) and the Private Health Facilities Act 1999 (Qld), provide evidence of it on request, and tell us as soon as reasonably practicable if a licence is suspended, cancelled or made subject to material conditions.

**Additional exclusions.** We do not cover any claim, inquiry, loss or liability arising from:

- (a) Obstetrics services. [[ref:me.excl.obstetrics]] applies without the availability of Endorsement E01: obstetrics cover is not available for day surgery and procedure centres. The carve-out for emergency treatment under [[ref:me.ext.good-samaritan]] continues to apply.
- (b) Overnight inpatient care. The care of a patient retained at a facility overnight, where the retention was neither required by a clinical emergency (including a deterioration managed under the hospital transfer plan pending transfer) nor pre-approved by us in writing. A facility operating as a hospital requires Endorsement E15. Cover for the same-day elements of an episode of care is not affected.

**Anaesthetic services.** Cover under [[ref:me.cover.healthcare-operations]] and [[ref:me.cover.vicarious-liability]] extends to the company's vicarious liability, and its liability for breach of a non-delegable duty of care, arising from anaesthetic services provided at a facility by a visiting anaesthetist (a visiting medical officer), including the company's own system failures in anaesthetic booking, pre-admission screening, equipment, monitoring and recovery staffing. The anaesthetist's own liability is never covered: every anaesthetist must hold their own medical indemnity insurance, verified through the company's credentialing processes.

**Same-day discharge systems.** Administrative and system error under [[ref:me.cover.healthcare-operations]] includes failures of the company's pre-admission assessment, discharge criteria, post-discharge instruction and follow-up contact systems for same-day patients.

Schedule variables: facilities in this category.

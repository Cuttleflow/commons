---
id: me.end.e15
type: endorsement
heading: E15 Private Hospital
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.me.ops.has_private_hospital
  - qs.me.hospital.beds
  - qs.me.hospital.high_risk_services
  rules:
  - when: qs.me.ops.has_private_hospital == yes and qs.me.hospital.beds > 200
    action: refer
  - when: qs.me.ops.has_private_hospital == yes and qs.me.hospital.high_risk_services == yes
    action: refer
  - when: qs.me.ops.has_private_hospital == yes
    action: apply
  reason: Applies because you operate a private hospital. Hospitals over 200 beds, or with cardiac surgery, neurosurgery or transplant services, refer.
---

This endorsement applies where the company operates one or more facilities shown in the schedule in the category private hospital: facilities licensed as private hospitals under the health facility legislation of the relevant State or Territory, including overnight surgical, medical, rehabilitation and mental health hospitals. [[ref:me.excl.medical-practitioners]] continues to apply.

**VMO credentialing register.** The company must maintain a current credentialing register for every visiting medical officer practising at a facility, recording for each: current registration, including any conditions, undertakings or notations; evidence of current individual medical indemnity insurance complying with the Medical Indemnity (Prudential Supervision and Product Standards) Act 2003 (Cth); the scope of clinical practice approved by the company's credentialing (or medical advisory) committee; and the date of the last annual review. This is an obligation under [[ref:me.section.obligations]].

**Obstetrics.** Cover for obstetrics services is not available unless the schedule expressly shows obstetrics cover as operative for a named facility under Endorsement E01. Where it does, the following obligations apply: the facility must hold a current licence or approval as an obstetric unit; every obstetrician holding delivery privileges must hold current individual medical indemnity insurance, verified through the credentialing register; and the company must provide us at each renewal with the facility's annual obstetrics statistics, including delivery numbers, caesarean section rate, and any serious adverse neonatal or maternal outcomes reported to the relevant perinatal data collection. The carve-out for emergency treatment under [[ref:me.ext.good-samaritan]] continues to apply.

**Employed medical practitioners: cover is secondary.** Where the company employs a medical practitioner directly under a contract of employment (as distinct from a VMO or contractor arrangement), cover for the company's liability arising from that practitioner's clinical acts, errors or omissions is in excess of any medical indemnity insurance held by or in respect of that practitioner. We will not pay any part of such a claim until the limit of the practitioner's own medical indemnity policy responding to the claim is exhausted, and then only for the company's own liability. Nothing in this paragraph covers the practitioner personally, and nothing in it limits s.45 of the Insurance Contracts Act 1984 (Cth) as it applies between the company and us. [WP REVIEW: confirm this excess-of-MDO clause operates as a true excess layer for s.45 purposes.]

**NSQHS accreditation.** The company must hold and maintain accreditation under the National Safety and Quality Health Service (NSQHS) Standards for each facility required to be accredited. If accreditation for any facility is conditioned, suspended, withdrawn or lapses, the company must tell us in writing within 30 days, and we may review the terms of this endorsement prospectively for the changed risk. A change to terms operates prospectively only and does not affect cover for healthcare operations already conducted.

**Mental health inpatient units.** Where the company operates a licensed mental health inpatient unit, cover under [[ref:me.cover.healthcare-operations]] and [[ref:me.cover.vicarious-liability]] extends to the company's civil liability arising from the detention, restraint, seclusion or involuntary treatment of a patient under the mental health legislation of the relevant State or Territory, including the Mental Health Act 2007 (NSW), the Mental Health and Wellbeing Act 2022 (Vic) and the Mental Health Act 2016 (Qld), provided the company complied with that legislation and its instruments. Compliance is an obligation under [[ref:me.section.obligations]]. Nothing in this paragraph covers liability arising from an act intended to cause harm, and [[ref:me.excl.molestation]] and [[ref:me.excl.fines-and-penalties]] continue to apply.

**Intensive and critical care.** Healthcare services include intensive care, high dependency and other critical care services provided within a facility's standard operations as described in the schedule. The company's liability arising from critical care staffing, equipment, escalation and transfer systems is covered as administrative and system error under [[ref:me.cover.healthcare-operations]].

Schedule variables: facilities in this category; licensed beds.

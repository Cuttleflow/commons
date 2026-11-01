---
id: me.end.e16
type: endorsement
heading: E16 Aged Care and Residential Care
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.me.ops.has_aged_care
  - qs.me.aged.acqsc_sanction
  - qs.me.aged.memory_care_beds
  - qs.me.aged.sirs_priority1_12m
  rules:
  - when: qs.me.ops.has_aged_care == yes and qs.me.aged.acqsc_sanction == yes
    action: refer
  - when: qs.me.ops.has_aged_care == yes and qs.me.aged.memory_care_beds > 50
    action: refer
  - when: qs.me.ops.has_aged_care == yes and qs.me.aged.sirs_priority1_12m > 3
    action: refer
  - when: qs.me.ops.has_aged_care == yes
    action: apply
  reason: Applies because you operate aged care or community care services. A current sanction, more than 50 memory care beds or more than 3 Priority 1 incidents in 12 months refers.
---

This endorsement applies where the company operates one or more facilities shown in the schedule in the category aged care or community health facility, including residential aged care facilities, memory care and dementia-specific units, respite facilities, and community and home care aged services. [[ref:me.excl.medical-practitioners]] continues to apply.

**Aged Care Act 2024.** This endorsement is drafted against the Aged Care Act 2024 (Cth), which commenced on 1 November 2025 and replaced the Aged Care Act 1997 (Cth). Conduct occurring before 1 November 2025 is assessed against the corresponding provisions of the Aged Care Act 1997 (Cth) then in force.

**SIRS procedures and notification.**

- (a) The company must maintain documented procedures complying with the Serious Incident Response Scheme (SIRS) under the Aged Care Act, including procedures for notifying the Aged Care Quality and Safety Commission (ACQSC) of a reportable incident within the Priority 1 and Priority 2 timeframes that apply from time to time.
- (b) Where the company makes a SIRS notification to the ACQSC and the incident notified has given rise to, or may give rise to, a claim, the company must notify us in writing of that incident within 14 days of the SIRS notification. A notification under this paragraph is treated as notification of a circumstance under [[ref:me.cover.notification-of-circumstances]].
- (c) A failure by the company to meet the ACQSC notification timelines that results in regulatory sanction does not of itself avoid cover; we may reduce our liability by the amount that fairly represents the prejudice we suffer.

Each of these is an obligation under [[ref:me.section.obligations]] and operates on the s.54 prejudice basis. [WP REVIEW: version 1.0.0 made the 14-day notification a condition precedent; this version makes it an obligation subject to s.54, which s.54 would in any case impose on a post-contract omission.] Nothing in this policy prevents, penalises or discourages the making of a SIRS report, and making one is never treated by us as an admission of liability.

**Worker screening.** Every worker of the company (employee or contractor) who has face-to-face contact with aged care residents must hold a current NDIS Worker Screening Clearance, an equivalent State or Territory clearance where applicable, or otherwise satisfy the aged care worker screening requirements under the Aged Care Act from time to time. The company must keep records of clearances and produce them on request. This is an obligation under [[ref:me.section.obligations]].

**Restrictive practices.** Cover under [[ref:me.cover.healthcare-operations]] and [[ref:me.cover.vicarious-liability]] extends to the company's civil liability arising from the use of a restrictive practice on a resident where, at the time of use: the practice had been approved under the company's documented behaviour support framework, including a behaviour support plan for the resident where required; the consent requirements under the Aged Care Act and the guardianship, medical treatment decision or equivalent legislation of the relevant State or Territory had been met; and the practice was not prohibited under the Aged Care Act or its regulations or rules. Any claim arising from a restrictive practice that was unapproved, non-compliant or prohibited is excluded. [[ref:me.excl.molestation]] continues to apply.

**Communicable disease outbreaks.** Cover under [[ref:me.cover.healthcare-operations]] extends to the company's civil liability arising from the transmission of COVID-19 or another communicable disease within a facility, provided that during the relevant outbreak period the company complied with the public health orders, directions and official guidance applicable to the facility, and maintained documented infection prevention and control procedures, including outbreak management plans, consistent with the Aged Care Act and ACQSC guidance. Where the company was in material breach of an applicable public health requirement during the period in which the transmission occurred, we may exclude the resulting claim to the extent the breach caused or contributed to the transmission.

**ACQSC inquiry costs.** The cover under [[ref:me.cover.inquiry-costs]] and [[ref:me.ext.sirs-proceedings]] applies to ACQSC-initiated investigations and SIRS-related proceedings concerning the company's aged care services, including any show-cause process, sanctions or enforceable-undertaking proceeding, compliance notice response, and any proceeding relating to a banning order against the company or a person acting for it. Fines and civil penalties are addressed only by [[ref:me.ext.statutory-liability]]; compensation orders are addressed by [[ref:me.ext.aged-care-compensation]].

**Dementia and cognitive impairment care.** Healthcare services include dementia care, memory support and the care of residents with cognitive impairment as part of the company's standard residential aged care operations, including secure memory support units, subject to the restrictive practices terms above.

Schedule variables: facilities in this category; operational beds.

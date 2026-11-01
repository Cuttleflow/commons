# Remediation, November 2026: pre-review fixes

Date: 2 November 2026

## Purpose
Every wording in the library was pre-reviewed against the Meridian wording standard. The review found 28 Critical and about 250 Major issues across 40 documents. This release fixes them, so that the Wording Partner's legal review checks the wordings rather than discovering their problems.

Every wording remains DRAFT — SUBJECT TO LEGAL REVIEW — NOT FOR USE.

## What changed

### Build tool (`tools/wordings/build.py`)
- **Heading-only references in tables.** A table cell containing a heading-only reference (`[[ref:...|heading]]`) was split at the pipe. The raw reference then printed in the published file. Affected: the Business Package, Allied Health, Medical Establishments, Technology Liability, Construction and Marine Cargo tables. Pipes inside a reference no longer split a cell.
- **Spaces inside a reference.** References may now contain spaces (`[[ref: id | heading]]`).
- **New check: unresolved brackets.** The build now stops when a clause has an unresolved `[[` or `]]`.
- **New check: duplicated article.** The build now stops when a clause writes "the [[ref:...]]". The reference supplies its own article, so the published text would read "the the".

### Library-wide positions applied in every relevant wording
- **ICA savings clause.** A single savings clause states that the Act prevails and that section 54 applies to every condition, exclusion, limit and obligation.
- **Sanctions.** A standalone sanctions condition names the Australian regimes, with the United Kingdom, United States and European Union regimes included as a deliberate scope choice. It replaces sanctions limbs that sat inside war exclusions.
- **Corporations Act sections 199A and 199B.** One statement is used across the library, tagged for the Wording Partner. It replaces earlier descriptions that differed from each other.
- **Fines and penalties.** Uninsurable fines and penalties, including work health and safety penalties, are named where a wording pays fines.
- **Other insurance.** Escape language exposed to section 45 is replaced with contribution, except for true excess cover over a specified policy.
- **Control group.** A control group definition limits company knowledge, so one employee's knowledge is not imputed to the company. Severability is applied through the knowledge and conduct tests.
- **Distribution.** A distribution posture statement says whether the wording is retail or business, and that it is not itself a PDS.
- **Cancellation.** The insured may cancel at any time for a pro-rata refund. Deductions for amounts paid or reserved are removed.
- **Change notes.** Change notes describe changes to the wording only.

### Structure
- Side A D&O now has single-source clauses (`source/sa`). Before this release it existed only as a published page.
- Endorsements that were listed but had no operative text are now shown as not yet available (PI, FS, Side A).
- The Personal Accident and Group Personal Accident non-Medicare medical expenses benefit is removed. It conflicted with the Private Health Insurance Act 2007 (Cth), and the open question is tagged for the Wording Partner.

### Defaults set for underwriter confirmation
Where a fix needed an underwriting choice, the market-standard position was set and marked "Default set for underwriter confirmation" in the wording's change note. Examples are a cap, a sub-limit, a default retroactive date, or "whichever is less".

## Versions

| Wording | From | To |
| --- | --- | --- |
| Accountants Professional Indemnity Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Allied Health Insurance | 1.3.0-DRAFT | 1.4.0-DRAFT |
| Architects and Engineers Professional Indemnity Insurance | 1.1.0-DRAFT | 1.2.0-DRAFT |
| Building Energy and Sustainability Professional Indemnity Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Building Surveyors and Certifiers Professional Indemnity Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Business Package Insurance | 2.1.0-DRAFT | 2.2.0-DRAFT |
| Commercial Motor Insurance — Individual Vehicles and Fleets | 3.0.0-DRAFT | 3.1.0-DRAFT |
| Comprehensive Crime Insurance | 2.0.0-DRAFT | 2.1.0-DRAFT |
| Construction All Risks and Liability Insurance | 2.1.0-DRAFT | 2.2.0-DRAFT |
| Corporate Travel Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Credit Intermediaries Professional Indemnity Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Cyber Insurance | 1.4.0-DRAFT | 1.5.0-DRAFT |
| Directors & Officers Liability Insurance | 1.3.0-DRAFT | 1.4.0-DRAFT |
| Education and Training Professional Indemnity Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Excess of Loss Insurance | 2.0.0-DRAFT | 2.1.0-DRAFT |
| Financial Advisers Professional Indemnity Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Financial Services Professional Indemnity Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Geoscience and Mineral Professional Indemnity Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Group Personal Accident and Sickness Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Home and Contents Insurance | 1.1.0-DRAFT | 1.2.0-DRAFT |
| Insurance Intermediaries Professional Indemnity Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Investment Managers Indemnity Insurance | 1.3.0-DRAFT | 1.4.0-DRAFT |
| Landlords Insurance | 1.1.0-DRAFT | 1.2.0-DRAFT |
| Management Liability Insurance | 1.4.0-DRAFT | 1.5.0-DRAFT |
| Marine Cargo Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Marketing, Media and Communications Professional Indemnity Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Medical Establishments Insurance | 1.1.0-DRAFT | 1.2.0-DRAFT |
| Personal Accident and Sickness Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Private Motor Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Professional Indemnity Insurance | 1.4.0-DRAFT | 1.5.0-DRAFT |
| Public and Products Liability Insurance | 2.0.0-DRAFT | 2.1.0-DRAFT |
| Real Estate and Strata Professional Indemnity Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Recruitment and Labour Hire Professional Indemnity Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Risk, Safety and Claims Consultants Professional Indemnity Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Side A Directors & Officers Liability Insurance | not previously in source (2.0.0-DRAFT page) | 2.1.0-DRAFT |
| Strata Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Technology Liability | 1.4.0-DRAFT | 1.5.0-DRAFT |
| Travel Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Veterinary Professional Indemnity Insurance | 1.0.0-DRAFT | 1.1.0-DRAFT |
| Private Motor Product Disclosure Statement template | 0.1.0-DRAFT | 0.2.0-DRAFT |

The detailed changes for each wording are in its change note, at `source/<class>/changes/<wording>-<version>.md`, and in the "Changes From" section of its Word file.

## Still open
- **[WP REVIEW] tags.** Every point that needs a legal answer carries one in the wording, including statute section numbers this release could not verify against the legislation.
- **Earlier versions.** Earlier versions of each Word file stay in `wordings/downloads/` by design, one file per version. The hub page links the current version only.

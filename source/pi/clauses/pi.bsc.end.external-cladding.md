---
id: pi.bsc.end.external-cladding
type: endorsement
heading: External Cladding Exclusion
profession: building-surveyors-certifiers
since: 1.0.0
status: draft
note: 'From the Surveyors review (October 2026). State laws permit cladding exclusions for certifiers in different terms: NSW Building and Development Certifiers Regulation 2020, Victorian Ministerial Orders
  since July 2019, and in Queensland the Building Regulation 2021 until 30 June 2027. The endorsement adopts each permitted form rather than one national text. Counsel to settle the text against each state
  instrument.'
trigger:
  questions:
  - qs.pi.activities.cladding_work
  - qs.pi.practice_states
  rules:
  - when: qs.pi.activities.cladding_work = yes
    action: apply
  restrictions:
  - when: '''NSW'' in qs.pi.practice_states'
    action: refer
    note: The exclusion must be in the form permitted by the Building and Development Certifiers Regulation 2020 (NSW). An underwriter confirms the form before binding.
  - when: '''VIC'' in qs.pi.practice_states'
    action: refer
    note: The exclusion must be in the form permitted by the current Victorian Ministerial Order. An underwriter confirms the form before binding.
  - when: '''QLD'' in qs.pi.practice_states and policy.inception_date >= 2027-07-01'
    action: refer
    note: Queensland permits a cladding exclusion for building certifiers only until 30 June 2027, except under licences exempted before then. Check the licence and the law in force.
  reason: Applies because you certify or inspect buildings with external wall cladding. The exclusion follows the form your state permits.
---

We do not cover any claim, loss or liability arising from the use, or proposed use, in a building of external wall cladding that is combustible or that does not comply with the building law that applies to the building, including any assessment, approval, certification or inspection of building work that includes that cladding.

This endorsement applies to building work in a state or territory only to the extent that, and in the terms in which, the law requiring you to hold this insurance in that state or territory permits such an exclusion. Where that law prescribes the words of a permitted exclusion, those words apply in place of the first paragraph for building work in that state or territory.

This endorsement does not apply to building work in a state or territory where that law does not permit an exclusion of this kind on the date the policy period starts.

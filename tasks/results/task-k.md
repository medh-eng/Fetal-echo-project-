# Task K — independent adversarial audit of twelve Diagnose/Decide units
Date: 22 November 2026
Auditor: ChatGPT (GPT-6), independent of the Claude drafter
Base audited: main at ead625d165f412b96bbba3605ba1f610ca27fdb2
Scope: Z2, XB4, XB2, XB1, XB8, XB3, XB5, XA6, Z3, XA2, Z1, Z5

## Method and limits
Compared the text blocks, tables, objectives, `claims` references, drills, explanations, and checklists with the actual ASE-2023-FETALECHO and AHA-2014-FETALCARDIAC ledger statements on main. Also inspected the units' `missing_claims` lists. This is a **unit-to-ledger audit**, not an additional independent re-reading of the original guideline PDFs. Task J's separate PDF cross-check is recorded in `tasks/results/task-j.csv`.

Structural checks: all 12 units' active claim citations exist, and none cites an `ai-extracted` claim. No duplicate ledger IDs in the four ledger files; all 109 unit drills have an answer entry. No fetal-sex references or patient material were found in the reviewed teaching text. No unit was clinically signed off here.

## Per-unit findings

### Z2 — Surveillance plans by lesion
- No material contradiction between the risk-group table, intervals, follow-up questions, and their cited ASE claims. The text correctly says intervals are suggestions at provider discretion (AS23-605).
- **Editorial follow-up:** the opening summary and objective use “must” broadly; retain the lesion-specific qualifiers in AS23-035/605 and avoid treating the suggested intervals as universal schedules. AS23-039 is still `ai-extracted` on the audited main; its absence is correctly disclosed.

### XB4 — Conotruncal lesions
- **Review before release:** “below 30° or above 60°” in the screening-clue block and the quoted AS23-352 comes from ASE Table 13, while the project records a differing cardiac-axis range in Table 3. The unit already discloses that disagreement; retain an explicit “Table 13” qualifier in learner-facing wording and obtain the co-editor's decision before presenting it as a single normal limit.
- The common-trunk/right-arch 22q11 statement is correctly conditioned on **both** findings (AS23-350). Do not generalise it to every right arch.
- No other material mismatch found in the twelve drills or the lesion-specific text.

### XB2 — Left-heart lesions
- No material mismatch found in the blocks, eleven drills or checklist against their current claims. The limits of prenatal coarctation diagnosis and selected late-hyperoxygenation assessment are retained.
- The `missing_claims` entry naming all Task J claims as unchecked will require a status refresh when the approved J findings enter the ledger. **Do not add AS23-412:** Task J still marks it DISTORTED.

### XB1 — Septal and atrioventricular lesions
- No material claim-support mismatch found. Inflow-angle and AV-valve-index descriptions correctly stop short of teaching the equation-dependent 2:1 threshold while the co-editor chooses how to teach it.
- After Task J integration, reclassify confirmed claim IDs AS23-250, AS23-255, AS23-257, AS23-272, AS23-276 and AS23-359 as available for a separate editorial inclusion decision; the missing list currently labels them all unreviewed.

### XB8 — Univentricular hearts
1. **Qualifer lost — XB8-Q05:** the stem refers to *left atrial isomerism and a slow ventricular rate*, but AS23-214 states a poor prognosis for the **combination of bradyarrhythmia, left atrial isomerism and discordant atrioventricular connections**. Suggested fix: add the discordant AV connection explicitly to the stem and explanation, or remove the prognostic inference. Do not teach the stronger inference from only two findings.
2. The other seven drills and segmental-checklist statements match their ledger entries. After J, AS23-217 and AS23-358 are available for consideration, but neither is yet in this unit.

### XB3 — Right-heart lesions
1. **Sharpen drill XB3-Q01:** “Which lesion should you consider?” after isolated reversed ductal flow could invite defensible alternatives, because the cue is not a unique diagnosis. Suggested fix: ask “Which *right-sided obstructive lesion is among the possibilities*?” and retain the explanation as a warning to complete the study, rather than treating this Doppler sign as diagnostic.
2. The categorical word “always” in Q07 and its related block does occur in its specific source claim AS23-429 and is limited to structural/functional pulmonary atresia **in severe tricuspid disease**. Keep this scope explicit.
3. No other clear ledger mismatch. J confirms AS23-426, -433, -361 and -362 for potential later teaching additions; update the missing list after importing J.

### XB5 — Arch and ductus
- No material ledger mismatch found in the nine drills, blocks or checklist. The vascular-ring U sign, need to exclude a double arch/aberrant subclavian, and separate sling airway risk have their stated claim support.
- The lack of a verified source for the proposed mirror-image right-arch/L-shape figure remains real: Task J explicitly withdrew the Figure 30F suggestion. Do not restore that candidate. AS23-307 is confirmed in J and can later inform a separate arch-branching addition.

### XA6 — Biometry and Z-scores
1. **Unsupported objective:** “why the equation used must be stated” is not in AS23-152–154, and the unit's own `missing_claims` says the reporting requirement lacks a claim. Replace with “explain why the choice of published Z-score equation matters,” or add a separately sourced reporting standard before teaching an obligation.
2. Optional-measurement phases, the annulus timing caveat, and the seven existing drills match their cited ASE claims. Do not add a Z-score reference equation or numerical normal values until one is selected and verified.

### Z3 — Delivery planning
1. **High-priority historical-practice limitation:** the Level P/1–5 table and related recommendations are from the **2014 AHA U.S. statement**. Although the opening calls it the 2014 scheme, the subsequent “place, timing and mode,” “recommended/not needed,” checklist, and scenario questions may be read as standing/current Indian delivery instructions. Put a prominent qualifier at point of use: historical AHA 2014 risk framework, not a current local protocol; review all timing, facility capability, referral and mode-of-delivery instructions against newer evidence and Indian services before release.
2. **Unsupported deadline — checklist title “Delivery plan before 36 weeks”:** AH14-306 supports a level-of-care plan **before delivery**, not a universal 36-week threshold. Rename to “Delivery plan before birth” unless a distinct source supplies the timing.
3. **Safety clarification:** the 2014 Class III statement that a specialist team need not be *in the delivery room* for many ductal-dependent lesions must not be read as “no neonatal resuscitation/stabilisation plan, prostaglandin access or cardiology pathway.” Level 2 explicitly requires a capable hospital and timely prostaglandin where indicated (AH14-319 and AH14-311). Clarify this adjacent to the table, block and Q07.
4. J confirms AH14-305, AH14-316, AH14-326 and the wellness-testing claims, but **AH14-314 still needs its expanded locator**. Refresh the misleading blanket `missing_claims` entry after J reconciliation. All ten currently keyed responses match their cited ledger wording, subject to the dated-source caveat.

### XA2 — Genetics and work-up
1. **Risk of false reassurance:** the table “Aneuploidy risk” contains 0% for transposition and heterotaxy (from the cited AHA 2014 table). Those are observed values in historical cited series, **not proof of zero biological risk**. Change the label or footnote to “reported series estimate (AHA 2014), not a rule-out test”; retain the clear advice to offer genetic assessment even in apparently isolated lesions (AH14-107/103).
2. The fetal/infant frequencies and 22q11 percentages are historical source estimates, not present-day counselling probabilities. Keep source, population and date next to any table/quiz and obtain an updated genetics source before release.
3. No additional unsupported claim found in the eight drills or extracardiac work-up checklist. J confirms AH14-014/114/117/330 etc., but do not assume they are included in this unit without an edit.

### Z1 — Counselling
- No material cited-claim mismatch in the six drills, blocks or checklist. The text avoids inventing gestational limits for India.
- The termination-law discussion is a **general 2014 counselling principle**, not a verified description of current Indian law. Maintain the `missing_claims` item and do not publish jurisdiction-specific legal advice until reviewed.
- J confirms several formerly omitted counselling entries, but they still require an editorial decision before insertion.

### Z5 — Fetal intervention
1. **Historical outcome framing:** 52/70 technically successful fetal aortic valvuloplasties (AH14-206) describes **one series reported in AHA 2014**. State that at the point of use and do not imply it represents current success or clinical benefit. The separate technical-versus-clinical outcome warning is appropriate.
2. The 2014 “no randomised trials” and unresolved technique/timing passages already identify their date. Newer outcome data and specialist review are required before the unit can guide candidacy or management.
3. The seven drills and current checklist statements track the cited AHA/ASE claims. After J, AH14-023, AH14-209, AH14-332 are confirmed and may be considered separately.

## Cross-cutting findings
- **Drill quality: 109 of 109 drills have correct answer index 0.** This makes repeated practice and scored testing predictable regardless of knowledge. Shuffle answer options (and the answer index) deterministically at display time, with tests that keep explanations and keys aligned; or edit a balanced set after independent review. Do not leave the existing first-option pattern in a high-stakes learner assessment.
- The twelve `missing_claims` lists accurately describe the **pre-J** situation on the audited main branch but must be reconciled with `tasks/results/task-j.csv` when J is applied. For the three locator findings (AS23-401, AS23-406, AH14-314) and the one distorted claim (AS23-412), keep the claims withheld pending repair and new check. Merely being “present” in the ledger is not approval.
- No missing active citation, no active `ai-extracted` citation and no duplicate ledger claim ID detected. These structural checks do not replace the full Python build, another independent audit of edited units, or the cardiology/genetics co-editors' sign-off.
- No misleading fetal-sex wording detected in the reviewed units. Patient images/metadata are not part of these units.

**Units with no material unit-to-ledger discrepancy in the current teaching text:** Z2, XB4 (with pre-existing Table 3/13 discrepancy reserved for co-editor), XB2, XB1, XB5, Z1. All still require the cross-cutting drill and J missing-list housekeeping.

## Required integration handoff
1. Apply safe wording fixes to XB8-Q05, XA6 objective, Z3 checklist and the date/context caveats in Z3/XA2/Z5; sharpen XB3-Q01. Preserve all existing `signed_by` and `verified_by` values.
2. Update `missing_claims` from the 53 confirmed Task J claims. Do **not** silently elevate the four unresolved ones.
3. Rebuild with `python tools/build.py`, independently validate the changed drill keys, then set `audited_by` for each reconciled unit. These 12 units remain unsigned until clinical review.
4. Record clinician/co-editor decisions for the equation/axis discrepancy, genetics, contemporary delivery plans, and fetal intervention outcomes.

**Status:** Independent Task K audit completed; lesson corrections and clinical sign-off are separate work. No clinical sign-off performed.

## Implementation follow-up — 23 November 2026

The twelve listed unit sources were updated on the integration branch in response to the findings above. Changes include the XB8-Q05 full three-part condition, XB3-Q01 cue limitation, XA6 reporting-objective correction, historical 2014 framing and risk-table cautions in Z3/XA2/Z1/Z5, Z3's removal of the unsupported 36-week checklist deadline, and reconciliation of `missing_claims` for the 53 confirmed Task J claims. The four unresolved claims remain out of teaching.

**Correction to the cross-cutting quiz observation:** all 109 YAML drills have `answer: 0`, but the course app's `tools/templates/app.html` and the generated stand-alone study page's `tools/build.py` both already shuffle each option *together with its correctness flag* at display time. The learner-facing option order is therefore randomised, and no mass key-reordering was warranted. The new `tools/check_round5.py` checks that the labelled shuffling logic and drill keys remain intact. If drills are exported to another unshuffled platform, their ordering must be independently randomised there.

**Build:** The `.github/workflows/validate-evidence.yml` GitHub workflow runs `python tools/build.py --check`, the full `python tools/build.py`, and regression checks. It also regenerates tracked `dist/` material only on the PR's integration branch after successful tests. This is technical validation, not evidence/clinical sign-off. The 23 November build initially passed on the current changes.

**Review boundary:** Although Task K was audited independently of Claude's 21 November draft, some remedial text above was written by ChatGPT, the auditor. `audited_by` remains null in all twelve units until a **different** independent auditor reviews those edits against the source ledgers and, as appropriate, original PDFs. All `signed_by` fields remain null; clinician/co-editor verification is still required before clinical release.

The three Task J locator fixes and the AS23-412 wording repair are recorded in `tasks/handoff/task-j-final-recheck.md` for independent PDF re-check, and all four retain `ai-extracted` status.

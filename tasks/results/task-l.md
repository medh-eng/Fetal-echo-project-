# Task L — independent audit of four new Diagnose units

**Date:** 23 November 2026  
**Auditor:** ChatGPT (GPT-6), independent of the Claude drafter  
**Base examined:** `claude/apply-j-k` at `0da10619bd435bff9cad741d1ceba6e32889ec9e` (open PR #10)  
**Units:** XC7, XC5, XC8, XB9  
**Sources compared:** `content/ledger/AHA-2014-FETALCARDIAC.yaml` and `content/ledger/ASE-2023-FETALECHO.yaml`; `prompts/04-audit.md`.

## Scope and limitations

Reviewed every section block, table row, objective, quiz stem, four response options, explanation and checklist item against the **specific cited ledger statements**. All citations used in these four drafts exist and have `ai-cross-checked` status on the examined branch. No clinical statement with an entirely absent ledger basis was found, but some qualifiers and source attributions need correction. This is **not** a fresh PDF-to-claim review: the guidelines' original PDF pages were not re-checked in this task. The cited 2014 U.S. statement is historical, not necessarily current Indian guidance. The drafts remain `audited_by: null` and `signed_by: null` until the fixes are applied and independently re-reviewed.

## XC7 — Maternal disease, drugs and exposures

1. **High — table inherits incomplete claim references.** The ten-row referral table is inside the `Not indicated (Class III)` block, whose only reference is `[AH14-005]`. Seven table rows instead depend on **AH14-001, AH14-003 and AH14-004** (Class I, IIa and IIb). The source claims do support those rows, but the table's displayed provenance does not. **Fix:** cite `[AH14-001, AH14-003, AH14-004, AH14-005]` on the table-bearing block, or move the table into a dedicated block with all four references; audit the regenerated chapter/study page for reference marks. This is the only clear missing *local* citation among the four units.

2. **High — unsafe ambiguous interaction of diabetes referral classes.** `XC7-Q02` and the row "Gestational diabetes with HbA1c below 6%" imply a Class III answer without giving diagnosis timing. But `AH14-001` separately says diabetes diagnosed **in the first trimester** is Class I. A learner can reasonably ask whether a case of gestational diabetes diagnosed early fits both. **Fix:** explicitly distinguish pregestational/first-trimester diagnosis from the population contemplated by `AH14-005`; clarify that the bare HbA1c value alone does not override a separate Class I indication. Obtain the cardiology co-editor's resolution of the overlap and adjust Q02 or withhold it until unambiguous.

3. **High — "vitamin K agonists" is an internally disputed source term.** `AH14-005` itself warns that recommendation 5 literally prints "vitamin K agonists" while its Table 2 reportedly concerns **antagonists**. The unit's phrase "as printed" flags transcription but nevertheless places the item in a "not indicated" referral list, where it could be mistaken for reliable medical advice about drug exposure. **Fix:** exclude this entry from the learner-facing recommendation list pending the co-editor's source-table check; place a source-discrepancy note in `missing_claims` or an editor-only annotation. Do **not** silently substitute a drug category, and do not advise medication changes. Independently verify the original page/table and look for newer guidance before release.

4. **Medium — missing level of evidence and date at table point of use.** The Class assignments themselves match the cited ledger: `AH14-001` **I**, `AH14-003` **IIa**, `AH14-004` **IIb**, `AH14-005` **III**. The unit doesn't contradict any of those classes, but it omits their varying **levels of evidence** (A/B/C) and leaves the table caption as generic "Exposure / Referral". **Fix:** make the caption "AHA 2014 U.S. referral categories (historical)" and offer LOE per row, backed only by the cited claims. Do not represent these categories as 2026 Indian rules. The planned comparison with AIUM 2020 is not ready because the AIUM claims are still `ai-extracted`.

5. **Drills/checklist:** Q01 (pregestational diabetes), Q03 (SSA/SSB without previous affected child), Q04 (NSAIDs by trimester), Q05 (paroxetine distinction), and Q06 (seroconversion-only infection) each have one ledger-supported correct option. Q02 needs the timing qualification above. The four checklist items follow the recommendation claims without recommending drug cessation; retain that boundary.

6. **Missing claims:** The four current `missing_claims` items are substantively honest, including lack of drug dose guidance, current Indian advice, unverified AIUM 2020 differences, and other referral categories. Add the disputed vitamin-K wording and the AH14-001/AH14-005 diabetes-category overlap as explicit editor decisions.

## XC5 — The heart in twins / twin-twin transfusion

1. **High — historical mortality/prevalence stated as timeless estimates.** The opening block and Q01 explanation state **10%–20%** of monochorionic twins and **90%–100%** untreated mortality, supported by `AH14-215`, but the learner-facing text does not identify the **AHA 2014** source date at the point of use. Such estimates depend strongly on the historical population and management setting and must not be presented as present-day counselling probabilities. **Fix:** prepend "AHA 2014 reported..." to that block and, where retained in quizzes, explain "historical estimate; not current prognosis after access to fetal therapy." Require an updated source and specialist review before release.

2. **Medium — post-laser recommendation needs visible 2014 scope.** `AH14-220` supports considering fetal echocardiography **24–48 hours after laser treatment in surviving twins**. The section and checklist preserve "consider" and the timing, and Q05 names AHA 2014, but the stand-alone block/checklist could appear to mandate an unchanging 2026 protocol. **Fix:** attach "as suggested in AHA 2014; confirm against the current fetal therapy protocol" to the block and checklist. Do not change "should be considered" to "must".

3. **Correctly retained qualifiers:** `AH14-216` supports recipient cardiac findings and potential persistence of RV outflow issues; `AH14-217` supports Quintero's lack of cardiac components and the proposed cardiac scores; `AH14-219` says predictive value is **controversial**, and the unit keeps that uncertainty. The first echocardiogram `AH14-218` is appropriately described as part of initial assessment. No additional claim mismatch in the five drills or checklist beyond the date-at-use qualification.

4. **Missing claims:** Correctly names absent staging details, contemporary treatment/referral, donor findings, and newer guidance. No treatment instruction or numerical treatment threshold was invented.

## XC8 — Extracardiac anomalies

1. **Medium — distinguish upper-end historical estimates from an expected rate.** `AH14-114` records **up to 20% in infants** and fetal reports reaching **as high as 50%–70%**. The block and XC8-Q02 mostly preserve "as high as"/"up to", but the overall objective "state how often" and the quiz may still teach those upper-end observations as a typical frequency. **Fix:** label both as *figures from series summarised in AHA 2014*, and specify that 50%–70% is an upper-end observation, not a universal fetal CHD rate. Confirm against updated, population-specific estimates before patient counselling.

2. **Medium — checklist changes a comparative statement into an absolute one.** `AH14-115` states that d-transposition and pulmonary atresia with intact septum are **more often isolated** relative to VSD/tricuspid atresia. The checklist asks if a lesion "is it usually isolated?", which may imply no extracardiac risk rather than the documented comparison. **Fix:** rewrite to "which lesions are more often associated vs more often reported isolated?" and remind learners that `AH14-116` still calls for detailed fetal anatomy survey **for every fetus** with CHD. In XC8-Q03's explanation, similarly add that "more often isolated" never excludes associated abnormalities.

3. **Other blocks, drills and checklist:** `AH14-115` matches the lesion contrasts. `AH14-116` matches the expert detailed survey for every fetus with CHD and the possibility of repeating assessment later. The five drills each have one defensible ledger-supported answer. Avoid drawing the false inference that an initially normal anatomy survey forever excludes abnormalities.

4. **Missing claims:** The gaps on organ-specific associations, extra work-up/prognosis and newer evidence are honestly noted.

## XB9 — Cardiac tumours, dysfunction and failure

1. **Medium-high — 2014 genetic association lacks context.** The block and XB9-Q03 repeat **over 60%** tuberous-sclerosis association for tumours found in mid/late gestation, supported by `AH14-111`. The source itself notes 2014 evidence. As written, the explanation risks implying a universal up-to-date probability across all fetal tumour types. **Fix:** explicitly label "reported in the AHA 2014 statement" wherever the percentage is shown, including the block, drill explanation and checklist; obtain a more recent genetics source for counselling and retain genetic testing recommendation subject to specialist review.

2. **Medium — regression language could imply certainty for an individual fetus.** The block, XB9-Q02 and checklist say rhabdomyomas "regress after 32 weeks" following the source phrasing in `AS23-522`. That matches the ledger literally but risks being read as a guarantee for **every** tumour. **Fix:** contextualise it as the pattern described by ASE 2023; avoid promising regression for a specific fetus without supporting evidence and the clinician's decision. Do not invent new proportions.

3. **Other claim checks:** `AS23-521` supports tumour type and effects on filling/function/rhythm; `AS23-523` supports myocardial disease, volume-loaded CHD, obstruction on both sides and arrhythmias as dysfunction causes; `AS23-524` supports overload, arrhythmia and compression as heart-failure mechanisms. All five quizzes have one ledger-supported best option. The final checklist gathers the same supported observations.

4. **Missing claims:** Imaging differentiation by tumour type, cardiomyopathy/effusion, heart-failure scoring/treatment and updated practice are correctly withheld.

## Cross-cutting and release gates

- **Claim integrity:** every cited claim in these four units is known and `ai-cross-checked`; none cites the separate `AI20-*` ledger, whose entries remain `ai-extracted` on PR #10. The 2014 U.S. statement is a historic source throughout; any Indian referral, genetic or TTTS clinical pathway needs a current source and named specialist review.
- **Quiz integrity:** **21 of 21** source YAML drills store `answer: 0`; however the course-app and standalone-study code already shuffles choices together with their correct-answer flags (verified in Task K), so this is *not* an exposed first-answer pattern in the current interface. Do not bulk-edit source answer indices without synchronising options and testing. Any new quiz/export platform needs its own shuffling check.
- **No fetal-sex wording** or patient-identifying data in the four inspected unit YAML files. No medication doses or medication-change instructions.
- **No video outlines** in these four new units; this is a production gap, not a claim contradiction.
- **Units with no material sentence-to-ledger contradiction:** XC5, XB9. XC8's main prose and drills also track its ledger. **XC7 has a definite table-attribution problem and a defensibly ambiguous diabetes question; those are priority fixes.** Every unit still needs a 2014-at-point-of-use safety pass.
- **Governance:** This audit does not change any lesson's `audited_by`, `signed_by`, or claim `verified_by`. Claude may apply the proposed fixes but cannot independently audit its own revised drafts; a different independent reviewer should confirm the final wording, and the editor-in-chief and relevant co-editors must approve the specialist content.

## Priority for implementation

1. XC7: repair table provenance, resolve conflicting diabetes-class conditions and withhold the vitamin-K wording pending verification.
2. XC5 and XB9: add prominent historical date/population qualifiers to mortality, tumour-genetics percentages and the post-laser timing recommendation.
3. XC8: preserve "reported upper end", not a normal expectation; change "usually isolated" to the supported comparison.
4. Regenerate the `dist/` study pages, drills, book, editor pack and app; run `python tools/build.py --check` and full `python tools/build.py` with no errors.
5. Independent re-audit of changed material and specialist sign-off; keep all four units unsigned until then.

**Status: Task L independent unit-to-ledger audit completed.** Recommendations are an editorial handoff, not a clinical release authorisation.

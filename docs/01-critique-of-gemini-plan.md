# Critique of the Gemini blueprint

Reviewed: "Comprehensive Blueprint for an Integrated Next-Generation Fetal Echocardiography Ecosystem" (25 pages, 62 citations).
Date of review: 12 Nov 2026.

## Verdict

The blueprint is a strong **wish list** and a weak **plan**. Its syllabus is broad and mostly sensible, and several of its teaching ideas are worth keeping. But it describes a product for a funded 20-person team in a US academic centre, schedules the hardest dependency first, leans on single-centre numbers as if they were rules, and says nothing about India. Followed as written, the project would stall in month 2 on the case library.

## What to keep

| Idea | Why it is right |
|---|---|
| One canonical knowledge source feeding book, app, video and study items | Prevents the four products drifting apart; this is the core of the new plan too |
| Teach the **sweep**, not isolated views | Matches how the examination is actually done |
| Perceptual drills on moving clips rather than text flashcards | The real skill is recognising "not normal" in a few beats |
| Video that shows the hand and the screen together | Learners fail on probe handling, which screen-only video hides |
| Burned-in patient text is the main de-identification risk in ultrasound | Correct and commonly missed |
| Calculators must show the equation, the source and the cohort | Correct, and it applies to every number in the book too |
| Never let a model recall regression constants from memory | Correct |

## Spot-checks of specific claims

I checked a sample of the blueprint's hard numbers against the literature. Result: some are accurate, some are stretched, one is a category error.

| Blueprint claim | Finding | Status |
|---|---|---|
| Boston CART: LV pressure > 47 mmHg and ascending aorta Z ≥ 0.57 gives 92% biventricular outcome; 9% in the unfavourable group | Matches Friedman et al., *Ultrasound Obstet Gynecol* 2018;52:212–220 (n = 24 and n = 34 in those two groups) | Accurate, but small groups |
| "Multi-Nomogram Z-Score Comparator" plotting Pettersen, Schneider, Boston, Kampmann, Olivieri for one fetal measurement | Pettersen 2008 is a **paediatric** dataset: 782 patients aged 1 day to 18 years, regressed on body surface area. Kampmann, Zilberman and Olivieri are also postnatal. A fetus has no BSA; fetal Z-scores are indexed to gestational age, femur length or BPD | **Category error.** Fetal and paediatric references are mixed |
| Pulmonary vein forward/reverse VTI ratio < 3 has "80% sensitivity and 100% specificity"; < 7 during hyperoxygenation "confirms severe restriction" | Published thresholds are < 5 (2005 series, PMID 16260632), ≤ 3 to optimise specificity (2011 series, PMID 21130471), and < 6.5 with hyperoxygenation in a single-centre study of 27 fetuses, where baseline < 3 had 60% sensitivity. A later series of 133 fetuses found most with ratio < 5 still had an adequate shunt | Stretched. Small single-centre numbers written as rules |
| "Mlodawski et al., 2026" mechanical PR regression equations to embed in the app | The cited link is a *J Clin Med* volume 14 paper (2025). Coefficients not independently verified. One cohort | Unverified; not ready to ship in a calculator |
| ISUOG 2023 and ASE 2023 as anchor guidelines | Both exist: Carvalho et al., UOG 2023;61:788–803; Moon-Grady et al., JASE 2023 | Accurate |
| Automated strain with a "logarithm-scaled kernel" and "ProID" segmentation as core curriculum | Comes from one research paper (citation 26). Not a standard clinical method | Over-weighted |
| Delivery-room figures for d-TGA ("40% sensitivity, 0% specificity") and HLHS ("80% vs 0% survival") | Source is a conference slide deck (citation 6), not a paper | Not citable as written |

Lesson: the blueprint's own "zero-hallucination loop" did not protect it. Models checking models is not verification. Every number needs a source locator and a human signature.

## Source quality

Of 62 citations:

- Two point to unlicensed copies of commercial textbooks (dokumen.pub, dl.icdst.org). These cannot be used or cited.
- Several are SEO listicles and vendor blogs (Slashdot, SourceForge "best DICOM viewers", Taskmonk, Tactionsoft).
- Many are ResearchGate mirrors instead of the journal of record.
- The text still contains raw artefacts (`[span_194](start_span)`, unrendered LaTeX), so nobody proofread it.

## Strategic problems

1. **No defined learner.** It promises to serve a trainee sonographer and a fetal interventionist with one product. Those are different products. Without a first audience there is no first release.

2. **The critical path starts with the hardest thing.** Phase 1 asks for 500+ de-identified DICOM studies covering 34+ lesion types in three months. Rare lesions take a single centre years to collect. Everything else waits on this.

3. **The 3D heart has no data source.** The virtual probe needs a beating, segmented 4D fetal heart. The blueprint says "derived from fetal CMR, CT and STIC datasets" but public fetal cardiac datasets are scarce and are mostly 2D images, not 4D volumes. This needs its own strategy.

4. **Over-engineered viewer.** OHIF, Cornerstone3D and a DICOMweb archive are tools for clinical reading rooms. A learner needs a sharp looping clip with a scale. Running a DICOM archive adds cost, hosting and privacy risk for little teaching gain.

5. **India is missing.** The compliance section covers HIPAA, GDPR, NIS2 and the FDA. A resource built in Nagpur on Indian patients is governed first by the PC-PNDT Act, the DPDP Act 2023 and Rules 2025, ICMR ethics guidance, and CDSCO for any software that gives patient-specific output.

6. **Calculators create liability.** A "biventricular probability calculator" and a "level-of-care triage engine" give patient-specific outputs from small cohorts. A disclaimer does not make that education. These belong late, behind expert review, or not at all.

7. **Quantity targets instead of quality targets.** "5,000+ flashcards" generated by a model is a cost, not an asset. Perceptual learning needs many *different* clips of the same finding; spacing the same clip trains memory of the clip.

8. **No authority plan.** A reference text is trusted because of who signs it. The blueprint has one line about "sign-off by a board-certified fetal cardiologist" and no editorial board, peer review or named authors.

9. **No proof it works.** There is no pilot, no pre/post test, no outcome measure. "Most advanced" has to be demonstrated.

10. **Missing content.** Parent counselling and ethics, structured reporting, pitfalls and artefacts, twins, growth restriction, maternal disease and drugs, hydrops and heart-failure scoring, genetics work-up after diagnosis, postnatal outcomes, audit and quality assurance, low-resource practice, regional languages.

11. **No money, team or distribution.** No budget lines, roles, pricing, licensing or route to learners.

12. **AI roles assigned by brand reputation.** "Gemini reads, ChatGPT calculates, Claude writes" is folklore. What matters is that the model that drafts is not the model that audits, and that both work from the source document.

## What changes in the new plan

| Gemini | New plan |
|---|---|
| Four pillars built in sequence over 12 months | One topic built end-to-end in all four formats in 8 weeks, then repeat |
| 500 DICOM studies first | Start with normal anatomy (available every day), synthetic models and prospective consented capture |
| OHIF + DICOMweb | Looping video + calibration sidecar; originals kept offline |
| 8 domains for everyone | 3 tiers: Detect, Diagnose, Decide. Detect ships first |
| Models audit models | Evidence ledger with source locator + named human sign-off; build fails without it |
| HIPAA / FDA | PC-PNDT, DPDP, ICMR, CDSCO first; US/EU later if sold there |
| Calculators early | Reference tables with visible formulae first; patient-specific tools only after expert review |
| No validation | Pilot study with pre/post testing built into Phase 1 |

See `02-master-plan.md`.

## Sources for the spot-checks

- Friedman KG et al. Improved technical success, postnatal outcome and refined predictors of outcome for fetal aortic valvuloplasty. UOG 2018;52:212–220. https://doi.org/10.1002/uog.17530
- Pettersen MD et al. Regression equations for calculation of z scores of cardiac structures… JASE 2008;21:922–934. https://pubmed.ncbi.nlm.nih.gov/18406572/
- Fetal pulmonary venous Doppler and need for emergent atrial septoplasty in HLHS (ratio < 5), 2005. PMID 16260632. https://pubmed.ncbi.nlm.nih.gov/16260632/ (author names to be confirmed in the ledger)
- Follow-up series proposing ratio ≤ 3 to optimise specificity, 2011. PMID 21130471. https://pubmed.ncbi.nlm.nih.gov/21130471/
- Maternal hyperoxygenation and pulmonary vein VTI ratio in 27 HLHS fetuses, 2021. PMID 34673647. https://pubmed.ncbi.nlm.nih.gov/34673647/
- Trends in pulmonary venous Doppler in fetal HLHS (133 fetuses). https://pmc.ncbi.nlm.nih.gov/articles/PMC9978270
- Carvalho JS et al. ISUOG Practice Guidelines (updated): fetal cardiac screening. UOG 2023;61:788–803. https://doi.org/10.1002/uog.26224

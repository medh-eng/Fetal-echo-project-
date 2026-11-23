# Task J final four-claim independent re-check handoff

Prepared 23 November 2026 from Task J (`tasks/results/task-j.csv`). These four claims remained `ai-extracted` after the first cross-check. The three source locators and one statement have now been corrected **without promoting their status**.

## Who should review?
Use Gemini or another independent model supplied with **both original society PDFs**, not Claude (the original extractor) or ChatGPT (which proposed these final amendments). Read the printed pages and tables. These are draft medical education statements, not approved clinical guidance.

| Claim | Current text / concern | Printed source to inspect | Action |
|---|---|---|---|
| AS23-401 | Serial assessment of progressive semilunar valve obstruction and significant regurgitation | ASE 2023 p. 715, Section IV.C.iv, introductory paragraph above semilunar-obstruction subsection | Verify the new locator and the breadth of both lesion groups |
| AS23-406 | The listed systemic venous, ductus venosus, umbilical arterial, umbilical venous and middle cerebral arterial Dopplers in progressive lesions | ASE 2023 p. 715, same introductory paragraph | Verify all five Doppler sites and scope |
| AS23-412 | Four-chamber aortic-stenosis observations now list LV hypertrophy, dilatation **or** dysfunction, instead of requiring dilatation and dysfunction together | ASE 2023 Table 13 p. 708, aortic stenosis row | Confirm punctuation, optional ascending-aortic dilatation and that the slash does not require a conjunction |
| AH14-314 | A later study of tethered/bowing septum primum found limited sensitivity/specificity for predicting compromise requiring emergent intervention | AHA 2014 pp. 2224–2225, Foramen Ovale-Dependent Lesions, including the text below Table 20 | Verify the new two-page locator and the specifically limited inference |

### Output and boundaries
Produce `tasks/results/task-j-final-recheck.csv` with header `claim_id,verdict,detail` and **exactly four rows**. Use `CONFIRMED`, `CORRECT LOCATOR`, `DISTORTED` or `NOT FOUND`; explain all exceptions precisely. Only then may the integration reviewer apply confirmed statuses using the repository's cross-check rules, followed by `python tools/build.py`.

Do not set `expert-verified`, alter any existing `verified_by` or `signed_by`, teach any disputed threshold, or imply that the 2014 AHA statement reflects today's protocols. The twelve Task K units deliberately do not cite these four claims.

# Work log

| Date | Who | Step | Unit | What changed |
|---|---|---|---|---|
| 2026-11-12 | Claude | Review | - | Critiqued the Gemini blueprint; wrote master plan, syllabus, AI workflow, governance |
| 2026-11-12 | Claude | Build | - | Evidence ledger format, validator and build script |
| 2026-11-12 | Claude | Harvest + draft | D1 | 12 seed claims (from search excerpts, unverified), draft unit, 8 drills, video outline |
| 2026-11-13 | Claude | Harvest | all Detect | 96 claims from the full ISUOG 2023 PDF with page locators; replaced the 12 seed claims and dropped the 2013 and handbook sources |
| 2026-11-13 | Claude | Draft | D1 | v0.2: 10 sections, 22 drills, video outline; review sheet added to the build |
| 2026-11-13 | Claude | Plan | - | Decisions recorded (Detect first, subscription, English, editor-in-chief, archive, Voluson); build plan written |
| 2026-11-13 | Claude | Sign-off | D1 | Dr Kunda approved the D1 review sheet (relayed by the project owner, not entered by her). 62 claims set to expert-verified and D1 signed with `tools/signoff.py`. Undo by restoring the ledger from the previous commit if she asks for changes |
| 2026-11-13 | Claude | Harvest + draft | F1 | New unit F1, ultrasound modes in fetal echocardiography (editor's request). 22 claims from the ASE 2023 fetal echo guideline, read through a web reader (first part only, about p. 705), plus claims reused from ISUOG 2023. All ai-extracted. Needs cross-check against the PDF by a different model, then sign-off |
| 2026-11-13 | Claude | Build | all | Build now also produces the course app (dist/app, installable, offline, saved progress, drill scheduling), a combined book (dist/book) and website pages (dist/web) |
| 2026-11-15 | Claude | Draft | D0, D7, D8, D9, D11, D13 | Six Detect units drafted from existing ledger claims only (no new claims). 65 new drills. All draft: need audit by a different model and editor sign-off |
| 2026-11-15 | Claude | Build | all | Editor's review pack (dist/editor): every unverified claim used by unsigned units, once each, plus open decisions from content/editor/questions.yaml. Units now ordered by number. `tools/apply_crosscheck.py` applies a cross-check CSV to the ledger |
| 2026-11-15 | Claude | Tools | - | Clinic tools: offline case catalogue and clip anonymiser (tested on a synthetic clip with a dummy name; not yet on a real export). Clinic checks form and pilot protocol written. Three tasks written for ChatGPT (cross-check all 118 claims, audit seven units, harvest rest of ASE) |
| 2026-11-16 | ChatGPT | Independent review handoff | A, B, C | Reviewed 118 ledger claims against the original society PDFs, audited the seven unsigned units against their cited ledgers, and prepared additional ASE claims for independent cross-check. Results are in `tasks/results/`. Clinical sign-off and application of changes remain with the project team. |

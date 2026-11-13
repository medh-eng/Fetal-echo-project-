# What will be built, and in what order

Version 0.1, 13 Nov 2026. Follows the decisions in `02-master-plan.md` section 13.

## The product: Detect tier

A subscription course for radiologists, gynaecologists and fellowship students who scan pregnancies. Goal: after it, they reliably recognise a heart that is not normal on a routine scan and know what to do next.

| Part | What the subscriber gets | Built from |
|---|---|---|
| **Course app** | 14 units. Each has four tabs: Read, Watch, Drill, Checklist. Runs in a browser, installs on a phone, works offline | Units in this repo |
| **Clip drills** | A clip plays for a few beats. Normal or not? Which view? Where is the problem? Hundreds of different clips, scheduled so weak areas return more often | The Mayflower archive |
| **Case atlas** | Searchable library of anonymised cases: by view, by finding, by gestation. Each with the editor's teaching note | The Mayflower archive |
| **Sweep trainer** | A 3D chest with a movable probe. Slide from abdomen to upper chest and see each plane form | 3D model; later, stored volumes |
| **Videos** | Short films: set-up, the sweep with hand and screen together, each view, pitfalls | Scripts generated from units |
| **Book** | The same content as a web book and PDF | Generated |
| **Assessment** | Entry test, unit tests, final test on unseen clips, certificate | Drill bank |
| **Supervisor view** | For fellowship directors: each fellow's progress and weak areas | App data |

Diagnose and Decide tiers follow on the same engine.

## Why this is better than the Gemini blueprint

| | Gemini blueprint | This plan |
|---|---|---|
| First release | Everything, in 12 months | Detect tier, one unit at a time |
| Cases | Collect 500 new studies first | Use the 14-year archive already held |
| Accuracy | Models check each other | Every statement tied to a page of a source and signed by the editor |
| Viewer | Hospital-grade DICOM system | Sharp looping clips that play on a phone |
| Law | US and EU | India first |
| Proof | None | Before-and-after test on fellows |
| Status | A document | Running: 96 sourced claims, one unit, a working study page |

## How it helps

**The editor-in-chief**

- Fourteen years of cases become an organised, searchable teaching library instead of files on a machine.
- Her time goes only where a clinician is needed: checking claims, choosing cases, recording teaching notes and videos. Drafting, formatting, building and scheduling are done by the tools.
- Every statement in her book can be traced to its source, which protects her name.
- Fellows arrive at the scan room already drilled on normal anatomy, so teaching time goes to the hard cases.
- The supervisor view shows which fellow is weak on which view.
- The same archive and engine produce the later tiers, lectures and papers.

**Subscribing doctors**

- They train the skill that matters: spotting "not normal" in a moving image, quickly.
- A fixed routine and checklist they can use on the next patient.
- Clear rules on when to refer, taken from the guideline.
- Short sessions on a phone between patients; drills return to what they got wrong.
- Real cases from Indian practice.

## Steps

Owner: **K** = Dr Kunda, **Y** = you, **C** = Claude, **X** = ChatGPT or Gemini.

### Done

1. Critique, master plan, syllabus, rules, repository. (C)
2. ISUOG 2023 guideline harvested from the full PDF: 96 claims with page references. (C)
3. Unit D1 rewritten on those claims: 10 sections, 22 drills, video outline, editor's review sheet. (C)

### Next two weeks

4. **Cross-check.** Give the guideline PDF, `content/ledger/ISUOG-2023-SCREEN.yaml` and `prompts/02-crosscheck.md` to ChatGPT or Gemini. Bring back its table. (Y, X) About 30 minutes.
5. **Sign-off of D1.** Dr Kunda goes through `dist/D1/review.md` (62 claims) and marks each OK / change / remove. (K) About 1 hour.
6. **Archive survey.** Tell me roughly what exists: how many cases, stills or clips or 4D volumes, how they are stored (machine hard disk, DVDs, PACS, external drives), and file types. (Y, K)
7. **Machine check.** On the Voluson, find out which export formats are available (video file, DICOM, 4D volume) and whether patient details can be hidden at export. Export one normal case all three ways. (Y)
8. **Consent check.** Confirm the consent wording covers teaching use in a paid product. (K, with the legal advisor)

### Weeks 3-6

9. **Case catalogue tool.** A simple offline app for the clinic computer: one row per case with code, gestation, view, mode, finding, quality, consent status, teaching note. No patient names. (C builds; K and Y fill)
10. **Anonymiser.** A program that runs on the clinic computer only: crops the patient banner, removes hidden data, converts to a web clip, writes the label file, and shows each result for a human check. Tested first on a clip with a dummy name. (C builds; Y runs)
11. **First 40 cases** through catalogue and anonymiser: 30 normal, 10 abnormal. Every clip checked by two people, including for any view that could show fetal sex. (Y, K)
12. **Course app, first version.** Home, unit page with four tabs, clip player, drill engine with scheduling, checklist, progress saved on the device. (C)
13. **Clip drills for D1** from the first 40 cases. (C drafts; K approves answers)

### Weeks 7-10

14. **Videos for D1.** Three films from the generated script. Phone on a tripod for the hand, screen capture from the machine. (K presents; Y records; C edits script and overlays)
15. **Sweep trainer prototype.** (C)
16. **Pilot.** 15-20 fellows and colleagues: test, two weeks of use, retest. (K recruits; C builds the test and analyses)

### Months 3-6

17. Units D2-D14, each through the same loop: harvest, cross-check, draft, audit, sign. Additional sources needed: ISUOG fetal echocardiography guideline, ASE 2023, AIUM, Indian guidance. (all)
18. Accounts, subscription payment, certificate, supervisor view. (C)
19. Legal consultation closed out; terms of use and privacy notice. (Y, advisor)
20. Launch of the Detect tier.

## What is needed from Dr Kunda in total, Phase 1

- About 1 hour to sign D1; similar for each later unit.
- Choosing and annotating the first 40 cases: a few sessions.
- Half a day to record three videos.
- A cardiologist's name to approach as co-editor before the Diagnose tier.

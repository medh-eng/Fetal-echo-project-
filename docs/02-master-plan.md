# Master plan: Fetal Echo Project

Version 0.2, 13 Nov 2026. Decisions in section 13 are recorded; build detail is in `06-build-plan.md`.

## 1. The idea in one paragraph

Build **one verified body of knowledge** and publish it four ways: a book, an app, videos and study material. Organise it around what the learner must be able to *do*: **Detect** an abnormal heart on a routine scan, **Diagnose** it on a fetal echocardiogram, and **Decide** what happens next for the pregnancy and the baby. Ship the Detect tier first, because that is where most hearts are missed and where the largest audience is. Build one topic completely, in all four formats, test it on real learners, then repeat.

## 2. Who it is for

| Tier | Learner | Question it answers | Size of audience |
|---|---|---|---|
| **Detect** | Sonologists, obstetricians and radiologists doing anomaly scans; trainees | "Is this heart normal? If not, what do I do?" | Largest |
| **Diagnose** | Fetal medicine specialists, paediatric cardiologists, fellows | "What exactly is this lesion and how will it behave?" | Medium |
| **Decide** | Fetal medicine and cardiac teams, neonatologists, counsellors | "What do we tell the family, where should delivery be, is intervention an option?" | Smallest |

Language is English. A parent-material strand was considered and is out of scope for now (see section 13).

Detect is the first release. Diagnose and Decide are written to reference depth later, with specialist co-authors.

## 3. Where it can honestly be the best

It will not out-rank the established textbooks on authority in year one. It can beat them on:

1. **Training the eye and the hand**, not only the memory.
2. **Format**: every topic exists as text, interactive, video and drills, generated from one source so they never disagree.
3. **Traceability**: every number links to its source and to the clinician who checked it.
4. **Context**: Indian practice, law and referral realities; regional languages; works offline on a phone.
5. **Evidence that it works**: a measured improvement in learners' detection, published.

## 4. Architecture: one spine, four skins

```
sources  ->  evidence ledger  ->  units  ->  build  ->  book / app / video scripts / study items
(papers)     (one claim = one     (lesson     (script)
              source + sign-off)   specs)
```

- **Evidence ledger.** Every factual statement is a *claim* with an ID, a source, a locator (section, table, page) and a status: `ai-extracted`, `ai-cross-checked`, `expert-verified`.
- **Unit.** One lesson: objectives, prose blocks, figures, drills and video beats. Every block cites claim IDs.
- **Build.** A script checks that every claim exists and is sourced, then generates the chapter, the drill set, the video script and the study page. A release build refuses to run if any claim lacks a named human sign-off.

This already works in this repository for the first unit. See `README.md`.

## 5. Innovations worth building

Ranked by teaching value against effort.

| # | Idea | What it is | Needs patient data? |
|---|---|---|---|
| 1 | **Sweep trainer** | A parametric 3D fetal thorax. The learner moves a virtual probe from stomach to upper mediastinum and watches the section change. Lesions are switched on as parameters (VSD size, aortic override, vessel size ratio) | No |
| 2 | **Three-second drills** | A clip plays for a few beats. Normal or not? Where? Each finding has many different clips so the learner cannot memorise one | Yes |
| 3 | **Lesion timelines** | A slider across gestation showing how each lesion evolves, e.g. aortic stenosis towards hypoplastic left heart | Mostly no (illustrated) |
| 4 | **Circulation sandbox** | A simple flow model of the fetal circulation. Narrow a valve or close the foramen and watch flows redistribute; press "birth" to see the transition. Labelled as a teaching model | No |
| 5 | **Missed-diagnosis casebook** | Real misses, why they happened (setting, view, assumption) and the habit that prevents each | Yes |
| 6 | **Embryology "what breaks when"** | A developmental timeline where each step links to the lesions that result when it fails | No |
| 7 | **Counselling guide** | For the clinician: how to explain each finding to parents, with diagrams. English | No |
| 8 | **Scan-room simulations** | Branching cases: you see a view, choose the next step, get feedback | Some |
| 9 | **Structured checklist and report template** | The five-view checklist as a printable and in-app tool | No |

Items 1, 4, 6, 7 and 9 need no patient data, so they can start now while the case library grows.

## 6. The media problem and how to solve it

Clips are the scarce resource. Three supply lines run in parallel:

1. **Own cases, captured prospectively.** From now on, with written consent, save a standard clip set at each cardiac examination: situs, four-chamber, LVOT, RVOT/3VV, 3VT, each in grey-scale and colour, plus a slow sweep. Normal hearts first: they are available daily and the Detect tier is mostly normal anatomy and variants.
2. **Permissioned and open-licensed material.** Collaborating centres, open-access papers under CC-BY, society resources with written permission. Each item logged with its licence.
3. **Illustration and synthetic models.** Commissioned diagrams and the parametric 3D heart cover rare lesions until real clips exist.

Realistic first target: **30 normal and 10 abnormal cases in three months**, not 500.

**Format.** Learners get looping MP4/WebM with a JSON sidecar holding scale, frame rate, gestational age and labels. Original DICOM stays offline in the clinic archive. No DICOM server.

## 7. Technology

Chosen to match what the team already builds (static HTML/JS progressive web apps) and to cost almost nothing to host.

| Layer | Choice | Why |
|---|---|---|
| Content | Markdown + YAML in this Git repository | Any AI and any human can read and edit it; full history |
| Book | Pandoc or Quarto to web, PDF and EPUB | One source, three outputs |
| App | Static PWA, offline-capable, no login at first | Works on a phone in a scan room with poor signal |
| 3D | Three.js, added in Phase 2 | Mature, runs in any browser |
| Scheduling of drills | FSRS via the open-source `ts-fsrs` library | Proven, free |
| Video hosting | Unlisted streaming host; clips for drills served as files | No patient archive online |
| Hosting | GitHub Pages or Cloudflare Pages | Free tier is enough |
| Backend | None until accounts or payments are needed | Fewer things to secure |

## 8. People

AI can draft, check and build. It cannot be the author of record.

| Role | Who | Status |
|---|---|---|
| Editor-in-chief and clinical lead | Dr Kunda Shahane | Confirmed |
| Product owner, build and operations | Your team, with AI tools | Proposed |
| Co-editor, cardiology | Fetal or paediatric cardiologist | **To recruit** before Diagnose tier |
| Section reviewers | Paediatric cardiac surgeon, neonatologist, geneticist, fetal MRI radiologist | To invite per chapter |
| Illustrator / 3D artist | Freelance | Phase 2 |
| Legal review | Health-law counsel | Phase 0, one consultation |
| Pilot learners | 15–20 sonologists and trainees | Phase 1 |

## 9. How the three AIs are used

Roles are by **function**, and they rotate. The rule that matters: the model that drafts a piece never audits it, and the auditor reads the source document, not the drafter's summary.

1. **Harvest.** A model with the source PDF attached extracts claims into the ledger with locators.
2. **Cross-check.** A different model, given the same PDF, confirms or disputes each claim.
3. **Draft.** A model writes the unit using only ledger claims.
4. **Audit.** A different model lists every sentence in the draft that is not backed by a cited claim.
5. **Sign.** The clinical lead reviews disputed and high-risk claims and signs the unit.

Hard rules: no number without a claim ID; no model recalls a threshold, equation or statistic from memory; every unit records which model did which step. Prompts are in `prompts/`. Detail in `04-ai-workflow.md`.

## 10. Law, ethics and safety

India first. This section needs one consultation with a health-law advisor before any patient clip is published; it is a working checklist, not legal advice.

- **PC-PNDT Act.** No published image, clip, caption or metadata may reveal or allow inference of fetal sex. Capture protocol excludes the perineum; every clip is reviewed for this before release.
- **DPDP Act 2023 and Rules 2025.** Written, specific consent for educational use, separate from consent for the scan; a withdrawal route; a record of who consented to what. The Rules phase in through May 2027.
- **Ethics.** Approval from an ethics committee for a teaching case repository, following ICMR guidance.
- **De-identification.** Crop the patient banner out of every frame; strip metadata; second-person check of each clip. Burned-in text is the main risk.
- **Copyright.** No figures or tables copied from textbooks or journals without licence. Facts and equations are restated in our own words with citation. Pirated copies of textbooks are never used as sources.
- **Software as a medical device.** Phase 1–2 tools are educational: reference tables, checklists, simulators on teaching cases. Anything that takes a real patient's measurements and returns advice is deferred until reviewed against CDSCO rules.
- **Clinical safety.** Every page carries its verification status. Unverified content is visibly marked draft.

Detail in `05-governance.md`.

## 11. Proving it works

Built into Phase 1, not bolted on.

- **Design.** 15–20 learners take a clip-based test (view identification, normal/abnormal, localisation), use the Detect module for two weeks, then retake a parallel test.
- **Measures.** Accuracy, time to decision, confidence calibration, and which drills were failed.
- **Use.** Results decide what Phase 2 builds, and are written up for publication.

## 12. Phases, steps and exit criteria

### Phase 0: Foundation (weeks 1–2)

1. Clinical lead reads this plan and marks changes.
2. Answer the five decisions in section 13.
3. Collect the core source PDFs into a private folder (ISUOG 2023 screening, ISUOG fetal echo, ASE 2023, AHA 2014, AIUM, relevant Indian guidance).
4. Review the existing consent wording against teaching use in a paid product; book the legal consultation; start the ethics application.
5. Define the standard clip set and test exporting one normal case from the ultrasound machine end-to-end through de-identification.

Exit: decisions recorded, sources in hand, one clean de-identified normal clip set.

### Phase 1: One complete slice (weeks 3–10)

Topic: **The normal heart in five views.**

1. Harvest and cross-check claims for the unit from the guidelines (about 80–120 claims).
2. Clinical lead verifies claims; unit moves from draft to verified.
3. Write the chapter; commission 8–10 diagrams.
4. Build the study page: checklist, 40 text drills, 30 clip drills from the first normals.
5. Record three videos: machine set-up; the five-view sweep with hand and screen; common pitfalls.
6. Prototype the sweep trainer with a simple geometric heart.
7. Run the pilot test with learners.

Exit: one topic live in four formats, pilot data collected, a measured learning gain or a clear reason why not.

### Phase 2: Detect tier, version 1 (months 3–6)

About 12 units: set-up and physics for the heart; situs; four-chamber; outflow tracts; three-vessel views; colour Doppler in screening; rhythm at screening level; first-trimester heart; normal variants and pitfalls; when and how to refer; what to say to the parents; quality assurance and audit. Sweep trainer with five common lesions. 300+ clip drills. Public launch of the Detect tier.

Exit: Detect tier complete and verified; 200 active learners; cardiology co-editor recruited.

### Phase 3: Diagnose tier (months 6–12)

Lesion atlas, about 40 lesions on a fixed template: definition, embryology, what each view shows, Doppler, differentials, associations and genetics, evolution in utero, counselling points, postnatal pathway. Function, arrhythmias, heart failure and hydrops, twins, maternal disease. Circulation sandbox. Lesion timelines. First book edition (web and PDF).

Exit: 40 lesions verified by cardiology co-editor; book v1 published.

### Phase 4: Decide tier and advanced tools (year 2)

Perinatal planning, fetal intervention, fetal MRI, counselling and ethics in depth, postnatal surgery overview. Reference calculators after regulatory review. Translations. Accreditation for CME credit. Print edition.

## 13. Decisions (recorded 13 Nov 2026)

| Question | Decision |
|---|---|
| First audience | **Detect tier.** Radiologists and gynaecologists doing obstetric scans, fellowship students, other doctors |
| Editor-in-chief | **Dr Kunda Shahane**, MBBS, MS (ObGy), FIFM, Fetal Medicine Consultant, Mayflower Clinic, Nagpur |
| Cardiology co-editor | Open. Needed before the Diagnose tier |
| Language | **English only.** The parent-material strand is dropped from scope for now |
| Business model | **Subscription** |
| Media | Existing normal and anomaly images and clips from 14 years of practice at Mayflower Clinic, to be anonymised; consent held |
| Machine | GE Voluson Signature 18 |

Consequences:

- Subscription means all content must be owned, licensed for commercial use, or open under a licence that permits it. Material licensed "non-commercial" cannot be used.
- An existing archive removes the biggest risk in the plan. The first job becomes cataloguing and anonymising it, not collecting new cases.
- To confirm: that the consent held covers publication for teaching in a paid product, not only clinical care. Where it does not, or cannot be shown, the case is used only after re-consent or not at all.
- Subscription needs accounts and payment, so a small backend enters at launch (Phase 2), not before.

## 14. Risks

| Risk | Mitigation |
|---|---|
| Clinical lead's time is the bottleneck | Verification is batched by risk: models pre-sort claims so the lead reads disputed and high-stakes ones first |
| Too few abnormal clips | Illustration and synthetic models; collaborating centres; Detect tier needs mostly normals |
| An error reaches learners | Release build blocks unverified claims; visible status on every page; public errata log |
| Scope creep | One slice at a time; nothing enters a phase without an exit criterion |
| Legal problem with patient media | Consultation and ethics approval before first publication; PC-PNDT review of every clip |
| Tools or models change | Content is plain text in Git, independent of any vendor |

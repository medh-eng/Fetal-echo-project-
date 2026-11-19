# Fetal Echo Project

A book, an app, videos and study material for fetal echocardiography, all generated from one verified body of knowledge.

**Status: draft. Nothing here is released for clinical use.**

## Start here

| Read | For |
|---|---|
| [docs/02-master-plan.md](docs/02-master-plan.md) | The plan: audience, architecture, phases, decisions needed |
| [docs/01-critique-of-gemini-plan.md](docs/01-critique-of-gemini-plan.md) | What was wrong with the first blueprint and what was kept |
| [docs/03-syllabus.md](docs/03-syllabus.md) | Full list of units in three tiers: Detect, Diagnose, Decide |
| [docs/04-ai-workflow.md](docs/04-ai-workflow.md) | How Claude, ChatGPT and Gemini are used, step by step |
| [docs/05-governance.md](docs/05-governance.md) | Consent, PC-PNDT, data protection, copyright, safety |
| [docs/06-build-plan.md](docs/06-build-plan.md) | What is being built, the steps, and who does each |
| [docs/07-clinic-checks.md](docs/07-clinic-checks.md) | One form: archive survey, Voluson export check, consent check |
| [docs/08-pilot-protocol.md](docs/08-pilot-protocol.md) | How the course will be tested on learners |

## How it works

```
content/sources/   registry of source documents
content/ledger/    claims: one fact, one source, one locator, one status
content/units/     lessons built only from claims
tools/build.py     checks everything, then generates the outputs
dist/<unit>/       chapter.md, drills.json, video-script.md, study.html, review.md
dist/app/          installable course app (all units, offline)
dist/book/         book.md, book.html, book.pdf (all units)
dist/web/          website pages and WordPress fragments for public units
dist/editor/       one review pack for the editor-in-chief (all unsigned units)
content/pilot/     pilot test: wording, items, answer key (key never reaches the page)
tools/clinic/      case catalogue, anonymiser and clip list builder, for the clinic computer
tasks/             ready-to-paste tasks for the other AI models
prompts/           the four prompts for harvest, cross-check, draft, audit
```

A claim moves through three states: `ai-extracted`, `ai-cross-checked`, `expert-verified`.
Every built page shows the lowest state it contains. A release build fails unless every claim is expert-verified and the unit is signed.

## Try it

```
pip install pyyaml
python tools/build.py            # validate and build drafts
python tools/build.py --check    # validate only
python tools/build.py --release  # must fail until a clinician has signed
```

Then open `dist/app/index.html` in a browser for the course app, or `dist/D1/study.html` for a single unit.

## What exists now

- **222 claims** from two guidelines (ISUOG 2023 screening, ASE 2023 fetal echocardiography), all with page references. ChatGPT has checked the first 118 against the PDFs, including a second pass on 22 that were reworded. Claude has checked the remaining 104 through a reader on the PDF text (limits in `tasks/results/task-1-crosscheck.md`). Status now: 57 expert-verified, 151 cross-checked, 14 awaiting re-check.
- **365 more claims for the Diagnose and Decide tiers** (lesion atlas, biometry, surveillance, delivery planning, counselling, intervention), harvested by Claude on 17 Nov from ASE 2023 and AHA 2014 and checked by Claude against the PDF pages. Independent review is complete: 311 confirmed, 49 require wording corrections and five require locator corrections. Results await application to the ledger. See [the batch summary](tasks/results/task-i-notes.md).
- **17 units, 189 drills**, all in the app and the book:
  - Detect: D0 Why hearts are missed, D1 Five views, D2 Machine set-up, D3 Laterality and situs, D4 Four-chamber view, D5 Outflow tracts, D6 Three-vessel views, D7 Colour Doppler, D8 Rate and rhythm, D9 The heart at 11 to 14 weeks, D10 Variants and pitfalls, D11 When and how to refer, D13 Quality and audit.
  - Foundation: F1 Ultrasound modes, F2 Fetal rhythm: tools and mechanisms.
  - Diagnose: XA5 The complete fetal echocardiogram, XC1 Assessing cardiac function.
- **All 17 units audited** by ChatGPT against the ledgers on 16 Nov; findings applied. The [six-unit re-audit](tasks/results/task-g.md) and [follow-up on the November 17 edits](tasks/results/task-g-addendum.md) are complete. The outstanding wording issues are listed in the re-audit.
- **Pilot test page** (`dist/app/test.html`): timed test on clips with a results file and a scoring script. Runs on placeholders until clips and the editor's answer key exist.
- **Clip drills** in the app: appear when a list of checked clips is placed on the hosting server (`tools/clinic/README.md`). No real clip has been used yet.
- **Sweep trainer** (`dist/app/sweep.html`): five schematic planes with a slider and a 'which plane?' test. Drawings await the editor's mark-up.
- **Status board** (`dist/editor/status-board.html`): all 51 units of the syllabus and the stage each has reached. 34 have no draft yet; each has its sources and next task in `content/plan/units.yaml`.
- **Nothing is currently signed.** D1 was signed on 13 Nov; the cross-check then found five of its claims had lost a qualifier, so they were reworded and D1 waits for the editor to approve those five again.
- **Editor's review pack** (`dist/editor/review-pack.html`): decisions, the five claims to approve again, and new claims a second AI has confirmed. Claims not yet cross-checked are held back from her.
- **Clinic tools** (`tools/clinic/`): offline case catalogue and clip anonymiser.
- Not drafted: D12 and D14 (no sources yet).

## Where things stand

| Next step | Who | Where |
|---|---|---|
| Apply the fourteen re-check results, including the AS23-089 locator correction | Claude | `tasks/results/task-h.csv` |
| Apply the eight independent reviews and return disputed wording for a fresh check | Claude | `tasks/claude-tasks.md`, task 15 |
| Pick one source per topic | Dr Kunda | `tasks/results/task-s1.md` |
| Independently check the 112 fetal arrhythmia claims, including the 14 separate dose entries and flagged figures | Claude or Gemini | `tasks/results/task-h2.yaml` |
| One sitting with the review pack | Dr Kunda | `dist/editor/review-pack.html` |
| Mark up the five sweep drawings | Dr Kunda | `dist/editor/sweep-schematics.html` |
| Clinic checks form (archive, Voluson export, consent) | Project owner | `docs/07-clinic-checks.md` |
| Resolve D1 and D0 wording and review the existing signed claim IS23-080 with the editor | Claude and Dr Kunda | `tasks/results/task-g.md` |
| Record sign-off; first real clips; lesion atlas drafts | Claude Sonnet / Opus | `tasks/claude-tasks.md`, tasks 3, 6, 7, 12 |

## Rules

See [AGENTS.md](AGENTS.md). No patient media in this repository, ever.

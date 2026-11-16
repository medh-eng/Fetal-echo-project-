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
tools/clinic/      case catalogue and anonymiser, for the clinic computer
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

- **222 claims** from two guidelines (ISUOG 2023 screening, ASE 2023 fetal echocardiography), all with page references. On 16 Nov 2026 ChatGPT checked the first 118 against the PDFs: 88 confirmed, 8 given corrected page references, 22 reworded to restore a lost qualifier. Status now: 57 expert-verified, 39 cross-checked, 126 awaiting cross-check (22 reworded, 104 newly extracted by ChatGPT).
- **16 units, 181 drills**, all in the app and the book:
  - Detect: D0 Why hearts are missed, D1 Five views, D2 Machine set-up, D3 Laterality and situs, D4 Four-chamber view, D5 Outflow tracts, D6 Three-vessel views, D7 Colour Doppler, D8 Rate and rhythm, D9 The heart at 11 to 14 weeks, D10 Variants and pitfalls, D11 When and how to refer, D13 Quality and audit.
  - Foundation: F1 Ultrasound modes, F2 Fetal rhythm: tools and mechanisms.
  - Diagnose: XA5 The complete fetal echocardiogram.
- **Nothing is currently signed.** D1 was signed on 13 Nov; the cross-check then found five of its claims had lost a qualifier, so they were reworded and D1 waits for the editor to approve those five again.
- **Editor's review pack** (`dist/editor/review-pack.html`): decisions, the five claims to approve again, and new claims a second AI has confirmed. Claims not yet cross-checked are held back from her.
- **Clinic tools** (`tools/clinic/`): offline case catalogue and clip anonymiser.
- Not drafted: D12 and D14 (no sources yet).

## Where things stand

| Next step | Who | Where |
|---|---|---|
| Re-check of 22 reworded claims; audit of 16 units | ChatGPT | `tasks/chatgpt-tasks-round2.md` |
| Cross-check of the 104 claims ChatGPT extracted | Claude Opus, or Gemini | `tasks/claude-tasks.md`, task 1 |
| Apply the results; fix units | Claude Sonnet | `tasks/claude-tasks.md`, task 2 |
| Clinic checks form (archive, Voluson export, consent) | Project owner | `docs/07-clinic-checks.md` |
| One sitting with the review pack | Dr Kunda | `dist/editor/review-pack.html` |
| Sweep trainer, pilot test page, clips in the app | Claude Opus / Sonnet | `tasks/claude-tasks.md`, tasks 4 to 6 |

## Rules

See [AGENTS.md](AGENTS.md). No patient media in this repository, ever.

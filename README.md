# Fetal Echo Project

A book, an app, videos and study material for fetal echocardiography, all generated from one verified body of knowledge.

**Status: early draft. Nothing here is verified for clinical use.**

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

- **118 claims**: 96 from the ISUOG 2023 screening guideline and 22 from the ASE 2023 fetal echocardiography guideline, all with page references. 62 are expert-verified.
- **8 units.** Signed: **D1** The normal heart in five views. Draft, awaiting cross-check, audit and signature: **D0** Why hearts are missed, **D7** Colour Doppler in screening, **D8** Rate and rhythm, **D9** The heart at 11 to 14 weeks, **D11** When and how to refer, **D13** Quality assurance and audit, **F1** Ultrasound modes. 102 drills in all.
- Course app, combined book and website page generated from the units.
- **Editor's review pack** (`dist/editor/review-pack.html`): one printable document with every open decision and every claim still to check, each listed once.
- **Clinic tools** (`tools/clinic/`): offline case catalogue and clip anonymiser.
- **Tasks for ChatGPT** (`tasks/chatgpt-tasks.md`): cross-check, audit and further harvest, ready to paste.

## Where things stand

| Next step | Who | Where |
|---|---|---|
| Run the three ChatGPT tasks and bring back the results | Project owner | `tasks/chatgpt-tasks.md` |
| Fill the clinic checks form (archive, Voluson export, consent) | Project owner | `docs/07-clinic-checks.md` |
| Apply results, fix units, rebuild the review pack | Claude | `tools/apply_crosscheck.py` |
| Sign the review pack | Dr Kunda | `dist/editor/review-pack.html` |

## Rules

See [AGENTS.md](AGENTS.md). No patient media in this repository, ever.

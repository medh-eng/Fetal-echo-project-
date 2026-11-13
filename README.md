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

- **118 claims**: 96 from the ISUOG 2023 screening guideline and 22 from the ASE 2023 fetal echocardiography guideline, all with page references.
- Unit **D1, The normal heart in five views**: 10 sections, 22 drills, video outline. Reviewed and signed by the editor on 13 Nov 2026 (62 claims expert-verified).
- Unit **F1, Ultrasound modes used in fetal echocardiography**: 13 sections, 15 drills, checklist, video outline. Draft: its 22 ASE claims are not yet cross-checked or signed.
- Course app, combined book and website page generated from the units.

## Rules

See [AGENTS.md](AGENTS.md). No patient media in this repository, ever.

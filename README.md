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

## How it works

```
content/sources/   registry of source documents
content/ledger/    claims: one fact, one source, one locator, one status
content/units/     lessons built only from claims
tools/build.py     checks everything, then generates the outputs
dist/<unit>/       chapter.md, drills.json, video-script.md, study.html
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

Then open `dist/D1/study.html` in a browser.

## What exists now

- Unit **D1, The normal heart in five views**: 12 seed claims, a short draft chapter, 8 drills, a video outline. All unverified, and the unit lists six areas still waiting for sourced claims.

## Rules

See [AGENTS.md](AGENTS.md). No patient media in this repository, ever.

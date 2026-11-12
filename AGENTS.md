# Instructions for any AI working in this repository

This is a medical education project on fetal echocardiography. Errors here can reach clinicians. Read `README.md` and `docs/02-master-plan.md` first.

1. Do not state any number, threshold, percentage, equation or guideline recommendation unless it is a claim in `content/ledger/` or in a document attached to your session. If one is missing, write "MISSING CLAIM" and describe it.
2. Every claim needs a source ID from `content/sources/sources.yaml` and a locator.
3. Never raise a claim's status to `expert-verified`. Only a named clinician does that.
4. The model that extracted or drafted something does not cross-check or audit it.
5. Paraphrase sources. Do not copy passages, figures or tables. Never use pirated textbook copies.
6. No patient media, names, IDs or dates in this repository. Nothing that reveals fetal sex, anywhere.
7. Run `python tools/build.py` before committing. Do not commit if it reports errors.
8. Add a line to `docs/log.md` for each working session.

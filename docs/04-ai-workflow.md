# Working with Claude, ChatGPT and Gemini

## Principle

A language model is a fast, well-read junior who sometimes invents things with total confidence. Two juniors agreeing is not proof. So:

1. Every fact enters through the **evidence ledger**, with a source and a locator.
2. A **different** model checks it against the **source document**, not against the first model's summary.
3. A **named clinician** signs it.
4. The build refuses to release anything unsigned.

## The loop for one unit

| Step | Who | Input | Output | Where it goes |
|---|---|---|---|---|
| 1. Harvest | Model A, with the PDF attached | Source PDF + `prompts/01-harvest.md` | Claims in YAML | `content/ledger/<unit>.yaml`, status `ai-extracted` |
| 2. Cross-check | Model B (different vendor), with the same PDF | Claims + PDF + `prompts/02-crosscheck.md` | Confirm / dispute / cannot find, per claim | Status becomes `ai-cross-checked`, or a `dispute` note is added |
| 3. Draft | Any model | Verified claims + unit template + `prompts/03-draft.md` | Unit YAML: text blocks, drills, video beats | `content/units/<unit>.yaml` |
| 4. Audit | A model that did not do step 3 | Draft + ledger + `prompts/04-audit.md` | List of unsupported sentences | Fix or add claims; repeat |
| 5. Sign | Clinical lead | Disputed and high-risk claims first, then the built chapter | `verified_by` and date on each claim | Status `expert-verified` |
| 6. Build | Script | `python tools/build.py` | Chapter, drills, video script, study page | `dist/` |

## Which model for what

Any of the three can do any step. Practical defaults, to be changed whenever experience says otherwise:

- **Gemini**: harvesting from long PDFs and Deep Research sweeps for sources. Always demand page and table locators.
- **ChatGPT**: cross-check and audit of work drafted elsewhere; generating drill variants from verified claims.
- **Claude**: drafting units, maintaining this repository, building the app and tools.

Rotate the harvest and cross-check roles between units so no single model's blind spots become the project's.

## Hard rules for every model

Paste these at the top of any session (also in `AGENTS.md`):

1. Do not state any number, threshold, percentage, equation or guideline recommendation unless it is in the ledger or in a document attached to this session. If you need one that is missing, say "MISSING CLAIM" and describe it.
2. Give a locator (section heading, table or figure number, page) for every extracted claim.
3. Paraphrase. Do not copy sentences from sources into text meant for publication.
4. Never use scanned or pirated copies of textbooks as sources.
5. Mark uncertainty plainly. "I could not find this in the document" is a good answer.
6. Record your model name in `extracted_by`, `checked_by` or the unit's `drafted_by`.

## How to hand work between tools

The repository is the shared memory. Each session:

1. Start by reading `README.md`, `docs/02-master-plan.md` and the unit you are working on.
2. Do one step of the loop.
3. Save the result into the repository (commit, or paste the YAML back for someone to commit).
4. Add a line to `docs/log.md`: date, model, step, unit, what changed.

Claude can read and write the repository directly. For ChatGPT and Gemini, either connect the GitHub repository in their apps or paste the relevant file in and the result back.

## What needs a human, always

- Whether a claim is true and current.
- Choosing between conflicting sources.
- Anything about a specific patient.
- Tone of counselling material.
- Final review of every clip for identity and for PC-PNDT compliance.

# Tasks for ChatGPT or Gemini, round 5 (21 Nov 2026)

Two jobs, both for a model that is **not Claude** (Claude extracted the claims and drafted the units). Task J first: the twelve new units cannot move forward while 57 claims they leave out are unchecked.

## Task J. Re-check 57 claims: 49 reworded after task I, 8 new

About 40 minutes. Attach: the two guideline PDFs (ASE 2023, AHA 2014) and `tasks/claims-for-chatgpt-or-gemini.md`. Your own task I results (`tasks/results/task-i2.csv` to `task-i8.csv`, `task-i-notes.md`) help for the 49.

```
57 claims are attached with the two guideline PDFs. 49 were found DISTORTED in your task I
check and have been reworded by their extractor, following your detail; the note on each
quotes your finding. 8 are new (AS23-358 to 362, AH14-330 to 332), harvested from the
"missing claims" table in your task-i-notes.md.

For each claim, read the printed page itself (not your earlier answer):
1. Does the new wording say what the page says, with the same strength (must, should,
   may, can) and the same scope (which lesion, which population, which condition)?
2. Did the rewording fix your finding without adding a new error?
3. Is the locator right?

Verdicts: CONFIRMED, CORRECT LOCATOR (give the right one), DISTORTED (say exactly what
is wrong), NOT FOUND.

Three to look at closely:
- AS23-327: now says early branching identifies the vessel, not the lesion, and names the
  other panels of Figure 26. Check against the figure caption on p. 715.
- AS23-284: now framed as the illustrated case of Figure 21, not a grading rule.
- AH14-332 (new): the pressure values are given as printed on p. 2218. Confirm the
  numbers and the endpoint ("favourable outcome for two-ventricle repair") exactly.

Not harvested: your Figure 30F candidate (L-shaped branching in a right arch with
mirror-image branching). The p. 718 caption for panel F describes a double aortic arch.
Tell us if you meant another page or figure.

Output: CSV, header claim_id,verdict,detail - one row per claim.
Use nothing from memory.
```

Save as `tasks/results/task-j.csv`. Then (Sonnet): `python tools/apply_crosscheck.py tasks/results/task-j.csv --by "..."`, rebuild, and put each confirmed claim into the unit that lists it under `missing_claims`.

## Task K. Audit twelve new Diagnose and Decide units

About 60 minutes; can be split across sessions. Attach: `content/ledger/ASE-2023-FETALECHO.yaml`, `content/ledger/AHA-2014-FETALCARDIAC.yaml`, `prompts/04-audit.md`, and these units from `content/units/`: Z2, XB4, XB2, XB1, XB8, XB3, XB5, XA6, Z3, XA2, Z1, Z5.

```
Twelve units were drafted by Claude on 21 Nov 2026 only from claims marked
ai-cross-checked. Audit each against the claims it cites, with prompts/04-audit.md.

For every text block, table row, drill and checklist item:
1. Does each sentence rest on the claims it cites? Flag any sentence that adds a fact,
   a number, a direction ("larger", "smaller"), or a strength ("must") the claims do not
   give.
2. Has a qualifier been lost (a "may" that became "is"; "in selected cases"; "when
   present"; a lesion-specific point stated as general)?
3. Drills: is exactly one option correct according to the cited claims? Is any wrong
   option actually defensible?
4. Z3 and Z5 rest mostly on AHA 2014. Flag any sentence that presents a 2014 statement
   as current practice without saying so.
5. Check that each unit's missing_claims list is honest about what was left out.

Output: one short list per unit, then "Units with nothing to fix: ...".
Use nothing from memory. If a fact is missing from the ledger, say MISSING CLAIM.
```

Save as `tasks/results/task-k.md`, then set `audited_by` in each unit when the findings are applied (Claude may apply them; Claude may not audit its own drafts).

## Still open from round 4

Task H (14 claims Claude reworded) was not applied: the tool stops because ChatGPT both extracted the originals and checked the rewording. The project owner to decide whether a check of Claude's rewording by the original extractor counts; if not, Gemini should do task H again.

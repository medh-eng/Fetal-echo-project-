# Tasks for ChatGPT or Gemini, round 6 (22 Nov 2026)

Both jobs need a model that is **not Claude**.

## Task L. Audit four new units

About 25 minutes. Attach: `content/ledger/AHA-2014-FETALCARDIAC.yaml`, `content/ledger/ASE-2023-FETALECHO.yaml`, `prompts/04-audit.md`, and from `content/units/`: XC7, XC5, XC8, XB9.

```
Four short units were drafted by Claude on 22 Nov 2026 only from claims marked ai-cross-checked.
Audit each against the claims it cites, using prompts/04-audit.md.
For every text block, table row, drill and checklist item:
1. Does each sentence rest on the claims it cites? Flag any added fact, number, direction or strength.
2. Has a qualifier been lost (Class and level of evidence, "may", "in selected cases")?
3. Drills: is exactly one option correct according to the cited claims? Is any wrong option defensible?
4. XC7 lists referral by recommendation class. Check every class against AH14-001, 003, 004, 005.
   AH14-005 prints "vitamin K agonists" as not indicated; the unit says "as printed". Is that fair?
5. Are the missing_claims lists honest about what was left out?
Output: one short list per unit, then "Units with nothing to fix: ...". Use nothing from memory.
```

Save as `tasks/results/task-l.md`. Claude applies the findings and sets `audited_by`.

## Task M. Re-check one claim

Attach the ASE 2023 PDF. Claim **AS23-412** (Table 13, aortic stenosis, key observations) was reworded on 22 Nov after task J found the earlier wording DISTORTED. Check the new wording against the printed table on p. 708: thickened valve in systole on the LV outflow view; a possibly dilated ascending aorta on the three-vessel view (plus/minus entry); LV hypertrophy or dilation/dysfunction on the four-chamber view, with no statement that dilation and dysfunction occur together. Verdict: CONFIRMED, CORRECT LOCATOR, DISTORTED or NOT FOUND, with the reason. Save as `tasks/results/task-m.csv` (header `claim_id,verdict,detail`).

## Still open

- **Task H** (14 claims Claude reworded, same-model rule): the project owner decides whether a check by the original extractor counts. If not, Gemini does it. It unblocks the 14 held-back claims and so the remaining Detect units.
- **H2 arrhythmia claims** (`tasks/results/task-h2.yaml`, 112 claims, ChatGPT-extracted): not in the ledger. They need a second model with the AHA 2024 source, which has no open copy; Dr Kunda or the owner to supply the paper.

## Task N. Cross-check the AIUM claims

About 30 minutes. Attach the AIUM Practice Parameter PDF, `content/ledger/AIUM-2020-FETALECHO.yaml` and `prompts/02-crosscheck.md`. Claude extracted all 41 claims (AI20-001 to AI20-062) on 23 Nov. Check each against the printed page: statement, every number, the class of each indication list (indicated, may be considered, limited data, only if the detailed scan is abnormal), and the E-page locator. Verdicts: CONFIRMED, CORRECT LOCATOR, DISTORTED, NOT FOUND. Save as `tasks/results/task-n.csv`. A claim not checked by a different model stays ai-extracted, so no unit can use it.

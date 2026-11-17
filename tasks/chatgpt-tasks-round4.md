# Tasks for ChatGPT, round 4 (16 Nov 2026, evening)

Three jobs. **Task I is the largest and matters most**: it unblocks the Diagnose and Decide tiers. Round 3 (`tasks/chatgpt-tasks-round3.md`, the harvest for the Diagnose and Decide tiers) is still open and matters more; do that first if time is short.

## Task G. Re-audit six revised units

About 15 minutes. Attach: the two ledger files from `content/ledger/`, your own `tasks/results/task-e.md`, and these six files from `content/units/`: D0, D1, D2, D5, D6, XA5.

```
On 16 Nov you audited seventeen units (attached: task-e.md). Claude has changed six of them
in response: D0, D1, D2, D5, D6 and XA5. The ledgers attached are the only permitted facts.

For each of the six units:
1. Go through your own findings for that unit one by one. Resolved, partly resolved, or
   not resolved? Quote the new text.
2. Has the change introduced a new error: a lost qualifier, a claim cited that does not
   support the sentence, an echocardiography requirement presented as a screening one?
3. D1 only: sentences were changed in the text, in drill D1-Q21, and in video beats
   5, 6, 10 and the last. Check each against the claims it cites.

Also: your finding 1 on D11 was not applied. The sentence "This is why quality screening
and timely referral matter" cites IS23-080, and the ledger wording of IS23-080 itself ends
"which is why quality screening and timely referral matter". Say whether you still hold
the finding, and if so whether the fault is in the claim (check it against the PDF if you
have it) rather than in the unit.

Output: one short list per unit, then one line: "Units with nothing left to fix: ...".
Use nothing from memory. If a fact is missing from the ledger, say MISSING CLAIM.
```

On 17 Nov ten units (D2, D3, D4, D6, D9, D10, D11, F2, XA5, XC1) also had single sentences changed to follow twelve reworded claims, listed in `tasks/results/task-1-crosscheck.md`. If time allows, check each changed sentence against its reworded claim.

Save as `tasks/results/task-g.md` (a pull request is fine).

## Task H. Sixteen claims that need eyes on the PDF (Gemini preferred; ChatGPT may do the twelve reworded ones)

About 20 minutes. Attach: both guideline PDFs, `tasks/claims-for-claude-or-gemini.md` (the sixteen claims) and `tasks/results/task-1-crosscheck.md`.

```
Sixteen claims are attached with the two guideline PDFs. Read the PDF page itself for each.
Twelve were reworded by Claude on 17 Nov after a cross-check; four could not be settled
because Claude's reader could not see table layout or figures (AS23-048, 076, 082, 119).

For each claim give: claim_id, verdict, detail.
Verdicts: CONFIRMED, CORRECT LOCATOR, DISTORTED, NOT FOUND.
For the four unsettled claims, look at the table cell or figure named in the note and say
exactly what it shows.
Also look at Table 3 of the ASE guideline (p. 686) and confirm, row by row, the
required/optional entries used by claims AS23-042, 046, 047, 049, 050, 054 and 063.
Use nothing from memory.
```

Save as `tasks/results/task-h.csv` (columns `claim_id,verdict,detail`). ChatGPT extracted the four unsettled claims, so those four must be checked by Gemini or Claude, not ChatGPT.

## Task I. Cross-check 349 claims Claude harvested on 17 Nov (ChatGPT or Gemini; not Claude)

Claude read both documents through a web reader that sees text, not pages: figures were not seen, tables were flattened, page numbers come from the reader. Your check against the PDF pages is what makes these claims usable.

Attach:
- the ASE 2023 PDF (as before) with `content/ledger/ASE-2023-FETALECHO.yaml`, and
- the AHA 2014 PDF (free copy: https://escholarship.org/uc/item/9dq2k9vh) with `content/ledger/AHA-2014-FETALCARDIAC.yaml`,
- and `prompts/02-crosscheck.md`.

One chat per batch, so each stays within length:

| Batch | Claims | Source pages |
|---|---|---|
| I1 | AS23-150 to 166 (biometry) and AS23-600 to 615 (IV.D, Table 15) | pp. 689-693, 718-719 |
| I2 | AS23-200 to 286 (single ventricle, AV valves, septal) | pp. 704-713, Tables 13-14 |
| I3 | AS23-300 to 351 (outflow tract lesions) | pp. 707-715 |
| I4 | AS23-400 to 447 (obstructive and regurgitant lesions) | pp. 708-718 |
| I5 | AS23-500 to 525 (arch, ductus, veins, other) | pp. 705-718 |
| I6 | AH14-001 to 025 (the Recommendations section) | pp. 2226-2227 |
| I7 | AH14-100 to 131 (genetics, extracardiac, wellness, counselling) | pp. 2206-2211 |
| I8 | AH14-200 to 220 and AH14-300 to 324 (intervention, TTTS, delivery planning) | pp. 2217-2226 |

Prompt for each batch:

```
Follow the attached prompts/02-crosscheck.md. Check every claim with the IDs [RANGE] in
the attached ledger against the attached PDF pages. For each give: claim_id, verdict,
detail. Verdicts: CONFIRMED, CORRECT LOCATOR, DISTORTED, NOT FOUND.
Pay special attention to:
- claims whose note says the table text was flattened: confirm the row and column;
- every number, threshold, percentage and gestation: confirm it digit by digit, and
  check for lost minus signs;
- the strength of wording (must / should / may / is reasonable) and, for AHA claims,
  the Class and Level of Evidence of each item.
Use nothing from memory.
```

Save each as `tasks/results/task-i1.csv` ... `task-i8.csv` (columns `claim_id,verdict,detail`). A pull request is fine.

Also look for, and report as MISSING CLAIM with page, these items the reader saw but Claude left out because the text was unclear: the TOF row of ASE Table 13 on aortic-to-pulmonary valve ratio and pulmonary valve Z-score as predictors of neonatal intervention; the pulmonary stenosis row on tricuspid regurgitation and the risk of sinusoids; the gestation at which ductal flow direction is read in tetralogy; AHA 2014 recommendation on nuchal translucency of 3 mm or more with abnormal ductus venosus flow.

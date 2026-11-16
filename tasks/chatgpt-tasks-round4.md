# Tasks for ChatGPT, round 4 (16 Nov 2026, evening)

Two short jobs. Round 3 (`tasks/chatgpt-tasks-round3.md`, the harvest for the Diagnose and Decide tiers) is still open and matters more; do that first if time is short.

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

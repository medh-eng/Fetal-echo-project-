# Tasks for ChatGPT, round 2 (16 Nov 2026)

Two jobs. A new chat for each. Paste the grey box as the first message and attach the files listed. Save the results in `tasks/results/` as before (a pull request is fine) or paste them into the Claude chat.

PDFs (keep them out of the repository):

- ISUOG 2023 screening guideline: https://www.isuog.org/static/a529f402-06f9-42b6-ae9abdc736c43bf2/UOG-2023-Carvalho-ISUOG-Practice-Guidelines-updated-fetal-cardiac-screening.pdf
- ASE 2023 fetal echocardiogram guideline: https://www.asecho.org/wp-content/uploads/2025/04/PIIS0894731723002067-1.pdf

---

## Task D. Re-check 22 reworded claims

About 10 minutes. Attach: both PDFs and `tasks/claims-for-chatgpt-or-gemini.md`.

```
In your cross-check of 16 Nov you marked 22 claims DISTORTED. Claude has reworded each one
from your explanation. Check the new wording against the attached PDFs, not against your
earlier notes.

For each claim in the attached file return one verdict:
- CONFIRMED: the document says this, with this strength of wording, at this place.
- CORRECT LOCATOR: true to the document but found elsewhere (give the locator).
- DISTORTED: the document says something different (say exactly what, with locator).
- NOT FOUND.

Be strict about numbers, units, qualifiers and the items in lists.

Output: a CSV in one code block with exactly this header and 22 rows:
claim_id,verdict,detail
Put detail in double quotes; leave it empty for CONFIRMED. Use nothing from memory.
```

Save as `tasks/results/task-d.csv`.

---

## Task E. Audit sixteen units

About 45 minutes; it can be split into two chats of eight units. Attach: the two ledger files from `content/ledger/` and all sixteen files from `content/units/`. PDFs are not needed.

```
You are the adversarial reviewer for a medical education course on the fetal heart.
Assume the drafts contain errors. Errors here can reach clinicians.

Attached are two ledger files (the only permitted facts; each claim has an id) and sixteen
unit files. In a unit, every text block, table, drill, checklist item and video beat lists
the claim ids it rests on. Blocks marked "kind: framing" may have no claims but must
contain no clinical fact.

Two groups:
- NEW units, never audited: D2, D3, D4, D5, D6, D10, F2, XA5. Audit in full.
- REVISED units, changed after your audit of 16 Nov: D0, D1, D7, D8, D9, D11, D13, F1.
  Check that each of your earlier findings was resolved without introducing a new error,
  then audit any text that is new.

Note that several ledger claims were reworded on 16 Nov; use the ledger as attached.

For each unit report:
1. Support. Does each cited claim support the sentence, table row, drill, checklist item
   or video beat as written? Flag overstatement, lost qualifiers, changed numbers, and
   claims cited that say something else. Check every table cell.
2. Unsupported clinical statements, including any inside a "framing" block.
3. Drills. The first option is meant to be the only correct one. Is exactly one option
   correct by the ledger? Could an expert argue for another? Is a wrong option supported
   by a claim?
4. Safety. Anything that could lead to a harmful action or to false reassurance.
5. Wording that could reveal or hint at fetal sex.
6. Mixing of sources. IS23 claims are a screening guideline; AS23 claims are an
   echocardiography guideline. Flag any place where an echocardiography requirement is
   presented as a screening requirement, or the reverse. Units F2 and XA5 are about
   echocardiography by design.

Output: one numbered list per unit; each finding with location, problem, and a suggested
fix using only ledger claims. Say so when a category has no findings. For the revised
units add one line: "Earlier findings resolved: all / all except ...". End with the ten
most important findings across all units.

Use nothing from memory. If a fact is missing from the ledger, say "MISSING CLAIM" and
describe it; do not supply it.
```

Save as `tasks/results/task-e.md`.

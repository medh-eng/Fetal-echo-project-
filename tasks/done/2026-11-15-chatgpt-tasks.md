# Tasks for ChatGPT, 15 Nov 2026

Three separate jobs. Start a **new chat for each**. Paste the text in the grey box as the first message and attach the files listed. Bring back exactly the output asked for; Claude applies it to the repository.

Why ChatGPT and not Claude: Claude extracted these claims and drafted these units. The project rule is that a different model checks them against the source.

Get the two PDFs first (both free to download):

- ISUOG 2023 screening guideline: https://www.isuog.org/resource/updated-isuog-practice-guidelines-fetal-cardiac-screening.html
- ASE 2023 fetal echocardiogram guideline: https://www.asecho.org/guideline/fetal-echo

Keep the PDFs out of the GitHub repository.

---

## Task A. Cross-check all 118 claims against the two guidelines

Time: about 30 minutes. Attach: both PDFs and `tasks/crosscheck-claims.md`. If ChatGPT stops part-way, tell it to continue from the next claim id.

```
You are auditing extracted claims against the two attached guideline PDFs for a medical
education project. Do not rely on memory or on the extractor's wording. Open the PDF and
find the passage for every claim.

The attached file crosscheck-claims.md lists claims in two groups, one per source document.
For each claim, find the passage at or near the locator given and return one verdict:

- CONFIRMED: the document says this, with this strength of wording, at this place.
- CORRECT LOCATOR: the claim is true to the document but is found elsewhere. Give the right
  section, table or figure, and page.
- DISTORTED: the document says something different. Say exactly what it says, with locator.
- NOT FOUND: you cannot find support in the document.

Be strict about numbers, units, "must / should / may", and lists (an item added or dropped
from a list is DISTORTED). The ASE claims were read through a web reader, so check every
ASE page number against the printed journal page numbers in the PDF.

For claim AS23-014 also answer: does the guideline text (around p. 689) list the aortic
arch and isthmus among the required pulsed-wave Doppler sites while Table 6 marks them
optional? Quote no more than a short phrase from each place and give both locators.

Output 1: a CSV in one code block, with exactly this header and one row per claim, all 118:
claim_id,verdict,detail
Put the detail in double quotes. Leave detail empty for CONFIRMED.

Output 2: for each of the two documents, up to ten important facts relevant to screening
the fetal heart or to ultrasound modes that are in the document but not in the claims.
Give each with its locator. Paraphrase; do not copy sentences.

Do not rewrite the claims. Do not add facts from memory. If you cannot open a PDF, stop
and say so.
```

Bring back: the CSV and the list of missed facts.

---

## Task B. Audit seven drafted units

Time: about 30 minutes. Attach: `content/ledger/ISUOG-2023-SCREEN.yaml`, `content/ledger/ASE-2023-FETALECHO.yaml`, and these seven files from `content/units/`: `D0-why-hearts-are-missed.yaml`, `D7-colour-doppler-in-screening.yaml`, `D8-rate-and-rhythm.yaml`, `D9-heart-at-11-14-weeks.yaml`, `D11-when-and-how-to-refer.yaml`, `D13-quality-assurance-and-audit.yaml`, `F1-ultrasound-modes.yaml`. The PDFs are not needed.

```
You are the adversarial reviewer for a medical education course on screening the fetal
heart. Assume the drafts contain errors. Errors here can reach clinicians.

Attached are two ledger files (the only permitted facts; each claim has an id) and seven
unit files. In a unit, every text block, table, drill, checklist item and video beat lists
the claim ids it rests on. Blocks marked "kind: framing" are allowed to have no claims but
must contain no clinical fact.

Work through each unit in turn and report:

1. Support. For every block, table row, drill, checklist item and video beat: does each
   cited claim actually support the sentence as written? Flag overstatement, lost
   qualifiers ("may", "where feasible", "in low-risk populations"), changed numbers, and
   claims cited that say something else.
2. Unsupported statements. Every clinical statement with no supporting claim, including
   any hidden inside a "framing" block.
3. Drills. For each drill the first option is meant to be the only correct one. Is exactly
   one option correct according to the ledger? Could an expert argue for another option?
   Is any wrong option actually supported by a claim?
4. Safety. Anything that could lead a learner to a harmful action or to false reassurance,
   for example a table that reads as "no referral needed".
5. Wording that could reveal or hint at fetal sex.
6. Mixing of sources. Units D7, D8, D9 and D13 use a screening guideline (IS23 claims) and
   an echocardiography guideline (AS23 claims). Flag any place where an echocardiography
   requirement is presented as a screening requirement.

Output: one numbered list per unit. Each finding has: location (section heading, drill id,
checklist item or video beat number), problem, suggested fix using only ledger claims.
If a category has no findings for a unit, say so. End with the five findings you consider
most important across all units.

Use nothing from memory. If you think a fact is missing from the ledger, say
"MISSING CLAIM" and describe it; do not supply it.
```

Bring back: the full list of findings.

---

## Task C. Harvest the unread part of the ASE guideline

Time: about 20 minutes. Attach: the ASE PDF and `content/ledger/ASE-2023-FETALECHO.yaml`.

```
You are extracting evidence for a medical education project. The attached PDF (ASE 2023
fetal echocardiogram guideline) is the only thing you may use. The attached YAML file holds
22 claims already extracted, numbered AS23-001 to AS23-022; do not repeat them.

Extract further claims, numbered from AS23-023, on these topics only:

a. Indications for fetal echocardiography and the timing of the study.
b. What a complete fetal echocardiogram must show, view by view (required and optional
   elements), including the sagittal arch views and venous connections.
c. Rhythm: normal rate, definitions of bradycardia and tachycardia, how each mechanism is
   recognised, normal atrioventricular interval values if stated.
d. Cardiac function and signs of heart failure or hydrops that the guideline lists.
e. Colour M-mode, and any ultrasound mode discussed after about page 705.
f. Early (first and early second trimester) fetal echocardiography.
g. Reporting, image storage, and quality or training requirements.

Rules:
1. One fact per claim. Paraphrase in plain English; do not copy sentences, tables or figures.
2. Give a locator for each: section heading, table or figure number, and the printed
   journal page number.
3. Keep the document's strength of wording (must / should / may / is recommended).
4. Use nothing from memory. If the document does not say it, it is not a claim.
5. If the document contradicts itself or is ambiguous, say so in `note`.
6. Aim for 60 to 100 claims.

Output YAML only, in one code block, in this shape:

- id: AS23-023
  statement: "..."
  source: ASE-2023-FETALECHO
  locator: "Section '...', Table n, p. nnn"
  status: ai-extracted
  extracted_by: "ChatGPT (your model name, today's date)"
  checked_by: null
  verified_by: null
  note: null
```

Bring back: the YAML. Claude or Gemini will cross-check it against the PDF before use.

---

## How to hand the results back

Paste each result into the Claude chat for this project, or save them in the repository as `tasks/results/task-a.csv`, `tasks/results/task-b.md`, `tasks/results/task-c.yaml`. Claude then:

- runs `python tools/apply_crosscheck.py tasks/results/task-a.csv --by "ChatGPT (model, date)"`,
- fixes the units from the audit findings,
- adds the new claims to the ledger and has them cross-checked,
- rebuilds the editor's review pack so Dr Kunda sees only confirmed claims.

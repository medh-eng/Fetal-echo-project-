# Tasks for Claude Opus or Sonnet

Written 16 Nov 2026 by Claude (Fable) for later sessions. Each task stands alone. Before any of them: read `AGENTS.md`, `README.md` and `docs/log.md`; run `python tools/build.py` before committing; add a line to `docs/log.md`; push to `main`.

Two rules that are easy to break:

- Claude drafted every unit and extracted or reworded claims IS23-001 to 096 and AS23-001 to 022. **No Claude model may cross-check those claims or audit those units.** Claude may cross-check the claims ChatGPT extracted (AS23-023 to 119, IS23-097 to 103).
- Never set a claim to `expert-verified` and never run `tools/signoff.py` unless the project owner states in the chat that Dr Kunda has approved, and which units.

Suggested model is given for each task. "Needs" lists what the project owner must supply first.

---

## 1. Cross-check the 104 claims ChatGPT extracted (Opus)

Needs: both guideline PDFs attached to the chat (links in `tasks/chatgpt-tasks-round2.md`).

1. Run `python tools/task_lists.py`; open `tasks/claims-for-claude-or-gemini.md`.
2. For every claim, find the passage in the PDF at or near the locator. Verdict: CONFIRMED, CORRECT LOCATOR, DISTORTED or NOT FOUND, as defined in `prompts/02-crosscheck.md`. Be strict about numbers, qualifiers and lists. Read the PDF page itself; do not rely on memory.
3. Pay particular attention to the claims with notes: AS23-069, 070, 072, 080, 081, 085, 100.
4. Write `tasks/results/task-f.csv` (`claim_id,verdict,detail`) and apply it: `python tools/apply_crosscheck.py tasks/results/task-f.csv --by "Claude Opus (version, date)"`.
5. For DISTORTED claims: do not reword them yourself and then mark them checked. Leave the dispute note; list them in the log for ChatGPT or Gemini to re-extract.
6. Rebuild. Report how many claims left "held back" in `dist/editor/review-pack.md`.

Done when: the CSV is in the repository, the ledger is updated, the build passes.

## 2. Apply ChatGPT's round-2 results (Sonnet)

Needs: `tasks/results/task-d.csv` and `tasks/results/task-e.md` from ChatGPT.

1. `python tools/apply_crosscheck.py tasks/results/task-d.csv --by "ChatGPT (model, date)"`.
2. Work through every finding in `task-e.md`. Fix the unit text using only ledger claims. Where the fix needs a fact that is not in the ledger, add a line to the unit's `missing_claims`; do not write the fact.
3. Do not weaken a finding because it is inconvenient. If you disagree with one, leave the text as is and record the disagreement in `docs/log.md` for the editor.
4. Rebuild; open `dist/app/index.html` and click through two of the changed units.

## 3. Record the editor's sign-off (Sonnet)

Needs: a statement from the project owner of which units Dr Kunda approved, the date, and any claims she marked "change" or "remove".

1. For "change": edit the claim's statement in the ledger exactly as she wrote it, and set `extracted_by` to record that the wording is hers. For "remove": delete the claim and every sentence that rests only on it.
2. For each approved unit: `python tools/signoff.py <UNIT> --name "Dr Kunda Shahane" --date YYYY-MM-DD --note "..."`, with `--skip` for any claim she did not approve.
3. Record her answers to the decisions in `content/editor/questions.yaml`, apply them to the units, and remove answered questions from that file.
4. `python tools/build.py --release` shows what still blocks a release.

## 4. Sweep trainer: apply the editor's mark-up (Sonnet)

Built on 16 Nov (`tools/templates/sweep.html`, generated into `dist/app/sweep.html`). The five schematics were drawn by Claude and go beyond what the claims state in places: which chamber is anterior, the course of each vessel, the position of the inferior vena cava relative to the aorta. Needs: Dr Kunda's marked-up printout of `dist/editor/sweep-schematics.html`. Change the drawings exactly as she marks them. Do not add lesions until the lesion claims exist (task 12).

## 5. Pilot test page (Sonnet)

Follow `docs/08-pilot-protocol.md`. Add a "Test" page to the app: a fixed set of items, each with a clip slot (use a grey placeholder until clips exist), four questions per item (plane, normal or not, where, how sure), a timer per item, no feedback during the test, and an export of the answers as a CSV with a participant code typed at the start. Two clip sets, A and B. Item definitions live in `content/pilot/set-a.yaml` and `set-b.yaml`; the answer key is filled by the editor later.

## 6. Clips in the app (Sonnet)

Needs: at least one real clip through the anonymiser with two checks (see `tools/clinic/README.md`).

Teach the app to load a `media.json` list that sits beside `index.html` on the hosting server (not in this repository) and to show clip drills: play a few beats, then ask plane, normal or not, and where. Only clips whose details file has two different checkers may be listed. Add a script that builds `media.json` from a folder of anonymiser `.json` files and refuses any with fewer than two checks.

## 7. Anonymiser: real exports (Sonnet)

Needs: the filled `docs/07-clinic-checks.md` and one exported file of each type from the Voluson, made with a dummy patient name. Extend `tools/clinic/anonymise.py` for whatever the form shows is needed (DICOM through `pydicom`, a saved crop preset per screen layout). Never commit an export, even a dummy one.

## 8. New sources (Opus for harvest planning; ChatGPT or Gemini to harvest or check)

Needs: PDFs of the ISUOG fetal echocardiography guideline and the AIUM practice parameter, plus any Indian guidance the editor names.

Add each to `content/sources/sources.yaml` with its licence. One model harvests with `prompts/01-harvest.md` into a new ledger file; a model from a different vendor cross-checks. Then revise F1, F2 and XA5 to cite them and note every point where the guidelines differ.

## 9. Units that still have no draft (Opus)

D12 (talking to parents) and D14 (limited equipment) have no claims in the ledger. Do not draft them from general knowledge. They need a source each, or Dr Kunda's own teaching recorded by the project owner and entered as claims with her as the source. D10 is thin for the same reason; its `missing_claims` lists what to ask her for.

## 10. Publish F1 on the clinic website (Sonnet)

Only after F1 is signed and `python tools/build.py --release` passes for it. Upload `dist/web/F1-...wp-fragment.html` through the WordPress connector as a draft page for the project owner to review; do not publish it yourself.

## 11. Later, larger pieces (Opus to plan, Sonnet to build)

Accounts and subscription payment; certificate; supervisor view; case atlas from the catalogue export. None of these should start before the pilot (task 5) has run.

## 12. Draft the lesion atlas and the Decide units as claims arrive (Opus)

Needs: results of `tasks/chatgpt-tasks-round3.md`, added to the ledger and cross-checked (by Claude, since ChatGPT extracted them; same method as task 1).

1. New ledger files: `content/ledger/AHA-2014-FETALCARDIAC.yaml` and `AHA-2024-ARRHYTHMIA-DRUGS.yaml` (`source:` line, then `claims:`). Lesion claims from ASE go into the existing ASE ledger. Keep the `lesion` and `aspect` fields.
2. One unit per row of `content/plan/units.yaml`, in this order: XB4, XB2, XB3, XB1, XB5, XB6, XB7, XB8, then XA6, XC2, XC3, XC4, Z3, Z1, D12, Z4, Z5. For lesion units use one section per lesion with the nine headings of `prompts/05-harvest-lesion.md`; leave out a heading that has no claim and list it under `missing_claims`.
3. Drug doses: never in unit text or drills until the cardiology co-editor exists and has signed. Put them under `missing_claims` as "dose held back".
4. AHA 2014 is twelve years old. Where ASE 2023 or AHA 2024 says something different, teach the newer one and note the difference.
5. Remove each unit from `content/plan/units.yaml` when its draft exists; the status board then tracks it automatically.

## 13. Lesions in the sweep trainer (Opus)

After task 12 and the editor's mark-up of the normal schematics: add a switch for each lesion whose `views` claims are cross-checked, changing only what those claims describe.

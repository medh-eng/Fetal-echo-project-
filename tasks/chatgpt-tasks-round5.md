# Tasks for ChatGPT or Gemini, round 5 (19 Nov 2026)

## Task J. Fresh check of 54 claims Claude reworded (ChatGPT or Gemini; not Claude)

About 30 minutes. Attach: both guideline PDFs, `tasks/claims-for-recheck-round5.md`, and `prompts/02-crosscheck.md`. These are the claims ChatGPT flagged in round 4 (49 wording, 5 locator). Claude has changed each one to match the review. The original wording is kept in each claim's `note`. Check the new wording and locator against the printed page. Save as `tasks/results/task-j.csv`.

## Task K. Fourteen claims from task H (Gemini only)

The 14 claims in `tasks/results/task-h.csv` were extracted by ChatGPT, reworded by Claude, and re-checked by ChatGPT on 19 Nov. `tools/apply_crosscheck.py` refuses to apply that result, because the checker is the same model family as the extractor (rule 4). Either Gemini repeats the check on the same 14 (attach `tasks/claims-for-claude-or-gemini.md` and both PDFs), or the project owner decides to accept the ChatGPT result and applies it by hand. AS23-089 also needs its locator changed to printed ASE p. 703, per the ChatGPT check.

## Task L. The 112 fetal arrhythmia claims (not Claude's to do yet)

`tasks/results/task-h2.yaml` was extracted by ChatGPT, so Claude or Gemini checks it. On 19 Nov Claude could not do this: the AHA 2024 statement (Circulation 149:e937) was not readable from the session, and the project owner's computer was not connected to fetch the PDF. Secondary reviews must not stand in for the statement, since their dose tables differ. Needs the PDF attached to a Claude session, or Gemini. Check the 14 dose entries first (AH24-067 onward). The two divided-dose entries whose period is missing from the printed Figure 3 should also go to a clinician.

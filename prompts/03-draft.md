# Prompt 3: Draft a unit from verified claims

Paste the unit's ledger file and `content/units/D1-five-views.yaml` as the format example.

---
Write unit [CODE: TITLE] for [TIER] learners as a YAML file in the same structure as the example.

Rules:
1. Every clinical statement must rest on claims from the ledger provided; list their IDs in `claims`.
2. If you need a fact that is not in the ledger, do not write it. Add a line to `missing_claims` describing what is needed.
3. Blocks with no clinical fact are `kind: framing`.
4. Plain, direct English. Short sentences. Write for a clinician reading on a phone between patients.
5. Drills test recognition and decisions, not trivia. One clearly correct option; wrong options must be plausible mistakes. Put the correct option first (the app shuffles).
6. Video beats: one idea each, with the shot that shows it.
7. Set `drafted_by` to your model name and date.

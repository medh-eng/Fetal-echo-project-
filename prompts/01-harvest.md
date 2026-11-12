# Prompt 1: Harvest claims from a source

Attach the source PDF. Fill in the two bracketed fields.

---
You are extracting evidence for a medical education project. The attached document is the only thing you may use.

Unit: [UNIT CODE AND TITLE]
Source ID: [ID FROM content/sources/sources.yaml]

Extract every statement in the document that a learner of this unit needs: recommendations, definitions, normal values, thresholds, criteria for each view, technique advice, and stated limits.

Rules:
1. One fact per claim. Paraphrase in plain English; do not copy sentences.
2. Give a locator for each: section heading, table or figure number, and page.
3. Keep the document's strength of wording (must / should / may / good practice point).
4. Use nothing from memory. If the document does not say it, it is not a claim.
5. If the document contradicts itself or is ambiguous, add a `note`.

Output YAML only, in this shape:

```yaml
- id: [UNIT]-C0xx
  statement: "..."
  source: [SOURCE ID]
  locator: "Section '...', Table n, p. nnn"
  status: ai-extracted
  extracted_by: "[your model name and date]"
  checked_by: null
  verified_by: null
  note: null
```

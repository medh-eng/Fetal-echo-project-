# Prompt 5: Harvest claims for the lesion atlas

Attach the source PDF. Fill in the bracketed fields. One lesion group per chat keeps the output manageable.

---
You are extracting evidence for the lesion atlas of a medical education project. The attached document is the only thing you may use.

Source ID: [ID FROM content/sources/sources.yaml]
Claim prefix and first number: [e.g. AS23-200]
Lesions to cover: [LIST]

For each lesion, extract every statement the document makes under these headings. If the document says nothing under a heading, write nothing for it; do not fill gaps from memory.

1. `definition`: what the lesion is and its spectrum.
2. `views`: what each view shows (four-chamber, outflow tracts, three-vessel, three-vessel-and-trachea, sagittal, short-axis). One claim per view.
3. `doppler`: colour and spectral Doppler findings, and what must be documented.
4. `measure`: measurements the document asks for.
5. `associations`: other cardiac lesions, extracardiac anomalies, genetic conditions.
6. `evolution`: how the lesion can change before birth, and signs of progression.
7. `followup`: timing of repeat studies.
8. `perinatal`: delivery planning and what is needed at birth.
9. `pitfall`: look-alikes and diagnostic traps.

Rules:
1. One fact per claim. Paraphrase in plain English; do not copy sentences, tables or figures.
2. Give a locator for each: section heading, table or figure number, and the printed journal page.
3. Keep the document's strength of wording (must / should / may / is recommended).
4. Give no drug dose, and no number that is not printed in the document.
5. If the document contradicts itself or is ambiguous, say so in `note`.

Output YAML only, in one code block:

```yaml
- id: [PREFIX-NUMBER]
  lesion: "[lesion name]"
  aspect: "[one of the nine headings above]"
  statement: "..."
  source: [SOURCE ID]
  locator: "Section '...', Table n, p. nnn"
  status: ai-extracted
  extracted_by: "[your model name and date]"
  checked_by: null
  verified_by: null
  note: null
```

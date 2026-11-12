# Governance: patients, law, copyright, safety

This is a working checklist prepared without legal training. Take it to a health-law advisor and the ethics committee before the first patient clip is published.

## 1. Patient media

### Consent
- Separate written consent for **educational use and publication** of de-identified images, distinct from consent for the scan.
- Available in Marathi, Hindi and English; explained verbally.
- States: what is kept, what is removed, where it may appear (book, app, video, online), that refusal does not affect care, and how to withdraw.
- Consent register kept at the clinic: case code, date, scope, witness. The register never enters this repository.

### PC-PNDT Act
- Nothing published may disclose fetal sex or allow it to be inferred: no perineal frames, no captions, no file names, no metadata.
- Standard clip set is cardiac and upper-abdominal only.
- Every clip gets an explicit "no sex information" check at review.
- Confirm with the advisor: record-keeping obligations when clinic images are reused for teaching.

### Digital Personal Data Protection Act 2023 and Rules 2025
- The Rules were notified in November 2025 and phase in through May 2027.
- Work on the basis of explicit consent and purpose limitation.
- A research exemption exists; do not assume a teaching product qualifies. Ask the advisor.

### Ethics
- Apply to an ethics committee for a prospective teaching case repository (ICMR national ethical guidelines).

### De-identification procedure
1. Export from the machine to an encrypted drive at the clinic.
2. Assign a random case code. The key linking code to patient stays in the clinic register only.
3. Crop every frame to remove the patient banner and any on-screen text. Check for text burned into the image area.
4. Convert to MP4/WebM; discard original metadata; write a clean JSON sidecar (gestational age in weeks, view, mode, scale, frame rate, labels).
5. Second person reviews: no name, ID, date, institution, operator, or sex information.
6. Only then copy to the project media store. Originals never leave the clinic.

No patient media is ever committed to this Git repository. The repository holds text, code and media *metadata* only.

## 2. Copyright and licensing

- Facts, measurements and equations are restated in our own words with citation.
- No figure, table or passage is copied from a textbook or journal without a licence or written permission. Log every permission in `content/sources/permissions.yaml` (to be created when first needed).
- Open-access material is used only within its licence terms, with attribution.
- Guidelines are cited and paraphrased, not reproduced.
- Decide the project's own licence once the open-or-paid decision is made.

## 3. Software and regulation

- Phase 1–2 tools are educational: checklists, reference tables, simulators, drills on teaching cases.
- No tool accepts a real patient's measurements and returns a diagnosis, probability or management advice until it has been reviewed against the CDSCO medical-device rules, and against FDA/EU rules if offered there.
- Every reference table shows its source, cohort and limits next to the numbers.

## 4. Clinical safety of content

- Every claim has a status; every built page shows the lowest status it contains.
- Public releases contain only `expert-verified` claims.
- Errata log is public. Each correction records what changed, when and who signed.
- Each unit has a review-by date (default 24 months, or on publication of a new guideline).

## 5. Checklist before first publication

- [ ] Legal consultation done; notes filed
- [ ] Ethics approval received
- [ ] Consent form finalised in three languages
- [ ] De-identification procedure tested on one case end-to-end
- [ ] Two-person review recorded for every clip
- [ ] All claims in the unit `expert-verified`
- [ ] Licence chosen; permissions logged

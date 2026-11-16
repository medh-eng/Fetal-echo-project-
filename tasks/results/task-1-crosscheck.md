# Task 1 result: cross-check of the 104 claims extracted by ChatGPT

17 Nov 2026. Checker: Claude (Fable 5.2). Extractor: ChatGPT. Table: `task-1-crosscheck.csv`.

## Result

| Verdict | Claims |
|---|---|
| Confirmed, raised to ai-cross-checked | 88 |
| Reworded to match the source; still ai-extracted until another model re-checks | 12 |
| Not settled; needs a reader who can see the PDF page | 4 |

No claim was found to be wrong in substance. Every page number given by ChatGPT matched where the passage was found, except AS23-023 (pp. 681-682, not p. 680), AS23-089 (p. 702) and AS23-070 (p. 684 only); those locators were corrected.

## How it was done, and its limits

Claude's workspace could not download the PDFs, and no browser was connected. The check was therefore made through a web reader: a second, smaller Claude model was given the publisher's PDF text (ASE: asecho.org copy of JASE 2023;36:679-723; ISUOG: isuog.org copy of UOG 2023;61:788-803) and asked, claim by claim, whether the text supports the statement, on which page, with a short quotation. Claude (Fable) then judged each claim from the quotation and the stated difference.

Controls: 13 deliberately false statements were mixed in among the claims (wrong thresholds, reversed orders, negated recommendations). All 13 were rejected, each with the correct passage.

Limits, stated plainly:
- The reader saw extracted text, not page images. **Figures were not seen**, only their captions.
- **Tables were flattened.** For Table 3 (required or optional, by modality) the column a cell belongs to was inferred from the order of the text, except where the cell itself begins "Required:" or "Optional:". Claims AS23-042, 046, 047, 049, 050, 054, 063 rest on that inference.
- Quotations were limited to 12 words, so a long claim is confirmed on the reader's judgement of the whole passage, with the quotation as a sample.
- This is weaker than a person, or a model, reading the PDF pages directly. The editor's own check of each claim remains the real verification.

## Reworded (12)

| Claim | What differed |
|---|---|
| AS23-023 | the guideline says 'abnormal results on screening ultrasound' and 'is indicated', not 'suspected cardiac disease' and 'requires'; wording found on pp. 681-682, not p. 680 |
| AS23-039 | 'together' is not in the source |
| AS23-041 | the source stresses attention to fetal lie and transducer orientation; 'established orientation' understated it |
| AS23-045 | the Figure 4 caption is about the fetal heart in general, not the four-chamber view only |
| AS23-068 | the source says 'annulus', not 'diameters' |
| AS23-069 | the source text says 'should be measured' and does not say 'diameters'; 'required' rests on Tables 3 and 4 |
| AS23-070 | the range is given as the normal fetal heart rate, not as a 'usual rate for image optimisation' |
| AS23-089 | the list of ascites, effusions and skin oedema is in Table 12 (p. 703) as scoring categories, not in the statement about initial assessment |
| AS23-100 | the p. 718 key point speaks of aortic and ductal arch laterality; 'relative to the trachea' is the wording of the p. 715 key point |
| AS23-106 | Table 8 says 'limited', not 'particularly difficult' |
| IS23-097 | the guideline says 'anatomical structures', not 'cardiac structures' |
| IS23-099 | the guideline says size and position, not size or position |

The old wording is kept in each claim's `note`. Units that cite these claims were changed to match: D2, D3, D4, D6, D9, D10, D11, F2, XA5, XC1.

## Not settled (4)

| Claim | Why |
|---|---|
| AS23-048 | Table 7 lists further pulmonary veins as 'additional views'; whether that column means optional could not be read from the flattened table text. |
| AS23-076 | The Table 9 cell for sinus tachycardia could not be separated from the neighbouring 'long VA' cell in the flattened text; '<200 beats/min' and 'regular' were found. |
| AS23-082 | Table 9 was found to say only that any modality showing atrial and ventricular contraction simultaneously may be used; 'preserved atrioventricular conduction' was not found in the text. Figure 13 could not be seen. |
| AS23-119 | Table 8 lists the soft-tissue index before 10 weeks and the bone index from 10 weeks under a limit for the thermal and mechanical indices; it does not say 'monitored'. The table layout needs reading from the PDF. |

Units still use these four claims with ChatGPT's wording (F1, F2, XA5). They stay held back from the editor.

# Tasks for ChatGPT, round 3: harvest for the Diagnose and Decide tiers

Written 16 Nov 2026. Do round 2 first (`chatgpt-tasks-round2.md`); it unblocks the Detect tier. These tasks open the next two tiers. A new chat for each task. Save each result in `tasks/results/` under the file name given. Everything ChatGPT extracts here will be cross-checked by Claude or Gemini before use.

For every task, paste the whole of `prompts/05-harvest-lesion.md` (tasks G2, H1) or `prompts/01-harvest.md` (the others) and fill in the fields as shown.

## From the ASE 2023 guideline (PDF already used)

| Task | Section of the PDF | Prompt fields | Save as |
|---|---|---|---|
| **G1** | III.F Cardiac Biometry and Table 4; Table 5 if present | Prompt 1. Unit: XA6 Biometry. Source: ASE-2023-FETALECHO. IDs from AS23-150. Every measurement: where, when in the cycle, required or optional. No reference values unless printed | `task-g1.yaml` |
| **G2a** | IV.C Structural heart disease: septal defects, atrioventricular septal defect, complex atrioventricular connections, univentricular hearts | Prompt 5. IDs from AS23-200 | `task-g2a.yaml` |
| **G2b** | IV.C: outflow tract lesions and look-alikes (tetralogy, transposition, double-outlet right ventricle, common trunk) | Prompt 5. IDs from AS23-300 | `task-g2b.yaml` |
| **G2c** | IV.C: progressive lesions, obstructive and regurgitant (aortic and pulmonary stenosis and atresia, hypoplastic left heart, Ebstein anomaly, coarctation) | Prompt 5. IDs from AS23-400 | `task-g2c.yaml` |
| **G2d** | IV.C: arch abnormalities, venous anomalies, heterotaxy and position, and anything in IV.C not covered above | Prompt 5. IDs from AS23-500 | `task-g2d.yaml` |

The section names for G2 are approximate. Between the four chats, cover the whole of section IV.C; if a lesion sits under a different heading, harvest it where it best fits and say so.

## From the AHA 2014 scientific statement

PDF: https://www.ahajournals.org/doi/10.1161/01.cir.0000437597.44550.5d (free to read). It is from 2014: add to each prompt the line "Mark in `note` any statement the document itself calls uncertain or investigational."

| Task | Sections | Prompt fields | Save as |
|---|---|---|---|
| **H1** | Extracardiac and genetic assessment; cardiac function, heart failure and hydrops; cardiomyopathy, tumours; maternal conditions in the indications tables | Prompt 1. Units: XA2, XC2, XC7, XC8, XB9. Source: AHA-2014-FETALCARDIAC. IDs from AH14-001 | `task-h1.yaml` |
| **H2** | Use the **AHA 2024** statement instead (https://www.ahajournals.org/doi/10.1161/CIR.0000000000001206): mechanisms, diagnosis and treatment of each fetal arrhythmia | Prompt 1. Units: XC3, XC4, Z4. Source: AHA-2024-ARRHYTHMIA-DRUGS. IDs from AH24-001. Record drug names and the document's strength of recommendation; put every dose in a separate claim marked `aspect: dose` | `task-h2.yaml` |
| **H3** | Counselling; delivery planning, classification by severity and delivery room care; fetal therapy and catheter intervention | Prompt 1. Units: D12, Z1, Z3, Z5. Source: AHA-2014-FETALCARDIAC. IDs from AH14-300 | `task-h3.yaml` |

## For Gemini (or ChatGPT with search): one source search

**S1.** Paste this:

```
Find the best available source documents for each topic below, for a paid medical
education course. For each topic give up to three candidates, preferring society
guidelines and consensus statements, then open-access reviews. For each candidate give:
full citation, DOI, year, whether it is free to read, and its exact licence (for example
CC BY, CC BY-NC, or copyright with no open licence). Flag CC BY-NC and similar, because a
paid course cannot reuse that material beyond citing facts. Do not summarise the content.

Topics: cardiac embryology and the origin of congenital heart defects; fetal circulation
and the transition at birth; ultrasound and Doppler physics for echocardiography; fetal
cardiac Z-scores and reference ranges; 3D/4D and STIC of the fetal heart; fetal cardiac
MRI; the fetal heart in monochorionic twins (TTTS, TAPS, selective growth restriction,
TRAP); the fetal heart in growth restriction; maternal hyperoxygenation testing; fetal
cardiac intervention (current indications and outcomes); long-term outcomes after surgery
for the major lesions; perinatal palliative care in congenital heart disease; fetal
echocardiography in low-resource settings; ISUOG guidance on fetal echocardiography;
Indian guidance on fetal echocardiography, on prenatal counselling, and on the legal
limits for termination of pregnancy (cite the Act and Rules).
```

Save as `tasks/results/task-s1.md`. Dr Kunda then picks one source per topic.

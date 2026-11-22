# Task K bundle: audit twelve units

Auditor must not be Claude.

## Instructions

Twelve units were drafted by Claude on 21 Nov 2026 only from claims marked
ai-cross-checked. Audit each against the claims it cites, with prompts/04-audit.md.

For every text block, table row, drill and checklist item:
1. Does each sentence rest on the claims it cites? Flag any sentence that adds a fact,
   a number, a direction ("larger", "smaller"), or a strength ("must") the claims do not
   give.
2. Has a qualifier been lost (a "may" that became "is"; "in selected cases"; "when
   present"; a lesion-specific point stated as general)?
3. Drills: is exactly one option correct according to the cited claims? Is any wrong
   option actually defensible?
4. Z3 and Z5 rest mostly on AHA 2014. Flag any sentence that presents a 2014 statement
   as current practice without saying so.
5. Check that each unit's missing_claims list is honest about what was left out.

Output: one short list per unit, then "Units with nothing to fix: ...".
Use nothing from memory. If a fact is missing from the ledger, say MISSING CLAIM.

## Audit prompt (prompts/04-audit.md)

# Prompt 4: Audit a drafted unit

Use a model that did not write the draft. Paste the unit file and its ledger.

---
You are the adversarial reviewer. Assume the draft contains errors.

1. For every block, drill and video beat: does each cited claim actually support the sentence as written? Flag overstatement, lost qualifiers, changed numbers, and claims cited that say something else.
2. List every clinical statement that has no supporting claim.
3. For each drill: is exactly one option correct according to the ledger? Could an expert argue for another option?
4. Flag anything that could mislead a learner into a harmful action or false reassurance.
5. Flag any wording that could reveal or hint at fetal sex.

Output a numbered list of findings, each with: location, problem, suggested fix. If you find nothing in a category, say so.

---
## Unit Z2

### Unit file

```yaml
# Unit Z2. Every text block and drill lists the claim IDs it rests on.
# Built only from claims that are ai-cross-checked (ASE 2023 claims extracted by Claude,
# cross-checked by ChatGPT on 19 Nov 2026). Decide tier: needs the cardiology co-editor
# before release. Intervals are the guideline's suggestions, not fixed rules.

id: Z2
title: "Surveillance plans by lesion"
tier: Decide
version: 0.1
summary: "Who needs a repeat fetal echocardiogram, how often, and what each repeat study must look at, organised by the risk the lesion carries."
drafted_by: "Claude (Opus 5.5, 21 Nov 2026)"
audited_by: null
signed_by: null

objectives:
  - "Say when a normal mid-trimester study needs no follow-up, and when it does."
  - "Group lesions by the risk that drives their follow-up: heart failure, arrhythmia, cyanosis, pulmonary venous obstruction, airway compromise."
  - "For each group, name the suggested interval and the findings to record."
  - "List the measurements that must be repeated at every study for the main progressive lesions."

sections:

  - heading: "Why a plan is needed"
    blocks:
      - text: "Some heart disease that looks mild at first evolves before birth. A repeat study is planned around what could change and what would change care at birth."
        kind: framing
        claims: []
      - text: "An abnormal fetal heart is usually reassessed every 2-8 weeks until about 34-36 weeks. The interval is guided by the lesion and the clinical concerns."
        claims: [AS23-035]
      - text: "Reassessment near term is aimed at the findings that could change care immediately after birth."
        claims: [AS23-036]
      - text: "Serial follow-up is indicated for diagnoses at risk of haemodynamic compromise after birth."
        claims: [AS23-601]

  - heading: "After a normal study"
    blocks:
      - text: "A normal mid-trimester fetal echocardiogram generally needs no follow-up, unless there is concern for a progressive lesion."
        claims: [AS23-037]
      - text: "If a progressive lesion is suspected despite a normal mid-trimester study, repeat assessment is recommended at intervals of up to 2-4 weeks."
        claims: [AS23-038]

  - heading: "Plans by risk group"
    blocks:
      - text: "The guideline's follow-up table groups lesions by the risk they carry. The intervals are suggestions; the cardiology and obstetric providers decide."
        claims: [AS23-605]
      - text: "Suggested follow-up by risk group."
        claims: [AS23-606, AS23-607, AS23-608, AS23-609, AS23-610, AS23-611, AS23-612, AS23-613]
        table:
          columns: ["Risk", "Examples", "Suggested interval", "What to assess"]
          rows:
            - ["Heart failure", "Hypoplastic left heart with mitral regurgitation; tetralogy with absent pulmonary valve; Ebstein anomaly; AVSD with valve regurgitation; cardiac tumours", "Every 2-4 weeks", "Comprehensive function assessment"]
            - ["Arrhythmia", "Long-QT syndrome; congenitally corrected transposition; left atrial isomerism", "Every 2-4 weeks", "Rate and rhythm"]
            - ["Atrioventricular block", "Congenitally corrected transposition; left atrial isomerism; others", "Every 2-4 weeks", "Atrioventricular interval; atrial and ventricular rates; hydrops; extracardiac Doppler"]
            - ["Tachycardia", "Atrial flutter; supraventricular tachycardia", "Every 2 weeks unless well controlled", "Rate and rhythm; heart size; hydrops and heart failure"]
            - ["Extracardiac cause of hydrops", "CPAM; sacrococcygeal teratoma; twin-twin transfusion; arteriovenous malformation; TRAP sequence; fetal anaemia", "Every 2-4 weeks", "Comprehensive function assessment"]
            - ["Cyanosis after birth", "Transposition with intact septum or VSD; DORV with subpulmonary VSD; tetralogy", "Every 4-8 weeks and late in the third trimester", "Atrial septal excursion; foramen opening; ductal shunting; consider maternal hyperoxygenation testing"]
            - ["Pulmonary venous obstruction after birth", "Hypoplastic left heart with restrictive atrial septum; obstructed anomalous pulmonary venous return; cor triatriatum", "Every 4-8 weeks and late in the third trimester", "Pulmonary venous forward-to-reverse ratio; atrial septal position and thickness; vertical vein Doppler; consider maternal hyperoxygenation testing"]
            - ["Respiratory compromise after birth", "Tetralogy with absent pulmonary valve; Ebstein anomaly; hypoplastic left heart with restrictive atrial septum", "Every 4-8 weeks and late in the third trimester", "Mediastinal shift; cardiothoracic area ratio; ventricular function; consider fetal MRI of the lungs"]
      - text: "After fetal intervention, follow-up is every 4 weeks in the third trimester. After intervention for aortic stenosis with evolving hypoplastic left heart: aortic outflow, arch flow direction, atrial septal flow, left ventricular size and function, mitral regurgitation and endocardial brightness. After intervention for hypoplastic left heart with a restrictive atrial septum: patency of the atrial communication and the pulmonary venous forward-to-reverse ratio."
        claims: [AS23-614, AS23-615]

  - heading: "What every repeat study must record, lesion by lesion"
    blocks:
      - text: "Semilunar valve stenosis: serial evaluation, including ventricular size and function and endocardial fibroelastosis."
        claims: [AS23-408]
      - text: "Semilunar valve stenosis: flow direction in the ductal and aortic arches at every examination, because abnormal direction heralds critical obstruction after birth; and flow direction at the atrial septum at every examination."
        claims: [AS23-409, AS23-410]
      - text: "Atrioventricular valve abnormality: a complete Doppler assessment at each examination, including valve stenosis and regurgitation and flow at the atrial septum and ductus."
        claims: [AS23-246]
      - text: "Valve regurgitation: follow serially, because it may worsen as pregnancy advances; progressive cardiomegaly is common when it is significant."
        claims: [AS23-440, AS23-441]
      - text: "Severe tricuspid disease with pulmonary atresia, structural or functional: ductal flow direction documented serially, because retrograde ductal flow can develop at any point."
        claims: [AS23-429]
      - text: "Hypoplastic left heart syndrome: the pulmonary venous forward-to-reverse velocity-time integral ratio at every study, with the last measurement near term. Maternal hyperoxygenation testing late in the third trimester may be considered in selected cases."
        claims: [AS23-220, AS23-223]
      - text: "D-transposition: the foramen ovale assessed late in gestation in every fetus."
        claims: [AS23-330]
      - text: "Congenitally corrected transposition: serial studies offered, to find progressive atrioventricular valve regurgitation and rhythm problems, including complete heart block."
        claims: [AS23-339]
      - text: "Tetralogy of Fallot: ductal flow direction at 28 weeks predicts the need for neonatal intervention."
        claims: [AS23-316]

  - heading: "From surveillance to the delivery plan"
    blocks:
      - text: "Certain critical lesions need cardiac intervention immediately after birth. A coordinated perinatal plan of care has the greatest potential to influence outcome."
        claims: [AS23-602, AS23-604]
      - text: "Once heart disease is diagnosed, maternal, fetal and neonatal providers must work together on its implications, the follow-up visits and the level of neonatal care expected. Image-based risk stratification paired with level-of-care plans is recommended. Unit Z3 covers the delivery plan."
        claims: [AS23-600, AS23-603]

missing_claims:
  - "AS23-039 (follow-up interval decided by the fetal cardiology and obstetric teams) is not yet cross-checked; the same point is made here through AS23-605."
  - "Follow-up plans for lesions not named in Table 15 (for example isolated ventricular septal defect, coarctation suspected on arch discrepancy) - need a source and the co-editor."
  - "How surveillance should be adapted where the patient lives far from a fetal cardiology centre (Indian practice) - the editor's input."
  - "Video outline not yet written."

drills:
  - id: Z2-Q01
    question: "A mid-trimester fetal echocardiogram is normal and there is no concern for a progressive lesion. What follow-up does the guideline suggest?"
    options:
      - "Generally none"
      - "Every 2-4 weeks until delivery"
      - "One repeat study at 28 weeks for everyone"
      - "A repeat study near term in every case"
    answer: 0
    explanation: "A normal mid-trimester study generally needs no follow-up unless a progressive lesion is a concern."
    claims: [AS23-037]

  - id: Z2-Q02
    question: "Why is the near-term study done in an abnormal heart?"
    options:
      - "To look for findings that could change care immediately after birth"
      - "To confirm the diagnosis made at mid-trimester, as a routine"
      - "To decide whether the pregnancy should continue"
      - "Only to measure fetal growth"
    answer: 0
    explanation: "Near-term reassessment is targeted to findings that could change care immediately after birth."
    claims: [AS23-036]

  - id: Z2-Q03
    question: "A fetus has Ebstein anomaly. Which risk group and suggested interval apply?"
    options:
      - "Heart failure: every 2-4 weeks with comprehensive function assessment"
      - "Cyanosis: every 4-8 weeks with atrial septal assessment only"
      - "No follow-up until birth"
      - "Tachycardia: every 2 weeks with rhythm only"
    answer: 0
    explanation: "Ebstein anomaly is one of the examples at risk of heart failure, followed every 2-4 weeks with comprehensive function assessment. It also appears in the respiratory-compromise group."
    claims: [AS23-606, AS23-612]

  - id: Z2-Q04
    question: "D-transposition with intact ventricular septum. What must be assessed late in gestation?"
    options:
      - "The foramen ovale"
      - "The ductus venosus only"
      - "Nuchal translucency"
      - "Nothing; transposition does not change before birth"
    answer: 0
    explanation: "Every fetus with D-transposition should have the foramen ovale assessed late in gestation. The cyanosis group also includes atrial septal excursion and ductal shunting."
    claims: [AS23-330, AS23-609]

  - id: Z2-Q05
    question: "Fetal aortic stenosis is being followed. What must be documented at every study?"
    options:
      - "Flow direction in the ductal and aortic arches, and at the atrial septum"
      - "Only the peak aortic velocity"
      - "Only the cardiac axis"
      - "Flow direction at the first study only"
    answer: 0
    explanation: "With semilunar stenosis, arch flow direction and atrial septal flow direction must be documented at every examination. Abnormal arch flow heralds critical obstruction after birth."
    claims: [AS23-409, AS23-410]

  - id: Z2-Q06
    question: "Hypoplastic left heart syndrome. Which measurement is repeated at every study, with the last one near term?"
    options:
      - "The pulmonary venous forward-to-reverse velocity-time integral ratio"
      - "The cardiac axis"
      - "The umbilical artery pulsatility index only"
      - "The nuchal translucency"
    answer: 0
    explanation: "In HLHS the pulmonary venous forward-to-reverse VTI ratio should be measured at every study, the last near term."
    claims: [AS23-220]

  - id: Z2-Q07
    question: "Fetal supraventricular tachycardia that is not yet controlled. What interval does the follow-up table suggest?"
    options:
      - "Every 2 weeks"
      - "Every 4-8 weeks"
      - "Only near term"
      - "No follow-up is needed"
    answer: 0
    explanation: "Tachycardia is followed every 2 weeks unless well controlled, assessing rate and rhythm, heart size, hydrops and heart failure."
    claims: [AS23-611]

  - id: Z2-Q08
    question: "Congenitally corrected transposition. What are serial studies looking for?"
    options:
      - "Progressive atrioventricular valve regurgitation and rhythm problems, including complete heart block"
      - "Closure of the ductus venosus"
      - "Growth of the aortic arch only"
      - "Nothing; serial studies are not offered"
    answer: 0
    explanation: "Serial studies are offered to find progressive atrioventricular valve regurgitation and rhythm abnormalities, including complete heart block."
    claims: [AS23-339]

  - id: Z2-Q09
    question: "Tetralogy of Fallot. Which finding at 28 weeks predicts the need for neonatal intervention?"
    options:
      - "Ductal flow direction"
      - "Fetal heart rate"
      - "Size of the left atrium"
      - "Presence of an echogenic focus"
    answer: 0
    explanation: "In tetralogy, ductal direction at 28 weeks predicts the need for neonatal intervention."
    claims: [AS23-316]

  - id: Z2-Q10
    question: "Are the intervals in the guideline's follow-up table fixed rules?"
    options:
      - "No: they are suggestions, at the discretion of the cardiology and obstetric providers"
      - "Yes: they must be followed exactly"
      - "Yes, for heart failure only"
      - "They apply only after fetal intervention"
    answer: 0
    explanation: "The intervals are suggestions; the cardiology and obstetric providers decide."
    claims: [AS23-605]

checklist:
  title: "Planning surveillance"
  items:
    - text: "Risk group named: heart failure, arrhythmia or block, tachycardia, cyanosis, pulmonary venous obstruction, respiratory compromise"
      claims: [AS23-606, AS23-607, AS23-609, AS23-610, AS23-611, AS23-612, AS23-613]
    - text: "Suggested interval chosen and agreed with the obstetric team"
      claims: [AS23-605]
    - text: "Measurements to repeat at each study listed in the report"
      claims: [AS23-246, AS23-409, AS23-410, AS23-220]
    - text: "Near-term study planned for findings that could change care at birth"
      claims: [AS23-036]
    - text: "Delivery-planning discussion started with maternal, fetal and neonatal providers"
      claims: [AS23-600]
```

### Claims cited (with ledger statement and locator)

| id | status | statement | locator |
|---|---|---|---|
| AS23-035 | expert-verified | An abnormal fetal heart is usually reassessed every 2–8 weeks until about 34–36 weeks, with the interval guided by the lesion and clinical concerns. | III.A. Timing of Examination, Equipment, and Image Storage, Timing, p. 682 |
| AS23-036 | expert-verified | Near-term reassessment is targeted to findings that could change care immediately after birth. | III.A. Timing of Examination, Equipment, and Image Storage, Timing, p. 682 |
| AS23-037 | expert-verified | A normal midtrimester fetal echocardiogram generally needs no follow-up unless there is concern for a progressive lesion. | III.A. Timing of Examination, Equipment, and Image Storage, Timing, p. 682 |
| AS23-038 | expert-verified | When a progressive lesion is suspected despite a normal midtrimester echocardiogram, repeat assessment is recommended at intervals of up to 2–4 weeks. | III.A. Timing of Examination, Equipment, and Image Storage, Timing, p. 682 |
| AS23-039 | ai-extracted | The follow-up interval should be decided by the fetal cardiology and obstetric teams caring for the patient. | III.A. Timing of Examination, Equipment, and Image Storage, Timing, p. 682 |
| AS23-220 | ai-cross-checked | In hypoplastic left heart syndrome, the pulmonary venous forward-to-reverse velocity-time integral ratio should be measured at every fetal echocardiogram, the last measurement near term. | IV.C.i Key Points, p. 704 |
| AS23-223 | ai-cross-checked | Maternal hyperoxygenation testing late in the third trimester may be considered in selected cases of hypoplastic left heart syndrome. | IV.C.i Key Points, p. 704 |
| AS23-246 | ai-cross-checked | At each examination with an atrioventricular valve abnormality, a complete Doppler assessment must be done, including valve stenosis and regurgitation and flow at the atrial septum and ductus. | IV.C.ii Key Points, p. 713 |
| AS23-316 | ai-cross-checked | In tetralogy of Fallot, ductal direction at 28 weeks predicts the need for neonatal intervention. | Table 13 (lesion-specific evaluation), p. 707 |
| AS23-330 | ai-cross-checked | Any fetus with D-transposition should have the patency of the foramen ovale assessed late in gestation. | IV.C.iii Key Points, p. 715 |
| AS23-339 | ai-cross-checked | Serial fetal echocardiography should be offered in congenitally corrected transposition to identify progressive atrioventricular valve regurgitation and rhythm abnormalities, including complete heart block. | IV.C.iii Key Points, p. 715 |
| AS23-408 | ai-cross-checked | Serial evaluation should be performed when valve stenosis is suspected, including ventricular size and function and endocardial fibroelastosis. | IV.C.iv Key Points (semilunar obstruction), p. 716 |
| AS23-409 | ai-cross-checked | Ductal and aortic arch flow direction must be documented at every examination; abnormal direction heralds critical obstruction after birth. | IV.C.iv Key Points (semilunar obstruction), p. 716 |
| AS23-410 | ai-cross-checked | Atrial septal flow direction must be documented at every examination when semilunar valve stenosis is present. | IV.C.iv Key Points (semilunar obstruction), p. 716 |
| AS23-429 | ai-cross-checked | Structural or functional pulmonary atresia in severe tricuspid disease is always associated with retrograde ductal flow, which can develop at any point and must be documented serially. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-440 | ai-cross-checked | Valve regurgitation should be followed serially, because it may worsen with advancing gestation. | IV.C.iv Key Points (regurgitation), p. 717 |
| AS23-441 | ai-cross-checked | Progressive cardiomegaly is common with significant atrioventricular or semilunar regurgitation. | IV.C.iv Key Points (regurgitation), p. 717 |
| AS23-600 | ai-cross-checked | Once fetal heart disease is diagnosed, maternal, fetal and neonatal providers must work together on its implications, follow-up visits and the expected level of neonatal care. | IV.D Key Points, p. 718; IV.D Imaging-Based Risk Assessment and Delivery Planning, p. 718 |
| AS23-601 | ai-cross-checked | Serial follow-up is indicated for diagnoses at risk of haemodynamic compromise after birth; Tables 14 and 15 list the situations. | IV.D Key Points, p. 718; IV.D Imaging-Based Risk Assessment and Delivery Planning, p. 718 |
| AS23-602 | ai-cross-checked | Certain forms of critical heart disease require cardiac intervention immediately after birth. | IV.D Imaging-Based Risk Assessment and Delivery Planning, p. 718 |
| AS23-603 | ai-cross-checked | Image-based risk stratification paired with level-of-care plans is recommended for prenatally diagnosed heart disease, and may standardise communication and perinatal management. | IV.D Key Points, p. 718; IV.D Imaging-Based Risk Assessment and Delivery Planning, p. 718 |
| AS23-604 | ai-cross-checked | A coordinated perinatal plan of care has the greatest potential to influence outcome. | IV.D Imaging-Based Risk Assessment and Delivery Planning, p. 718 |
| AS23-605 | ai-cross-checked | Follow-up intervals in Table 15 are suggestions, at the discretion of the cardiology and obstetric providers. | Table 15 (follow-up imaging for specific CHD diagnoses), p. 719 (column header) |
| AS23-606 | ai-cross-checked | Fetal heart disease at risk of heart failure (examples: hypoplastic left heart with mitral regurgitation, tetralogy with absent pulmonary valve, Ebstein anomaly, atrioventricular septal defect with valve regurgitation, cardiac tumours) is followed every 2-4 weeks with comprehensive function assessment. | Table 15 (follow-up imaging for specific CHD diagnoses), p. 719 |
| AS23-607 | ai-cross-checked | Fetal heart disease at risk of arrhythmia (examples: long-QT syndrome, congenitally corrected transposition, left atrial isomerism) is followed every 2-4 weeks with documentation of rate and rhythm. | Table 15 (follow-up imaging for specific CHD diagnoses), p. 719 |
| AS23-608 | ai-cross-checked | An extracardiac anomaly at risk of hydrops (examples: CPAM, sacrococcygeal teratoma, twin-twin transfusion, arteriovenous malformation, TRAP sequence, fetal anaemia) is followed every 2-4 weeks with comprehensive function assessment. | Table 15 (follow-up imaging for specific CHD diagnoses), p. 719 |
| AS23-609 | ai-cross-checked | A fetus at risk of cyanosis after birth (examples: transposition with intact septum or ventricular septal defect, double-outlet right ventricle with subpulmonary defect, tetralogy) is followed every 4-8 weeks and late in the third trimester, assessing atrial septal excursion, foramen opening and ductal shunting, with maternal hyperoxygenation testing considered. | Table 15 (follow-up imaging for specific CHD diagnoses), p. 719 |
| AS23-610 | ai-cross-checked | A fetus at risk of pulmonary venous obstruction after birth (examples: hypoplastic left heart with restrictive atrial septum, obstructed anomalous pulmonary venous return, cor triatriatum) is followed every 4-8 weeks and late in the third trimester, assessing the pulmonary venous forward-to-reverse ratio, atrial septal position and thickness, vertical vein Doppler, with maternal hyperoxygenation testing considered. | Table 15 (follow-up imaging for specific CHD diagnoses), p. 719 |
| AS23-611 | ai-cross-checked | Fetal tachycardia (atrial flutter, supraventricular tachycardia) is followed every 2 weeks unless well controlled, assessing rate and rhythm, heart size, hydrops and heart failure. | Table 15 (follow-up imaging for specific CHD diagnoses), p. 719 |
| AS23-612 | ai-cross-checked | A fetus at risk of respiratory compromise after birth (examples: tetralogy with absent pulmonary valve, Ebstein anomaly, hypoplastic left heart with restrictive atrial septum) is followed every 4-8 weeks and late in the third trimester, assessing mediastinal shift, cardiothoracic area ratio and ventricular function, with fetal MRI of the lungs considered. | Table 15 (follow-up imaging for specific CHD diagnoses), p. 719 |
| AS23-613 | ai-cross-checked | A fetus at risk of atrioventricular block (congenitally corrected transposition, left atrial isomerism, others) is followed every 2-4 weeks, assessing the atrioventricular interval, atrial and ventricular rates, hydrops and extracardiac Doppler. | Table 15 (follow-up imaging for specific CHD diagnoses), p. 719 |
| AS23-614 | ai-cross-checked | After fetal intervention for aortic stenosis with evolving hypoplastic left heart, follow-up is every 4 weeks in the third trimester, assessing aortic outflow, arch flow direction, atrial septal flow, left ventricular size and function, mitral regurgitation and endocardial brightness. | Table 15 (follow-up imaging for specific CHD diagnoses), p. 719 |
| AS23-615 | ai-cross-checked | After fetal intervention for hypoplastic left heart with restrictive atrial septum, follow-up is every 4 weeks in the third trimester, assessing patency of the atrial communication and the pulmonary venous forward-to-reverse ratio. | Table 15 (follow-up imaging for specific CHD diagnoses), p. 719 |

---
## Unit XB4

### Unit file

```yaml
# Unit XB4. Every text block and drill lists the claim IDs it rests on.
# Built only from ai-cross-checked claims (ASE 2023, extracted by Claude, cross-checked by
# ChatGPT on 19 Nov 2026). Claims reworded on 21 Nov and awaiting re-check are left out and
# listed under missing_claims. Diagnose tier: needs the cardiology co-editor before release.
# One section per lesion; each block starts with the aspect it covers.

id: XB4
title: "Lesion atlas: conotruncal lesions (tetralogy, transposition, DORV, common trunk)"
tier: Diagnose
version: 0.1
summary: "How outflow tract lesions are found when the four-chamber view looks normal, and, lesion by lesion, what to image, measure, look for and plan."
drafted_by: "Claude (Opus 5.5, 21 Nov 2026)"
audited_by: null
signed_by: null

objectives:
  - "Explain why outflow tract lesions are missed on the four-chamber view and which views find them."
  - "Give the differential diagnosis of a ventricular septal defect with an overriding vessel."
  - "For tetralogy, absent pulmonary valve, DORV, common trunk, D-transposition and congenitally corrected transposition: name the key findings, measurements, associations and perinatal points."
  - "Name the conotruncal findings that change delivery planning."

sections:

  - heading: "Finding outflow lesions"
    blocks:
      - text: "Outflow tract lesions are found at screening with the outflow, three-vessel and three-vessel-and-trachea views. They often show little abnormality on the four-chamber view."
        claims: [AS23-300]
      - text: "When the four-chamber view is normal, Table 13 of the guideline lists three clues: an abnormal cardiac axis (below 30° or above 60°), a left ventricular outflow view that is abnormal or cannot be obtained, and an abnormal three-vessel view."
        claims: [AS23-352]
      - text: "Sweeps from the four-chamber view through the outflow, three-vessel and three-vessel-and-trachea views detail the segmental anatomy. Short-axis and coronal views help locate the ventricular septal defect and show how the great arteries relate."
        claims: [AS23-301, AS23-302]
      - text: "Outflow lesions are often associated with anomalies of the veins, atrioventricular valves, septum, branch pulmonary arteries and arch. A complete evaluation includes the branch pulmonary arteries at their origins."
        claims: [AS23-303, AS23-306]
      - text: "The aortic arch is at risk in any lesion with subaortic obstruction or a subpulmonary ventricular septal defect. Image it with two-dimensional and Doppler imaging in axial and sagittal planes."
        claims: [AS23-308]
      - text: "Pitfall: a ventricular septal defect with an overriding great vessel has a differential diagnosis - tetralogy of Fallot, pulmonary atresia with ventricular septal defect, double-outlet right ventricle and common arterial trunk."
        claims: [AS23-304]

  - heading: "Tetralogy of Fallot"
    blocks:
      - text: "Definition: an overriding aorta with obstruction below or at the pulmonary valve that ranges from mild stenosis to atresia, or a dilated outflow with absent pulmonary valve."
        claims: [AS23-309]
      - text: "Views: the branch pulmonary arteries must be identified at their origins. Discontinuity, segmental stenosis and major aortopulmonary collaterals can coexist with an outflow or ductus that looks patent."
        claims: [AS23-311]
      - text: "Measure: the branch pulmonary arteries, the pulmonary valve annulus serially, and the infundibulum."
        claims: [AS23-315]
      - text: "Associations: atrioventricular septal defect; bilateral superior venae cavae, a retroaortic innominate vein, right aortic arch, vascular rings and aortopulmonary window. Imaging the arch and the thymus allows counselling tailored to the risk of 22q11 deletion."
        claims: [AS23-312, AS23-314, AS23-313]
      - text: "Perinatal: ductal flow direction at 28 weeks predicts the need for neonatal intervention."
        claims: [AS23-316]

  - heading: "Absent pulmonary valve syndrome"
    blocks:
      - text: "Definition and associations: most often with tetralogy and a subaortic ventricular septal defect, but it can occur with an intact ventricular septum. Telling these apart is critical for surgical planning and for assessing 22q11.2 deletion."
        claims: [AS23-317, AS23-318]
      - text: "Views: a hypoplastic pulmonary annulus with tiny leaflets and to-and-fro colour flow across the valve. Key findings: dilated main and branch pulmonary arteries, and an enlarged right atrium and ventricle."
        claims: [AS23-319, AS23-320]
      - text: "Doppler: the ductus is typically absent, but look for it, because its presence affects prognosis."
        claims: [AS23-321]
      - text: "Evolution: progressive right ventricular dysfunction predicts perinatal death; left ventricular dysfunction independently predicts fetal death."
        claims: [AS23-323]
      - text: "Pitfall and perinatal: note the side of the arch, because an aneurysmal branch pulmonary artery on the same side may compress the airway. An abnormal cardiac position from segmental fluid trapping in the lung may signal airway obstruction after birth and can predict outcome. Fetal MRI may be useful to measure lung volumes or fluid trapping."
        claims: [AS23-322, AS23-324, AS23-325]

  - heading: "Double-outlet right ventricle"
    blocks:
      - text: "Definition: the ventricular septal defect may be subaortic, subpulmonary, doubly committed or remote. Its position and the relative sizes of aorta and pulmonary artery must be determined."
        claims: [AS23-340]
      - text: "Measure: the relationship of the defect to the great vessels and the pathway from left ventricle to aorta - the defect's size and any atrioventricular valve attachments that could prevent a biventricular repair."
        claims: [AS23-286]
      - text: "Subaortic defect: may resemble tetralogy in anatomy and in physiology after birth."
        claims: [AS23-341]
      - text: "Subpulmonary defect (Taussig-Bing): a posterior vessel gives rise to the pulmonary artery over the defect, with an anterior aorta. The anterior aorta may be obstructed below the valve and coarctation often accompanies it, so image the arch carefully in two dimensions and colour."
        claims: [AS23-343, AS23-342]
      - text: "Perinatal: with a subpulmonary defect and a straddling mitral valve, a neonatal Damus-Kaye-Stansel operation may be more feasible than an arterial switch."
        claims: [AS23-344]

  - heading: "Common arterial trunk"
    blocks:
      - text: "Definition: a single arterial trunk gives rise directly to the coronary arteries, the aorta and one or both pulmonary arteries. The spectrum runs from pulmonary-dominant forms (smaller aortic part, with or without arch interruption) to aortic-dominant forms."
        claims: [AS23-345, AS23-346]
      - text: "Views: the ductus is often absent, but one may be present in any form."
        claims: [AS23-348]
      - text: "Measure: truncal valve velocity and regurgitation, and the proximal branch pulmonary arteries."
        claims: [AS23-351]
      - text: "Evolution: truncal valve function, especially significant regurgitation, can affect survival in utero."
        claims: [AS23-347]
      - text: "Associations: with a right aortic arch the risk of 22q11 deletion is above 50%."
        claims: [AS23-350]

  - heading: "D-transposition of the great arteries"
    blocks:
      - text: "Pitfall: a posterior pulmonary artery arising from the left ventricular outflow is seen in both D-transposition and congenitally corrected transposition."
        claims: [AS23-328]
      - text: "Measure: the size of the foramen ovale, best defined in the sagittal view; a septal excursion index is an additional measurement."
        claims: [AS23-331]
      - text: "Follow-up and perinatal: every fetus with D-transposition should have the foramen ovale assessed late in gestation, and delivery planned where the atrial communication can be enlarged if shunting is inadequate."
        claims: [AS23-330, AS23-329]
      - text: "Evolution: constriction of the ductus can be lethal in critical heart disease, and transposition is at higher risk."
        claims: [AS23-332]
      - text: "Limits: it is still hard to predict which fetuses with a restrictive atrial septum will need intervention immediately after birth; maternal hyperoxygenation testing has been studied but the data are incomplete."
        claims: [AS23-333]

  - heading: "Congenitally corrected transposition"
    blocks:
      - text: "Definition: atrioventricular and ventriculoarterial discordance together give physiologically corrected flow."
        claims: [AS23-334]
      - text: "Associations: a ventricular septal defect may be present in 60% to 70%, of variable type and site. Tricuspid valve dysplasia, Ebstein malformation and coarctation can occur with it."
        claims: [AS23-336, AS23-337]
      - text: "Views and measure: tricuspid displacement and regurgitation are common and affect prognosis; measure atrioventricular intervals and assess the ventricular septal defect."
        claims: [AS23-354]
      - text: "Evolution and follow-up: rhythm problems, including congenital heart block, can arise before birth and affect survival. Serial studies should be offered to find progressive atrioventricular valve regurgitation and rhythm abnormalities."
        claims: [AS23-338, AS23-339]

missing_claims:
  - "Awaiting re-check after rewording on 21 Nov (round 5, task J), so not used here: key observations for tetralogy (AS23-310) and D-transposition (AS23-326); early branching identifies the pulmonary artery (AS23-327); four-chamber clues to corrected transposition (AS23-335); ductal dependence in common trunk (AS23-349); bicuspid pulmonary valve in D-transposition (AS23-360); counselling only after fetal echocardiography (AS23-305); arch sidedness and branching (AS23-307)."
  - "Aortic-to-pulmonary valve ratio and pulmonary valve Z-score as predictors in tetralogy (AS23-353): the checker asks the editor to reconcile the ratio's direction with the reference the guideline cites before it is taught."
  - "Cardiac axis: Table 13 gives below 30° or above 60° (AS23-352), while Table 3 gives a different normal range - flagged for the editor on 17 Nov; the co-editor to decide which the course teaches."
  - "Pulmonary atresia with ventricular septal defect: definition, views and collateral assessment - not in the claims held beyond its place in the differential."
  - "Delivery planning by lesion (place, timing, what is needed at birth) - unit Z3."
  - "Video outline not yet written."

drills:
  - id: XB4-Q01
    question: "The four-chamber view is normal. Which views find most outflow tract lesions at screening?"
    options:
      - "Outflow, three-vessel and three-vessel-and-trachea views"
      - "Four-chamber view at a different angle"
      - "Abdominal situs view"
      - "Ductus venosus Doppler"
    answer: 0
    explanation: "Outflow lesions are found with the outflow, three-vessel and three-vessel-and-trachea views and often show little on the four-chamber view."
    claims: [AS23-300]

  - id: XB4-Q02
    question: "You see a ventricular septal defect with an overriding great vessel. Which list is the differential the guideline gives?"
    options:
      - "Tetralogy of Fallot, pulmonary atresia with VSD, double-outlet right ventricle, common arterial trunk"
      - "Tetralogy only"
      - "D-transposition and corrected transposition"
      - "Coarctation and interrupted arch"
    answer: 0
    explanation: "These four make up the differential of a VSD with an overriding vessel."
    claims: [AS23-304]

  - id: XB4-Q03
    question: "Tetralogy of Fallot: the outflow and duct look patent. Why still image the branch pulmonary arteries at their origins?"
    options:
      - "Discontinuity, segmental stenosis and major aortopulmonary collaterals can coexist with a patent-looking outflow"
      - "Because the branches are always absent in tetralogy"
      - "Only to measure the heart rate"
      - "It is not needed when the outflow looks patent"
    answer: 0
    explanation: "The branch pulmonary arteries must be identified at their origins for exactly this reason."
    claims: [AS23-311]

  - id: XB4-Q04
    question: "Tetralogy of Fallot. Why image the arch and the thymus?"
    options:
      - "To tailor counselling to the risk of 22q11 deletion"
      - "To measure the cardiac axis"
      - "To predict heart block"
      - "To estimate gestational age"
    answer: 0
    explanation: "Imaging the arch and the thymus allows counselling tailored to the risk of 22q11 deletion."
    claims: [AS23-313]

  - id: XB4-Q05
    question: "Absent pulmonary valve syndrome. Which pair of findings fits?"
    options:
      - "Hypoplastic annulus with to-and-fro flow; dilated main and branch pulmonary arteries"
      - "Large annulus with forward flow only; small pulmonary arteries"
      - "Normal pulmonary valve; dilated aorta"
      - "Absent tricuspid valve; small right ventricle"
    answer: 0
    explanation: "APVS shows a hypoplastic annulus with tiny leaflets and to-and-fro flow, and dilated main and branch pulmonary arteries with an enlarged right heart."
    claims: [AS23-319, AS23-320]

  - id: XB4-Q06
    question: "Tetralogy with absent pulmonary valve. Why does the side of the aortic arch matter?"
    options:
      - "An aneurysmal branch pulmonary artery on the same side may compress the airway"
      - "It decides the mode of delivery"
      - "It predicts heart block"
      - "It does not matter in this lesion"
    answer: 0
    explanation: "Arch position matters because an aneurysmal ipsilateral branch pulmonary artery may compress the airway."
    claims: [AS23-322]

  - id: XB4-Q07
    question: "Double-outlet right ventricle with a subpulmonary defect. What else must be imaged carefully, and why?"
    options:
      - "The aortic arch, because subaortic obstruction and coarctation often accompany it"
      - "The ductus venosus, because it is often absent"
      - "The pulmonary veins, because they are always anomalous"
      - "Nothing else; the defect is the whole lesion"
    answer: 0
    explanation: "The anterior aorta may be obstructed below the valve and coarctation often accompanies it, so the arch needs careful 2D and colour imaging."
    claims: [AS23-342, AS23-308]

  - id: XB4-Q08
    question: "Common arterial trunk with a right aortic arch. What is the stated risk of 22q11 deletion?"
    options:
      - "Above 50%"
      - "Below 5%"
      - "No association"
      - "Exactly the same as with a left arch"
    answer: 0
    explanation: "In common arterial trunk a right aortic arch is associated with a 22q11 deletion risk above 50%."
    claims: [AS23-350]

  - id: XB4-Q09
    question: "Common arterial trunk. Which valve finding can affect survival before birth?"
    options:
      - "Significant truncal valve regurgitation"
      - "A bicuspid aortic valve"
      - "Mild tricuspid regurgitation"
      - "None; the trunk is well tolerated in every case"
    answer: 0
    explanation: "Truncal valve function, especially significant regurgitation, can affect survival in utero."
    claims: [AS23-347]

  - id: XB4-Q10
    question: "D-transposition is diagnosed at 22 weeks. What must be assessed late in gestation?"
    options:
      - "Patency of the foramen ovale"
      - "Nuchal translucency"
      - "Pulmonary valve annulus serially"
      - "Nothing more; transposition is fixed"
    answer: 0
    explanation: "Every fetus with D-transposition should have the foramen ovale assessed late in gestation, with delivery where the atrial communication can be enlarged."
    claims: [AS23-330, AS23-329]

  - id: XB4-Q11
    question: "A posterior pulmonary artery arises from the left ventricular outflow. Does this alone tell you it is D-transposition?"
    options:
      - "No: corrected transposition shows the same appearance"
      - "Yes: it only occurs in D-transposition"
      - "Yes, if the heart rate is normal"
      - "No: it is a normal variant"
    answer: 0
    explanation: "Both D-transposition and congenitally corrected transposition show a posterior pulmonary artery from the left ventricular outflow."
    claims: [AS23-328]

  - id: XB4-Q12
    question: "Congenitally corrected transposition. Which rhythm problem must serial studies watch for?"
    options:
      - "Complete heart block"
      - "Sinus arrhythmia"
      - "Premature atrial beats only"
      - "None; rhythm is always normal"
    answer: 0
    explanation: "Rhythm abnormalities including congenital heart block can arise in fetal life; serial studies should be offered."
    claims: [AS23-338, AS23-339]

checklist:
  title: "Conotruncal lesion: minimum record"
  items:
    - text: "Outflow, three-vessel and three-vessel-and-trachea views and sweeps recorded"
      claims: [AS23-300, AS23-301]
    - text: "Position of the ventricular septal defect and relation of the great arteries defined"
      claims: [AS23-302, AS23-340]
    - text: "Branch pulmonary arteries imaged at their origins"
      claims: [AS23-306, AS23-311]
    - text: "Arch imaged in axial and sagittal planes when the arch is at risk"
      claims: [AS23-308]
    - text: "Arch and thymus imaged where 22q11 deletion is a concern"
      claims: [AS23-313]
    - text: "D-transposition: foramen ovale reassessed late in gestation"
      claims: [AS23-330]
    - text: "Corrected transposition: atrioventricular intervals and rhythm recorded; serial studies offered"
      claims: [AS23-354, AS23-339]
```

### Claims cited (with ledger statement and locator)

| id | status | statement | locator |
|---|---|---|---|
| AS23-286 | ai-cross-checked | In double-outlet right ventricle, additional assessment covers the relationship of the ventricular septal defect to the great vessels and the left ventricle-to-aorta pathway: the defect's size and any atrioventricular valve attachments that could preclude biventricular repair. | Table 13 (lesion-specific evaluation), DORV row, p. 707 |
| AS23-300 | ai-cross-checked | Outflow tract lesions are found at screening with the outflow, three-vessel and three-vessel-and-trachea views, and often show little abnormality on the four-chamber view. | IV.C.iii Look-Alike Outflow Tract Lesions, p. 713 |
| AS23-301 | ai-cross-checked | Sweeps from the four-chamber view through the outflow, three-vessel and three-vessel-and-trachea views detail the segmental anatomy of outflow lesions. | IV.C.iii Look-Alike Outflow Tract Lesions, p. 713 |
| AS23-302 | ai-cross-checked | Short-axis and coronal views help locate ventricular septal defects and show how the great arteries relate to each other. | IV.C.iii Look-Alike Outflow Tract Lesions, p. 713 |
| AS23-303 | ai-cross-checked | Outflow tract heart disease is often associated with anomalies of the veins, atrioventricular valves, septum, branch pulmonary arteries and arch. | IV.C.iii Look-Alike Outflow Tract Lesions, p. 713 |
| AS23-304 | ai-cross-checked | A ventricular septal defect with an overriding great vessel has a differential diagnosis that includes tetralogy of Fallot, pulmonary atresia with ventricular septal defect, double-outlet right ventricle and common arterial trunk. | IV.C.iii Lesions with a VSD and Overriding Great Vessel, p. 714; Figure 26 |
| AS23-305 | ai-extracted | Suspected outflow tract abnormalities should be evaluated by fetal echocardiography before prognosis, associated abnormalities and further testing, including genetic testing, are discussed with the patient. | IV.C.iii Key Points, p. 715 |
| AS23-306 | ai-cross-checked | A complete evaluation of an outflow tract lesion includes imaging the branch pulmonary arteries at their origins. | IV.C.iii Key Points, p. 715 |
| AS23-307 | ai-extracted | Aortic arch sidedness must be documented at least once in pregnancy, and an attempt made to define the branching pattern, especially when the aortic and ductal arches are on opposite sides of the trachea. | IV.C.iii Key Points, p. 715 |
| AS23-308 | ai-cross-checked | The aortic arch is at risk in any lesion with subaortic obstruction or a subpulmonary ventricular septal defect and should be imaged with two-dimensional and Doppler imaging in axial and sagittal planes. | IV.C.iii Key Points, p. 715 |
| AS23-309 | ai-cross-checked | Tetralogy of Fallot has an overriding aorta with variable obstruction below or at the pulmonary valve, from mild stenosis to atresia, or a dilated outflow with absent pulmonary valve. | IV.C.iii Lesions with a VSD and Overriding Great Vessel, p. 714 |
| AS23-310 | ai-extracted | Key observations listed for tetralogy of Fallot: an abnormal axis or left ventricular outflow tract together with a ventricular septal defect and an overriding vessel; and an abnormal three-vessel view. | Table 13 (lesion-specific evaluation), p. 707 |
| AS23-311 | ai-cross-checked | In tetralogy of Fallot the branch pulmonary arteries must be identified at their origins, because discontinuity, segmental stenosis and major aortopulmonary collaterals can coexist with an outflow or ductus that looks patent. | IV.C.iii Lesions with a VSD and Overriding Great Vessel, p. 714 |
| AS23-312 | ai-cross-checked | Tetralogy of Fallot may occur with atrioventricular septal defect. | IV.C.iii Lesions with a VSD and Overriding Great Vessel, p. 714 |
| AS23-313 | ai-cross-checked | Imaging the arch and the thymus allows counselling tailored to the risk of 22q11 deletion. | IV.C.iii Lesions with a VSD and Overriding Great Vessel, p. 714 |
| AS23-314 | ai-cross-checked | Venous and arch variants listed with tetralogy of Fallot include bilateral superior venae cavae, a retroaortic innominate vein, right aortic arch, vascular rings and aortopulmonary window. | Table 13 (lesion-specific evaluation), p. 707 |
| AS23-315 | ai-cross-checked | Additional measurements listed for tetralogy of Fallot are the branch pulmonary arteries, serial pulmonary valve annulus and the infundibulum. | Table 13 (lesion-specific evaluation), p. 707 |
| AS23-316 | ai-cross-checked | In tetralogy of Fallot, ductal direction at 28 weeks predicts the need for neonatal intervention. | Table 13 (lesion-specific evaluation), p. 707 |
| AS23-317 | ai-cross-checked | Absent pulmonary valve syndrome is most often linked with tetralogy of Fallot with a subaortic ventricular septal defect, but may also occur with an intact ventricular septum. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-318 | ai-cross-checked | Distinguishing absent pulmonary valve with a subaortic ventricular septal defect from absent pulmonary valve with an intact septum is critical for surgical planning and for assessing 22q11.2 deletion. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-319 | ai-cross-checked | Absent pulmonary valve syndrome shows a hypoplastic pulmonary annulus with tiny leaflets and to-and-fro colour flow across the valve. | Table 13 (lesion-specific evaluation), p. 709 |
| AS23-320 | ai-cross-checked | In absent pulmonary valve syndrome, dilatation of the main and branch pulmonary arteries and of the right atrium and ventricle are key findings. | Table 13 (lesion-specific evaluation), p. 709 |
| AS23-321 | ai-cross-checked | In absent pulmonary valve syndrome the ductus arteriosus is typically absent, but its presence should be assessed because it affects prognosis. | Table 13 (lesion-specific evaluation), p. 709; IV.C.iv, p. 717 |
| AS23-322 | ai-cross-checked | In tetralogy with absent pulmonary valve, arch position matters because an aneurysmal branch pulmonary artery on the same side may compress the airway. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-323 | ai-cross-checked | In absent pulmonary valve syndrome, progressive right ventricular dysfunction predicts perinatal death, and left ventricular dysfunction independently predicts fetal death. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-324 | ai-cross-checked | Cardiac position should be assessed in tetralogy with absent pulmonary valve, because an abnormal axis from segmental fluid trapping in the lung may signal airway obstruction after birth and can predict outcome. | IV.C.iv Key Points (regurgitation), p. 717 |
| AS23-325 | ai-cross-checked | Fetal MRI may be useful to measure lung volumes or fluid trapping in tetralogy with absent pulmonary valve. | IV.D Imaging-Based Risk Assessment and Delivery Planning, p. 718 |
| AS23-326 | ai-extracted | Key observations listed for d-TGA (l-TGA has a separate row): an abnormal three-vessel view, an abnormal left ventricular outflow view, and parallel outflows. | Table 13 (lesion-specific evaluation), p. 707 |
| AS23-327 | ai-extracted | A vessel arising from the left ventricular outflow that branches early is a pulmonary artery. Early branching identifies the vessel, not the lesion: in the illustrated case (Figure 26E) the diagnosis was d-TGA, while the same figure shows a posterior pulmonary artery from the left ventricular outflow in a Taussig-Bing double-outlet right ventricle and in l-TGA. | IV.C.iii Lesions with LV Outflow Giving Rise to a Posterior Pulmonary Artery, pp. 714-715; Figure 26E |
| AS23-328 | ai-cross-checked | Both D-transposition and congenitally corrected transposition show a posterior pulmonary artery arising from the left ventricular outflow. | IV.C.iii Lesions with LV Outflow Giving Rise to a Posterior Pulmonary Artery, pp. 714-715; Figure 26 |
| AS23-329 | ai-cross-checked | A diagnosis of D-transposition should prompt imaging of the atrial septum late in gestation, and delivery where the atrial communication can be enlarged if shunting is inadequate. | IV.C.iii Lesions with LV Outflow Giving Rise to a Posterior Pulmonary Artery, pp. 714-715 |
| AS23-330 | ai-cross-checked | Any fetus with D-transposition should have the patency of the foramen ovale assessed late in gestation. | IV.C.iii Key Points, p. 715 |
| AS23-331 | ai-cross-checked | In D-transposition the foramen ovale size is best defined in the sagittal view; a septal excursion index is an additional measurement. | Table 13 (lesion-specific evaluation), p. 707 |
| AS23-332 | ai-cross-checked | Constriction of the ductus arteriosus can be lethal in critical heart disease, with transposition at higher risk. | Table 14 (mechanisms and patterns of progression), pp. 710-711 |
| AS23-333 | ai-cross-checked | Gaps remain in predicting which fetuses with D-transposition and a restrictive atrial septum will need intervention immediately after birth; maternal hyperoxygenation testing has been studied but data are incomplete. | IV.D Imaging-Based Risk Assessment and Delivery Planning, p. 718 |
| AS23-334 | ai-cross-checked | In congenitally corrected transposition, atrioventricular and ventriculoarterial discordance together give physiologically corrected flow. | IV.C.iii Lesions with LV Outflow Giving Rise to a Posterior Pulmonary Artery, pp. 714-715 |
| AS23-335 | ai-extracted | Congenitally corrected transposition (l-TGA) may be identified on the four-chamber view by an abnormal crux and a moderator band at the apex of the left-sided right ventricle. | IV.C.iii Lesions with LV Outflow Giving Rise to a Posterior Pulmonary Artery, pp. 714-715 |
| AS23-336 | ai-cross-checked | A ventricular septal defect may be present in 60% to 70% of cases of congenitally corrected transposition, of variable type and location. | IV.C.iii Lesions with LV Outflow Giving Rise to a Posterior Pulmonary Artery, pp. 714-715 |
| AS23-337 | ai-cross-checked | Tricuspid valve dysplasia, Ebstein malformation and coarctation of the aorta can be associated with congenitally corrected transposition. | IV.C.iii Lesions with LV Outflow Giving Rise to a Posterior Pulmonary Artery, pp. 714-715 |
| AS23-338 | ai-cross-checked | In congenitally corrected transposition, rhythm abnormalities including congenital heart block can arise in fetal life and affect survival. | IV.C.iii Lesions with LV Outflow Giving Rise to a Posterior Pulmonary Artery, pp. 714-715 |
| AS23-339 | ai-cross-checked | Serial fetal echocardiography should be offered in congenitally corrected transposition to identify progressive atrioventricular valve regurgitation and rhythm abnormalities, including complete heart block. | IV.C.iii Key Points, p. 715 |
| AS23-340 | ai-cross-checked | In double-outlet right ventricle the ventricular septal defect may be subaortic, subpulmonary, doubly committed or remote; its position and the relative sizes of aorta and pulmonary artery must be determined. | IV.C.iii Lesions with a VSD and Overriding Great Vessel, p. 714 |
| AS23-341 | ai-cross-checked | Double-outlet right ventricle with a subaortic defect may resemble tetralogy of Fallot in anatomy and postnatal physiology. | IV.C.iii Lesions with a VSD and Overriding Great Vessel, p. 714 |
| AS23-342 | ai-cross-checked | With a subpulmonary ventricular septal defect, the anterior aorta may be obstructed below the valve, and coarctation often accompanies it, so the arch needs careful two-dimensional and colour imaging. | IV.C.iii Lesions with a VSD and Overriding Great Vessel, DORV paragraph, p. 714 |
| AS23-343 | ai-cross-checked | The Taussig-Bing anomaly shows a posterior vessel giving rise to the pulmonary artery over a subpulmonary ventricular septal defect, with an anterior aorta. | IV.C.iii Lesions with LV Outflow Giving Rise to a Posterior Pulmonary Artery, pp. 714-715; Figure 26A |
| AS23-344 | ai-cross-checked | In double-outlet right ventricle with a subpulmonary defect and a straddling mitral valve, a neonatal Damus-Kaye-Stansel operation may be more feasible than an arterial switch. | IV.C.iii Lesions with LV Outflow Giving Rise to a Posterior Pulmonary Artery, pp. 714-715; Figure 25 |
| AS23-345 | ai-cross-checked | In common arterial trunk a single arterial trunk gives rise directly to the coronary arteries, the aorta and one or both pulmonary arteries. | IV.C.iii Lesions with a VSD and Overriding Great Vessel, p. 714 |
| AS23-346 | ai-cross-checked | Common arterial trunk ranges from pulmonary-dominant forms (smaller aortic part, with or without arch interruption) to aortic-dominant forms. | IV.C.iii Lesions with a VSD and Overriding Great Vessel, p. 714 |
| AS23-347 | ai-cross-checked | Function of the truncal valve, especially significant regurgitation, can affect survival in utero. | IV.C.iii Lesions with a VSD and Overriding Great Vessel, p. 714 |
| AS23-348 | ai-cross-checked | In common arterial trunk the ductus arteriosus is often absent, but one may be present in all forms. | IV.C.iii Lesions with a VSD and Overriding Great Vessel, p. 714 |
| AS23-349 | ai-extracted | A ductus may be present in any form of common arterial trunk; the more pulmonary-dominant variants and common trunk with interrupted aortic arch depend entirely on ductal patency for perfusion of the lower body, and these fetuses need prostaglandin E1 started at birth. | IV.C.iii Lesions with a VSD and Overriding Great Vessel, p. 714 |
| AS23-350 | ai-cross-checked | In common arterial trunk, a right aortic arch is associated with a risk of 22q11 deletion above 50%. | Table 13 (lesion-specific evaluation), p. 707 |
| AS23-351 | ai-cross-checked | In common arterial trunk, truncal valve velocity and regurgitation and the proximal branch pulmonary artery dimensions are assessed. | Table 13 (lesion-specific evaluation), p. 707 |
| AS23-352 | ai-cross-checked | Outflow tract lesions with a normal four-chamber view are suspected when the cardiac axis is abnormal (below 30° or above 60°), the left ventricular outflow view is abnormal or not obtainable, or the three-vessel view is abnormal. | Table 13, outflow tract category heading, p. 707 |
| AS23-353 | ai-cross-checked | In tetralogy of Fallot, an aortic-to-pulmonary valve ratio below 0.6 and a pulmonary valve Z-score below -5, with no ductus arteriosus, predict the need for neonatal intervention. | Table 13, TOF row, p. 707 |
| AS23-354 | ai-cross-checked | In congenitally corrected transposition, tricuspid displacement and regurgitation are common and affect prognosis; atrioventricular intervals and ventricular septal defect are measured, and serial monitoring for heart block is listed. | Table 13, l-TGA row, p. 708 |
| AS23-360 | ai-extracted | In d-TGA the pulmonary valve may be bicuspid. | Table 13, d-TGA, outflow imaging, p. 707 |

---
## Unit XB2

### Unit file

```yaml
# Unit XB2. Every text block and drill lists the claim IDs it rests on.
# Built only from ai-cross-checked claims (ASE 2023, extracted by Claude, cross-checked by
# ChatGPT on 19 Nov 2026). Claims reworded on 21 Nov and awaiting re-check are left out and
# listed under missing_claims. Diagnose tier: needs the cardiology co-editor before release.

id: XB2
title: "Lesion atlas: left heart (aortic stenosis, HLHS, mitral, coarctation)"
tier: Diagnose
version: 0.1
summary: "Obstruction on the left side of the heart: how it shows, what to measure, the signs that it is critical or progressing, and the left atrial pressure problem."
drafted_by: "Claude (Opus 5.5, 21 Nov 2026)"
audited_by: null
signed_by: null

objectives:
  - "Name the findings that suggest progressive semilunar obstruction on a screening-level view."
  - "List what to record in fetal aortic stenosis at every study, and the signs of critical obstruction."
  - "Describe the findings of hypoplastic left heart syndrome and how left atrial hypertension is looked for."
  - "Describe the assessment of mitral valve abnormalities."
  - "Give the signs of coarctation and its main diagnostic limit."

sections:

  - heading: "Suspecting left heart obstruction"
    blocks:
      - text: "Progressive semilunar valve obstruction is suspected when the three-vessel view is abnormal or the four chambers are asymmetric."
        claims: [AS23-356]
      - text: "Fetal aortic and pulmonary stenosis span a broad range of severity."
        claims: [AS23-400]

  - heading: "Aortic stenosis"
    blocks:
      - text: "Doppler: evaluate valve morphology, size, patency and competence with colour, pulsed-wave and continuous-wave Doppler."
        claims: [AS23-404]
      - text: "Pitfall: aortic valve Doppler may not reflect severity when left ventricular dysfunction is severe. Reversed flow in the transverse arch predicts severe obstruction."
        claims: [AS23-413]
      - text: "Critical obstruction: retrograde flow in the arch on the side of the obstructed valve heralds critical obstruction at any gestation. If it is absent at first, look for it again through the pregnancy."
        claims: [AS23-405]
      - text: "Measure: ventricular size (end-diastolic diameter and length), whether the left ventricle forms the apex, hypertrophy, endocardial fibroelastosis, and systolic and diastolic function. These help judge severity and suitability for prenatal intervention. Assess the function of both ventricles."
        claims: [AS23-407, AS23-411]
      - text: "Associations: the arch and isthmus are at risk of coarctation and should be assessed."
        claims: [AS23-416]
      - text: "Evolution: with longer-standing obstruction the ascending aorta can dilate or become hypoplastic, so repeat the measurements. With severe left ventricular dysfunction, the left ventricle may stop forming the apex late in pregnancy."
        claims: [AS23-403, AS23-417]
      - text: "Left atrial pressure: in severe aortic obstruction, raised left atrial pressure can cause left-to-right atrial shunting and atrial restriction, altering pulmonary venous flow. Assess foramen ovale size and flow."
        claims: [AS23-415]
      - text: "Follow-up: serial evaluation from the time stenosis is suspected, including ventricular size and function and fibroelastosis. Document ductal and arch flow direction and atrial septal flow direction at every study."
        claims: [AS23-408, AS23-409, AS23-410]

  - heading: "Hypoplastic left heart syndrome"
    blocks:
      - text: "Definition: a small left ventricle on the four-chamber view, with mitral and aortic stenosis or atresia. It is the most common form of single ventricle, with an incidence of 0.26 per 1,000 live births."
        claims: [AS23-231, AS23-203]
      - text: "Views: assess aortic valve patency, the size of the ascending aorta, the transverse arch, and the direction of flow in the distal transverse arch. The ascending aorta diameter may predict outcome after the Norwood operation."
        claims: [AS23-232, AS23-233]
      - text: "Associations: tricuspid regurgitation with right ventricular dysfunction may increase the risk of fetal death and of illness and death after birth."
        claims: [AS23-234]
      - text: "Left atrial hypertension: the pulmonary venous forward-to-reverse velocity-time integral ratio is used to detect it. Measure it at every study, the last near term. A ratio below 3 predicts inadequate left atrial egress and a greater chance of emergency atrial septoplasty in the newborn."
        claims: [AS23-221, AS23-220, AS23-222]
      - text: "Maternal hyperoxygenation: may be considered late in the third trimester in selected cases. Lack of pulmonary vasoreactivity - a fall of less than 10% in pulmonary artery pulsatility index - is associated with neonatal instability and urgent opening of the atrial septum after birth."
        claims: [AS23-223, AS23-224]
      - text: "Evolution: foramen ovale restriction can lead to pulmonary congestion (nutmeg lung) and, in HLHS, to hypoxaemia, left atrial hypertension and the need for urgent balloon atrial septostomy after birth."
        claims: [AS23-282]
      - text: "Pitfall: isolated restriction of the foramen ovale may make the left-sided structures look small, with no consequence after birth."
        claims: [AS23-283]

  - heading: "Mitral valve abnormalities"
    blocks:
      - text: "Effect: mitral valve abnormalities may reduce flow to the left heart and reverse flow at the foramen ovale."
        claims: [AS23-261]
      - text: "Views and Doppler: image the mitral valve and atrial septum in two dimensions and colour, and use pulsed-wave Doppler of the pulmonary veins to look for raised left atrial pressure."
        claims: [AS23-262, AS23-263]
      - text: "Mitral stenosis: the valve may be parachute or hypoplastic; the papillary muscles and a Z-score of the valve are listed for assessment. Foramen ovale size and the pulmonary venous forward-to-reverse ratio are additional measurements. Flow direction at the foramen ovale is critical in judging whether the mitral valve is adequate."
        claims: [AS23-267, AS23-279, AS23-269]
      - text: "Mitral regurgitation: isolated mitral dysplasia and mitral arcade cause significant regurgitation, and any degree of mitral regurgitation in the fetus is abnormal. When it is present, consider left ventricular outflow obstruction."
        claims: [AS23-264, AS23-265]

  - heading: "Coarctation of the aorta"
    blocks:
      - text: "Views: a right ventricle larger than the left, an ascending aorta smaller than the superior vena cava, and a small transverse arch and isthmus. Isolated coarctation is suspected when the transverse aorta is smaller than the ductal arch."
        claims: [AS23-443, AS23-446]
      - text: "Measure: the aortic isthmus."
        claims: [AS23-447]
      - text: "Pitfall: prenatal diagnosis of coarctation has substantial false-positive and false-negative rates."
        claims: [AS23-444]

missing_claims:
  - "Awaiting re-check after rewording on 21 Nov (round 5, task J): key observations in aortic stenosis (AS23-412); severity from the mitral regurgitant jet (AS23-414); progression and hydrops in severe obstruction (AS23-401, 402, 406); peak velocity and annulus size in atrioventricular valve disease (AS23-266); Figure 21 assessment of atrial restriction (AS23-284); lesions with restrictive foramen ovale (AS23-281); HLHS with mitral regurgitation in the follow-up table (AS23-423); warning signs on the three-vessel-and-trachea view (AS23-445); gradients not indicating severity (AS23-362, new)."
  - "Interrupted aortic arch: no claims held - needs a source."
  - "Fetal intervention for aortic stenosis with evolving HLHS: candidacy and outcomes are in unit Z5."
  - "Normal values and Z-scores for the measurements named here - unit XA6 and a Z-score source."
  - "Delivery planning for ductal-dependent left heart lesions - unit Z3."
  - "Video outline not yet written."

drills:
  - id: XB2-Q01
    question: "A screening scan shows asymmetric four chambers and an abnormal three-vessel view. Which group of lesions does the guideline suggest?"
    options:
      - "Progressive semilunar valve obstruction"
      - "Normal variant; no action"
      - "Atrial septal defect only"
      - "Venous anomalies only"
    answer: 0
    explanation: "Progressive semilunar obstruction is suspected when the three-vessel view is abnormal or the four chambers are asymmetric."
    claims: [AS23-356]

  - id: XB2-Q02
    question: "Fetal aortic stenosis with a poorly contracting left ventricle. The aortic valve velocity is low. What is the trap?"
    options:
      - "Valve Doppler may not reflect severity when left ventricular dysfunction is severe"
      - "A low velocity always means mild stenosis"
      - "Low velocity means the valve is normal"
      - "Velocity is the only measure that matters"
    answer: 0
    explanation: "Aortic valve Doppler may not reflect severity with severe LV dysfunction; reversed flow in the transverse arch predicts severe obstruction."
    claims: [AS23-413]

  - id: XB2-Q03
    question: "In aortic stenosis, which arch finding heralds critical obstruction at any gestation?"
    options:
      - "Retrograde flow in the arch on the side of the obstructed valve"
      - "Antegrade flow in the arch"
      - "A left-sided arch"
      - "A large thymus"
    answer: 0
    explanation: "Retrograde ipsilateral arch flow heralds critical obstruction; if absent at first, it should be looked for repeatedly."
    claims: [AS23-405]

  - id: XB2-Q04
    question: "Which features help judge severity and suitability for prenatal intervention in aortic stenosis?"
    options:
      - "Ventricular size, apex formation, hypertrophy, endocardial fibroelastosis and function"
      - "Fetal heart rate only"
      - "Nuchal translucency"
      - "Umbilical cord insertion"
    answer: 0
    explanation: "These ventricular features help judge severity and candidacy for prenatal intervention."
    claims: [AS23-407]

  - id: XB2-Q05
    question: "HLHS. A pulmonary venous forward-to-reverse VTI ratio below 3 predicts what?"
    options:
      - "Inadequate left atrial egress and greater likelihood of emergency atrial septoplasty in the newborn"
      - "A normal transition at birth"
      - "Complete heart block"
      - "Coarctation"
    answer: 0
    explanation: "A ratio below 3 predicts inadequate left atrial egress and a greater likelihood of emergency septoplasty."
    claims: [AS23-222]

  - id: XB2-Q06
    question: "HLHS with maternal hyperoxygenation testing late in pregnancy. Which result is associated with neonatal instability?"
    options:
      - "A fall of less than 10% in pulmonary artery pulsatility index"
      - "A fall of more than 10% in pulmonary artery pulsatility index"
      - "A rise in fetal heart rate"
      - "No change in umbilical artery flow"
    answer: 0
    explanation: "Lack of vasoreactivity (a fall of less than 10% in branch PA pulsatility index) is associated with neonatal instability and urgent atrial septal opening."
    claims: [AS23-224]

  - id: XB2-Q07
    question: "The left heart looks small and the foramen ovale appears restrictive, with no other heart disease. What does the guideline warn?"
    options:
      - "Isolated foramen restriction may make left structures look small with no consequence after birth"
      - "This is always hypoplastic left heart syndrome"
      - "Immediate delivery is needed"
      - "The finding has no relevance at all"
    answer: 0
    explanation: "In isolation, foramen ovale restriction can make left-sided structures appear smaller but have no consequence after delivery."
    claims: [AS23-283]

  - id: XB2-Q08
    question: "Mild mitral regurgitation is seen in a fetus. How should it be regarded?"
    options:
      - "As abnormal; and consider left ventricular outflow obstruction"
      - "As a normal finding"
      - "As normal unless the heart rate is low"
      - "As an artefact of colour gain"
    answer: 0
    explanation: "Any degree of fetal mitral regurgitation is abnormal; with mitral regurgitation, consider associated LV outflow obstruction."
    claims: [AS23-264, AS23-265]

  - id: XB2-Q09
    question: "Mitral stenosis. Which finding is critical in judging whether the mitral valve is adequate?"
    options:
      - "Direction of flow at the foramen ovale"
      - "Fetal heart rate"
      - "Cardiac axis"
      - "Thymus size"
    answer: 0
    explanation: "Flow direction at the foramen ovale is critical in judging adequacy of the mitral valve."
    claims: [AS23-269]

  - id: XB2-Q10
    question: "Which set of findings suggests coarctation?"
    options:
      - "Right ventricle larger than left, ascending aorta smaller than the superior vena cava, small arch and isthmus"
      - "Left ventricle larger than right with a dilated ascending aorta"
      - "Normal four chambers with a large isthmus"
      - "Pericardial effusion only"
    answer: 0
    explanation: "These are the coarctation findings listed in Table 13."
    claims: [AS23-443]

  - id: XB2-Q11
    question: "A colleague says a prenatal diagnosis of coarctation is reliable. What does the guideline say?"
    options:
      - "It has substantial false-positive and false-negative rates"
      - "It is never wrong"
      - "It has false positives but no false negatives"
      - "It is reliable if the heart rate is normal"
    answer: 0
    explanation: "Prenatal diagnosis of coarctation has substantial false-positive and false-negative rates."
    claims: [AS23-444]

checklist:
  title: "Left heart obstruction: each study"
  items:
    - text: "Valve morphology, size, patency and competence with colour, pulsed-wave and continuous-wave Doppler"
      claims: [AS23-404]
    - text: "Arch and ductal flow direction documented"
      claims: [AS23-409, AS23-405]
    - text: "Atrial septal flow direction documented; foramen ovale size"
      claims: [AS23-410, AS23-415]
    - text: "Left ventricular size, apex, hypertrophy, fibroelastosis and function; both ventricles' function"
      claims: [AS23-407, AS23-411]
    - text: "Arch and isthmus assessed for coarctation"
      claims: [AS23-416, AS23-447]
    - text: "HLHS: pulmonary venous forward-to-reverse VTI ratio, last one near term"
      claims: [AS23-220]
```

### Claims cited (with ledger statement and locator)

| id | status | statement | locator |
|---|---|---|---|
| AS23-203 | ai-cross-checked | Hypoplastic left heart syndrome is the most common form of single ventricle, with an incidence of 0.26 per 1,000 live births. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 |
| AS23-220 | ai-cross-checked | In hypoplastic left heart syndrome, the pulmonary venous forward-to-reverse velocity-time integral ratio should be measured at every fetal echocardiogram, the last measurement near term. | IV.C.i Key Points, p. 704 |
| AS23-221 | ai-cross-checked | The pulmonary venous forward-to-reverse velocity-time integral ratio is used to detect left atrial hypertension. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 |
| AS23-222 | ai-cross-checked | In hypoplastic left heart syndrome, a pulmonary venous forward-to-reverse velocity-time integral ratio below 3 predicts inadequate left atrial egress and a greater likelihood of emergency atrial septoplasty in the newborn. | Table 13 (lesion-specific evaluation), HLHS row, p. 705 |
| AS23-223 | ai-cross-checked | Maternal hyperoxygenation testing late in the third trimester may be considered in selected cases of hypoplastic left heart syndrome. | IV.C.i Key Points, p. 704 |
| AS23-224 | ai-cross-checked | Lack of pulmonary vasoreactivity on maternal hyperoxygenation (a fall of less than 10% in pulmonary artery pulsatility index) is associated with neonatal instability and urgent opening of the atrial septum after birth. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 |
| AS23-231 | ai-cross-checked | Hypoplastic left heart syndrome shows a small left ventricle on the four-chamber view with mitral and aortic stenosis or atresia. | Table 13 (lesion-specific evaluation), p. 705 |
| AS23-232 | ai-cross-checked | In hypoplastic left heart syndrome, aortic valve patency, ascending aorta size, the transverse arch and the direction of flow in the distal transverse arch should be assessed. | Table 13 (lesion-specific evaluation), p. 705 |
| AS23-233 | ai-cross-checked | In hypoplastic left heart syndrome, the ascending aorta diameter may predict outcome after the Norwood operation. | Table 13 (lesion-specific evaluation), p. 705 |
| AS23-234 | ai-cross-checked | In hypoplastic left heart syndrome, tricuspid regurgitation with right ventricular dysfunction may increase the risk of fetal death and postnatal morbidity and mortality. | Table 13 (lesion-specific evaluation), p. 705 |
| AS23-261 | ai-cross-checked | Mitral valve abnormalities may reduce flow to the left heart and reverse flow at the foramen ovale. | IV.C.ii Congenital Mitral Valve Abnormalities, p. 712 |
| AS23-262 | ai-cross-checked | With a mitral valve abnormality, two-dimensional and colour Doppler imaging of the mitral valve and atrial septum should be performed. | IV.C.ii Congenital Mitral Valve Abnormalities, p. 712 |
| AS23-263 | ai-cross-checked | With a mitral valve abnormality, pulsed-wave Doppler of the pulmonary veins should be used to look for increased left atrial pressure. | IV.C.ii Congenital Mitral Valve Abnormalities, p. 712 |
| AS23-264 | ai-cross-checked | Isolated mitral dysplasia and mitral arcade cause significant mitral regurgitation; any degree of mitral regurgitation in the fetus is abnormal. | IV.C.ii Congenital Mitral Valve Abnormalities, p. 712 |
| AS23-265 | ai-cross-checked | When mitral regurgitation is present, associated left ventricular outflow obstruction should be considered. | IV.C.ii Congenital Mitral Valve Abnormalities, p. 712 |
| AS23-266 | ai-extracted | With abnormal atrioventricular valves, peak velocity may underestimate stenosis because fetal flow can redistribute; annulus size should be documented in right atrioventricular valve disease, and left-to-right shunting at atrial level in left atrioventricular valve obstruction. | IV.C.ii General Imaging Approach, p. 712 |
| AS23-267 | ai-cross-checked | Mitral stenosis may have parachute or hypoplastic morphology; papillary muscles and a Z-score of the valve are listed for assessment. | Table 13 (lesion-specific evaluation), p. 706 |
| AS23-269 | ai-cross-checked | The direction of flow at the foramen ovale is critical in judging whether the mitral valve is adequate. | Table 13 (lesion-specific evaluation), p. 706 |
| AS23-279 | ai-cross-checked | In mitral stenosis, foramen ovale dimension and the pulmonary vein forward-to-reverse ratio are listed as additional measurements. | Table 13 (lesion-specific evaluation), mitral stenosis row, p. 706 |
| AS23-281 | ai-extracted | Restriction of the foramen ovale occurs in d-TGA, hypoplastic left heart syndrome and critical left heart obstruction, and can also occur without other heart disease. | Table 14 (mechanisms and patterns of progression), pp. 710-711 |
| AS23-282 | ai-cross-checked | Foramen ovale restriction can lead to pulmonary congestion (nutmeg lung) and, in hypoplastic left heart syndrome, to postnatal hypoxaemia, left atrial hypertension and the need for urgent balloon atrial septostomy. | Table 14 (mechanisms and patterns of progression), pp. 710-711 |
| AS23-283 | ai-cross-checked | Isolated foramen ovale restriction may make the left-sided structures look small without consequence after birth. | Table 14 (mechanisms and patterns of progression), pp. 710-711 |
| AS23-284 | ai-extracted | In an illustrated fetus with left heart obstruction (Figure 21), atrial septal restriction was assessed from left-to-right flow across the atrial septum, enlarged pulmonary veins with to-and-fro flow, and a pulsed Doppler forward-and-reverse pulmonary venous pattern described as consistent with moderately raised left atrial pressure. This is an illustrated case, not a grading rule. | Figure 21 caption, p. 711 |
| AS23-356 | ai-cross-checked | Progressive semilunar valve obstruction is suspected when the three-vessel view is abnormal or the four chambers are asymmetric. | Table 13, category heading, p. 708 |
| AS23-362 | ai-extracted | In semilunar valve stenosis, Doppler pressure gradients may be measured and reported, but they do not necessarily indicate how severe the stenosis is. | IV.C.iv Semilunar Valve Obstruction, Key Points, p. 716 |
| AS23-400 | ai-cross-checked | Fetal aortic and pulmonary stenosis span a broad range of severity. | IV.C.iv Semilunar Valve Obstruction with an Intact Ventricular Septum, pp. 715-716 |
| AS23-401 | ai-extracted | The lesions with the greatest potential to progress in utero include semilunar valve obstruction with an intact ventricular septum and lesions with significant valve regurgitation; serial assessment of both is essential. | IV.C.iv Semilunar Valve Obstruction with an Intact Ventricular Septum, pp. 715-716 |
| AS23-403 | ai-cross-checked | With longer-standing obstruction the downstream great artery can dilate or become hypoplastic, so measurements need repeating. | IV.C.iv Semilunar Valve Obstruction with an Intact Ventricular Septum, pp. 715-716 |
| AS23-404 | ai-cross-checked | Valve morphology, size, patency and competence should be evaluated with colour, pulsed-wave and continuous-wave Doppler. | IV.C.iv Semilunar Valve Obstruction with an Intact Ventricular Septum, pp. 715-716; Figure 27 |
| AS23-405 | ai-cross-checked | Retrograde flow in the arch on the same side as the obstructed valve heralds critical obstruction at any gestational age; if absent at first, it should be looked for repeatedly through the pregnancy. | IV.C.iv Semilunar Valve Obstruction with an Intact Ventricular Septum, pp. 715-716; Figure 28 |
| AS23-407 | ai-cross-checked | Ventricular size (end-diastolic diameter and length), whether the ventricle forms the apex, hypertrophy, endocardial fibroelastosis and systolic and diastolic function help judge severity and suitability for prenatal intervention. | IV.C.iv Semilunar Valve Obstruction with an Intact Ventricular Septum, pp. 715-716 |
| AS23-408 | ai-cross-checked | Serial evaluation should be performed when valve stenosis is suspected, including ventricular size and function and endocardial fibroelastosis. | IV.C.iv Key Points (semilunar obstruction), p. 716 |
| AS23-409 | ai-cross-checked | Ductal and aortic arch flow direction must be documented at every examination; abnormal direction heralds critical obstruction after birth. | IV.C.iv Key Points (semilunar obstruction), p. 716 |
| AS23-410 | ai-cross-checked | Atrial septal flow direction must be documented at every examination when semilunar valve stenosis is present. | IV.C.iv Key Points (semilunar obstruction), p. 716 |
| AS23-411 | ai-cross-checked | Evaluation of both ventricles' function is recommended in aortic and pulmonary stenosis. | IV.C.iv Key Points (semilunar obstruction), p. 716 |
| AS23-412 | ai-extracted | Key observations listed for aortic stenosis: a thickened valve in systole on the left ventricular outflow view; with or without a dilated ascending aorta on the three-vessel view; and left ventricular hypertrophy, or dilation and dysfunction, on the four-chamber view. | Table 13 (lesion-specific evaluation), p. 708 |
| AS23-413 | ai-cross-checked | In aortic stenosis, aortic valve Doppler may not reflect severity when left ventricular dysfunction is severe; reversed flow in the transverse arch predicts severe obstruction. | Table 13 (lesion-specific evaluation), p. 708 |
| AS23-414 | ai-extracted | In aortic stenosis, continuous-wave Doppler of mitral regurgitation gives insight into severity and ventricular function: higher velocities in more severe disease suggest preserved function; low velocities could suggest less severe obstruction, severe myocardial dysfunction, or a primary problem that is myocardial or related to severe atrioventricular valve regurgitation rather than outflow obstruction. | IV.C.iv Semilunar Valve Obstruction with an Intact Ventricular Septum, pp. 715-716 |
| AS23-415 | ai-cross-checked | In severe aortic obstruction, raised left atrial pressure can cause left-to-right atrial shunting and atrial restriction, altering pulmonary venous flow; foramen ovale size and flow should be assessed. | IV.C.iv Semilunar Valve Obstruction with an Intact Ventricular Septum, pp. 715-716 |
| AS23-416 | ai-cross-checked | In aortic stenosis the arch and isthmus are at risk of coarctation and should be assessed. | Table 13 (lesion-specific evaluation), p. 708 |
| AS23-417 | ai-cross-checked | Aortic stenosis with severe left ventricular dysfunction can progress to a left ventricle that no longer forms the apex late in pregnancy. | Figure 27 caption, p. 716 |
| AS23-423 | ai-extracted | Table 15 gives hypoplastic left heart syndrome with mitral regurgitation as an example of fetal heart disease at risk of heart failure, for which it suggests comprehensive assessment of cardiac function every 2-4 weeks, the interval being at the discretion of the fetal cardiology and obstetric providers. | Table 15 (follow-up imaging for specific CHD diagnoses), p. 719 |
| AS23-443 | ai-cross-checked | Coarctation is suggested by a right ventricle larger than the left, an ascending aorta smaller than the superior vena cava, and a small transverse arch and isthmus. | Table 13 (lesion-specific evaluation), p. 709 |
| AS23-444 | ai-cross-checked | Prenatal diagnosis of coarctation has substantial false-positive and false-negative rates. | Table 13 (lesion-specific evaluation), p. 709 |
| AS23-445 | ai-extracted | On the three-vessel-and-trachea view, a size discrepancy between the arches, abnormal colour flow direction, a 'U' shape, or separation of the superior vena cava and trachea by one or two arches should alert the examiner to arch abnormalities, including coarctation, ductal aneurysm, right aortic arch and vascular rings. | IV.C.v Isolated Arch Abnormalities, p. 717 |
| AS23-446 | ai-cross-checked | Isolated coarctation is suspected when the transverse aorta is smaller than the ductal arch. | Figure 30D caption, p. 718 |
| AS23-447 | ai-cross-checked | The aortic isthmus is listed as an additional measurement in suspected coarctation. | Table 13 (lesion-specific evaluation), p. 709 |

---
## Unit XB1

### Unit file

```yaml
# Unit XB1. Every text block and drill lists the claim IDs it rests on.
# Built only from ai-cross-checked claims (ASE 2023, extracted by Claude, cross-checked by
# ChatGPT on 19 Nov 2026). Claims reworded on 21 Nov and awaiting re-check are left out and
# listed under missing_claims. Diagnose tier: needs the cardiology co-editor before release.

id: XB1
title: "Lesion atlas: septal and atrioventricular lesions (AVSD, common valve, straddling, VSD)"
tier: Diagnose
version: 0.1
summary: "How to examine an abnormal atrioventricular junction, how to judge balance in AVSD, and the traps of straddling, overriding and crisscross connections."
drafted_by: "Claude (Opus 5.5, 21 Nov 2026)"
audited_by: null
signed_by: null

objectives:
  - "Set out the imaging approach to any atrioventricular valve abnormality."
  - "Describe what to examine when an atrioventricular septal defect is suspected, and how imbalance is measured."
  - "Define straddling and overriding valves and say why they matter for surgery."
  - "Name the associations and pitfalls of a common atrioventricular valve."

sections:

  - heading: "Approach to any atrioventricular valve abnormality"
    blocks:
      - text: "Lesions of the atrioventricular junction may be isolated, often with aneuploidy including trisomy 21, or complex, with several associated defects."
        claims: [AS23-249]
      - text: "Malformed atrioventricular valves carry high rates of ventricular disproportion, ventricular septal defects and malformation of the outflows and great arteries, and may lead to single-ventricle palliation."
        claims: [AS23-238]
      - text: "Start with the four-chamber view, the atrioventricular septum aligned perpendicular to the beam. A sagittal view of the thorax best shows valve morphology, chordae and papillary muscles in short axis. Use non-standard planes and en face imaging when the junction looks abnormal. Obtain cephalad sweeps to define the outflows and great arteries."
        claims: [AS23-240, AS23-243, AS23-247, AS23-242]
      - text: "Measure the annulus in early diastole at the hinge points."
        claims: [AS23-241]
      - text: "Evaluate every cardiac structure, including ventricular size and function and the balance of the junction over the ventricles."
        claims: [AS23-239]
      - text: "Doppler: pulsed-wave Doppler of inflow is essential, but peak velocity may underestimate stenosis because fetal flow can redistribute. At each study a complete Doppler assessment must cover stenosis, regurgitation and flow at the atrial septum and ductus."
        claims: [AS23-244, AS23-246]
      - text: "Delineate any additional lesion that affects the surgical approach, to help decide between palliation and biventricular repair."
        claims: [AS23-248]

  - heading: "Atrioventricular septal defect"
    blocks:
      - text: "Views: examine the left atrioventricular valve en face for a cleft or common orifice; check the atrial septum for a primum defect and the ventricular septum for an inlet defect."
        claims: [AS23-251, AS23-252]
      - text: "Doppler: assess valve regurgitation with colour Doppler."
        claims: [AS23-256]
      - text: "Measuring balance: the valve area over each ventricle can be measured in diastole from a parasagittal view to give an atrioventricular valve index. The right-to-left ventricular inflow angle can be measured from an apical four-chamber view; a smaller angle means greater imbalance."
        claims: [AS23-253, AS23-254]
      - text: "Unbalanced AVSD: measure the right and left atrioventricular valve diameter or area; the Cohen index, valve index and inflow angle are listed. Regurgitation of the common valve may progress. Consider right or left atrial isomerism (heterotaxy)."
        claims: [AS23-237, AS23-236, AS23-235]

  - heading: "Common atrioventricular valve"
    blocks:
      - text: "Views: suspected when the crux lacks offset, or the valves appear at the same level, with large atrial or ventricular septal defects."
        claims: [AS23-258]
      - text: "Associations: bilateral superior venae cavae, an interrupted inferior vena cava, or total anomalous pulmonary venous return."
        claims: [AS23-259]
      - text: "Pitfall: additional ventricular septal defects may be missed unless they are looked for."
        claims: [AS23-260]

  - heading: "Straddling, overriding and crisscross connections"
    blocks:
      - text: "Definitions: in a straddling valve, chordae pass through a ventricular septal defect and attach in the opposite ventricle. In an overriding valve, the annulus sits over the septum and opens into both ventricles."
        claims: [AS23-270, AS23-271]
      - text: "Suspect a complex junction when the four-chamber view does not show two separate valves with offset at the crux. Image the valves with combined two-dimensional, colour and pulsed-wave Doppler from several views; video clips and live scanning show straddling better than still images."
        claims: [AS23-273, AS23-275, AS23-278]
      - text: "Associations: straddling can occur with D- or L-looped ventricles and carries a risk of heart block. If the left valve is hypoplastic, the fetus is at risk of left atrial hypertension."
        claims: [AS23-280, AS23-268]
      - text: "Surgery: a straddling or overriding valve may make closure of the ventricular septal defect impossible and may require a single-ventricle approach."
        claims: [AS23-277]
      - text: "Pitfall: in a crisscross heart, foreshortening can cause confusion between one and two ventricles."
        claims: [AS23-274]

  - heading: "Ventricular septal defect"
    blocks:
      - text: "Evolution: a ventricular septal defect can get smaller, with less severe or resolved disease. This usually happens with simple isolated defects, including muscular ones, but can occur in other heart disease."
        claims: [AS23-285]

missing_claims:
  - "Awaiting re-check after rewording on 21 Nov (round 5, task J): the abnormal crux of AVSD with valve levels when closed (AS23-250); the valve index threshold and its dependence on the equation (AS23-255); outflow obstruction in AVSD (AS23-257); crisscross anatomy and discordance (AS23-272, 276, 359)."
  - "Isolated ventricular septal defect: types, views, colour settings, and how often each closes - needs a source."
  - "Atrial septal defects (secundum, sinus venosus) and the normal foramen ovale - needs a source."
  - "Genetic work-up after AVSD - unit XA2."
  - "Video outline not yet written."

drills:
  - id: XB1-Q01
    question: "An atrioventricular junction lesion is found with no other defect. Which association should be considered?"
    options:
      - "Aneuploidy, including trisomy 21"
      - "Maternal diabetes only"
      - "No association; isolated lesions are always sporadic"
      - "Fetal anaemia"
    answer: 0
    explanation: "Isolated AV junction lesions are often associated with aneuploidy, including trisomy 21."
    claims: [AS23-249]

  - id: XB1-Q02
    question: "Which view best shows atrioventricular valve morphology, chordae and papillary muscles in short axis?"
    options:
      - "A sagittal view of the fetal thorax"
      - "The three-vessel-and-trachea view"
      - "The abdominal situs view"
      - "The ductal arch view"
    answer: 0
    explanation: "A sagittal view of the thorax best shows the valve in short axis."
    claims: [AS23-243]

  - id: XB1-Q03
    question: "Peak inflow velocity across a stenotic atrioventricular valve looks modest. Why be careful?"
    options:
      - "Peak velocity may underestimate stenosis because fetal flow can redistribute"
      - "Peak velocity always overestimates stenosis"
      - "Velocity cannot be measured in the fetus"
      - "There is no reason; modest velocity excludes stenosis"
    answer: 0
    explanation: "Fetal flow redistribution means peak velocity may underestimate severity."
    claims: [AS23-244]

  - id: XB1-Q04
    question: "AVSD is suspected. What should be examined en face?"
    options:
      - "The left atrioventricular valve, for a cleft or common orifice"
      - "The pulmonary valve, for leaflet number"
      - "The ductus venosus"
      - "The aortic arch"
    answer: 0
    explanation: "The left AV valve should be examined en face for a cleft or common orifice."
    claims: [AS23-251]

  - id: XB1-Q05
    question: "In AVSD, what does a smaller right-to-left ventricular inflow angle indicate?"
    options:
      - "Greater imbalance"
      - "A balanced defect"
      - "A normal heart"
      - "Heart block"
    answer: 0
    explanation: "The inflow angle is measured from an apical four-chamber view; a smaller angle indicates greater imbalance."
    claims: [AS23-254]

  - id: XB1-Q06
    question: "Features of an unbalanced AVSD are seen. Which condition should be considered?"
    options:
      - "Right or left atrial isomerism (heterotaxy)"
      - "Isolated coarctation"
      - "Ductal constriction"
      - "Twin-twin transfusion"
    answer: 0
    explanation: "With unbalanced AVSD, right or left atrial isomerism should be considered."
    claims: [AS23-235]

  - id: XB1-Q07
    question: "A common atrioventricular valve is seen. Which venous anomalies often accompany it?"
    options:
      - "Bilateral superior venae cavae, interrupted inferior vena cava, total anomalous pulmonary venous return"
      - "None; veins are always normal"
      - "Persistent right umbilical vein only"
      - "Agenesis of the ductus venosus only"
    answer: 0
    explanation: "These three are listed with a common AV valve."
    claims: [AS23-259]

  - id: XB1-Q08
    question: "With a common atrioventricular valve, what may be missed unless specifically looked for?"
    options:
      - "Additional ventricular septal defects"
      - "A right aortic arch"
      - "The fetal heart rate"
      - "The pulmonary valve"
    answer: 0
    explanation: "Additional VSDs may be missed unless looked for."
    claims: [AS23-260]

  - id: XB1-Q09
    question: "Chordae from one atrioventricular valve pass through a VSD and attach in the opposite ventricle. What is this called, and why does it matter?"
    options:
      - "A straddling valve; closure of the VSD may be impossible"
      - "An overriding valve; it has no surgical relevance"
      - "A cleft valve; it always closes after birth"
      - "A normal variant"
    answer: 0
    explanation: "This is straddling. A straddling or overriding valve may make VSD closure impossible and require a single-ventricle approach."
    claims: [AS23-270, AS23-277]

  - id: XB1-Q10
    question: "Straddling valve with a hypoplastic left atrioventricular valve. Which risk follows?"
    options:
      - "Left atrial hypertension"
      - "Pulmonary valve regurgitation"
      - "Ductal aneurysm"
      - "No added risk"
    answer: 0
    explanation: "With a hypoplastic left AV valve, the fetus is at risk of left atrial hypertension."
    claims: [AS23-268]

  - id: XB1-Q11
    question: "How is straddling anatomy best shown?"
    options:
      - "Video clips and live scanning, from several views"
      - "One still image in the four-chamber view"
      - "M-mode only"
      - "It cannot be shown before birth"
    answer: 0
    explanation: "Clips and live scanning show straddling better than stills; combined 2D, colour and pulsed-wave from multiple views are recommended."
    claims: [AS23-278, AS23-275]

checklist:
  title: "Atrioventricular junction: minimum record"
  items:
    - text: "Four-chamber view with the septum perpendicular; sagittal short-axis view of the valve; en face views"
      claims: [AS23-240, AS23-243, AS23-247]
    - text: "Annulus measured in early diastole at the hinge points"
      claims: [AS23-241]
    - text: "Balance assessed: valve index and inflow angle where an AVSD is present"
      claims: [AS23-253, AS23-254, AS23-237]
    - text: "Complete Doppler: stenosis, regurgitation, atrial septal and ductal flow"
      claims: [AS23-246, AS23-256]
    - text: "Outflows defined with cephalad sweeps"
      claims: [AS23-242]
    - text: "Additional VSDs looked for; straddling recorded on clips"
      claims: [AS23-260, AS23-278]
```

### Claims cited (with ledger statement and locator)

| id | status | statement | locator |
|---|---|---|---|
| AS23-235 | ai-cross-checked | With features of an unbalanced atrioventricular septal defect, right or left atrial isomerism (heterotaxy) should be considered. | Table 13 (lesion-specific evaluation), p. 705 |
| AS23-236 | ai-cross-checked | In unbalanced atrioventricular septal defect, regurgitation of the common valve may be progressive. | Table 13 (lesion-specific evaluation), p. 705 |
| AS23-237 | ai-cross-checked | For unbalanced atrioventricular septal defect, right and left atrioventricular valve diameter or area are measured, and the Cohen index, atrioventricular valve index and right-to-left ventricular inflow angle are listed. | Table 13 (lesion-specific evaluation), pp. 705-706 |
| AS23-238 | ai-cross-checked | Abnormal or malformed atrioventricular valves carry high rates of ventricular disproportion, ventricular septal defects and malformation of the outflow tracts and great arteries, and may need single-ventricle palliation. | IV.C.ii AV valve abnormalities, General Imaging Approach, p. 712 |
| AS23-239 | ai-cross-checked | With an atrioventricular valve abnormality, all cardiac structures, including ventricular size and function and the balance of the atrioventricular junction over the ventricles, should be evaluated. | IV.C.ii Key Points, p. 713 |
| AS23-240 | ai-cross-checked | The four-chamber view is the starting point, with the atrioventricular septum aligned perpendicular to the beam to define valve morphology. | IV.C.ii AV valve abnormalities, General Imaging Approach, p. 712 |
| AS23-241 | ai-cross-checked | Atrioventricular valve annular dimensions should be measured in early diastole at the hinge points. | IV.C.ii AV valve abnormalities, General Imaging Approach, p. 712 |
| AS23-242 | ai-cross-checked | Cephalad sweeps should be obtained to define outflow tract and great artery anatomy when an atrioventricular valve abnormality is present. | IV.C.ii AV valve abnormalities, General Imaging Approach, p. 712 |
| AS23-243 | ai-cross-checked | A sagittal view of the fetal thorax best shows atrioventricular valve morphology, chordae and papillary muscles in short axis. | IV.C.ii AV valve abnormalities, General Imaging Approach, p. 712 |
| AS23-244 | ai-cross-checked | Pulsed-wave Doppler evaluation of atrioventricular inflow is essential; peak velocity may underestimate the severity of stenosis because fetal flow can redistribute. | IV.C.ii AV valve abnormalities, General Imaging Approach, p. 712 |
| AS23-246 | ai-cross-checked | At each examination with an atrioventricular valve abnormality, a complete Doppler assessment must be done, including valve stenosis and regurgitation and flow at the atrial septum and ductus. | IV.C.ii Key Points, p. 713 |
| AS23-247 | ai-cross-checked | Non-standard planes and en face imaging should be used when an abnormality of the atrioventricular junction is suspected. | IV.C.ii Key Points, p. 713 |
| AS23-248 | ai-cross-checked | Additional lesions that affect the surgical approach must be delineated, to help decide between palliation and biventricular repair. | IV.C.ii Key Points, p. 713 |
| AS23-249 | ai-cross-checked | Lesions of the atrioventricular junction may be isolated (often with aneuploidy, including trisomy 21) or complex, with multiple associated defects. | IV.C.ii opening, p. 704 |
| AS23-250 | ai-extracted | An abnormal crux on the four-chamber view, with the septal leaflet of the right-sided atrioventricular valve at the same level as the anterior leaflet of the left-sided valve when the valves are closed, should prompt further assessment for atrioventricular septal defect. | IV.C.ii AV Septal Defects, p. 712; Figures 23, 24 |
| AS23-251 | ai-cross-checked | In suspected atrioventricular septal defect, the left atrioventricular valve should be examined en face for a cleft or common orifice. | IV.C.ii AV Septal Defects, p. 712 |
| AS23-252 | ai-cross-checked | In suspected atrioventricular septal defect, the atrial septum should be checked for a primum defect and the ventricular septum for an inlet defect. | IV.C.ii AV Septal Defects, p. 712 |
| AS23-253 | ai-cross-checked | The valve area over each ventricle can be measured in diastole from a parasagittal view to derive an atrioventricular valve index. | IV.C.ii AV Septal Defects, p. 712; Figure 23 |
| AS23-254 | ai-cross-checked | The right-to-left ventricular inflow angle can be measured from an apical four-chamber view; a smaller angle indicates greater imbalance. | IV.C.ii AV Septal Defects, p. 712; Figure 24, pp. 712-713 |
| AS23-255 | ai-extracted | When the common atrioventricular valve area over each ventricle is measured in a parasagittal view in diastole, an atrioventricular valve index of about 2:1 or higher suggests that single-ventricle palliation will be needed; the threshold depends on which equation is used to calculate the index. | IV.C.ii AV Septal Defects, p. 712; Figure 23, p. 713 |
| AS23-256 | ai-cross-checked | In atrioventricular septal defect, valve regurgitation should be assessed with colour Doppler. | IV.C.ii General Imaging Approach, p. 712; Table 13, common AV valve, p. 706 |
| AS23-257 | ai-extracted | In atrioventricular septal defect, the outflow tracts should be assessed for obstruction from the conal septum, from subvalvular fibrous tissue, or from the atrioventricular valve or its accessory tissue. | IV.C.ii AV Septal Defects, p. 712 |
| AS23-258 | ai-cross-checked | A common atrioventricular valve is suspected when the crux lacks offset or the atrioventricular valves appear at the same level, with large atrial or ventricular septal defects. | Table 13 (lesion-specific evaluation), p. 706 |
| AS23-259 | ai-cross-checked | A common atrioventricular valve often accompanies bilateral superior venae cavae, an interrupted inferior vena cava or total anomalous pulmonary venous return. | Table 13 (lesion-specific evaluation), p. 706 |
| AS23-260 | ai-cross-checked | With a common atrioventricular valve, additional ventricular septal defects may be missed unless specifically looked for. | Table 13 (lesion-specific evaluation), p. 706 |
| AS23-268 | ai-cross-checked | With straddling valves, if the left atrioventricular valve is hypoplastic the fetus is at risk of left atrial hypertension. | Table 13 (lesion-specific evaluation), straddling valves row, p. 706 |
| AS23-270 | ai-cross-checked | In a straddling atrioventricular valve, chordae pass through a ventricular septal defect and attach in the opposite ventricle. | IV.C.ii Straddling/Overriding AV Valves and Crisscross Heart, pp. 712-713 |
| AS23-271 | ai-cross-checked | In an overriding atrioventricular valve, the annulus sits over the ventricular septum and opens into both ventricles. | IV.C.ii Straddling/Overriding AV Valves and Crisscross Heart, pp. 712-713 |
| AS23-272 | ai-extracted | In a crisscross ('twisted') atrioventricular connection the two valve apparatuses cross, usually so that the atrium on the right opens into the left-sided ventricle and the atrium on the left into the right-sided ventricle; looping may give either atrioventricular concordance or discordance. | IV.C.ii Straddling/Overriding AV Valves and Crisscross Heart, pp. 712-713 |
| AS23-273 | ai-cross-checked | A complex atrioventricular junction is suspected when the four-chamber view does not show two separate atrioventricular valves with offset at the crux. | Table 13 (lesion-specific evaluation), p. 706 |
| AS23-274 | ai-cross-checked | Foreshortening in a crisscross heart can cause confusion between one and two ventricles. | Table 13 (lesion-specific evaluation), p. 706 |
| AS23-275 | ai-cross-checked | Atrioventricular valves in complex connections should be imaged with combined two-dimensional, colour and pulsed-wave Doppler from multiple views. | IV.C.ii Straddling/Overriding AV Valves and Crisscross Heart, pp. 712-713; Figure 25 |
| AS23-277 | ai-cross-checked | A straddling or overriding atrioventricular valve may make closure of the ventricular septal defect impossible and may require a single-ventricle approach. | IV.C.ii Straddling/Overriding AV Valves and Crisscross Heart, pp. 712-713 |
| AS23-278 | ai-cross-checked | The anatomy of straddling valves is shown better with video clips and live scanning than with still images. | Figure 25 caption, p. 714 |
| AS23-280 | ai-cross-checked | Straddling can be associated with D- or L-looped ventricles and a risk of heart block. | Table 13 (lesion-specific evaluation), p. 706 |
| AS23-285 | ai-cross-checked | Reduction in size of a ventricular septal defect, with less severe or resolved disease, usually occurs with simple isolated ventricular or muscular defects but can occur in other heart disease. | Table 14 (mechanisms and patterns of progression), pp. 710-711 |

---
## Unit XB8

### Unit file

```yaml
# Unit XB8. Every text block and drill lists the claim IDs it rests on.
# Built only from ai-cross-checked claims (ASE 2023, extracted by Claude, cross-checked by
# ChatGPT on 19 Nov 2026). Hypoplastic left heart syndrome is taught in detail in XB2;
# this unit covers the single-ventricle examination as a whole.
# Diagnose tier: needs the cardiology co-editor before release.

id: XB8
title: "Lesion atlas: univentricular hearts"
tier: Diagnose
version: 0.1
summary: "The complete examination of a suspected single ventricle, segment by segment, and the findings that decide ductal dependence, surgery and prognosis."
drafted_by: "Claude (Opus 5.5, 21 Nov 2026)"
audited_by: null
signed_by: null

objectives:
  - "Define a univentricular atrioventricular connection and name its forms."
  - "Carry out the segmental examination of a suspected single ventricle."
  - "Name the single most powerful predictor of prostaglandin need after birth."
  - "Recognise tricuspid atresia and double-inlet left ventricle and their main risks."

sections:

  - heading: "What single ventricle means"
    blocks:
      - text: "In a univentricular atrioventricular connection the atria connect completely or mainly to one ventricle. It includes double-inlet left ventricle, single inlet and common inlet."
        claims: [AS23-201]
      - text: "Single ventricle is often detected at routine screening because the four-chamber view is abnormal, and most cases are diagnosed before birth. Suspect it, or ventricular disproportion, when the axial chest view clearly lacks two symmetric ventricles."
        claims: [AS23-200, AS23-225]
      - text: "Hypoplastic left heart syndrome is the most common form, at 0.26 per 1,000 live births; hypoplastic right heart syndrome occurs in 0.22 per 1,000."
        claims: [AS23-203, AS23-204]
      - text: "Treatment is a series of palliative operations ending in a total cavopulmonary (Fontan) connection."
        claims: [AS23-202]

  - heading: "The complete examination"
    blocks:
      - text: "A complete fetal echocardiogram must be done before a reasonable prognosis can be given. Use a segmental approach to find the associated findings that matter."
        claims: [AS23-216, AS23-206]
      - text: "Assess visceroatrial situs, systemic venous connections, the atrioventricular junction, ventricular morphology and function, and heart rate and rhythm."
        claims: [AS23-205]
      - text: "Veins: look for interruption of the inferior vena cava and for bilateral superior venae cavae. Assess the pulmonary venous connections, because anomalous drainage affects the surgical approach and outcome. Venous anatomy is needed for counselling and postnatal planning."
        claims: [AS23-207, AS23-208, AS23-218]
      - text: "Atrioventricular junction: the tricuspid or mitral valve may be hypoplastic or atretic, or a common valve may be unbalanced. Measure valve diameter or area and assess regurgitation with colour Doppler. Significant regurgitation can affect fetal well-being and the outcome of surgery."
        claims: [AS23-209, AS23-219, AS23-210]
      - text: "Outflows: image them thoroughly for orientation, patency, size and flow direction. When the aortic valve is stenotic or atretic, measure the ascending aorta."
        claims: [AS23-211, AS23-212]
      - text: "Ductal dependence: retrograde flow in the aortic or ductal arch is described as perhaps the single most powerful indicator that prostaglandin will be needed after birth."
        claims: [AS23-213]
      - text: "Function and rhythm: function is assessed qualitatively in practice; strain imaging is not routine. Bradyarrhythmias are associated with left atrial isomerism and discordant atrioventricular connections, and that combination carries a poor prognosis and a high risk of death in utero."
        claims: [AS23-215, AS23-214]

  - heading: "Tricuspid atresia"
    blocks:
      - text: "Views: no atrioventricular connection on the right, a small right ventricle and a ventricular septal defect."
        claims: [AS23-226]
      - text: "Measure: the ventricular septal defect, in two orthogonal planes."
        claims: [AS23-228]
      - text: "Evolution: obstruction at the defect can progress and compromise flow to the outflow arising from the right ventricle, leading to pulmonary stenosis or coarctation."
        claims: [AS23-227]

  - heading: "Double-inlet left ventricle"
    blocks:
      - text: "Views: both atrioventricular valves open into the morphological left ventricle; the four-chamber view shows a large ventricular septal defect or no septum."
        claims: [AS23-229]
      - text: "Associations: with L-looped ventricles there is a risk of complete heart block."
        claims: [AS23-230]

  - heading: "Heterotaxy with a single ventricle"
    blocks:
      - text: "Regurgitation of the common atrioventricular valve may progress and can affect prognosis."
        claims: [AS23-517]

missing_claims:
  - "Awaiting re-check after rewording on 21 Nov (round 5, task J): flow direction and restriction at the atrial septum, ductus and isthmus (AS23-217); adequacy of the atrial septal defect when the left valve is hypoplastic in double-inlet left ventricle (AS23-358)."
  - "Heterotaxy and isomerism: recognition and associated lesions - unit XB7; ASE has little on it and a source is needed."
  - "Outcomes of the staged single-ventricle pathway, and what to tell parents - needs a source; unit Z7."
  - "Video outline not yet written."

drills:
  - id: XB8-Q01
    question: "Which defines a univentricular atrioventricular connection?"
    options:
      - "The atria connect completely or mainly to one ventricle"
      - "One great artery arises from both ventricles"
      - "There is a large ventricular septal defect with two normal valves"
      - "One ventricle is slightly smaller than the other"
    answer: 0
    explanation: "Atria connect completely or mainly to one ventricle: double-inlet LV, single inlet and common inlet."
    claims: [AS23-201]

  - id: XB8-Q02
    question: "Single ventricle is suspected at screening. When can a reasonable prognosis be given?"
    options:
      - "After a complete fetal echocardiogram"
      - "Immediately, from the four-chamber view"
      - "Only after birth"
      - "After genetic testing alone"
    answer: 0
    explanation: "A complete fetal echocardiogram must be performed before a reasonable prognosis can be given."
    claims: [AS23-216]

  - id: XB8-Q03
    question: "Single ventricle. Why must the pulmonary veins be traced?"
    options:
      - "Anomalous drainage affects the surgical approach and outcome"
      - "They are always normal, so it confirms the diagnosis"
      - "To measure the fetal heart rate"
      - "They are not assessed in single ventricle"
    answer: 0
    explanation: "Anomalous pulmonary venous drainage affects surgical approach and outcome."
    claims: [AS23-208]

  - id: XB8-Q04
    question: "Which finding is described as perhaps the single most powerful indicator that prostaglandin will be needed after birth?"
    options:
      - "Retrograde flow in the aortic or ductal arch"
      - "A small left atrium"
      - "Mild tricuspid regurgitation"
      - "A right aortic arch"
    answer: 0
    explanation: "Retrograde arch flow is perhaps the single most powerful indicator of prostaglandin need."
    claims: [AS23-213]

  - id: XB8-Q05
    question: "Single ventricle with left atrial isomerism and slow ventricular rate. What does the guideline say about this combination?"
    options:
      - "Poor prognosis and a high risk of death in utero"
      - "No effect on prognosis"
      - "The rate always recovers by term"
      - "It improves surgical outcome"
    answer: 0
    explanation: "Bradyarrhythmias with left atrial isomerism and discordant connections carry a poor prognosis and high risk of fetal death."
    claims: [AS23-214]

  - id: XB8-Q06
    question: "No right atrioventricular connection, a small right ventricle and a VSD. Which lesion, and what can progress?"
    options:
      - "Tricuspid atresia; obstruction at the VSD"
      - "Ebstein anomaly; tricuspid regurgitation"
      - "Pulmonary atresia; ductal constriction"
      - "AVSD; cleft mitral valve"
    answer: 0
    explanation: "These findings suggest tricuspid atresia; obstruction at the VSD can progress, leading to pulmonary stenosis or coarctation."
    claims: [AS23-226, AS23-227]

  - id: XB8-Q07
    question: "Double-inlet left ventricle with L-looped ventricles. Which risk should be watched for?"
    options:
      - "Complete heart block"
      - "Ductal aneurysm"
      - "Pericardial effusion only"
      - "None"
    answer: 0
    explanation: "DILV with L-looping is at risk of complete heart block."
    claims: [AS23-230]

  - id: XB8-Q08
    question: "How is ventricular function usually assessed in single ventricle in practice?"
    options:
      - "Qualitatively; strain imaging is not routine"
      - "Always with strain imaging"
      - "It is not assessed"
      - "By heart rate alone"
    answer: 0
    explanation: "Function is assessed qualitatively in routine practice; strain is not routinely used."
    claims: [AS23-215]

checklist:
  title: "Single ventricle: segmental record"
  items:
    - text: "Situs, systemic veins (IVC interruption, bilateral SVC), pulmonary veins"
      claims: [AS23-205, AS23-207, AS23-208]
    - text: "Atrioventricular valves: diameter or area, regurgitation by colour"
      claims: [AS23-219]
    - text: "Outflows: orientation, patency, size, flow direction; ascending aorta if the aortic valve is abnormal"
      claims: [AS23-211, AS23-212]
    - text: "Arch flow direction recorded (prostaglandin need)"
      claims: [AS23-213]
    - text: "Function (qualitative) and rate and rhythm"
      claims: [AS23-215, AS23-205]
```

### Claims cited (with ledger statement and locator)

| id | status | statement | locator |
|---|---|---|---|
| AS23-200 | ai-cross-checked | Single-ventricle heart disease is often detected at routine screening because of an abnormal four-chamber view, and most cases are diagnosed before birth. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 |
| AS23-201 | ai-cross-checked | A univentricular atrioventricular connection is one in which the atria connect completely or mainly to one ventricle; it includes double-inlet left ventricle, single inlet and common inlet. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 |
| AS23-202 | ai-cross-checked | Single-ventricle heart disease needs a series of palliative operations ending in a total cavopulmonary (Fontan) connection. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 |
| AS23-203 | ai-cross-checked | Hypoplastic left heart syndrome is the most common form of single ventricle, with an incidence of 0.26 per 1,000 live births. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 |
| AS23-204 | ai-cross-checked | Hypoplastic right heart syndrome has an incidence of 0.22 per 1,000 live births. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 |
| AS23-205 | ai-cross-checked | In suspected single ventricle, visceroatrial situs, systemic venous connections, the atrioventricular junction, ventricular morphology and function, and heart rate and rhythm should be assessed. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 |
| AS23-206 | ai-cross-checked | A segmental approach to imaging is recommended in single ventricle to identify important associated findings. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 |
| AS23-207 | ai-cross-checked | In single ventricle, the inferior vena cava should be evaluated for interruption and bilateral superior venae cavae should be looked for. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 (Venous Connections) |
| AS23-208 | ai-cross-checked | In single ventricle, pulmonary venous connections should be assessed, because anomalous drainage affects the surgical approach and outcome. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 (Venous Connections) |
| AS23-209 | ai-cross-checked | In single ventricle the tricuspid or mitral valve may be hypoplastic or atretic, or a common atrioventricular valve may be unbalanced. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 (AV Junctions) |
| AS23-210 | ai-cross-checked | Significant atrioventricular valve regurgitation in single ventricle can affect fetal well-being and postnatal surgical outcome. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 (AV Junctions) |
| AS23-211 | ai-cross-checked | In single ventricle, the outflow tracts should be imaged thoroughly for orientation, patency, size and flow direction. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 (Ventriculoarterial Junction) |
| AS23-212 | ai-cross-checked | When the aortic valve is stenotic or atretic in single ventricle, the ascending aorta diameter should be measured. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 (Ventriculoarterial Junction) |
| AS23-213 | ai-cross-checked | Retrograde flow in the aortic or ductal arch is described as perhaps the single most powerful indicator that prostaglandin will be needed after birth. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 (Ventriculoarterial Junction) |
| AS23-214 | ai-cross-checked | Bradyarrhythmias are associated with left atrial isomerism and discordant atrioventricular connections; the combination carries a poor prognosis and a high risk of death in utero. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 (Rhythm, Function, and Morphology) |
| AS23-215 | ai-cross-checked | In single ventricle, function is assessed qualitatively in practice; strain imaging is not routinely used. | IV.C.i Single Ventricles and Assessment for Ductal Dependence, p. 704 (Rhythm, Function, and Morphology) |
| AS23-216 | ai-cross-checked | A complete fetal echocardiogram must be performed for a suspected single ventricle before a reasonable prognosis can be given. | IV.C.i Key Points, p. 704 |
| AS23-217 | ai-extracted | In single ventricle, the direction of flow and any restriction must be demonstrated at the atrial septum, and at the ductus arteriosus and the aortic isthmus when these are present. | IV.C.i Key Points, p. 704 |
| AS23-218 | ai-cross-checked | In single ventricle, systemic and pulmonary venous anatomy should be imaged, for counselling and postnatal planning. | IV.C.i Key Points, p. 704 |
| AS23-219 | ai-cross-checked | In single ventricle, atrioventricular valve diameter or area should be measured and regurgitation assessed with colour Doppler. | IV.C.i Key Points, p. 704 |
| AS23-225 | ai-cross-checked | Ventricular disproportion or single ventricle is suspected when the axial chest view clearly lacks two symmetric ventricles. | Table 13 (lesion-specific evaluation), category 'SV and ventricular disproportion', p. 705 |
| AS23-226 | ai-cross-checked | Tricuspid atresia is suspected when there is no atrioventricular connection on the right, a small right ventricle and a ventricular septal defect. | Table 13 (lesion-specific evaluation), p. 705 |
| AS23-227 | ai-cross-checked | In tricuspid atresia, obstruction at the ventricular septal defect can be progressive, compromising flow to the outflow tract arising from the right ventricle (leading to pulmonary stenosis or coarctation). | Table 13 (lesion-specific evaluation), p. 705 |
| AS23-228 | ai-cross-checked | Ventricular septal defect dimensions can be measured in two orthogonal planes. | Table 13 (lesion-specific evaluation), tricuspid atresia row, p. 705 |
| AS23-229 | ai-cross-checked | In double-inlet left ventricle both atrioventricular valves open into the morphological left ventricle; the four-chamber view shows a large ventricular septal defect or no ventricular septum. | Table 13 (lesion-specific evaluation), p. 705 |
| AS23-230 | ai-cross-checked | Double-inlet left ventricle with L-looped ventricles is at risk of complete heart block. | Table 13 (lesion-specific evaluation), p. 705 |
| AS23-358 | ai-extracted | In double-inlet left ventricle, if the left atrioventricular valve is hypoplastic or atretic, the adequacy of the atrial septal defect should be assessed. | Table 13, double-inlet LV, other key points, p. 705 |
| AS23-517 | ai-cross-checked | In heterotaxy with atrial isomerism, regurgitation of the common atrioventricular valve may be progressive and can affect prognosis. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |

---
## Unit XB3

### Unit file

```yaml
# Unit XB3. Every text block and drill lists the claim IDs it rests on.
# Built only from ai-cross-checked claims (ASE 2023, extracted by Claude, cross-checked by
# ChatGPT on 19 Nov 2026). Tricuspid atresia is taught in XB8. Claims reworded on 21 Nov
# and awaiting re-check are left out. Diagnose tier: needs the cardiology co-editor.

id: XB3
title: "Lesion atlas: right heart (pulmonary stenosis and atresia, Ebstein anomaly, tricuspid dysplasia)"
tier: Diagnose
version: 0.1
summary: "Right-sided obstruction and right-sided regurgitation: what each looks like, the Doppler that matters, the traps, and how these lesions progress."
drafted_by: "Claude (Opus 5.5, 21 Nov 2026)"
audited_by: null
signed_by: null

objectives:
  - "Describe the four-chamber and three-vessel findings in pulmonary stenosis, including when the four-chamber view looks normal."
  - "Explain what reversed ductal flow means, and how coronary fistulae are looked for."
  - "Name the first clue to Ebstein anomaly or tricuspid dysplasia and the Doppler that separates true from functional pulmonary atresia."
  - "Explain why severe regurgitation leads to cardiomegaly, heart failure and hydrops."

sections:

  - heading: "Pulmonary stenosis and atresia with intact septum"
    blocks:
      - text: "Views: right atrial enlargement and a right ventricle smaller than the left, hypertrophied and with reduced function. The four-chamber view may look normal, with reversed colour flow in the ductus or main pulmonary artery on the three-vessel view."
        claims: [AS23-418]
      - text: "Doppler: increased A-wave reversal in the systemic veins is common. Reversed ductal flow suggests ductal dependence."
        claims: [AS23-419, AS23-420]
      - text: "Measure: the tricuspid annulus and the pulsed-wave inflow duration."
        claims: [AS23-422]
      - text: "Coronary fistulae: pulmonary valve atresia or near-atresia with a small right ventricle can be associated with coronary artery fistulae. Suspect them when low-velocity colour Doppler shows to-and-fro flow in the right ventricular free wall or septum. Tricuspid regurgitation greater than mild on colour Doppler is associated with a low risk of these sinusoids."
        claims: [AS23-421, AS23-448]
      - text: "Follow-up: serial evaluation from the time stenosis is suspected; flow direction in the ductal and aortic arches and at the atrial septum at every study; function of both ventricles."
        claims: [AS23-408, AS23-409, AS23-410, AS23-411]

  - heading: "Ebstein anomaly and tricuspid valve dysplasia"
    blocks:
      - text: "First clue: significant right atrial dilatation, with or without right ventricular dilatation."
        claims: [AS23-424]
      - text: "Views: tricuspid valve anatomy on the four-chamber and short-axis views clarifies the diagnosis."
        claims: [AS23-425]
      - text: "Doppler: pulsed- and continuous-wave Doppler of the regurgitant jet is critical to exclude primary pulmonary obstruction and to gauge right ventricular systolic pressure."
        claims: [AS23-427]
      - text: "Functional pulmonary atresia: in severe tricuspid disease the right ventricle may be unable to exceed systemic pressure and open the pulmonary valve. Structural or functional pulmonary atresia here is always associated with retrograde ductal flow, which can appear at any point, so document ductal flow serially."
        claims: [AS23-428, AS23-429]
      - text: "Measure: the tricuspid annulus and peak tricuspid regurgitation velocity, both listed as predicting progression. Image and measure the branch pulmonary arteries, because their hypoplasia correlates with lung hypoplasia. Assess left ventricular morphology, size and function, because left ventricular dysfunction can cause compromise."
        claims: [AS23-436, AS23-431, AS23-432]
      - text: "Associations and evolution: hypoplasia of the pulmonary valve and main pulmonary artery is common, because right ventricular output is reduced. Look for other defects, including coarctation and ventricular septal defect."
        claims: [AS23-430, AS23-435]
      - text: "Rhythm: assess it, because atrial ectopy and supraventricular tachyarrhythmias are common."
        claims: [AS23-434]

  - heading: "Why severe regurgitation is dangerous"
    blocks:
      - text: "Significant atrioventricular or semilunar regurgitation imposes a volume load that the fetal circulation tolerates poorly, causing progressive cardiomegaly."
        claims: [AS23-438, AS23-441]
      - text: "Severe tricuspid regurgitation with progressive cardiomegaly can evolve into heart failure and hydrops. When both ventricles fail, redistribution of preload is impaired, with haemodynamic instability, raised filling pressures and hydrops."
        claims: [AS23-437, AS23-439]
      - text: "Pulmonary regurgitation with a patent ductus can cause a circular shunt and placental steal."
        claims: [AS23-442]
      - text: "Regurgitation may worsen as pregnancy advances, so follow it serially."
        claims: [AS23-440]

missing_claims:
  - "Awaiting re-check after rewording on 21 Nov (round 5, task J): vena contracta width relative to the annulus (AS23-426); left ventricular mechanics in severe tricuspid disease (AS23-433); ductal anatomy and left pulmonary artery stenosis in pulmonary stenosis (AS23-361, new); gradients not indicating severity (AS23-362, new)."
  - "Displacement of the tricuspid septal leaflet as a measure separating Ebstein anomaly from dysplasia, and outcome scores (for example the Celermajer index) - not in the claims held; needs a source."
  - "Fetal pulmonary valvuloplasty for pulmonary atresia with intact septum - unit Z5."
  - "Video outline not yet written."

drills:
  - id: XB3-Q01
    question: "The four-chamber view looks normal, but the three-vessel view shows reversed flow in the ductus. Which lesion should you consider?"
    options:
      - "Pulmonary stenosis or atresia"
      - "Coarctation"
      - "Normal finding at mid-trimester"
      - "Ductal aneurysm"
    answer: 0
    explanation: "In pulmonary stenosis the four-chamber view may look normal while reversed colour flow is seen in the ductus or main PA."
    claims: [AS23-418]

  - id: XB3-Q02
    question: "What does reversed ductal flow suggest in pulmonary stenosis?"
    options:
      - "Ductal dependence"
      - "Mild disease that needs no follow-up"
      - "Ductal constriction"
      - "A normal transition"
    answer: 0
    explanation: "Reversed ductal flow suggests ductal dependence."
    claims: [AS23-420]

  - id: XB3-Q03
    question: "Pulmonary atresia with a small right ventricle. How do you look for coronary fistulae?"
    options:
      - "Low-velocity colour Doppler for to-and-fro flow in the right ventricular free wall or septum"
      - "High-velocity colour scale on the aortic arch"
      - "M-mode of the left ventricle"
      - "They cannot be seen before birth"
    answer: 0
    explanation: "Fistulae are suspected when low-velocity colour shows to-and-fro flow in the RV free wall or septum."
    claims: [AS23-421]

  - id: XB3-Q04
    question: "Pulmonary stenosis with more than mild tricuspid regurgitation on colour. What does this suggest about sinusoids?"
    options:
      - "A low risk of sinusoids"
      - "A high risk of sinusoids"
      - "Sinusoids are certain"
      - "No relation"
    answer: 0
    explanation: "Tricuspid regurgitation greater than mild is associated with a low risk of sinusoids."
    claims: [AS23-448]

  - id: XB3-Q05
    question: "What is the first clue to Ebstein anomaly or tricuspid dysplasia?"
    options:
      - "Significant right atrial dilatation"
      - "A small left ventricle"
      - "A right aortic arch"
      - "Pericardial effusion"
    answer: 0
    explanation: "Significant right atrial dilatation, with or without RV dilatation, is the first clue."
    claims: [AS23-424]

  - id: XB3-Q06
    question: "Severe tricuspid regurgitation; the pulmonary valve does not seem to open. Why is Doppler of the regurgitant jet critical?"
    options:
      - "To exclude primary pulmonary obstruction and gauge right ventricular pressure"
      - "To measure the heart rate"
      - "To confirm that the valve is normal"
      - "It is not useful here"
    answer: 0
    explanation: "PW and CW Doppler of the TR jet exclude primary pulmonary obstruction and show whether the RV can generate pressure; the RV may fail to open the valve (functional atresia)."
    claims: [AS23-427, AS23-428]

  - id: XB3-Q07
    question: "Severe tricuspid disease with pulmonary atresia, structural or functional. Which ductal finding is always present?"
    options:
      - "Retrograde ductal flow"
      - "Antegrade ductal flow"
      - "Ductal aneurysm"
      - "Absent ductus"
    answer: 0
    explanation: "It is always associated with retrograde ductal flow, which can develop at any point and must be documented serially."
    claims: [AS23-429]

  - id: XB3-Q08
    question: "Ebstein anomaly. Why measure the branch pulmonary arteries?"
    options:
      - "Their hypoplasia correlates with lung hypoplasia"
      - "To estimate gestational age"
      - "To predict heart block"
      - "They are not measured"
    answer: 0
    explanation: "Branch PA hypoplasia correlates with lung hypoplasia."
    claims: [AS23-431]

  - id: XB3-Q09
    question: "Ebstein anomaly. Which rhythm problems are common?"
    options:
      - "Atrial ectopy and supraventricular tachyarrhythmias"
      - "Complete heart block in every case"
      - "None"
      - "Ventricular fibrillation"
    answer: 0
    explanation: "Atrial ectopy and supraventricular tachyarrhythmias are common, so rhythm should be assessed."
    claims: [AS23-434]

  - id: XB3-Q10
    question: "Pulmonary regurgitation with a patent ductus. What can result?"
    options:
      - "A circular shunt and placental steal"
      - "Ductal closure"
      - "Improved cardiac output"
      - "Coarctation"
    answer: 0
    explanation: "This combination can cause a circular shunt and placental steal."
    claims: [AS23-442]

checklist:
  title: "Right heart lesion: each study"
  items:
    - text: "Ductal flow direction documented"
      claims: [AS23-409, AS23-429]
    - text: "Atrial septal flow direction documented"
      claims: [AS23-410]
    - text: "Tricuspid annulus; tricuspid regurgitation velocity by PW and CW"
      claims: [AS23-422, AS23-436, AS23-427]
    - text: "Branch pulmonary arteries measured"
      claims: [AS23-431]
    - text: "Left ventricle: size and function; both ventricles' function"
      claims: [AS23-432, AS23-411]
    - text: "Heart size and signs of hydrops; rhythm"
      claims: [AS23-437, AS23-434]
    - text: "Pulmonary atresia with small RV: low-velocity colour for fistulae"
      claims: [AS23-421]
```

### Claims cited (with ledger statement and locator)

| id | status | statement | locator |
|---|---|---|---|
| AS23-361 | ai-extracted | Outflow imaging in pulmonary stenosis includes the ductal anatomy; left pulmonary artery stenosis can result from abnormal ductal insertion. | Table 13, pulmonary stenosis, outflow imaging, p. 708 |
| AS23-362 | ai-extracted | In semilunar valve stenosis, Doppler pressure gradients may be measured and reported, but they do not necessarily indicate how severe the stenosis is. | IV.C.iv Semilunar Valve Obstruction, Key Points, p. 716 |
| AS23-408 | ai-cross-checked | Serial evaluation should be performed when valve stenosis is suspected, including ventricular size and function and endocardial fibroelastosis. | IV.C.iv Key Points (semilunar obstruction), p. 716 |
| AS23-409 | ai-cross-checked | Ductal and aortic arch flow direction must be documented at every examination; abnormal direction heralds critical obstruction after birth. | IV.C.iv Key Points (semilunar obstruction), p. 716 |
| AS23-410 | ai-cross-checked | Atrial septal flow direction must be documented at every examination when semilunar valve stenosis is present. | IV.C.iv Key Points (semilunar obstruction), p. 716 |
| AS23-411 | ai-cross-checked | Evaluation of both ventricles' function is recommended in aortic and pulmonary stenosis. | IV.C.iv Key Points (semilunar obstruction), p. 716 |
| AS23-418 | ai-cross-checked | Pulmonary stenosis may show right atrial enlargement and a right ventricle smaller than the left, hypertrophied and with reduced function, but the four-chamber view may look normal; reversed colour flow in the ductus or main pulmonary artery may be seen on the three-vessel view. | Table 13 (lesion-specific evaluation), p. 708 |
| AS23-419 | ai-cross-checked | In pulmonary stenosis, increased A-wave reversal in the systemic veins is common. | Table 13 (lesion-specific evaluation), p. 708 |
| AS23-420 | ai-cross-checked | Reversed ductal flow suggests ductal dependence. | Table 13 (lesion-specific evaluation), pulmonary stenosis row, p. 708 |
| AS23-421 | ai-cross-checked | Pulmonary valve atresia or near-atresia with a small right ventricle can be associated with coronary artery fistulae, suspected when to-and-fro flow is seen in the right ventricular free wall or septum with low-velocity colour Doppler. | IV.C.iv Semilunar Valve Obstruction with an Intact Ventricular Septum, p. 716; Table 13, pulmonary stenosis, other key points, p. 708 |
| AS23-422 | ai-cross-checked | In pulmonary stenosis, tricuspid annulus dimension and pulsed-wave inflow duration are listed as key measurements. | Table 13 (lesion-specific evaluation), p. 708 |
| AS23-424 | ai-cross-checked | Significant right atrial dilatation, with or without right ventricular dilatation, is the first clue to Ebstein anomaly or tricuspid valve dysplasia. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-425 | ai-cross-checked | Tricuspid valve anatomy on the four-chamber and short-axis views clarifies the diagnosis of Ebstein anomaly or tricuspid dysplasia. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-426 | ai-extracted | Tricuspid regurgitation severity can be assessed by measuring the width of the vena contracta relative to the valve annulus. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-427 | ai-cross-checked | Pulsed- and continuous-wave Doppler of the tricuspid regurgitant jet is critical to exclude primary pulmonary obstruction and to gauge right ventricular systolic pressure. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-428 | ai-cross-checked | In severe tricuspid disease, the right ventricle may be unable to exceed systemic pressure and open the pulmonary valve (functional pulmonary atresia). | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-429 | ai-cross-checked | Structural or functional pulmonary atresia in severe tricuspid disease is always associated with retrograde ductal flow, which can develop at any point and must be documented serially. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-430 | ai-cross-checked | In Ebstein anomaly or tricuspid dysplasia, hypoplasia of the pulmonary valve and main pulmonary artery is common because right ventricular output is reduced. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-431 | ai-cross-checked | Branch pulmonary arteries should be imaged and measured, because their hypoplasia correlates with lung hypoplasia. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-432 | ai-cross-checked | Left ventricular morphology, size and function should be assessed, because left ventricular dysfunction can cause compromise. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-433 | ai-extracted | In severe tricuspid valve disease, failure of left ventricular radial displacement to augment, reduced circumferential strain and left ventricular dyssynchrony are key features, probably reflecting ventricular interaction; these methods are still considered investigational. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-434 | ai-cross-checked | Rhythm should be assessed in Ebstein anomaly and tricuspid dysplasia, because atrial ectopy and supraventricular tachyarrhythmias are common. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-435 | ai-cross-checked | Other defects, including coarctation and ventricular septal defect, should be looked for in Ebstein anomaly and tricuspid dysplasia. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-436 | ai-cross-checked | Tricuspid annulus dimension and peak tricuspid regurgitation velocity are listed as predictive of progression. | Table 13 (lesion-specific evaluation), p. 708 |
| AS23-437 | ai-cross-checked | Severe tricuspid regurgitation with progressive cardiomegaly can evolve into heart failure and hydrops. | Figure 29 caption, p. 718 |
| AS23-438 | ai-cross-checked | Significant atrioventricular or semilunar regurgitation imposes a volume load that the fetal circulation tolerates poorly, causing progressive cardiomegaly. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-439 | ai-cross-checked | Dysfunction of both ventricles can impair redistribution of preload, leading to haemodynamic instability, raised filling pressures and hydrops. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-440 | ai-cross-checked | Valve regurgitation should be followed serially, because it may worsen with advancing gestation. | IV.C.iv Key Points (regurgitation), p. 717 |
| AS23-441 | ai-cross-checked | Progressive cardiomegaly is common with significant atrioventricular or semilunar regurgitation. | IV.C.iv Key Points (regurgitation), p. 717 |
| AS23-442 | ai-cross-checked | Pulmonary regurgitation with a patent ductus arteriosus can cause a circular shunt and placental steal. | Table 14 (mechanisms and patterns of progression), pp. 710-711 |
| AS23-448 | ai-cross-checked | In pulmonary stenosis, tricuspid regurgitation greater than mild on colour Doppler is associated with a low risk of sinusoids. | Table 13, pulmonary stenosis row, p. 708 |

---
## Unit XB5

### Unit file

```yaml
# Unit XB5. Every text block and drill lists the claim IDs it rests on.
# Built only from ai-cross-checked claims (ASE 2023, extracted by Claude, cross-checked by
# ChatGPT on 19 Nov 2026). Coarctation is taught in XB2. Diagnose tier: needs the
# cardiology co-editor before release.

id: XB5
title: "Lesion atlas: arch and vessels (right arch, double arch, aberrant subclavian, ductus)"
tier: Diagnose
version: 0.1
summary: "Reading the three-vessel-and-trachea view: the normal V, the signs of rings, slings and right arch, and the two ductal problems - aneurysm and constriction."
drafted_by: "Claude (Opus 5.5, 21 Nov 2026)"
audited_by: null
signed_by: null

objectives:
  - "Describe the normal three-vessel-and-trachea view and the four signs that should prompt a closer look."
  - "Recognise the U sign of a vascular ring and say what must then be excluded."
  - "State why vascular rings and slings matter for delivery planning."
  - "Tell a ductal aneurysm from ductal constriction and give the consequences of each."

sections:

  - heading: "The normal view and the warning signs"
    blocks:
      - text: "On the normal three-vessel-and-trachea view, two arches of similar size form a V to the left of the trachea."
        claims: [AS23-500]
      - text: "Use this view to assess vascular anatomy: vascular rings, slings and right aortic arch are readily detected on it. Arch abnormalities are suspected when the three-vessel or three-vessel-and-trachea view is abnormal."
        claims: [AS23-510, AS23-357]
      - text: "Four signs should prompt evaluation for coarctation, ductal aneurysm, right aortic arch or vascular ring: a size mismatch between the arches, abnormal flow, a U shape, or separation of the superior vena cava from the trachea."
        claims: [AS23-502]
      - text: "Trace the ductal and aortic arches and the origins of the head and neck vessels with axial, sagittal and parasagittal two-dimensional and colour imaging."
        claims: [AS23-501]

  - heading: "Vascular rings and double aortic arch"
    blocks:
      - text: "Key sign: a U shape around the trachea and oesophagus, instead of a V."
        claims: [AS23-503]
      - text: "Next step: exclude aberrant subclavian arteries and a double aortic arch."
        claims: [AS23-504]
      - text: "Double aortic arch: colour Doppler shows two arches encircling the trachea and oesophagus, with the innominate vein passing in front of both. Colour and power Doppler can show retrograde and antegrade flow in the smaller arch."
        claims: [AS23-508, AS23-507]
      - text: "Associations: a vascular ring carries an increased risk of tracheal anomalies, including complete tracheal rings."
        claims: [AS23-505]

  - heading: "Aberrant subclavian artery and pulmonary artery sling"
    blocks:
      - text: "Attempt to diagnose an aberrant subclavian artery, especially when the side of the arch is abnormal. An isolated aberrant right subclavian artery runs behind the oesophagus and is seen more clearly with colour Doppler."
        claims: [AS23-511, AS23-509]
      - text: "A pulmonary artery sling is not a vascular ring, but it may coexist with airway abnormalities. Delivery should be where assisted ventilation is available if needed."
        claims: [AS23-506]

  - heading: "Ductal aneurysm"
    blocks:
      - text: "Views: a pulsatile, tortuous duct late in gestation, on the three-vessel, three-vessel-and-trachea or sagittal arch views. Measure it at its widest."
        claims: [AS23-512, AS23-513]
      - text: "Course: it occurs at 35-40 weeks in 1%-2% of fetuses and mostly closes spontaneously, with a low risk of rupture or compression. It is generally a normal variant with no consequence for the newborn, but it is associated with connective tissue disorders."
        claims: [AS23-514, AS23-513]

  - heading: "Ductal constriction"
    blocks:
      - text: "Causes: it occurs in isolation and is associated with cyclo-oxygenase inhibitors (non-steroidal anti-inflammatory drugs) and certain foods or herbal teas. It rarely occurs with structural heart disease."
        claims: [AS23-515]
      - text: "Consequences: isolated constriction can lead to right heart failure, hydrops, and persistent pulmonary hypertension after birth. In critical heart disease it can be lethal, with transposition at higher risk."
        claims: [AS23-516, AS23-332]

  - heading: "Veins seen alongside arch and other lesions"
    blocks:
      - text: "A left superior vena cava draining to the coronary sinus is listed as a common venous variation with coarctation."
        claims: [AS23-519]

missing_claims:
  - "Awaiting re-check after rewording on 21 Nov (round 5, task J): arch sidedness and branching pattern in outflow lesions (AS23-307)."
  - "Right aortic arch: mirror-image against aberrant left subclavian branching, the L shape, and the association with 22q11 deletion and with intracardiac disease - needs a source (the checker's suggested Figure 30F claim was not found in the caption)."
  - "How to report an isolated right arch or aberrant subclavian artery, and whether genetic testing is offered - needs a source and the co-editor."
  - "Systemic and pulmonary venous anomalies are planned for unit XB6; ASE has little on veins."
  - "Video outline not yet written."

drills:
  - id: XB5-Q01
    question: "What does the normal three-vessel-and-trachea view show?"
    options:
      - "Two arches of similar size forming a V to the left of the trachea"
      - "Two arches forming a U around the trachea"
      - "A single arch to the right of the trachea"
      - "Three arches side by side"
    answer: 0
    explanation: "Normally the ductal and aortic arches form a V to the left of the trachea."
    claims: [AS23-500]

  - id: XB5-Q02
    question: "The arches form a U around the trachea and oesophagus. What is this the key sign of?"
    options:
      - "A vascular ring"
      - "A normal heart"
      - "Ductal constriction"
      - "Tetralogy of Fallot"
    answer: 0
    explanation: "A U shape instead of a V is the key sign of a vascular ring."
    claims: [AS23-503]

  - id: XB5-Q03
    question: "A vascular ring is suspected. What must then be excluded?"
    options:
      - "Aberrant subclavian arteries and a double aortic arch"
      - "Coarctation only"
      - "Heart block"
      - "Nothing; the diagnosis is complete"
    answer: 0
    explanation: "With a suspected vascular ring, aberrant subclavian arteries and a double arch should be excluded."
    claims: [AS23-504]

  - id: XB5-Q04
    question: "Why does a vascular ring matter for the newborn?"
    options:
      - "It carries an increased risk of tracheal anomalies, including complete tracheal rings"
      - "It always needs surgery on the first day"
      - "It causes heart failure before birth"
      - "It has no consequence"
    answer: 0
    explanation: "A vascular ring carries an increased risk of tracheal anomalies."
    claims: [AS23-505]

  - id: XB5-Q05
    question: "A pulmonary artery sling is diagnosed. Where should the baby be delivered?"
    options:
      - "Where assisted ventilation is available if needed"
      - "At home"
      - "Anywhere; a sling has no airway relevance"
      - "Only where fetal surgery is possible"
    answer: 0
    explanation: "A sling may coexist with airway abnormalities; delivery should be where assisted ventilation is available."
    claims: [AS23-506]

  - id: XB5-Q06
    question: "Which tool shows an aberrant right subclavian artery behind the oesophagus more clearly?"
    options:
      - "Colour Doppler"
      - "M-mode"
      - "Grey scale at high gain"
      - "Pulsed-wave Doppler of the umbilical artery"
    answer: 0
    explanation: "An isolated aberrant right subclavian artery is seen more clearly with colour Doppler."
    claims: [AS23-509]

  - id: XB5-Q07
    question: "A pulsatile, tortuous duct is seen at 37 weeks. What is the usual course?"
    options:
      - "It mostly closes spontaneously, with a low risk of rupture or compression"
      - "It always ruptures"
      - "It needs delivery within a day"
      - "It always causes hydrops"
    answer: 0
    explanation: "Ductal aneurysm mostly closes spontaneously with low risk, though it is associated with connective tissue disorders."
    claims: [AS23-514]

  - id: XB5-Q08
    question: "Isolated ductal constriction is found. Which history should you ask about?"
    options:
      - "Non-steroidal anti-inflammatory drugs and certain foods or herbal teas"
      - "Paternal age"
      - "Previous caesarean section"
      - "Maternal height"
    answer: 0
    explanation: "Constriction is associated with cyclo-oxygenase inhibitors and certain foods or herbal teas."
    claims: [AS23-515]

  - id: XB5-Q09
    question: "What can isolated ductal constriction lead to?"
    options:
      - "Right heart failure, hydrops, and persistent pulmonary hypertension after birth"
      - "Left heart hypoplasia"
      - "Complete heart block"
      - "Nothing; it is harmless"
    answer: 0
    explanation: "Isolated constriction can lead to right heart failure, hydrops and PPHN."
    claims: [AS23-516]

checklist:
  title: "Arch and ductus: minimum record"
  items:
    - text: "Three-vessel-and-trachea view: V or not; arch sizes and flow; SVC position against the trachea"
      claims: [AS23-500, AS23-502, AS23-510]
    - text: "Arches and head and neck vessels traced in axial, sagittal and parasagittal planes with colour"
      claims: [AS23-501]
    - text: "U sign: aberrant subclavian and double arch excluded"
      claims: [AS23-503, AS23-504]
    - text: "Aberrant subclavian looked for when arch sidedness is abnormal"
      claims: [AS23-511]
    - text: "Ring or sling: airway risk passed on to the delivery plan"
      claims: [AS23-505, AS23-506]
    - text: "Ductal aneurysm measured at its widest; constriction: drug and diet history"
      claims: [AS23-513, AS23-515]
```

### Claims cited (with ledger statement and locator)

| id | status | statement | locator |
|---|---|---|---|
| AS23-307 | ai-extracted | Aortic arch sidedness must be documented at least once in pregnancy, and an attempt made to define the branching pattern, especially when the aortic and ductal arches are on opposite sides of the trachea. | IV.C.iii Key Points, p. 715 |
| AS23-332 | ai-cross-checked | Constriction of the ductus arteriosus can be lethal in critical heart disease, with transposition at higher risk. | Table 14 (mechanisms and patterns of progression), pp. 710-711 |
| AS23-357 | ai-cross-checked | Arch abnormalities are suspected when the three-vessel or three-vessel-and-trachea view is abnormal. | Table 13, category heading, p. 709 |
| AS23-500 | ai-cross-checked | On the normal three-vessel-and-trachea view, two arches of similar size form a V to the left of the trachea. | IV.C.v Isolated Arch Abnormalities, p. 717; Figure 30A |
| AS23-501 | ai-cross-checked | Axial, sagittal and parasagittal two-dimensional and colour imaging should trace the ductal and aortic arches and the origins of the head and neck vessels. | IV.C.v Isolated Arch Abnormalities, p. 717 |
| AS23-502 | ai-cross-checked | A size mismatch between arches, abnormal flow, a U shape, or separation of the superior vena cava from the trachea should prompt evaluation for coarctation, ductal aneurysm, right aortic arch or vascular ring. | IV.C.v Isolated Arch Abnormalities, p. 717 |
| AS23-503 | ai-cross-checked | On the three-vessel-and-trachea view, a U shape around the trachea and oesophagus, instead of a V, is the key sign of a vascular ring. | Table 13 (lesion-specific evaluation), p. 709 |
| AS23-504 | ai-cross-checked | With a suspected vascular ring, aberrant subclavian arteries and a double aortic arch should be excluded. | Table 13 (lesion-specific evaluation), p. 709 |
| AS23-505 | ai-cross-checked | A vascular ring carries an increased risk of tracheal anomalies, including complete tracheal rings. | Table 13 (lesion-specific evaluation), p. 709 |
| AS23-506 | ai-cross-checked | A pulmonary artery sling is not a vascular ring but may coexist with airway abnormalities; delivery should be where assisted ventilation is available if needed. | IV.C.v Isolated Arch Abnormalities, p. 717 |
| AS23-507 | ai-cross-checked | Colour and power Doppler on the three-vessel-and-trachea view can show retrograde and antegrade flow in the smaller arch of a double arch. | IV.C.v Isolated Arch Abnormalities, p. 717 |
| AS23-508 | ai-cross-checked | In double aortic arch, colour Doppler shows two arches encircling the trachea and oesophagus, with the innominate vein passing in front of both. | Figure 30G caption, p. 718 |
| AS23-509 | ai-cross-checked | An isolated aberrant right subclavian artery running behind the oesophagus is seen more clearly with colour Doppler. | Figure 30C caption, p. 718 |
| AS23-510 | ai-cross-checked | The three-vessel-and-trachea view should be used to assess vascular anatomy, because vascular rings, slings and right aortic arch are readily detectable on it. | IV.C.v Isolated Arch Abnormalities, Key Points, p. 718 |
| AS23-511 | ai-cross-checked | Attempts should be made to diagnose an aberrant subclavian artery, especially when an abnormality of arch sidedness is suspected. | IV.C.v Isolated Arch Abnormalities, Key Points, p. 718 |
| AS23-512 | ai-cross-checked | A ductal aneurysm appears late in gestation as a pulsatile, tortuous duct on the three-vessel, three-vessel-and-trachea or sagittal arch views. | Table 13 (lesion-specific evaluation), p. 709 |
| AS23-513 | ai-cross-checked | A ductal aneurysm should be measured at its widest; it is generally a normal variant with no clinical consequence in the newborn. | Table 13 (lesion-specific evaluation), p. 709 |
| AS23-514 | ai-cross-checked | Ductal aneurysm occurs at 35-40 weeks in 1%-2% of fetuses, mostly closes spontaneously with a low risk of rupture or compression, and is associated with connective tissue disorders. | Table 14 (mechanisms and patterns of progression), pp. 710-711 |
| AS23-515 | ai-cross-checked | Ductal constriction occurs in isolation and is associated with cyclo-oxygenase inhibitors (non-steroidal anti-inflammatory drugs) and certain foods or herbal teas; it rarely occurs with structural heart disease. | Table 14 (mechanisms and patterns of progression), pp. 710-711 |
| AS23-516 | ai-cross-checked | Isolated ductal constriction can lead to right heart failure, hydrops and persistent pulmonary hypertension after birth. | Table 14 (mechanisms and patterns of progression), pp. 710-711 |
| AS23-519 | ai-cross-checked | A left superior vena cava draining to the coronary sinus is listed as a common venous variation with coarctation. | Table 13 (lesion-specific evaluation), p. 709 |

---
## Unit XA6

### Unit file

```yaml
# Unit XA6. Every text block and drill lists the claim IDs it rests on.
# Built only from ai-cross-checked claims (ASE 2023). This first version covers what to
# measure and how measurements are expressed; it gives no normal values, because no
# Z-score source has been chosen yet (tasks/results/task-s1.md, topic 4).
# Diagnose tier: needs the cardiology co-editor before release.

id: XA6
title: "Biometry and Z-scores"
tier: Diagnose
version: 0.1
summary: "Which cardiac measurements a complete study requires, which are optional, how they are timed, and why they are expressed as Z-scores."
drafted_by: "Claude (Opus 5.5, 21 Nov 2026)"
audited_by: null
signed_by: null

objectives:
  - "List the measurements a complete fetal echocardiogram requires."
  - "Name the optional measurements and the phase of the cycle each is taken in."
  - "Explain what a Z-score is and why the equation used must be stated."
  - "Say when measurements beyond the standard list are needed."

sections:

  - heading: "Required in every study"
    blocks:
      - text: "Fetal heart rate and rhythm should be documented in every fetal echocardiogram, alongside the valve annulus measurements."
        claims: [AS23-150]
      - text: "A complete study requires a measured cardiothoracic area ratio. The guideline's measurement table lists the cardiothoracic ratio as required, and as prognostic in twin-twin transfusion, anaemia, sacrococcygeal teratoma, CPAM and congenital high airway obstruction."
        claims: [AS23-044, AS23-167]
      - text: "The cardiac axis must be assessed in two dimensions; measuring the angle is optional."
        claims: [AS23-043]
      - text: "Compare the measurements made in every study with published or internal normal values."
        claims: [AS23-155]

  - heading: "Optional measurements and their timing"
    blocks:
      - text: "Optional measurements listed in the guideline, with where and when each is taken."
        claims: [AS23-157, AS23-158, AS23-159, AS23-160, AS23-161, AS23-162, AS23-163, AS23-164, AS23-165, AS23-166]
        table:
          columns: ["Measurement", "View or method", "Phase"]
          rows:
            - ["Right and left ventricular length", "Four-chamber view", "Diastole"]
            - ["Transverse atrial dimensions", "-", "-"]
            - ["Main pulmonary artery", "Proximal to the bifurcation", "Systole"]
            - ["Branch pulmonary arteries", "-", "Systole"]
            - ["Ascending aorta", "-", "Systole"]
            - ["Transverse arch against ductal arch; isthmus against distal ductus", "Long axis of the arch or three-vessel-and-trachea view", "Systole"]
            - ["Free wall and septal thickness", "Low short-axis view", "Diastole"]
            - ["Ventricular dimensions", "Low short-axis view", "Diastole; add systole if function is a concern"]
            - ["Ventricular volumes and ejection fraction", "-", "-"]
            - ["Combined cardiac output, indexed to estimated fetal weight", "Vessel area, velocity-time integral and heart rate", "-"]
      - text: "Aortic and pulmonary annuli are listed as measured at end-diastole or early systole, with the valve open or closed."
        claims: [AS23-168]

  - heading: "Measurements for specific lesions"
    blocks:
      - text: "Additional cardiac and vessel measurements should be made for specific structural defects. Optional measurements, especially when an abnormality is found, are not limited to the standard list. The lesion units (XB1 to XB8) give the measurements listed for each lesion."
        claims: [AS23-151, AS23-156]

  - heading: "Z-scores"
    blocks:
      - text: "Fetal cardiac measurements are usually converted to Z-scores: the deviation from the mean in standard deviations, adjusted for gestational age."
        claims: [AS23-152]
      - text: "Several published Z-score equations exist. Some use biparietal diameter and femur length instead of gestational age. The guideline tabulates them with their strengths and weaknesses."
        claims: [AS23-153, AS23-154]

missing_claims:
  - "The Z-score source the course will teach and its normal values for each structure - the editor to choose (tasks/results/task-s1.md, topic 4)."
  - "Required annulus measurements and their timing (AS23-068, AS23-069) are not yet cross-checked (task H was not applied); and the guideline is inconsistent on semilunar annulus timing (flagged 17 Nov). The co-editor to decide what the course teaches."
  - "Whether reports must name the Z-score equation used - a sensible practice but not a claim held; the co-editor to decide. (The equation-dependent valve index threshold, AS23-255, is awaiting re-check.)"
  - "How to measure each structure step by step, with images - needs a source and the editor's own clips."
  - "Video outline not yet written."

drills:
  - id: XA6-Q01
    question: "Which of these is required in every complete fetal echocardiogram?"
    options:
      - "A measured cardiothoracic area ratio"
      - "Ventricular volumes and ejection fraction"
      - "Combined cardiac output"
      - "Free wall thickness"
    answer: 0
    explanation: "A complete study requires a measured cardiothoracic area ratio; the others are optional."
    claims: [AS23-044, AS23-167]

  - id: XA6-Q02
    question: "The cardiac axis. What must be done, and what is optional?"
    options:
      - "Assess it in two dimensions; measuring the angle is optional"
      - "Measure the angle in every study; assessment is optional"
      - "Neither is needed in a complete study"
      - "Only colour Doppler is required"
    answer: 0
    explanation: "Axis must be assessed in 2D; measuring the angle is optional."
    claims: [AS23-043]

  - id: XA6-Q03
    question: "What does a Z-score express?"
    options:
      - "Deviation from the mean in standard deviations, adjusted for gestational age"
      - "The percentage of normal size"
      - "The absolute size in millimetres"
      - "The ratio of left to right"
    answer: 0
    explanation: "A Z-score is the deviation from the mean in SDs, adjusted for gestational age."
    claims: [AS23-152]

  - id: XA6-Q04
    question: "Two centres report different Z-scores for the same measurement. What is one likely reason?"
    options:
      - "Several published equations exist, some based on fetal biometry rather than gestational age"
      - "Z-scores never differ between centres"
      - "Z-scores are not adjusted for gestation"
      - "One centre measured in millimetres"
    answer: 0
    explanation: "Several equations exist, including some using BPD and femur length."
    claims: [AS23-153]

  - id: XA6-Q05
    question: "In which phase are the branch pulmonary arteries and ascending aorta measured?"
    options:
      - "Systole"
      - "Early diastole"
      - "End-diastole only"
      - "Any phase"
    answer: 0
    explanation: "These optional vessel measurements are taken in systole."
    claims: [AS23-160, AS23-161]

  - id: XA6-Q06
    question: "Ventricular dimensions on the low short-axis view. When are systolic measurements added?"
    options:
      - "When function is a concern"
      - "Always"
      - "Never"
      - "Only in twins"
    answer: 0
    explanation: "Dimensions are taken in diastole, with systolic measurements added if function is a concern."
    claims: [AS23-164]

  - id: XA6-Q07
    question: "An abnormality is found. Are you limited to the standard measurement list?"
    options:
      - "No: additional measurements should be made for specific defects"
      - "Yes: only listed measurements may be taken"
      - "Yes, unless the patient asks"
      - "Measurements should stop once an abnormality is found"
    answer: 0
    explanation: "Additional measurements should be made for specific defects; optional ones are not limited to the table."
    claims: [AS23-151, AS23-156]

checklist:
  title: "Biometry in the report"
  items:
    - text: "Heart rate and rhythm documented"
      claims: [AS23-150]
    - text: "Cardiothoracic area ratio measured"
      claims: [AS23-044]
    - text: "Cardiac axis assessed"
      claims: [AS23-043]
    - text: "Measurements compared with published or internal normals"
      claims: [AS23-155]
    - text: "Lesion-specific measurements added"
      claims: [AS23-151]
```

### Claims cited (with ledger statement and locator)

| id | status | statement | locator |
|---|---|---|---|
| AS23-043 | expert-verified | The cardiac axis must be assessed in two dimensions. Measuring the angle is optional. | III.E. Standard Views and Imaging Planes, Table 3, cardiac axis row, p. 686 |
| AS23-044 | expert-verified | A complete study requires a measured cardiac-to-thoracic area ratio. | III.E. Standard Views and Imaging Planes, Table 3, cardiac size row, p. 686; III.F, Table 4, p. 690 |
| AS23-068 | ai-extracted | Measurement of the mitral and tricuspid valve annulus in early diastole is required. | III.F. Cardiac Biometry and Measurement Data, Table 4, p. 690 |
| AS23-069 | ai-extracted | Measurement of the aortic and pulmonary valve annuli is required in a complete study. | III.F. Cardiac Biometry and Measurement Data, p. 689; Table 4, pp. 691–692 |
| AS23-150 | ai-cross-checked | Fetal heart rate and rhythm should be documented in every fetal echocardiogram, alongside the valve annulus measurements. | III.F Cardiac Biometry and Measurement Data, p. 689 |
| AS23-151 | ai-cross-checked | Additional cardiac and vessel measurements should be made for specific structural defects; Table 4 lists them. | III.F Cardiac Biometry and Measurement Data, p. 689 |
| AS23-152 | ai-cross-checked | Fetal cardiac measurements are typically converted to Z-scores, which express the deviation from the mean in standard deviations, adjusted for gestational age. | III.F Cardiac Biometry and Measurement Data, p. 689 |
| AS23-153 | ai-cross-checked | Several published Z-score equations exist; some alternative formulas use biparietal diameter and femur length instead of gestational age. | III.F Cardiac Biometry and Measurement Data, p. 689 |
| AS23-154 | ai-cross-checked | Table 5 lists the published fetal cardiac Z-score equations with their strengths and weaknesses. | Table 5, p. 693; referred to in III.F, p. 689 |
| AS23-155 | ai-cross-checked | Measurements made in every study should be compared with published or internal normal values. | Table 4 (measurements), footnote, p. 692 |
| AS23-156 | ai-cross-checked | Optional measurements, especially when abnormalities are found, are not limited to those listed in Table 4. | Table 4 (measurements), footnote, p. 692 |
| AS23-157 | ai-cross-checked | Right and left ventricular length, measured in diastole on the four-chamber view, is an optional measurement. | Table 4 (measurements), p. 690 |
| AS23-158 | ai-cross-checked | Transverse atrial dimensions are an optional measurement. | Table 4 (measurements), p. 690 |
| AS23-159 | ai-cross-checked | The main pulmonary artery diameter, measured proximal to the bifurcation in systole, is optional. | Table 4 (measurements), p. 691 |
| AS23-160 | ai-cross-checked | Branch pulmonary artery diameters, measured in systole, are optional. | Table 4 (measurements), p. 691 |
| AS23-161 | ai-cross-checked | The ascending aorta diameter, measured in systole, is optional. | Table 4 (measurements), p. 691 |
| AS23-162 | ai-cross-checked | Optional arch measurements, taken in systole from the long axis of the aortic arch or the three-vessel-and-trachea view, compare the transverse aortic arch with the ductal arch and the aortic isthmus with the distal ductus arteriosus. | Table 4 (measurements), p. 691 |
| AS23-163 | ai-cross-checked | Ventricular free wall and septal thickness, measured in diastole on a low short-axis view, are optional. | Table 4 (measurements), p. 692 |
| AS23-164 | ai-cross-checked | Right and left ventricular dimensions are optional measurements taken in diastole on a low short-axis view, with systolic measurements added if function is a concern. | Table 4 (measurements), p. 692 |
| AS23-165 | ai-cross-checked | Right and left ventricular volumes, with ejection fraction, are optional measurements. | Table 4 (measurements), p. 692 |
| AS23-166 | ai-cross-checked | Combined cardiac output (pulmonary plus aortic), indexed to estimated fetal weight, is an optional measurement, calculated from vessel cross-sectional area, velocity-time integral and heart rate. | Table 4 (measurements), p. 692 |
| AS23-167 | ai-cross-checked | The cardiothoracic ratio is a required measurement; it is also prognostic in twin-twin transfusion, anaemia, sacrococcygeal teratoma, CPAM and congenital high airway obstruction. | Table 4, p. 690 |
| AS23-168 | ai-cross-checked | Aortic and pulmonary annuli are listed as measured at end-diastole or early systole, with the valve open or closed. | Table 4, semilunar valve row, p. 691 |
| AS23-255 | ai-extracted | When the common atrioventricular valve area over each ventricle is measured in a parasagittal view in diastole, an atrioventricular valve index of about 2:1 or higher suggests that single-ventricle palliation will be needed; the threshold depends on which equation is used to calculate the index. | IV.C.ii AV Septal Defects, p. 712; Figure 23, p. 713 |

---
## Unit Z3

### Unit file

```yaml
# Unit Z3. Every text block and drill lists the claim IDs it rests on.
# Built only from ai-cross-checked claims. Most rest on the AHA 2014 statement (extracted by
# Claude, cross-checked by ChatGPT on 19 Nov 2026), with ASE 2023 where it speaks. AHA 2014
# is twelve years old; levels of care and timing were written for US practice.
# Decide tier: needs the cardiology co-editor and an Indian perspective before release.
# No drug doses anywhere (Claude task rule 3).

id: Z3
title: "Planning delivery: place, timing, mode, first-hour needs"
tier: Decide
version: 0.1
summary: "Assigning a level of care before birth, choosing where and when to deliver, and the fetal findings that predict trouble in the first hour for each lesion."
drafted_by: "Claude (Opus 5.5, 21 Nov 2026)"
audited_by: null
signed_by: null

objectives:
  - "Explain why a coordinated perinatal plan matters and who makes it."
  - "Assign a level of care (P, 1 to 5) from the fetal diagnosis."
  - "State the guidance on timing and mode of delivery."
  - "Name the fetal findings that call for a specialist team in the delivery room."

sections:

  - heading: "Why plan, and who plans"
    blocks:
      - text: "Prenatal diagnosis of critical heart disease affects illness in the newborn, and survival to a lesser extent; studies showing improved survival are sparse. Infants with ductal-dependent lesions diagnosed before birth are less compromised before surgery."
        claims: [AH14-300, AH14-301]
      - text: "A coordinated perinatal plan of care has the greatest potential to influence outcome. Certain critical lesions need cardiac intervention immediately after birth."
        claims: [AS23-604, AS23-602]
      - text: "Maternal, fetal and neonatal providers must work together once heart disease is diagnosed. Intrapartum care should be coordinated among the obstetric, neonatal and cardiology teams."
        claims: [AS23-600, AH14-302]
      - text: "The fetal diagnostic team should assign an anticipated level of care, and plans for the delivery room and the newborn should be made before delivery. Image-based risk stratification paired with level-of-care plans is recommended."
        claims: [AH14-306, AS23-603]

  - heading: "Levels of care"
    blocks:
      - text: "The AHA 2014 level-of-care scheme. Many newborns with heart disease need no specialised delivery room care."
        claims: [AH14-307, AH14-317, AH14-318, AH14-319, AH14-320, AH14-321, AH14-322]
        table:
          columns: ["Level", "Meaning", "Examples", "Delivery plan"]
          rows:
            - ["P", "Palliative care planned, with a severe or fatal chromosomal or multisystem disease", "-", "Family support and palliative care; normal delivery at the local hospital"]
            - ["1", "No predicted instability in the delivery room or first days", "VSD, AVSD, mild tetralogy", "Normal delivery at the local hospital; routine care; later cardiology review"]
            - ["2", "Minimal risk in the delivery room, but catheter or surgery needed after birth", "Ductal-dependent lesions: HLHS, critical coarctation, severe aortic stenosis, interrupted arch, PA/IVS, severe tetralogy", "Consider planned induction near term; hospital with a neonatologist and accessible cardiology; prostaglandin if indicated; then transfer"]
            - ["3", "Likely instability needing immediate specialist stabilisation", "d-TGA with concerning septum primum (all d-TGA without an atrial septal defect may reasonably be treated as at risk); uncontrolled arrhythmia; complete heart block with heart failure", "Planned induction at 38-39 weeks; caesarean if needed to coordinate; neonatologist and cardiac specialist in the delivery room"]
            - ["4", "Instability at placental separation; immediate catheter or surgery in the delivery room", "HLHS or d-TGA with severely restrictive or intact atrial septum (d-TGA also with abnormal ductus); obstructed TAPVR; Ebstein with hydrops; absent pulmonary valve with severe airway obstruction; uncontrolled arrhythmia with hydrops; complete heart block with low rate, fibroelastosis or hydrops", "Caesarean in a cardiac facility, usually at 38-39 weeks, specialists in the delivery room"]
            - ["5", "Transplantation planned", "HLHS with intact atrial septum, or severe Ebstein or cardiomyopathy with severe ventricular dysfunction", "Listing after 35 weeks; caesarean when a heart is available; specialised cardiac team in the delivery room"]

  - heading: "Place, timing and mode"
    blocks:
      - text: "Place: for heart disease at risk, plan delivery near a cardiac centre with the resources needed. Ductal-dependent lesions need a prostaglandin infusion soon after birth; delivery at a centre with a neonatologist and access to paediatric cardiology is recommended."
        claims: [AH14-303, AH14-310]
      - text: "Timing: elective induction before 39 weeks is not recommended unless there are obstetric, logistic or fetal well-being reasons."
        claims: [AH14-304]
      - text: "The transition: the ductus usually closes over 12 to 72 hours after birth. Infants with ventricular or atrioventricular septal defects are stable until pulmonary resistance falls, usually weeks after birth, and need no specialised delivery room care."
        claims: [AH14-308, AH14-309]

  - heading: "Recommendations on specialised delivery room care"
    blocks:
      - text: "Recommended (Class I): for d-TGA, and for sustained or uncontrolled tachyarrhythmia with heart failure or hydrops."
        claims: [AH14-024]
      - text: "Reasonable (Class IIa): for HLHS with a restrictive or intact atrial septum and abnormal pulmonary vein flow (forward-to-reverse ratio below 3) or an abnormal third-trimester hyperoxia test; and for complete heart block with low ventricular rate, dysfunction or hydrops."
        claims: [AH14-025]
      - text: "May be considered (Class IIb): tetralogy with absent pulmonary valve, or Ebstein anomaly with hydrops."
        claims: [AH14-026]
      - text: "Not needed (Class III): shunt lesions, most ductal-dependent lesions, and controlled arrhythmias."
        claims: [AH14-027]

  - heading: "Fetal predictors, lesion by lesion"
    blocks:
      - text: "Ductal-dependent circulation: pulmonary flow is ductal-dependent when ductal flow runs from aorta to pulmonary artery or the duct is reversed in orientation (inferior angle below 90°); systemic flow is ductal-dependent with left-to-right atrial flow. For these, prostaglandin E1 is started and no specialised delivery room care is needed."
        claims: [AH14-311]
      - text: "HLHS with restrictive or intact atrial septum: a pulmonary vein forward-to-reverse VTI ratio below 3, or no change in branch pulmonary artery pulsatility with third-trimester maternal hyperoxygenation, should lead to a plan for possible urgent decompression of the left atrium."
        claims: [AH14-312]
      - text: "D-transposition: septum primum angle below 30° to the atrial septum, bowing more than 50% into the left atrium, loss of normal swinging motion, or a hypermobile septum primum have been reported to predict restriction. These call for planned urgent balloon atrial septostomy, on site if possible, and prostaglandin E1. A small or abnormal ductus with foramen concerns means high risk; deliver where hypoxia and pulmonary hypertension can be managed."
        claims: [AH14-325, AH14-313]
      - text: "Obstructed TAPVR: a decompressing vein below the diaphragm, or accelerated flow in it, should lead to consideration of ECMO."
        claims: [AH14-323]
      - text: "Tetralogy with absent pulmonary valve: lobar emphysema (fluid trapping) on MRI suggests planning specialised ventilation and considering ECMO."
        claims: [AH14-327]
      - text: "Ebstein anomaly with hydrops or uncontrolled arrhythmia: early delivery may be considered, with measures to lower pulmonary resistance, treat arrhythmia and support output."
        claims: [AH14-328]
      - text: "Tachyarrhythmia with rapid rate, reduced function, effusion or hydrops: consider early delivery if gestation is appropriate, with urgent cardioversion or medical therapy in the delivery room. For uncontrolled tachycardia, planned cardioversion or antiarrhythmic therapy in the delivery room is indicated."
        claims: [AH14-329, AH14-315]
      - text: "Complete heart block: a falling cardiovascular profile score (to below 7), a very low ventricular rate, reduced function or fibroelastosis, or hydrops should lead to consideration of early delivery and of chronotropic drugs or temporary pacing in the delivery room. Planned chronotropic drugs or pacing in the early newborn period is reasonable."
        claims: [AH14-324, AH14-315]

  - heading: "Monitoring before delivery"
    blocks:
      - text: "Cardiotocography is unlikely to be useful in fetal bradycardia or complete heart block."
        claims: [AH14-119]

missing_claims:
  - "Awaiting re-check after rewording on 21 Nov (round 5, task J): caesarean against vaginal birth (AH14-305); hydrops in complex heart disease and delivery (AH14-316); septum primum criteria in a later study (AH14-314); ductal flow and pulmonary hypertension therapy in d-TGA (AH14-326); fetal wellness testing (AH14-017, 118, 120)."
  - "Mode of delivery: without AH14-305 the unit says nothing on caesarean against vaginal birth beyond the level-of-care table."
  - "Indian adaptation: where level 3 and 4 care is available, transport distances, and how the levels map to Indian hospitals - the editor's input and an Indian source."
  - "Prostaglandin dosing and newborn drug doses - held back until the cardiology co-editor signs (Claude task rule 3)."
  - "Newer guidance than AHA 2014 on delivery planning, where it exists - source search."
  - "Video outline not yet written."

drills:
  - id: Z3-Q01
    question: "Who should assign the anticipated level of care, and when?"
    options:
      - "The fetal diagnostic team, before delivery"
      - "The neonatologist, after birth"
      - "The obstetrician, in labour"
      - "No one; it is decided at birth"
    answer: 0
    explanation: "The fetal diagnostic team should assign a level of care, and plans should be made before delivery."
    claims: [AH14-306]

  - id: Z3-Q02
    question: "A fetus has an isolated ventricular septal defect. Which level of care fits?"
    options:
      - "Level 1: normal delivery at the local hospital, later cardiology review"
      - "Level 4: caesarean in a cardiac facility"
      - "Level 5: transplantation planned"
      - "Level 3: planned induction at a specialist centre"
    answer: 0
    explanation: "VSD is a level 1 example; these infants are stable until pulmonary resistance falls, weeks after birth."
    claims: [AH14-318, AH14-309]

  - id: Z3-Q03
    question: "Hypoplastic left heart syndrome with an open atrial septum. Which level, and what is needed at birth?"
    options:
      - "Level 2: delivery with a neonatologist and accessible cardiology; prostaglandin if indicated; then transfer"
      - "Level 1: routine care at a local hospital"
      - "Level 4: catheter intervention in the delivery room"
      - "Level P: palliative care only"
    answer: 0
    explanation: "Ductal-dependent lesions such as HLHS fall under level 2."
    claims: [AH14-319]

  - id: Z3-Q04
    question: "D-transposition without an atrial septal defect. How may it reasonably be regarded?"
    options:
      - "At risk: level 3, with specialists in the delivery room"
      - "Level 1: no risk at birth"
      - "Level P"
      - "Level 2 only if the ductus is large"
    answer: 0
    explanation: "All d-TGA without an atrial septal defect may reasonably be considered at risk (level 3)."
    claims: [AH14-320]

  - id: Z3-Q05
    question: "HLHS with a restrictive atrial septum: pulmonary vein forward-to-reverse VTI ratio below 3. What should be planned?"
    options:
      - "Possible urgent decompression of the left atrium"
      - "Routine delivery at the local hospital"
      - "Delivery before 34 weeks"
      - "No change in plan"
    answer: 0
    explanation: "A ratio below 3, or no response to maternal hyperoxygenation, should lead to a plan for urgent left atrial decompression."
    claims: [AH14-312]

  - id: Z3-Q06
    question: "What does AHA 2014 say about elective induction before 39 weeks?"
    options:
      - "Not recommended unless there are obstetric, logistic or fetal well-being reasons"
      - "Recommended for all heart disease"
      - "Required for ductal-dependent lesions"
      - "It gives no guidance"
    answer: 0
    explanation: "Elective induction before 39 weeks is not recommended without obstetric, logistic or fetal well-being reasons."
    claims: [AH14-304]

  - id: Z3-Q07
    question: "Which group needs no specialised delivery room care, according to the recommendations?"
    options:
      - "Shunt lesions, most ductal-dependent lesions and controlled arrhythmias"
      - "d-TGA"
      - "Uncontrolled tachyarrhythmia with hydrops"
      - "HLHS with intact atrial septum"
    answer: 0
    explanation: "Class III: specialised delivery room care is not needed for these."
    claims: [AH14-027]

  - id: Z3-Q08
    question: "Fetal Doppler shows aorta-to-pulmonary flow in the ductus. What does this predict?"
    options:
      - "Ductal-dependent pulmonary circulation; prostaglandin E1 after birth"
      - "Ductal-dependent systemic circulation"
      - "A normal transition"
      - "Complete heart block"
    answer: 0
    explanation: "Aorta-to-PA ductal flow predicts ductal-dependent pulmonary circulation; PGE1 is started."
    claims: [AH14-311]

  - id: Z3-Q09
    question: "Complete heart block with fibroelastosis and a falling cardiovascular profile score. What should be considered?"
    options:
      - "Early delivery, with chronotropic drugs or temporary pacing in the delivery room"
      - "Cardiotocography to guide timing"
      - "Routine delivery at term without plans"
      - "Delivery at home"
    answer: 0
    explanation: "These findings should lead to consideration of early delivery and of chronotropic drugs or pacing. Cardiotocography is unlikely to help in heart block."
    claims: [AH14-324, AH14-119]

  - id: Z3-Q10
    question: "When does the ductus usually close after birth?"
    options:
      - "Over 12 to 72 hours"
      - "Within one minute"
      - "After several months"
      - "Never in a normal baby"
    answer: 0
    explanation: "The ductus usually closes over 12 to 72 hours, which is why ductal-dependent lesions present then."
    claims: [AH14-308]

checklist:
  title: "Delivery plan before 36 weeks"
  items:
    - text: "Level of care assigned and written in the report"
      claims: [AH14-306, AH14-317, AH14-318, AH14-319, AH14-320, AH14-321, AH14-322]
    - text: "Obstetric, neonatal and cardiology teams agree the plan"
      claims: [AH14-302, AS23-600]
    - text: "Place of delivery fits the level; transfer arranged if needed"
      claims: [AH14-303, AH14-310]
    - text: "Timing: no elective induction before 39 weeks without a reason"
      claims: [AH14-304]
    - text: "Lesion-specific predictors checked and first-hour needs listed (septostomy, ECMO, pacing, cardioversion, ventilation)"
      claims: [AH14-312, AH14-325, AH14-323, AH14-324, AH14-327, AH14-329]
```

### Claims cited (with ledger statement and locator)

| id | status | statement | locator |
|---|---|---|---|
| AH14-017 | ai-extracted | Fetal wellness assessment in known congenital heart disease may be reasonable: maternal kick counts, and non-stress testing and biophysical profile from the third trimester in fetuses at risk of hypoxaemia or acidosis (Class IIb, LOE C). | Recommendations, Fetal Wellness Assessment, p. 2227, recommendation 17 |
| AH14-024 | ai-cross-checked | Specialised delivery room care should be planned for d-TGA, and for sustained or uncontrolled tachyarrhythmia with heart failure or hydrops (Class I, LOE B/C). | Recommendations, Specialized Delivery Room Care, p. 2227, recommendation 24 |
| AH14-025 | ai-cross-checked | Specialised delivery room planning is reasonable for hypoplastic left heart with restrictive or intact atrial septum and abnormal pulmonary vein flow (forward-to-reverse ratio below 3) or an abnormal third-trimester hyperoxia test, and for complete heart block with low ventricular rate, dysfunction or hydrops (Class IIa, LOE B/C). | Recommendations, Specialized Delivery Room Care, p. 2227, recommendation 25 |
| AH14-026 | ai-cross-checked | Specialised delivery room planning may be considered for tetralogy with absent pulmonary valve, or Ebstein anomaly with hydrops (Class IIb, LOE C). | Recommendations, Specialized Delivery Room Care, p. 2227, recommendation 26 |
| AH14-027 | ai-cross-checked | Specialised delivery room care is not needed for shunt lesions, most ductal-dependent lesions, or controlled arrhythmias (Class III, LOE B/C). | Recommendations, Specialized Delivery Room Care, p. 2227, recommendation 27 |
| AH14-119 | ai-cross-checked | Cardiotocography is unlikely to be useful in fetal bradycardia or complete heart block. | Fetal Wellness Assessment, Cardiotocography and Nonstress Testing, p. 2209 |
| AH14-300 | ai-cross-checked | Prenatal diagnosis of critical heart disease affects neonatal morbidity, and mortality to a lesser extent; studies showing improved survival are sparse. | Perinatal Management and Outcome of Fetuses With CHD, Impact on Morbidity / Survival, pp. 2221-2222 |
| AH14-301 | ai-cross-checked | Infants with ductal-dependent lesions diagnosed before birth are less compromised before surgery. | Perinatal Management and Outcome of Fetuses With CHD, Impact on Morbidity, pp. 2221-2222 |
| AH14-302 | ai-cross-checked | Intrapartum care should be coordinated among the obstetric, neonatal and cardiology teams. | Perinatal Management and Outcome of Fetuses With CHD, Delivery Planning, p. 2222 |
| AH14-303 | ai-cross-checked | Planning should be made for delivery near a cardiac centre with the needed resources for fetuses with heart disease at risk. | Perinatal Management and Outcome of Fetuses With CHD, Delivery Planning, p. 2222 |
| AH14-304 | ai-cross-checked | Elective induction before 39 weeks is not recommended unless there are obstetric, logistic or fetal well-being reasons. | Perinatal Management and Outcome of Fetuses With CHD, Delivery Planning, p. 2222 |
| AH14-305 | ai-extracted | The studies available in 2014 did not show an inherent advantage of caesarean over vaginal birth for fetuses with congenital heart disease; no randomised trials of delivery route in severe congenital heart disease were reported. | Perinatal Management and Outcome of Fetuses With CHD, Delivery Planning, p. 2222 |
| AH14-306 | ai-cross-checked | The fetal diagnostic team should assign an anticipated level of care, and delivery room and neonatal plans should be made before delivery. | Perinatal Management and Outcome of Fetuses With CHD, Delivery Room and Neonatal Care Planning, p. 2223 |
| AH14-307 | ai-cross-checked | Many newborns with heart disease need no specialised delivery room care. | Perinatal Management and Outcome of Fetuses With CHD, Delivery Room and Neonatal Care Planning, p. 2223 |
| AH14-308 | ai-cross-checked | The ductus arteriosus usually closes over 12 to 72 hours after birth. | Perinatal Management and Outcome of Fetuses With CHD, Transitional Circulation, p. 2224 |
| AH14-309 | ai-cross-checked | Infants with ventricular or atrioventricular septal defect are stable until pulmonary resistance falls, usually weeks after birth; no specialised delivery room care is recommended. | Perinatal Management and Outcome of Fetuses With CHD, CHD With Minimal Risk During Transition, p. 2224 |
| AH14-310 | ai-cross-checked | Ductal-dependent lesions need prostaglandin infusion soon after birth; delivery at a centre with a neonatologist and access to paediatric cardiology is recommended. | Perinatal Management and Outcome of Fetuses With CHD, Ductal-Dependent Lesions, p. 2224 |
| AH14-311 | ai-cross-checked | Ductal-dependent pulmonary circulation is predicted by aorta-to-pulmonary flow in the ductus or reversed ductal orientation (inferior angle below 90°), and ductal-dependent systemic circulation by left-to-right atrial flow; for these, no specialised delivery room care is needed (Class I, LOE B) and prostaglandin E1 is started (I, B). | Table 20 (fetal predictors for delivery planning), p. 2225 |
| AH14-312 | ai-cross-checked | In HLHS with restrictive or intact atrial septum, a pulmonary vein forward-to-reverse velocity-time integral ratio below 3, or no change in branch pulmonary artery pulsatility with third-trimester maternal hyperoxygenation, should lead to a plan for possible urgent decompression of the left atrium (Class IIa, LOE B). | Table 20 (fetal predictors for delivery planning), p. 2225 |
| AH14-313 | ai-cross-checked | In D-transposition, a small or abnormal ductus with concerns about the foramen ovale indicates high risk of compromise and need for urgent balloon septostomy; such fetuses should be delivered where hypoxia and pulmonary hypertension can be managed. | Perinatal Management and Outcome of Fetuses With CHD, Foramen Ovale-Dependent Lesions, p. 2225 |
| AH14-314 | ai-extracted | In d-TGA, a later study found that a tethered or bowing septum primum did not predict postnatal compromise needing emergent intervention with acceptable sensitivity or specificity. | Perinatal Management and Outcome of Fetuses With CHD, Foramen Ovale-Dependent Lesions, p. 2225 |
| AH14-315 | ai-cross-checked | Planned cardioversion or antiarrhythmic therapy in the delivery room is indicated for uncontrolled tachycardia; planned chronotropic drugs or pacing in the early newborn period is reasonable for complete heart block. | Perinatal Management and Outcome of Fetuses With CHD, Fetal Arrhythmias, p. 2226 |
| AH14-316 | ai-extracted | Hydrops in complex congenital heart disease is ominous; if it is attributed to heart failure, delivery may be considered when the gestational age is appropriate and the primary pathology is treatable or reversible, with immediate treatment prepared. | Perinatal Management and Outcome of Fetuses With CHD, Complex CHD With Heart Failure, p. 2226 |
| AH14-317 | ai-cross-checked | Level of care P: heart disease with palliative care planned (with a severe or fatal chromosomal or multisystem disease); arrange family support and palliative care; normal delivery at the local hospital. | Table 19 (level of care assignment), p. 2223 |
| AH14-318 | ai-cross-checked | Level of care 1: heart disease without predicted instability in the delivery room or first days (for example VSD, AVSD, mild tetralogy); normal delivery at the local hospital with routine care and later cardiology review. | Table 19 (level of care assignment), p. 2223 |
| AH14-319 | ai-cross-checked | Level of care 2: minimal risk of instability in the delivery room but needing catheterisation or surgery after birth (ductal-dependent lesions such as HLHS, critical coarctation, severe aortic stenosis, interrupted arch, PA/IVS, severe tetralogy); consider planned induction near term, delivery at a hospital with a neonatologist and accessible cardiology, start prostaglandin if indicated, then transfer. | Table 19 (level of care assignment), p. 2223 |
| AH14-320 | ai-cross-checked | Level of care 3: likely instability in the delivery room needing immediate specialist stabilisation (d-TGA with concerning atrial septum primum - all d-TGA without an atrial septal defect may reasonably be considered at risk - uncontrolled arrhythmias, complete heart block with heart failure); planned induction at 38-39 weeks, caesarean if needed to coordinate, delivery where rapid stabilising care is possible, neonatologist and cardiac specialist in the delivery room. | Table 19 (level of care assignment), p. 2223 |
| AH14-321 | ai-cross-checked | Level of care 4: expected instability at placental separation needing immediate catheterisation or surgery in the delivery room (HLHS with severely restrictive or intact atrial septum; d-TGA with severely restrictive or intact atrial septum and abnormal ductus; obstructed TAPVR; Ebstein with hydrops; tetralogy with absent pulmonary valve and severe airway obstruction; uncontrolled arrhythmia with hydrops; complete heart block with low ventricular rate, endocardial fibroelastosis or hydrops); caesarean in a cardiac facility with specialists in the delivery room, usually at 38-39 weeks. | Table 19 (level of care assignment), p. 2223 |
| AH14-322 | ai-cross-checked | Level of care 5: heart disease for which transplantation is planned (HLHS with intact atrial septum, or heart disease including severe Ebstein or cardiomyopathy with severe ventricular dysfunction); listing after 35 weeks, caesarean when a heart is available, specialised cardiac team in the delivery room. | Table 19 (level of care assignment), p. 2223 |
| AH14-323 | ai-cross-checked | For obstructed TAPVR, a decompressing vein below the diaphragm or accelerated flow in it should lead to consideration of ECMO (Class IIb, LOE C). | Table 20 (fetal predictors for delivery planning), p. 2225 |
| AH14-324 | ai-cross-checked | For complete heart block, a falling cardiovascular profile score (to below 7), very low ventricular rate, reduced function or endocardial fibroelastosis, or hydrops should lead to consideration of early delivery and of chronotropic drugs or temporary pacing in the delivery room (Class IIa, LOE C). | Table 20 (fetal predictors for delivery planning), p. 2225 |
| AH14-325 | ai-cross-checked | In d-TGA, foramen ovale findings reported to predict restriction are: septum primum angle below 30° to the atrial septum, bowing of septum primum more than 50% into the left atrium, loss of normal swinging motion, and a hypermobile septum primum; these call for planned urgent balloon atrial septostomy, on site if possible (Class I, LOE B), and prostaglandin E1 (I, B). | Table 20 (fetal predictors for delivery planning), p. 2225 |
| AH14-326 | ai-extracted | In d-TGA, abnormal ductal flow (accelerated forward, bidirectional or reversed diastolic flow) should lead to consideration of treatment for pulmonary hypertension (Class IIb, LOE C); Table 20 also lists a small ductus among abnormal ductal findings. | Table 20 (fetal predictors for delivery planning), p. 2225 |
| AH14-327 | ai-cross-checked | In tetralogy with absent pulmonary valve, lung findings of lobar emphysema (fluid trapping) on MRI suggest planning specialised ventilation and considering ECMO (Class IIb, LOE C). | Table 20 (fetal predictors for delivery planning), p. 2225 |
| AH14-328 | ai-cross-checked | In Ebstein anomaly with hydrops or uncontrolled arrhythmia, early delivery may be considered, with measures to lower pulmonary resistance, treat arrhythmia and support output (Class IIb, LOE C). | Table 20 (fetal predictors for delivery planning), p. 2225 |
| AH14-329 | ai-cross-checked | In tachyarrhythmia with rapid rate, reduced function, or pericardial effusion or hydrops, early delivery should be considered if gestation is appropriate, with urgent cardioversion or medical therapy in the delivery room if possible (Class I, LOE C). | Table 20 (fetal predictors for delivery planning), p. 2225 |
| AS23-600 | ai-cross-checked | Once fetal heart disease is diagnosed, maternal, fetal and neonatal providers must work together on its implications, follow-up visits and the expected level of neonatal care. | IV.D Key Points, p. 718; IV.D Imaging-Based Risk Assessment and Delivery Planning, p. 718 |
| AS23-602 | ai-cross-checked | Certain forms of critical heart disease require cardiac intervention immediately after birth. | IV.D Imaging-Based Risk Assessment and Delivery Planning, p. 718 |
| AS23-603 | ai-cross-checked | Image-based risk stratification paired with level-of-care plans is recommended for prenatally diagnosed heart disease, and may standardise communication and perinatal management. | IV.D Key Points, p. 718; IV.D Imaging-Based Risk Assessment and Delivery Planning, p. 718 |
| AS23-604 | ai-cross-checked | A coordinated perinatal plan of care has the greatest potential to influence outcome. | IV.D Imaging-Based Risk Assessment and Delivery Planning, p. 718 |

---
## Unit XA2

### Unit file

```yaml
# Unit XA2. Every text block and drill lists the claim IDs it rests on.
# Built only from ai-cross-checked claims: mainly AHA 2014 (extracted by Claude,
# cross-checked by ChatGPT on 19 Nov 2026), with ASE 2023 for lesion-specific points.
# Genetic testing has changed a great deal since 2014: this unit needs a newer source and a
# clinical geneticist's review before release (units.yaml: needs S).

id: XA2
title: "Genetics of congenital heart disease and the work-up after diagnosis"
tier: Diagnose
version: 0.1
summary: "How often fetal heart disease is chromosomal, which lesions carry which risk, what testing to offer, and the rest of the work-up once a heart defect is found."
drafted_by: "Claude (Opus 5.5, 21 Nov 2026)"
audited_by: null
signed_by: null

objectives:
  - "Give the approximate rate of chromosomal abnormality in fetal heart disease, and why it is higher than in infants."
  - "Name the lesions with the highest and lowest aneuploidy risk, and those linked with 22q11 deletion."
  - "State what testing and counselling to offer, and what must be disclosed before microarray."
  - "Describe the extracardiac survey after a cardiac diagnosis."

sections:

  - heading: "How common, and why it matters"
    blocks:
      - text: "About 15% of infants with heart disease have a recognisable chromosomal abnormality, mostly aneuploidies: trisomies 21, 13 and 18, and monosomy X."
        claims: [AH14-100]
      - text: "In the fetus the rate is higher: abnormal karyotypes are found in 30% to 40% in most series, probably because affected fetuses die more often before birth. Even isolated heart disease diagnosed by ultrasound carries a risk of at least 15% to 30%."
        claims: [AH14-101, AH14-102]
      - text: "Genetic results may prompt a further search for anomalies, inform recurrence risk, and influence decisions on termination or palliative care."
        claims: [AH14-104]

  - heading: "Risk by lesion"
    blocks:
      - text: "Ventricular and atrioventricular septal defects are the lesions most often associated with an abnormal karyotype. Of fetuses with atrioventricular septal defect and normal situs, 50% to 70% have trisomy 21."
        claims: [AH14-108, AH14-109]
      - text: "Risk of aneuploidy by lesion, from the AHA 2014 tables (ranges across published series)."
        claims: [AH14-112]
        table:
          columns: ["Lesion", "Aneuploidy risk"]
          rows:
            - ["Atrioventricular septal defect", "46-73%"]
            - ["Common arterial trunk", "19-78%"]
            - ["Tetralogy of Fallot", "7-39%"]
            - ["Hypoplastic left heart", "4-9%"]
            - ["Transposition", "0%"]
            - ["Heterotaxy", "0%"]
      - text: "Heterotaxy, D-transposition, congenitally corrected transposition and pulmonary atresia with intact septum are rarely aneuploid, but parents should still be offered testing."
        claims: [AH14-107]

  - heading: "22q11 deletion"
    blocks:
      - text: "Conotruncal lesions and right aortic arch are associated with 22q11 deletion."
        claims: [AH14-110]
      - text: "Estimated frequency of 22q11 deletion by lesion, from AHA 2014."
        claims: [AH14-113]
        table:
          columns: ["Lesion", "22q11 deletion"]
          rows:
            - ["Interrupted aortic arch", "50-90%"]
            - ["Common arterial trunk", "35-40%"]
            - ["Isolated arch anomaly", "25%"]
            - ["Tetralogy of Fallot", "8-35%"]
            - ["Transposition", "Below 1%"]
      - text: "On the scan: imaging the arch and the thymus allows counselling tailored to the risk of 22q11 deletion. In common arterial trunk with a right aortic arch the risk is above 50%. In absent pulmonary valve syndrome, telling the subaortic-VSD form from the intact-septum form matters for assessing 22q11.2 deletion."
        claims: [AS23-313, AS23-350, AS23-318]

  - heading: "Other genetic clues"
    blocks:
      - text: "A cardiac tumour found in mid or late gestation should prompt genetic testing: over 60% of such fetuses have tuberous sclerosis."
        claims: [AH14-111]
      - text: "Lesions of the atrioventricular junction may be isolated, often with aneuploidy including trisomy 21."
        claims: [AS23-249]

  - heading: "What to offer"
    blocks:
      - text: "Genetic testing and counselling should be recommended for every fetus with a cardiac malformation, with or without other anomalies."
        claims: [AH14-103]
      - text: "Before microarray testing, disclose that it may find variants of unknown significance. Microarray cannot detect balanced rearrangements. In 2014, whether it should replace routine cytogenetic testing was still debated."
        claims: [AH14-105, AH14-106]

  - heading: "The extracardiac survey"
    blocks:
      - text: "Every fetus with heart disease should have a detailed survey of all fetal anatomy by an expert operator. Some anomalies are only detectable later, so a repeat assessment may be appropriate."
        claims: [AH14-116]
      - text: "Ventricular septal defect and tricuspid atresia are often associated with other anomalies; D-transposition and pulmonary atresia with intact septum are more often isolated."
        claims: [AH14-115]

missing_claims:
  - "Awaiting re-check after rewording on 21 Nov (round 5, task J): recommendation 14, genetic counselling with offer of aneuploidy testing and detailed anatomy scan (AH14-014); extracardiac anomaly rates (AH14-114); fetal MRI for extracardiac screening (AH14-015, 016, 117); parental testing (AH14-330, new)."
  - "Current testing: exome and genome sequencing, rapid aneuploidy tests, and how testing has changed since 2014 - needs a newer source and a clinical geneticist."
  - "Availability and cost of each test in India, and the legal framework (PC-PNDT) for prenatal genetic testing - needs an Indian source and the editor's input."
  - "Recurrence risks for siblings and offspring - needs a source."
  - "Video outline not yet written."

drills:
  - id: XA2-Q01
    question: "Why is the rate of chromosomal abnormality higher in fetuses with heart disease than in infants?"
    options:
      - "Affected fetuses more often die before birth"
      - "Fetal testing is less accurate"
      - "Heart disease causes aneuploidy after birth"
      - "It is not higher"
    answer: 0
    explanation: "Fetal series show 30-40% abnormal karyotypes, more than infants, probably because of higher mortality in utero."
    claims: [AH14-101]

  - id: XA2-Q02
    question: "Heart disease appears isolated on ultrasound. What is the risk of a chromosomal abnormality?"
    options:
      - "At least 15% to 30%"
      - "Under 1%"
      - "Zero, if the defect is isolated"
      - "Over 90%"
    answer: 0
    explanation: "Isolated heart disease on ultrasound carries a risk of at least 15-30%."
    claims: [AH14-102]

  - id: XA2-Q03
    question: "Atrioventricular septal defect with normal situs. What proportion have trisomy 21?"
    options:
      - "50% to 70%"
      - "About 5%"
      - "None"
      - "All"
    answer: 0
    explanation: "50-70% of fetuses with AVSD and normal situs have trisomy 21."
    claims: [AH14-109]

  - id: XA2-Q04
    question: "D-transposition is diagnosed. The aneuploidy risk is very low. Should testing still be offered?"
    options:
      - "Yes: parents should still be offered testing"
      - "No: testing is never indicated in transposition"
      - "Only if the mother is over 35"
      - "Only after birth"
    answer: 0
    explanation: "These lesions are rarely aneuploid, but testing should still be offered. Genetic testing and counselling should be recommended for every fetus with a cardiac malformation."
    claims: [AH14-107, AH14-103]

  - id: XA2-Q05
    question: "Which lesion has the highest estimated frequency of 22q11 deletion?"
    options:
      - "Interrupted aortic arch"
      - "Transposition"
      - "Hypoplastic left heart"
      - "Atrioventricular septal defect"
    answer: 0
    explanation: "AHA 2014 Table 11 gives 50-90% for interrupted aortic arch."
    claims: [AH14-113]

  - id: XA2-Q06
    question: "A cardiac tumour is seen at 26 weeks. What should it prompt?"
    options:
      - "Genetic testing: over 60% have tuberous sclerosis"
      - "Immediate delivery"
      - "No further action"
      - "Fetal intervention"
    answer: 0
    explanation: "A tumour in mid or late gestation should prompt genetic testing; over 60% have tuberous sclerosis."
    claims: [AH14-111]

  - id: XA2-Q07
    question: "Before microarray testing, what must parents be told?"
    options:
      - "It may find variants of unknown significance"
      - "It detects every genetic cause"
      - "It detects balanced rearrangements"
      - "It needs no consent"
    answer: 0
    explanation: "Variants of unknown significance should be disclosed before testing; microarray cannot detect balanced rearrangements."
    claims: [AH14-105]

  - id: XA2-Q08
    question: "After a cardiac diagnosis, what survey of the rest of the fetus is recommended?"
    options:
      - "A detailed survey of all anatomy by an expert, repeated later if appropriate"
      - "None; the heart is the only concern"
      - "Fetal MRI for every case"
      - "Only a growth scan"
    answer: 0
    explanation: "A detailed expert survey is recommended for every fetus with heart disease; some anomalies only appear later."
    claims: [AH14-116]

checklist:
  title: "Work-up after a cardiac diagnosis"
  items:
    - text: "Genetic counselling and testing recommended"
      claims: [AH14-103]
    - text: "Microarray: variants of unknown significance disclosed beforehand"
      claims: [AH14-105]
    - text: "Arch and thymus imaged where 22q11 deletion is possible"
      claims: [AS23-313, AH14-110]
    - text: "Detailed extracardiac survey by an expert; repeat planned if appropriate"
      claims: [AH14-116]
    - text: "Cardiac tumour: tuberous sclerosis testing"
      claims: [AH14-111]
```

### Claims cited (with ledger statement and locator)

| id | status | statement | locator |
|---|---|---|---|
| AH14-014 | ai-extracted | Fetuses with known congenital heart disease should have genetic counselling with an offer of testing for aneuploidy, and a detailed anatomy ultrasound (Class I, LOE A). | Recommendations, Extracardiac Assessment, p. 2227, recommendation 14 |
| AH14-015 | ai-extracted | Fetal brain MRI is reasonable when a brain abnormality is suspected in known congenital heart disease, and chest MRI to assess lung volume with congenital diaphragmatic hernia (Class IIa, LOE B). | Recommendations, Extracardiac Assessment, p. 2227, recommendation 15 |
| AH14-100 | ai-cross-checked | About 15% of infants with heart disease have a recognisable chromosomal abnormality, mostly aneuploidies such as trisomies 21, 13 and 18 and monosomy X. | Extracardiac Assessment of the Fetus With CHD, Genetic Abnormalities and CHD, p. 2206 |
| AH14-101 | ai-cross-checked | Fetuses with heart disease have abnormal karyotypes in 30% to 40% in most series, more than infants, likely because of higher mortality in utero. | Extracardiac Assessment of the Fetus With CHD, p. 2206 |
| AH14-102 | ai-cross-checked | Isolated heart disease diagnosed by ultrasound carries a risk of chromosomal abnormality of at least 15% to 30%. | Extracardiac Assessment of the Fetus With CHD, Genetic Testing of Fetuses With CHD, p. 2207 |
| AH14-103 | ai-cross-checked | Genetic testing and counselling should be recommended for all fetuses with a cardiac malformation, with or without other anomalies. | Extracardiac Assessment of the Fetus With CHD, Genetic Testing of Fetuses With CHD, p. 2207 |
| AH14-104 | ai-cross-checked | Genetic results may prompt a further search for anomalies, inform recurrence risk, and influence decisions on termination or palliative care. | Extracardiac Assessment of the Fetus With CHD, p. 2207 |
| AH14-105 | ai-cross-checked | Microarray testing may reveal variants of unknown significance, and this should be disclosed before testing; it cannot detect balanced rearrangements. | Extracardiac Assessment of the Fetus With CHD, Available Genetic Testing, pp. 2206-2207 |
| AH14-106 | ai-cross-checked | Whether microarray should replace routine cytogenetic testing was debated at the time of writing. | Extracardiac Assessment of the Fetus With CHD, p. 2206 |
| AH14-107 | ai-cross-checked | Heterotaxy, D-transposition, congenitally corrected transposition and pulmonary atresia with intact septum are rarely aneuploid, but parents should still be offered testing. | Extracardiac Assessment of the Fetus With CHD, Genetic Abnormalities Associated With CHD, p. 2207 |
| AH14-108 | ai-cross-checked | Ventricular and atrioventricular septal defects are the lesions most often associated with an abnormal karyotype. | Extracardiac Assessment of the Fetus With CHD, p. 2207 |
| AH14-109 | ai-cross-checked | Of fetuses with atrioventricular septal defect and normal situs, 50% to 70% have trisomy 21. | Extracardiac Assessment of the Fetus With CHD, p. 2207 |
| AH14-110 | ai-cross-checked | Conotruncal lesions and right aortic arch are associated with 22q11 deletion. | Extracardiac Assessment of the Fetus With CHD, p. 2207 |
| AH14-111 | ai-cross-checked | A cardiac tumour found in mid or late gestation should prompt genetic testing; over 60% of such fetuses have tuberous sclerosis. | Extracardiac Assessment of the Fetus With CHD, p. 2207 |
| AH14-112 | ai-cross-checked | Table 10 gives a risk of aneuploidy of 46-73% with atrioventricular septal defect, 7-39% with tetralogy of Fallot, 19-78% with common arterial trunk, 4-9% with hypoplastic left heart, and 0% with transposition and with heterotaxy. | Table 10, p. 2207 |
| AH14-113 | ai-cross-checked | Table 11 gives an estimated 22q11 deletion frequency of 50-90% with interrupted aortic arch, 35-40% with common arterial trunk, 8-35% with tetralogy of Fallot, 25% with isolated arch anomaly, and below 1% with transposition. | Table 11, p. 2208 |
| AH14-114 | ai-extracted | Extracardiac anomalies occur in up to 20% of infants with congenital heart disease; the proportion is higher in fetuses, with figures as high as 50% to 70% reported. | Extracardiac Assessment of the Fetus With CHD, Extracardiac Abnormalities, p. 2208 |
| AH14-115 | ai-cross-checked | Ventricular septal defect and tricuspid atresia are often associated with other anomalies; D-transposition and pulmonary atresia with intact septum are more often isolated. | Extracardiac Assessment of the Fetus With CHD, p. 2208 |
| AH14-116 | ai-cross-checked | A detailed survey of all fetal anatomy, by an expert operator, is recommended for every fetus diagnosed with heart disease; some anomalies may only be detectable later, so repeat assessment may be appropriate. | Extracardiac Assessment of the Fetus With CHD, Fetal Survey, p. 2208 |
| AH14-330 | ai-extracted | Parental testing may be used as adjunctive testing to assess recurrence risk when a balanced translocation is suspected in one parent, or to clarify the clinical significance of copy-number variants found on microarray testing of the fetus. | Genetic Testing of Fetuses With CHD, p. 2207 |
| AS23-249 | ai-cross-checked | Lesions of the atrioventricular junction may be isolated (often with aneuploidy, including trisomy 21) or complex, with multiple associated defects. | IV.C.ii opening, p. 704 |
| AS23-313 | ai-cross-checked | Imaging the arch and the thymus allows counselling tailored to the risk of 22q11 deletion. | IV.C.iii Lesions with a VSD and Overriding Great Vessel, p. 714 |
| AS23-318 | ai-cross-checked | Distinguishing absent pulmonary valve with a subaortic ventricular septal defect from absent pulmonary valve with an intact septum is critical for surgical planning and for assessing 22q11.2 deletion. | IV.C.iv Severe Atrioventricular and Semilunar Valve Regurgitation, pp. 716-717 |
| AS23-350 | ai-cross-checked | In common arterial trunk, a right aortic arch is associated with a risk of 22q11 deletion above 50%. | Table 13 (lesion-specific evaluation), p. 707 |

---
## Unit Z1

### Unit file

```yaml
# Unit Z1. Every text block and drill lists the claim IDs it rests on.
# Built only from ai-cross-checked claims (AHA 2014, extracted by Claude, cross-checked by
# ChatGPT on 19 Nov 2026). Several counselling claims were reworded on 21 Nov and await
# re-check; they are listed under missing_claims. This is a thin first version.
# Indian law on termination is not in any claim held; nothing here states a legal limit.

id: Z1
title: "Counselling in depth"
tier: Decide
version: 0.1
summary: "What counselling after a fetal cardiac diagnosis must cover, how parents react, and how to stay neutral while supporting their decision."
drafted_by: "Claude (Opus 5.5, 21 Nov 2026)"
audited_by: null
signed_by: null

objectives:
  - "List the essential elements of counselling after a fetal cardiac diagnosis."
  - "Describe the effect of referral and diagnosis on maternal anxiety."
  - "Explain how to discuss uncertainty and long-term outcome."
  - "State the counsellor's duty on bias and on the parents' decision."

sections:

  - heading: "Why counselling matters"
    blocks:
      - text: "Referral for fetal echocardiography is associated with increased maternal anxiety, which rises further when heart disease is found. Distress is greater after a prenatal diagnosis than after a postnatal one."
        claims: [AH14-130]

  - heading: "What counselling must cover"
    blocks:
      - text: "The limits of the examination, such as maternal habitus, fetal position and gestational age."
        claims: [AH14-123]
      - text: "Natural history, prognosis and genetic associations - and helping to relieve parental guilt."
        claims: [AH14-124]
      - text: "Long-term outcome: information should be current, and what is not known should be stated with its caveats."
        claims: [AH14-125]
      - text: "Genetic results can inform recurrence risk and decisions on termination or palliative care. Before microarray testing, disclose that it may find variants of unknown significance."
        claims: [AH14-104, AH14-105]
      - text: "The option of termination should be discussed, including the time limits set by the law that applies."
        claims: [AH14-128]

  - heading: "Staying neutral"
    blocks:
      - text: "Counsellors should avoid personal bias and support whatever decision the parents make."
        claims: [AH14-129]

  - heading: "Counselling about fetal procedures"
    blocks:
      - text: "Families considering fetal aortic valvuloplasty should receive extensive counselling on the risks to mother and fetus and the expected course compared with standard care, including the lack of long-term outcome data. Technical success of a fetal procedure does not always mean clinical success after birth."
        claims: [AH14-207, AH14-202]

missing_claims:
  - "Awaiting re-check after rewording on 21 Nov (round 5, task J): the aims of counselling and the care team (AH14-121); timing - offered soon after the scan, ideally the same day (AH14-122); evidence on counselling techniques (AH14-126); checking understanding, avoiding overload, several sessions (AH14-127); visual aids and online information (AH14-331, new); evaluating on fetal echocardiography before discussing prognosis (AS23-305)."
  - "Indian law on termination of pregnancy (MTP Act and its amendments), the gestational limits, and the role of medical boards - needs an Indian legal source (tasks/results/task-s1.md, topic 15) and the legal advisor. The course must state the limits exactly as the law does."
  - "PC-PNDT obligations during counselling - needs an Indian legal source."
  - "How to break bad news; the editor's own approach and wording from her practice - the editor's teaching, recorded as claims."
  - "Counselling in Indian languages and with family members present - the editor's input."
  - "Palliative care and bereavement - unit Z8."
  - "Video outline not yet written."

drills:
  - id: Z1-Q01
    question: "What does the evidence say about maternal anxiety around fetal echocardiography?"
    options:
      - "Referral raises anxiety, and diagnosis raises it further"
      - "Referral lowers anxiety"
      - "Anxiety is the same after prenatal and postnatal diagnosis"
      - "Diagnosis has no effect on anxiety"
    answer: 0
    explanation: "Referral is associated with increased anxiety, which rises further with a diagnosis; distress is greater after prenatal than postnatal diagnosis."
    claims: [AH14-130]

  - id: Z1-Q02
    question: "The image quality was poor because of maternal habitus. Should this be mentioned in counselling?"
    options:
      - "Yes: the limits of the examination should be discussed"
      - "No: it will only worry the parents"
      - "Only if the parents ask"
      - "Only in the written report"
    answer: 0
    explanation: "Counselling should discuss the limits of the examination, such as maternal habitus, fetal position and gestational age."
    claims: [AH14-123]

  - id: Z1-Q03
    question: "A mother asks whether something she did caused the defect. Which element of counselling applies?"
    options:
      - "Helping to relieve parental guilt, alongside natural history and genetic associations"
      - "Avoid the question"
      - "Refer her to another clinic"
      - "Tell her the cause is unknowable and move on"
    answer: 0
    explanation: "Counselling should cover natural history, prognosis and genetic associations, and help relieve parental guilt."
    claims: [AH14-124]

  - id: Z1-Q04
    question: "Long-term outcome data for the lesion are limited. What should counselling do?"
    options:
      - "Give current information and state what is not known, with caveats"
      - "Give the best-case outcome only"
      - "Avoid discussing the long term"
      - "Quote outcomes from decades ago without comment"
    answer: 0
    explanation: "Outcome information should be current, and the unknown stated with caveats."
    claims: [AH14-125]

  - id: Z1-Q05
    question: "The counsellor would personally choose to continue the pregnancy. How should this affect the counselling?"
    options:
      - "It should not: avoid personal bias and support the parents' decision"
      - "Share the personal view to help them decide"
      - "Encourage the parents towards that choice"
      - "Withhold information on termination"
    answer: 0
    explanation: "Counsellors should avoid personal bias and support whatever decision the parents make."
    claims: [AH14-129]

  - id: Z1-Q06
    question: "Should the option of termination be discussed?"
    options:
      - "Yes, including the time limits set by the applicable law"
      - "Never"
      - "Only if the parents raise it"
      - "Only for lethal lesions"
    answer: 0
    explanation: "The option of termination should be discussed, including the legal time limits."
    claims: [AH14-128]

checklist:
  title: "Counselling: essentials"
  items:
    - text: "Limits of the examination explained"
      claims: [AH14-123]
    - text: "Natural history, prognosis and genetic associations covered; guilt addressed"
      claims: [AH14-124]
    - text: "Outcome information current; uncertainty stated"
      claims: [AH14-125]
    - text: "All options discussed, including termination within the legal limits"
      claims: [AH14-128]
    - text: "No personal bias; the parents' decision supported"
      claims: [AH14-129]
```

### Claims cited (with ledger statement and locator)

| id | status | statement | locator |
|---|---|---|---|
| AH14-104 | ai-cross-checked | Genetic results may prompt a further search for anomalies, inform recurrence risk, and influence decisions on termination or palliative care. | Extracardiac Assessment of the Fetus With CHD, p. 2207 |
| AH14-105 | ai-cross-checked | Microarray testing may reveal variants of unknown significance, and this should be disclosed before testing; it cannot detect balanced rearrangements. | Extracardiac Assessment of the Fetus With CHD, Available Genetic Testing, pp. 2206-2207 |
| AH14-121 | ai-extracted | Prenatal counselling aims to give an accurate diagnosis, a clear prognosis and the management options, and to support the parents' decisions; a care team, which may include a social worker or genetic counsellor, should support the family. | Prenatal Counseling and Parental Stress, p. 2209 |
| AH14-122 | ai-extracted | Counselling should be offered soon after the fetal echocardiogram, ideally on the same day. | Prenatal Counseling and Parental Stress, Essential Elements, p. 2209 |
| AH14-123 | ai-cross-checked | Counselling should discuss the limitations of the examination, such as maternal habitus, fetal position and gestational age. | Prenatal Counseling and Parental Stress, Essential Elements, p. 2209 |
| AH14-124 | ai-cross-checked | Counselling should cover natural history, prognosis and genetic associations, and help relieve parental guilt. | Prenatal Counseling and Parental Stress, Essential Elements, p. 2209 |
| AH14-125 | ai-cross-checked | Long-term outcome information given in counselling should be current, and what is unknown should be stated with caveats. | Prenatal Counseling and Parental Stress, Essential Elements, pp. 2209-2210 |
| AH14-126 | ai-extracted | In 2014, specific techniques for counselling after a prenatal diagnosis of congenital heart disease had not been studied scientifically. | Prenatal Counseling and Parental Stress, Techniques, p. 2210 |
| AH14-127 | ai-extracted | Counsellors should check understanding and avoid overloading parents with information; several sessions may be needed, particularly if the mother is alone at the first visit; counselling support should continue through the pregnancy, including at follow-up scans. | Prenatal Counseling and Parental Stress, Techniques, p. 2210 |
| AH14-128 | ai-cross-checked | The option of termination should be discussed, including the time limits set by the applicable law. | Prenatal Counseling and Parental Stress, Techniques, p. 2210 |
| AH14-129 | ai-cross-checked | Counsellors should avoid personal bias and support whatever decision the parents make. | Prenatal Counseling and Parental Stress, Decision Making, p. 2210 |
| AH14-130 | ai-cross-checked | Referral for fetal echocardiography is associated with increased maternal anxiety, which rises further when heart disease is found; distress is greater after prenatal than postnatal diagnosis. | Prenatal Counseling and Parental Stress, Parental Stress, p. 2210 |
| AH14-202 | ai-cross-checked | Technical success of a fetal procedure does not always translate into clinical success after birth. | Fetal Cardiac Catheter Intervention / Cardiac Lesions Amenable to Fetal Intervention, Overview, p. 2217 |
| AH14-207 | ai-cross-checked | Families considering aortic valvuloplasty should receive extensive counselling on the risks to mother and fetus and the expected course compared with standard care, including the lack of long-term outcome data. | Fetal Cardiac Catheter Intervention / Cardiac Lesions Amenable to Fetal Intervention, AS With Evolving HLHS, p. 2218 |
| AH14-331 | ai-extracted | Printed diagrams, drawings, models, videos and other media may help convey the diagnosis to parents; counsellors should advise on the usefulness of online information but warn families about misleading data. | Prenatal Counseling and Parental Stress, Techniques, p. 2210 |
| AS23-305 | ai-extracted | Suspected outflow tract abnormalities should be evaluated by fetal echocardiography before prognosis, associated abnormalities and further testing, including genetic testing, are discussed with the patient. | IV.C.iii Key Points, p. 715 |

---
## Unit Z5

### Unit file

```yaml
# Unit Z5. Every text block and drill lists the claim IDs it rests on.
# Built only from ai-cross-checked claims (AHA 2014 and ASE 2023, extracted by Claude,
# cross-checked by ChatGPT on 19 Nov 2026). AHA 2014 is twelve years old: outcome figures
# and candidacy criteria need a newer source (tasks/results/task-s1.md, topic 10) and the
# cardiology co-editor before release. No drug doses.

id: Z5
title: "Fetal cardiac intervention"
tier: Decide
version: 0.1
summary: "Why some lesions are treated before birth, which fetuses may be candidates, what the procedures aim to do, and how to counsel and follow up."
drafted_by: "Claude (Opus 5.5, 21 Nov 2026)"
audited_by: null
signed_by: null

objectives:
  - "State the rationale for fetal cardiac intervention and its main limit."
  - "Name the signs of evolving hypoplastic left heart in aortic stenosis and the candidacy criteria for valvuloplasty."
  - "Describe the problem of the restrictive atrial septum in HLHS, and the role of intervention in pulmonary atresia with intact septum."
  - "Describe counselling and follow-up after a fetal procedure."

sections:

  - heading: "The idea, and its limit"
    blocks:
      - text: "Fetal cardiac intervention rests on the idea that some lesions progress in utero, and that there may be a limited window when their effects on growth and function can still be reversed."
        claims: [AH14-201]
      - text: "Technical success of a fetal procedure does not always translate into clinical success after birth."
        claims: [AH14-202]
      - text: "Any fetal therapy must be weighed against the risk to the mother and the chance of successful treatment after birth. In 2014 there were no randomised trials of fetal cardiac therapy."
        claims: [AH14-131]

  - heading: "Aortic stenosis with evolving hypoplastic left heart"
    blocks:
      - text: "Signs of evolution: retrograde transverse arch flow, severe left ventricular dysfunction, monophasic short mitral inflow, and left-to-right flow at the foramen ovale."
        claims: [AH14-204]
      - text: "Aim of valvuloplasty: open the valve, promote antegrade flow and left heart growth, and make a biventricular repair possible."
        claims: [AH14-203]
      - text: "Candidates need stenosis, not atresia, with antegrade flow; little or no subvalvar obstruction; and strong evidence of evolving hypoplastic left heart."
        claims: [AH14-205]
      - text: "Assessment on fetal echocardiography: ventricular size (end-diastolic diameter and length), whether the ventricle forms the apex, hypertrophy, endocardial fibroelastosis, and systolic and diastolic function help judge severity and suitability for prenatal intervention."
        claims: [AS23-407]
      - text: "Results: in one reported series of 70 fetuses, balloon valvuloplasty was technically successful in 52 (74%)."
        claims: [AH14-206]
      - text: "After the procedure: delivery and management at a specialised congenital heart centre are recommended. Follow-up is every 4 weeks in the third trimester, assessing aortic outflow, arch flow direction, atrial septal flow, left ventricular size and function, mitral regurgitation and endocardial brightness."
        claims: [AH14-208, AS23-614]

  - heading: "HLHS with a restrictive or intact atrial septum"
    blocks:
      - text: "Greater reversal of pulmonary venous flow during atrial contraction, and reduced pulmonary vasoreactivity to maternal hyperoxygenation, indicate clinically important atrial restriction."
        claims: [AH14-210]
      - text: "In 2014 it was unresolved whether balloon septoplasty or a stent is better, and what timing best prevents pulmonary vascular damage."
        claims: [AH14-211]
      - text: "After intervention, follow-up is every 4 weeks in the third trimester, assessing patency of the atrial communication and the pulmonary venous forward-to-reverse ratio."
        claims: [AS23-615]

  - heading: "Mitral valve dysplasia syndrome"
    blocks:
      - text: "With mitral valve dysplasia, severe regurgitation and aortic stenosis, severe left-sided dilatation can compress the right heart and cause hydrops, which is most often lethal."
        claims: [AH14-212]

  - heading: "Pulmonary atresia with intact septum"
    blocks:
      - text: "Fetal intervention here is controversial. Only a small subset should be considered, and it may be lifesaving with severe tricuspid regurgitation and hydrops."
        claims: [AH14-213]
      - text: "Even a very small right ventricle can be rehabilitated through staged surgery if the tricuspid valve is of adequate size."
        claims: [AH14-214]

  - heading: "Counselling"
    blocks:
      - text: "Families considering aortic valvuloplasty should receive extensive counselling on the risks to mother and fetus and on the expected course compared with standard care, including the lack of long-term outcome data."
        claims: [AH14-207]

missing_claims:
  - "Awaiting re-check after rewording on 21 Nov (round 5, task J): recommendation 23, the lesions for which catheter intervention may be considered (AH14-023); mortality in HLHS with highly restrictive or intact septum (AH14-209); predictors of a two-ventricle outcome after valvuloplasty, with z-score and pressure cut-offs (AH14-332, new)."
  - "Outcomes since 2014 (survival, biventricular circulation, maternal complications) from current registries - needs a newer source (tasks/results/task-s1.md, topic 10)."
  - "Where fetal cardiac intervention is available to Indian patients, and referral routes - the editor's input."
  - "Transplacental drug therapy for arrhythmia and heart failure - unit Z4."
  - "Video outline not yet written."

drills:
  - id: Z5-Q01
    question: "What is the rationale for fetal cardiac intervention?"
    options:
      - "Some lesions progress in utero, and there may be a window when their effects can still be reversed"
      - "All heart lesions are easier to repair before birth"
      - "It removes the need for surgery after birth"
      - "It is proven by randomised trials"
    answer: 0
    explanation: "The rationale is progression in utero with a possible limited window for reversal."
    claims: [AH14-201]

  - id: Z5-Q02
    question: "A fetal valvuloplasty was technically successful. Can the family be told the outcome will be good?"
    options:
      - "No: technical success does not always mean clinical success after birth"
      - "Yes: technical success guarantees a biventricular repair"
      - "Yes, if done before 28 weeks"
      - "Only if the mother had no complications"
    answer: 0
    explanation: "Technical success does not always translate into clinical success after birth."
    claims: [AH14-202]

  - id: Z5-Q03
    question: "Aortic stenosis. Which findings suggest evolving hypoplastic left heart?"
    options:
      - "Retrograde arch flow, severe LV dysfunction, monophasic short mitral inflow, left-to-right flow at the foramen ovale"
      - "Antegrade arch flow and normal LV function"
      - "Right-to-left flow at the foramen ovale only"
      - "A normal mitral inflow with two waves"
    answer: 0
    explanation: "These four are the signs listed in AHA 2014 Table 16."
    claims: [AH14-204]

  - id: Z5-Q04
    question: "Which fetus could be a candidate for aortic valvuloplasty?"
    options:
      - "Aortic stenosis (not atresia) with antegrade flow, little subvalvar obstruction, and strong evidence of evolving HLHS"
      - "Aortic atresia with no antegrade flow"
      - "Mild aortic stenosis with a normal left ventricle"
      - "Any fetus with a small left ventricle"
    answer: 0
    explanation: "Candidates need stenosis with antegrade flow, minimal subvalvar obstruction and strong evidence of evolving HLHS."
    claims: [AH14-205]

  - id: Z5-Q05
    question: "HLHS: which findings indicate clinically important atrial restriction?"
    options:
      - "Greater pulmonary venous flow reversal in atrial contraction, and reduced vasoreactivity to maternal hyperoxygenation"
      - "Forward pulmonary venous flow throughout the cycle"
      - "A large foramen ovale with right-to-left flow"
      - "Normal fetal heart rate"
    answer: 0
    explanation: "Greater reversal of pulmonary venous flow and reduced vasoreactivity to hyperoxygenation indicate important restriction."
    claims: [AH14-210]

  - id: Z5-Q06
    question: "Pulmonary atresia with intact septum. When may fetal intervention be lifesaving?"
    options:
      - "With severe tricuspid regurgitation and hydrops"
      - "In every case"
      - "Only when the right ventricle is normal size"
      - "Never"
    answer: 0
    explanation: "Intervention is controversial; only a small subset should be considered, and it may be lifesaving with severe TR and hydrops."
    claims: [AH14-213]

  - id: Z5-Q07
    question: "After fetal aortic valvuloplasty, where should the baby be delivered?"
    options:
      - "At a specialised congenital heart centre"
      - "At the local hospital"
      - "At home"
      - "Anywhere with a neonatologist"
    answer: 0
    explanation: "Delivery and management at a specialised congenital heart centre are recommended."
    claims: [AH14-208]

checklist:
  title: "Before discussing fetal intervention"
  items:
    - text: "Signs of evolution documented (arch flow, LV function, mitral inflow, atrial flow)"
      claims: [AH14-204]
    - text: "Ventricular size, apex, hypertrophy, fibroelastosis and function measured"
      claims: [AS23-407]
    - text: "Candidacy criteria checked: stenosis with antegrade flow, little subvalvar obstruction"
      claims: [AH14-205]
    - text: "Family counselled on maternal and fetal risk, expected course and missing long-term data"
      claims: [AH14-207]
    - text: "Delivery at a specialised centre and follow-up every 4 weeks planned"
      claims: [AH14-208, AS23-614]
```

### Claims cited (with ledger statement and locator)

| id | status | statement | locator |
|---|---|---|---|
| AH14-023 | ai-extracted | Fetal catheter intervention may be considered for aortic stenosis with antegrade flow and evolving hypoplastic left heart; aortic stenosis with severe mitral regurgitation and restrictive atrial septum; hypoplastic left heart with severely restrictive or intact atrial septum; and pulmonary atresia with intact ventricular septum (Class IIb, LOE B/C). | Recommendations, Fetal Intervention, p. 2227, recommendation 23 |
| AH14-131 | ai-cross-checked | Fetal therapy must be weighed against the risk to the mother and the potential for successful treatment after birth; at the time of writing no randomised trials of fetal cardiac therapy existed. | Fetal Therapy for Cardiovascular Conditions Before Birth, p. 2211 |
| AH14-201 | ai-cross-checked | Fetal cardiac intervention rests on the idea that some lesions progress in utero, and that there may be a limited window when their effects on growth and function can still be reversed. | Fetal Cardiac Catheter Intervention / Cardiac Lesions Amenable to Fetal Intervention, Overview, p. 2217 |
| AH14-202 | ai-cross-checked | Technical success of a fetal procedure does not always translate into clinical success after birth. | Fetal Cardiac Catheter Intervention / Cardiac Lesions Amenable to Fetal Intervention, Overview, p. 2217 |
| AH14-203 | ai-cross-checked | The aim of fetal valvuloplasty for aortic stenosis with evolving hypoplastic left heart is to open the valve, promote antegrade flow and left heart growth, and make a biventricular repair possible. | Fetal Cardiac Catheter Intervention / Cardiac Lesions Amenable to Fetal Intervention, Table 16, p. 2217 |
| AH14-204 | ai-cross-checked | Signs of evolving hypoplastic left heart in aortic stenosis include retrograde transverse arch flow, severe left ventricular dysfunction, monophasic short mitral inflow and left-to-right flow at the foramen ovale. | Fetal Cardiac Catheter Intervention / Cardiac Lesions Amenable to Fetal Intervention, Table 16, p. 2217 |
| AH14-205 | ai-cross-checked | Candidates for aortic valvuloplasty need stenosis, not atresia, with antegrade flow, little or no subvalvar obstruction, and strong evidence of evolving hypoplastic left heart. | Fetal Cardiac Catheter Intervention / Cardiac Lesions Amenable to Fetal Intervention, AS With Evolving HLHS, p. 2218 |
| AH14-206 | ai-cross-checked | In one reported series of 70 fetuses, aortic balloon valvuloplasty was technically successful in 52 (74%). | Fetal Cardiac Catheter Intervention / Cardiac Lesions Amenable to Fetal Intervention, AS With Evolving HLHS, p. 2218 |
| AH14-207 | ai-cross-checked | Families considering aortic valvuloplasty should receive extensive counselling on the risks to mother and fetus and the expected course compared with standard care, including the lack of long-term outcome data. | Fetal Cardiac Catheter Intervention / Cardiac Lesions Amenable to Fetal Intervention, AS With Evolving HLHS, p. 2218 |
| AH14-208 | ai-cross-checked | After fetal aortic valvuloplasty, delivery and management at a specialised congenital heart centre are recommended. | Fetal Cardiac Catheter Intervention / Cardiac Lesions Amenable to Fetal Intervention, AS With Evolving HLHS, p. 2218 |
| AH14-209 | ai-extracted | Hypoplastic left heart with a highly restrictive or intact atrial septum has extremely high mortality, and the newborn typically becomes critically ill at birth; lesser degrees of atrial restriction are typical of hypoplastic left heart syndrome. | Fetal Cardiac Catheter Intervention / Cardiac Lesions Amenable to Fetal Intervention, HLHS With Restrictive or Intact Atrial Septum, p. 2218 |
| AH14-210 | ai-cross-checked | Greater reversal of pulmonary venous flow during atrial contraction, and reduced pulmonary vasoreactivity to maternal hyperoxygenation, indicate clinically important atrial restriction. | Fetal Cardiac Catheter Intervention / Cardiac Lesions Amenable to Fetal Intervention, HLHS With Restrictive or Intact Atrial Septum, p. 2218 |
| AH14-211 | ai-cross-checked | Whether balloon septoplasty or stent is better, and the best timing to prevent pulmonary vascular damage, were unresolved. | Fetal Cardiac Catheter Intervention / Cardiac Lesions Amenable to Fetal Intervention, HLHS With Restrictive or Intact Atrial Septum, p. 2218 |
| AH14-212 | ai-cross-checked | In mitral valve dysplasia with severe regurgitation and aortic stenosis, severe left-sided dilatation can compress the right heart and cause hydrops, which is most often lethal. | Fetal Cardiac Catheter Intervention / Cardiac Lesions Amenable to Fetal Intervention, Mitral Valve Dysplasia Syndrome, pp. 2218-2219 |
| AH14-213 | ai-cross-checked | Fetal intervention in pulmonary atresia with intact septum is controversial; only a small subset should be considered, and it may be lifesaving with severe tricuspid regurgitation and hydrops. | Fetal Cardiac Catheter Intervention / Cardiac Lesions Amenable to Fetal Intervention, Pulmonary Atresia With Intact Ventricular Septum, p. 2219 |
| AH14-214 | ai-cross-checked | Even a very small right ventricle can be rehabilitated through staged surgery if the tricuspid valve is of adequate size. | Fetal Cardiac Catheter Intervention / Cardiac Lesions Amenable to Fetal Intervention, Pulmonary Atresia With Intact Ventricular Septum, p. 2219 |
| AH14-332 | ai-extracted | In aortic stenosis with evolving hypoplastic left heart considered for fetal intervention, factors predicting a favourable outcome for two-ventricle repair include a left ventricular long-axis z score above -2, a left ventricle able to generate at least 10 mm Hg across the aortic valve or a 15 mm Hg mitral regurgitant jet, and a mitral valve diameter z score above -3. | Fetal Cardiac Catheter Intervention, AS With Evolving HLHS, p. 2218 |
| AS23-407 | ai-cross-checked | Ventricular size (end-diastolic diameter and length), whether the ventricle forms the apex, hypertrophy, endocardial fibroelastosis and systolic and diastolic function help judge severity and suitability for prenatal intervention. | IV.C.iv Semilunar Valve Obstruction with an Intact Ventricular Septum, pp. 715-716 |
| AS23-614 | ai-cross-checked | After fetal intervention for aortic stenosis with evolving hypoplastic left heart, follow-up is every 4 weeks in the third trimester, assessing aortic outflow, arch flow direction, atrial septal flow, left ventricular size and function, mitral regurgitation and endocardial brightness. | Table 15 (follow-up imaging for specific CHD diagnoses), p. 719 |
| AS23-615 | ai-cross-checked | After fetal intervention for hypoplastic left heart with restrictive atrial septum, follow-up is every 4 weeks in the third trimester, assessing patency of the atrial communication and the pulmonary venous forward-to-reverse ratio. | Table 15 (follow-up imaging for specific CHD diagnoses), p. 719 |

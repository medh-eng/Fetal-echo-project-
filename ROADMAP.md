# Fetal Echo Project — Roadmap

A book, app, videos and study material for fetal echocardiography from one verified body of knowledge. Status: draft; nothing is released for clinical use.

Progress checklist for the Repo Command Center app (`- [x]` done, `- [ ]` remaining). Updated 2026-11-25 from the repo's docs and the project progress notes (13 to 24 Nov); edit freely, and keep it current when work moves. Owner tags: **C** Claude, **K** Dr Kunda (single editor), **P** project owner (Pon), **X** ChatGPT or Gemini (a model that is not Claude).

Where things stand: 638 claims (201 expert-verified, 381 cross-checked, 56 awaiting cross-check); 33 of 51 syllabus units drafted, 6 signed (D0, D1, D5, D7, D8, D13).

## Done
- [x] Critique, master plan, syllabus, governance notes, repository
- [x] ISUOG 2023, ASE 2023 and AHA 2014 harvested into claims with page references; AIUM 2020 harvested (41 claims, 23 Nov)
- [x] Course app, book, website page, sweep trainer (drawings await K), pilot test page
- [x] 33 units drafted: Detect 13 of 15, Foundation 2, Diagnose and Decide 18
- [x] ChatGPT cross-checks and audits (tasks A to K and L) applied; task L fixes to XC7, XC5, XC8, XB9 applied 25 Nov
- [x] Editor's review pack of 19 Nov approved by K (21 Nov): 6 units signed, 142 claims verified
- [x] Decisions recorded: consent covers teaching use in a paid product (Q4); K is the single editor, no cardiology co-editor gate (Q5)
- [x] Case catalogue tool and anonymiser built and tested on a made-up clip; clinic checks form and pilot protocol drafted
- [x] First three archive image folders reviewed by C (23 and 24 Nov); 23 candidate book images chosen with reasons (`BOOK_IMAGES\INDEX.md` on the owner's PC)

## Remaining: waiting on Claude (C)
- [ ] Put the chosen figures into the units with captions and make short loops for the app. Blocked: the images are on the owner's PC, and patient media must not enter the repo. Needs the chat linked to the desktop app with `BOOK_IMAGES` added, K's sign-off on each figure, and the anonymiser run on every clip (C, P)
- [ ] Set `audited_by` on XC7, XC5, XC8, XB9 once task O comes back clean (C, after X)
- [ ] After tasks M and N: apply findings; use the AIUM claims to strengthen XA5, F1 and the D units on views and documentation (C, after X)
- [ ] Apply the task H result to the 14 held-back claims once decided, then draft the units they unblock (C, after P and X)
- [ ] Draft D12 and D14 and the 18 undrafted syllabus units; each needs sources chosen first (C, after K and P)
- [ ] Video outlines for the 16 Diagnose and Decide units (none written)
- [ ] Clip drills for D1 and the case atlas from the first cases (C drafts; K approves answers)
- [ ] Add a unit or section for the missing normal views once K records them
- [ ] Accounts, subscription payment, certificate, supervisor view (C)

## Remaining: waiting on Dr Kunda (K)
- [ ] Record the missing views from one normal heart: stomach/situs, left outflow, right outflow, three-vessel, three-vessel-trachea, ductal arch; 2D and red/blue colour; cardiac preset, narrow sector
- [ ] Look through `BOOK_IMAGES` once and sign or reject each figure
- [ ] Sign the remaining drafted units (27 unsigned), starting with the review pack `dist/editor/review-pack.html`
- [ ] XC7 decisions: diabetes overlap (first-trimester Class I vs gestational HbA1c below 6% Class III); the printed "vitamin K agonists" item; AHA 2014 vs AIUM 2020 on indications
- [ ] Answer the open image questions: what "HR 95" on the STIC image refers to; what files 10_5, 10_38, 10_9 and 10_1 show; the 108 bpm image in c021102-16; the meaning of "hammock view"
- [ ] Mark up the five sweep drawings (`dist/editor/sweep-schematics.html`)
- [ ] Three D1 videos (about half a day to record)
- [ ] Choose sources for undrafted units (`tasks/results/task-s1.md`)

## Remaining: waiting on the project owner (P)
- [ ] Merge PR #10 and the Task L fixes branch, which carries them
- [ ] Copy only the machine's export folder into `Desktop\CLAUDE ECHO` from now on, never the patient-named folder or the PDF report
- [ ] Decide task H (14 claims, same-model rule) and supply the AHA 2024 arrhythmia paper for the 112 held claims
- [ ] Archive survey of the 14-year archive: how many cases, stills or clips or 4D volumes, how stored (only the recent exports are known)
- [ ] Machine check: DICOM and 4D export formats (MP4 clips and stills are confirmed; the export banner already shows only gestational age)
- [ ] Hosting and password plan; clinic checks form (`docs/09-hosting-pilot.md`, `docs/07-clinic-checks.md`)
- [ ] Health-law consultation, ethics application, terms of use and privacy notice

## Remaining: waiting on a model that is not Claude (X)
- [ ] Task O: re-audit XC7, XC5, XC8, XB9 after the fixes (`tasks/chatgpt-tasks-round6.md`)
- [ ] Task M: re-check AS23-412 against the printed Table 13, p. 708
- [ ] Task N: cross-check the 41 AIUM claims
- [ ] Task H: only if P decides a non-Claude check is needed
- [ ] Second-model check of the 112 arrhythmia claims once the AHA 2024 paper is supplied

## Remaining: shared, later
- [ ] First 40 cases through catalogue and anonymiser, each checked by two people, including for any view that could show fetal sex
- [ ] Sweep trainer upgrade from schematic drawings to real planes
- [ ] Pilot with 15–20 fellows and colleagues
- [ ] Launch of the Detect tier

## Notes
Steps are from docs/06-build-plan.md. Daily detail is in the project's Progress notes and `docs/log.md`. Rules that never change: every claim has a source and a locator; only a named clinician raises a claim to expert-verified; the model that drafts a piece does not audit it; no patient media, names or fetal-sex information in the repo.

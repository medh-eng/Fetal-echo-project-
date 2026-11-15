# Clinic checks: one form, about 30 minutes

To be filled by the project owner at the clinic. Dr Kunda is needed only for the three lines marked **K**. Tick or write a number; rough answers are fine. Give the filled form to Claude.

No patient names, numbers or dates on this form.

## A. What is in the archive

| Question | Answer |
|---|---|
| Roughly how many pregnancies have stored cardiac images? | under 100 / 100-500 / 500-2000 / over 2000 |
| What is stored for a typical case? | stills only / stills and clips / clips and 4D volumes |
| Where are they? (tick all) | on the Voluson disk / DVDs / external drives / clinic computer / PACS |
| File types seen | JPG / BMP / AVI / MP4 / DICOM / Voluson volume (.vol) / not sure |
| Is there any list or register that says which cases were abnormal? | yes, electronic / yes, paper / no |
| **K** Roughly how many abnormal hearts are in the archive? | under 20 / 20-50 / 50-150 / over 150 |
| **K** Are outcomes after birth known for the abnormal cases? | most / some / few |

## B. What the Voluson can export

Use one **normal** case. Try each export and tick what works.

| Export | Works? | Notes |
|---|---|---|
| Clip as a video file (AVI or MP4) to USB | yes / no | file type and size: |
| Still as JPG or BMP to USB | yes / no | |
| DICOM to USB | yes / no | |
| 4D volume file to USB | yes / no | |
| Option to hide patient name at export ("anonymise", "hide patient data") | yes / no / not found | |
| Is the patient name inside the picture area, or only in the top banner? | banner only / inside the picture / both | |
| Screen size of an exported clip (right-click, Properties, Details) | ___ x ___ pixels | |

Then run the anonymiser on the exported clip (see `tools/clinic/README.md`) and look at the result with a second person. Write here whether any text remained: ____________

## C. Consent

| Question | Answer |
|---|---|
| Is there a signed consent form for each archive case? | all / most / some / none |
| Does the form mention use of images for teaching? | yes / no / some versions |
| Does it mention publication (book, online, app)? | yes / no / some versions |
| Does it mention commercial or paid use? | yes / no |
| **K** Is there a legal advisor the clinic already uses who can review this? | yes (name kept at clinic) / no |

Attach a blank copy of each version of the consent form (no patient details).

## What happens with the answers

- A decides how the catalogue is filled and how many cases to aim for first.
- B decides whether the anonymiser needs DICOM or 4D support and fixes the crop box.
- C decides which cases can be used at all. Until C is settled, no archive clip is published.

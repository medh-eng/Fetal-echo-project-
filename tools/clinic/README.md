# Clinic tools

These two tools run on the clinic computer. Nothing they produce is ever put in this repository.

## 1. Case catalogue (`catalogue.html`)

Copy the file to the clinic computer and open it in Chrome or Edge. No internet and no installation are needed.

- One row per case: code, gestation, views, modes, finding, quality, consent, where the original is, teaching note.
- The case code is random. Write the code beside the patient's entry in the clinic register; that register is the only link.
- The tool refuses text that looks like a date, an ID number, a name title or the sex of the fetus.
- Data is kept in that browser on that computer. Press **Export backup** at the end of every session and keep the file on the clinic drive.

## 2. Anonymiser (`anonymise.py`)

Set up once:

1. Install Python 3 from python.org (tick "Add to PATH").
2. In a command window: `pip install opencv-python numpy`
3. Install ffmpeg (so clips play in every browser).

For each exported clip or still:

1. `python anonymise.py preview EXPORT.avi` shows the picture size and saves a grid picture to help choose the crop box.
2. `python anonymise.py make EXPORT.avi --crop x,y,w,h --weeks 21 --view 4CV --mode 2D --finding normal` writes a clean clip, a details file and a check sheet into the folder `clean`.
3. Two different people look at the check sheet, play the whole clip, and each runs `python anonymise.py approve clean/FE-XXXXXX.json --initials XX`.

For a clip that is not normal, add `--region` with where the finding is (`situs`, `position-size`, `atria-veins`, `ventricles-septum`, `av-valves`, `outflow`, `vessels-arches`, `rhythm`). The clip drills use it for the question "where is the problem?".

What it removes: everything outside the crop box (the patient banner), any area given with `--mask`, all metadata, and sound. What it cannot do: notice a name burned into the middle of the image, or a frame that shows fetal sex. That is why two people check every clip.

The same crop box usually works for every export made with the same machine layout, so it only has to be chosen once per layout.

Tested on a made-up clip carrying a dummy name (15 Nov 2026). **Not yet tested on a real Voluson export.** Do the first real run on one normal case and look at the result together before doing more.

DICOM files and 4D volumes are not handled yet. This waits on the export check in `docs/07-clinic-checks.md`.

## 3. List of clips for the course app (`build_media.py`)

After clips have two checks each:

1. `python build_media.py clean` writes `clean/media.json`. It lists only clips checked by two different people, and tells you which it left out and why.
2. Clips kept for the pilot test must not appear in the drills. Put their codes in a text file, one per line, and add `--exclude that-file.txt`.
3. Upload the clip files and `media.json` into a folder called `media` beside the app's `index.html` on the hosting server. Pilot clips go into `media/pilot`. Never into the code repository.

The app then shows a "Clip drills" card. Tested with made-up clips only.

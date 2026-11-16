#!/usr/bin/env python3
"""Anonymiser for teaching clips. Runs on the clinic computer only.

Originals never leave the clinic. This program reads an exported clip or still,
keeps only the part of the picture you choose (so the patient banner is cut
off), blacks out any further areas you name, writes a new file with no
metadata and no sound, and makes a contact sheet for two people to check.

  1. See where to crop (saves the first frame with a ruler grid):
       python anonymise.py preview EXPORT.avi

  2. Make the anonymised clip:
       python anonymise.py make EXPORT.avi --crop 120,90,960,720 \
           --weeks 21 --view 4CV --mode 2D --finding normal
     Optional:  --mask x,y,w,h   black out an area inside the picture (repeatable)
                --out FOLDER     where clean files go        (default: clean)
                --key FOLDER     where the key file is kept  (default: key-keep-at-clinic)

  3. Two people look at the contact sheet and the clip, then each records a check:
       python anonymise.py approve clean/FE-XXXXXX.json --initials KS
       python anonymise.py approve clean/FE-XXXXXX.json --initials PS

A clip is ready for the course only when its .json shows two different checkers.

Needs:  pip install opencv-python numpy
Better: ffmpeg installed as well (gives files that play in every browser).

Crop and mask numbers are x,y,width,height in pixels of the original picture.
DICOM files are not handled yet; export as a video file or image for now.
"""
import argparse
import csv
import json
import secrets
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import cv2
import numpy as np

STILLS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}
VIEWS = ["abdomen", "4CV", "LVOT", "RVOT", "3VV", "3VT", "sweep", "arch-sagittal", "other"]
REGIONS = ["situs", "position-size", "atria-veins", "ventricles-septum", "av-valves", "outflow",
           "vessels-arches", "rhythm"]  # where the finding is; same codes as content/pilot/form.yaml
MODES = ["2D", "colour", "power", "PW", "CW", "M-mode", "3D-4D", "other"]
ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"  # no look-alike characters


def box(text):
    try:
        x, y, w, h = (int(v) for v in text.split(","))
    except ValueError:
        raise argparse.ArgumentTypeError("use x,y,width,height, for example 120,90,960,720")
    if w <= 0 or h <= 0 or x < 0 or y < 0:
        raise argparse.ArgumentTypeError("width and height must be positive; x and y not negative")
    return x, y, w, h


def frames(path):
    """Yield (frame, fps) for a video, or one frame for a still."""
    if path.suffix.lower() in STILLS:
        img = cv2.imread(str(path))
        if img is None:
            sys.exit(f"cannot read {path}")
        yield img, 0.0
        return
    cap = cv2.VideoCapture(str(path))
    if not cap.isOpened():
        sys.exit(f"cannot open {path}")
    fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        yield frame, fps
    cap.release()


def preview(a):
    src = Path(a.input)
    frame, _ = next(frames(src))
    h, w = frame.shape[:2]
    out = frame.copy()
    step = 100 if max(w, h) > 800 else 50
    for x in range(0, w, step):
        cv2.line(out, (x, 0), (x, h), (0, 255, 255), 1)
        cv2.putText(out, str(x), (x + 2, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 255), 1)
    for y in range(0, h, step):
        cv2.line(out, (0, y), (w, y), (0, 255, 255), 1)
        cv2.putText(out, str(y), (2, y + 14), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 255), 1)
    dest = Path(tempfile.gettempdir()) / "anonymise-preview.png"
    cv2.imwrite(str(dest), out)
    print(f"Picture is {w} x {h} pixels. Grid saved to {dest}")
    print("This preview still shows patient details. Delete it when you have your crop numbers.")
    print("Choose a crop box that holds the ultrasound image and none of the text around it.")


def new_code(out_dir):
    while True:
        code = "FE-" + "".join(secrets.choice(ALPHABET) for _ in range(6))
        if not (out_dir / f"{code}.json").exists():
            return code


def make(a):
    src = Path(a.input)
    out_dir, key_dir = Path(a.out), Path(a.key)
    out_dir.mkdir(parents=True, exist_ok=True)
    key_dir.mkdir(parents=True, exist_ok=True)
    if out_dir.resolve() == key_dir.resolve():
        sys.exit("the key folder must be different from the clean folder")
    code = new_code(out_dir)
    x, y, w, h = a.crop
    still = src.suffix.lower() in STILLS

    kept, fps, n = [], 0.0, 0
    writer, tmp = None, None
    for frame, fps in frames(src):
        fh, fw = frame.shape[:2]
        if x + w > fw or y + h > fh:
            sys.exit(f"crop {a.crop} does not fit inside the {fw} x {fh} picture")
        part = frame[y:y + h, x:x + w].copy()
        for mx, my, mw, mh in a.mask or []:
            # mask boxes are given in original-picture pixels
            x0, y0 = max(mx - x, 0), max(my - y, 0)
            x1, y1 = min(mx - x + mw, w), min(my - y + mh, h)
            if x1 > x0 and y1 > y0:
                part[y0:y1, x0:x1] = 0
        if still:
            cv2.imwrite(str(out_dir / f"{code}.png"), part)
        else:
            if writer is None:
                w2, h2 = w - w % 2, h - h % 2  # even size for video encoders
                tmp = out_dir / f"{code}.tmp.avi"
                writer = cv2.VideoWriter(str(tmp), cv2.VideoWriter_fourcc(*"MJPG"), fps, (w2, h2))
            writer.write(part[:h2, :w2])
        n += 1
        if n % max(1, int((fps or 25) // 2)) == 1 and len(kept) < 400:
            kept.append(part)
    if n == 0:
        sys.exit("no frames could be read")

    media = f"{code}.png"
    browser_safe = True
    if not still:
        writer.release()
        media = f"{code}.mp4"
        ff = shutil.which("ffmpeg")
        if ff:
            # -map_metadata -1: drop all metadata; -an: no sound; -bitexact: no encoder tags
            r = subprocess.run([ff, "-y", "-loglevel", "error", "-i", str(tmp), "-map_metadata", "-1",
                                "-map_chapters", "-1", "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p",
                                "-crf", "18", "-movflags", "+faststart", "-fflags", "+bitexact",
                                "-flags:v", "+bitexact", str(out_dir / media)])
            if r.returncode != 0:
                sys.exit("ffmpeg failed; nothing was written")
        else:
            browser_safe = False
            cap = cv2.VideoCapture(str(tmp))
            w2, h2 = int(cap.get(3)), int(cap.get(4))
            vw = cv2.VideoWriter(str(out_dir / media), cv2.VideoWriter_fourcc(*"mp4v"), fps, (w2, h2))
            while True:
                ok, f = cap.read()
                if not ok:
                    break
                vw.write(f)
            cap.release()
            vw.release()
        tmp.unlink()

    # contact sheet: up to 12 frames spread across the clip
    pick = [kept[i] for i in np.linspace(0, len(kept) - 1, min(12, len(kept))).astype(int)]
    tw = 320
    th = int(tw * h / w)
    cols = min(4, len(pick))
    rows = -(-len(pick) // cols)
    sheet = np.zeros((rows * th, cols * tw, 3), np.uint8)
    for i, f in enumerate(pick):
        r, c = divmod(i, cols)
        sheet[r * th:(r + 1) * th, c * tw:(c + 1) * tw] = cv2.resize(f, (tw, th))
    cv2.imwrite(str(out_dir / f"{code}.check.png"), sheet)

    side = {
        "code": code, "file": media, "kind": "still" if still else "clip",
        "gestation_weeks": a.weeks, "view": a.view, "mode": a.mode, "finding": a.finding,
        "region": a.region,
        "width": w if still else w - w % 2, "height": h if still else h - h % 2,
        "frames": n, "frame_rate": round(fps, 2) if not still else None,
        "masked_areas": len(a.mask or []), "plays_in_all_browsers": browser_safe,
        "labels": [], "teaching_note": "",
        "checks": [],  # two different people must be recorded here before use
    }
    (out_dir / f"{code}.json").write_text(json.dumps(side, indent=2) + "\n", encoding="utf-8")

    key = key_dir / "KEY-keep-at-clinic.csv"
    first = not key.exists()
    with open(key, "a", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        if first:
            wr.writerow(["code", "original_file"])
        wr.writerow([code, str(src.resolve())])

    print(f"\nMade {out_dir / media}  ({n} frame(s))")
    print(f"Check sheet: {out_dir / (code + '.check.png')}")
    print(f"Key (never leaves the clinic): {key}")
    if not browser_safe:
        print("NOTE: ffmpeg was not found, so this clip may not play in every browser. Install ffmpeg and remake.")
    print("\nNow two people each look at the check sheet AND play the whole clip. Confirm there is:")
    print("  - no name, ID, date, time, hospital or operator text anywhere in any frame")
    print("  - nothing that shows or hints at the sex of the fetus")
    print(f"Then each runs:  python anonymise.py approve {out_dir / (code + '.json')} --initials XX")


def approve(a):
    p = Path(a.sidecar)
    side = json.loads(p.read_text(encoding="utf-8"))
    who = a.initials.strip().upper()
    if any(c["by"] == who for c in side["checks"]):
        sys.exit(f"{who} has already checked this clip; the second check must be a different person")
    side["checks"].append({"by": who, "no_identity": True, "no_sex_information": True})
    p.write_text(json.dumps(side, indent=2) + "\n", encoding="utf-8")
    left = 2 - len(side["checks"])
    print(f"{side['code']}: check recorded for {who}. " +
          ("Ready for the course." if left <= 0 else f"{left} more check needed, by a different person."))


def main():
    ap = argparse.ArgumentParser(description="Anonymise ultrasound clips for teaching (clinic computer only).")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("preview", help="save the first frame with a pixel grid")
    p.add_argument("input")
    p.set_defaults(fn=preview)
    m = sub.add_parser("make", help="crop, mask, strip metadata, write clean file")
    m.add_argument("input")
    m.add_argument("--crop", type=box, required=True)
    m.add_argument("--mask", type=box, action="append")
    m.add_argument("--weeks", type=int, required=True, help="gestation in completed weeks")
    m.add_argument("--view", choices=VIEWS, required=True)
    m.add_argument("--mode", choices=MODES, required=True)
    m.add_argument("--finding", required=True, help="'normal' or a short description; no patient details")
    m.add_argument("--region", choices=REGIONS, help="for an abnormal clip: where the finding is (used by the clip drills)")
    m.add_argument("--out", default="clean")
    m.add_argument("--key", default="key-keep-at-clinic")
    m.set_defaults(fn=make)
    v = sub.add_parser("approve", help="record one person's check of a clean clip")
    v.add_argument("sidecar")
    v.add_argument("--initials", required=True)
    v.set_defaults(fn=approve)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()

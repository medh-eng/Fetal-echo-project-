#!/usr/bin/env python3
"""Build media.json for the course app from a folder of anonymised clips.

    python build_media.py clean            (writes clean/media.json)

Run at the clinic, on the folder the anonymiser wrote. A clip is listed only if its details file
records checks by two different people. Then upload the clips and media.json to the folder
`media/` beside the app's index.html on the hosting server. Never to the code repository.

Clips named in the pilot test must not be listed here: pass --exclude with a text file of
their codes (one per line).
"""
import argparse
import json
import sys
from pathlib import Path

PLANE = {"abdomen": "abdomen", "4CV": "4CV", "LVOT": "LVOT", "RVOT": "RVOT-3VV", "3VV": "RVOT-3VV", "3VT": "3VT"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--exclude", help="text file of clip codes kept for the pilot test")
    a = ap.parse_args()
    folder = Path(a.folder)
    held = set(Path(a.exclude).read_text().split()) if a.exclude else set()
    clips, refused = [], []
    for p in sorted(folder.glob("FE-*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        who = {c["by"] for c in d.get("checks", []) if c.get("no_identity") and c.get("no_sex_information")}
        if d["code"] in held:
            refused.append(f"{d['code']}: kept for the pilot test")
        elif len(who) < 2:
            refused.append(f"{d['code']}: {len(who)} of 2 checks")
        elif not (folder / d["file"]).exists():
            refused.append(f"{d['code']}: media file missing")
        elif d["finding"] != "normal" and not d.get("region"):
            refused.append(f"{d['code']}: abnormal clip with no --region label")
        else:
            clips.append({"code": d["code"], "file": d["file"], "kind": d["kind"], "weeks": d["gestation_weeks"],
                          "mode": d["mode"], "plane": PLANE.get(d["view"], "none"), "normal": d["finding"] == "normal",
                          "region": d.get("region"), "finding": d["finding"], "note": d.get("teaching_note", "")})
    (folder / "media.json").write_text(json.dumps({"clips": clips}, indent=1) + "\n", encoding="utf-8")
    print(f"listed {len(clips)} clip(s) in {folder / 'media.json'}")
    for r in refused:
        print("  left out  " + r)
    if not clips:
        sys.exit(1)


if __name__ == "__main__":
    main()

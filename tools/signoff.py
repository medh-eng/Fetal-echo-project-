#!/usr/bin/env python3
"""Record the editor's sign-off of a unit.

    python tools/signoff.py D1 --name "Dr Kunda Shahane" --date 2026-11-13 \
        --note "approval of review sheet, relayed by the project owner"

Marks every claim the unit uses as expert-verified and signs the unit.
Run this ONLY on the instruction of the named clinician, after she has gone
through dist/<unit>/review.md. An AI must never run it on its own judgement
(AGENTS.md rule 3). Claims she marked "change" or "remove" must be corrected
in the ledger first; list any to leave unsigned with --skip.
"""
import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def used_claims(u):
    out = []
    def add(refs):
        for r in refs or []:
            if r not in out:
                out.append(r)
    for s in u.get("sections", []):
        for b in s.get("blocks", []):
            add(b.get("claims"))
    for d in u.get("drills", []):
        add(d.get("claims"))
    for b in u.get("video", {}).get("beats", []):
        add(b.get("claims"))
    for c in u.get("checklist", {}).get("items", []):
        add(c.get("claims"))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("unit")
    ap.add_argument("--name", required=True)
    ap.add_argument("--date", required=True)
    ap.add_argument("--note", default="")
    ap.add_argument("--skip", nargs="*", default=[])
    a = ap.parse_args()

    upath = next((p for p in (ROOT / "content/units").glob("*.yaml")
                  if yaml.safe_load(p.read_text(encoding="utf-8"))["id"] == a.unit), None)
    if not upath:
        sys.exit(f"no unit {a.unit}")
    unit = yaml.safe_load(upath.read_text(encoding="utf-8"))
    want = [c for c in used_claims(unit) if c not in a.skip]
    who = f"{a.name}, {a.date}" + (f" ({a.note})" if a.note else "")
    done = set()

    for lp in sorted((ROOT / "content/ledger").glob("*.yaml")):
        text = lp.read_text(encoding="utf-8")
        parts = re.split(r"(?m)^(?=- id: )", text)
        for i, part in enumerate(parts):
            m = re.match(r"- id: (\S+)", part)
            if not m or m.group(1) not in want:
                continue
            part = re.sub(r"(?m)^  status: .*$", "  status: expert-verified", part)
            if re.search(r"(?m)^  checked_by: null$", part):
                part = re.sub(r"(?m)^  checked_by: null$",
                              f'  checked_by: "{a.name} (editor review of the unit review sheet; '
                              f'no separate AI cross-check recorded)"', part)
            part = re.sub(r"(?m)^  verified_by: .*$", f'  verified_by: "{who}"', part)
            parts[i] = part
            done.add(m.group(1))
        lp.write_text("".join(parts), encoding="utf-8")

    missing = [c for c in want if c not in done]
    if missing:
        sys.exit(f"claims not found in ledger: {missing}")
    utext = upath.read_text(encoding="utf-8")
    utext = re.sub(r"(?m)^signed_by: .*$", f'signed_by: "{who}"', utext)
    upath.write_text(utext, encoding="utf-8")
    print(f"{a.unit}: {len(done)} claims marked expert-verified; unit signed by {who}")
    if a.skip:
        print(f"left unsigned: {', '.join(a.skip)}")


if __name__ == "__main__":
    main()

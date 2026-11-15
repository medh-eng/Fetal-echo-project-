#!/usr/bin/env python3
"""Apply a cross-check result table to the ledger.

    python tools/apply_crosscheck.py results.csv --by "ChatGPT (GPT-x, 2026-11-16)"

results.csv has a header row and three columns:  claim_id,verdict,detail
Verdicts (prompts/02-crosscheck.md): CONFIRMED, CORRECT LOCATOR, DISTORTED, NOT FOUND.

What happens to each claim:
  CONFIRMED         ai-extracted -> ai-cross-checked; checked_by recorded.
  CORRECT LOCATOR   status unchanged; the proposed locator is written into `note`
                    for a person or the harvesting model to confirm.
  DISTORTED / NOT FOUND   status unchanged; a DISPUTE is written into `note`.

The checker must be a different model from the extractor (AGENTS.md rule 4).
Claims already expert-verified are never changed in status; a non-confirming
verdict on one of them is written into `note` and reported, for the editor.
"""
import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERDICTS = {"CONFIRMED", "CORRECT LOCATOR", "DISTORTED", "NOT FOUND"}


def field(part, name):
    m = re.search(rf"(?m)^  {name}: (.*(?:\n    .*)*)$", part)
    return m.group(1) if m else None


def set_field(part, name, value):
    line = f"  {name}: {json.dumps(value, ensure_ascii=False)}"
    if re.search(rf"(?m)^  {name}: ", part):
        return re.sub(rf"(?m)^  {name}: .*(?:\n    .*)*$", lambda _: line, part, count=1)
    return part.rstrip("\n") + "\n" + line + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--by", required=True, help='checker, e.g. "ChatGPT (model, date)"')
    a = ap.parse_args()

    rows = {}
    with open(a.csv, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            cid = (r.get("claim_id") or "").strip()
            verdict = (r.get("verdict") or "").strip().upper()
            if not cid:
                continue
            if verdict not in VERDICTS:
                sys.exit(f"{cid}: unknown verdict '{verdict}'")
            rows[cid] = (verdict, (r.get("detail") or "").strip())

    seen, report = set(), {v: [] for v in VERDICTS}
    for lp in sorted((ROOT / "content/ledger").glob("*.yaml")):
        text = lp.read_text(encoding="utf-8")
        parts = re.split(r"(?m)^(?=- id: )", text)
        for i, part in enumerate(parts):
            m = re.match(r"- id: (\S+)", part)
            if not m or m.group(1) not in rows:
                continue
            cid = m.group(1)
            verdict, detail = rows[cid]
            seen.add(cid)
            status = (field(part, "status") or "").strip()
            extractor = (field(part, "extracted_by") or "").strip().strip('"')
            if extractor and extractor.split(",")[0].split("(")[0].strip().lower() == \
                    a.by.split(",")[0].split("(")[0].strip().lower():
                sys.exit(f"{cid}: checker '{a.by}' is the same model as the extractor '{extractor}'")
            if verdict == "CONFIRMED":
                if status == "ai-extracted":
                    part = re.sub(r"(?m)^  status: .*$", "  status: ai-cross-checked", part, count=1)
                    part = set_field(part, "checked_by", a.by)
            else:
                old = field(part, "note")
                old = "" if old in (None, "null") else re.sub(r"\s+", " ", old).strip().strip("'\"") + " "
                label = "LOCATOR" if verdict == "CORRECT LOCATOR" else "DISPUTE"
                part = set_field(part, "note", f"{old}{label} ({a.by}): {verdict}. {detail}".strip())
                if status == "expert-verified":
                    print(f"ATTENTION: {cid} is expert-verified but the cross-check says {verdict}. "
                          "Show the editor.")
            parts[i] = part
            report[verdict].append(cid)
        lp.write_text("".join(parts), encoding="utf-8")

    for v in ("CONFIRMED", "CORRECT LOCATOR", "DISTORTED", "NOT FOUND"):
        print(f"{v}: {len(report[v])}" + (f"  ({', '.join(report[v])})" if v != "CONFIRMED" and report[v] else ""))
    missing = sorted(set(rows) - seen)
    if missing:
        print(f"not in ledger: {', '.join(missing)}")
    print("Now run: python tools/build.py")


if __name__ == "__main__":
    main()

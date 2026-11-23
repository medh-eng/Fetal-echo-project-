#!/usr/bin/env python3
"""Regression checks for the round-5 fetal-echo evidence and draft-unit handoff.

These checks test traceability and quiz-key integrity; they are not medical sign-off.
Run after python tools/build.py, or independently with PyYAML installed.
"""
import csv
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
UNIT_IDS = (
    "Z2", "XB4", "XB2", "XB1", "XB8", "XB3",
    "XB5", "XA6", "Z3", "XA2", "Z1", "Z5",
)


def main():
    claims = {}
    for p in (ROOT / "content/ledger").glob("*.yaml"):
        for c in (yaml.safe_load(p.read_text(encoding="utf-8")) or {}).get("claims", []):
            assert c["id"] not in claims, f"Duplicate claim ID: {c['id']}"
            claims[c["id"]] = c

    with (ROOT / "tasks/results/task-j.csv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 57, f"Expected 57 Task J findings, got {len(rows)}"
    counts = {}
    for row in rows:
        verdict, claim_id = row["verdict"], row["claim_id"]
        counts[verdict] = counts.get(verdict, 0) + 1
        c = claims[claim_id]
        if verdict == "CONFIRMED":
            assert c["status"] in ("ai-cross-checked", "expert-verified"), claim_id
            assert c.get("checked_by"), claim_id
        else:
            assert c["status"] == "ai-extracted", claim_id
    assert counts == {"CONFIRMED": 53, "CORRECT LOCATOR": 3, "DISTORTED": 1}, counts

    all_drills = []
    for unit_id in UNIT_IDS:
        matches = list((ROOT / "content/units").glob(f"{unit_id}-*.yaml"))
        assert len(matches) == 1, (unit_id, matches)
        u = yaml.safe_load(matches[0].read_text(encoding="utf-8"))
        assert u["id"] == unit_id
        assert not u.get("signed_by") or u.get("audited_by"), f"Signed without audit: {unit_id}"

        pieces = []
        for section in u.get("sections", []):
            pieces.extend(section.get("blocks", []))
        pieces.extend(u.get("drills", []))
        pieces.extend((u.get("checklist") or {}).get("items", []))
        pieces.extend((u.get("video") or {}).get("beats", []))

        for piece in pieces:
            for claim_id in piece.get("claims") or []:
                assert claim_id in claims, (unit_id, "missing claim", claim_id)
                assert claims[claim_id]["status"] != "ai-extracted", (
                    unit_id, "uncross-checked claim cited", claim_id
                )

        for d in u.get("drills", []):
            assert d["id"] not in all_drills, f"Repeated drill: {d['id']}"
            all_drills.append(d["id"])
            assert len(d["options"]) == 4, (unit_id, d["id"])
            assert len(set(d["options"])) == 4, (unit_id, d["id"])
            assert isinstance(d.get("answer"), int), (unit_id, d["id"])
            assert 0 <= d["answer"] < 4, (unit_id, d["id"])
            assert d.get("explanation") and d.get("claims"), d["id"]

    assert len(all_drills) == 109, f"Expected 109 Task K drills, got {len(all_drills)}"

    # The source file can store any answer index because both teaching interfaces
    # shuffle labelled answers, not merely the visible strings.
    app = (ROOT / "tools/templates/app.html").read_text(encoding="utf-8")
    page = (ROOT / "tools/build.py").read_text(encoding="utf-8")
    labelled_shuffle = "shuffle(it.options.map((text, i) => ({ text, correct: i === it.answer })))"
    assert labelled_shuffle in app, "App must shuffle answers together with correctness"
    assert labelled_shuffle in page, "Study page must shuffle answers together with correctness"
    print(f"Round-5 checks passed: {len(rows)} Task J claims; "
          f"{len(UNIT_IDS)} audited units; {len(all_drills)} drills with intact keys.")


if __name__ == "__main__":
    main()

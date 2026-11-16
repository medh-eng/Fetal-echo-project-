#!/usr/bin/env python3
"""Score the pilot test (docs/08-pilot-protocol.md).

    python tools/pilot_score.py FOLDER_OF_RESULT_CSVS [--out pilot-results]

Reads every pilot-*.csv saved from the test page, compares the answers with the editor's key in
content/pilot/set-*.yaml, and writes:
    participants.csv   one row per participant and sitting
    summary.md         before against after, each learner compared with themselves
    items.csv          how often each clip was answered correctly (to find bad clips)

Refuses to run if a key is incomplete or unsigned. Result files hold participant codes only;
keep them out of this repository all the same.
"""
import argparse
import csv
import statistics
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def load_keys():
    keys, problems = {}, []
    for path in sorted((ROOT / "content/pilot").glob("set-*.yaml")):
        d = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not d.get("key_signed_by"):
            problems.append(f"{path.name}: key_signed_by is empty")
        for it in d["items"]:
            k = it.get("key") or {}
            if k.get("plane") is None or k.get("normal") is None or (k["normal"] is False and not k.get("region")):
                problems.append(f"{path.name}: item {it['id']} has an incomplete key")
            keys[it["id"]] = k
    return keys, problems


def share(n, d):
    return round(n / d, 3) if d else ""


def score(rows, keys):
    """rows: the answers of one participant in one sitting."""
    r = dict(items=0, plane_ok=0, abnormal=0, caught=0, normal=0, passed=0, located=0, sure_wrong=0, sure=0, secs=[])
    for a in rows:
        k = keys.get(a["item"])
        if k is None:
            continue
        said_normal = a["normal"] == "normal"
        r["items"] += 1
        r["plane_ok"] += a["plane"] == k["plane"]
        r["secs"].append(float(a["seconds"] or 0))
        if k["normal"]:
            r["normal"] += 1
            r["passed"] += said_normal
        else:
            r["abnormal"] += 1
            if not said_normal:
                r["caught"] += 1
                r["located"] += a["region"] == k["region"]
        if a["sure"] == "3":
            r["sure"] += 1
            r["sure_wrong"] += said_normal != bool(k["normal"])
    return {
        "items": r["items"],
        "plane_correct": share(r["plane_ok"], r["items"]),
        "abnormal_caught": share(r["caught"], r["abnormal"]),
        "normal_passed": share(r["passed"], r["normal"]),
        "located_of_caught": share(r["located"], r["caught"]),
        "very_sure_and_wrong": share(r["sure_wrong"], r["sure"]),
        "median_seconds": round(statistics.median(r["secs"]), 1) if r["secs"] else "",
    }


MEASURES = ["plane_correct", "abnormal_caught", "normal_passed", "located_of_caught", "very_sure_and_wrong", "median_seconds"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--out", default="pilot-results")
    ap.add_argument("--allow-unsigned", action="store_true", help="for a dry run with a made-up key only")
    a = ap.parse_args()
    keys, problems = load_keys()
    if problems and not a.allow_unsigned:
        sys.exit("The answer key is not ready:\n  " + "\n  ".join(problems[:12]) +
                 ("\n  ..." if len(problems) > 12 else ""))
    sittings, forms, per_item = {}, {}, {}
    for f in sorted(Path(a.folder).glob("*.csv")):
        with open(f, newline="", encoding="utf-8-sig") as fh:
            for row in csv.DictReader(fh):
                who = (row["participant"], row["sitting"])
                if row["item"].startswith("form:"):
                    forms.setdefault(row["participant"], {})[row["item"][5:]] = row["plane"]
                else:
                    sittings.setdefault(who, {"set": row["set"], "rows": []})["rows"].append(row)
                    k = keys.get(row["item"])
                    if k and k.get("normal") is not None:
                        t = per_item.setdefault(row["item"], [0, 0, 0])
                        t[0] += 1
                        t[1] += row["plane"] == k["plane"]
                        t[2] += (row["normal"] == "normal") == bool(k["normal"])
    if not sittings:
        sys.exit("No result files found.")
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    scored = {who: dict(score(v["rows"], keys), set=v["set"]) for who, v in sittings.items()}
    with open(out / "participants.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["participant", "sitting", "set", "items"] + MEASURES + ["specialty", "years", "scans", "training"])
        for (p, s), r in sorted(scored.items()):
            fm = forms.get(p, {})
            w.writerow([p, s, r["set"], r["items"]] + [r[m] for m in MEASURES] + [fm.get(k, "") for k in ("specialty", "years", "scans", "training")])
    with open(out / "items.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["item", "answers", "plane_correct", "normal_call_correct"])
        for i, (n, pl, nm) in sorted(per_item.items()):
            w.writerow([i, n, share(pl, n), share(nm, n)])
    pairs = sorted(p for (p, s) in scored if s == "1" and (p, "2") in scored)
    lines = ["# Pilot results", "",
             f"{len({p for p, _ in scored})} participant(s); {len(pairs)} with both tests. "
             "Each learner is compared with themselves. With this number of learners the result is a direction and a size, not proof.", ""]
    if pairs:
        lines += ["| Measure | Before (median) | After (median) | Median change | Range of change | Improved / same / worse |", "|---|---|---|---|---|---|"]
        for m in MEASURES:
            d = [(scored[(p, "1")][m], scored[(p, "2")][m]) for p in pairs]
            d = [(b, c) for b, c in d if b != "" and c != ""]
            if not d:
                continue
            ch = [round(c - b, 3) for b, c in d]
            better = (lambda x: x < 0) if m in ("very_sure_and_wrong", "median_seconds") else (lambda x: x > 0)
            lines.append(f"| {m.replace('_', ' ')} | {round(statistics.median(b for b, _ in d), 3)} | {round(statistics.median(c for _, c in d), 3)} | "
                         f"{round(statistics.median(ch), 3)} | {min(ch)} to {max(ch)} | "
                         f"{sum(better(x) for x in ch)} / {sum(x == 0 for x in ch)} / {sum(not better(x) and x != 0 for x in ch)} |")
        order = {}
        for p in pairs:
            order.setdefault(scored[(p, "1")]["set"], []).append(p)
        lines += ["", "First test by set: " + ", ".join(f"set {k}: {len(v)}" for k, v in sorted(order.items())) +
                  ". The two groups should be about equal in size (crossover)."]
    else:
        lines.append("No participant has both tests yet.")
    fb = [(p, k, v) for p, f in sorted(forms.items()) for k, v in f.items() if k in ("helped", "not_helped", "missing", "change", "recommend") and v]
    if fb:
        lines += ["", "## What learners said", ""] + [f"- {p}, {k.replace('_', ' ')}: {v}" for p, k, v in fb]
    (out / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"scored {len(scored)} sitting(s), {len(pairs)} paired -> {out}/")


if __name__ == "__main__":
    main()

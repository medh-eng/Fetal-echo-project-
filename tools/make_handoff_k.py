#!/usr/bin/env python3
"""Write one file for task K (audit of the twelve 21 Nov units) for a non-Claude model.

    python tools/make_handoff_k.py

Output: tasks/handoff/task-k-bundle.md = the audit prompt, then for each unit its
source file (text, drills, citations) and the claims it cites, with statements and
locators. Replaces attaching the two ledgers whole.
"""
import glob
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
UNITS = ["Z2", "XB4", "XB2", "XB1", "XB8", "XB3", "XB5", "XA6", "Z3", "XA2", "Z1", "Z5"]

claims = {}
for f in glob.glob(str(ROOT / "content/ledger/*.yaml")):
    for c in yaml.safe_load(open(f, encoding="utf-8"))["claims"]:
        claims[c["id"]] = c

prompt = (ROOT / "prompts/04-audit.md").read_text(encoding="utf-8")
task = (ROOT / "tasks/chatgpt-tasks-round5.md").read_text(encoding="utf-8")
m = re.search(r"## Task K.*?```\n(.*?)```", task, re.S)
out = ["# Task K bundle: audit twelve units", "", "Auditor must not be Claude.", "",
       "## Instructions", "", m.group(1).strip(), "", "## Audit prompt (prompts/04-audit.md)", "", prompt.strip(), ""]
for u in UNITS:
    p = glob.glob(str(ROOT / f"content/units/{u}-*.yaml"))[0]
    text = Path(p).read_text(encoding="utf-8")
    ids = sorted(set(re.findall(r"\b(?:AS23|AH14|IS23|ED)-\d+\b", text)))
    out += [f"---", f"## Unit {u}", "", "### Unit file", "", "```yaml", text.strip(), "```", "",
            "### Claims cited (with ledger statement and locator)", "",
            "| id | status | statement | locator |", "|---|---|---|---|"]
    for i in ids:
        c = claims.get(i)
        if c:
            s = c["statement"].replace("|", "/").replace("\n", " ")
            out.append(f"| {i} | {c['status']} | {s} | {c['locator']} |")
        else:
            out.append(f"| {i} | NOT IN LEDGER | | |")
    out.append("")
dest = ROOT / "tasks/handoff/task-k-bundle.md"
dest.write_text("\n".join(out), encoding="utf-8")
print(dest, dest.stat().st_size, "bytes")

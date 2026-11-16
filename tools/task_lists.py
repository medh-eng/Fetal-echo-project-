#!/usr/bin/env python3
"""Write the claim lists that go with cross-check tasks for other models.

    python tools/task_lists.py

tasks/claims-for-chatgpt-or-gemini.md   claims extracted or reworded by Claude, not yet cross-checked
tasks/claims-for-claude-or-gemini.md    claims extracted by ChatGPT, not yet cross-checked

The model that extracted a claim never cross-checks it (AGENTS.md rule 4).
"""
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def main():
    groups = {"claude": {}, "chatgpt": {}}
    for f in sorted((ROOT / "content/ledger").glob("*.yaml")):
        d = yaml.safe_load(f.read_text(encoding="utf-8"))
        for c in d["claims"]:
            if c["status"] != "ai-extracted":
                continue
            fam = (re.match(r"[A-Za-z]+", c.get("extracted_by") or "") or [""])[0].lower()
            if fam in groups:
                groups[fam].setdefault(d["source"], []).append(c)
    for fam, name, who in (("claude", "claims-for-chatgpt-or-gemini.md", "Claude"),
                           ("chatgpt", "claims-for-claude-or-gemini.md", "ChatGPT")):
        n = sum(len(v) for v in groups[fam].values())
        out = [f"# Claims awaiting cross-check: extracted by {who}", "",
               f"{n} claims. Attach this file together with the guideline PDFs. "
               f"The checker must not be {who}.", ""]
        for src, cs in groups[fam].items():
            out += [f"## Source: {src} ({len(cs)} claims)", "", "| claim_id | statement | locator given |", "|---|---|---|"]
            for c in cs:
                note = f" (Note: {c['note']})" if c.get("note") else ""
                out.append(f"| {c['id']} | {c['statement']}{note} | {c['locator']} |")
            out.append("")
        (ROOT / "tasks" / name).write_text("\n".join(out), encoding="utf-8")
        print(f"{name}: {n} claims")


if __name__ == "__main__":
    main()

"""One sign-off pack for the editor-in-chief, covering every unsigned unit.

Called from build.py. Writes dist/editor/review-pack.md and .html.
Each claim that still needs her check appears once, however many units use it,
so that her time is spent once per fact.
"""
import html
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
e = html.escape


def used(u):
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


def build(units, claims):
    pending_units = [u for u in units if not u.get("signed_by")]
    qpath = ROOT / "content/editor/questions.yaml"
    questions = (yaml.safe_load(qpath.read_text(encoding="utf-8")) or []) if qpath.exists() else []

    where = {}
    for u in pending_units:
        for cid in used(u):
            if claims[cid]["status"] != "expert-verified":
                where.setdefault(cid, []).append(u["id"])
    flagged = [c for c in sorted(where) if claims[c].get("note")]
    plain = [c for c in sorted(where) if not claims[c].get("note")]

    md = ["# Editor's review pack", "",
          "For Dr Kunda Shahane, editor-in-chief. Everything that needs her decision or signature is in this one document.",
          "Each claim appears once, even if several units use it. Claims she has already verified are not repeated.", "",
          f"**{len(pending_units)} unit(s) awaiting signature. {len(where)} claim(s) to check. {len(questions)} decision(s).**", ""]

    md += ["## Part A. Decisions", ""]
    if not questions:
        md += ["None open.", ""]
    for q in questions:
        md += [f"**{q['id']}. {q['question']}**", ""]
        md += [f"- [ ] {o}" for o in q.get("options", [])]
        md += ["", f"If no answer: {q['default']}", f"Affects: {q['affects']}", ""]

    md += ["## Part B. Units awaiting signature", "",
           "| Unit | Title | Claims used | Already verified | In this pack | Sign |", "|---|---|---|---|---|---|"]
    for u in pending_units:
        cs = used(u)
        done = sum(1 for c in cs if claims[c]["status"] == "expert-verified")
        md.append(f"| {u['id']} | {u['title']} | {len(cs)} | {done} | {len(cs) - done} | |")
    md += ["", "Read each unit as the learner will see it in `dist/<unit>/chapter.md`, or in the app.", ""]

    def table(ids):
        rows = ["| Claim | Statement | Where in source | AI check | Used in | OK / change / remove |",
                "|---|---|---|---|---|---|"]
        for cid in ids:
            c = claims[cid]
            checked = "cross-checked" if c["status"] == "ai-cross-checked" else "not yet"
            note = f" **Note:** {c['note']}" if c.get("note") else ""
            rows.append(f"| {cid} | {c['statement']}{note} | {c['source']}: {c['locator']} | {checked} | "
                        f"{', '.join(where[cid])} | |")
        return rows

    md += ["## Part C. Claims to check", "",
           "Mark each: OK / change (write the correction) / remove.", ""]
    if flagged:
        md += ["### Read these first (flagged)", ""] + table(flagged) + [""]
    md += ["### All other claims", ""] + table(plain) + [""]
    md += ["## Signature", "",
           "I have checked the claims above and approve these units for release, except where marked:", "",
           "Units: " + "   ".join(f"[ ] {u['id']}" for u in pending_units), "",
           "Signed: ____________________   Date: __________", ""]

    out = ROOT / "dist" / "editor"
    out.mkdir(parents=True, exist_ok=True)
    text = "\n".join(md)
    (out / "review-pack.md").write_text(text, encoding="utf-8")
    (out / "review-pack.html").write_text(to_html(md), encoding="utf-8")
    print(f"built editor pack: {len(pending_units)} unit(s), {len(where)} claim(s) -> dist/editor/")


def inline(s):
    s = e(s)
    out, bold = [], False
    for i, part in enumerate(s.split("**")):
        out.append(part if i % 2 == 0 else f"<strong>{part}</strong>")
    s = "".join(out)
    return s.replace("[ ]", "&#9744;")


def to_html(lines):
    body, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("### "):
            body.append(f"<h3>{inline(ln[4:])}</h3>")
        elif ln.startswith("## "):
            body.append(f"<h2>{inline(ln[3:])}</h2>")
        elif ln.startswith("# "):
            body.append(f"<h1>{inline(ln[2:])}</h1>")
        elif ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head, rest = rows[0], rows[2:]
            body.append("<table><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr>" +
                        "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rest) +
                        "</table>")
            continue
        elif ln.startswith("- "):
            body.append(f"<p class='opt'>{inline(ln[2:])}</p>")
        elif ln.strip():
            body.append(f"<p>{inline(ln)}</p>")
        i += 1
    return ("<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
            "<meta name='viewport' content='width=device-width, initial-scale=1'>"
            "<meta name='robots' content='noindex'><title>Editor's review pack</title><style>"
            "body{font:15px/1.5 Georgia,serif;color:#1c2430;max-width:1000px;margin:0 auto;padding:20px}"
            "h1{font-size:1.6rem}h2{font-size:1.2rem;margin-top:1.8em;border-bottom:1px solid #d9dee5}"
            "table{border-collapse:collapse;width:100%;font:13px/1.4 system-ui,sans-serif;margin:10px 0}"
            "th,td{border:1px solid #c9cfd8;padding:5px 7px;text-align:left;vertical-align:top}th{background:#eee}"
            "td:last-child{min-width:110px}.opt{margin:.2em 0 .2em 1em}"
            "@media print{body{font-size:11pt;max-width:none}tr{break-inside:avoid}}"
            "</style></head><body>" + "\n".join(body) + "</body></html>\n")

#!/usr/bin/env python3
"""Validate the evidence ledger and build every output from one source.

    python tools/build.py              # validate, then build drafts into dist/
    python tools/build.py --check      # validate only
    python tools/build.py --release    # fail unless every claim is expert-verified

Outputs per unit in dist/<unit>/:
    chapter.md        book chapter with numbered references
    drills.json       study items for the app
    video-script.md   shot list and narration
    study.html        self-contained study page (open in any browser)
    review.md         sign-off sheet for the editor-in-chief
"""
import argparse
import html
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
ROOT = Path(__file__).resolve().parent.parent
STATUSES = ["ai-extracted", "ai-cross-checked", "expert-verified"]


def load(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate(release=False):
    """Return (errors, warnings, sources, claims_by_id, units)."""
    errors, warnings = [], []
    sources = load(ROOT / "content/sources/sources.yaml") or {}
    claims = {}

    for path in sorted((ROOT / "content/ledger").glob("*.yaml")):
        data = load(path) or {}
        for c in data.get("claims", []):
            cid = c.get("id", "?")
            where = f"{path.name}:{cid}"
            if cid in claims:
                errors.append(f"{where}: duplicate claim id")
            claims[cid] = c
            for field in ("statement", "source", "locator", "status"):
                if not c.get(field):
                    errors.append(f"{where}: missing '{field}'")
            if c.get("source") and c["source"] not in sources:
                errors.append(f"{where}: unknown source '{c['source']}'")
            status = c.get("status")
            if status and status not in STATUSES:
                errors.append(f"{where}: bad status '{status}'")
            if status in ("ai-cross-checked", "expert-verified") and not c.get("checked_by"):
                errors.append(f"{where}: status '{status}' needs checked_by")
            if status == "expert-verified" and not c.get("verified_by"):
                errors.append(f"{where}: expert-verified needs verified_by")
            if c.get("extracted_by") and c.get("extracted_by") == c.get("checked_by"):
                errors.append(f"{where}: checker must differ from extractor")
            if release and status != "expert-verified":
                errors.append(f"{where}: not expert-verified (release build)")

    units = []
    for path in sorted((ROOT / "content/units").glob("*.yaml")):
        u = load(path)
        units.append(u)
        used = set()

        def check_refs(refs, where, framing=False):
            if not refs and not framing:
                errors.append(f"{where}: clinical content with no claims")
            for r in refs or []:
                used.add(r)
                if r not in claims:
                    errors.append(f"{where}: cites unknown claim '{r}'")

        for s in u.get("sections", []):
            for i, b in enumerate(s.get("blocks", []), 1):
                check_refs(b.get("claims"), f"{path.name}:'{s['heading']}' block {i}",
                           framing=b.get("kind") == "framing")
        for d in u.get("drills", []):
            check_refs(d.get("claims"), f"{path.name}:{d.get('id')}")
            if not 0 <= d.get("answer", -1) < len(d.get("options", [])):
                errors.append(f"{path.name}:{d.get('id')}: answer index out of range")
        for i, b in enumerate(u.get("video", {}).get("beats", []), 1):
            check_refs(b.get("claims"), f"{path.name}:video beat {i}", framing=True)
        for i, c in enumerate(u.get("checklist", {}).get("items", []), 1):
            check_refs(c.get("claims"), f"{path.name}:checklist item {i}")

        unused = [c for c in claims if c.startswith(u["id"] + "-") and c not in used]
        if unused:
            warnings.append(f"{path.name}: claims never used: {', '.join(unused)}")
        if release and not u.get("signed_by"):
            errors.append(f"{path.name}: unit not signed (release build)")
        for m in u.get("missing_claims", []):
            warnings.append(f"{path.name}: MISSING CLAIM - {m}")

    return errors, warnings, sources, claims, units


def unit_status(unit, claims):
    """Lowest status among the claims a unit uses."""
    used = set()
    for s in unit.get("sections", []):
        for b in s.get("blocks", []):
            used.update(b.get("claims") or [])
    for d in unit.get("drills", []):
        used.update(d.get("claims") or [])
    for c in unit.get("checklist", {}).get("items", []):
        used.update(c.get("claims") or [])
    for b in unit.get("video", {}).get("beats", []):
        used.update(b.get("claims") or [])
    levels = [STATUSES.index(claims[c]["status"]) for c in used if c in claims]
    return STATUSES[min(levels)] if levels else "ai-extracted"


def banner(status):
    if status == "expert-verified":
        return "Verified content."
    return ("DRAFT - NOT FOR CLINICAL USE. Contains claims with status "
            f"'{status}' that no clinician has verified.")


def cite(src):
    parts = [src.get("authors"), src.get("title"), src.get("journal")]
    tail = " ".join(str(x) for x in [src.get("year"), src.get("volume")] if x)
    if src.get("pages"):
        tail += f":{src['pages']}"
    text = ". ".join(p for p in parts if p)
    if tail.strip():
        text += f". {tail.strip()}"
    if src.get("doi"):
        text += f". doi:{src['doi']}"
    return text


def build_chapter(u, claims, sources, status):
    order = []

    def marks(refs):
        out = []
        for r in refs or []:
            if r not in order:
                order.append(r)
            out.append(str(order.index(r) + 1))
        return f" [{', '.join(out)}]" if out else ""

    lines = [f"# {u['title']}", "", f"> {banner(status)}", "",
             f"Unit {u['id']} | Tier: {u['tier']} | Version {u['version']}", "",
             "## You will be able to", ""]
    lines += [f"- {o}" for o in u.get("objectives", [])]
    for s in u.get("sections", []):
        lines += ["", f"## {s['heading']}", ""]
        for b in s.get("blocks", []):
            lines += [b["text"] + marks(b.get("claims")), ""]
            t = b.get("table")
            if t:
                lines += ["| " + " | ".join(t["columns"]) + " |",
                          "|" + "---|" * len(t["columns"])]
                lines += ["| " + " | ".join(r) + " |" for r in t["rows"]] + [""]
    ck = u.get("checklist")
    if ck:
        lines += [f"## {ck['title']}", ""]
        lines += [f"- [ ] {i['text']}" + marks(i.get("claims")) for i in ck["items"]] + [""]
    if u.get("missing_claims"):
        lines += ["## Still to be written (awaiting sourced claims)", ""]
        lines += [f"- {m}" for m in u["missing_claims"]]
        lines.append("")
    lines += ["## References", ""]
    for i, cid in enumerate(order, 1):
        c = claims[cid]
        lines.append(f"{i}. {cite(sources[c['source']])} - {c['locator']}. "
                     f"*Claim {cid}, {c['status']}.*")
    return "\n".join(lines) + "\n"


def build_drills(u, claims, status):
    return {
        "unit": u["id"], "title": u["title"], "status": status,
        "items": [{
            "id": d["id"], "question": d["question"], "options": d["options"],
            "answer": d["answer"], "explanation": d["explanation"],
            "claims": d["claims"],
            "status": STATUSES[min(STATUSES.index(claims[c]["status"]) for c in d["claims"])],
        } for d in u.get("drills", [])],
    }


def build_review(u, claims, sources):
    """Sign-off sheet for the editor: every claim the unit uses, grouped by status."""
    used = []
    def add(refs):
        for r in refs or []:
            if r not in used:
                used.append(r)
    for s in u.get("sections", []):
        for b in s.get("blocks", []):
            add(b.get("claims"))
    for d in u.get("drills", []):
        add(d.get("claims"))
    for b in u.get("video", {}).get("beats", []):
        add(b.get("claims"))
    for c in u.get("checklist", {}).get("items", []):
        add(c.get("claims"))
    lines = [f"# Review sheet: {u['id']} {u['title']}", "",
             "For the editor-in-chief. Check each claim against the source at the place given.",
             "Mark: OK / change (write the correction) / remove.", "",
             f"{len(used)} claims used in this unit.", "",
             "| Claim | Statement | Where in source | Status | Editor |", "|---|---|---|---|---|"]
    for cid in sorted(used):
        c = claims[cid]
        lines.append(f"| {cid} | {c['statement']} | {c['source']}: {c['locator']} | {c['status']} | |")
    lines += ["", "Signed: ____________________   Date: __________"]
    return "\n".join(lines) + "\n"


def build_video(u, status):
    v = u.get("video")
    if not v:
        return None
    lines = [f"# Video script: {v['title']}", "", f"> {banner(status)}", "",
             f"Unit {u['id']} | Target length: {v['target_minutes']} min", "",
             "| # | Shot | Narration | Claims |", "|---|---|---|---|"]
    for i, b in enumerate(v["beats"], 1):
        lines.append(f"| {i} | {b['shot']} | {b['narration']} | "
                     f"{', '.join(b.get('claims') or []) or '-'} |")
    return "\n".join(lines) + "\n"


PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>
:root{--ink:#1c2430;--mute:#5d6b7a;--line:#d9dee5;--bg:#f6f4ef;--card:#fff;--accent:#9b2c3f;--ok:#1f6f4a;--bad:#a23b2a}
*{box-sizing:border-box}body{margin:0;font:17px/1.55 Georgia,'Times New Roman',serif;color:var(--ink);background:var(--bg)}
main{max-width:720px;margin:0 auto;padding:20px 18px 80px}
h1{font-size:1.7rem;line-height:1.2;margin:.4em 0 .2em}h2{font-size:1.15rem;margin:1.6em 0 .4em}
.meta,.small{font:13px/1.4 system-ui,sans-serif;color:var(--mute)}
.banner{font:14px/1.4 system-ui,sans-serif;background:#fff3cd;border:1px solid #e0c97a;padding:10px 12px;border-radius:6px;margin:12px 0}
.banner.ok{background:#e3f3ea;border-color:#9ccdb3}
nav{display:flex;gap:8px;margin:16px 0;border-bottom:1px solid var(--line)}
nav button{font:15px system-ui,sans-serif;background:none;border:0;border-bottom:3px solid transparent;padding:8px 4px;margin-right:12px;cursor:pointer;color:var(--mute)}
nav button[aria-selected=true]{color:var(--ink);border-color:var(--accent);font-weight:600}
sup{font:11px system-ui,sans-serif;color:var(--accent)}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:18px;margin:14px 0}
.opt{display:block;width:100%;text-align:left;font:16px/1.4 system-ui,sans-serif;background:#fff;border:1px solid var(--line);border-radius:8px;padding:12px;margin:8px 0;cursor:pointer;color:var(--ink)}
.opt:hover:not(:disabled){border-color:var(--ink)}.opt.right{border-color:var(--ok);background:#e3f3ea}.opt.wrong{border-color:var(--bad);background:#f7e4e0}
.next{font:15px system-ui,sans-serif;background:var(--ink);color:#fff;border:0;border-radius:8px;padding:10px 18px;cursor:pointer;margin-top:8px}
ol.refs{font:14px/1.45 system-ui,sans-serif;color:var(--mute);padding-left:22px}
ul{padding-left:22px}[hidden]{display:none}table{border-collapse:collapse;width:100%;font:14px/1.4 system-ui,sans-serif;margin:10px 0}th,td{border:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}th{background:#eee}
</style></head><body><main>
<div class="meta">Fetal Echo Project &middot; Unit __ID__ &middot; __TIER__ tier &middot; v__VERSION__</div>
<h1>__TITLE__</h1>
<div class="banner __BANNERCLASS__">__BANNER__</div>
<nav role="tablist"><button id="t-read" aria-selected="true">Read</button><button id="t-drill" aria-selected="false">Drill</button></nav>
<section id="read">__READ__</section>
<section id="drill" hidden><div id="quiz"></div></section>
</main>
<script>
const DATA = __DATA__;
const $ = s => document.querySelector(s);
function tab(which){
  $('#read').hidden = which !== 'read'; $('#drill').hidden = which !== 'drill';
  $('#t-read').setAttribute('aria-selected', which === 'read');
  $('#t-drill').setAttribute('aria-selected', which === 'drill');
}
$('#t-read').onclick = () => tab('read');
$('#t-drill').onclick = () => { tab('drill'); if (!started) start(); };
function shuffle(a){ a = a.slice(); for (let i = a.length - 1; i > 0; i--){ const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
function esc(s){ const d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
let started = false, queue = [], pos = 0, score = 0;
function start(){ started = true; queue = shuffle(DATA.items); pos = 0; score = 0; show(); }
function show(){
  const q = $('#quiz');
  if (pos >= queue.length){
    q.innerHTML = '<div class="card"><h2 style="margin-top:0">' + score + ' of ' + queue.length + ' correct</h2><p class="small">Missed items come back first next time once scheduling is added.</p><button class="next" id="again">Go again</button></div>';
    $('#again').onclick = start; return;
  }
  const it = queue[pos];
  const opts = shuffle(it.options.map((text, i) => ({ text, correct: i === it.answer })));
  q.innerHTML = '<div class="card"><div class="small">Question ' + (pos + 1) + ' of ' + queue.length + '</div><p><strong>' + esc(it.question) + '</strong></p><div id="opts"></div><div id="fb"></div></div>';
  opts.forEach(o => {
    const b = document.createElement('button'); b.className = 'opt'; b.textContent = o.text;
    b.onclick = () => {
      document.querySelectorAll('.opt').forEach((x, k) => { x.disabled = true; if (opts[k].correct) x.classList.add('right'); });
      if (o.correct) score++; else b.classList.add('wrong');
      $('#fb').innerHTML = '<p>' + esc(it.explanation) + '</p><div class="small">Rests on ' + it.claims.join(', ') + ' (' + it.status + ')</div><button class="next" id="nx">Next</button>';
      $('#nx').onclick = () => { pos++; show(); };
    };
    $('#opts').appendChild(b);
  });
}
</script></body></html>
"""


def build_page(u, claims, sources, status, drills):
    order, parts = [], []
    e = html.escape

    def marks(refs):
        nums = []
        for r in refs or []:
            if r not in order:
                order.append(r)
            nums.append(str(order.index(r) + 1))
        return f"<sup>{','.join(nums)}</sup>" if nums else ""

    parts.append("<h2>You will be able to</h2><ul>" +
                 "".join(f"<li>{e(o)}</li>" for o in u.get("objectives", [])) + "</ul>")
    for s in u.get("sections", []):
        parts.append(f"<h2>{e(s['heading'])}</h2>")
        for b in s.get("blocks", []):
            parts.append(f"<p>{e(b['text'])}{marks(b.get('claims'))}</p>")
            t = b.get("table")
            if t:
                parts.append("<table><tr>" + "".join(f"<th>{e(c)}</th>" for c in t["columns"]) + "</tr>" +
                             "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in t["rows"]) +
                             "</table>")
    ck = u.get("checklist")
    if ck:
        parts.append(f"<h2>{e(ck['title'])}</h2><ul>" +
                     "".join(f"<li>{e(i['text'])}{marks(i.get('claims'))}</li>" for i in ck["items"]) + "</ul>")
    if u.get("missing_claims"):
        parts.append("<h2>Still to be written</h2><ul class='small'>" +
                     "".join(f"<li>{e(m)}</li>" for m in u["missing_claims"]) + "</ul>")
    parts.append("<h2>References</h2><ol class='refs'>")
    for cid in order:
        c = claims[cid]
        parts.append(f"<li>{e(cite(sources[c['source']]))} &ndash; {e(c['locator'])}. "
                     f"<em>{e(cid)}, {e(c['status'])}</em></li>")
    parts.append("</ol>")

    page = PAGE
    for key, val in {
        "__TITLE__": e(u["title"]), "__ID__": e(u["id"]), "__TIER__": e(u["tier"]),
        "__VERSION__": e(str(u["version"])), "__BANNER__": e(banner(status)),
        "__BANNERCLASS__": "ok" if status == "expert-verified" else "",
        "__READ__": "\n".join(parts),
        "__DATA__": json.dumps(drills, ensure_ascii=False).replace("</", "<\\/"),
    }.items():
        page = page.replace(key, val)
    return page


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="validate only")
    ap.add_argument("--release", action="store_true",
                    help="fail unless all claims are expert-verified and units signed")
    args = ap.parse_args()

    errors, warnings, sources, claims, units = validate(release=args.release)
    for w in warnings:
        print(f"warning: {w}")
    for err in errors:
        print(f"ERROR:   {err}")
    counts = {s: sum(1 for c in claims.values() if c.get("status") == s) for s in STATUSES}
    print(f"\n{len(claims)} claims: " + ", ".join(f"{n} {s}" for s, n in counts.items()))
    if errors:
        print(f"{len(errors)} error(s). Nothing built.")
        return 1
    if args.check:
        print("Ledger is valid.")
        return 0

    for u in units:
        status = unit_status(u, claims)
        out = ROOT / "dist" / u["id"]
        out.mkdir(parents=True, exist_ok=True)
        drills = build_drills(u, claims, status)
        (out / "chapter.md").write_text(build_chapter(u, claims, sources, status), encoding="utf-8")
        (out / "drills.json").write_text(json.dumps(drills, indent=2, ensure_ascii=False) + "\n",
                                         encoding="utf-8")
        script = build_video(u, status)
        if script:
            (out / "video-script.md").write_text(script, encoding="utf-8")
        (out / "review.md").write_text(build_review(u, claims, sources), encoding="utf-8")
        (out / "study.html").write_text(build_page(u, claims, sources, status, drills),
                                        encoding="utf-8")
        print(f"built {u['id']} ({status}) -> dist/{u['id']}/")
    import outputs
    outputs.build_all(units, claims, sources, unit_status, banner, cite, STATUSES)
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Cross-unit outputs: the course app, the combined book, and website pages.

Called from build.py after the per-unit outputs. Everything here is generated
from the same units and ledger, so the app, book and website cannot disagree.
"""
import html
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
TEMPLATES = Path(__file__).resolve().parent / "templates"
e = html.escape


def model(u, claims, sources, unit_status, banner, cite):
    """One neutral description of a unit, used by the app, book and web page."""
    status = unit_status(u, claims)
    order = []

    def refs(rs):
        out = []
        for r in rs or []:
            if r not in order:
                order.append(r)
            out.append(order.index(r) + 1)
        return out

    sections = []
    for s in u.get("sections", []):
        sections.append({"heading": s["heading"], "blocks": [
            {"text": b["text"], "refs": refs(b.get("claims")), "table": b.get("table")}
            for b in s.get("blocks", [])]})
    checklist = None
    if u.get("checklist"):
        checklist = {"title": u["checklist"]["title"], "items": [
            {"text": i["text"], "refs": refs(i.get("claims"))} for i in u["checklist"]["items"]]}
    drills = []
    for d in u.get("drills", []):
        drills.append({"id": d["id"], "question": d["question"], "options": d["options"],
                       "answer": d["answer"], "explanation": d["explanation"], "claims": d["claims"],
                       "status": min((claims[c]["status"] for c in d["claims"]),
                                     key=["ai-extracted", "ai-cross-checked", "expert-verified"].index)})
    video = None
    if u.get("video"):
        v = u["video"]
        video = {"title": v["title"], "minutes": v["target_minutes"], "beats": [
            {"shot": b["shot"], "narration": b["narration"]} for b in v["beats"]]}
    return {
        "id": u["id"], "title": u["title"], "tier": u["tier"], "version": u["version"],
        "summary": u.get("summary", ""), "public": bool(u.get("public")),
        "status": status, "banner": banner(status),
        "objectives": u.get("objectives", []), "sections": sections, "checklist": checklist,
        "drills": {"items": drills}, "video": video, "missing": u.get("missing_claims", []),
        "references": [f"{cite(sources[claims[c]['source']])} – {claims[c]['locator']}. ({c}, {claims[c]['status']})"
                       for c in order],
    }


def build_app(models):
    out = DIST / "app"
    out.mkdir(parents=True, exist_ok=True)
    data = json.dumps({"units": models}, ensure_ascii=False).replace("</", "<\\/")
    page = (TEMPLATES / "app.html").read_text(encoding="utf-8").replace("__DATA__", data)
    (out / "index.html").write_text(page, encoding="utf-8")
    (out / "manifest.webmanifest").write_text(json.dumps({
        "name": "Fetal Echo Course", "short_name": "Fetal Echo", "start_url": "./index.html",
        "display": "standalone", "background_color": "#f6f4ef", "theme_color": "#9b2c3f",
        "icons": [{"src": "icon.svg", "sizes": "any", "type": "image/svg+xml", "purpose": "any"}],
    }, indent=2) + "\n", encoding="utf-8")
    (out / "icon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" rx="20" fill="#9b2c3f"/>'
        '<path d="M50 78 22 50a16 16 0 0 1 28-12 16 16 0 0 1 28 12z" fill="#fff"/></svg>\n', encoding="utf-8")
    # Cache name changes with content so installed copies update.
    import hashlib
    ver = hashlib.sha1(page.encode()).hexdigest()[:10]
    (out / "sw.js").write_text(
        f"const C='fetal-echo-{ver}';\n"
        "self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(['./','./index.html','./manifest.webmanifest','./icon.svg'])));self.skipWaiting();});\n"
        "self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))));self.clients.claim();});\n"
        "self.addEventListener('fetch',e=>{e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request)));});\n",
        encoding="utf-8")


def md_unit(m):
    lines = [f"# {m['title']}", "", f"> {m['banner']}", "",
             f"Unit {m['id']} | Tier: {m['tier']} | Version {m['version']}", "", "## You will be able to", ""]
    lines += [f"- {o}" for o in m["objectives"]]
    for s in m["sections"]:
        lines += ["", f"## {s['heading']}", ""]
        for b in s["blocks"]:
            lines += [b["text"] + (f" [{', '.join(map(str, b['refs']))}]" if b["refs"] else ""), ""]
            if b["table"]:
                t = b["table"]
                lines += ["| " + " | ".join(t["columns"]) + " |", "|" + "---|" * len(t["columns"])]
                lines += ["| " + " | ".join(r) + " |" for r in t["rows"]] + [""]
    if m["checklist"]:
        lines += [f"## {m['checklist']['title']}", ""]
        lines += [f"- [ ] {i['text']}" + (f" [{', '.join(map(str, i['refs']))}]" if i["refs"] else "")
                  for i in m["checklist"]["items"]] + [""]
    if m["missing"]:
        lines += ["## Still to be written", ""] + [f"- {x}" for x in m["missing"]] + [""]
    lines += ["## References", ""] + [f"{i}. {r}" for i, r in enumerate(m["references"], 1)]
    return "\n".join(lines) + "\n"


def build_book(models):
    out = DIST / "book"
    out.mkdir(parents=True, exist_ok=True)
    worst = "expert-verified" if all(m["status"] == "expert-verified" for m in models) else "draft"
    head = ["---", "title: Fetal Echocardiography", "subtitle: Detect and foundation units",
            "author: Edited by Dr Kunda Shahane, Mayflower Clinic, Nagpur", "---", "",
            ("> DRAFT - NOT FOR CLINICAL USE. Units marked draft contain claims no clinician has verified."
             if worst == "draft" else "> All units verified."), "", "# Contents", ""]
    head += [f"- {m['id']} {m['title']} ({'verified' if m['status'] == 'expert-verified' else 'draft'})" for m in models]
    body = "\n\n\\newpage\n\n".join(md_unit(m).replace("\n# ", "\n# ", 1) for m in models)
    (out / "book.md").write_text("\n".join(head) + "\n\n" + body, encoding="utf-8")
    if shutil.which("pandoc"):
        css = out / "book.css"
        css.write_text("body{font:16px/1.55 Georgia,serif;max-width:46em;margin:2em auto;padding:0 1em;color:#1c2430}"
                       "blockquote{background:#fff3cd;border:1px solid #e0c97a;margin:1em 0;padding:.5em 1em}"
                       "table{border-collapse:collapse}th,td{border:1px solid #ccc;padding:4px 8px;text-align:left;vertical-align:top}"
                       "h1{page-break-before:always}h1:first-of-type{page-break-before:avoid}", encoding="utf-8")
        r = subprocess.run(["pandoc", str(out / "book.md"), "-s", "--toc", "--toc-depth=1", "-c", "book.css",
                            "-o", str(out / "book.html")], capture_output=True, text=True)
        if r.returncode:
            print("warning: pandoc failed:", r.stderr.strip()[:200])
        else:
            chrome = shutil.which("google-chrome") or shutil.which("chromium")
            if chrome:
                subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                                f"--print-to-pdf={out / 'book.pdf'}", (out / "book.html").as_uri()],
                               capture_output=True, timeout=120)
    else:
        print("warning: pandoc not found; only book.md written")


def web_page(m, fragment=False):
    """Public-facing article for a unit. Carries its verification status; draft pages are noindex."""
    parts = []
    parts.append(f'<div class="fe-banner">{e(m["banner"])}</div>')
    parts.append("<h2>What you will learn</h2><ul>" + "".join(f"<li>{e(o)}</li>" for o in m["objectives"]) + "</ul>")
    for s in m["sections"]:
        parts.append(f"<h2>{e(s['heading'])}</h2>")
        for b in s["blocks"]:
            sup = f"<sup>{','.join(map(str, b['refs']))}</sup>" if b["refs"] else ""
            parts.append(f"<p>{e(b['text'])}{sup}</p>")
            if b["table"]:
                t = b["table"]
                parts.append('<div class="fe-scroll"><table><thead><tr>' + "".join(f"<th>{e(c)}</th>" for c in t["columns"]) +
                             "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>"
                                                              for r in t["rows"]) + "</tbody></table></div>")
    if m["checklist"]:
        parts.append(f"<h2>{e(m['checklist']['title'])}</h2><ul>" +
                     "".join(f"<li>{e(i['text'])}</li>" for i in m["checklist"]["items"]) + "</ul>")
    parts.append("<h2>References</h2><ol class='fe-refs'>" + "".join(f"<li>{e(r)}</li>" for r in m["references"]) + "</ol>")
    parts.append('<p class="fe-note">Educational material for clinicians. It does not replace the guidelines cited, '
                 'and is not a substitute for clinical judgement. Edited by Dr Kunda Shahane, '
                 'Fetal Medicine Consultant, Mayflower Clinic, Nagpur.</p>')
    css = ("<style>.fe-banner{background:#fff3cd;border:1px solid #e0c97a;padding:10px 12px;border-radius:6px;margin:12px 0;font:14px/1.4 system-ui,sans-serif}"
           ".fe-scroll{overflow-x:auto}.fe-scroll table{border-collapse:collapse;width:100%}"
           ".fe-scroll th,.fe-scroll td{border:1px solid #d9dee5;padding:6px 8px;text-align:left;vertical-align:top}.fe-scroll th{background:#f0f0f0}"
           ".fe-refs,.fe-note{font-size:.85em;color:#5d6b7a}</style>")
    body = css + "\n".join(parts)
    if fragment:
        return body
    robots = "" if m["status"] == "expert-verified" else '<meta name="robots" content="noindex">'
    return (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">{robots}'
            f'<title>{e(m["title"])}</title>'
            '<style>body{font:17px/1.6 Georgia,serif;max-width:46em;margin:0 auto;padding:16px;color:#1c2430;background:#fff}</style>'
            f'</head><body><h1>{e(m["title"])}</h1><p>{e(m["summary"])}</p>{body}</body></html>')


def build_web(models):
    out = DIST / "web"
    out.mkdir(parents=True, exist_ok=True)
    pages = [m for m in models if m["public"]]
    for m in pages:
        slug = m["title"].lower().replace(" ", "-")
        (out / f"{m['id']}-{slug}.html").write_text(web_page(m), encoding="utf-8")
        (out / f"{m['id']}-{slug}.wp-fragment.html").write_text(web_page(m, fragment=True), encoding="utf-8")
    if pages:
        (out / "README.md").write_text(
            "# Website pages\n\nOne standalone page and one body-only fragment (for pasting into a WordPress "
            "'Custom HTML' block) per unit marked `public: true`.\n\n"
            "Draft pages are marked noindex and show a draft banner. Do not publish a page until its unit is "
            "fully expert-verified (docs/05-governance.md).\n", encoding="utf-8")


def build_all(units, claims, sources, unit_status, banner, cite, statuses):
    models = [model(u, claims, sources, unit_status, banner, cite) for u in units]
    build_app(models)
    build_book(models)
    build_web(models)
    print(f"built app, book and {sum(1 for m in models if m['public'])} web page(s) -> dist/app, dist/book, dist/web")

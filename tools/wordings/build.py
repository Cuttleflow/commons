#!/usr/bin/env python3
"""Single-source build for Commons policy wordings.

Each clause is a Markdown file with a YAML header in source/<class>/clauses/.
A wording is described by a manifest: source/<class>/base.yaml for the base wording,
source/<class>/professions/<slug>.yaml for a profession wording, which pins a base
version and lists overrides (replace, add, delete).

Usage:
  python3 tools/wordings/build.py check            # run the checks only
  python3 tools/wordings/build.py build            # checks, then write HTML, .docx and build records
  python3 tools/wordings/build.py build --no-docx  # as above without .docx (used by CI)

Cross-references are written [[ref:<clause id>]] and printed as "the <heading> <kind>",
for example "the Financial Services exclusion". [[ref:<id>|heading]] prints the heading only.
Clause numbers are never written in clause text; the checks reject them.
"""
import hashlib, html, json, pathlib, re, sys
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
SOURCE = ROOT / "source"
TEMPLATE = pathlib.Path(__file__).with_name("page_template.html")

KIND = {  # how a reference to each clause type reads
    "definition": "definition", "cover": "clause", "extension": "extension",
    "exclusion": "exclusion", "payment": "provision", "obligation": "obligation",
    "condition": "condition", "section": "section", "preamble": "section",
    "claims": "section", "library": "", "notice": "", "endorsement": "endorsement",
}
REF = re.compile(r"\[\[ref:([a-z0-9.\-]+)(\|heading)?\]\]")
LITERAL_NUMBER = re.compile(r"\b(?:Sections?|[Cc]lauses?|[Pp]aragraph|[Ss]ub-?clause)\s+\d+(?:\.\d+)*\b")


class BuildError(Exception):
    pass


LINK = {"ids": None, "page": ""}
QUESTIONS = {}  # platform question id -> question record, for the class being built
ACTIONS = {
    "apply": "Apply automatically",
    "refer": "Refer to the underwriter, with the endorsement pre-selected",
    "suggest": "Suggest to the underwriter (quote not held)",
    "broker_option": "Offer as a priced option",
}
RESPONSES = (  # what an underwriter may do with a referred or suggested endorsement (SPEC-URE-001 Addendum B)
    "Attach", "Attach with amended sub-limit", "Attach with special excess",
    "Attach with premium loading", "Do not attach", "Decline risk",
)
QREF = re.compile(r"\bqs\.[a-z0-9_.]+[a-z0-9_]")  # set while rendering a document: ids present in it, page for other clauses


# ---------------------------------------------------------------- loading

def load_clause(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        raise BuildError(f"{path}: missing YAML header")
    meta = yaml.safe_load(m.group(1))
    meta["body"] = m.group(2).strip()
    meta["path"] = str(path.relative_to(ROOT))
    return meta


def load_class(cls):
    clauses = {}
    for p in sorted((SOURCE / cls / "clauses").glob("*.md")):
        c = load_clause(p)
        if c["id"] in clauses:
            raise BuildError(f"duplicate clause id {c['id']}")
        if p.stem != c["id"]:
            raise BuildError(f"{p}: file name must equal id {c['id']}")
        clauses[c["id"]] = c
    return clauses


def load_questions(cls):
    p = SOURCE / cls / "questions.yaml"
    if not p.exists():
        return {}
    return {q["id"]: q for q in yaml.safe_load(p.read_text(encoding="utf-8"))["questions"]}


def check_trigger(c, errors):
    """An endorsement must say when it is used: platform questions, rules, default actions and reason text."""
    t = c.get("trigger")
    if c["type"] != "endorsement":
        if t:
            errors.append(f"{c['path']}: only endorsements carry a trigger")
        return
    if not t:
        errors.append(f"{c['path']}: endorsement has no trigger (questions, rules, reason)")
        return
    qs = t.get("questions") or []
    if not qs:
        errors.append(f"{c['path']}: trigger lists no questions")
    for q in qs:
        if q not in QUESTIONS:
            errors.append(f"{c['path']}: trigger question {q} is not in questions.yaml")
    if not t.get("rules"):
        errors.append(f"{c['path']}: trigger has no rules")
    for r in (t.get("rules") or []) + (t.get("restrictions") or []):
        if r.get("action") not in ACTIONS:
            errors.append(f"{c['path']}: trigger action '{r.get('action')}' is not one of {', '.join(ACTIONS)}")
        for q in QREF.findall(str(r.get("when", ""))):
            if q not in qs:
                errors.append(f"{c['path']}: rule uses {q}, which is not in the trigger's questions")
    for r in t.get("restrictions") or []:
        if r.get("action") != "refer":
            errors.append(f"{c['path']}: a restriction must refer to the underwriter")
        if not r.get("note"):
            errors.append(f"{c['path']}: a restriction needs a note explaining it")
    if not t.get("reason"):
        errors.append(f"{c['path']}: trigger has no reason text")
    for r in t.get("responses") or []:
        if r not in RESPONSES:
            errors.append(f"{c['path']}: underwriter response '{r}' is not one of {', '.join(RESPONSES)}")


def load_manifest(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- resolving

def resolve(cls, manifest, clauses, errors):
    """Return (structure, clause map) for a wording after applying overrides."""
    if "base" in manifest:  # profession wording
        base = load_manifest(SOURCE / cls / "base.yaml")
        pinned = str(manifest["base"]).split("@")[-1]
        if pinned != str(base["version"]):
            errors.append(f"{manifest['id']}: pins base {pinned} but the base is {base['version']} (stale pin)")
        structure = [dict(section=s["section"], clauses=list(s["clauses"])) for s in base["structure"]]
    else:
        structure = [dict(section=s["section"], clauses=list(s["clauses"])) for s in manifest["structure"]]
    cmap = dict(clauses)
    present = {c for s in structure for c in s["clauses"]} | {s["section"] for s in structure}
    for op in manifest.get("overrides", []) or []:
        kind, target = op.get("op"), op.get("target")
        if kind in ("replace", "delete") and target not in present:
            errors.append(f"{manifest['id']}: override {kind} targets {target}, which is not in the base wording")
            continue
        if kind == "replace":
            new = cmap.get(op["with"])
            if new is None:
                errors.append(f"{manifest['id']}: replacement clause {op['with']} does not exist")
                continue
            for s in structure:
                s["clauses"] = [op["with"] if c == target else c for c in s["clauses"]]
        elif kind == "delete":
            for s in structure:
                s["clauses"] = [c for c in s["clauses"] if c != target]
        elif kind == "add":
            after = op.get("after")
            if op["clause"] not in cmap:
                errors.append(f"{manifest['id']}: added clause {op['clause']} does not exist")
                continue
            placed = False
            for s in structure:
                if after in s["clauses"]:
                    s["clauses"].insert(s["clauses"].index(after) + 1, op["clause"]); placed = True
                elif after == s["section"]:
                    s["clauses"].insert(0, op["clause"]); placed = True
            if not placed:
                errors.append(f"{manifest['id']}: add {op['clause']} after {after}, which is not in the wording")
        else:
            errors.append(f"{manifest['id']}: unknown override {kind}")
    return structure, cmap


def ref_text(c, heading_only=False):
    if heading_only:
        return c["heading"]
    if c["type"] == "definition":
        return f"the definition of {c['heading']}"
    kind = KIND.get(c["type"], "")
    return f"the {c['heading']} {kind}".strip()


# ---------------------------------------------------------------- checks

def check(manifest, structure, cmap, errors):
    in_doc = [c for s in structure for c in s["clauses"]] + [s["section"] for s in structure if s["section"] in cmap]
    ids = set(in_doc)
    seen = {}
    for cid in in_doc:
        c = cmap.get(cid)
        if c is None:
            errors.append(f"{manifest['id']}: clause {cid} is listed but no clause file exists")
            continue
        key = (c["type"], c["heading"].lower())
        if key in seen:
            errors.append(f"{manifest['id']}: duplicate {c['type']} heading '{c['heading']}' ({seen[key]}, {cid})")
        seen[key] = cid
        for m in REF.finditer(c["body"]):
            if m.group(1) not in ids:
                errors.append(f"{c['path']}: reference to {m.group(1)}, which is not in {manifest['id']}")
        for m in LITERAL_NUMBER.finditer(c["body"]):
            errors.append(f"{c['path']}: literal clause number '{m.group(0)}' — use [[ref:...]]")
        check_trigger(c, errors)
        if c.get("status") == "draft" and not manifest.get("draft"):
            errors.append(f"{c['path']}: draft clause in a wording that is not marked draft")
    return ids


# ---------------------------------------------------------------- rendering helpers

def inline_html(text, cmap):
    def ref(m):
        c = cmap[m.group(1)]
        href = f'#{c["id"]}' if LINK["ids"] is None or c["id"] in LINK["ids"] else f'{LINK["page"]}#{c["id"]}'
        return f'<a href="{href}">{html.escape(ref_text(c, bool(m.group(2))))}</a>'
    parts, last = [], 0
    for m in REF.finditer(text):
        parts.append(html.escape(text[last:m.start()], quote=False)); parts.append(ref(m)); last = m.end()
    parts.append(html.escape(text[last:], quote=False))
    out = "".join(parts)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"<em>\1</em>", out)
    return out


def plain(text, cmap):
    t = REF.sub(lambda m: ref_text(cmap[m.group(1)], bool(m.group(2))), text)
    return t


def blocks(body):
    """Split a clause body into blocks: ('p', text) ('ul', [items]) ('ol', [items]) ('table', rows)."""
    out = []
    for chunk in re.split(r"\n\s*\n", body.strip()):
        lines = [l.rstrip() for l in chunk.splitlines() if l.strip()]
        if not lines:
            continue
        if all(l.startswith("- ") for l in lines):
            out.append(("ul", [l[2:] for l in lines]))
        elif all(re.match(r"\d+\. ", l) for l in lines):
            out.append(("ol", [re.sub(r"^\d+\. ", "", l) for l in lines]))
        elif lines[0].startswith("|"):
            rows = [[c.strip() for c in l.strip("|").split("|")] for l in lines]
            rows = [r for r in rows if not all(set(c) <= set("-: ") for c in r)]
            out.append(("table", rows))
        else:
            out.append(("p", " ".join(lines)))
    return out


def note_html(c):
    """Wording note for an endorsement: when the platform uses it. Shown on web pages only, not in the policy document."""
    t = c.get("trigger")
    if not t:
        return ""
    qs = "".join(f"<li>{html.escape(QUESTIONS[q]['text'])} <code>{html.escape(q)}</code></li>" for q in t["questions"])
    rules = "".join(f"<li>When <code>{html.escape(str(r['when']))}</code>: {html.escape(ACTIONS[r['action']])}</li>"
                    for r in t["rules"])
    restr = "".join(f"<li>When <code>{html.escape(str(r['when']))}</code>: {html.escape(ACTIONS[r['action']])}. "
                    f"{html.escape(r['note'])}</li>" for r in t.get("restrictions") or [])
    return ('<div class="wnote"><div class="mono nlabel">Wording note — platform rule (not part of the policy)</div>'
            f'<p><strong>Questions</strong></p><ul>{qs}</ul>'
            f'<p><strong>Default rules</strong> (the first rule that matches applies; agencies may set their own actions and thresholds)</p><ul>{rules}</ul>'
            + (f'<p><strong>Restrictions</strong> (always apply)</p><ul>{restr}</ul>' if restr else "")
            + (f'<p><strong>Underwriter responses</strong> (on a referral or suggestion): {html.escape("; ".join(t["responses"]))}</p>'
               if t.get("responses") else "")
            + f'<p><strong>Reason shown on the quote and schedule:</strong> {html.escape(t["reason"])}</p></div>')


def body_html(c, cmap):
    h = []
    for kind, val in blocks(c["body"]):
        if kind == "p":
            h.append(f"<p>{inline_html(val, cmap)}</p>")
        elif kind in ("ul", "ol"):
            h.append(f"<{kind}>" + "".join(f"<li>{inline_html(i, cmap)}</li>" for i in val) + f"</{kind}>")
        else:
            head, *rows = val
            h.append("<table><thead><tr>" + "".join(f"<th>{inline_html(x, cmap)}</th>" for x in head) + "</tr></thead><tbody>"
                     + "".join("<tr>" + "".join(f"<td>{inline_html(x, cmap)}</td>" for x in r) + "</tr>" for r in rows)
                     + "</tbody></table>")
    return "\n".join(h)


# ---------------------------------------------------------------- HTML

def professions_html(manifest):
    """On a base wording page: the profession wordings built on it."""
    profs = manifest.get("professions") or []
    if not profs:
        return ""
    rows = "".join(
        f'<li><a href="{html.escape(p["slug"])}.html">{html.escape(p["title"])}</a>'
        f' <span class="pmeta">v{html.escape(str(p["version"]))} · {html.escape(p["doc_ref"])}'
        f' · <a href="{html.escape(p["slug"])}-endorsement.html">endorsement form</a></span></li>'
        for p in profs)
    return ('<div class="professions"><div class="mono plabel">Profession wordings built on this wording</div>'
            f'<ul>{rows}</ul></div>')


def extra_links(manifest):
    links = manifest.get("links", [])
    return "".join(f'<a class="btn" href="{html.escape(u)}">{html.escape(t)}</a>' for t, u in links)


def render_html(manifest, structure, cmap, slug, docx_name):
    v = manifest["version"]
    out = []
    for s in structure:
        sec = cmap.get(s["section"])
        if sec:
            out.append(f'<h2 id="{sec["id"]}">{html.escape(sec["heading"])}</h2>')
            if sec["body"]:
                out.append(body_html(sec, cmap))
        if s["section"] == "pi.section.definitions" or (sec and sec["type"] == "section" and s["clauses"]
                                                       and all(cmap[c]["type"] == "definition" for c in s["clauses"])):
            out.append("<table class=\"defs\"><tbody>")
            for cid in s["clauses"]:
                c = cmap[cid]
                out.append(f'<tr id="{cid}"><td><strong>{html.escape(c["heading"])}</strong></td><td>{body_html(c, cmap)}</td></tr>')
            out.append("</tbody></table>")
            continue
        for cid in s["clauses"]:
            c = cmap[cid]
            tag = "h2" if c["type"] in ("preamble", "claims", "library", "notice") else "h3"
            out.append(f'<{tag} id="{cid}">{html.escape(c["heading"])}</{tag}>')
            out.append(body_html(c, cmap))
            if c.get("trigger"):
                out.append(note_html(c))
    draft = f'<span class="draft-flag">Draft v{html.escape(v)}</span>' if manifest.get("draft") else f'<span>v{html.escape(v)}</span>'
    banner = ('<div class="banner"><strong>DRAFT — subject to legal review — not for use.</strong> This wording is not settled and '
              'must not be issued, quoted from, or bound until Wording Partner sign-off. It is provided as source material under '
              'CC BY 4.0, without warranty.</div>') if manifest.get("draft") else ""
    kicker = manifest.get("kicker", "Cuttleflow Commons · " + manifest["title"].replace(" Insurance", ""))
    main = (f'<main class="wrap"><div class="wtitle"><div class="kick">{html.escape(kicker)}</div>'
            f'<h1 class="serif">{html.escape(manifest["title"])}</h1><div class="sub">{html.escape(manifest["summary"])}</div>'
            f'<div class="actions">{draft}<a class="btn" href="downloads/{docx_name}">Download .docx</a>{extra_links(manifest)}'
            f'<a class="btn" href="https://github.com/cuttleflow/commons/issues/new?template=propose-change.md&amp;title=%5B{manifest["doc_ref"]}%5D+">Suggest a change</a></div>'
            f'{banner}{professions_html(manifest)}</div><article class="article">\n' + "\n".join(out) + "\n</article>")
    desc = (f"{manifest['title']} — an open Australian policy wording from the Cuttleflow Commons. "
            "Working draft, subject to legal review; read it, adapt it under CC BY 4.0, and suggest changes.")
    page = TEMPLATE.read_text(encoding="utf-8")
    return (page.replace("{{title}}", html.escape(manifest["title"])).replace("{{slug}}", slug)
                .replace("{{description}}", html.escape(desc)).replace("{{main}}", main))


# ---------------------------------------------------------------- .docx

def render_docx(manifest, structure, cmap, path, changes_md):
    from docx import Document
    from docx.enum.text import WD_BREAK
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Pt, RGBColor, Cm

    INK, GREEN, ORANGE = RGBColor(0x1C, 0x19, 0x15), RGBColor(0x2E, 0x5C, 0x4E), RGBColor(0xC2, 0x4E, 0x2C)
    doc = Document()
    st = doc.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(10.5); st.font.color.rgb = INK
    for s in doc.sections:
        s.left_margin = s.right_margin = Cm(2.2); s.top_margin = s.bottom_margin = Cm(2.0)
        s.different_first_page_header_footer = True
    v, ref = manifest["version"], manifest["doc_ref"]

    def run(p, text, bold=False, italic=False, font=None, size=None, color=None):
        r = p.add_run(text); r.bold = bold; r.italic = italic
        if font: r.font.name = font; r._element.rPr.rFonts.set(qn("w:eastAsia"), font)
        if size: r.font.size = Pt(size)
        if color is not None: r.font.color.rgb = color
        return r

    def bookmark(p, name, idx):
        start = OxmlElement("w:bookmarkStart"); start.set(qn("w:id"), str(idx)); start.set(qn("w:name"), name)
        end = OxmlElement("w:bookmarkEnd"); end.set(qn("w:id"), str(idx))
        p._p.insert(0, start); p._p.append(end)

    def link(p, anchor, text):
        h = OxmlElement("w:hyperlink"); h.set(qn("w:anchor"), anchor)
        r = OxmlElement("w:r"); rpr = OxmlElement("w:rPr"); u = OxmlElement("w:u"); u.set(qn("w:val"), "single")
        col = OxmlElement("w:color"); col.set(qn("w:val"), "2E5C4E"); rpr.append(col); rpr.append(u); r.append(rpr)
        t = OxmlElement("w:t"); t.text = text; t.set(qn("xml:space"), "preserve"); r.append(t); h.append(r)
        p._p.append(h)

    def inline(p, text):
        pos = 0
        for m in REF.finditer(text):
            styled(p, text[pos:m.start()])
            c = cmap[m.group(1)]
            link(p, bm(c["id"]), ref_text(c, bool(m.group(2))))
            pos = m.end()
        styled(p, text[pos:])

    def styled(p, text):
        for part in re.split(r"(\*\*.+?\*\*)", text):
            if part.startswith("**") and part.endswith("**"):
                run(p, part[2:-2], bold=True)
            elif part:
                run(p, part)

    def bm(cid):  # Word bookmark names: letters, digits, underscore; max 40 chars
        return ("c_" + re.sub(r"[^A-Za-z0-9]", "_", cid))[:40]

    def body(c):
        for kind, val in blocks(c["body"]):
            if kind == "p":
                inline(doc.add_paragraph(), val)
            elif kind in ("ul", "ol"):
                for i in val:
                    inline(doc.add_paragraph(style="List Bullet" if kind == "ul" else "List Number"), i)
            else:
                t = doc.add_table(rows=0, cols=len(val[0])); t.style = "Table Grid"
                for r_ in val:
                    cells = t.add_row().cells
                    for cell, x in zip(cells, r_):
                        cell.paragraphs[0].text = ""; inline(cell.paragraphs[0], x)

    # cover page
    for _ in range(3): doc.add_paragraph()
    p = doc.add_paragraph(); run(p, "cuttleflow ", font="Consolas", size=12); run(p, "SYSTEMS", font="Consolas", size=12, bold=True)
    p = doc.add_paragraph(); run(p, manifest["class"], font="Consolas", size=9, color=ORANGE)
    p = doc.add_paragraph(); run(p, "Policy Wording" if "base" not in manifest else manifest["title"], font="Georgia", size=30, bold=True)
    if manifest.get("form") == "endorsement":
        p = doc.add_paragraph(); run(p, "Policy endorsement", font="Georgia", size=14, italic=True, color=GREEN)
    elif "base" in manifest:
        p = doc.add_paragraph(); run(p, "Integrated profession wording", font="Georgia", size=14, italic=True, color=GREEN)
    p = doc.add_paragraph(); run(p, "Cuttleflow Systems — Open Source Insurance Wording", font="Georgia", size=13, italic=True, color=GREEN)
    p = doc.add_paragraph(); run(p, f"Version {v} · {manifest['date']} · CC BY 4.0 (wording text only)", font="Consolas", size=9, color=GREEN)
    if "base" in manifest:
        p = doc.add_paragraph(); run(p, f"{'Attaches to' if manifest.get('form') == 'endorsement' else 'Built on'} base wording {manifest['base']}", font="Consolas", size=9, color=GREEN)
    p = doc.add_paragraph(); run(p, f"Document ref {ref} · CUTTLEFLOW PTY LTD T/A CUTTLEFLOW SYSTEMS", font="Consolas", size=9)
    if manifest.get("draft"):
        p = doc.add_paragraph(); run(p, "DRAFT — SUBJECT TO LEGAL REVIEW — NOT FOR USE", bold=True, color=ORANGE)
    for _ in range(8): doc.add_paragraph()
    p = doc.add_paragraph(); run(p, "33°53′S · 151°16′E · Sydney", font="Consolas", size=8)
    p.add_run().add_break(WD_BREAK.PAGE)

    # running header and footer (suppressed on the cover by different_first_page_header_footer)
    sec = doc.sections[0]
    hp = sec.header.paragraphs[0]
    run(hp, ("DRAFT — NOT FOR USE · " if manifest.get("draft") else "") + f"{manifest['title'].upper()} · V{v}", font="Consolas", size=8, color=GREEN)
    fp = sec.footer.paragraphs[0]
    run(fp, f"33°53′S · 151°16′E · Sydney     {ref} · CUTTLEFLOW PTY LTD T/A CUTTLEFLOW SYSTEMS", font="Consolas", size=8)

    idx = 0
    for s in structure:
        sc = cmap.get(s["section"])
        if sc:
            p = doc.add_paragraph(); run(p, sc["heading"], font="Georgia", size=16, bold=True, color=INK); bookmark(p, bm(sc["id"]), idx); idx += 1
            if sc["body"]:
                body(sc)
        if sc and s["clauses"] and all(cmap[c]["type"] == "definition" for c in s["clauses"]):
            t = doc.add_table(rows=0, cols=2); t.style = "Table Grid"; t.autofit = False
            for cid in s["clauses"]:
                c = cmap[cid]; cells = t.add_row().cells
                cells[0].width, cells[1].width = Cm(4.6), Cm(12.0)
                p = cells[0].paragraphs[0]; run(p, c["heading"], bold=True); bookmark(p, bm(cid), idx); idx += 1
                first = True
                for kind, val in blocks(c["body"]):
                    p = cells[1].paragraphs[0] if first else cells[1].add_paragraph(); first = False
                    inline(p, val if kind == "p" else "; ".join(val))
            continue
        for cid in s["clauses"]:
            c = cmap[cid]
            big = c["type"] in ("preamble", "claims", "library", "notice")
            p = doc.add_paragraph(); run(p, c["heading"], font="Georgia", size=16 if big else 12.5, bold=True, color=INK if big else GREEN)
            bookmark(p, bm(cid), idx); idx += 1
            body(c)

    if changes_md:
        p = doc.add_paragraph(); run(p, f"Changes From the Previous Version", font="Georgia", size=16, bold=True)
        doc.add_paragraph("Recorded in accordance with the Cuttleflow open wording library versioning requirements.")
        for kind, val in blocks(changes_md):
            if kind == "ul":
                for i in val: inline(doc.add_paragraph(style="List Bullet"), i)
            elif kind == "p":
                inline(doc.add_paragraph(), val)

    p = doc.add_paragraph(); run(p, "Cuttleflow Systems — Open Source Insurance Wording", italic=True, size=9)
    p = doc.add_paragraph(); run(p, f"{ref} · v{v} · {manifest['date']} · © 2026 Cuttleflow Pty Ltd trading as Cuttleflow Systems", font="Consolas", size=8)
    if manifest.get("draft"):
        p = doc.add_paragraph(); run(p, "This document is a draft subject to legal review. It must not be issued, quoted from, or bound until Wording Partner sign-off.", size=9, italic=True)
    doc.core_properties.title = manifest["title"]; doc.core_properties.author = "Cuttleflow Pty Ltd trading as Cuttleflow Systems"
    doc.save(path)


# ---------------------------------------------------------------- endorsement form

def endorsement(manifest, base_manifest, cmap):
    """Build the base-plus-endorsement form of a profession wording from the same overrides."""
    base_title = base_manifest["title"]
    gen = {}
    order = []

    def add(cid, heading, body, trigger=None):
        gen[cid] = dict(id=cid, type="preamble", heading=heading, body=body, path="(generated)", trigger=trigger)
        order.append(cid)

    add("end.application", "Application",
        f"This endorsement attaches to and forms part of the Meridian {base_title} wording, version {base_manifest['version']} "
        f"(document reference {base_manifest['doc_ref']}), referred to here as the base wording. It changes the base wording only "
        "as set out below. All other terms, conditions, exclusions and limits of the base wording continue to apply.\n\n"
        "Words defined in the base wording have the same meaning in this endorsement. Where this endorsement and the base "
        "wording conflict, this endorsement applies to the extent of the conflict.\n\n"
        f"The same terms are published as a single integrated wording, {manifest['title']}, version {manifest['version']}. "
        "Both documents are generated from the same source and have the same effect.")
    for i, op in enumerate(manifest.get("overrides", []) or []):
        kind = op["op"]
        if kind == "replace":
            old, new = cmap[op["target"]], cmap[op["with"]]
            intro = f"{ref_text(old)[0].upper() + ref_text(old)[1:]} in the base wording is deleted and replaced with the following."
            add(f"end.{i}", f"Replaced: {old['heading']}", intro + f"\n\n**{new['heading']}**\n\n" + new["body"])
        elif kind == "add" and cmap[op["clause"]]["type"] in ("library", "endorsement"):
            new = cmap[op["clause"]]  # optional endorsements are reproduced as they appear in the integrated wording
            add(f"end.{i}", new["heading"], new["body"], new.get("trigger"))
        elif kind == "add":
            new = cmap[op["clause"]]
            after = cmap.get(op["after"])
            where = f", after {ref_text(after)}" if after else ""
            noun = KIND.get(new["type"], "clause") or "clause"
            add(f"end.{i}", f"Added: {new['heading']}", f"The following {noun} is added to the base wording{where}."
                + f"\n\n**{new['heading']}**\n\n" + new["body"])
        elif kind == "delete":
            old = cmap[op["target"]]
            add(f"end.{i}", f"Removed: {old['heading']}", f"{ref_text(old)[0].upper() + ref_text(old)[1:]} in the base wording does not apply.")
    em = dict(manifest)
    em.update({"id": manifest["id"] + "-endorsement", "form": "endorsement",
               "title": manifest.get("endorsement_title", manifest["title"] + " — Endorsement"),
               "summary": f"The {manifest['title']} terms, in the form of an endorsement to the base {base_title} wording."})
    allmap = dict(cmap); allmap.update(gen)
    return em, [dict(section="endorsement", clauses=order)], allmap


# ---------------------------------------------------------------- record

def build_record(manifest, structure, cmap):
    rec = {"wording": manifest["id"], "version": str(manifest["version"]), "doc_ref": manifest["doc_ref"],
           "base": manifest.get("base"), "clauses": []}
    for s in structure:
        for cid in ([s["section"]] if s["section"] in cmap else []) + s["clauses"]:
            c = cmap[cid]
            text = c["heading"] + "\n" + plain(c["body"], cmap)
            rec["clauses"].append({"id": cid, "heading": c["heading"], "sha256": hashlib.sha256(text.encode()).hexdigest()})
    rec["endorsements"] = [
        {"id": c["id"], "heading": c["heading"], "trigger": c["trigger"],
         "questions": [QUESTIONS[q] for q in c["trigger"]["questions"]]}
        for s in structure for c in (cmap[x] for x in s["clauses"]) if c.get("trigger")]
    rec["sha256"] = hashlib.sha256(json.dumps(rec["clauses"], sort_keys=True).encode()).hexdigest()
    return rec


# ---------------------------------------------------------------- main

def wordings():
    """Yield (class, manifest path) for every wording in source/."""
    for cls_dir in sorted(p for p in SOURCE.iterdir() if p.is_dir()):
        yield cls_dir.name, cls_dir / "base.yaml"
        for m in sorted((cls_dir / "professions").glob("*.yaml")) if (cls_dir / "professions").exists() else []:
            yield cls_dir.name, m


def main(argv):
    mode = argv[1] if len(argv) > 1 else "check"
    errors, built = [], []
    for cls, mpath in wordings():
        QUESTIONS.clear(); QUESTIONS.update(load_questions(cls))
        clauses = load_class(cls)
        manifest = load_manifest(mpath)
        structure, cmap = resolve(cls, manifest, clauses, errors)
        check(manifest, structure, cmap, errors)
        built.append((cls, manifest, structure, cmap))
    if errors:
        print("Checks failed:\n" + "\n".join(f"  - {e}" for e in errors))
        return 1
    print(f"Checks passed for {len(built)} wording(s).")
    if mode != "build":
        return 0
    for cls, manifest, structure, cmap in built:
        if "base" not in manifest:
            manifest["professions"] = sorted(
                (dict(slug=m["slug"], title=m["title"], version=m["version"], doc_ref=m["doc_ref"])
                 for c, m, _s, _m in built if c == cls and "base" in m), key=lambda p: p["title"])
    for cls, manifest, structure, cmap in built:
        QUESTIONS.clear(); QUESTIONS.update(load_questions(cls))
        slug = manifest["slug"]
        if "base" in manifest:
            bslug = load_manifest(SOURCE / cls / "base.yaml")["slug"]
            manifest["links"] = [("Endorsement form", f"{slug}-endorsement.html"), ("Base wording", f"{bslug}.html")]
        stem = manifest["file_stem"]
        docx_name = f"{stem}_v{manifest['version']}.docx"
        (ROOT / "wordings" / f"{slug}.html").write_text(render_html(manifest, structure, cmap, slug, docx_name), encoding="utf-8")
        rec_dir = ROOT / "records" / manifest["id"]; rec_dir.mkdir(parents=True, exist_ok=True)
        (rec_dir / f"{manifest['version']}.json").write_text(json.dumps(build_record(manifest, structure, cmap), indent=1) + "\n")
        if "--no-docx" not in argv:
            ch = SOURCE / cls / "changes" / f"{manifest['id']}-{manifest['version']}.md"
            render_docx(manifest, structure, cmap, ROOT / "wordings" / "downloads" / docx_name,
                        ch.read_text(encoding="utf-8") if ch.exists() else "")
        print(f"Built {manifest['id']} {manifest['version']} -> wordings/{slug}.html")
        if "base" in manifest:
            base_manifest = load_manifest(SOURCE / cls / "base.yaml")
            em, es, emap = endorsement(manifest, base_manifest, cmap)
            eslug, edocx = f"{slug}-endorsement", f"{stem}_Endorsement_v{manifest['version']}.docx"
            em["links"] = [("Integrated wording", f"{slug}.html"), ("Base wording", f"{base_manifest['slug']}.html")]
            LINK.update(ids=set(es[0]["clauses"]), page=f"{base_manifest['slug']}.html")
            (ROOT / "wordings" / f"{eslug}.html").write_text(render_html(em, es, emap, eslug, edocx), encoding="utf-8")
            if "--no-docx" not in argv:
                render_docx(em, es, emap, ROOT / "wordings" / "downloads" / edocx, "")
            LINK.update(ids=None, page="")
            print(f"Built {em['id']} {manifest['version']} -> wordings/{eslug}.html")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except BuildError as e:
        print(f"Build error: {e}"); sys.exit(1)

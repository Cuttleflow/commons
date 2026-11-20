#!/usr/bin/env python3
"""Build the Commons wording list from one data file.

Reads  tools/hub/library.json   (groups, order, descriptions, profession links)
       wordings/<slug>.html     (current code and version of each wording)
Writes index.html               (the list between the hub markers, and every data-n count)
       why.html                 (its data-n counts)
       assets/library.js        (the related-wordings block on each wording page)

Usage:
  python3 tools/hub/build_hub.py                      # rebuild in place
  python3 tools/hub/build_hub.py --copy-to PATH       # also write an identical copy of index.html
                                                      # (e.g. ../website/site/commons/index.html)
  python3 tools/hub/build_hub.py --check              # fail if index.html or library.js is out of date

Fails if a wording page exists that library.json does not list, or the reverse.
"""
import html, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "tools" / "hub" / "library.json"
INDEX = ROOT / "index.html"
LIBJS = ROOT / "assets" / "library.js"
BASE = "https://commons.cuttleflow.com/wordings/"
HUB = "https://commons.cuttleflow.com/"

esc = lambda s: html.escape(s, quote=False)
attr = lambda s: html.escape(s, quote=True)


def meta(slug):
    page = (ROOT / "wordings" / f"{slug}.html").read_text(encoding="utf-8")
    ver = re.search(r'class="draft-flag">Draft (v\d+\.\d+\.\d+)', page)
    code = re.search(r"title=%5B(20\d\d/[A-Z]+/\d+(?:-[A-Z]+)?)%5D", page)
    if not (ver and code):
        sys.exit(f"build_hub: cannot read version or code from wordings/{slug}.html")
    return code.group(1), ver.group(1)


def load():
    d = json.loads(DATA.read_text(encoding="utf-8"))
    W, P = d["wordings"], d["professions"]
    listed = [s for g in d["groups"] for sg in g["subgroups"] for s in sg["slugs"]]
    allp = [s for v in P.values() for s in v]
    pages = {p.stem for p in (ROOT / "wordings").glob("*.html") if not p.stem.endswith("-endorsement")}
    errors = []
    for s in sorted(pages - set(listed) - set(allp)):
        errors.append(f"wordings/{s}.html is not listed in library.json")
    for s in sorted((set(listed) | set(allp)) - pages):
        errors.append(f"library.json lists {s}, but wordings/{s}.html does not exist")
    for s in allp:
        if not (ROOT / "wordings" / f"{s}-endorsement.html").exists():
            errors.append(f"profession wording {s} has no wordings/{s}-endorsement.html")
    for s in set(listed) | set(allp):
        if s not in W:
            errors.append(f"library.json has no entry under 'wordings' for {s}")
    if errors:
        sys.exit("build_hub:\n  " + "\n  ".join(errors))
    for s in W:
        W[s]["code"], W[s]["ver"] = meta(s)
    return d


def q(*parts):
    return attr(" ".join(parts).lower())


def row(s, W, P):
    w = W[s]
    subs = P.get(s, [])
    subq = " ".join(W[p]["title"] + " " + W[p]["code"] for p in subs)
    out = [f'<li class="wrow" data-own="{q(w["title"], w["code"], w["desc"])}" data-q="{q(w["title"], w["code"], w["desc"], subq)}">'
           f'<a class="wlink" href="{BASE}{s}.html"><span class="wt">{esc(w["title"])}</span><span class="wd">{esc(w["desc"])}</span></a>'
           f'<span class="wm"><span>{w["code"]}</span><span>{w["ver"]} draft</span></span>']
    if subs:
        subs = sorted(subs, key=lambda p: W[p]["short"])
        out.append(f'<details class="wsub"><summary>{len(subs)} profession wordings built on this form</summary><ul>')
        for p in subs:
            x = W[p]
            out.append(f'<li class="wprow" data-q="{q(x["title"], x["code"])}"><a href="{BASE}{p}.html">{esc(x["short"])}</a>'
                       f'<span class="wm"><span>{x["code"]}</span><span>{x["ver"]} draft</span>'
                       f'<a href="{BASE}{p}-endorsement.html">Endorsement</a></span></li>')
        out.append("</ul></details>")
    out.append("</li>")
    return "\n".join(out)


def build_section(d):
    W, P = d["wordings"], d["professions"]
    nav, parts, total = [], [], 0
    for g in d["groups"]:
        slugs = [s for sg in g["subgroups"] for s in sg["slugs"]]
        n = len(slugs) + sum(len(P.get(s, [])) for s in slugs)
        total += n
        name = esc(g["name"])
        nav.append(f'<a href="#g-{g["id"]}" data-g="{g["id"]}">{name}<span>{n}</span></a>')
        parts.append(f'<section class="wgroup" id="g-{g["id"]}" data-g="{g["id"]}"><header class="wgh"><h3>{name}</h3>'
                     f'<span class="mono wcount">{n} wording{"" if n == 1 else "s"}</span></header>\n<p class="wgb">{esc(g["blurb"])}</p>')
        for sg in g["subgroups"]:
            if sg["label"]:
                parts.append(f'<h4 class="wsg mono">{esc(sg["label"])}</h4>')
            parts.append('<ul class="wrows">\n' + "\n".join(row(s, W, P) for s in sg["slugs"]) + "\n</ul>")
        parts.append("</section>")
    counts = {"wordings": total, "groups": len(d["groups"]), "professions": sum(len(v) for v in P.values())}
    section = f'''<section class="section" id="wordings">
<div class="eyebrow-rule"><span class="mono" style="color:var(--green)">The wordings</span><span class="mono" style="color:var(--ink-55)"><span data-n="wordings">{counts["wordings"]}</span> wordings &middot; <span data-n="groups">{counts["groups"]}</span> groups &middot; all draft</span></div>
<div class="wlib">
<aside class="wnav-wrap">
<label class="wsearch"><span class="sr">Search the wordings</span><input id="wq" type="search" placeholder="Search name or code" autocomplete="off"></label>
<nav class="wnav" aria-label="Wording groups">
{chr(10).join(nav)}
</nav>
</aside>
<div class="wlist">
<p class="wnote">Every wording is a draft and is not for use until Wording Partner sign-off. Profession wordings are listed under the form they are built on, and each is also published as an endorsement to that form.</p>
<p class="wempty" id="wempty" hidden>No wording matches that search. <a href="https://github.com/cuttleflow/commons/issues/new/choose">Suggest a new wording</a>.</p>
<p class="sr" id="wlive" aria-live="polite"></p>
{chr(10).join(parts)}
</div>
</div>
</section>'''
    return section, counts


CSS = '''.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.wlib [hidden]{display:none!important}
.wlib>*{min-width:0}
.wlib{display:grid;grid-template-columns:240px 1fr;gap:44px;padding-top:26px;align-items:start}
.wnav-wrap{position:sticky;top:84px}
.wsearch input{width:100%;font:inherit;font-size:14px;padding:10px 12px;border:1px solid var(--rule);background:var(--paper);color:var(--ink);border-radius:0}
.wsearch input:focus{outline:2px solid var(--green);outline-offset:1px}
.wnav{display:flex;flex-direction:column;margin-top:18px;border-top:1px solid var(--rule)}
.wnav a{display:flex;justify-content:space-between;gap:12px;padding:9px 0 9px 12px;border-bottom:1px solid var(--rule-soft);border-left:2px solid transparent;font-size:13.5px;line-height:1.35;color:var(--ink-78);text-decoration:none}
.wnav a span{font-family:var(--mono);font-size:11px;color:var(--ink-55);padding-top:2px}
.wnav a:hover{color:var(--ink)}
.wnav a.on{border-left-color:var(--orange);color:var(--ink);font-weight:500}
.wnav a.dim{opacity:.4}
.wnote{font-size:13px;line-height:1.55;color:var(--ink-72);max-width:70ch;margin:0 0 6px}
.wempty{font-size:15px;margin:24px 0}
.wgroup{padding:30px 0 6px;scroll-margin-top:84px}
.wgroup+.wgroup{border-top:1px solid var(--rule)}
.wgh{display:flex;justify-content:space-between;align-items:baseline;gap:16px}
.wgh h3{font-family:var(--serif);font-size:26px;font-weight:500;line-height:1.2;margin:0}
.wcount{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-55);white-space:nowrap}
.wgb{font-size:14px;color:var(--ink-72);margin:6px 0 10px;max-width:64ch}
.wsg{font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--green);margin:20px 0 2px;font-weight:400}
.wrows{list-style:none;margin:0;padding:0}
.wrow{display:grid;grid-template-columns:1fr auto;column-gap:24px;padding:13px 0;border-bottom:1px solid var(--rule-soft)}
.wrow:last-child{border-bottom:0}
.wlink{display:block;text-decoration:none;color:var(--ink);min-width:0}
.wlink .wt{display:block;font-size:16.5px;font-weight:500;line-height:1.35}
.wlink:hover .wt{color:var(--orange-dark);text-decoration:underline;text-underline-offset:3px}
.wlink .wd{display:block;font-size:13.5px;line-height:1.5;color:var(--ink-72);margin-top:2px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.wm{display:flex;gap:12px;font-family:var(--mono);font-size:11.5px;color:var(--ink-55);white-space:nowrap;padding-top:4px}
.wm a{color:var(--green)}
.wsub{grid-column:1/-1;margin-top:10px;border-left:2px solid var(--vellum);padding-left:14px}
.wsub summary{cursor:pointer;font-size:13.5px;color:var(--green);padding:4px 0}
.wsub ul{list-style:none;margin:4px 0 0;padding:0}
.wprow{display:flex;justify-content:space-between;gap:16px;padding:8px 0;border-top:1px solid var(--rule-soft);font-size:14.5px}
.wprow>a{color:var(--ink);text-decoration:none}
.wprow>a:hover{color:var(--orange-dark);text-decoration:underline}
@media (max-width:900px){
 .wlib{grid-template-columns:1fr;gap:0}
 .wnav-wrap{position:static;padding:4px 0 8px;border-bottom:1px solid var(--rule)}
 .wnav{flex-direction:row;overflow-x:auto;gap:8px;margin-top:10px;border-top:0;scrollbar-width:none;-webkit-overflow-scrolling:touch}
 .wnav::-webkit-scrollbar{display:none}
 .wnav a{flex:none;border:1px solid var(--rule);padding:6px 10px;font-size:13px;white-space:nowrap;gap:8px}
 .wnav a.on{border-color:var(--ink);background:var(--ink);color:var(--paper)}
 .wnav a.on span{color:var(--vellum)}
 .wnote{margin-top:16px}
 .wgroup{scroll-margin-top:120px}
 .wgh h3{font-size:22px}
 .wrow{grid-template-columns:1fr}
 .wlink .wd{white-space:normal;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
 .wm{padding-top:6px;font-size:11px;flex-wrap:wrap}
 .wprow{flex-direction:column;gap:2px}
}'''

JS = '''<script>
(function(){
 var q=document.getElementById('wq'); if(!q) return;
 var groups=[].slice.call(document.querySelectorAll('.wgroup'));
 var links=[].slice.call(document.querySelectorAll('.wnav a'));
 var empty=document.getElementById('wempty'), live=document.getElementById('wlive');
 function setOn(id){links.forEach(function(a){var on=a.dataset.g===id;a.classList.toggle('on',on);if(on&&window.innerWidth<=900){a.parentNode.scrollLeft=a.offsetLeft-a.parentNode.offsetLeft-20;}});}
 if('IntersectionObserver' in window){
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)setOn(e.target.dataset.g);});},{rootMargin:'-30% 0px -65% 0px'});
  groups.forEach(function(g){io.observe(g);});
 }
 q.addEventListener('input',function(){
  var t=q.value.trim().toLowerCase(), shown=0;
  groups.forEach(function(g){
   var n=0;
   g.querySelectorAll('.wrow').forEach(function(r){
    var hit=!t||r.dataset.q.indexOf(t)>-1; r.hidden=!hit; if(hit)n++;
    var d=r.querySelector('details');
    if(d){var own=r.dataset.own.indexOf(t)>-1,sub=0;d.querySelectorAll('.wprow').forEach(function(p){p.hidden=!!t&&!own&&p.dataset.q.indexOf(t)<0;if(!p.hidden)sub++;});d.open=!!t&&!own&&sub>0;}
   });
   g.querySelectorAll('.wsg').forEach(function(h){h.hidden=!h.nextElementSibling.querySelector('.wrow:not([hidden])');});
   g.hidden=n===0; shown+=n;
   var a=document.querySelector('.wnav a[data-g="'+g.dataset.g+'"]'); if(a)a.classList.toggle('dim',n===0);
  });
  empty.hidden=shown>0; live.textContent=t?(shown+' matching entries'):'';
 });
})();
</script>'''


def build_libjs(d, counts):
    W, P = d["wordings"], d["professions"]
    groups = [{"id": g["id"], "name": g["name"], "subs": [sg["slugs"] for sg in g["subgroups"]]} for g in d["groups"]]
    items = {s: {"t": w["title"], "cls": w["cls"], "code": w["code"], "ver": w["ver"]} for s, w in W.items()}
    # One item per line, so parallel changes to different wordings merge without conflicts.
    item_lines = ",\n".join(f'  {json.dumps(s)}:{json.dumps(v, ensure_ascii=False, separators=(",", ":"))}' for s, v in sorted(items.items()))
    data = ("{\n" + f' "total":{counts["wordings"]},\n'
            + f' "groups":{json.dumps(groups, ensure_ascii=False, separators=(",", ":"))},\n'
            + f' "professions":{json.dumps(P, ensure_ascii=False, separators=(",", ":"))},\n'
            + ' "items":{\n' + item_lines + "\n }\n}")
    return f'''/* Related wordings on each wording page. GENERATED by tools/hub/build_hub.py from
   tools/hub/library.json -- do not edit by hand. Shows the other wordings in the same
   product group (for a profession wording: its base form and the other professions),
   and links back to the full library. */
var COMMONS_LIBRARY = {data};
(function(){{
  var box=document.getElementById("more-wordings"); if(!box) return;
  var L=COMMONS_LIBRARY, here=(location.pathname.split("/").pop()||"").replace(".html","").replace(/-endorsement$/,"");
  var parent=null, list=[], label="";
  Object.keys(L.professions).forEach(function(p){{ if(L.professions[p].indexOf(here)>-1) parent=p; }});
  if(parent){{
    list=[parent].concat(L.professions[parent].filter(function(s){{return s!==here;}}));
    label="More built on "+L.items[parent].t;
  }} else {{
    L.groups.forEach(function(g){{
      var mine=g.subs.filter(function(sub){{return sub.indexOf(here)>-1;}})[0]; if(!mine) return;
      var rest=[].concat.apply([],g.subs.filter(function(sub){{return sub!==mine;}}));
      list=mine.concat(rest).filter(function(s){{return s!==here;}}); label="More in "+g.name;
    }});
    if(L.professions[here]) list=L.professions[here].concat(list);
  }}
  var head=box.parentNode.querySelector(".eyebrow-rule");
  if(head){{
    var sp=head.querySelectorAll("span");
    if(sp[0]) sp[0].textContent=label||"The rest of the library";
    if(sp[1]) sp[1].innerHTML='<a href="{HUB}#wordings">All '+L.total+' wordings &rarr;</a>';
  }}
  list.slice(0,8).forEach(function(s){{
    var w=L.items[s]; if(!w) return;
    var a=document.createElement("a"); a.className="more-card"; a.href=s+".html";
    var c=document.createElement("span"); c.className="cls"; c.textContent=w.cls;
    var t=document.createElement("span"); t.className="t"; t.textContent=w.t;
    var st=document.createElement("span"); st.className="st"; st.textContent=w.code+" \\u00b7 "+w.ver+" draft";
    a.appendChild(c); a.appendChild(t); a.appendChild(st); box.appendChild(a);
  }});
  if(list.length>8){{
    var m=document.createElement("a"); m.className="more-card"; m.href="{HUB}#wordings";
    m.innerHTML='<span class="cls">Library</span><span class="t">See all '+L.total+' wordings</span><span class="st">'+(list.length-8)+' more in this group &rarr;</span>';
    box.appendChild(m);
  }}
}})();
'''


def replace_between(s, start, end, new, what):
    i, j = s.find(start), s.find(end)
    if i < 0 or j < 0:
        sys.exit(f"build_hub: index.html is missing the {what} markers {start} ... {end}")
    return s[: i + len(start)] + "\n" + new + "\n" + s[j:]


def main(argv):
    d = load()
    section, counts = build_section(d)
    s = INDEX.read_text(encoding="utf-8")
    s = replace_between(s, "<!-- hub:list:start -->", "<!-- hub:list:end -->", section, "list")
    s = replace_between(s, "/* hub:css:start */", "/* hub:css:end */", CSS, "CSS")
    s = replace_between(s, "<!-- hub:js:start -->", "<!-- hub:js:end -->", JS, "script")
    for k, v in counts.items():
        s = re.sub(rf'(<span data-n="{k}">)\d+(</span>)', rf"\g<1>{v}\g<2>", s)
    s = re.sub(r'(content="The library holds )\d+', rf"\g<1>{counts['wordings']}", s)
    s = re.sub(r'("description":"The library holds )\d+', rf"\g<1>{counts['wordings']}", s)
    js = build_libjs(d, counts)
    if "--check" in argv:
        stale = [p.name for p, new in ((INDEX, s), (LIBJS, js)) if p.read_text(encoding="utf-8") != new]
        if stale:
            sys.exit("build_hub: out of date, run tools/hub/build_hub.py: " + ", ".join(stale))
        print("build_hub: up to date"); return
    WHY = ROOT / "why.html"
    w = WHY.read_text(encoding="utf-8")
    for k, v in counts.items():
        w = re.sub(rf'(<span data-n="{k}">)\d+(</span>)', rf"\g<1>{v}\g<2>", w)
    INDEX.write_text(s, encoding="utf-8")
    LIBJS.write_text(js, encoding="utf-8")
    WHY.write_text(w, encoding="utf-8")
    if "--copy-to" in argv:
        dest = pathlib.Path(argv[argv.index("--copy-to") + 1])
        dest.write_text(s, encoding="utf-8")
        print(f"build_hub: copied index.html to {dest}")
    print(f"build_hub: {counts['wordings']} wordings, {counts['groups']} groups, {counts['professions']} profession wordings")


if __name__ == "__main__":
    main(sys.argv[1:])

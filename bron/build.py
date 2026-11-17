"""Bouwt de website uit de bestanden in de map bron.

Gebruik (vanuit de hoofdmap van de repo):
    pip install markdown pymdown-extensions
    python bron/build.py

Elke module staat in bron/module-N.md. Een module bestaat uit pagina's,
gescheiden door een regel als:  === blok-2 | display: flex
"""

import html
import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
BRON = ROOT / "bron"

SITE_TITEL = "Webdevelopment"
SITE_ONDERTITEL = "Keuzedeel Oriëntatie op applicatieontwikkeling"


# ---------- demo-blokken: HTML/CSS die echt getekend wordt ----------

DEMO_BASIS = (
    "<style>body{margin:0;padding:14px;font-family:Arial,sans-serif;"
    "font-size:15px;color:#1B1F3B;background:#fff}</style>"
)


def demo_validator(language, inputs, options, attrs, md):
    for k, v in inputs.items():
        options[k] = v
    return True


def demo_formatter(src, language, class_name, options, md, **kwargs):
    titel = options.get("titel", "")
    doc = DEMO_BASIS + src
    srcdoc = html.escape(doc, quote=True)
    kop = f'<div class="demo-titel">{html.escape(titel)}</div>' if titel else ""
    return (
        f'<figure class="demo">{kop}<iframe class="demo-frame" loading="lazy" '
        f'title="{html.escape(titel or "Voorbeeld")}" srcdoc="{srcdoc}" '
        "style=\"height:40px\" onload=\"this.style.height=(this.contentDocument.body.offsetHeight+4)+'px'\">"
        "</iframe></figure>"
    )


def maak_md():
    return markdown.Markdown(
        extensions=[
            "admonition",
            "attr_list",
            "md_in_html",
            "tables",
            "pymdownx.details",
            "pymdownx.highlight",
            "pymdownx.inlinehilite",
            "pymdownx.superfences",
        ],
        extension_configs={
            "pymdownx.highlight": {"use_pygments": True, "css_class": "code"},
            "pymdownx.superfences": {
                "custom_fences": [
                    {
                        "name": "demo",
                        "class": "demo",
                        "format": demo_formatter,
                        "validator": demo_validator,
                    }
                ]
            },
        },
    )


# ---------- bronbestanden lezen ----------

def lees_module(pad):
    tekst = pad.read_text(encoding="utf-8")
    meta = {}
    if tekst.startswith("---"):
        _, kop, tekst = tekst.split("---", 2)
        for regel in kop.strip().splitlines():
            sleutel, _, waarde = regel.partition(":")
            meta[sleutel.strip()] = waarde.strip()
    paginas = []
    huidig = None
    for regel in tekst.splitlines():
        m = re.match(r"^===\s*([a-z0-9-]+)\s*\|\s*(.+?)\s*$", regel)
        if m:
            huidig = {"slug": m.group(1), "titel": m.group(2), "regels": []}
            paginas.append(huidig)
        elif huidig is not None:
            huidig["regels"].append(regel)
    for p in paginas:
        p["md"] = "\n".join(p["regels"]).strip() + "\n"
        del p["regels"]
        m = re.match(r"blok-(\d+)", p["slug"])
        p["label"] = f"Blok {m.group(1)}" if m else ""
    meta["nr"] = int(meta["nr"])
    meta["tags"] = [t.strip() for t in meta.get("tags", "").split("|") if t.strip()]
    meta["paginas"] = paginas
    meta["map"] = f"module-{meta['nr']}"
    return meta


# ---------- HTML ----------

def pagina_html(titel, inhoud, diepte, extra_head=""):
    pre = "../" * diepte
    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(titel)}</title>
<link rel="stylesheet" href="{pre}assets/style.css">
{extra_head}</head>
<body>
<header class="site">
  <div class="bar">
    <a class="merk" href="{pre}index.html"><span>&lt;/&gt;</span> {SITE_TITEL}</a>
    <nav><a href="{pre}index.html">Alle modules</a></nav>
  </div>
</header>
{inhoud}
<script>
  (function () {{
    var d = document.querySelector('.inhoudsopgave');
    if (!d) return;
    var smal = window.matchMedia('(max-width: 860px)');
    if (smal.matches) d.removeAttribute('open');
    d.querySelector('summary').addEventListener('click', function (e) {{ if (!smal.matches) e.preventDefault(); }});
  }})();
</script>
<footer class="site">{SITE_ONDERTITEL} · ROC Midden Nederland</footer>
</body>
</html>
"""


def bouw_home(modules):
    kaarten = []
    for m in modules:
        examen = m.get("soort") == "examen"
        klasse = "module examen" if examen else "module"
        if m.get("status") == "binnenkort":
            klasse += " binnenkort"
        label = f"Module {m['nr']}" + (" · Examen" if examen else "")
        tags = "".join(f"<span>{html.escape(t)}</span>" for t in m["tags"])
        kaarten.append(
            f'<a class="{klasse}" href="{m["map"]}/index.html">'
            f'<div class="nr">{label}</div><h2>{html.escape(m["titel"])}</h2>'
            f'<p>{html.escape(m["kort"])}</p><div class="tags">{tags}</div></a>'
        )
    inhoud = f"""<main class="home">
  <div class="intro">
    <h1>Bouw je eigen website</h1>
    <p>{SITE_ONDERTITEL}. Zes modules, stap voor stap. Kies een module om de uitleg en de opdrachten te bekijken.</p>
  </div>
  <div class="modules">
    {''.join(kaarten)}
  </div>
</main>"""
    (ROOT / "index.html").write_text(pagina_html(SITE_TITEL, inhoud, 0), encoding="utf-8")


def bouw_module(m):
    map_ = ROOT / m["map"]
    if map_.exists():
        shutil.rmtree(map_)
    map_.mkdir()
    paginas = m["paginas"]
    for i, p in enumerate(paginas):
        bestand = "index.html" if i == 0 else f"{p['slug']}.html"
        p["bestand"] = bestand

    for i, p in enumerate(paginas):
        md = maak_md()
        body = md.convert(p["md"])

        links = []
        for j, q in enumerate(paginas):
            actief = ' class="actief"' if j == i else ""
            nummer = f'<small>{q["label"].split()[-1]}</small>' if q["label"] else ""
            if not q["label"] and j > 0 and paginas[j - 1]["label"]:
                links.append("<hr>")
            links.append(f'<a href="{q["bestand"]}"{actief}>{nummer}{html.escape(q["titel"])}</a>')
        zijbalk = "\n".join(links)

        vorige = paginas[i - 1] if i > 0 else None
        volgende = paginas[i + 1] if i + 1 < len(paginas) else None

        def knop(q, richting):
            if not q:
                return "<span></span>"
            naam = (q["label"] + " · " if q["label"] else "") + q["titel"]
            pijl_l, pijl_r = ("← ", "") if richting == "vorige" else ("", " →")
            return f'<a class="{richting}" href="{q["bestand"]}">{pijl_l}{html.escape(naam)}{pijl_r}</a>'

        label = f'<div class="bloklabel">{p["label"].upper()}</div>' if p["label"] else ""
        inhoud = f"""<div class="kruimel"><a href="../index.html">Modules</a> › Module {m['nr']}</div>
<div class="module-kop"><h1>Module {m['nr']} · {html.escape(m['titel'])}</h1><p>{html.escape(m['kort'])}</p></div>
<div class="layout">
  <aside>
    <details class="inhoudsopgave" open>
      <summary>In deze module</summary>
      <nav>{zijbalk}</nav>
    </details>
  </aside>
  <article>
    {label}
    <h2 class="paginatitel">{html.escape(p['titel'])}</h2>
    {body}
    <div class="vorige-volgende">{knop(vorige, 'vorige')}{knop(volgende, 'volgende')}</div>
  </article>
</div>"""
        titel = f"{p['titel']} · Module {m['nr']} · {SITE_TITEL}"
        (map_ / p["bestand"]).write_text(pagina_html(titel, inhoud, 1), encoding="utf-8")


def bouw_assets():
    from pygments.formatters import HtmlFormatter
    css = (BRON / "style-basis.css").read_text(encoding="utf-8")
    kleuren = HtmlFormatter(style="github-dark").get_style_defs(".code")
    kleuren = "\n".join(r for r in kleuren.splitlines() if not r.startswith(".code { background") and "pre {" not in r)
    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "assets" / "style.css").write_text(css + "\n/* codekleuren (pygments) */\n" + kleuren + "\n", encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")


def main():
    bouw_assets()
    modules = [lees_module(p) for p in sorted(BRON.glob("module-*.md"))]
    modules.sort(key=lambda m: m["nr"])
    for m in modules:
        bouw_module(m)
    bouw_home(modules)
    print(f"Klaar: {len(modules)} modules, {sum(len(m['paginas']) for m in modules)} pagina's.")


if __name__ == "__main__":
    main()

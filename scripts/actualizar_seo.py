#!/usr/bin/env python3
"""
Actualizar SEO + sitemap.xml — CyR 1º ESO
═══════════════════════════════════════════════════════════════════
Hace dos cosas en una pasada (idempotente):

  1. Regenera sitemap.xml con todos los HTMLs públicos del sitio.
  2. Inyecta canonical + Open Graph + Twitter Card en cada HTML que
     no los tenga ya. Los bloques se colocan justo antes del
     <link rel="preconnect"> para mantener el orden lógico del <head>.

Uso:
    python3 scripts/actualizar_seo.py

Se ancla automáticamente a la raíz del sitio. Lánzalo cada vez que
añadas/edites páginas, cambies títulos o descripciones.
"""
import os, re, sys, glob
from pathlib import Path
from datetime import date

# ── Configuración del sitio ─────────────────────────────────────────
DOMAIN = "https://cyr1-ies-jdq.malonso72.workers.dev"
SITE_NAME = "CyR 1º ESO — IES Jiménez de Quesada"
OG_IMAGE = f"{DOMAIN}/img/fachadaiesjdq.jpg"

# ── Anclar a la raíz del sitio ──────────────────────────────────────
os.chdir(Path(__file__).resolve().parent.parent)

# UTF-8 stdout (consolas Windows cp1252)
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

EXCLUDE_PARTS = {"documentacion", "_soluciones", ".git", ".wrangler", "node_modules", "templates"}
TODAY = date.today().isoformat()

# ── Helpers ─────────────────────────────────────────────────────────

def is_public(rel: Path) -> bool:
    return not any(p in EXCLUDE_PARTS for p in rel.parts)

def canonical_for(rel: Path) -> str:
    parts = list(rel.parts)
    if parts[-1] == "index.html":
        if len(parts) == 1:
            return f"{DOMAIN}/"
        return f"{DOMAIN}/" + "/".join(parts[:-1]) + "/"
    return f"{DOMAIN}/" + "/".join(parts)

def priority_for(rel: Path):
    parts = rel.parts
    if len(parts) == 1 and parts[0] == "index.html":
        return ("1.0", "weekly")
    if parts[-1] == "index.html":
        return ("0.8", "monthly")
    return ("0.7", "monthly")

def attr_safe(s: str) -> str:
    return (s.replace("&amp;", "\x00AMP\x00")
             .replace("&", "&amp;").replace("\x00AMP\x00", "&amp;")
             .replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))

def extract_title(content: str) -> str:
    m = re.search(r"<title>([^<]+)</title>", content, re.IGNORECASE)
    return m.group(1).strip() if m else "IES Jiménez de Quesada"

def extract_description(content: str) -> str:
    m = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', content, re.IGNORECASE)
    return m.group(1).strip() if m else "Material educativo · IES Jiménez de Quesada · Santa Fe (Granada)"

# ── Bloques SEO ─────────────────────────────────────────────────────

def block_canonical(canonical):
    return f'<link rel="canonical" href="{canonical}">'

def block_og(title, description, url):
    return ('\n<!-- ══ Open Graph ══ -->\n'
            f'<meta property="og:title" content="{attr_safe(title)}">\n'
            f'<meta property="og:description" content="{attr_safe(description)}">\n'
            f'<meta property="og:image" content="{OG_IMAGE}">\n'
            f'<meta property="og:url" content="{url}">\n'
            '<meta property="og:type" content="website">\n'
            '<meta property="og:locale" content="es_ES">\n'
            f'<meta property="og:site_name" content="{attr_safe(SITE_NAME)}">')

def block_twitter(title, description):
    return ('\n<!-- ══ Twitter Card ══ -->\n'
            '<meta name="twitter:card" content="summary_large_image">\n'
            f'<meta name="twitter:title" content="{attr_safe(title)}">\n'
            f'<meta name="twitter:description" content="{attr_safe(description)}">\n'
            f'<meta name="twitter:image" content="{OG_IMAGE}">')

def inject_seo(content: str, canonical: str):
    title = extract_title(content)
    description = extract_description(content)

    has_canonical = re.search(r'<link\s+rel="canonical"', content) is not None
    has_og = re.search(r'property="og:title"', content) is not None
    has_twitter = re.search(r'name="twitter:card"', content) is not None

    blocks, changes = [], []
    if not has_canonical:
        blocks.append(block_canonical(canonical));    changes.append("canonical")
    if not has_og:
        blocks.append(block_og(title, description, canonical)); changes.append("og")
    if not has_twitter:
        blocks.append(block_twitter(title, description));       changes.append("twitter")
    if not blocks:
        return content, []

    addition = "\n".join(blocks) + "\n"
    m = re.search(r'^[ \t]*<link\s+rel="preconnect"', content, re.MULTILINE)
    if m:
        return content[:m.start()] + addition + content[m.start():], changes
    return content.replace("</head>", addition + "</head>", 1), changes

# ── Sitemap ─────────────────────────────────────────────────────────

def build_sitemap():
    htmls = []
    for p in sorted(Path(".").rglob("*.html")):
        rel = Path(*p.parts)
        if not is_public(rel):
            continue
        htmls.append(rel)

    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for rel in htmls:
        url = canonical_for(rel)
        prio, freq = priority_for(rel)
        out += ["  <url>",
                f"    <loc>{url}</loc>",
                f"    <lastmod>{TODAY}</lastmod>",
                f"    <changefreq>{freq}</changefreq>",
                f"    <priority>{prio}</priority>",
                "  </url>"]
    out.append("</urlset>")
    out.append("")
    return "\n".join(out), len(htmls)

# ── Main ────────────────────────────────────────────────────────────

def main():
    modif = canon = og = tw = 0
    for p in sorted(Path(".").rglob("*.html")):
        rel = Path(*p.parts)
        if not is_public(rel):
            continue
        content = p.read_text(encoding="utf-8")
        canonical = canonical_for(rel)
        new_content, changes = inject_seo(content, canonical)
        if changes:
            p.write_text(new_content, encoding="utf-8")
            modif += 1
            if "canonical" in changes: canon += 1
            if "og" in changes:        og += 1
            if "twitter" in changes:   tw += 1

    sitemap, n_urls = build_sitemap()
    Path("sitemap.xml").write_text(sitemap, encoding="utf-8")

    print(f"Sitio:            {DOMAIN}")
    print(f"HTMLs procesados: {sum(1 for _ in Path('.').rglob('*.html') if is_public(Path(_)))}")
    print(f"HTMLs modificados:{modif}")
    print(f"  canonical:      {canon}")
    print(f"  og:             {og}")
    print(f"  twitter:        {tw}")
    print(f"sitemap.xml:      {n_urls} URLs")

if __name__ == "__main__":
    main()

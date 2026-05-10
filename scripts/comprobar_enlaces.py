#!/usr/bin/env python3
"""
Comprobador de enlaces internos
═══════════════════════════════════════════
Verifica que todos los enlaces (href, src) de los HTMLs apuntan a archivos
que existen en el repo. Detecta enlaces rotos antes de hacer push.

Uso:
    python3 scripts/comprobar_enlaces.py

El script se ancla automáticamente a la raíz de su propio sitio
(la carpeta padre de scripts/), así que se puede invocar desde
cualquier directorio.
"""
import os, re, glob, sys
from pathlib import Path

# Forzar UTF-8 en stdout para que funcione en consolas Windows (cp1252)
# que no soportan caracteres Unicode como ✗ o ✓.
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

# Anclar el cwd a la raíz del sitio (carpeta padre de scripts/),
# para que glob('**/*.html') solo recorra ESTE sitio, no los hermanos.
os.chdir(Path(__file__).resolve().parent.parent)

EXCLUDE = ["documentacion/", "_soluciones/", ".git/", "node_modules/", ".wrangler/", "assets/templates/"]

def main():
    # Normaliza separadores a '/' para que las exclusiones funcionen
    # tanto en Linux/Mac como en Windows (donde glob devuelve '\').
    htmls = [f for f in glob.glob("**/*.html", recursive=True)
             if not any(e in f.replace("\\", "/") for e in EXCLUDE)]

    broken = []
    total_links = 0
    for f in htmls:
        with open(f, encoding="utf-8", errors="ignore") as fh:
            content = fh.read()
        # Buscar href y src
        links = re.findall(r'(?:href|src)="([^"]+)"', content)
        for link in links:
            # Saltar enlaces externos, mailto, anclas puras y URLs sin protocolo (//ejemplo.com)
            if link.startswith(("http", "https", "mailto:", "#", "data:", "javascript:", "//")):
                continue
            total_links += 1
            # Quitar query y ancla
            target = link.split("?")[0].split("#")[0]
            if not target: continue
            # Resolver ruta relativa
            base_dir = os.path.dirname(f)
            full_target = os.path.normpath(os.path.join(base_dir, target))
            if not os.path.exists(full_target):
                broken.append((f, link, full_target))

    print(f"HTMLs analizados:    {len(htmls)}")
    print(f"Enlaces internos:    {total_links}")
    print(f"Enlaces rotos:       {len(broken)}")
    print()

    if broken:
        for src, link, target in broken[:50]:
            print(f"  [X] {src}")
            print(f"    enlace: {link}")
            print(f"    busca:  {target}")
            print()
        if len(broken) > 50:
            print(f"  ... y {len(broken)-50} más.")
        return 1  # exit code 1 si hay enlaces rotos
    else:
        print("[OK] Todos los enlaces internos validos.")
        return 0

if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
Auditor de imágenes huérfanas
═════════════════════════════════════════
Detecta imágenes en el repo que no están enlazadas desde ningún HTML/CSS/JS.
Las muestra ordenadas por tamaño descendente para que decidas qué borrar.

Uso:
    python3 scripts/auditar_imagenes_huerfanas.py
    python3 scripts/auditar_imagenes_huerfanas.py --mover  # Las mueve a /tmp/orfan_backup/

El script se ancla automáticamente a la raíz de su propio sitio
(la carpeta padre de scripts/), así que se puede invocar desde
cualquier directorio.
"""
import os, sys, glob, shutil
from pathlib import Path

# Anclar el cwd a la raíz del sitio (carpeta padre de scripts/),
# para que glob('**/*.{ext}') solo recorra ESTE sitio, no los hermanos.
os.chdir(Path(__file__).resolve().parent.parent)

EXCLUDE = ["documentacion/", "_soluciones/", ".git/", "node_modules/", ".wrangler/"]

def is_excluded(p):
    return any(e in p for e in EXCLUDE)

def main():
    move_orphans = "--mover" in sys.argv

    # Cargar contenido textual de todos los HTML/CSS/JS
    text_blob = ""
    for ext in ["html", "css", "js"]:
        for f in glob.glob(f"**/*.{ext}", recursive=True):
            if is_excluded(f): continue
            try:
                with open(f, encoding="utf-8", errors="ignore") as fh:
                    text_blob += fh.read() + "\n"
            except Exception:
                pass

    # Listar imágenes
    imgs = []
    for ext in ["jpg", "jpeg", "png", "svg", "gif", "webp", "ico"]:
        imgs += glob.glob(f"**/*.{ext}", recursive=True)
    imgs = [f for f in imgs if not is_excluded(f)]

    orphans = [(f, os.path.getsize(f)) for f in imgs if os.path.basename(f) not in text_blob]
    orphans.sort(key=lambda x: -x[1])

    print(f"Total imágenes:      {len(imgs)}")
    print(f"Posibles huérfanas:  {len(orphans)}")
    if not orphans:
        print("✓ Ninguna huérfana encontrada.")
        return

    total = sum(s for _, s in orphans)
    print(f"Tamaño huérfanas:    {total/1024/1024:.1f} MB")
    print()
    for f, s in orphans:
        print(f"  {s/1024:7.0f} KB  {f}")

    if move_orphans:
        backup = "/tmp/orfan_backup"
        os.makedirs(backup, exist_ok=True)
        for f, _ in orphans:
            target_dir = os.path.join(backup, os.path.dirname(f))
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(f, os.path.join(target_dir, os.path.basename(f)))
        print(f"\n✓ Movidas {len(orphans)} huérfanas a {backup}")
        print("  Si todo sigue funcionando, borra esa carpeta. Si algo falla, restáuralas desde ahí.")
    else:
        print("\nPara mover las huérfanas a /tmp/orfan_backup/, ejecuta:")
        print("    python3 scripts/auditar_imagenes_huerfanas.py --mover")

if __name__ == "__main__":
    main()

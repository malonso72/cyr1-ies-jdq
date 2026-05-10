#!/usr/bin/env python3
"""
Auditor de archivos pesados
══════════════════════════════════════
Lista los archivos del sitio que superan un umbral de tamaño,
para detectar candidatos a optimizar (imágenes sin comprimir,
HTMLs con base64, etc.).

Uso:
    python3 scripts/auditar_archivos_pesados.py
    python3 scripts/auditar_archivos_pesados.py --umbral 200   # KB

El script se ancla automáticamente a la raíz de su propio sitio
(la carpeta padre de scripts/), así que se puede invocar desde
cualquier directorio.
"""
import os, sys, glob
from pathlib import Path

# Anclar el cwd a la raíz del sitio (carpeta padre de scripts/),
# para que glob('**/*') solo recorra ESTE sitio, no los hermanos.
os.chdir(Path(__file__).resolve().parent.parent)

EXCLUDE = ["documentacion/", "_soluciones/", ".git/", "node_modules/", ".wrangler/"]

def main():
    umbral_kb = 100
    if "--umbral" in sys.argv:
        try:
            umbral_kb = int(sys.argv[sys.argv.index("--umbral") + 1])
        except (ValueError, IndexError):
            print("⚠ Argumento --umbral inválido, usando 100 KB")

    files = []
    for f in glob.glob("**/*", recursive=True):
        if not os.path.isfile(f): continue
        if any(e in f for e in EXCLUDE): continue
        s = os.path.getsize(f)
        if s > umbral_kb * 1024:
            files.append((f, s))

    files.sort(key=lambda x: -x[1])

    print(f"Archivos > {umbral_kb} KB: {len(files)}")
    print()
    for f, s in files[:40]:
        print(f"  {s/1024:7.0f} KB  {f}")

    if len(files) > 40:
        print(f"\n  ... y {len(files)-40} más. Usa --umbral mayor para acotar.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Genera versiones STANDALONE de cada sesión de la Academia Cyber-IES.

Para cada sesión sNN.html:
  - Inline el contenido de common.css y academia.css en <style>
  - Inline el contenido de common.js, academia.js y sNN.js en <script>
  - Reemplaza el <iframe src="../retos/sNN-reto-*.html"> por un <iframe srcdoc="...">
    con el HTML del reto escapado dentro
  - Elimina las referencias a archivos externos
  - Quita el favicon (lo deja como SVG inline si interesa, pero por simplicidad lo quitamos)

Salida: _academia-v3/standalone/sNN.html  (un único archivo autocontenido)

Cada standalone:
  - Funciona abierto desde file:// sin red (excepto Google Fonts si se mantiene CDN)
  - Es lo que Manuel sube a Moodle como tarea
  - El alumno descarga UN archivo y lo abre
"""

import re
import os
import sys
from pathlib import Path

ROOT = Path('/sessions/cool-gallant-cray/mnt/cyr1-ies-jdq')
ACAD = ROOT / '_academia-v3'
STANDALONE = ACAD / 'standalone'
STANDALONE.mkdir(exist_ok=True)

# Assets compartidos
COMMON_CSS = (ROOT / 'assets/css/common.css').read_text(encoding='utf-8')
ACADEMIA_CSS = (ACAD / 'assets/css/academia.css').read_text(encoding='utf-8')
COMMON_JS = (ROOT / 'assets/js/common.js').read_text(encoding='utf-8')
ACADEMIA_JS = (ACAD / 'assets/js/academia.js').read_text(encoding='utf-8')

SESIONES = ['s01', 's02', 's12', 's13', 's14', 's15', 's16', 's17', 's18']


def escape_srcdoc(html: str) -> str:
    """Escapa el HTML para usarlo en el atributo srcdoc='...'.
    Como el atributo va entre comillas DOBLES, solo necesitamos escapar las dobles."""
    # Escapar las comillas dobles
    return html.replace('"', '&quot;')


def build_standalone(sesion_id: str) -> str:
    sesion_dir = ACAD / 'sesiones'
    html_path = sesion_dir / f'{sesion_id}.html'
    js_path = sesion_dir / f'{sesion_id}.js' if (sesion_dir / f'{sesion_id}.js').exists() else None
    html = html_path.read_text(encoding='utf-8')

    # S1 tiene el JS inline, las demás tienen JS externo. Detectamos:
    sesion_js = ''
    if js_path is not None:
        sesion_js = js_path.read_text(encoding='utf-8')

    # 1. Quitar <link rel="stylesheet" href="../../assets/css/common.css">
    html = re.sub(r'<link rel="stylesheet" href="\.\./\.\./assets/css/common\.css">', '', html)
    # 2. Quitar <link rel="stylesheet" href="../assets/css/academia.css">
    html = re.sub(r'<link rel="stylesheet" href="\.\./assets/css/academia\.css">', '', html)
    # 3. Quitar <script src="../../assets/js/common.js"></script>
    html = re.sub(r'<script src="\.\./\.\./assets/js/common\.js"></script>', '', html)
    # 4. Quitar <script src="../assets/js/academia.js"></script>
    html = re.sub(r'<script src="\.\./assets/js/academia\.js"></script>', '', html)
    # 5. Quitar <script src="sNN.js"></script>
    html = re.sub(rf'<script src="{sesion_id}\.js"></script>', '', html)
    # 6. Quitar favicon (referencia a ../../favicon.svg)
    html = re.sub(r'<link rel="icon"[^>]*>', '', html)

    # 7. Quitar el chrome del sitio (header curso-hd, nav curso-navcross) para que el archivo
    # standalone sea solo la sesión (sin navegación al resto del sitio que no existe en standalone)
    # MEJOR: mantenerlo pero hacer que el botón "Volver al sitio" NO funcione (queda como un link roto)
    # Simplificación: convertir los enlaces externos a "#" o eliminarlos.
    # Por simplicidad ahora: dejar el chrome pero convertir hrefs problemáticos en '#'.
    # Reemplazar enlaces a ../../index.html → '#' (no salir del archivo)
    html = re.sub(r'href="\.\./\.\./index\.html"', 'href="#"', html)
    # Reemplazar enlaces a ../index.html (Academia) → '#'
    html = re.sub(r'href="\.\./index\.html"', 'href="#"', html)
    # Reemplazar enlaces a sNN.html (siguiente sesión) → '#' (no existe en standalone)
    html = re.sub(r'href="s\d{2}\.html"', 'href="#"', html)

    # Quitar enlace "Abrir en pestaña nueva ↗" del reto (apuntaba a archivo externo)
    html = re.sub(
        r'<a href="\.\./retos/[^"]+" target="_blank"[^>]*>[^<]+</a>',
        '',
        html,
    )

    # 8. Inyectar CSS combinado justo antes de </head> (del HTML padre).
    # IMPORTANTE: hacerlo ANTES del srcdoc replacement para no afectar al </head> del reto.
    css_inline = (
        '<style id="cyr-common-css">\n' + COMMON_CSS + '\n</style>\n'
        '<style id="cyr-academia-css">\n' + ACADEMIA_CSS + '\n</style>'
    )
    html = html.replace('</head>', css_inline + '\n</head>', 1)

    # 9. Inyectar JS combinado justo antes de </body> (del HTML padre).
    # IMPORTANTE: ANTES del srcdoc replacement, y con count=1 para afectar SOLO el primer match.
    js_inline = (
        '<script id="cyr-common-js">\n' + COMMON_JS + '\n</script>\n'
        '<script id="cyr-academia-js">\n' + ACADEMIA_JS + '\n</script>\n'
    )
    if sesion_js:
        js_inline += '<script id="cyr-sesion-js">\n' + sesion_js + '\n</script>\n'
    html = html.replace('</body>', js_inline + '</body>', 1)

    # 10. AHORA reemplazar iframe externo del reto por iframe srcdoc con el reto embebido.
    # Esto va al final para que las inyecciones de CSS y JS anteriores NO se mezclen con
    # los </head>/</body> que vengan dentro del HTML del reto.
    iframe_pattern = re.compile(
        r'<iframe\s+class="iframe-reto"\s+src="\.\./retos/([^"]+)"([^>]*)></iframe>',
        re.DOTALL,
    )
    m = iframe_pattern.search(html)
    if m:
        reto_filename = m.group(1)
        extra_attrs = m.group(2)
        reto_path = ACAD / 'retos' / reto_filename
        if reto_path.exists():
            reto_html = reto_path.read_text(encoding='utf-8')
            srcdoc = escape_srcdoc(reto_html)
            nuevo_iframe = (
                f'<iframe class="iframe-reto"{extra_attrs} '
                f'srcdoc="{srcdoc}"></iframe>'
            )
            html = html[:m.start()] + nuevo_iframe + html[m.end():]
        else:
            print(f"  ⚠️ Reto no encontrado: {reto_path}", file=sys.stderr)
    # Si no hay iframe (S1, S2), no pasa nada — siguen igual.

    return html


def main():
    print(f"Generando {len(SESIONES)} HTMLs standalone en {STANDALONE}/\n")
    resultados = []
    for sid in SESIONES:
        try:
            html = build_standalone(sid)
            out = STANDALONE / f'{sid}.html'
            out.write_text(html, encoding='utf-8')
            kb = len(html) / 1024
            resultados.append((sid, kb, True, ''))
            print(f"  ✓ {sid}.html ({kb:.1f} KB)")
        except Exception as e:
            resultados.append((sid, 0, False, str(e)))
            print(f"  ✗ {sid}.html — ERROR: {e}")

    print(f"\n{sum(1 for r in resultados if r[2])} / {len(SESIONES)} OK")
    total_kb = sum(r[1] for r in resultados)
    print(f"Tamaño total: {total_kb:.1f} KB")


if __name__ == '__main__':
    main()

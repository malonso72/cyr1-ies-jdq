# -*- coding: utf-8 -*-
"""Plantilla de las páginas de reto de T2 · micro:bit (CyR 1º ESO).

Reutiliza el CSS, el JS de la pregunta y las listas (pasos / secuencia / claves) del
taller de T1, para que un reto de micro:bit se lea igual que una sesión de Scratch.
Sólo cambian los bloques (los dibuja `makecodesvg.py`), la barra de navegación, el
botón de abrir el editor y la entrega (aquí es un archivo .hex).
"""
import os
import sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
sys.path.insert(0, os.path.join(AQUI, '..', 'generadores-t1'))

from makecodesvg import script_svg, scripts_svg, matriz_svg      # noqa: E402

from plantilla import (CSS as CSS_T1, JS, e, pasos, secuencia, claves,   # noqa: E402,F401
                       pregunta, pista, ojo, logros, tabla, _boton)

RAIZ = '../../../'          # desde trimestres/t2-microbit/retos/
EDITOR = 'https://makecode.microbit.org/?lang=es'

CSS = CSS_T1 + '''
  .matriz{display:block;max-width:100%;height:auto;}
  .placa{display:flex;gap:18px;align-items:center;flex-wrap:wrap;margin:10px 0 16px;}
  .placa figure{margin:0;}
  .placa figcaption{font-size:.85rem;color:#555D6B;margin-top:6px;text-align:center;}
  .placa .lado{flex:1 1 260px;}
  .cat{display:inline-block;padding:1px 8px;border-radius:5px;color:#fff;font-weight:600;
    font-size:.86rem;font-family:Consolas,Monaco,Menlo,'Liberation Mono',monospace;white-space:nowrap;}
  .cat-basico{background:#1E90FF}.cat-entrada{background:#D400D4}.cat-led{background:#5C2D91}
  .cat-radio{background:#E3008C}.cat-bucles{background:#00AA00}.cat-logica{background:#00A4A6}
  .cat-variables{background:#DC143C}.cat-matematica{background:#9400D3}.cat-juego{background:#007A4B}
  .cat-musica{background:#E63022}
  .bl{font-family:Consolas,Monaco,Menlo,'Liberation Mono',monospace;font-weight:600;
    background:#EEF3F9;padding:0 5px;border-radius:4px;white-space:nowrap;}
  .nivel{display:inline-block;font-size:.8rem;font-weight:700;letter-spacing:.04em;
    text-transform:uppercase;padding:2px 10px;border-radius:12px;margin-left:8px;vertical-align:middle;}
  .nivel-t{background:#1B4F8A;color:#fff;}
  .nivel-a{background:#D4700A;color:#fff;}
  .nivel-m{background:#666;color:#fff;}
  .amplia{border:1px dashed #D4700A;background:#FFF9F2;border-radius:10px;padding:12px 16px;margin:18px 0;}
  .amplia h3{margin:0 0 6px;font-size:1rem;color:#A8560A;}
  .amplia ul{margin:0;padding-left:20px;}
'''


# ------------------------------------------------------------------ piezas
def caja(bloques, alt, pie=None, ancho=None, fondo=None, escala=1.0):
    """Caja gris con un script de MakeCode dentro."""
    est = []
    if ancho:
        est.append('max-width:%dpx' % ancho)
    if fondo:
        est.append('background:%s' % fondo)
    st = (' style="%s"' % ';'.join(est)) if est else ''
    pie_html = ('\n  <p class="pie">%s</p>' % pie) if pie else ''
    return ('<div class="caja-bloques"%s>\n  %s%s\n</div>'
            % (st, script_svg(bloques, alt, escala=escala), pie_html))


def caja_varios(grupos, alt, pie=None, ancho=None):
    """Varios scripts sueltos (varios eventos) en la misma caja, como en el editor."""
    st = (' style="max-width:%dpx"' % ancho) if ancho else ''
    pie_html = ('\n  <p class="pie">%s</p>' % pie) if pie else ''
    return ('<div class="caja-bloques"%s>\n  %s%s\n</div>'
            % (st, scripts_svg(grupos, alt), pie_html))


def dos_cajas(a, b):
    return ('<div class="dos-col">\n<div><p class="col-tit">%s</p>%s</div>\n'
            '<div><p class="col-tit">%s</p>%s</div>\n</div>'
            % (a[0], caja(a[1], a[2], a[3] if len(a) > 3 else None),
               b[0], caja(b[1], b[2], b[3] if len(b) > 3 else None)))


def placa(patron, alt, pie=None, coords=False, marcar=None, lado=None):
    """La matriz de la placa, con texto al lado si se quiere."""
    fig = ('<figure>%s%s</figure>'
           % (matriz_svg(patron, alt, coords=coords, marcar=marcar),
              ('<figcaption>%s</figcaption>' % pie) if pie else ''))
    if lado:
        return '<div class="placa">%s<div class="lado">%s</div></div>' % (fig, lado)
    return '<div class="placa">%s</div>' % fig


def cat(nombre, texto=None):
    """Etiqueta con el color de la categoría del editor: «Básico», «Entrada»…"""
    return '<span class="cat cat-%s">%s</span>' % (nombre, texto or nombre.capitalize())


def bl(texto):
    """Nombre de un bloque escrito en el texto, tal cual se lee en el editor."""
    return '<span class="bl">%s</span>' % texto


def amplia(items):
    """Enlaces a las ampliaciones que salen de este reto."""
    li = ''.join('\n  <li>%s</li>' % t for t in items)
    return ('<div class="amplia">\n<h3>🚀 Si vas sobrado</h3>\n'
            '<p style="margin:0 0 6px">Estas ampliaciones salen de este reto. No son obligatorias: '
            'son para cuando lo tienes hecho y comprobado en la placa.</p>'
            '<ul>%s\n</ul>\n</div>' % li)


# ------------------------------------------------------------------ página
_PAG = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#1E90FF">
<link rel="icon" type="image/svg+xml" href="{R}favicon.svg">
<title>{PRE} · {TIT} · micro:bit · CyR 1º ESO</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="https://cyr1-ies-jdq.malonso72.workers.dev/trimestres/t2-microbit/retos/{ARCH}.html">
<meta property="og:title" content="{PRE} · {TIT} · CyR 1º ESO">
<meta property="og:description" content="{DESC}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600;700&family=Barlow+Condensed:wght@600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{R}assets/css/common.css">
<link rel="stylesheet" href="{R}assets/css/hub.css">
<link rel="stylesheet" href="{R}assets/css/unidad.css">
<style>{CSS}</style>
</head>
<body>
<a href="#main-content" class="skip-link">Saltar al contenido principal</a>

<header class="curso-hd">
<a class="curso-lg" href="{R}index.html">CyR 1º ESO</a>
<span class="curso-sb">T2 · micro:bit</span>
</header>
<nav class="curso-navcross" role="navigation" aria-label="Navegación del trimestre">
<a href="{R}index.html"><span>🏠</span><span class="nc-lbl">Índice</span></a>
<span class="nc-sep">·</span>
<a href="../index.html"><span>📋</span><span class="nc-lbl">Hub T2</span></a>
<span class="nc-sep">·</span>
<a href="index.html"><span>🎯</span><span class="nc-lbl">Retos</span></a>
<span class="nc-sep">·</span>
<span class="nc-current"><span>✏️</span><span class="nc-lbl">{CORTO}</span></span>
</nav>

<div id="main-content">
<section class="unidad-titulo-hero">
  <div class="num">{PRE}</div>
  <h1>{TIT}</h1>
  <div class="duracion">T2 · micro:bit · 1º ESO{NIVEL}</div>
</section>

<main class="ej-main">

<p><strong>Lo que vas a conseguir:</strong> {CONSIGUE}</p>

{ABRIR}

{SECCIONES}

<div class="entrega">
<h3>📤 Qué tienes que entregar</h3>
{ENTREGA}
</div>

<h2>Navegación</h2>
<div class="bg">{NAV}</div>

</main>
</div>

<p class="foot">
IES Jiménez de Quesada · Santa Fe (Granada)<br>
CyR 1º ESO · Curso 2026-27 · Manuel Alonso Herrera
<br><a href="https://tecnologia-ies-jdq.malonso72.workers.dev/">🏛️ Otras asignaturas del departamento</a>
</p>

<script src="{R}assets/js/common.js"></script>
<script src="{R}assets/js/header.js"></script>
<script>{JS}</script>
<script data-goatcounter="https://malonso72.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>
'''

_ABRIR = ('<a class="abrir-scratch" href="' + EDITOR + '" target="_blank" rel="noopener">'
          '🔌 Abrir MakeCode en otra pestaña</a>\n'
          '<p class="consejo">Consejo: deja MakeCode a un lado de la pantalla y esta página al '
          'otro. El simulador de la izquierda del editor te enseña lo que hará la placa antes de '
          'copiarle el programa.</p>')

_ENTREGA_STD = '''<p style="margin:0 0 10px;"><strong>Antes de nada:</strong> MakeCode guarda el proyecto en este navegador, pero el ordenador es de todos: lo que vale es el <strong>archivo</strong>.</p>
<ol>
  <li>Abajo, en la casilla del nombre del proyecto (junto al botón <strong>Descargar</strong>), escribe <strong>{NOMBRE}_TuNombre</strong>.</li>
  <li>Pulsa <strong>Descargar</strong>. Aparece en tu carpeta <strong>Descargas</strong> un archivo <code>microbit-{NOMBRE}_TuNombre.hex</code>. Si el navegador te ofrece conectar la placa, puedes decir que no: el archivo ya está.</li>
  <li>Para probarlo en la placa: conéctala por USB. Aparece una unidad llamada <strong>MICROBIT</strong>; arrastra el <code>.hex</code> dentro. La luz amarilla de detrás parpadea unos segundos y el programa arranca solo.</li>
  <li>Sube el <code>.hex</code> a la tarea de <strong>Moodle</strong> de este reto.</li>
</ol>'''

_NIVEL = {'t': ' <span class="nivel nivel-t">troncal</span>',
          'a': ' <span class="nivel nivel-a">ampliación</span>',
          'm': ' <span class="nivel nivel-m">requiere servo</span>'}


def pagina(arch, pre, titulo, desc, consigue, secciones, nivel='t', entrega=None,
           abrir=True, anterior=None, siguiente=None, nav_extra='', nombre_hex=None):
    """Renderiza la página completa de un reto.

    arch: nombre del archivo sin .html (r01, a03, m01). pre: «Reto 4», «Ampliación 2».
    secciones: lista de (título, HTML); las de título None no llevan número.
    anterior / siguiente: (archivo, etiqueta) o None.
    """
    cuerpo = []
    n = 0
    for tit, cont in secciones:
        if tit is None:
            cuerpo.append(cont)
        else:
            n += 1
            cuerpo.append('<h2><span class="h2n">%d</span>%s</h2>\n%s' % (n, tit, cont))

    nav = []
    if anterior:
        nav.append(_boton(anterior[0] + '.html', '⬅️', 'Anterior', anterior[1]))
    nav.append(_boton('index.html', '🎯', 'Todos los retos', 'Índice del trimestre'))
    if siguiente:
        nav.append(_boton(siguiente[0] + '.html', '➡️', 'Siguiente', siguiente[1]))
    if nav_extra:
        nav.append(nav_extra)

    corto = pre.replace('Reto ', 'R').replace('Ampliación ', 'A').replace('Sin material ', 'M')
    nombre = nombre_hex or pre.replace(' ', '')
    return (_PAG
            .replace('{CSS}', CSS)
            .replace('{JS}', JS)
            .replace('{R}', RAIZ)
            .replace('{ARCH}', arch)
            .replace('{PRE}', pre)
            .replace('{CORTO}', corto)
            .replace('{TIT}', titulo)
            .replace('{DESC}', desc)
            .replace('{NIVEL}', _NIVEL.get(nivel, ''))
            .replace('{CONSIGUE}', consigue)
            .replace('{ABRIR}', _ABRIR if abrir else '')
            .replace('{SECCIONES}', '\n\n'.join(cuerpo))
            .replace('{ENTREGA}', (entrega or _ENTREGA_STD).replace('{NOMBRE}', nombre))
            .replace('{NAV}', ''.join(nav)))

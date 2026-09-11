# -*- coding: utf-8 -*-
"""Plantilla de las páginas de sesión de T1 · Scratch (CyR 1º ESO).

Una sesión se describe con un diccionario y se renderiza siempre con la misma
estructura, para que la sesión 20 tenga el mismo criterio que la sesión 1.
"""
import html as _html
from scratchsvg import script_svg

RAIZ = '../../../'          # desde trimestres/t1-scratch/sesiones/
CUAD = '../materiales/cuadernillo-scratch-parte-1.pdf'
EDITOR = 'https://scratch.mit.edu/projects/editor/'


def e(t):
    return _html.escape(t, quote=True)


# ------------------------------------------------------------------ piezas
def caja(bloques, alt, pie=None, ancho=None, fondo=None, escala=1.0):
    """Caja gris con un script de Scratch dentro."""
    est = []
    if ancho:
        est.append('max-width:%dpx' % ancho)
    if fondo:
        est.append('background:%s' % fondo)
    st = (' style="%s"' % ';'.join(est)) if est else ''
    pie_html = ('\n  <p class="pie">%s</p>' % pie) if pie else ''
    return ('<div class="caja-bloques"%s>\n  %s%s\n</div>'
            % (st, script_svg(bloques, alt, escala=escala), pie_html))


def dos_cajas(a, b):
    """Dos scripts uno al lado del otro (objetos distintos)."""
    return ('<div class="dos-col">\n<div><p class="col-tit">%s</p>%s</div>\n'
            '<div><p class="col-tit">%s</p>%s</div>\n</div>'
            % (a[0], caja(a[1], a[2], a[3] if len(a) > 3 else None),
               b[0], caja(b[1], b[2], b[3] if len(b) > 3 else None)))


def pasos(items):
    li = ''.join('\n  <li><span class="n">%d</span><span>%s</span></li>' % (i + 1, t)
                 for i, t in enumerate(items))
    return '<ol class="paso-lista">%s\n</ol>' % li


def pregunta(pid, texto, opciones, correcta):
    """opciones: lista de (clave, texto del botón, explicación)."""
    bot = ''.join(
        '\n    <button data-op="%s" data-ex="%s">%s</button>' % (k, e(x), t)
        for k, t, x in opciones)
    return ('<div class="comprueba" data-ok="%s">\n  <p class="preg">%s</p>\n'
            '  <div class="ops">%s\n  </div>\n  <div class="fb" id="fb%s"></div>\n</div>'
            % (correcta, texto, bot, pid))


def pista(resumen, cuerpo):
    return ('<details class="pista">\n  <summary>%s</summary>\n'
            '  <div class="cuerpo">%s</div>\n</details>' % (resumen, cuerpo))


def ojo(titulo, cuerpo):
    return ('<div class="aviso-ojo">\n  <h3>⚠️ %s</h3>\n%s\n</div>' % (titulo, cuerpo))


def logros(items):
    li = ''.join('\n  <li>%s</li>' % t for t in items)
    return '<ul class="logro">%s\n</ul>' % li


def tabla(cabeceras, filas):
    th = ''.join('<th scope="col">%s</th>' % c for c in cabeceras)
    tr = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in f) for f in filas)
    return ('<div class="tabla-env"><table class="tabla-cyr"><thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>' % (th, tr))


# ------------------------------------------------------------------ CSS
CSS = '''
  .ej-main{max-width:900px;margin:0 auto;padding:16px 16px 50px;font-size:1.02rem;line-height:1.6;}
  .ej-main p{margin:0 0 12px;}
  .ej-main h2{font-family:'Barlow Condensed',sans-serif;font-size:1.35rem;color:#1B4F8A;
    margin:26px 0 10px;padding-bottom:5px;border-bottom:2px solid #E3E8EF;}
  .ej-main h2 .h2n{display:inline-flex;align-items:center;justify-content:center;
    width:25px;height:25px;border-radius:50%;background:#1B4F8A;color:#fff;font-size:.85rem;
    margin-right:9px;vertical-align:2px;}
  .paso-lista{list-style:none;margin:0 0 12px;padding:0;}
  .paso-lista li{display:grid;grid-template-columns:30px 1fr;gap:10px;align-items:start;
    padding:9px 0;border-bottom:1px dashed #D8DDE5;}
  .paso-lista li:last-child{border-bottom:none;}
  .paso-lista .n{width:26px;height:26px;border-radius:50%;background:#1B4F8A;color:#fff;
    font-weight:700;font-size:.82rem;display:flex;align-items:center;justify-content:center;}
  .bloques{max-width:100%;height:auto;display:block;}
  .caja-bloques{background:#F4F6F9;border:1px solid #D8DDE5;border-radius:10px;
    padding:12px;margin:10px 0 16px;overflow-x:auto;}
  .caja-bloques .pie{font-size:.82rem;color:#555D6B;margin:8px 2px 0;}
  .dos-col{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:10px 0 16px;}
  .dos-col .col-tit{font-weight:700;color:#1B4F8A;font-size:.92rem;margin:0 0 4px;}
  @media(max-width:700px){.dos-col{grid-template-columns:1fr;}}
  .aviso-ojo{border-left:5px solid #D4700A;background:#FFF6EC;border-radius:0 8px 8px 0;
    padding:12px 16px;margin:16px 0;}
  .aviso-ojo h3{margin:0 0 6px;font-size:1rem;color:#A8560A;}
  .aviso-ojo .caja-bloques{background:#fff;}
  .entrega{border:2px solid #1A6B3A;background:#F0F9F3;border-radius:10px;padding:14px 18px;margin:22px 0;}
  .entrega h3{margin:0 0 8px;font-size:1.05rem;color:#1A6B3A;}
  .entrega ol{margin:0;padding-left:20px;}
  .entrega li{margin-bottom:5px;}
  .logro{list-style:none;margin:0;padding:0;}
  .logro li{padding:7px 0 7px 30px;position:relative;border-bottom:1px dashed #D8DDE5;}
  .logro li:last-child{border-bottom:none;}
  .logro li::before{content:"\\2610";position:absolute;left:4px;top:6px;font-size:1.15rem;color:#1B4F8A;}
  details.pista{border:1px solid #D8DDE5;border-radius:8px;padding:0;margin:14px 0;background:#fff;}
  details.pista>summary{cursor:pointer;padding:11px 14px;font-weight:600;color:#1B4F8A;
    list-style:none;user-select:none;}
  details.pista>summary::-webkit-details-marker{display:none;}
  details.pista>summary::before{content:"\\25B8 ";}
  details.pista[open]>summary::before{content:"\\25BE ";}
  details.pista .cuerpo{padding:0 14px 14px;}
  .comprueba{background:#FFFBE8;border:1px solid #E8D27A;border-radius:10px;padding:14px 16px;margin:18px 0;}
  .comprueba .preg{font-weight:600;color:#6B5A12;margin:0 0 10px;}
  .comprueba .ops{display:flex;flex-direction:column;gap:7px;}
  .comprueba .ops button{text-align:left;padding:10px 12px;border:1px solid #D8C470;
    background:#FFFDF4;border-radius:6px;cursor:pointer;font:inherit;font-size:.95rem;color:#3A3527;}
  .comprueba .ops button:hover{background:#FDF3CF;}
  .comprueba .ops button.ok{background:#EAFAF0;border-color:#1A6B3A;color:#155C30;}
  .comprueba .ops button.mal{background:#FDECEB;border-color:#C0321E;color:#8E2418;}
  .comprueba .ops button:disabled{cursor:default;}
  .comprueba .fb{display:none;margin-top:11px;padding:11px 13px;border-radius:6px;
    font-size:.94rem;line-height:1.55;background:#EEF6FF;border:1px solid #B7D4EF;color:#123A66;}
  .comprueba .fb.ver{display:block;}
  .abrir-scratch{display:inline-flex;align-items:center;gap:8px;background:#1B4F8A;color:#fff;
    text-decoration:none;padding:10px 18px;border-radius:8px;font-weight:600;margin:4px 0 8px;}
  .abrir-scratch:hover{background:#123A66;}
  .consejo{font-size:.9rem;color:#555D6B;margin-top:2px;}
  .tabla-env{overflow-x:auto;margin:10px 0 16px;}
  .tabla-cyr{border-collapse:collapse;width:100%;font-size:.94rem;}
  .tabla-cyr th,.tabla-cyr td{border:1px solid #D8DDE5;padding:7px 10px;text-align:left;vertical-align:top;}
  .tabla-cyr th{background:#EEF3F9;color:#1B4F8A;}
  .tabla-cyr tbody tr:nth-child(even){background:#FAFBFD;}
  @media(max-width:640px){.ej-main{font-size:1rem;}}
'''

JS = '''
(function(){
  "use strict";
  document.querySelectorAll('.comprueba').forEach(function(caja){
    var correcta = caja.getAttribute('data-ok');
    var fb = caja.querySelector('.fb');
    var bots = caja.querySelectorAll('.ops button');
    bots.forEach(function(b){
      b.addEventListener('click', function(){
        var bien = (b.getAttribute('data-op') === correcta);
        fb.className = 'fb ver';
        fb.textContent = (bien ? '\\u2714 ' : '\\u2718 ') + b.getAttribute('data-ex');
        bots.forEach(function(x){
          x.disabled = true;
          if (x.getAttribute('data-op') === correcta) x.classList.add('ok');
          else if (x === b) x.classList.add('mal');
        });
      });
    });
  });
})();
'''

# ------------------------------------------------------------------ página
_PAG = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#FF8C1A">
<link rel="icon" type="image/svg+xml" href="{R}favicon.svg">
<title>S{NN} · {TIT} · Scratch · CyR 1º ESO</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="https://cyr1-ies-jdq.malonso72.workers.dev/trimestres/t1-scratch/sesiones/s{NN}.html">
<meta property="og:title" content="S{NN} · {TIT} · CyR 1º ESO">
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
<span class="curso-sb">T1 · Scratch</span>
</header>
<nav class="curso-navcross" role="navigation" aria-label="Navegación del trimestre">
<a href="{R}index.html"><span>🏠</span><span class="nc-lbl">Índice</span></a>
<span class="nc-sep">·</span>
<a href="../index.html"><span>📋</span><span class="nc-lbl">Hub T1</span></a>
<span class="nc-sep">·</span>
<a href="index.html"><span>🗓️</span><span class="nc-lbl">Sesiones</span></a>
<span class="nc-sep">·</span>
<span class="nc-current"><span>✏️</span><span class="nc-lbl">S{NN}</span></span>
<span class="nc-sep">·</span>
<a href="../juegos/index.html"><span>🎮</span><span class="nc-lbl">Juegos</span></a>
</nav>

<div id="main-content">
<section class="unidad-titulo-hero">
  <div class="num">Sesión {NN}</div>
  <h1>{TIT}</h1>
  <div class="duracion">T1 · Scratch · 1º ESO</div>
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
          '🐱 Abrir Scratch en otra pestaña</a>\n'
          '<p class="consejo">Consejo: deja Scratch a un lado de la pantalla y esta página '
          'al otro. Así no tienes que ir y venir.</p>')

_ENTREGA_STD = '''<p style="margin:0 0 10px;"><strong>Antes de nada:</strong> como no usamos cuenta de Scratch, tu proyecto sólo existe en esta pestaña. Si la cierras sin descargarlo, <strong>se pierde</strong>.</p>
<ol>
  <li><strong>Archivo → Guardar en tu ordenador.</strong> Se descarga un archivo <code>.sb3</code> que aparece en tu carpeta <strong>Descargas</strong>.</li>
  <li>Cámbiale el nombre a <strong>Sesion{NN}_TuNombre.sb3</strong>.</li>
  <li>Súbelo a la tarea de <strong>Moodle</strong> de la sesión {NN}.</li>
</ol>'''


def _boton(href, icono, clave, nota, clase=''):
    return ('<a href="%s" class="bc%s"><span class="bi">%s</span>'
            '<span class="bk">%s</span><span class="bn">%s</span></a>'
            % (href, clase, icono, clave, nota))


def pagina(num, titulo, desc, consigue, secciones, entrega=None,
           cuadernillo=None, abrir=True, nav_extra=''):
    """Renderiza la página completa de una sesión.

    `secciones` es una lista de (título de sección, HTML). Se numeran solas.
    `cuadernillo` es el número de página del PDF, o None.
    """
    nn = '%02d' % num
    cuerpo = []
    n = 0
    for tit, cont in secciones:
        if tit is None:
            # Una sección sin título no lleva número y no gasta ninguno.
            cuerpo.append(cont)
        else:
            n += 1
            cuerpo.append('<h2><span class="h2n">%d</span>%s</h2>\n%s' % (n, tit, cont))

    nav = []
    if num > 1:
        nav.append(_boton('s%02d.html' % (num - 1), '⬅️', 'Sesión anterior', 'S%02d' % (num - 1)))
    nav.append(_boton('index.html', '🗓️', 'Todas las sesiones', 'Índice del trimestre'))
    if num < 20:
        nav.append(_boton('s%02d.html' % (num + 1), '➡️', 'Sesión siguiente', 'S%02d' % (num + 1)))
    if cuadernillo:
        nav.append(_boton('%s#page=%d' % (CUAD, cuadernillo), '📒', 'Cuadernillo',
                          'Página %d, para consultar' % cuadernillo))
    if nav_extra:
        nav.append(nav_extra)

    return (_PAG
            .replace('{CSS}', CSS)
            .replace('{JS}', JS)
            .replace('{R}', RAIZ)
            .replace('{NN}', nn)
            .replace('{TIT}', titulo)
            .replace('{DESC}', desc)
            .replace('{CONSIGUE}', consigue)
            .replace('{ABRIR}', _ABRIR if abrir else '')
            .replace('{SECCIONES}', '\n\n'.join(cuerpo))
            .replace('{ENTREGA}', (entrega or _ENTREGA_STD).replace('{NN}', nn))
            .replace('{NAV}', ''.join(nav)))


# ------------------------------------------------------------------ página de juego
# Las tres bases del proyecto final viven en trimestres/t1-scratch/juegos/ y usan el
# mismo esqueleto que una sesión: misma profundidad de rutas, mismo CSS y mismo JS de
# la pregunta. Sólo cambian el hero, la barra de navegación y la entrega.
RAIZ_J = '../../../'        # desde trimestres/t1-scratch/juegos/

_NAV_SES = (
    '<a href="index.html"><span>\U0001F5D3️</span><span class="nc-lbl">Sesiones</span></a>\n'
    '<span class="nc-sep">·</span>\n'
    '<span class="nc-current"><span>✏️</span><span class="nc-lbl">S{NN}</span></span>\n'
    '<span class="nc-sep">·</span>\n'
    '<a href="../juegos/index.html"><span>\U0001F3AE</span>'
    '<span class="nc-lbl">Juegos</span></a>')

_NAV_JUE = (
    '<a href="../sesiones/index.html"><span>\U0001F5D3️</span>'
    '<span class="nc-lbl">Sesiones</span></a>\n'
    '<span class="nc-sep">·</span>\n'
    '<a href="index.html"><span>\U0001F3AE</span><span class="nc-lbl">Juegos</span></a>\n'
    '<span class="nc-sep">·</span>\n'
    '<span class="nc-current"><span>\U0001F680</span><span class="nc-lbl">{TIT}</span></span>')

_PAG_JUEGO = (_PAG
    .replace('<title>S{NN} · {TIT} · Scratch · CyR 1º ESO</title>',
             '<title>{TIT} · Proyecto final · Scratch · CyR 1º ESO</title>')
    .replace('https://cyr1-ies-jdq.malonso72.workers.dev/trimestres/t1-scratch/sesiones/s{NN}.html',
             'https://cyr1-ies-jdq.malonso72.workers.dev/trimestres/t1-scratch/juegos/{SLUG}.html')
    .replace('<meta property="og:title" content="S{NN} · {TIT} · CyR 1º ESO">',
             '<meta property="og:title" content="{TIT} · Proyecto final · CyR 1º ESO">')
    .replace(_NAV_SES, _NAV_JUE)
    .replace('<div class="num">Sesión {NN}</div>',
             '<div class="num">Proyecto final · opción {OPC}</div>'))

_ENTREGA_JUEGO = (
    '<p style="margin:0 0 10px;"><strong>Antes de nada:</strong> como no usamos cuenta de '
    'Scratch, tu proyecto sólo existe en esta pestaña. Si la cierras sin descargarlo, '
    '<strong>se pierde</strong>.</p>\n<ol>\n'
    '  <li><strong>Archivo → Guardar en tu ordenador.</strong> Se descarga un archivo '
    '<code>.sb3</code> que aparece en tu carpeta <strong>Descargas</strong>.</li>\n'
    '  <li>Cámbiale el nombre a <strong>ProyectoFinal_TuNombre.sb3</strong>.</li>\n'
    '  <li>Súbelo a la tarea de <strong>Moodle</strong> que toque: la primera versión jugable '
    'en la sesión 18, la mejorada en la 19 y la definitiva en la 20.</li>\n</ol>')


def pagina_juego(slug, titulo, opcion, desc, consigue, secciones, guia=None, guia_nota=None):
    """Renderiza una de las bases del proyecto final (carpeta juegos/)."""
    cuerpo = []
    n = 0
    for tit, cont in secciones:
        if tit is None:
            cuerpo.append(cont)
        else:
            n += 1
            cuerpo.append('<h2><span class="h2n">%d</span>%s</h2>\n%s' % (n, tit, cont))

    nav = [_boton('index.html', '\U0001F3AE', 'Las tres opciones', 'Volver a elegir'),
           _boton('../sesiones/s17.html', '\U0001F4DD', 'S17 · Tu versión',
                  'La ficha de diseño'),
           _boton('../sesiones/s18.html', '\U0001F9F0', 'S18 · Kit de piezas',
                  'Las ocho piezas para montarlo')]
    if guia:
        nav.append(_boton('../materiales/guias-juegos/' + guia, '\U0001F4D5',
                          'Guía antigua en PDF',
                          guia_nota or 'Consulta. Está hecha con Scratch 2'))

    return (_PAG_JUEGO
            .replace('{CSS}', CSS)
            .replace('{JS}', JS)
            .replace('{R}', RAIZ_J)
            .replace('{SLUG}', slug)
            .replace('{OPC}', opcion)
            .replace('{TIT}', titulo)
            .replace('{DESC}', desc)
            .replace('{CONSIGUE}', consigue)
            .replace('{ABRIR}', _ABRIR)
            .replace('{SECCIONES}', '\n\n'.join(cuerpo))
            .replace('{ENTREGA}', _ENTREGA_JUEGO)
            .replace('{NAV}', ''.join(nav)))

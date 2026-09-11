# -*- coding: utf-8 -*-
"""Higiene de trimestres/t1-scratch/presentacion.html sin cambiar cómo se ve.

Es la única página de T1 que quedaba con dos h1, sin <main> y sin metadatos.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import T1
P = os.path.join(T1, 'presentacion.html')
h = open(P, encoding='utf-8').read()
orig = h

# 1 · metadatos que faltaban
h = h.replace(
    '<title>Scratch · Presentación inicial</title>',
    '<title>Presentación inicial · T1 Scratch · CyR 1º ESO</title>\n'
    '<meta name="theme-color" content="#201124">\n'
    '<link rel="icon" type="image/svg+xml" href="../../favicon.svg">\n'
    '<meta name="description" content="Presentación de apertura del trimestre de Scratch para '
    'proyectar en clase: qué se va a hacer en las 20 sesiones. CyR 1º ESO · IES Jiménez de Quesada.">\n'
    '<link rel="canonical" href="https://cyr1-ies-jdq.malonso72.workers.dev/trimestres/t1-scratch/presentacion.html">\n'
    '<meta property="og:title" content="Presentación inicial · T1 Scratch · CyR 1º ESO">\n'
    '<meta property="og:description" content="Apertura del trimestre de Scratch para proyectar en clase.">\n'
    '<meta property="og:type" content="website">\n'
    '<meta property="og:locale" content="es_ES">')

# 2 · un solo h1: la última diapositiva pasa a h2 con el mismo aspecto exacto
h = h.replace('h1{font-size:clamp(56px,10vw,140px);line-height:1;margin:.1em 0;text-align:center}',
              'h1,h2.hero{font-size:clamp(56px,10vw,140px);line-height:1;margin:.1em 0;'
              'text-align:center}')
h = h.replace('<h1>¿Preparados?</h1>', '<h2 class="hero">¿Preparados?</h2>')

# 3 · <main> alrededor de las diapositivas
h = h.replace('</style></head><body>\n<div class="slide active">',
              '</style></head><body>\n<main>\n<div class="slide active">')
h = h.replace('<div class="counter" id="c">', '</main>\n<div class="counter" id="c">')

# 4 · los botones de navegación, con nombre accesible
h = h.replace('<button onclick="go(-1)">‹</button>',
              '<button type="button" aria-label="Diapositiva anterior" onclick="go(-1)">‹</button>')
h = h.replace('<button onclick="go(1)">›</button>',
              '<button type="button" aria-label="Diapositiva siguiente" onclick="go(1)">›</button>')

assert h != orig
open(P, 'w', encoding='utf-8').write(h)
print('presentacion.html corregida (%d bytes)' % len(h))

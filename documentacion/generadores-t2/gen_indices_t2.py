# -*- coding: utf-8 -*-
"""Hub de T2 (tres tarjetas, como T1) y el índice de los retos."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun_t2 import escribir, escribir_t2

TRONCAL = [
    ('r01', 'Hola, micro:bit', 'al iniciar, para siempre, mostrar cadena e ícono'),
    ('r02', 'El corazón que late', 'pausa y animación; dibujar con mostrar LEDs'),
    ('r03', 'Los botones: un evento para cada uno', 'al presionarse el botón A / B / A+B'),
    ('r04', 'Cada LED tiene su dirección', 'coordenadas x e y; graficar y ocultar'),
    ('r05', 'La luz que se enciende sola', 'sensor de luz y si… si no'),
    ('r06', 'El contador de turnos', 'variables: fijar y cambiar por'),
    ('r07', 'El interruptor: un botón, dos estados', 'variable verdadero/falso'),
    ('r08', 'El cronómetro', 'el bucle cuenta, los botones mandan'),
    ('r09', 'El bucle «para»: una fila que se enciende', 'para índice de 0 a 4'),
    ('r10', 'La serpiente: un bucle dentro de otro', 'bucles anidados'),
    ('r11', 'El dado: agitar y azar', 'si agitado; escoger al azar'),
    ('r12', 'Piedra, papel o tijera', 'si… si no, si… si no'),
    ('r13', 'Radio: dos placas que se hablan', 'grupo, enviar número, al recibir'),
    ('r14', 'La brújula', 'dirección de la brújula, tramos con «o», calibración'),
    ('r15', 'Esquiva enemigos: tu primer juego', 'sprites, colisión, puntuación'),
]

AMPLIACIONES = [
    ('Pantalla', 'los retos 4 y 9', [('a01', 'Dibujar el «1» LED a LED'), ('a05', 'La fila al revés: el bucle «mientras»')]),
    ('Sensores', 'el reto 5', [('a02', 'El termostato'), ('a03', 'Brillo al revés'),
                         ('a04', 'Termómetro de barras'), ('a06', 'El parking: contar sombras'),
                         ('a07', 'Frío o caliente')]),
    ('Sonido (V2)', 'el reto 5', [('a08', 'El sonómetro de la clase'), ('a09', 'El theremin: música con la mano')]),
    ('Juego', 'el reto 15', [('a10', 'Naves: dispara con A+B'), ('a11', 'Dos enemigos a la vez')]),
    ('Radio', 'el reto 13', [('a12', 'Dos jugadores por radio')]),
]

SIN_MATERIAL = [('m01', 'Control de un servomotor'), ('m02', 'La barrera de parking'),
                ('m03', 'La barrera automática con sensor de luz')]

HEAD = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#1E90FF">
<link rel="icon" type="image/svg+xml" href="{R}favicon.svg">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="https://cyr1-ies-jdq.malonso72.workers.dev/trimestres/t2-microbit/{CANON}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:image" content="https://cyr1-ies-jdq.malonso72.workers.dev/img/fachadaiesjdq.jpg">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="CyR 1º ESO — IES Jiménez de Quesada">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600;700&family=Barlow+Condensed:wght@600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{R}assets/css/common.css">
<link rel="stylesheet" href="{R}assets/css/hub.css">
<style>
  details.criterios .aprender-grid{margin:0;padding:0;max-width:none}
  .bc .bn small{display:block;color:#6B7280;margin-top:2px}
  .nota-grupo{color:#555D6B;font-size:.9rem;margin:-6px 0 10px}
  .grupo-tit{margin:18px 0 8px;font-size:.98rem;color:#1B4F8A}
</style>
</head>
<body>
<a href="#main-content" class="skip-link">Saltar al contenido principal</a>

<header class="curso-hd">
  <span class="curso-sb">T2 · micro:bit</span>
</header>
'''

FOOT = '''
<p class="foot">
  IES Jiménez de Quesada · Santa Fe (Granada)<br>
  CyR 1º ESO · Curso 2026-27 · Manuel Alonso Herrera
  <br><a href="https://tecnologia-ies-jdq.malonso72.workers.dev/">🏛️ Otras asignaturas del departamento</a>
</p>

</div>

</div>

<script src="{R}assets/js/common.js"></script>
<script src="{R}assets/js/header.js"></script>
<script data-goatcounter="https://malonso72.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>
'''

HUB = HEAD + '''
<nav class="curso-navcross" role="navigation" aria-label="Navegación del trimestre">
  <a href="../../index.html"><span>🏠</span><span class="nc-lbl">Índice</span></a>
  <span class="nc-sep">·</span>
  <span class="nc-current"><span>📋</span><span class="nc-lbl">Hub T2</span></span>
  <span class="nc-sep">·</span>
  <a href="retos/index.html"><span>🎯</span><span class="nc-lbl">Retos</span></a>
</nav>

<div id="main-content">

<section class="unidad-titulo-hero">
  <div class="num">Trimestre 2</div>
  <h1>🔌 micro:bit</h1>
  <div class="duracion">⏱️ 15 retos · Computación física: LEDs, botones, sensores, radio y un juego</div>
</section>

<div class="hub-main">

<div class="section-title">📚 Por dónde empezar</div>
<div class="bg bg-large">
  <a href="presentacion.html" class="bc">
    <span class="bi">📺</span>
    <span class="bk">Presentación</span>
    <span class="bn">Qué es la micro:bit, qué lleva dentro y cómo se programa</span>
  </a>
  <a href="https://makecode.microbit.org/?lang=es" target="_blank" rel="noopener" class="bc tipo-tool">
    <span class="bi">🔌</span>
    <span class="bk">Abrir MakeCode</span>
    <span class="bn">El editor oficial, en el navegador, con simulador. Sin instalar nada y sin cuenta</span>
  </a>
  <a href="retos/index.html" class="bc">
    <span class="bi">🎯</span>
    <span class="bk">Los 15 retos</span>
    <span class="bn">Cada uno con su programa dibujado, su pregunta, su reto y su entrega. Y 12 ampliaciones para quien va rápido</span>
  </a>
</div>

<details class="criterios">
  <summary>📋 Enfoque de trabajo</summary>
  <div class="criterios-body">
    <p>Se trabaja <strong>por parejas</strong>, con una micro:bit V2 por pareja y MakeCode abierto al lado en el navegador. Cada reto tiene su página: un programa que hay que <strong>leer y entender antes de montar el tuyo</strong>, una pregunta de comprensión, el reto con sus pasos y la entrega. El programa se prueba primero en el simulador y después en la placa de verdad.</p>
    <p>Los <strong>15 retos troncales</strong> los hace todo el mundo, en orden, porque cada uno introduce algo que el siguiente necesita. Las <strong>ampliaciones</strong> no son obligatorias: son la continuación de un reto para las parejas que lo terminan antes. No hay proyecto final: el trimestre son retos cortos, y lo que se evalúa es lo que se entrega de cada uno.</p>
  </div>
</details>

<details class="criterios">
  <summary>📖 Qué se aprende y con qué se evalúa</summary>
  <div class="criterios-body">
<section class="aprender-grid">
  <div class="aprender-card saber">
    <h3>📖 Saber</h3>
    <ul>
      <li>Qué lleva la placa: matriz de 25 LEDs, botones, sensores de luz, temperatura, movimiento y brújula, micrófono, altavoz y radio</li>
      <li>La diferencia entre <em>al iniciar</em>, <em>para siempre</em> y un <em>evento</em>, y cuándo va cada cosa en cada sitio</li>
      <li>Coordenadas x e y de la matriz, empezando en cero</li>
      <li>Un sensor es un número; una decisión es un <em>si</em>; un bucle repite</li>
      <li>Qué es un sprite y cómo se hace un juego con ellos</li>
    </ul>
  </div>
  <div class="aprender-card hacer">
    <h3>🛠️ Hacer</h3>
    <ul>
      <li>Montar en MakeCode el programa de cada reto y probarlo en el simulador</li>
      <li>Descargar el <code>.hex</code>, copiarlo a la placa y comprobar que funciona sin el ordenador</li>
      <li>Medir un sensor antes de decidir un umbral</li>
      <li>Usar variables para contar, para guardar un estado y para el azar</li>
      <li>Comunicar dos placas por radio, juntando dos parejas</li>
    </ul>
  </div>
  <div class="aprender-card evaluar">
    <h3>✅ Evaluar</h3>
    <ul>
      <li><strong>Funciona en la placa</strong>, no sólo en el simulador</li>
      <li><strong>Hace lo que pide el reto</strong>, incluidos los cambios que se piden en «Tu reto»</li>
      <li><strong>Lo explicas:</strong> sabes decir qué hace cada bloque y por qué está donde está</li>
      <li><strong>Entregado:</strong> el <code>.hex</code> de cada reto está en Moodle con tu nombre</li>
    </ul>
  </div>
</section>
  </div>
</details>
''' + FOOT

INDICE = HEAD + '''
<nav class="curso-navcross" role="navigation" aria-label="Navegación del trimestre">
  <a href="../../../index.html"><span>🏠</span><span class="nc-lbl">Índice</span></a>
  <span class="nc-sep">·</span>
  <a href="../index.html"><span>📋</span><span class="nc-lbl">Hub T2</span></a>
  <span class="nc-sep">·</span>
  <span class="nc-current"><span>🎯</span><span class="nc-lbl">Retos</span></span>
</nav>

<div id="main-content">

<section class="unidad-titulo-hero">
  <div class="num">micro:bit</div>
  <h1>🎯 Los retos</h1>
  <div class="duracion">15 troncales, en orden · 12 ampliaciones para quien va rápido</div>
</section>

<div class="hub-main">

<div class="section-title">🧭 Los 15 retos troncales</div>
<p class="nota-grupo">En este orden: cada uno usa lo que enseña el anterior.</p>
<div class="bg">
{TRONCAL}
</div>

<div class="section-title" id="ampliaciones">🚀 Ampliaciones</div>
<p class="nota-grupo">No son obligatorias. Cada grupo sale de un reto troncal: hazlas cuando ese reto ya funcione en la placa.</p>
{AMPLIACIONES}

<div class="section-title">🔧 Requieren servo (este curso no se hacen)</div>
<p class="nota-grupo">Tres retos que necesitan un servomotor. Se conservan por si algún año hay material.</p>
<div class="bg">
{SIN_MATERIAL}
</div>
''' + FOOT


def tarjeta(arch, icono, clave, nota, sub=None):
    n = nota + ('<small>%s</small>' % sub if sub else '')
    return ('  <a href="%s.html" class="bc"><span class="bi">%s</span><span class="bk">%s</span>'
            '<span class="bn">%s</span></a>' % (arch, icono, clave, n))


def render():
    tron = '\n'.join(tarjeta(a, '%d' % (i + 1), t, idea) for i, (a, t, idea) in enumerate(TRONCAL))
    amp = ''
    for grupo, sale, items in AMPLIACIONES:
        amp += ('<p class="grupo-tit"><strong>%s</strong> · sale de %s</p>\n<div class="bg">\n' % (grupo, sale))
        amp += '\n'.join(tarjeta(a, '🚀', t, 'Ampliación %d' % int(a[1:])) for a, t in items)
        amp += '\n</div>\n'
    sm = '\n'.join(tarjeta(a, '🔧', t, 'Requiere servo') for a, t in SIN_MATERIAL)
    hub = (HUB.replace('{R}', '../../').replace('{TITLE}', 'T2 · micro:bit · CyR 1º ESO')
           .replace('{DESC}', 'Trimestre 2 · micro:bit · Computación física con MakeCode: 15 retos '
                              'y 12 ampliaciones · CyR 1º ESO · IES Jiménez de Quesada.')
           .replace('{CANON}', ''))
    idx = (INDICE.replace('{R}', '../../../').replace('{TITLE}', 'Los retos · micro:bit · CyR 1º ESO')
           .replace('{DESC}', 'Índice de los 15 retos troncales de micro:bit, las 12 ampliaciones y los '
                              'tres que requieren servo · CyR 1º ESO.')
           .replace('{CANON}', 'retos/')
           .replace('{TRONCAL}', tron).replace('{AMPLIACIONES}', amp).replace('{SIN_MATERIAL}', sm))
    escribir_t2('index.html', hub)
    escribir('index', idx)


if __name__ == '__main__':
    render()

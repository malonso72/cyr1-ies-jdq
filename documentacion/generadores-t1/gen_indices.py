# -*- coding: utf-8 -*-
"""Rehace el índice de sesiones de T1 y parchea el hub del trimestre."""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import T1 as BASE

TITULOS = {
    1: 'Introducción a Scratch', 2: 'Movimiento y direcciones', 3: 'Bucles',
    4: 'Condicionales I', 5: 'Condicionales II y teclado',
    6: 'Animaciones con disfraces', 7: 'Preguntas y respuestas', 8: 'Variables I',
    9: 'Variables II, azar y puntuación', 10: 'Juego de carreras',
    11: 'Mensajes entre objetos', 12: 'Laberinto I', 13: 'Laberinto II',
    14: 'Piedra, papel o tijera', 15: 'Pong I', 16: 'Pong II',
    17: 'Proyecto final: idea y diseño', 18: 'Proyecto final: construcción',
    19: 'Proyecto final: mejoras', 20: 'Presentación de proyectos',
}

QUE_HACES = {
    1: 'Montas tu primer programa y aprendes a descargarlo para entregarlo.',
    2: 'Recorres un cuadrado y vuelves justo al punto de partida.',
    3: 'Cuadrado, triángulo y pentágono cambiando sólo dos números.',
    4: 'Un bucle que vigila y se para cuando tú se lo dices.',
    5: 'Mueves el personaje con las cuatro flechas del teclado.',
    6: 'Consigues que el personaje camine de verdad, no que patine.',
    7: 'Un diálogo en el que el personaje usa lo que tú contestas.',
    8: 'Una calculadora que guarda dos números en dos variables.',
    9: 'Un quiz de sumas con marcador de aciertos.',
    10: 'Dos corredores y un ganador distinto en cada partida.',
    11: 'Que un objeto reaccione justo cuando otro hace algo.',
    12: 'Un laberinto con paredes que no se pueden atravesar.',
    13: 'Le añades meta, cronómetro y un segundo nivel.',
    14: 'Juegas contra el ordenador, que elige sin hacer trampas.',
    15: 'La mecánica del Pong: pelota que rebota y pala que sigue al ratón.',
    16: 'Marcador, fin de partida y dificultad que sube sola.',
    17: 'Eliges tu proyecto y escribes la ficha de diseño. Hoy no se programa.',
    18: 'Kit de piezas reutilizables y primera versión jugable.',
    19: 'Depuras los seis fallos típicos y pules el resultado.',
    20: 'Rúbrica, guion de un minuto y entrega definitiva.',
}

BLOQUES = [
    ('🧱 Fundamentos', 'S01–S05',
     'El editor, las direcciones, los bucles y las condiciones. Todo lo que hace falta '
     'para que un programa haga algo y reaccione.', range(1, 6)),
    ('🎛️ Datos e interacción', 'S06–S11',
     'Animar, preguntar, guardar datos en variables, usar el azar y coordinar dos objetos '
     'con mensajes.', range(6, 12)),
    ('🎮 Juegos completos', 'S12–S16',
     'Tres juegos de principio a fin: laberinto, piedra-papel-tijera y Pong. Aquí se junta '
     'todo lo anterior.', range(12, 17)),
    ('🚀 Proyecto final', 'S17–S20',
     'Tu propio proyecto: diseñarlo, construirlo, depurarlo y presentarlo.', range(17, 21)),
]


def tarjetas(nums):
    return ''.join(
        '\n  <a href="s%02d.html" class="bc">'
        '<span class="bi">🗓️</span>'
        '<span class="bk">S%02d · %s</span>'
        '<span class="bn">%s</span></a>' % (n, n, TITULOS[n], QUE_HACES[n])
        for n in nums)


secciones = ''.join(
    '\n<div class="section-title">%s <span style="font-weight:400;opacity:.7">· %s</span></div>'
    '\n<p class="bloque-int">%s</p>'
    '\n<div class="bg bg-large">%s</div>\n' % (tit, rango, desc, tarjetas(nums))
    for tit, rango, desc, nums in BLOQUES)

INDICE = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#FF8C1A">
<link rel="icon" type="image/svg+xml" href="../../../favicon.svg">
<title>Sesiones · T1 Scratch · CyR 1º ESO</title>
<meta name="description" content="Las 20 sesiones del trimestre de Scratch de CyR 1º ESO: fundamentos, datos e interacción, juegos completos y proyecto final. IES Jiménez de Quesada.">
<link rel="canonical" href="https://cyr1-ies-jdq.malonso72.workers.dev/trimestres/t1-scratch/sesiones/index.html">
<meta property="og:title" content="Sesiones · T1 Scratch · CyR 1º ESO">
<meta property="og:description" content="Las 20 sesiones del trimestre de Scratch, con Scratch abierto al lado y entrega en Moodle.">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600;700&family=Barlow+Condensed:wght@600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../../assets/css/common.css">
<link rel="stylesheet" href="../../../assets/css/hub.css">
<style>
  .ses-intro{max-width:900px;margin:0 auto;padding:6px 16px 0;font-size:1.02rem;line-height:1.6;}
  .ses-intro p{margin:0 0 12px;}
  .como{background:#F4F6F9;border:1px solid #D8DDE5;border-radius:10px;padding:14px 18px;margin:14px 0 6px;}
  .como h2{font-family:'Barlow Condensed',sans-serif;font-size:1.2rem;color:#1B4F8A;margin:0 0 8px;}
  .como ol{margin:0;padding-left:20px;}
  .como li{margin-bottom:4px;}
  .bloque-int{max-width:900px;margin:-2px auto 10px;padding:0 4px;color:#555D6B;font-size:.95rem;}
</style>
</head>
<body>
<a href="#main-content" class="skip-link">Saltar al contenido principal</a>

<header class="curso-hd">
<a class="curso-lg" href="../../../index.html">CyR 1º ESO</a>
<span class="curso-sb">T1 · Scratch</span>
</header>

<nav class="curso-navcross" role="navigation" aria-label="Navegación del trimestre">
<a href="../../../index.html"><span>🏠</span><span class="nc-lbl">Índice</span></a>
<span class="nc-sep">·</span>
<a href="../index.html"><span>📋</span><span class="nc-lbl">Hub T1</span></a>
<span class="nc-sep">·</span>
<span class="nc-current"><span>🗓️</span><span class="nc-lbl">Sesiones</span></span>
<span class="nc-sep">·</span>
<a href="../juegos/index.html"><span>🎮</span><span class="nc-lbl">Juegos</span></a>
<span class="nc-sep">·</span>
<a href="../teoria.html"><span>📖</span><span class="nc-lbl">Teoría</span></a>
</nav>

<div id="main-content">
<section class="unidad-titulo-hero">
  <div class="num">Trimestre 1</div>
  <h1>🗓️ Las 20 sesiones de Scratch</h1>
  <div class="duracion">De los primeros bloques al proyecto final</div>
</section>

<main class="ses-intro">
<div class="como">
  <h2>Cómo funciona cada sesión</h2>
  <ol>
    <li>Entras desde <strong>Moodle</strong> en la sesión que toca.</li>
    <li>Abres <strong>Scratch</strong> con el botón de la página y lo dejas a un lado de la
      pantalla, con la sesión al otro. Así no tienes que ir y venir.</li>
    <li>Lees el programa, contestas a la pregunta y haces la actividad.</li>
    <li><strong>Archivo → Guardar en tu ordenador</strong> y subes el <code>.sb3</code> a Moodle.</li>
  </ol>
</div>
<p>Se trabaja en <strong>scratch.mit.edu</strong>, dentro del navegador: no hay nada que instalar
y <strong>no hace falta cuenta</strong>. Como no hay cuenta, tu proyecto sólo existe en esa
pestaña: si la cierras sin descargarlo, se pierde.</p>
<p>El <a href="../materiales/cuadernillo-scratch-parte-1.pdf">cuadernillo en PDF</a> está hecho con
una versión antigua de Scratch y muchos bloques ya no se llaman igual. Queda como consulta:
cada sesión enlaza su página exacta cuando viene a cuento.</p>
</main>

<div class="hub-main">
{SECCIONES}
</div>
</div>

<p class="foot">
IES Jiménez de Quesada · Santa Fe (Granada)<br>
CyR 1º ESO · Curso 2026-27 · Manuel Alonso Herrera
<br><a href="https://tecnologia-ies-jdq.malonso72.workers.dev/">🏛️ Otras asignaturas del departamento</a>
</p>
<script src="../../../assets/js/common.js"></script>
<script src="../../../assets/js/header.js"></script>
<script data-goatcounter="https://malonso72.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>
'''

ruta = BASE + 'sesiones/index.html'
open(ruta, 'w', encoding='utf-8').write(INDICE.replace('{SECCIONES}', secciones))
print('escrito sesiones/index.html (%d bytes)' % os.path.getsize(ruta))


# ------------------------------------------------------------------ hub T1
hub = open(BASE + 'index.html', encoding='utf-8').read()

CAMBIOS = [
    # coherencia con lo que de verdad se hace en clase
    ('<li>Variables, listas y mensajes en Scratch</li>',
     '<li>Variables y mensajes entre objetos en Scratch</li>'),
    ('<li>Usar variables y listas para guardar el estado del juego (puntos, vidas, niveles)</li>',
     '<li>Usar variables para guardar el estado del juego (puntos, vidas, niveles)</li>'),
    ('<li>Compartir y comentar proyectos en la comunidad Scratch</li>',
     '<li>Descargar el proyecto en un archivo <code>.sb3</code> y entregarlo en Moodle</li>'),
    # la tarjeta de sesiones
    ('<span class="bn">20 sesiones guiadas (s01–s20) con objetivos y entregas</span>',
     '<span class="bn">20 sesiones completas, para trabajar con Scratch abierto al lado</span>'),
    # el cuadernillo deja de venderse como material de trabajo
    ('<span class="bk">Cuadernillo Scratch · Parte 1</span>\n'
     '    <span class="bn">PDF imprimible para alumnado</span>',
     '<span class="bk">Cuadernillo Scratch (consulta)</span>\n'
     '    <span class="bn">PDF antiguo, hecho con Scratch 2: varios bloques ya no se llaman '
     'así. Cada sesión enlaza su página exacta</span>'),
]

for viejo, nuevo in CAMBIOS:
    if viejo not in hub and nuevo not in hub:
        print('  AVISO: no encontrado ->', viejo[:70])
    hub = hub.replace(viejo, nuevo)

# botón para abrir Scratch, el primero de los recursos
ANCLA = '<div class="section-title">📚 Recursos del trimestre</div>\n<div class="bg bg-large">'
BOTON = ANCLA + '''
  <a href="https://scratch.mit.edu/projects/editor/" target="_blank" rel="noopener" class="bc tipo-tool">
    <span class="bi">🐱</span>
    <span class="bk">Abrir Scratch</span>
    <span class="bn">Editor oficial, en el navegador. Sin instalar nada y sin cuenta</span>
  </a>'''
if 'Abrir Scratch' in hub:
    pass                      # ya estaba: el generador se puede reejecutar sin duplicar
elif ANCLA in hub:
    hub = hub.replace(ANCLA, BOTON)
else:
    print('  AVISO: no encontrado el ancla de recursos')

# el enfoque de trabajo, puesto al día
VIEJO_ENF = ('<p>Cada semana se trabaja sobre un mini-reto del cuadernillo y se cierra con una '
             'pequeña entrega. Al final del trimestre se realiza un <strong>proyecto integrador'
             '</strong> (animación o videojuego propio) en parejas, que incluye guion, diseño y '
             'código. La evaluación combina las entregas semanales, el cuaderno del alumno y el '
             'proyecto final.</p>')
NUEVO_ENF = ('<p>Cada sesión tiene su propia página: un programa que hay que <strong>leer y '
             'entender antes de escribir el tuyo</strong>, una pregunta de comprensión, la '
             'actividad y la entrega. Se trabaja con Scratch abierto al lado, en el navegador, '
             'sin instalar nada y sin cuenta.</p>\n'
             '    <p>Las <strong>cuatro últimas sesiones</strong> son un proyecto propio: diseño, '
             'construcción, depuración y presentación. La evaluación combina las entregas de cada '
             'sesión en Moodle y ese proyecto final, con una rúbrica que el alumnado conoce desde '
             'la sesión 17.</p>')
if VIEJO_ENF in hub:
    hub = hub.replace(VIEJO_ENF, NUEVO_ENF)
else:
    print('  AVISO: no encontrado el párrafo de enfoque')

open(BASE + 'index.html', 'w', encoding='utf-8').write(hub)
print('parcheado index.html del hub (%d bytes)' % os.path.getsize(BASE + 'index.html'))

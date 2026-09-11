# -*- coding: utf-8 -*-
"""Presentación inicial de T1 · Scratch, para proyectar el primer día.

Se genera para poder reutilizar dos piezas que ya existen y están dibujadas:
el mapa del editor de la S01 y un script de bloques de verdad. Una presentación
que enseña Scratch con capturas de otra versión es el problema del cuadernillo
otra vez.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagramas import mapa_editor
from scratchsvg import script_svg
from comun import T1

PROGRAMA = [
    ('hat', 'events', ['al hacer clic en', ('icon', 'bandera')]),
    ('stack', 'looks', ['decir', ('txt', '¡Hola! Soy Sprite1'), 'durante', ('num', '2'),
                        'segundos']),
    ('stack', 'motion', ['mover', ('num', '100'), 'pasos']),
    ('stack', 'sound', ['iniciar sonido', ('drop', 'Miau')]),
]

CSS_EXTRA = '''
.lienzo{background:#fff;border-radius:18px;padding:1.1rem 1.3rem;width:100%;z-index:2;
  box-shadow:0 18px 50px rgba(0,0,0,.38);margin-top:1.2rem}
.lienzo.ancho{max-width:940px}.lienzo.medio{max-width:620px}
.lienzo svg{width:100%;height:auto;display:block;max-height:60vh}
.mini{font-size:clamp(15px,1.6vw,23px);color:#c9b8d4;margin-top:1rem}
.cards.tres{grid-template-columns:repeat(3,1fr)}
.cards .tit{display:block;font-weight:700;color:#ffd166;margin-bottom:.3rem}
@media(max-width:800px){.cards.tres{grid-template-columns:1fr}}
'''


def slide(tag, cuerpo, activa=False):
    return ('<div class="slide%s"><div class="grid"></div>'
            '<div class="tag">%s</div>%s</div>'
            % (' active' if activa else '', tag, cuerpo))


def tarjetas(items, clase=''):
    return ('<div class="cards%s">%s</div>'
            % (clase, ''.join('<div class="card">%s</div>' % t for t in items)))


SLIDES = [
    slide('MODO CREADOR DE VIDEOJUEGOS',
          '<h1><span class="orange">SCRATCH</span></h1>'
          '<p>Programación por bloques · juegos · animaciones · historias interactivas</p>',
          activa=True),

    slide('PREGUNTA CERO',
          '<h2>¿Se puede aprender a programar creando videojuegos?</h2>'
          '<p>Este trimestre la respuesta va a ser sí.</p>'),

    slide('ASÍ ES POR DENTRO',
          '<div class="lienzo ancho">' + mapa_editor() + '</div>'
          '<p class="mini"><strong>Cuatro zonas y ya está:</strong> la paleta, el área de código, '
          'el escenario y la lista de objetos. Se abre en el navegador: no hay nada que '
          'instalar.</p>'),

    slide('UN PROGRAMA ES UNA PILA DE BLOQUES',
          '<div class="lienzo medio">'
          + script_svg(PROGRAMA,
                       'Programa: al hacer clic en la bandera verde, decir ¡Hola! Soy Sprite1 '
                       'durante 2 segundos, mover 100 pasos e iniciar el sonido Miau')
          + '</div>'
          '<p class="mini">Se arrastran y se encajan, como piezas de construcción. El de arriba '
          'tiene forma de sombrero: es el que arranca todo.</p>'),

    slide('LO QUE VAIS A USAR',
          tarjetas(['🎭 Objetos', '🖼️ Fondos', '🧩 Bloques',
                    '🔁 Bucles', '❓ Condicionales', '🔢 Variables'])),

    slide('OJO CON ESTO',
          '<h2>No usamos cuenta</h2>'
          '<p>Tu proyecto sólo existe <strong>en la pestaña</strong>. Si la cierras sin '
          'descargarlo, se pierde.</p>'
          '<p class="mini">Archivo → Guardar en tu ordenador → aparece un <code>.sb3</code> en '
          'Descargas → se sube a Moodle. Todas las clases.</p>'),

    slide('PROGRESIÓN',
          '<div class="num">20</div>'
          '<p>sesiones: dieciséis para aprender y las cuatro últimas para el proyecto final.</p>'),

    slide('EL PROYECTO FINAL',
          '<h2>Eliges uno y lo haces tuyo</h2>'
          + tarjetas(['<span class="tit">🧱 Arkanoid</span>Rompe los ladrillos',
                      '<span class="tit">👾 Space Invaders</span>Nave y marcianos',
                      '<span class="tit">☄️ Esquivar</span>Aguanta con tres vidas'], ' tres')
          + '<p class="mini">El juego viene montado. Lo que se evalúa es tu versión: qué le '
            'cambias y qué le añades.</p>'),

    slide('SISTEMA LISTO',
          '<h2 class="hero">¿Preparados?</h2><p>La sesión 1 empieza ahora.</p>'),
]

PAG = '''<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Presentación inicial · T1 Scratch · CyR 1º ESO</title>
<meta name="theme-color" content="#201124">
<link rel="icon" type="image/svg+xml" href="../../favicon.svg">
<meta name="description" content="Presentación de apertura del trimestre de Scratch para proyectar en clase: cómo es el editor por dentro, qué es un programa y qué se hace en las 20 sesiones. CyR 1º ESO · IES Jiménez de Quesada.">
<link rel="canonical" href="https://cyr1-ies-jdq.malonso72.workers.dev/trimestres/t1-scratch/presentacion.html">
<meta property="og:title" content="Presentación inicial · T1 Scratch · CyR 1º ESO">
<meta property="og:description" content="Apertura del trimestre de Scratch para proyectar en clase.">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<style>
*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;overflow:hidden;font-family:system-ui,-apple-system,Segoe UI,sans-serif;background:#201124;color:#fff}
.slide{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:6vh 7vw;opacity:0;pointer-events:none;transition:.45s;background:radial-gradient(circle at 75% 25%,rgba(255,140,26,.22),transparent 32%),radial-gradient(circle at 20% 80%,rgba(89,180,255,.18),transparent 35%),#201124}
.slide.active{opacity:1;pointer-events:auto}.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.055) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.055) 1px,transparent 1px);background-size:48px 48px}
h1,h2.hero{font-size:clamp(56px,10vw,140px);line-height:1;margin:.1em 0;text-align:center}.orange{color:#ff8c1a}.blue{color:#59b4ff}h2{font-size:clamp(34px,6vw,76px);text-align:center;margin:.2em 0}p{font-size:clamp(20px,2.5vw,34px);max-width:1050px;text-align:center;color:#f8e9ff}.tag{font-family:monospace;color:#ffd166;border:1px solid rgba(255,209,102,.5);padding:.45rem 1rem;border-radius:999px;background:rgba(255,209,102,.1);z-index:2}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;max-width:1200px;width:100%;z-index:2;margin-top:2rem}.card{border:1px solid rgba(255,140,26,.35);border-radius:20px;padding:1.2rem;background:rgba(255,140,26,.12);font-size:clamp(16px,1.8vw,24px);text-align:center}.num{font-family:monospace;font-size:clamp(74px,12vw,180px);font-weight:900;color:#ff8c1a}.nav{position:absolute;right:2vw;bottom:2vh;display:flex;gap:.7rem;z-index:5}.nav button{width:48px;height:48px;border-radius:10px;border:1px solid #ffd166;background:rgba(255,209,102,.12);color:#fff;font-size:24px}.counter{position:absolute;left:2vw;bottom:3vh;color:rgba(255,255,255,.55);font-family:monospace;z-index:5}@media(max-width:800px){.cards{grid-template-columns:1fr 1fr}}
{EXTRA}
</style></head><body>
<main>
{SLIDES}
</main>
<div class="counter" id="c">01 / {N}</div><div class="nav"><button type="button" aria-label="Diapositiva anterior" onclick="go(-1)">‹</button><button type="button" aria-label="Diapositiva siguiente" onclick="go(1)">›</button></div>
<script>let s=0;const slides=[...document.querySelectorAll('.slide')];function show(){slides.forEach((x,i)=>x.classList.toggle('active',i===s));document.getElementById('c').textContent=String(s+1).padStart(2,'0')+' / '+String(slides.length).padStart(2,'0')}function go(d){s=Math.max(0,Math.min(slides.length-1,s+d));show()}document.addEventListener('keydown',e=>{if(['ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();go(1)}if(['ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();go(-1)}});show();</script>
<script data-goatcounter="https://malonso72.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body></html>
'''

html = (PAG.replace('{EXTRA}', CSS_EXTRA.strip())
           .replace('{SLIDES}', '\n'.join(SLIDES))
           .replace('{N}', '%02d' % len(SLIDES)))
ruta = os.path.join(T1, 'presentacion.html')
open(ruta, 'w', encoding='utf-8').write(html)
print('  presentacion.html  %6d bytes · %d diapositivas' % (len(html), len(SLIDES)))

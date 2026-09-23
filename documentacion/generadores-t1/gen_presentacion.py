# -*- coding: utf-8 -*-
"""Presentación inicial de T1 · Scratch, para proyectar el primer día.

No es una apertura motivacional: es **la visita guiada al programa**. Qué hay en
la pantalla, qué hay en cada pestaña, qué hay en cada cajón de la paleta y qué
significa la forma de cada bloque. Al salir de aquí el alumnado tiene que saber
dónde buscar las cosas.

Se genera para poder reutilizar lo que ya está dibujado —el mapa del editor de la
S01 y el motor de bloques de las 21 sesiones— en vez de meter capturas de otra
versión de Scratch, que es justo el problema del cuadernillo.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagramas import mapa_editor, _gato
from scratchsvg import script_svg, rep, hexa, op, var
from comun import T1

BANDERA = ('hat', 'events', ['al hacer clic en', ('icon', 'bandera')])


# ---------------------------------------------------------------- piezas
def slide(tag, cuerpo, activa=False):
    return ('<div class="slide%s"><div class="grid"></div>'
            '<div class="tag">%s</div>%s</div>'
            % (' active' if activa else '', tag, cuerpo))


def tarjetas(items, clase=''):
    return ('<div class="cards%s">%s</div>'
            % (clase, ''.join('<div class="card">%s</div>' % t for t in items)))


def pieza(bloques, alt, pie):
    """Un bloque suelto sobre un lienzo claro, con su explicación debajo."""
    return ('<div class="pieza"><div class="lienzo">%s</div><span>%s</span></div>'
            % (script_svg(bloques, alt), pie))


def piezas(items, clase=''):
    return '<div class="piezas%s">%s</div>' % (clase, ''.join(items))


CATEGORIAS = [
    ('#4C97FF', 'Movimiento', 'Cambiar de sitio: mover, girar, ir a x e y'),
    ('#9966FF', 'Apariencia', 'Cómo se ve: decir, disfraces, tamaño, mostrar'),
    ('#CF63CF', 'Sonido', 'Los sonidos que trae cada objeto'),
    ('#FFBF00', 'Eventos', 'Cuándo arranca: la bandera, una tecla, un aviso'),
    ('#FFAB19', 'Control', 'Repetir y decidir. Aquí está casi todo'),
    ('#5CB1D6', 'Sensores', 'Lo que el programa puede mirar: ¿tocando?, ¿tecla?'),
    ('#59C059', 'Operadores', 'Cuentas y comparaciones: + − × ÷, =, y, o'),
    ('#FF8C1A', 'Variables', 'Cajas con nombre donde guardas datos'),
    ('#FF6680', 'Mis bloques', 'Bloques que te inventas tú. Este año no'),
]


def cajones():
    return ('<div class="cajones">%s</div>' % ''.join(
        '<div class="cajon"><span class="pt" style="background:%s"></span>'
        '<span class="ct"><span class="cn">%s</span><span class="cd">%s</span></span></div>' % c
        for c in CATEGORIAS))


def escenario():
    """El escenario con sus coordenadas: lo que más cuesta situar."""
    W, H = 620, 400
    x0, y0, w, h = 70, 34, 480, 336          # el escenario, 480x360 a escala
    cx, cy = x0 + w / 2.0, y0 + h / 2.0
    a = []
    a.append('<rect x="%d" y="%d" width="%d" height="%d" rx="8" fill="#FFFFFF" '
             'stroke="#C7D0DB" stroke-width="2"/>' % (x0, y0, w, h))
    a.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#C7D0DB" '
             'stroke-dasharray="5 5"/>' % (x0, cy, x0 + w, cy))
    a.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="#C7D0DB" '
             'stroke-dasharray="5 5"/>' % (cx, y0, cx, y0 + h))
    a.append(_gato(cx, cy, 26))

    def t(x, y, s, anc='middle', col='#555D6B', fs=15, peso='600'):
        a.append('<text x="%.1f" y="%.1f" text-anchor="%s" fill="%s" font-size="%d" '
                 'font-weight="%s" font-family="%s">%s</text>'
                 % (x, y, anc, col, fs, peso, "'Barlow',Arial,sans-serif", s))

    t(cx, cy + 54, 'x: 0   y: 0', col='#1B4F8A', fs=17, peso='700')
    t(x0 + 10, y0 + 22, '−240, 180', 'start')
    t(x0 + w - 10, y0 + 22, '240, 180', 'end')
    t(x0 + 10, y0 + h - 12, '−240, −180', 'start')
    t(x0 + w - 10, y0 + h - 12, '240, −180', 'end')
    t(cx, y0 - 12, 'y crece hacia arriba  ↑', fs=16, col='#1B4F8A')
    t(x0 + w, y0 + h + 24, 'x crece hacia la derecha  →', 'end', fs=16, col='#1B4F8A')
    return ('<svg viewBox="0 0 %d %d" role="img" aria-label="El escenario de Scratch mide 480 '
            'por 360: el centro es x igual a 0 e y igual a 0, la esquina superior izquierda es '
            'x menos 240 e y 180, y la inferior derecha x 240 e y menos 180">'
            '<title>Las coordenadas del escenario de Scratch</title>%s</svg>'
            % (W, H, ''.join(a)))


# ---------------------------------------------------------------- diapositivas
SLIDES = [
    slide('MODO CREADOR DE VIDEOJUEGOS',
          '<h1><span class="orange">SCRATCH</span></h1>'
          '<p>Programación por bloques · juegos · animaciones · historias interactivas</p>',
          activa=True),

    slide('PREGUNTA CERO',
          '<h2>¿Se puede aprender a programar creando videojuegos?</h2>'
          '<p>Este trimestre la respuesta va a ser sí. Pero primero hay que saber '
          '<strong>dónde está cada cosa</strong>.</p>'),

    # ---- la pantalla
    slide('LA PANTALLA',
          '<div class="lienzo ancho">' + mapa_editor() + '</div>'
          '<p class="mini"><strong>Cuatro zonas y ya está.</strong> Se abre en el navegador, en '
          '<span class="mono">scratch.mit.edu</span>: no hay nada que instalar.</p>'),

    slide('EL ESCENARIO',
          '<div class="lienzo medio">' + escenario() + '</div>'
          '<p class="mini">Mide siempre lo mismo: <strong>480 de ancho por 360 de alto</strong>. '
          'El centro es el <span class="mono">0, 0</span>. Cuando un bloque diga '
          '<span class="mono">ir a x: 100 y: −50</span>, ya sabes dónde va a acabar.</p>'),

    slide('LOS OBJETOS',
          '<h2>Cada objeto va por su cuenta</h2>'
          + tarjetas(['<span class="tit">Su código</span>Los bloques que le pongas a uno '
                      '<strong>no</strong> los tiene el otro',
                      '<span class="tit">Sus disfraces</span>Sus propios dibujos, para animarlo',
                      '<span class="tit">Sus sonidos</span>El gato trae '
                      '<span class="mono">Miau</span>; los demás, otros'], ' tres')
          + '<p class="mini">El escenario es común; el código, no. <strong>Antes de arrastrar un '
            'bloque, mira qué objeto tienes seleccionado</strong> abajo a la derecha. Es el fallo '
            'que va a tener media clase.</p>'),

    slide('LAS TRES PESTAÑAS',
          '<h2>Arriba a la izquierda</h2>'
          + tarjetas(['<span class="tit">Código</span>Donde se programa. Aquí vais a estar el '
                      '90 % del tiempo',
                      '<span class="tit">Disfraces</span>Los dibujos del objeto. Se editan y se '
                      'crean nuevos',
                      '<span class="tit">Sonidos</span>Los sonidos de ese objeto, y una '
                      'biblioteca para añadir más'], ' tres')
          + '<p class="mini">Las tres son <strong>del objeto que tengas seleccionado</strong>. '
            'Si cambias de objeto, cambian las tres.</p>'),

    # ---- la paleta
    slide('LA PALETA · NUEVE CAJONES',
          '<p class="mini sup"><strong>El color te dice dónde buscar.</strong> Todos los bloques '
          'están aquí, repartidos por colores.</p>' + cajones()
          + '<p class="mini">Y abajo del todo, el botón de <strong>Extensiones</strong>: Música, '
            'Lápiz, Texto a voz… <strong>No están en la paleta hasta que las añades.</strong> '
            'Este trimestre no hace falta ninguna.</p>'),

    slide('MOVIMIENTO Y APARIENCIA',
          piezas([
              pieza([('stack', 'motion', ['mover', ('num', '10'), 'pasos'])],
                    'Bloque mover 10 pasos', 'Avanza en la dirección a la que mire'),
              pieza([('stack', 'motion', ['ir a x:', ('num', '0'), 'y:', ('num', '0')])],
                    'Bloque ir a x 0 y 0', 'Lo coloca en un punto exacto'),
              pieza([('stack', 'looks', ['decir', ('txt', '¡Hola!'), 'durante', ('num', '2'),
                                         'segundos'])],
                    'Bloque decir ¡Hola! durante 2 segundos', 'Saca un bocadillo'),
              pieza([('stack', 'looks', ['siguiente disfraz'])],
                    'Bloque siguiente disfraz', 'Cambia el dibujo: así se anda'),
          ])),

    slide('EVENTOS Y CONTROL',
          piezas([
              pieza([BANDERA], 'Bloque al hacer clic en la bandera verde',
                    'Un <strong>sombrero</strong>: arranca el programa'),
              pieza([('hat', 'events', ['al presionar tecla', ('drop', 'espacio')])],
                    'Bloque al presionar la tecla espacio', 'Otro sombrero, con una tecla'),
              pieza([('c', 'control', ['repetir', ('num', '10')],
                      [('stack', 'motion', ['mover', ('num', '10'), 'pasos'])])],
                    'Bloque repetir 10 veces con mover 10 pasos dentro',
                    'Repite lo de dentro. Ahorra escribir'),
              pieza([('c', 'control', ['si', hexa('sensing', '¿tocando', ('drop', 'borde'), '?'),
                                       'entonces'],
                      [('stack', 'sound', ['iniciar sonido', ('drop', 'Miau')])])],
                    'Bloque si está tocando el borde entonces iniciar sonido Miau',
                    'Decide: sólo hace lo de dentro si se cumple'),
          ])),

    slide('SENSORES Y OPERADORES',
          piezas([
              pieza([('c', 'control', ['si', hexa('sensing', '¿tecla', ('drop', 'espacio'),
                                                  'presionada?'), 'entonces'],
                      [('stack', 'motion', ['mover', ('num', '10'), 'pasos'])])],
                    'Bloque si la tecla espacio está presionada entonces mover 10 pasos',
                    'Miran el teclado, el ratón y los choques'),
              pieza([('stack', 'sensing', ['preguntar', ('txt', '¿Cómo te llamas?'), 'y esperar'])],
                    'Bloque preguntar ¿Cómo te llamas? y esperar',
                    'Para el programa y espera tu respuesta'),
              pieza([('stack', 'looks', ['decir', op('unir', ('txt', 'Hola, '),
                                                     rep('sensing', 'respuesta')),
                                         'durante', ('num', '2'), 'segundos'])],
                    'Bloque decir unir Hola con respuesta durante 2 segundos',
                    'Los operadores hacen cuentas y pegan textos'),
              pieza([('stack', 'motion', ['mover', op('número aleatorio entre', ('num', '1'),
                                                      'y', ('num', '10')), 'pasos'])],
                    'Bloque mover un número aleatorio entre 1 y 10 pasos',
                    'El azar: lo que hace que un juego no sea siempre igual'),
          ])),

    slide('SONIDO Y VARIABLES',
          piezas([
              pieza([('stack', 'sound', ['iniciar sonido', ('drop', 'Miau')])],
                    'Bloque iniciar sonido Miau', 'Suena, y el programa sigue'),
              pieza([('stack', 'variables', ['dar a', ('drop', 'Puntos'), 'el valor',
                                             ('num', '0')])],
                    'Bloque dar a Puntos el valor 0',
                    'Mete un dato en la caja. <strong>Machaca</strong> lo que hubiera'),
              pieza([('stack', 'variables', ['sumar a', ('drop', 'Puntos'), ('num', '1')])],
                    'Bloque sumar a Puntos 1',
                    'Le <strong>añade</strong>. Es el bloque de contar'),
              pieza([('stack', 'looks', ['decir', var('Puntos'), 'durante', ('num', '2'),
                                         'segundos'])],
                    'Bloque decir la variable Puntos durante 2 segundos',
                    'La variable se arrastra dentro de otro bloque'),
          ])),

    slide('LA FORMA IMPORTA',
          '<h2>Cada bloque sólo encaja donde puede</h2>' +
          piezas([
              pieza([BANDERA], 'Bloque sombrero al hacer clic en la bandera',
                    '<strong>Sombrero.</strong> Va arriba del todo y no admite nada encima'),
              pieza([('stack', 'motion', ['mover', ('num', '10'), 'pasos'])],
                    'Bloque apilable mover 10 pasos',
                    '<strong>Apilable.</strong> Muesca arriba y abajo: se encadena'),
              pieza([('cap', 'control', ['detener', ('drop', 'todos')])],
                    'Bloque final detener todos',
                    '<strong>Final.</strong> Sin muesca abajo: detrás no va nada'),
          ], ' tres')
          + '<p class="mini">Y los que van <strong>dentro de un hueco</strong>: el '
            '<strong>hexágono</strong> sólo entra en huecos hexagonales —vale sí o no— y el '
            '<strong>óvalo</strong> en los redondeados —vale un número o un texto—. '
            'Si no encaja, es que no va ahí.</p>'),

    # ---- cómo se trabaja
    slide('UN PROGRAMA ES UNA PILA',
          '<div class="lienzo medio">'
          + script_svg([BANDERA,
                        ('stack', 'looks', ['decir', ('txt', '¡Hola! Soy Sprite1'), 'durante',
                                            ('num', '2'), 'segundos']),
                        ('stack', 'motion', ['mover', ('num', '100'), 'pasos']),
                        ('stack', 'sound', ['iniciar sonido', ('drop', 'Miau')])],
                       'Programa: al hacer clic en la bandera verde, decir ¡Hola! Soy Sprite1 '
                       'durante 2 segundos, mover 100 pasos e iniciar el sonido Miau')
          + '</div>'
          '<p class="mini">Se arrastran de la paleta al área de código y se encajan. Se ejecuta '
          '<strong>de arriba abajo</strong>, y arranca al pulsar la <strong>bandera verde</strong>. '
          'El círculo rojo lo para.</p>'),

    slide('OJO CON ESTO',
          '<h2>No usamos cuenta</h2>'
          '<p>Tu proyecto sólo existe <strong>en la pestaña</strong>. Si la cierras sin '
          'descargarlo, se pierde.</p>'
          '<p class="mini">Archivo → Guardar en tu ordenador → aparece un '
          '<span class="mono">.sb3</span> en Descargas → se sube a Moodle. '
          '<strong>Todas las clases.</strong></p>'),

    slide('PROGRESIÓN',
          '<div class="num">21</div>'
          '<p>sesiones: <strong>dieciséis</strong> para aprender, <strong>una</strong> para '
          'aprender a cazar fallos y las <strong>cuatro últimas</strong> para el proyecto '
          'final.</p>'),

    slide('EL PROYECTO FINAL',
          '<h2>Eliges uno y lo haces tuyo</h2>'
          + tarjetas(['<span class="tit">🧱 Arkanoid</span>Rompe los ladrillos',
                      '<span class="tit">👾 Space Invaders</span>Nave y marcianos',
                      '<span class="tit">☄️ Esquivar</span>Aguanta con tres vidas'], ' tres')
          + '<p class="mini">El juego viene montado. Lo que se evalúa es '
            '<strong>tu versión</strong>: qué le cambias y qué le añades.</p>'),

    slide('SISTEMA LISTO',
          '<h2 class="hero">¿Preparados?</h2><p>La sesión 1 empieza ahora.</p>'),
]

CSS_EXTRA = '''
.lienzo{background:#fff;border-radius:18px;padding:1rem 1.2rem;width:100%;z-index:2;
  box-shadow:0 18px 50px rgba(0,0,0,.38)}
.lienzo.ancho{max-width:880px;margin-top:.8rem}
.lienzo.medio{max-width:540px;margin-top:.8rem}
.lienzo svg{width:100%;height:auto;display:block;max-height:54vh}
.mini{font-size:clamp(14px,1.5vw,21px);color:#c9b8d4;margin-top:.9rem;max-width:1100px}
.mono{font-family:monospace;color:#ffd166}
.cards .tit{display:block;font-weight:700;color:#ffd166;margin-bottom:.3rem}
.cards.tres{grid-template-columns:repeat(3,1fr)}
.cajones{display:grid;grid-template-columns:repeat(3,1fr);gap:.65rem;max-width:1150px;
  width:100%;z-index:2;margin-top:1.1rem}
.cajon{display:grid;grid-template-columns:13px 1fr;gap:.7rem;align-items:stretch;
  border:1px solid rgba(255,255,255,.14);border-radius:14px;padding:.65rem .85rem;
  background:rgba(255,255,255,.05);text-align:left}
.cajon .pt{border-radius:7px;display:block}
.cajon .cn{display:block;font-weight:700;font-size:clamp(14px,1.6vw,22px);color:#fff}
.cajon .cd{display:block;font-size:clamp(11px,1.2vw,16px);color:#c9b8d4;line-height:1.35}
.piezas{display:grid;grid-template-columns:repeat(2,1fr);gap:.9rem;max-width:1100px;
  width:100%;z-index:2;margin-top:1rem}
.piezas.tres{grid-template-columns:repeat(3,1fr)}
.pieza{display:flex;flex-direction:column;gap:.45rem;align-items:center}
.pieza .lienzo{padding:.6rem .7rem;box-shadow:0 10px 26px rgba(0,0,0,.3)}
.pieza .lienzo svg{max-height:19vh}
.pieza span{font-size:clamp(11px,1.25vw,17px);color:#c9b8d4;text-align:center;line-height:1.35}
@media(max-width:800px){.cards.tres,.cajones,.piezas,.piezas.tres{grid-template-columns:1fr}}
'''

PAG = '''<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Presentación inicial · T1 Scratch · CyR 1º ESO</title>
<meta name="theme-color" content="#201124">
<link rel="icon" type="image/svg+xml" href="../../favicon.svg">
<meta name="description" content="Visita guiada a Scratch para proyectar el primer día: la pantalla, el escenario, las pestañas, los nueve cajones de la paleta y qué significa la forma de cada bloque. CyR 1º ESO · IES Jiménez de Quesada.">
<link rel="canonical" href="https://cyr1-ies-jdq.malonso72.workers.dev/trimestres/t1-scratch/presentacion.html">
<meta property="og:title" content="Presentación inicial · T1 Scratch · CyR 1º ESO">
<meta property="og:description" content="Visita guiada a Scratch para proyectar el primer día de clase.">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<style>
*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;overflow:hidden;font-family:system-ui,-apple-system,Segoe UI,sans-serif;background:#201124;color:#fff}
.slide{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:5vh 6vw;opacity:0;pointer-events:none;transition:.45s;background:radial-gradient(circle at 75% 25%,rgba(255,140,26,.22),transparent 32%),radial-gradient(circle at 20% 80%,rgba(89,180,255,.18),transparent 35%),#201124}
.slide.active{opacity:1;pointer-events:auto}.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.055) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.055) 1px,transparent 1px);background-size:48px 48px}
h1,h2.hero{font-size:clamp(56px,10vw,140px);line-height:1;margin:.1em 0;text-align:center}.orange{color:#ff8c1a}.blue{color:#59b4ff}h2{font-size:clamp(26px,4.2vw,54px);text-align:center;margin:.2em 0}p{font-size:clamp(18px,2.2vw,30px);max-width:1050px;text-align:center;color:#f8e9ff}.tag{font-family:monospace;color:#ffd166;border:1px solid rgba(255,209,102,.5);padding:.45rem 1rem;border-radius:999px;background:rgba(255,209,102,.1);z-index:2}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;max-width:1200px;width:100%;z-index:2;margin-top:1.3rem}.card{border:1px solid rgba(255,140,26,.35);border-radius:20px;padding:1rem 1.1rem;background:rgba(255,140,26,.12);font-size:clamp(14px,1.5vw,21px);text-align:center;line-height:1.4}.num{font-family:monospace;font-size:clamp(74px,12vw,180px);font-weight:900;color:#ff8c1a}.nav{position:absolute;right:2vw;bottom:2vh;display:flex;gap:.7rem;z-index:5}.nav button{width:48px;height:48px;border-radius:10px;border:1px solid #ffd166;background:rgba(255,209,102,.12);color:#fff;font-size:24px}.counter{position:absolute;left:2vw;bottom:3vh;color:rgba(255,255,255,.55);font-family:monospace;z-index:5}@media(max-width:800px){.cards{grid-template-columns:1fr 1fr}}
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

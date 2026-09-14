# -*- coding: utf-8 -*-
"""Presentación inicial de T2 · micro:bit, para proyectar el primer día.

Igual que la de T1: no es una apertura motivacional, es la visita guiada. Qué lleva la
placa, cómo es la pantalla de MakeCode, qué hay en cada cajón, qué significa la forma
de cada bloque, cómo va el programa del ordenador a la placa y qué se entrega.
Reutiliza el motor de bloques y los dibujos de las páginas de reto.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bloques import *                                  # noqa: F401,F403
from makecodesvg import script_svg, scripts_svg, matriz_svg, boton
from diagramas_t2 import placa_svg, mapa_makecode
from comun_t2 import T2


# ---------------------------------------------------------------- piezas
def slide(tag, cuerpo, activa=False):
    return ('<div class="slide%s"><div class="grid"></div>'
            '<div class="tag">%s</div>%s</div>'
            % (' active' if activa else '', tag, cuerpo))


def tarjetas(items, clase=''):
    return ('<div class="cards%s">%s</div>'
            % (clase, ''.join('<div class="card">%s</div>' % t for t in items)))


def pieza(bloques, alt, pie):
    return ('<div class="pieza"><div class="lienzo">%s</div><span>%s</span></div>'
            % (script_svg(bloques, alt), pie))


def piezas(items, clase=''):
    return '<div class="piezas%s">%s</div>' % (clase, ''.join(items))


CATEGORIAS = [
    ('#1E90FF', 'Básico', 'Mostrar cosas, pausar, al iniciar, para siempre'),
    ('#D400D4', 'Entrada', 'Botones, agitar, luz, temperatura, brújula, sonido'),
    ('#E63022', 'Música', 'Tonos y melodías por el altavoz'),
    ('#5C2D91', 'LED', 'Encender y apagar un LED por sus coordenadas'),
    ('#E3008C', 'Radio', 'Hablar con otra placa sin cables'),
    ('#00AA00', 'Bucles', 'Repetir: para, mientras, repetir N veces'),
    ('#00A4A6', 'Lógica', 'Decidir: si… entonces, comparar, y, o'),
    ('#DC143C', 'Variables', 'Cajas con nombre donde guardas un número'),
    ('#9400D3', 'Matemática', 'Cuentas, azar, valor absoluto'),
]


def cajones():
    return ('<div class="cajones">%s</div>' % ''.join(
        '<div class="cajon"><span class="pt" style="background:%s"></span>'
        '<span class="ct"><span class="cn">%s</span><span class="cd">%s</span></span></div>' % c
        for c in CATEGORIAS))


SLIDES = [
    slide('COMPUTACIÓN FÍSICA',
          '<h1><span class="orange">MICRO:BIT</span></h1>'
          '<p>Un ordenador del tamaño de una tarjeta · sensores · LEDs · radio</p>',
          activa=True),

    slide('PREGUNTA CERO',
          '<h2>¿Puede una placa más pequeña que tu móvil notar la luz, saber hacia dónde apunta '
          'y hablar con otra sin cables?</h2>'
          '<p>Sí. Y la vais a programar vosotros. Pero primero, <strong>qué lleva y dónde está '
          'cada cosa</strong>.</p>'),

    slide('LA PLACA',
          '<div class="lienzo medio">' + placa_svg() + '</div>'
          '<p class="mini"><strong>Por delante:</strong> 25 LEDs, dos botones, el logo táctil, '
          'el micrófono y los pines. <strong>Por detrás:</strong> el acelerómetro, la brújula, la '
          'radio, el altavoz, el USB y el botón de reinicio. Es la <strong>V2</strong>.</p>'),

    slide('LO QUE PUEDE HACER',
          '<h2>Lee, decide y actúa</h2>'
          + tarjetas(['<span class="tit">👁️ Lee</span>Botones, luz, temperatura, movimiento, '
                      'brújula, sonido. Cada sensor es <strong>un número</strong>',
                      '<span class="tit">🧠 Decide</span>Con <span class="mono">si… entonces</span>, '
                      'bucles y variables: lo mismo que en Scratch',
                      '<span class="tit">💡 Actúa</span>Enciende LEDs, escribe, suena, manda un '
                      'mensaje por radio a otra placa'], ' tres')
          + '<p class="mini">El programa no corre en el ordenador: se <strong>copia a la placa</strong> '
            'y ella lo ejecuta sola, con la pila puesta y sin cables.</p>'),

    # ---- la pantalla
    slide('LA PANTALLA',
          '<div class="lienzo ancho">' + mapa_makecode() + '</div>'
          '<p class="mini"><strong>Cuatro zonas.</strong> Se abre en el navegador, en '
          '<span class="mono">makecode.microbit.org</span>: nada que instalar, sin cuenta.</p>'),

    slide('LA CAJA DE BLOQUES · NUEVE CAJONES',
          cajones()
          + '<p class="mini sup">Y en <strong>Avanzado</strong>, el cajón <strong>Juego</strong>: '
            'los sprites, para el último reto. Los colores no coinciden con los de Scratch; los '
            'nombres, casi.</p>'),

    slide('BÁSICO Y ENTRADA',
          '<h2>Los dos cajones de casi todos los programas</h2>' +
          piezas([
              pieza([INICIAR([])], 'Bloque al iniciar',
                    '<strong>al iniciar.</strong> Se ejecuta una vez, al arrancar'),
              pieza([SIEMPRE([])], 'Bloque para siempre',
                    '<strong>para siempre.</strong> El «por siempre» de Scratch'),
              pieza([ICONO('corazón')], 'Bloque mostrar ícono corazón',
                    '<strong>mostrar ícono.</strong> Cuarenta dibujos ya hechos'),
              pieza([BOTON('A', [])], 'Bloque al presionarse el botón A',
                    '<strong>al presionarse el botón.</strong> Un evento: arranca solo'),
          ])),

    slide('LED, LÓGICA Y VARIABLES',
          '<h2>Los que llegan a partir del reto 4</h2>' +
          piezas([
              pieza([GRAFICAR(2, 2)], 'Bloque graficar x 2 y 2',
                    '<strong>graficar x y.</strong> Enciende un LED por sus coordenadas'),
              pieza([SI(compara(LUZ, '<', 25), [])], 'Bloque si nivel de luz menor que 25 entonces',
                    '<strong>si… entonces.</strong> Con un sensor dentro de la comparación'),
              pieza([FIJAR('turno', 0)], 'Bloque fijar turno a 0',
                    '<strong>fijar … a.</strong> Guarda un número en una variable'),
              pieza([PARA('índice', 4, [])], 'Bloque para índice de 0 a 4 ejecutar',
                    '<strong>para índice.</strong> Cuenta de 0 a 4 por ti'),
          ])),

    slide('LA FORMA IMPORTA',
          '<h2>Cada bloque sólo encaja donde puede</h2>' +
          piezas([
              pieza([BOTON('B', [])], 'Bloque de evento, plano por arriba',
                    '<strong>Evento.</strong> Plano por arriba, sin muesca: va suelto, no dentro de nada'),
              pieza([PAUSA(100)], 'Bloque apilable pausa 100 ms',
                    '<strong>Apilable.</strong> Muesca arriba y abajo: se encadena'),
              pieza([('stack', 'basico', ['mostrar número', LUZ])], 'Reporter nivel de luz dentro de mostrar número',
                    '<strong>Redondeado.</strong> Vale un número: va en un hueco redondo'),
              pieza([SI(boton('A'), [])], 'Booleano botón A presionado dentro de un si',
                    '<strong>Hexágono.</strong> Vale sí o no: va en un hueco hexagonal'),
          ])),

    # ---- cómo se trabaja
    slide('UN PROGRAMA SON VARIOS EVENTOS',
          '<div class="lienzo medio">'
          + scripts_svg([[INICIAR([CADENA('Hola')])],
                         [BOTON('A', [ICONO('corazón')])],
                         [SIEMPRE([PAUSA(1000), BORRAR])]],
                        'Programa: al iniciar, mostrar cadena Hola; al presionarse el botón A, '
                        'mostrar ícono corazón; para siempre, pausa 1000 y borrar la pantalla')
          + '</div>'
          '<p class="mini">En Scratch todo colgaba de la bandera. Aquí hay <strong>varios bloques '
          'sueltos</strong> y la placa los vigila todos a la vez: uno arranca al encender, otro al '
          'pulsar, otro da vueltas sin parar.</p>'),

    slide('LA MATRIZ',
          '<div class="lienzo medio">' + matriz_svg('..#..:..#..:#####:..#..:..#..', 'La matriz con las coordenadas y el LED central señalado', coords=True, marcar=[(2, 2)]) + '</div>'
          '<p class="mini">Cada LED tiene su <strong>x</strong> (columna) y su <strong>y</strong> '
          '(fila). Se empieza en <strong>cero</strong>, y la <strong>y crece hacia abajo</strong>: '
          'al revés que en Scratch. El del centro es <span class="mono">x=2, y=2</span>.</p>'),

    slide('DEL SIMULADOR A LA PLACA',
          '<h2>Tres pasos, todas las clases</h2>'
          + tarjetas(['<span class="tit">1 · Simulador</span>La placa dibujada de la izquierda '
                      'hace lo mismo que la de verdad. Prueba ahí primero',
                      '<span class="tit">2 · Descargar</span>Escribe el nombre del proyecto y pulsa '
                      'Descargar: sale un archivo <span class="mono">.hex</span>',
                      '<span class="tit">3 · A la placa</span>Conecta el USB: aparece la unidad '
                      '<span class="mono">MICROBIT</span>. Arrastra el archivo dentro'], ' tres')
          + '<p class="mini">La luz amarilla de detrás parpadea unos segundos y el programa '
            'arranca. Ya puedes desenchufar: sigue funcionando.</p>'),

    slide('OJO CON ESTO',
          '<h2>Una placa por pareja, y lo que vale es el archivo</h2>'
          '<p>MakeCode guarda el proyecto en el navegador, pero el ordenador es de todos. El '
          'archivo <span class="mono">.hex</span> con <strong>vuestro nombre</strong> se sube a '
          'Moodle en cada reto.</p>'
          '<p class="mini">Y la placa se cuida: se coge por los bordes, no se dobla, no se '
          'moja, y los pines no se tocan con nada metálico que no sea la pinza que toca.</p>'),

    slide('PROGRESIÓN',
          '<div class="num">15</div>'
          '<p>retos, en orden, y <strong>doce ampliaciones</strong> para quien va rápido. Del '
          '«Hola» al juego con sprites.</p>'),

    slide('SISTEMA LISTO',
          '<h2 class="hero">¿Preparados?</h2><p>El reto 1 empieza ahora.</p>'),
]

CSS_EXTRA = '''
.lienzo{background:#fff;border-radius:18px;padding:1rem 1.2rem;width:100%;z-index:2;
  box-shadow:0 18px 50px rgba(0,0,0,.38)}
.lienzo.ancho{max-width:880px;margin-top:.8rem}
.lienzo.medio{max-width:520px;margin-top:.8rem}
.lienzo svg{width:100%;height:auto;display:block;max-height:54vh;margin:0 auto}
.mini{font-size:clamp(14px,1.5vw,21px);color:#c9d6e8;margin-top:.9rem;max-width:1100px}
.mono{font-family:monospace;color:#ffd166}
.cards .tit{display:block;font-weight:700;color:#ffd166;margin-bottom:.3rem}
.cards.tres{grid-template-columns:repeat(3,1fr)}
.cajones{display:grid;grid-template-columns:repeat(3,1fr);gap:.65rem;max-width:1150px;
  width:100%;z-index:2;margin-top:1.1rem}
.cajon{display:flex;gap:.7rem;align-items:stretch;
  border:1px solid rgba(255,255,255,.14);border-radius:14px;padding:.6rem .8rem;
  background:rgba(255,255,255,.05);text-align:left}
.cajon .pt{flex:0 0 12px;border-radius:6px;display:block}
.cajon .ct{flex:1 1 auto;min-width:0}
.cajon .cn{display:block;font-weight:700;font-size:clamp(14px,1.55vw,21px);color:#fff}
.cajon .cd{display:block;font-size:clamp(11px,1.15vw,16px);color:#c9d6e8;line-height:1.3}
.mini.sup{margin:.9rem 0 0}
.piezas{display:grid;grid-template-columns:repeat(2,1fr);gap:.7rem 1.2rem;max-width:900px;
  width:100%;z-index:2;margin-top:1rem}
.pieza{display:flex;flex-direction:column;gap:.45rem;align-items:center}
.pieza .lienzo{padding:.6rem .7rem;box-shadow:0 10px 26px rgba(0,0,0,.3)}
.pieza .lienzo svg{max-height:17vh}
.pieza span{font-size:clamp(11px,1.25vw,17px);color:#c9d6e8;text-align:center;line-height:1.35}
@media(max-width:800px){.cards.tres,.cajones,.piezas{grid-template-columns:1fr}}
'''

PAG = '''<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Presentación inicial · T2 micro:bit · CyR 1º ESO</title>
<meta name="theme-color" content="#0F1C2E">
<link rel="icon" type="image/svg+xml" href="../../favicon.svg">
<meta name="description" content="Visita guiada a la micro:bit y a MakeCode para proyectar el primer día: qué lleva la placa, la pantalla del editor, los nueve cajones, la forma de los bloques, cómo pasa el programa a la placa y qué se entrega. CyR 1º ESO · IES Jiménez de Quesada.">
<link rel="canonical" href="https://cyr1-ies-jdq.malonso72.workers.dev/trimestres/t2-microbit/presentacion.html">
<meta property="og:title" content="Presentación inicial · T2 micro:bit · CyR 1º ESO">
<meta property="og:description" content="Visita guiada a la micro:bit y a MakeCode para proyectar el primer día de clase.">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<style>
*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;overflow:hidden;font-family:system-ui,-apple-system,Segoe UI,sans-serif;background:#0F1C2E;color:#fff}
.slide{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:5vh 6vw;opacity:0;pointer-events:none;transition:.45s;background:radial-gradient(circle at 75% 25%,rgba(30,144,255,.25),transparent 32%),radial-gradient(circle at 20% 80%,rgba(255,59,59,.16),transparent 35%),#0F1C2E}
.slide.active{opacity:1;pointer-events:auto}.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.055) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.055) 1px,transparent 1px);background-size:48px 48px}
h1,h2.hero{font-size:clamp(56px,10vw,140px);line-height:1;margin:.1em 0;text-align:center}.orange{color:#ff8c1a}.blue{color:#59b4ff}h2{font-size:clamp(26px,4.2vw,54px);text-align:center;margin:.2em 0}p{font-size:clamp(18px,2.2vw,30px);max-width:1050px;text-align:center;color:#eaf2ff}.tag{font-family:monospace;color:#ffd166;border:1px solid rgba(255,209,102,.5);padding:.45rem 1rem;border-radius:999px;background:rgba(255,209,102,.1);z-index:2}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;max-width:1200px;width:100%;z-index:2;margin-top:1.3rem}.card{border:1px solid rgba(30,144,255,.45);border-radius:20px;padding:1rem 1.1rem;background:rgba(30,144,255,.14);font-size:clamp(14px,1.5vw,21px);text-align:center;line-height:1.4}.num{font-family:monospace;font-size:clamp(74px,12vw,180px);font-weight:900;color:#ff8c1a}.nav{position:absolute;right:2vw;bottom:2vh;display:flex;gap:.7rem;z-index:5}.nav button{width:48px;height:48px;border-radius:10px;border:1px solid #ffd166;background:rgba(255,209,102,.12);color:#fff;font-size:24px}.counter{position:absolute;left:2vw;bottom:3vh;color:rgba(255,255,255,.55);font-family:monospace;z-index:5}@media(max-width:800px){.cards{grid-template-columns:1fr 1fr}}
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

if __name__ == '__main__':
    html = (PAG.replace('{EXTRA}', CSS_EXTRA.strip())
               .replace('{SLIDES}', '\n'.join(SLIDES))
               .replace('{N}', '%02d' % len(SLIDES)))
    ruta = os.path.join(T2, 'presentacion.html')
    open(ruta, 'w', encoding='utf-8').write(html)
    print('  presentacion.html  %6d bytes · %d diapositivas' % (len(html), len(SLIDES)))

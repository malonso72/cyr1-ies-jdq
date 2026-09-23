# -*- coding: utf-8 -*-
"""Sesión 17 de T1 · Scratch: depuración.

Es la única sesión del trimestre en la que el alumnado no monta un programa desde cero:
abre cinco que **casi** funcionan y averigua qué les pasa. Los cinco fallos son los que
de verdad cometen en las dieciséis sesiones anteriores, y los cinco reaparecen en el
proyecto final.

Los mismos programas que se dibujan en la página se exportan al `.sb3` que se descarga
el alumnado (`materiales/depuracion.sb3`) y a la versión arreglada, que es privada
(`_soluciones/sb3/depuracion-resuelto.sb3`). No hay dos versiones que mantener: si se
toca un programa aquí, cambian la página, el archivo del alumno y el del profesor.

    python3 gen_s17_depuracion.py
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scratchsvg import hexa
from plantilla import pagina, caja, claves, pregunta, pista, ojo, logros, tabla
from comun import escribir, T1, REPO
from sb3 import Objeto, DISFRACES, proyecto, escribir_sb3

BANDERA = ('hat', 'events', ['al hacer clic en', ('icon', 'bandera')])
ROTACION = ('stack', 'motion', ['fijar estilo de rotación a', ('drop', 'no rotar')])


def ir_a(x, y):
    return ('stack', 'motion', ['ir a x:', ('num', str(x)), 'y:', ('num', str(y))])


def decir(texto, seg='2'):
    return ('stack', 'looks', ['decir', ('txt', texto), 'durante', ('num', seg), 'segundos'])


def si(cond, hijos):
    return ('c', 'control', ['si', cond, 'entonces'], hijos)


TOCA_BORDE = hexa('sensing', '¿tocando', ('drop', 'borde'), '?')
TOCA_RATON = hexa('sensing', '¿tocando', ('drop', 'puntero del ratón'), '?')

# ═══════════════════════════════════════════════════════════════════════════
# Los cinco. De cada uno, la versión rota (la que se entrega) y la arreglada.
# ═══════════════════════════════════════════════════════════════════════════

# 1 · Falta colocarse al empezar: cada partida arranca donde acabó la anterior.
ROTO1 = [
    BANDERA,
    ('stack', 'motion', ['mover', ('num', '80'), 'pasos']),
    decir('¡Ya estoy!', '1'),
]
BIEN1 = [BANDERA, ir_a(-120, 130)] + ROTO1[1:]

# 2 · Falta el estilo de rotación: al apuntar a la izquierda, el gato sale del revés.
ROTO2 = [
    BANDERA,
    ir_a(120, 65),
    ('stack', 'motion', ['apuntar en dirección', ('num', '-90')]),
    ('stack', 'motion', ['mover', ('num', '120'), 'pasos']),
]
BIEN2 = [BANDERA, ROTACION] + ROTO2[1:]

# 3 · Un lado de menos: el cuadrado no cierra.
CUERPO3 = [
    ('stack', 'motion', ['mover', ('num', '90'), 'pasos']),
    ('stack', 'control', ['esperar', ('num', '0.4'), 'segundos']),
    ('stack', 'motion', ['girar', ('icon', 'giro-d'), ('num', '90'), 'grados']),
]
ROTO3 = [
    BANDERA,
    ROTACION,
    ir_a(-45, -45),
    ('stack', 'motion', ['apuntar en dirección', ('num', '90')]),
    ('c', 'control', ['repetir', ('num', '3')], CUERPO3),
]
BIEN3 = ROTO3[:-1] + [('c', 'control', ['repetir', ('num', '4')], CUERPO3)]

# 4 · La comprobación está fuera del bucle: se mira una vez y ya no se mira más.
AVISO4 = [decir('¡He llegado al borde!')]
ROTO4 = [
    BANDERA,
    ROTACION,
    ir_a(-200, 0),
    ('stack', 'motion', ['apuntar en dirección', ('num', '90')]),
    si(TOCA_BORDE, AVISO4),
    ('c', 'control', ['por siempre'], [('stack', 'motion', ['mover', ('num', '5'), 'pasos'])]),
]
BIEN4 = ROTO4[:4] + [
    ('c', 'control', ['por siempre'], [
        ('stack', 'motion', ['mover', ('num', '5'), 'pasos']),
        si(TOCA_BORDE, AVISO4),
    ]),
]

# 5 · La variable no se pone a cero: la puntuación se hereda de la partida anterior.
CUERPO5 = [
    ('c', 'control', ['por siempre'], [
        si(TOCA_RATON, [
            ('stack', 'variables', ['sumar a', ('drop', 'Puntos'), ('num', '1')]),
            ('stack', 'control', ['esperar', ('num', '0.5'), 'segundos']),
        ]),
    ]),
]
ROTO5 = [BANDERA, ('stack', 'variables', ['mostrar variable', ('drop', 'Puntos')])] + CUERPO5
BIEN5 = ([BANDERA,
          ('stack', 'variables', ['dar a', ('drop', 'Puntos'), 'el valor', ('num', '0')]),
          ('stack', 'variables', ['mostrar variable', ('drop', 'Puntos')])] + CUERPO5)

SOSPECHOSOS = [
    ('SeVaSolo', 'nave', (-120, 130),
     'Avanza un poco y avisa de que ya está.',
     'La primera vez va bien. Pulsa la bandera cuatro o cinco veces seguidas y mira dónde '
     'acaba: cada partida empieza donde terminó la anterior, y al final se queda pegado al '
     'borde.',
     ROTO1, BIEN1, 420),
    ('CabezaAbajo', 'gato', (120, 65),
     'Va hacia la izquierda.',
     'Hacia la izquierda va, pero sale <strong>del revés</strong>, con las patas arriba. '
     'Y el bloque de mover no tiene nada raro.',
     ROTO2, BIEN2, 420),
    ('Cuadrado', 'jugador', (-45, -45),
     'Recorre un cuadrado y vuelve al punto de partida.',
     'Hace tres lados y se para mirando hacia arriba, lejos de donde salió. No cierra.',
     ROTO3, BIEN3, 460),
    ('NoAvisa', 'marciano', (-200, 0),
     'Avanza hasta el borde y avisa cuando llega.',
     'Avanza hasta el borde, se queda ahí clavado… y no dice nada. El bloque de decir está '
     'puesto y el texto está bien escrito.',
     ROTO4, BIEN4, 500),
    ('Marcador', 'pelota', (60, -120),
     'Suma un punto cada vez que lo tocas con el ratón, empezando de cero.',
     'Sumar, suma. El problema es el principio: juega una partida, pulsa la bandera otra vez '
     'y verás que la puntuación sigue donde la dejaste.',
     ROTO5, BIEN5, 520),
]

# ═══════════════════════════════════════════════════════════════════════════
# La página
# ═══════════════════════════════════════════════════════════════════════════
ARCHIVO = 'depuracion.sb3'
RUTA_MATERIAL = os.path.join(T1, 'materiales', ARCHIVO)


def ficha(i, datos):
    nombre, _disfraz, _pos, deberia, ves, roto, _bien, ancho = datos
    return (
        '<div style="margin:20px 0 26px;padding-left:16px;'
        'border-left:3px solid var(--bd,#E2E8F0)">'
        '<h3 style="margin:0 0 6px;font-size:1.05rem">%d · <code>%s</code></h3>'
        '<p><strong>Lo que debería hacer:</strong> %s</p>'
        '<p><strong>Lo que hace:</strong> %s</p>'
        '%s</div>'
        % (i, nombre, deberia, ves,
           caja(roto, 'Programa del objeto %s, con un fallo' % nombre, ancho=ancho)))


s17 = pagina(
    17, 'Depuración: encuentra el fallo',
    'Sesión 17 de Scratch: cinco programas que casi funcionan, un fallo en cada uno y el '
    'método para encontrarlo sin tocar bloques al azar. CyR 1º ESO.',
    'cinco programas arreglados y, sobre todo, <strong>un método</strong> para cuando el que '
    'falle sea el tuyo.',
    [
        ('Hoy no montas: arreglas',
         '<p>En las dieciséis sesiones anteriores has montado programas desde cero. Hoy te doy '
         'cinco <strong>hechos</strong>, y a los cinco les pasa algo. Ninguno da error ni se '
         'pone rojo: arrancan, hacen cosas… y no hacen lo que deberían. Ésos son los fallos '
         'de verdad, y los que te vas a encontrar la semana que viene en tu proyecto.</p>'
         '<p>La tentación, cuando algo no va, es cambiar bloques a ver si suena la flauta. '
         'Casi nunca sale, y de paso rompes lo que sí funcionaba. Se hace al revés:</p>' +
         claves([
             ('1. Mira lo que hace, no lo que querías que hiciera',
              'Descríbelo en voz alta: «avanza, llega al borde y se queda quieto». Media '
              'depuración es darse cuenta de qué está pasando de verdad.'),
             ('2. Prueba un trozo solo',
              'Haz clic directamente sobre un montón de bloques: se ejecuta ahí mismo, sin la '
              'bandera. Así sabes si el fallo está dentro de esos bloques o en cómo arrancan.'),
             ('3. Cambia una cosa cada vez',
              'Una, y pruebas. Si cambias tres a la vez y funciona, no sabrás cuál era — y si '
              'sigue fallando, tampoco.'),
         ])),

        ('Descarga los cinco',
         '<p>Los cinco programas están en un proyecto de Scratch que tienes que descargar:</p>'
         '<p style="text-align:center;margin:16px 0"><a class="bc" href="../materiales/%s" download>'
         '<span class="bi">📥</span><span class="bk">depuracion.sb3</span>'
         '<span class="bn">Los cinco objetos, con su fallo cada uno</span></a></p>'
         '<p>Para abrirlo en Scratch: <strong>Archivo → Cargar desde tu ordenador</strong>, y '
         'eliges el archivo que te acabas de descargar.</p>' % ARCHIVO +
         ojo('Lo que tengas abierto se pierde',
             '<p>Al cargar un proyecto, Scratch <strong>sustituye</strong> lo que hubiera en la '
             'pestaña. Si tenías algo tuyo sin descargar, descárgalo antes.</p>') +
         '<p>Cada objeto de la lista es un sospechoso. Al pulsar la bandera arrancan los cinco '
         'a la vez, así que trabaja <strong>de uno en uno</strong>: selecciona el objeto y haz '
         'clic sobre su montón de bloques para probarlo solo.</p>'),

        ('Los cinco sospechosos',
         '<p>De cada uno te digo qué debería hacer y qué hace. Lo que falta es el porqué.</p>' +
         ''.join(ficha(i + 1, d) for i, d in enumerate(SOSPECHOSOS))),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Un personaje tuyo debería avisar cuando toca al enemigo, y no avisa '
                       'nunca. El bloque <em>si …  entonces</em> está puesto y la condición es '
                       'la correcta. ¿Qué miras primero?',
                  [('otro', 'Cambio el bloque de decir por uno de sonido, por si acaso',
                    'No: eso es cambiar cosas a ver si suena la flauta. Además, si el aviso no '
                    'llega a ejecutarse, dará igual que sea un decir o un sonido.'),
                   ('dentro', 'Si ese <em>si</em> está dentro de un <em>por siempre</em> o '
                    'suelto debajo de la bandera',
                    'Correcto. Un <em>si</em> suelto se comprueba <strong>una sola vez</strong>, '
                    'en el instante en que arranca el programa; si en ese momento no se tocaban, '
                    'no vuelve a mirarse nunca más. Para vigilar algo hay que preguntarlo una y '
                    'otra vez, y eso es meterlo dentro del bucle.'),
                   ('borrar', 'Borro el programa y lo monto otra vez desde el principio',
                    'Es lo último, no lo primero: tardas mucho y lo más probable es que vuelvas '
                    'a cometer el mismo fallo, porque no habrás llegado a saber cuál era.')],
                  'dentro')),

        ('Tu actividad',
         '<p><strong>Arregla los cinco.</strong> Uno por uno: lo pruebas, averiguas qué le pasa, '
         'lo corriges y lo vuelves a probar hasta que haga lo que promete la ficha.</p>'
         '<p>Y apunta lo que has hecho. Por cada objeto, <strong>una línea</strong>: qué le '
         'pasaba y qué bloque tocaste. Eso es lo que se entrega junto al proyecto, y es lo que '
         'de verdad demuestra que lo has entendido.</p>' +
         tabla(['Objeto', 'Qué le pasaba', 'Qué hice'],
               [[('<code>%s</code>' % d[0]), '…', '…'] for d in SOSPECHOSOS]) +
         pista('¿Te has atascado? Abre las pistas',
               '<p>No son las soluciones: son el sitio donde mirar.</p>'
               '<ul>'
               '<li><code>SeVaSolo</code> — ¿de dónde sale? ¿Quién le dice dónde empieza?</li>'
               '<li><code>CabezaAbajo</code> — el problema no es el movimiento, es el dibujo. '
               'Hay un bloque de Movimiento que decide si el disfraz gira o no.</li>'
               '<li><code>Cuadrado</code> — cuenta los lados que hace y los que tiene un '
               'cuadrado.</li>'
               '<li><code>NoAvisa</code> — ¿cuántas veces se ejecuta ese <em>si</em>? '
               'Míralo con atención: ¿está dentro de algo o está suelto?</li>'
               '<li><code>Marcador</code> — no falla al sumar, falla al empezar. ¿Qué vale '
               '<em>Puntos</em> justo antes de que sumes el primero?</li>'
               '</ul>')),

        ('Lo has conseguido si…',
         logros(['Los cinco hacen lo que promete su ficha.',
                 '<code>SeVaSolo</code> empieza en el mismo sitio aunque pulses la bandera diez '
                 'veces.',
                 '<code>Marcador</code> vuelve a cero en cada partida.',
                 'Tienes escrita una línea por objeto: qué le pasaba y qué tocaste.',
                 'Sabrías explicarle a un compañero la diferencia entre un <em>si</em> suelto y '
                 'un <em>si</em> dentro de un <em>por siempre</em>.'])),
    ],
    entrega='<ol>'
            '<li><strong>Archivo → Guardar en tu ordenador.</strong> Se descarga un '
            '<code>.sb3</code> a tu carpeta <strong>Descargas</strong>.</li>'
            '<li>Cámbiale el nombre a <strong>Sesion17_TuNombre.sb3</strong>.</li>'
            '<li>Súbelo a la tarea de <strong>Moodle</strong> de la sesión 17, junto con las '
            '<strong>cinco líneas</strong> de la tabla: qué le pasaba a cada uno y qué '
            'tocaste.</li></ol>')

escribir(17, s17)


# ═══════════════════════════════════════════════════════════════════════════
# Los dos .sb3: el del alumnado (roto) y el del profesor (arreglado)
# ═══════════════════════════════════════════════════════════════════════════
def construir(indice_programa):
    objetos = []
    for nombre, disfraz, (x, y), _d, _v, roto, bien, _a in SOSPECHOSOS:
        programa = [roto, bien][indice_programa]
        objetos.append(Objeto(nombre, [DISFRACES[disfraz]], [programa], x=x, y=y, tamano=70))
    return proyecto(objetos, variables_iniciales={'Puntos': 0})


if __name__ == '__main__':
    os.makedirs(os.path.dirname(RUTA_MATERIAL), exist_ok=True)
    pj, assets = construir(0)
    n = escribir_sb3(RUTA_MATERIAL, pj, assets)
    print('  %-26s %6d bytes · el que se descarga el alumnado' % (ARCHIVO, n))

    destino = os.path.join(REPO, '_soluciones', 'sb3')
    os.makedirs(destino, exist_ok=True)
    pj, assets = construir(1)
    n = escribir_sb3(os.path.join(destino, 'depuracion-resuelto.sb3'), pj, assets)
    print('  %-26s %6d bytes · privado, con los cinco arreglados'
          % ('depuracion-resuelto.sb3', n))

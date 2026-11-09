# -*- coding: utf-8 -*-
"""Sesiones 12 a 16 de T1 · Scratch: laberinto, piedra-papel-tijera y Pong."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scratchsvg import op, var, rep, hexa, tecla
from plantilla import pagina, caja, dos_cajas, pasos, secuencia, claves, pregunta, pista, ojo, logros, tabla
from comun import escribir, GUIA

BANDERA = ('hat', 'events', ['al hacer clic en', ('icon', 'bandera')])
RESP = rep('sensing', 'respuesta')
NEGRO = '#1A1A1A'


def guia(archivo, nombre):
    return ('<a href="%s%s" class="bc"><span class="bi">📕</span>'
            '<span class="bk">Guía en PDF</span><span class="bn">%s</span></a>'
            % (GUIA, archivo, nombre))


def si(cond, hijos):
    return ('c', 'control', ['si', cond, 'entonces'], hijos)


# ============================================================ S12
# S12 en dos clases (Manuel, 09-11-2026): la Parte 1 es dibujar la carretera (su primer
# dibujo en Scratch, con capturas paso a paso) y la Parte 2 programar el coche sobre un
# fondo común que se descarga de la página. Antes era un laberinto negro: la estrella de la
# biblioteca tiene el contorno negro y devolvía al gato a la salida. Ahora salirse es tocar
# el verde del césped, que no tiene ningún objeto.
VERDE12 = '#4CAF50'
SALIDA12 = [('stack', 'motion', ['ir a x:', ('num', '-200'), 'y:', ('num', '-120')])]
MOV12 = [
    BANDERA,
    ('stack', 'looks', ['fijar tamaño al', ('num', '35'), '%']),
    ('stack', 'motion', ['fijar estilo de rotación a', ('drop', 'izquierda-derecha')]),
    ('stack', 'motion', ['apuntar en dirección', ('num', '90')]),
] + SALIDA12 + [
    ('c', 'control', ['por siempre'], [
        si(tecla('flecha derecha'), [('stack', 'motion', ['apuntar en dirección', ('num', '90')]),
                                     ('stack', 'motion', ['sumar a x', ('num', '3')])]),
        si(tecla('flecha izquierda'), [('stack', 'motion', ['apuntar en dirección', ('num', '-90')]),
                                       ('stack', 'motion', ['sumar a x', ('num', '-3')])]),
        si(tecla('flecha arriba'), [('stack', 'motion', ['sumar a y', ('num', '3')])]),
        si(tecla('flecha abajo'), [('stack', 'motion', ['sumar a y', ('num', '-3')])]),
    ]),
]
CESPED12 = [
    si(hexa('sensing', '¿tocando el color', ('color', VERDE12), '?'),
       [('stack', 'sound', ['iniciar sonido', ('drop', 'pop')])] + SALIDA12 +
       [('stack', 'motion', ['apuntar en dirección', ('num', '90')])]),
]

IMG12 = '../img/s12/'


def captura(arch, alt):
    """Captura del editor de Scratch, para la Parte 1 (su primer dibujo)."""
    return ('<figure style="margin:10px 0 4px"><img class="captura" src="%s%s" alt="%s" '
            'loading="lazy" style="display:block;max-width:100%%;height:auto;border:1px solid '
            '#CFD8DC;border-radius:8px"><figcaption style="font-size:.85rem;color:#555D6B;'
            'margin-top:4px">%s</figcaption></figure>' % (IMG12, arch, alt, alt))


def sub1(n, tit):
    """Apartado de la Parte 1. No lleva la clase «sub»: esos son los de «Tu actividad»."""
    return ('<h3 style="font-family:\'Barlow Condensed\',sans-serif;font-size:1.18rem;'
            'color:#1B4F8A;margin:22px 0 8px"><span style="display:inline-block;min-width:2.4em;'
            'margin-right:6px;padding:1px 7px;border-radius:6px;background:#1B4F8A;color:#fff;'
            'font-size:.95rem;text-align:center">1.%d</span>%s</h3>\n' % (n, tit))


VERDE_TXT = '<strong>Color 35, Saturación 80, Brillo 70</strong>'

PARTE1 = (
    '<p><strong>Hoy dibujas el fondo del juego:</strong> un césped verde y una carretera gris '
    'por la que circulará un coche en la Parte 2. Es la primera vez que dibujas en Scratch: '
    'sigue los pasos en orden y mira cada imagen. Lo marcado en <strong>rojo</strong> es lo '
    'que tienes que pulsar.</p>\n'
    + sub1(1, 'Pinta el césped y la carretera')
    + pasos([
        'Abajo a la derecha, haz clic en <strong>Escenario</strong>. A partir de ahora lo que '
        'dibujes será el fondo, no un objeto.' + captura('p1-escenario.jpg', 'El Escenario, abajo a la derecha'),
        'Arriba, abre la pestaña <strong>Fondos</strong>. Verás el fondo en blanco, «backdrop1».',
        'Abajo, pulsa <strong>Convertir a mapa de bits</strong>. Así el bote de pintura rellena '
        'todo el fondo de un solo clic.'
        + captura('p2-fondos-mapa-bits.jpg', 'La pestaña Fondos (arriba) y el botón Convertir a mapa de bits (abajo)'),
        'Elige la herramienta <strong>Rellenar</strong> (el bote de pintura). Haz clic en el '
        'cuadrado de color de <strong>Rellenar</strong>, arriba, y mueve las tres barras hasta '
        + VERDE_TXT + '. Es el verde del césped.'
        + captura('p3-verde.jpg', 'El verde del césped: Color 35, Saturación 80, Brillo 70'),
        'Haz clic una vez dentro del recuadro de dibujo. Todo el fondo se vuelve verde.'
        + captura('p4-cesped.jpg', 'Con el bote, un clic y el fondo entero queda verde'),
        'Elige la herramienta <strong>Rectángulo</strong> y comprueba que arriba está marcado '
        '<strong>Relleno</strong>, no Contorneado.',
        'Cambia el color de <strong>Rellenar</strong> a gris: <strong>Saturación 0, Brillo 50</strong>. '
        'Cuando la saturación es 0, el Color da igual.'
        + captura('p5-gris.jpg', 'El gris de la carretera: Saturación 0, Brillo 50'),
        'Dibuja el primer tramo: pincha abajo a la izquierda y, sin soltar, arrastra hasta la '
        'derecha. Debe ocupar todo el ancho del fondo y, de alto, más o menos <strong>una cuarta '
        'parte</strong> del fondo. Si es más estrecho, el coche no cabrá.'
        + captura('p6-rect1.jpg', 'El primer tramo, de izquierda a derecha y abajo'),
        'Dibuja otros dos tramos del mismo ancho: uno <strong>vertical</strong> a la derecha, de '
        'abajo arriba, y otro <strong>horizontal arriba</strong>, de derecha a izquierda. Cada '
        'tramo tiene que <strong>montarse</strong> un poco sobre el anterior: si entre dos tramos '
        'queda una rendija verde, el coche chocará ahí.'
        + captura('p7-tres.jpg', 'Los tres tramos: abajo, a la derecha y arriba'),
    ])
    + ojo('Si te equivocas',
          '<p style="margin-bottom:0">Pulsa la flecha de <strong>deshacer</strong> (arriba, junto '
          'al nombre «backdrop1») tantas veces como haga falta. Deshace los pasos de uno en '
          'uno.</p>')
    + sub1(2, 'Marca la salida y la raya del centro')
    + pasos([
        'Antes de cambiar de color, <strong>haz clic fuera del recuadro de dibujo</strong>, en la '
        'zona de alrededor.',
        'Cambia el color de <strong>Rellenar</strong> a blanco: <strong>Saturación 0, Brillo 100</strong>.',
        'Con el <strong>Rectángulo</strong>, dibuja la línea de salida: un rectángulo muy estrecho '
        'que cruce el tramo de abajo, cerca del borde izquierdo.',
        'Dibuja la raya del centro con rectángulos pequeños y alargados, separados entre sí, '
        'siguiendo los tres tramos. Haz clic fuera del dibujo después de cada uno.',
    ])
    + ojo('El rectángulo recién dibujado sigue seleccionado',
          '<p>Hasta que haces clic fuera, el último rectángulo sigue seleccionado, con puntitos '
          'azules alrededor. Si cambias el color en ese momento, <strong>cambia el color de ese '
          'rectángulo</strong>, no el del siguiente. Aquí el tramo de arriba se ha vuelto blanco '
          'por eso. Se arregla con <em>deshacer</em>, o con el bote de pintura en gris sobre el '
          'tramo.</p>' + captura('p8-ojo.jpg', 'El tramo de arriba se ha vuelto blanco al cambiar de color sin hacer clic fuera'))
    + captura('p9-final.jpg', 'Así queda: césped, carretera, salida y raya del centro')
    + sub1(3, 'Dibuja un segundo fondo más difícil')
    + '<p>Un segundo fondo, con una carretera más difícil. Esta la diseñas tú.</p>'
    + pasos([
        'En la pestaña <strong>Fondos</strong>, abajo a la izquierda, pasa el ratón por el botón '
        'del fondo y elige el <strong>pincel</strong> (<strong>Pinta</strong>): aparece un fondo '
        'nuevo en blanco, «backdrop2».',
        'Conviértelo a mapa de bits y pinta el césped igual que en el 1.1.',
        'Dibuja una carretera con <strong>al menos cinco tramos</strong>, más difícil que la '
        'primera: más giros o tramos más estrechos, pero que el coche quepa.',
        'Marca la salida y la raya del centro igual que en el 1.2.',
    ])
    + '<h3 style="margin-top:20px">Lo has conseguido si…</h3>'
    + logros(['No queda nada blanco en el fondo: todo es césped o carretera.',
              'La carretera es continua: no hay rendijas verdes entre los tramos.',
              'Los tramos son anchos, más o menos una cuarta parte del fondo.',
              'La salida y la raya del centro están dibujadas (apartado 1.2).',
              'Hay un segundo fondo con una carretera de al menos cinco tramos (apartado 1.3).'])
    + '<div style="border:2px solid #1A6B3A;background:#F0F9F3;border-radius:10px;padding:14px 18px;margin:18px 0">'
      '<h3 style="margin:0 0 8px">📤 Qué tienes que entregar hoy</h3>'
      '<div style="margin:0 0 10px;padding:8px 12px;background:#fff;border:1.5px solid #1A6B3A;border-radius:8px">'
      '<p style="margin:0 0 6px"><strong>Cómo se valora.</strong> Todo va en el mismo archivo. Un '
      'apartado cuenta si está hecho; a medias no suma.</p>'
      '<table style="border-collapse:collapse;margin:6px 0 8px;font-size:.95rem"><thead><tr>'
      '<th style="border:1px solid #BFD8C6;padding:5px 10px;background:#E3F2E8;color:#1A6B3A;text-align:left">Lo que entregas hecho</th>'
      '<th style="border:1px solid #BFD8C6;padding:5px 10px;background:#E3F2E8;color:#1A6B3A">Nota</th></tr></thead><tbody>'
      + ''.join('<tr><td style="border:1px solid #BFD8C6;padding:5px 10px">%s</td><td style="border:1px '
                'solid #BFD8C6;padding:5px 10px;text-align:center;font-weight:700;color:#1A6B3A">%s</td></tr>' % f
                for f in (('1.1', '5'), ('1.1 y 1.2', '8'), ('1.1, 1.2 y 1.3', '10')))
    + '</tbody></table><p style="margin:0">Sin el 1.1 hecho no hay nota, aunque estén los demás: lo repites.</p></div>'
      '<ol style="margin:0;padding-left:20px"><li><strong>Archivo → Guardar en tu ordenador.</strong> '
      'Se descarga un archivo <code>.sb3</code> en tu carpeta <strong>Descargas</strong>.</li>'
      '<li>Cámbiale el nombre a <strong>Sesion12-1_TuNombre.sb3</strong>.</li>'
      '<li>Súbelo a la tarea de <strong>Moodle</strong> «S12 · Parte 1».</li></ol></div>'
)

PARTE2 = (
    '<h2 style="margin-top:34px;padding:10px 14px;background:#1B4F8A;color:#fff;border-radius:10px">'
    'Parte 2 · Programa el coche</h2>\n'
    '<p><strong>En la segunda clase</strong> todos usáis <strong>el mismo fondo</strong>, este. '
    'Descárgalo y cárgalo en Scratch como se explica en el 5.1.</p>\n'
    '<figure style="margin:10px 0"><img class="captura" src="../materiales/carretera.svg" '
    'alt="El fondo común de la carretera" style="display:block;width:100%;max-width:480px;'
    'height:auto;border:1px solid #CFD8DC;border-radius:8px"></figure>\n'
    '<a class="abrir-scratch" href="../materiales/carretera.svg" download="carretera.svg">'
    '📥 Descargar el fondo de la carretera</a>'
)

s12 = pagina(
    12, 'Carretera',
    'Sesión 12 de Scratch, en dos clases: dibujar una carretera en el editor de pintura y '
    'programar un coche que la recorre sin salirse, con sumar a x e y y ¿tocando el color? CyR 1º ESO.',
    'un <strong>juego de carreras</strong> en dos clases: en la primera <strong>dibujas la '
    'carretera</strong>; en la segunda <strong>programas un coche</strong> que la recorre sin '
    'salirse al césped.',
    [
        ('Parte 1 · Dibuja la carretera', PARTE1),
        (None, PARTE2),
        ('Dos bloques nuevos y una idea',
         claves([
             ('sumar a x (3) y sumar a y (3)',
              'Mueven el objeto en horizontal y en vertical sin girarlo. Para recorrer una '
              'carretera de tramos rectos van mejor que <em>mover</em>, porque el coche no tiene '
              'que girar para subir o bajar.'),
             ('¿tocando el color ( )?',
              'Una condición de Sensores que mira si el objeto está pisando un color concreto de '
              'la pantalla. Así se entera el programa de que el coche se ha salido.'),
             ('Y la idea',
              'En Scratch los bordes de la carretera no existen. Lo que hay es un dibujo verde y '
              'un programa que dice «si estás tocando el verde, vuelve a la salida». Para el '
              'jugador el efecto es el mismo.'),
         ])
         + '<p>El <strong>estilo de rotación izquierda-derecha</strong> ya lo conoces de sesiones '
           'anteriores: con él, al apuntar a -90 el coche mira a la izquierda en vez de ponerse '
           'boca abajo.</p>'),

        ('Lee estos dos trozos',
         '<p>Primero, el movimiento. Cuatro condicionales, uno por flecha, dentro de un <em>por '
         'siempre</em> que los vigila todo el rato:</p>'
         + caja(MOV12, 'Programa del coche: fijar tamaño al 35 por ciento, estilo de rotación '
                       'izquierda-derecha, apuntar a 90, ir a la salida y, por siempre, cuatro '
                       'condicionales que mueven el coche según la flecha pulsada')
         + '<p>Y ahora el césped. Este trozo va dentro del mismo <em>por siempre</em>, debajo de '
           'los cuatro anteriores:</p>'
         + caja(CESPED12, 'Condicional: si está tocando el verde del césped, iniciar el sonido '
                          'pop, volver a la salida y apuntar a 90',
                pie='Si tocas el césped, vuelves a la salida. Es el castigo clásico de los juegos '
                    'de carreras, y se resuelve con un solo condicional.')
         + secuencia([
             'Al pulsar la bandera, el coche se pone a su tamaño, mirando a la derecha y en la '
             'salida.',
             'El <em>por siempre</em> mira las cuatro flechas una y otra vez. La que esté pulsada '
             'mueve el coche 3 pasos en su sentido; las de izquierda y derecha, además, lo giran '
             'hacia donde va.',
             'En cada vuelta mira también si el coche pisa el verde. Si lo pisa, suena y lo '
             'devuelve a la salida mirando a la derecha.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Pones el condicional del césped y, al probarlo, el coche atraviesa el '
                       'césped como si nada. ¿Cuál es la causa más probable?',
                  [('color', 'El verde del bloque no es exactamente el mismo que el del césped',
                    'Casi seguro que es esto. El bloque compara colores <b>exactos</b>. Hay que '
                    'abrir el cuadradito de color del bloque, elegir el <b>cuentagotas</b> y pinchar '
                    'directamente sobre el césped del escenario.'),
                   ('fondo', 'El bloque sólo detecta objetos, no dibujos del fondo',
                    'No. <em>¿tocando el color?</em> mira los píxeles de la pantalla, vengan del '
                    'fondo o de otro objeto. Justamente por eso sirve para una carretera pintada.'),
                   ('siempre', 'Falta un segundo por siempre para el césped',
                    'No hace falta. El condicional del césped va dentro del mismo <em>por '
                    'siempre</em> que las flechas, y así se comprueba en cada vuelta.')],
                  'color')),

        ('Tu actividad',
         pasos([
             'Carga el fondo común: abajo a la derecha, pasa el ratón por el botón de '
             '<strong>Fondos</strong> y elige <strong>Cargar fondo</strong>. Abre el archivo '
             '<strong>carretera.svg</strong> que has descargado (está en tu carpeta '
             '<strong>Descargas</strong>).',
             'Borra el gato y añade el coche: botón <strong>Elige un objeto</strong>, escribe '
             '<strong>Convertible</strong> y elige el descapotable morado.',
             'Monta en el coche los dos trozos de arriba: el movimiento y, dentro del mismo '
             '<em>por siempre</em>, debajo de los cuatro <em>si</em>, el condicional del césped.',
             'El verde del bloque <em>¿tocando el color?</em> se coge con el '
             '<strong>cuentagotas</strong>: haz clic en el color del bloque, después en el '
             'cuentagotas, y pincha en el césped del escenario. No lo elijas a ojo.',
             'Prueba: el coche recorre la carretera de la salida al final. Si toca el césped, '
             'suena y vuelve a la salida. En las esquinas, llega hasta el centro del tramo y '
             'entonces gira.'])),

        ('Lo has conseguido si…',
         logros(['El coche se mueve con las cuatro flechas y mira hacia donde va.',
                 'Al tocar el césped suena y vuelve a la salida.',
                 'Se puede recorrer toda la carretera, de la salida al final, sin salirse.'])),
    ],
    entrega=('<p style="margin:0 0 10px;"><strong>Antes de nada:</strong> como no usamos cuenta '
             'de Scratch, tu proyecto sólo existe en esta pestaña. Si la cierras sin descargarlo, '
             '<strong>se pierde</strong>.</p>\n<ol>\n'
             '  <li><strong>Archivo → Guardar en tu ordenador.</strong> Se descarga un archivo '
             '<code>.sb3</code> que aparece en tu carpeta <strong>Descargas</strong>.</li>\n'
             '  <li>Cámbiale el nombre a <strong>Sesion12-2_TuNombre.sb3</strong>.</li>\n'
             '  <li>Súbelo a la tarea de <strong>Moodle</strong> «S12 · Parte 2».</li>\n</ol>'))


# ============================================================ S13
META13 = [
    si(hexa('sensing', '¿tocando', ('drop', 'Meta'), '?'),
       [('stack', 'looks', ['decir', op('unir', ('txt', 'Has tardado '),
                                        rep('sensing', 'cronómetro')),
                            'durante', ('num', '3'), 'segundos']),
        ('cap', 'control', ['detener', ('drop', 'todos')])]),
]
CRONO13 = [
    BANDERA,
    ('stack', 'sensing', ['reiniciar cronómetro']),
    ('stack', 'looks', ['cambiar fondo a', ('drop', 'nivel1')]),
]
NIVEL13 = [
    si(hexa('sensing', '¿tocando', ('drop', 'Meta'), '?'),
       [('stack', 'looks', ['cambiar fondo a', ('drop', 'nivel2')]),
        ('stack', 'motion', ['ir a x:', ('num', '-200'), 'y:', ('num', '-140')]),
        ('stack', 'variables', ['sumar a', ('drop', 'Nivel'), ('num', '1')])]),
]

s13 = pagina(
    13, 'Laberinto II',
    'Sesión 13 de Scratch: añadir meta, cronómetro y un segundo nivel al laberinto. '
    'CyR 1º ESO.',
    'que tu laberinto se pueda <strong>ganar</strong>: con meta, con tiempo y con un segundo nivel.',
    [
        ('La meta',
         '<p>Un laberinto sin meta es un pasillo. Crea un objeto nuevo —una bandera, una estrella, '
         'un trozo de queso— llámalo <strong>Meta</strong> y ponlo al final del recorrido.</p>'
         '<p>Este condicional va dentro del <strong>por siempre</strong> del personaje, junto a los '
         'que ya tenías:</p>' +
         caja(META13, 'Condicional: si está tocando el objeto Meta, decir Has tardado seguido del '
                      'cronómetro durante 3 segundos y detener todos',
              pie='<strong>cronómetro</strong> es un informador de Sensores: cuenta segundos desde '
                  'que se reinició. No hay que crearlo, ya existe.')),

        ('El cronómetro',
         '<p>El cronómetro corre solo desde que se abre Scratch, así que hay que ponerlo a cero al '
         'empezar la partida. Este es el arranque completo:</p>' +
         caja(CRONO13, 'Programa de arranque: al hacer clic en la bandera, reiniciar cronómetro y '
                       'cambiar el fondo a nivel1', ancho=420)),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Por error colocas el <em>detener (todos)</em> <strong>antes</strong> del '
                       'bloque que dice «Has tardado…». ¿Qué ve el jugador al llegar a la meta?',
                  [('mensaje', 'El mensaje, y después el juego se para',
                    'No. Los bloques se ejecutan de arriba abajo, y <em>detener todos</em> apaga el '
                    'programa en el momento en que le llega el turno.'),
                   ('nada', 'Nada: el juego se para sin decir nada',
                    'Correcto. El programa muere en el <em>detener</em> y nunca llega al bloque de '
                    'debajo. Por eso <b>detener (todos) va siempre el último</b>.'),
                   ('siempre', 'El mensaje se queda en pantalla para siempre',
                    'Eso pasaría con <em>decir (…)</em> sin duración, que es otro bloque distinto. '
                    'Aquí el problema es el orden.')],
                  'nada')),

        ('Tu actividad',
         pasos([
             'Añade la meta: botón <strong>Elige un objeto</strong>, escribe <strong>Crystal</strong> '
             'y elige <strong>Crystal</strong>. Cámbiale el nombre a <strong>Meta</strong> en la '
             'casilla <em>Objeto</em>, debajo del escenario, y colócala al final del laberinto.',
             'Añade el condicional de la meta y comprueba que el juego termina y dice el tiempo.',
             'Añade <strong>reiniciar cronómetro</strong> al arranque. Juega dos veces seguidas y '
             'comprueba que el tiempo empieza de cero las dos.',
             'Dibuja un <strong>segundo fondo</strong> con un laberinto más difícil. Los fondos se '
             'crean igual que el primero, con el botón de abajo a la derecha.',
             'Crea la variable <strong>Nivel</strong> y añade al arranque, justo debajo de '
             '<em>reiniciar cronómetro</em>, el bloque <strong>dar a (Nivel) el valor (1)</strong>. '
             'Si no lo pones, la segunda partida empieza en el nivel donde acabó la primera: es el '
             'mismo fallo del marcador de la sesión 9.',
             'Cambia el condicional de la meta para que, en vez de terminar, pase al nivel 2:']) +
         caja(NIVEL13, 'Condicional: si está tocando la Meta, cambiar el fondo a nivel2, volver a '
                       'la salida y sumar 1 a la variable Nivel',
              pie='Acuérdate de <strong>mover el objeto Meta</strong> al final del segundo '
                  'laberinto: cambiar el fondo no lo cambia a él de sitio.') +
         pista('¿Y cómo hago que en el nivel 2 termine de verdad?',
               '<p>Con la variable <strong>Nivel</strong> que has creado en el paso 5. En vez de mirar sólo '
               'si tocas la Meta, mira <em>además</em> en qué nivel estás: si <code>Nivel</code> '
               'vale 2, el juego termina; si vale 1, pasa al siguiente fondo.</p>'
               '<p style="margin-bottom:0">Para juntar dos condiciones en una se usa el operador '
               'verde <strong>&lt; &gt; y &lt; &gt;</strong>, que tiene dos huecos hexagonales.</p>')),

        ('Lo has conseguido si…',
         logros(['Al llegar a la meta pasa algo: mensaje, sonido o cambio de nivel.',
                 'El cronómetro empieza en cero en cada partida.',
                 'Al volver a jugar se empieza otra vez en el nivel 1.',
                 'Hay dos niveles con laberintos distintos.',
                 'El juego termina de verdad al acabar el último nivel.',
                 'Sabrías explicar por qué <em>detener (todos)</em> va siempre al final.'])),
    ],
    nav_extra=guia('ejercicio-de-juego-laberinto.pdf', 'Laberinto, material de apoyo'))

# ============================================================ S14
P14 = [
    BANDERA,
    ('stack', 'variables', ['dar a', ('drop', 'sorteo'), 'el valor',
                            op('número aleatorio entre', ('num', '1'), 'y', ('num', '3'))]),
    si(hexa('operators', var('sorteo'), '=', ('num', '1')),
       [('stack', 'variables', ['dar a', ('drop', 'maquina'), 'el valor', ('txt', 'piedra')])]),
    si(hexa('operators', var('sorteo'), '=', ('num', '2')),
       [('stack', 'variables', ['dar a', ('drop', 'maquina'), 'el valor', ('txt', 'papel')])]),
    si(hexa('operators', var('sorteo'), '=', ('num', '3')),
       [('stack', 'variables', ['dar a', ('drop', 'maquina'), 'el valor', ('txt', 'tijera')])]),
    ('stack', 'sensing', ['preguntar', ('txt', 'piedra, papel o tijera'), 'y esperar']),
    ('stack', 'looks', ['decir', op('unir', ('txt', 'Yo he sacado '), var('maquina')),
                        'durante', ('num', '2'), 'segundos']),
    ('ce', 'control', ['si', hexa('operators', RESP, '=', var('maquina')), 'entonces'],
     [('stack', 'looks', ['decir', ('txt', '¡Empate!'), 'durante', ('num', '2'), 'segundos'])],
     ['si no'],
     [('stack', 'looks', ['decir', ('txt', 'Uno de los dos ha ganado…'),
                          'durante', ('num', '2'), 'segundos'])]),
]
GANA14 = [
    si(hexa('operators',
            hexa('operators', RESP, '=', ('txt', 'piedra')), 'y',
            hexa('operators', var('maquina'), '=', ('txt', 'tijera'))),
       [('stack', 'looks', ['decir', ('txt', '¡Ganas tú!'), 'durante', ('num', '2'), 'segundos']),
        ('stack', 'variables', ['sumar a', ('drop', 'MisPuntos'), ('num', '1')])]),
]

s14 = pagina(
    14, 'Piedra, papel o tijera',
    'Sesión 14 de Scratch: azar, comparación de textos y el operador y. Un juego contra el '
    'ordenador. CyR 1º ESO.',
    'un juego <strong>contra el ordenador</strong> en el que él elige a la vez que tú y sin hacer '
    'trampas.',
    [
        ('Cómo elige el ordenador',
         '<p>El ordenador no sabe sacar «piedra»: sabe sacar <strong>números</strong>. Así que se '
         'hace en dos pasos: primero se sortea un número del 1 al 3, y después se traduce a '
         'palabra.</p>'
         '<p>Es un truco que vas a usar muchas veces: <em>los ordenadores manejan números; las '
         'palabras se las ponemos nosotros encima</em>.</p>'),

        ('Lee este programa',
         caja(P14, 'Programa: sortear un número entre 1 y 3 en la variable sorteo, traducirlo a '
                   'piedra, papel o tijera en la variable maquina, preguntar al jugador, anunciar '
                   'la jugada de la máquina y, si coinciden, decir ¡Empate!, si no, decir que uno '
                   'de los dos ha ganado') +
         secuencia([
             'Se sortea <code>sorteo</code>: 1, 2 o 3.',
             'Los tres condicionales traducen ese número a una palabra en <code>maquina</code>. '
             'Sólo uno de los tres se cumple.',
             'Se pregunta al jugador <em>después</em> del sorteo, pero eso no es trampa: el '
             'ordenador ya había decidido y no puede cambiar.',
             'Se anuncia la jugada de la máquina.',
             'El último condicional compara las dos jugadas. De momento sólo sabe detectar el '
             'empate — lo demás lo vas a añadir tú.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'En una partida, ¿cuántas combinaciones distintas pueden salir?',
                  [('tres', '3, una por cada jugada posible',
                    'No: 3 son las jugadas de <b>uno</b> de los dos. Hay que contar las de los dos '
                    'a la vez.'),
                   ('nueve', '9',
                    'Correcto: 3 jugadas tuyas × 3 de la máquina. Pero fíjate en algo importante: '
                    '<b>no hacen falta 9 condicionales</b>. Con uno resuelves los 3 empates, y de '
                    'las 6 que quedan basta con comprobar las 3 en las que ganas tú; si no ganas y '
                    'no empatas, has perdido.'),
                   ('seis', '6, quitando los empates',
                    'Los empates también son resultados posibles. Son 9 en total, de los cuales 3 '
                    'son empate.')],
                  'nueve')),

        ('Tu actividad',
         pasos([
             'Monta el programa tal cual y comprueba que detecta los empates.',
             'Añade los <strong>tres casos en los que ganas tú</strong>: piedra vence a tijera, '
             'papel vence a piedra, tijera vence a papel.',
             'Si no es empate y no has ganado, entonces has perdido. No hace falta comprobarlo: '
             'basta con un <em>si no</em>.',
             'Crea las variables <code>MisPuntos</code> y <code>SusPuntos</code> y lleva el marcador.',
             '<strong>Reto:</strong> mete todo dentro de un <em>repetir hasta que</em> que termine '
             'cuando alguno llegue a 3 puntos.']) +
         caja(GANA14, 'Condicional con el operador y: si la respuesta es piedra y la máquina sacó '
                      'tijera, decir ¡Ganas tú! y sumar un punto',
              pie='El operador verde <strong>&lt;&gt; y &lt;&gt;</strong> junta dos condiciones: '
                  'sólo vale «sí» cuando <em>las dos</em> se cumplen a la vez.') +
         ojo('Cuidado con lo que escribe el jugador',
             '<p>El programa compara textos, así que «Piedra» con mayúscula, «piedra » con un '
             'espacio detrás o «tijeras» en plural <strong>no coinciden</strong> y el juego dirá '
             'que has perdido.</p>'
             '<p style="margin-bottom:0">Por eso el bloque de preguntar dice exactamente qué hay '
             'que escribir. Si quieres afinar, hay quien pide un número (1, 2 o 3) en vez de una '
             'palabra: menos bonito, pero mucho más difícil de equivocar.</p>')),

        ('Lo has conseguido si…',
         logros(['La máquina saca una jugada distinta cada partida.',
                 'El juego distingue correctamente ganar, perder y empatar.',
                 'Hay un marcador para los dos jugadores.',
                 'Has usado el operador <em>y</em> al menos tres veces.'])),
    ],
    nav_extra=guia('ejercicio-piedra-papel-tijera.pdf', 'Piedra, papel o tijera en PDF'))

# ============================================================ S15
PELOTA15 = [
    BANDERA,
    ('stack', 'looks', ['fijar tamaño al', ('num', '50'), '%']),
    ('stack', 'motion', ['ir a x:', ('num', '0'), 'y:', ('num', '100')]),
    ('stack', 'motion', ['apuntar en dirección', ('num', '160')]),
    ('c', 'control', ['por siempre'], [
        ('stack', 'motion', ['mover', ('num', '8'), 'pasos']),
        ('stack', 'motion', ['si toca un borde, rebotar']),
    ]),
]
PALA15 = [
    BANDERA,
    ('stack', 'motion', ['fijar estilo de rotación a', ('drop', 'no rotar')]),
    ('c', 'control', ['por siempre'], [
        ('stack', 'motion', ['ir a x:', rep('sensing', 'posición x del ratón'),
                             'y:', ('num', '-140')]),
    ]),
]

s15 = pagina(
    15, 'Pong I',
    'Sesión 15 de Scratch: la mecánica básica del Pong. Pelota que rebota y pala que sigue al '
    'ratón. CyR 1º ESO.',
    'la mecánica del <strong>Pong</strong>: una pelota que rebota por toda la pantalla y una pala '
    'que sigue a tu ratón.',
    [
        ('Dos objetos, dos programas, a la vez',
         '<p>El Pong es el videojuego más antiguo que se sigue jugando, y por dentro es asombrosamente '
         'simple: <strong>una pelota que no para nunca</strong> y <strong>una pala que obedece al '
         'jugador</strong>. Hoy montas esas dos piezas. La puntuación y el final de la partida son '
         'la sesión que viene.</p>'
         '<p>Necesitas dos objetos: una pelota (la <em>Ball</em> de la biblioteca vale) y una pala. '
         'La pala la puedes dibujar tú: un rectángulo alargado con la herramienta de dibujo.</p>'),

        ('Lee estos dos programas',
         dos_cajas(('Objeto <strong>Pelota</strong>', PELOTA15,
                    'Programa de la pelota: fijar tamaño al 50 por ciento, ir a x 0 y 100, apuntar '
                    'en dirección 160 y, por siempre, mover 8 pasos y si toca un borde rebotar'),
                   ('Objeto <strong>Pala</strong>', PALA15,
                    'Programa de la pala: fijar estilo de rotación a no rotar y, por siempre, ir a '
                    'la posición x del ratón manteniendo la y en menos 140')) +
         '<p>Aquí no hay un orden que seguir: los dos programas arrancan con la bandera y '
         '<strong>corren a la vez</strong>, cada uno a lo suyo.</p>' +
         claves([
             ('La pelota',
              'Se coloca arriba y apunta hacia abajo y a la derecha (dirección 160). Su '
              '<strong>por siempre</strong> hace sólo dos cosas: <em>mover (8) pasos</em> y '
              '<em>si toca un borde, rebotar</em>. Ese par de bloques es todo el «motor» del '
              'juego.'),
             ('La pala',
              'Tiene su propio <strong>por siempre</strong>. <strong>posición x del ratón</strong> '
              'es un informador de Sensores: vale la coordenada horizontal del cursor. Al '
              'metérselo al <em>ir a x:</em>, la pala se pega al ratón en horizontal, pero se '
              'queda siempre a la misma altura.')])),

        ('Comprueba que lo has entendido',
         pregunta('1', '¿Por qué la pala usa <em>ir a x: (…) y: (−140)</em> y no <em>mover (…) pasos</em>?',
                  [('lento', 'Porque mover es más lento',
                    'No es cuestión de velocidad: los dos bloques van igual de rápido dentro del bucle.'),
                   ('coloca', 'Porque la pala tiene que estar exactamente donde está el ratón, y '
                    '<em>ir a</em> la coloca ahí; <em>mover</em> sólo la empuja un poco',
                    'Correcto. <b>ir a</b> es un salto a una posición concreta; <b>mover</b> es un '
                    'desplazamiento relativo. Para seguir al ratón hace falta lo primero.'),
                   ('pelota', 'Porque mover sólo funciona en la pelota',
                    'No: <em>mover</em> funciona en cualquier objeto. Lo que pasa es que no sirve '
                    'para lo que queremos aquí.')],
                  'coloca')),

        ('Tu actividad',
         pasos([
             'Borra el gato: clic derecho sobre su icono y <strong>borrar</strong>. Hoy no hace '
             'falta.',
             'Añade la pelota (busca <strong>Ball</strong>) y la pala (busca <strong>Paddle</strong>). '
             'A la pala cámbiale el nombre a <strong>Pala</strong>: la sesión 16 la busca con ese '
             'nombre. Monta los dos programas, cada uno en el suyo.',
             'Comprueba que la pala se mueve con el ratón y no se sale por arriba ni por abajo.',
             'Ajusta la <strong>velocidad de la pelota</strong> (los 8 pasos). Busca un valor que '
             'se pueda seguir con la vista pero no aburra.',
             'Cambia la <strong>anchura de la pala</strong> desde la pestaña Disfraces. Una pala '
             'ancha hace el juego fácil; una estrecha, imposible.',
             'Ponle un fondo oscuro para que la pelota se vea bien.']) +
         ojo('De momento la pelota rebota también abajo',
             '<p>Con <em>si toca un borde, rebotar</em>, la pelota rebota en los <strong>cuatro</strong> '
             'bordes, incluido el de abajo. Eso significa que ahora mismo es imposible perder: la '
             'pala no sirve para nada.</p>'
             '<p style="margin-bottom:0">Está bien así. En la sesión siguiente le quitarás ese '
             'rebote de abajo y ahí es donde el juego se convierte en un juego.</p>')),

        ('Lo has conseguido si…',
         logros(['La pelota rebota por toda la pantalla sin pararse.',
                 'La pala sigue al ratón en horizontal y se queda a su altura.',
                 'La pala no gira ni se pone del revés.',
                 'La pelota se ve bien contra el fondo.'])),
    ],
    nav_extra=guia('ejercicio-de-pong.pdf', 'Pong, material de apoyo'))

# ============================================================ S16
PUNTOS16 = [
    si(hexa('sensing', '¿tocando', ('drop', 'Pala'), '?'),
       [('stack', 'sound', ['iniciar sonido', ('drop', 'Pop')]),
        ('stack', 'motion', ['apuntar en dirección',
                             op('número aleatorio entre', ('num', '-45'), 'y', ('num', '45'))]),
        ('stack', 'variables', ['sumar a', ('drop', 'Puntos'), ('num', '1')]),
        ('stack', 'motion', ['mover', ('num', '20'), 'pasos'])]),
]
FIN16 = [
    si(hexa('operators', rep('motion', 'posición en y'), '<', ('num', '-155')),
       [('stack', 'looks', ['decir', op('unir', ('txt', 'Fin. Puntos: '), var('Puntos')),
                            'durante', ('num', '3'), 'segundos']),
        ('cap', 'control', ['detener', ('drop', 'todos')])]),
]
DIFI16 = [
    ('stack', 'motion', ['mover', op(('num', '8'), '+', op(var('Puntos'), '/', ('num', '5'))),
                         'pasos']),
]

s16 = pagina(
    16, 'Pong II',
    'Sesión 16 de Scratch: marcador, fin de partida y dificultad creciente en el Pong. '
    'CyR 1º ESO.',
    'que tu Pong sea un juego de verdad: con <strong>marcador</strong>, con <strong>final</strong> '
    'y cada vez más difícil.',
    [
        ('Lo que le falta al Pong de la sesión anterior',
         '<p>Tienes una pelota que rebota y una pala que se mueve, pero no se puede ni ganar ni '
         'perder. Hoy añades las tres cosas que convierten eso en un juego: '
         '<strong>puntuar</strong>, <strong>perder</strong> y <strong>subir la dificultad</strong>.</p>'
         '<p>Todo lo de hoy va <strong>dentro del por siempre de la pelota</strong>, debajo de los '
         'bloques que ya tienes.</p>'),

        ('Los puntos',
         caja(PUNTOS16, 'Condicional: si la pelota está tocando la Pala, iniciar el sonido Pop, '
                        'apuntar en una dirección aleatoria entre menos 45 y 45, sumar 1 a Puntos '
                        'y mover 20 pasos',
              pie='El <strong>apuntar en dirección aleatoria</strong> hace que la pelota no salga '
                  'siempre con el mismo ángulo, y el <strong>mover 20 pasos</strong> del final la '
                  'despega de la pala. Ahora verás por qué hace falta.') +
         '<p>Recuerda crear la variable <code>Puntos</code> y ponerla a <strong>0</strong> al '
         'arrancar, en el mismo sitio donde colocas la pelota.</p>'),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Montas el marcador pero <strong>sin</strong> el <em>mover (20) pasos</em> del '
                       'final. Al probarlo, cada vez que la pelota toca la pala el marcador sube de '
                       'golpe 5 o 6 puntos. ¿Por qué?',
                  [('varias', 'Porque la pelota rebota varias veces seguidas en la pala',
                    'Estás cerca, pero no es que rebote varias veces: es que <b>no ha dejado de '
                    'tocarla</b> en ningún momento.'),
                   ('bucle', 'Porque el por siempre da muchas vueltas por segundo y, mientras la '
                    'pelota siga encima de la pala, cuenta un punto en cada vuelta',
                    'Exacto. La condición «¿tocando la Pala?» sigue siendo verdad durante varias '
                    'vueltas seguidas del bucle. Por eso hay que <b>alejar la pelota</b> justo '
                    'después de sumar el punto — o esperar un poco antes de seguir mirando.'),
                   ('suma', 'Porque el bloque sumar a suma más de 1 cuando va muy rápido',
                    'No. <em>sumar a (Puntos) (1)</em> suma exactamente 1 cada vez que se ejecuta. '
                    'El problema es cuántas veces se ejecuta.')],
                  'bucle')),

        ('Tu actividad',
         pasos([
             'Crea <code>Puntos</code>, ponla a 0 al arrancar y añade el condicional de la pala.',
             'Prueba primero <strong>sin</strong> el <em>mover 20 pasos</em> para ver el fallo del '
             'marcador con tus propios ojos. Después añádelo y comprueba que se arregla.',
             'Añade el <strong>final de partida</strong>: cuando la pelota se te escapa por '
             'abajo, se acabó. Va en el mismo <em>por siempre</em>, debajo de todo.',
             'Sube la dificultad: sustituye el <em>mover (8) pasos</em> por este otro, que hace que '
             'la pelota vaya más rápido cuanto más puntos llevas.',
             '<strong>Reto:</strong> guarda el récord en una variable <code>Récord</code> y '
             'muéstralo. Pista: sólo hay que actualizarlo si <code>Puntos</code> es mayor.']) +
         caja(FIN16, 'Condicional: si la posición en y de la pelota es menor que menos 155, decir Fin '
                     'seguido de los puntos durante 3 segundos y detener todos',
              pie='<strong>posición en y</strong> vale cuánto está de arriba o de abajo la pelota, de '
                  '−180 a 180. La pala está en −140, así que por debajo de −155 la pelota ya ha '
                  'pasado de largo. No hace falta quitar el <em>si toca un borde, rebotar</em>: '
                  'esta comprobación salta antes de que la pelota llegue al borde de abajo.') +
         caja(DIFI16, 'Bloque mover, con el operador 8 más Puntos dividido entre 5, pasos',
              pie='Con 0 puntos avanza 8; con 20 puntos avanza 12. La dificultad sube sola.') +
         ojo('Prueba tu propio juego a fondo',
             '<p>Antes de entregar, juega tres partidas enteras. Los fallos del Pong casi nunca se '
             'ven en los diez primeros segundos: aparecen cuando la pelota coge velocidad, cuando '
             'llega justo a una esquina o cuando roza el lateral de la pala.</p>')),

        ('Lo has conseguido si…',
         logros(['El marcador sube <strong>exactamente uno</strong> por cada toque de pala.',
                 'La partida termina cuando se te escapa la pelota, y dice la puntuación.',
                 'La pelota va más rápido a medida que subes puntos.',
                 'Al volver a jugar, el marcador empieza en 0.',
                 'Has jugado tres partidas seguidas sin que aparezca ningún fallo raro.'])),
    ],
    nav_extra=guia('ejercicio-de-pong.pdf', 'Pong, material de apoyo'))

for n, h in [(12, s12), (13, s13), (14, s14), (15, s15), (16, s16)]:
    escribir(n, h)

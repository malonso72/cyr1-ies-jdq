# -*- coding: utf-8 -*-
"""Sesiones 01 a 05 de T1 · Scratch."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scratchsvg import hexa, tecla
from plantilla import pagina, caja, pasos, pregunta, pista, ojo, logros, tabla
from diagramas import mapa_editor, rosa_direcciones
from comun import escribir, CUADERNILLO

BANDERA = ('hat', 'events', ['al hacer clic en', ('icon', 'bandera')])

# ============================================================ S01
P01 = [
    BANDERA,
    ('stack', 'looks', ['decir', ('txt', '¡Hola! Soy Sprite1'), 'durante', ('num', '2'), 'segundos']),
    ('stack', 'motion', ['mover', ('num', '100'), 'pasos']),
    ('stack', 'sound', ['iniciar sonido', ('drop', 'Miau')]),
]

s01 = pagina(
    1, 'Introducción a Scratch',
    'Primera sesión de Scratch: conocer el editor, montar tu primer programa y aprender a '
    'descargar el proyecto para entregarlo en Moodle. CyR 1º ESO.',
    'un proyecto tuyo, con un personaje que saluda, se mueve y hace ruido — y descargado '
    'en tu ordenador para poder entregarlo.',
    [
        ('Dónde está cada cosa',
         '<p>Scratch se abre en el navegador. No hay que instalar nada y no hace falta cuenta. '
         'Esta es la pantalla que te vas a encontrar:</p>\n'
         '<div class="caja-bloques">' + mapa_editor() +
         '<p class="pie">Las cuatro zonas que vas a usar todo el trimestre. '
         'Fíjate en la <strong>1</strong>: los bloques están repartidos por colores, y el color '
         'te dice en qué categoría buscarlos.</p></div>\n' +
         pasos([
             '<strong>Paleta.</strong> Todos los bloques que existen, ordenados por color. '
             'Azul es movimiento, morado apariencia, rosa sonido, amarillo eventos…',
             '<strong>Área de código.</strong> Arrastras los bloques aquí y los encajas unos '
             'debajo de otros, como piezas de construcción.',
             '<strong>Escenario.</strong> Lo que se ve cuando el programa funciona. '
             'La <strong>bandera verde</strong> lo arranca y el <strong>círculo rojo</strong> lo para.',
             '<strong>Objetos.</strong> Los personajes. Empiezas con uno solo, el gato, que se '
             'llama <strong>Sprite1</strong>. Cada objeto tiene <em>su propio</em> código.'])),

        ('Lee este programa',
         '<p>Este es el programa que vas a montar hoy. Son cuatro bloques y cada uno viene de una '
         'categoría distinta:</p>\n' +
         caja(P01, 'Programa: al hacer clic en la bandera verde, decir ¡Hola! Soy Sprite1 durante '
                   '2 segundos, mover 100 pasos e iniciar el sonido Miau',
              pie='El bloque amarillo de arriba tiene forma de sombrero: es el que <em>arranca</em> '
                  'todo. Ningún programa funciona sin uno.') +
         pasos([
             'Pulsas la bandera verde y el programa empieza.',
             'El gato saca un bocadillo con el texto durante 2 segundos.',
             'Se desplaza 100 pasos en la dirección a la que esté mirando.',
             'Suena el maullido y el programa termina.'])),

        ('Comprueba que lo has entendido',
         pregunta('1',
                  'Terminas el ejercicio, cierras la pestaña de Scratch y te vas a casa. '
                  'Al día siguiente, ¿dónde está tu proyecto?',
                  [('cuenta', 'Guardado en mi cuenta de Scratch',
                    'No. En clase trabajamos sin cuenta, así que Scratch no guarda nada en '
                    'Internet. No hay ningún sitio del que recuperarlo.'),
                   ('perdido', 'En ningún sitio: se ha perdido',
                    'Exacto, y es lo más importante de hoy. Sin cuenta, el proyecto sólo existe '
                    'en esa pestaña. Al cerrarla desaparece. Por eso hay que descargarlo antes.'),
                   ('descargas', 'En la carpeta Descargas del ordenador',
                    'Sólo si antes hiciste Archivo, Guardar en tu ordenador. Cerrar la pestaña '
                    'no descarga nada por su cuenta.')],
                  'perdido')),

        ('Tu actividad',
         pasos([
             'Abre Scratch con el botón de arriba. Ya tienes al gato, <strong>Sprite1</strong>.',
             'Cambia el fondo: botón <strong>Elegir un fondo</strong>, abajo del todo a la derecha.',
             'Monta el programa de arriba arrastrando los cuatro bloques.',
             'Cambia el texto del bocadillo por un saludo tuyo.',
             'Añade un <strong>segundo objeto</strong> con el botón del gato (abajo a la derecha) '
             'y hazle decir algo también. Acuérdate: tienes que seleccionarlo primero, porque cada '
             'objeto tiene su propio código.']) +
         ojo('Esto se te va a olvidar la primera semana',
             '<p>Scratch <strong>no guarda solo</strong>. Antes de irte de clase:</p>'
             '<p style="margin:0"><strong>Archivo → Guardar en tu ordenador.</strong> '
             'Se descarga un archivo <code>.sb3</code> a tu carpeta <strong>Descargas</strong>. '
             'Ese archivo es tu proyecto, y es lo que subes a Moodle.</p>')),

        ('Lo has conseguido si…',
         logros(['El fondo ya no es blanco.',
                 'Al pulsar la bandera verde, el gato dice algo tuyo.',
                 'Se mueve y suena el maullido.',
                 'Tienes un segundo objeto que también hace algo.',
                 'Has descargado el <code>.sb3</code> y sabes en qué carpeta está.'])),
    ],
    cuadernillo=CUADERNILLO[1])

# ============================================================ S02
P02 = [
    BANDERA,
    ('stack', 'motion', ['fijar estilo de rotación a', ('drop', 'no rotar')]),
    ('stack', 'motion', ['ir a x:', ('num', '-120'), 'y:', ('num', '0')]),
    ('stack', 'motion', ['apuntar en dirección', ('num', '90')]),
    ('stack', 'motion', ['mover', ('num', '120'), 'pasos']),
    ('stack', 'control', ['esperar', ('num', '1'), 'segundos']),
    ('stack', 'motion', ['apuntar en dirección', ('num', '180')]),
    ('stack', 'motion', ['mover', ('num', '120'), 'pasos']),
    ('stack', 'control', ['esperar', ('num', '1'), 'segundos']),
    ('stack', 'sound', ['iniciar sonido', ('drop', 'Miau')]),
]
PISTA02 = [
    ('stack', 'motion', ['apuntar en dirección', ('num', '-90')]),
    ('stack', 'motion', ['mover', ('num', '120'), 'pasos']),
    ('stack', 'control', ['esperar', ('num', '1'), 'segundos']),
    ('stack', 'motion', ['apuntar en dirección', ('num', '0')]),
    ('stack', 'motion', ['mover', ('num', '120'), 'pasos']),
]

s02 = pagina(
    2, 'Movimiento y direcciones',
    'Sesión 2 de Scratch: la rosa de direcciones, apuntar en dirección y mover pasos. '
    'El personaje recorre una ruta cerrada. CyR 1º ESO.',
    'que tu personaje recorra un cuadrado y <strong>vuelva exactamente al punto de partida</strong>.',
    [
        ('Las cuatro direcciones',
         '<p>Antes de mover nada hay que saber hacia dónde. En Scratch las direcciones son '
         'números, y sólo necesitas cuatro:</p>\n'
         '<div class="caja-bloques" style="max-width:420px">' + rosa_direcciones() +
         '<p class="pie">Ojo: tu cuadernillo escribe <strong>270</strong>, <strong>315</strong> y '
         '<strong>225</strong>. El editor de hoy usa números de −180 a 180, así que en pantalla '
         'verás <strong>−90</strong>, <strong>−45</strong> y <strong>−135</strong>. '
         'Son las mismas direcciones con otro nombre.</p></div>'),

        ('Lee este programa',
         '<p>Este programa hace dos lados del cuadrado: primero hacia la derecha, después hacia '
         'abajo. Faltan los otros dos.</p>\n' +
         caja(P02, 'Programa: fijar estilo de rotación a no rotar, ir a x menos 120 y 0, '
                   'apuntar en dirección 90, mover 120 pasos, esperar 1 segundo, apuntar en '
                   'dirección 180, mover 120 pasos, esperar 1 segundo e iniciar sonido Miau') +
         pasos([
             'El <strong>ir a x: y:</strong> del principio coloca al gato siempre en el mismo '
             'sitio. Sin él, cada vez que pulses la bandera empezaría donde acabó la vez anterior.',
             'Apunta a la <strong>derecha</strong> (90) y avanza 120 pasos.',
             'La <strong>espera de 1 segundo</strong> sólo está para que puedas ver el recorrido. '
             'Sin ella el gato llegaría al final de golpe.',
             'Apunta hacia <strong>abajo</strong> (180) y avanza otros 120.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', '¿Qué dirección hay que poner para que el personaje vaya hacia arriba?',
                  [('n90', '90', 'No: 90 es hacia la derecha. Es la dirección con la que empieza '
                    'el gato cuando abres Scratch.'),
                   ('n0', '0', 'Correcto. El 0 apunta hacia arriba, como la aguja de un reloj a '
                    'las doce. Desde ahí los números crecen girando hacia la derecha.'),
                   ('n180', '180', 'No: 180 es justo la contraria, hacia abajo.')],
                  'n0')),

        ('Tu actividad',
         '<p><strong>Completa el cuadrado.</strong> Añade los dos lados que faltan para que el '
         'gato vuelva al punto de partida: hacia la izquierda y hacia arriba.</p>'
         '<p>Cuando te salga, prueba a cambiar los 120 pasos por otro número. El cuadrado tiene '
         'que seguir cerrando.</p>' +
         pista('¿Te has atascado? Abre la pista',
               '<p>Estos son los bloques que faltan, y van <strong>debajo</strong> de los que ya '
               'hay, justo antes del sonido:</p>' +
               caja(PISTA02, 'Pista: apuntar en dirección menos 90, mover 120 pasos, esperar 1 '
                             'segundo, apuntar en dirección 0 y mover 120 pasos', ancho=420)) +
         ojo('El gato boca abajo',
             '<p>Si no pones el bloque <strong>fijar estilo de rotación a (no rotar)</strong>, al '
             'apuntar hacia la izquierda el gato aparece del revés. No es un fallo tuyo: al girar '
             'la dirección, gira el dibujo entero.</p>')),

        ('Lo has conseguido si…',
         logros(['El gato dibuja un cuadrado y termina donde empezó.',
                 'Al pulsar la bandera dos veces seguidas, hace exactamente lo mismo.',
                 'No aparece boca abajo en ningún momento.',
                 'Sabrías decir qué número corresponde a cada una de las cuatro direcciones.'])),
    ],
    cuadernillo=CUADERNILLO[2])

# ============================================================ S03
P03 = [
    BANDERA,
    ('stack', 'motion', ['ir a x:', ('num', '0'), 'y:', ('num', '0')]),
    ('stack', 'motion', ['apuntar en dirección', ('num', '90')]),
    ('c', 'control', ['repetir', ('num', '4')], [
        ('stack', 'motion', ['mover', ('num', '100'), 'pasos']),
        ('stack', 'motion', ['girar', ('icon', 'giro-d'), ('num', '90'), 'grados']),
    ]),
    ('stack', 'sound', ['iniciar sonido', ('drop', 'Miau')]),
]
LARGO03 = [
    BANDERA,
    ('stack', 'motion', ['mover', ('num', '100'), 'pasos']),
    ('stack', 'motion', ['girar', ('icon', 'giro-d'), ('num', '90'), 'grados']),
    ('stack', 'motion', ['mover', ('num', '100'), 'pasos']),
    ('stack', 'motion', ['girar', ('icon', 'giro-d'), ('num', '90'), 'grados']),
    ('stack', 'motion', ['mover', ('num', '100'), 'pasos']),
    ('stack', 'motion', ['girar', ('icon', 'giro-d'), ('num', '90'), 'grados']),
    ('stack', 'motion', ['mover', ('num', '100'), 'pasos']),
    ('stack', 'motion', ['girar', ('icon', 'giro-d'), ('num', '90'), 'grados']),
]
SIEMPRE03 = [
    BANDERA,
    ('c', 'control', ['por siempre'], [
        ('stack', 'motion', ['mover', ('num', '4'), 'pasos']),
        ('stack', 'motion', ['si toca un borde, rebotar']),
    ]),
]

s03 = pagina(
    3, 'Bucles',
    'Sesión 3 de Scratch: repetir y por siempre. Recorrer polígonos sin escribir el mismo '
    'bloque muchas veces. CyR 1º ESO.',
    'que el gato <strong>recorra</strong> un cuadrado, un triángulo y un pentágono y vuelva al '
    'punto de partida, <strong>sin repetir ni un bloque</strong>.',
    [
        ('El problema que resuelve un bucle',
         '<p>Para recorrer un cuadrado hay que avanzar y girar cuatro veces. Se puede escribir '
         'así, y funciona:</p>' +
         caja(LARGO03, 'Programa largo: mover 100 pasos y girar 90 grados a la derecha, repetido '
                       'cuatro veces seguidas', ancho=330,
              pie='Ocho bloques. Y para un pentágono harían falta diez.') +
         '<p>Un <strong>bucle</strong> hace lo mismo con dos bloques. Le dices cuántas veces y '
         'metes dentro lo que se repite:</p>' +
         caja(P03, 'Programa con bucle: ir a x 0 y 0, apuntar en dirección 90, repetir 4 veces '
                   'mover 100 pasos y girar 90 grados a la derecha, e iniciar sonido Miau')),

        ('Qué hace, paso a paso',
         pasos([
             'El gato se coloca en el centro mirando a la derecha.',
             'Entra en el <strong>repetir (4)</strong>. Ejecuta lo de dentro: avanza y gira.',
             'Vuelve arriba y lo hace otra vez. Y otra. Y otra. Cuatro en total.',
             'Cuando ha dado las cuatro vueltas, <strong>sale</strong> del bucle y sigue con el '
             'bloque de abajo: el maullido.',
             'Como ha girado 90 grados cuatro veces, ha dado una vuelta completa: '
             '4 × 90 = <strong>360</strong>. Por eso el cuadrado cierra.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Cambias el giro de 90 a 100 grados y dejas el resto igual. ¿Qué pasa?',
                  [('cierra', 'Sale un cuadrado un poco más grande',
                    'No. El número de pasos es lo que cambia el tamaño; los grados cambian el '
                    'giro, no la longitud del lado.'),
                   ('abierto', 'La figura no cierra: el gato no vuelve al punto de partida',
                    'Correcto. 4 × 100 = 400 grados, más de una vuelta completa. Para que una '
                    'figura cierre, la suma de todos los giros tiene que dar exactamente 360.'),
                   ('igual', 'No se nota nada, 90 y 100 están muy cerca',
                    'Se nota, y bastante: sobran 40 grados y el recorrido queda torcido.')],
                  'abierto')),

        ('Tu actividad',
         '<p>Con el mismo programa, cambiando sólo dos números, recorre estas tres figuras:</p>' +
         tabla(['Figura', 'Repetir', 'Girar', 'Comprobación'],
               [['Cuadrado', '4', '90', '4 × 90 = 360 ✔'],
                ['Triángulo', '3', '120', '3 × 120 = 360 ✔'],
                ['Pentágono', '5', '72', '5 × 72 = 360 ✔']]) +
         '<p>¿Ves la regla? <strong>Los grados son 360 dividido entre el número de lados.</strong> '
         'Pruébala con un hexágono (6 lados) sin mirar la tabla.</p>' +
         ojo('El cuadrado no se queda pintado',
             '<p>El gato <strong>recorre</strong> el cuadrado, pero no deja ninguna línea detrás: '
             'en la pantalla no vas a ver ninguna figura dibujada. Lo que tienes que mirar es '
             'que <strong>acabe donde empezó</strong>, y ahí sabes que ha cerrado.</p>'
             '<p style="margin-bottom:0">Para que deje rastro haría falta añadir la extensión '
             '<strong>Lápiz</strong>, con el botón de abajo a la izquierda. No está en la paleta '
             'por defecto y hoy no la necesitamos.</p>') +
         pista('¿Y el bucle que no se acaba nunca?',
               '<p>Existe otro bucle, <strong>por siempre</strong>, que no lleva número: repite '
               'hasta que pares el programa con el círculo rojo. Se usa para cosas que tienen que '
               'estar vigilando todo el rato.</p>' +
               caja(SIEMPRE03, 'Programa: al hacer clic en la bandera, por siempre mover 4 pasos '
                               'y si toca un borde rebotar', ancho=330) +
               '<p style="margin-bottom:0">Fíjate en que <strong>no tiene muesca abajo</strong>: '
               'no se le puede encajar nada detrás, porque nunca llegaría el turno.</p>')),

        ('Lo has conseguido si…',
         logros(['Has hecho las tres figuras cambiando sólo dos números.',
                 'Las tres cierran: el gato acaba exactamente donde empezó.',
                 'Sabrías explicar por qué los giros tienen que sumar 360.',
                 'Sabes la diferencia entre <em>repetir (10)</em> y <em>por siempre</em>.'])),
    ],
    cuadernillo=CUADERNILLO[3])

# ============================================================ S04
P04 = [
    BANDERA,
    ('stack', 'motion', ['ir a x:', ('num', '0'), 'y:', ('num', '0')]),
    ('c', 'control', ['repetir hasta que', tecla('espacio')], [
        ('stack', 'motion', ['mover', ('num', '4'), 'pasos']),
        ('stack', 'motion', ['si toca un borde, rebotar']),
    ]),
    ('stack', 'looks', ['decir', ('txt', '¡Me has parado!'), 'durante', ('num', '2'), 'segundos']),
    ('cap', 'control', ['detener', ('drop', 'todos')]),
]
VAR04 = [
    ('c', 'control', ['repetir hasta que', hexa('sensing', '¿tocando', ('drop', 'borde'), '?')], [
        ('stack', 'motion', ['mover', ('num', '4'), 'pasos']),
    ]),
]

s04 = pagina(
    4, 'Condicionales I',
    'Sesión 4 de Scratch: repetir hasta que. Un bucle que vigila una condición y se para '
    'cuando ocurre algo. CyR 1º ESO.',
    'un personaje que se mueve sin parar y <strong>sólo se detiene cuando tú se lo dices</strong>.',
    [
        ('El nombre de esta sesión engaña un poco',
         ojo('Hoy todavía no hay ningún «si… entonces»',
             '<p>Se llama «Condicionales I», pero aquí todavía <strong>no vas a usar un '
             '«si… entonces»</strong>. Eso llega en la sesión siguiente. Lo de hoy es un bucle que '
             'lleva una <em>condición</em> dentro: <strong>repetir hasta que</strong>. Es el paso '
             'previo, y el nombre viene del cuadernillo antiguo.</p>')),

        ('Lee este programa',
         caja(P04, 'Programa: ir a x 0 y 0, repetir hasta que la tecla espacio esté presionada '
                   'moviendo 4 pasos y rebotando en los bordes, después decir ¡Me has parado! '
                   'durante 2 segundos y detener todos',
              pie='El bloque azul claro con forma de hexágono es una <strong>condición</strong>: '
                  'sólo puede valer sí o no. Encaja únicamente en huecos de esa misma forma.') +
         pasos([
             'El gato empieza en el centro.',
             '<strong>repetir hasta que</strong> mira la condición <em>antes de cada vuelta</em>: '
             '¿está pulsada la barra espaciadora?',
             'Si la respuesta es <strong>no</strong>, ejecuta lo de dentro (avanza y rebota) y '
             'vuelve a preguntar.',
             'Si la respuesta es <strong>sí</strong>, se sale del bucle y pasa al bloque de abajo.',
             'El <strong>detener (todos)</strong> del final apaga el programa entero. Fíjate en su '
             'forma: no tiene muesca abajo, porque después de él no puede ir nada.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Arrancas el programa y no pulsas nunca la barra espaciadora. ¿Qué pasa?',
                  [('para', 'El gato se para solo al cabo de un rato',
                    'No. El bucle no tiene un número de vueltas ni un tiempo límite: sólo mira '
                    'esa condición.'),
                   ('siempre', 'El gato sigue moviéndose y rebotando indefinidamente',
                    'Correcto. La condición nunca se cumple, así que el bucle nunca termina y los '
                    'bloques de debajo nunca llegan a ejecutarse. Puedes pararlo con el círculo rojo.'),
                   ('error', 'Scratch da un error',
                    'No. Para Scratch esto es perfectamente válido: hay muchos programas pensados '
                    'para no acabar nunca, como los videojuegos.')],
                  'siempre')),

        ('Tu actividad',
         '<p>Haz estas tres versiones, una detrás de otra. Descarga sólo la última.</p>' +
         pasos([
             'Monta el programa tal cual está arriba y compruébalo.',
             'Cambia la condición por <strong>¿ratón presionado?</strong> — está en Sensores, '
             'y tiene la misma forma de hexágono, así que encaja en el mismo hueco.',
             'Cambia la condición por <strong>¿tocando (borde)?</strong> El gato se moverá hasta '
             'chocar con el borde y ahí se parará. Para esta versión tendrás que quitar el bloque '
             'de rebotar, o no chocará nunca.']) +
         caja(VAR04, 'Tercera versión: repetir hasta que tocando borde, mover 4 pasos', ancho=380)),

        ('Lo has conseguido si…',
         logros(['El gato se mueve y rebota hasta que pulsas espacio.',
                 'Al pararse, dice algo y el programa termina.',
                 'Has probado las tres condiciones distintas en el mismo hueco.',
                 'Sabrías explicar la diferencia entre <em>repetir (10)</em> y '
                 '<em>repetir hasta que</em>.'])),
    ],
    cuadernillo=CUADERNILLO[4])

# ============================================================ S05
P05 = [
    BANDERA,
    ('c', 'control', ['repetir hasta que', tecla('espacio')], [
        ('c', 'control', ['si', tecla('flecha derecha'), 'entonces'], [
            ('stack', 'motion', ['apuntar en dirección', ('num', '90')]),
            ('stack', 'motion', ['mover', ('num', '10'), 'pasos'])]),
        ('c', 'control', ['si', tecla('flecha izquierda'), 'entonces'], [
            ('stack', 'motion', ['apuntar en dirección', ('num', '-90')]),
            ('stack', 'motion', ['mover', ('num', '10'), 'pasos'])])]),
    ('stack', 'sound', ['iniciar sonido', ('drop', 'Miau')]),
]
PISTA05 = [
    ('c', 'control', ['si', tecla('flecha arriba'), 'entonces'], [
        ('stack', 'motion', ['apuntar en dirección', ('num', '0')]),
        ('stack', 'motion', ['mover', ('num', '10'), 'pasos'])]),
]
ROT05 = [('stack', 'motion', ['fijar estilo de rotación a', ('drop', 'no rotar')])]

s05 = pagina(
    5, 'Condicionales II y teclado',
    'Sesión 5 de Scratch: condicionales anidados dentro de un bucle. Mover el personaje con '
    'las cuatro flechas del teclado. CyR 1º ESO.',
    'que tu personaje se mueva por el escenario con las <strong>cuatro flechas</strong> del '
    'teclado, y que maúlle cuando pulses la barra espaciadora.',
    [
        ('Lee este programa',
         '<p>Este es el programa de partida. Todavía <em>no</em> es el tuyo: tú vas a completarlo.</p>' +
         caja(P05, 'Programa: al hacer clic en la bandera verde, repetir hasta que se pulse '
                   'espacio, con dos condicionales dentro que mueven el personaje a la derecha y a '
                   'la izquierda; al salir del bucle, iniciar el sonido Miau',
              pie='Si en tu cuadernillo ves <strong>270</strong> donde aquí pone <strong>−90</strong>, '
                  'es lo mismo: dos formas de nombrar la dirección hacia la izquierda.')),

        ('Qué hace, paso a paso',
         pasos([
             'Al pulsar la bandera verde, el programa arranca.',
             '<strong>repetir hasta que</strong> vigila una y otra vez si has pulsado la barra '
             'espaciadora. Mientras no la pulses, todo lo de dentro se repite sin parar.',
             'Dentro hay <strong>dos condicionales</strong>, uno debajo del otro. Cada uno pregunta '
             'por una flecha distinta. A esto se le llama <em>anidar</em>: meter código dentro de '
             'otro código.',
             'Si pulsas la <strong>flecha derecha</strong>, el personaje apunta a la derecha '
             '(dirección 90) y avanza. Con la <strong>flecha izquierda</strong>, apunta a −90 y '
             'avanza también.',
             'El <strong>miau</strong> está <em>fuera</em> del bucle. Por eso no suena mientras te '
             'mueves: suena cuando el bucle termina.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Antes de tocar nada: ¿cuándo suena el miau?',
                  [('mover', 'Cada vez que el personaje se mueve',
                    'No. El miau no está dentro del bucle: está debajo, fuera. Los bloques de '
                    'dentro se repiten muchas veces; el de fuera espera a que el bucle acabe.'),
                   ('espacio', 'Sólo cuando pulsas la barra espaciadora',
                    'Correcto. El bloque del sonido está fuera del bucle, así que no se ejecuta '
                    'hasta que el bucle termina — y el bucle termina justo al pulsar espacio.'),
                   ('inicio', 'Al pulsar la bandera verde, nada más empezar',
                    'No. Al pulsar la bandera lo primero que se ejecuta es el bucle, y el bucle no '
                    'deja pasar al siguiente bloque hasta que termina.')],
                  'espacio')),

        ('Tu actividad',
         '<p>El programa sólo sabe ir a la derecha y a la izquierda. '
         '<strong>Añádele lo que le falta para subir y bajar</strong> con las otras dos flechas.</p>'
         '<p>Necesitarás dos condicionales más, iguales a los que ya hay pero preguntando por la '
         '<strong>flecha arriba</strong> y la <strong>flecha abajo</strong>. Las direcciones son '
         '<strong>0</strong> para arriba y <strong>180</strong> para abajo.</p>' +
         pista('¿Te has atascado? Abre la pista',
               '<p>Así queda el condicional de subir. El de bajar es idéntico, cambiando la flecha '
               'y la dirección. Ojo: los dos nuevos van <em>dentro</em> del '
               '<strong>repetir hasta que</strong>, debajo de los que ya hay.</p>' +
               caja(PISTA05, 'Pista: si la tecla flecha arriba está presionada, apuntar en '
                             'dirección 0 y mover 10 pasos', ancho=420)) +
         ojo('Ojo con esto',
             '<p>Al ir hacia la izquierda verás que el gato aparece <strong>boca abajo</strong>. '
             'No es un fallo tuyo: al apuntar en dirección −90 el personaje gira entero.</p>'
             '<p style="margin-bottom:8px;">Ya lo arreglaste en la <strong>sesión 2</strong>: '
             'es el mismo bloque, y va otra vez justo debajo de la bandera verde.</p>' +
             caja(ROT05, 'Bloque fijar estilo de rotación a no rotar', ancho=400))),

        ('Lo has conseguido si…',
         logros(['El personaje se mueve con las <strong>cuatro</strong> flechas.',
                 'Se mueve <strong>mientras</strong> mantienes la tecla, no una sola vez.',
                 'Al pulsar la barra espaciadora, se para y suena el miau.',
                 'Sabrías explicar con tus palabras qué hace <em>repetir hasta que</em>.'])),
    ],
    cuadernillo=CUADERNILLO[5])

for n, h in [(1, s01), (2, s02), (3, s03), (4, s04), (5, s05)]:
    escribir(n, h)

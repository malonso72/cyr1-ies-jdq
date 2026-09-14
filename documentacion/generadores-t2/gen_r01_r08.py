# -*- coding: utf-8 -*-
"""Retos 1 a 8 del troncal de T2 · micro:bit."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bloques import *                                  # noqa: F401,F403
from plantilla_t2 import (pagina, caja, caja_varios, dos_cajas, placa, cat, bl, amplia,
                          pasos, secuencia, claves, pregunta, pista, ojo, logros, tabla)
from comun_t2 import escribir

TODO_ON = '#####:#####:#####:#####:#####'
NADA = '.....:.....:.....:.....:.....'

# ============================================================ R1 · Hola, micro:bit
P1 = [
    INICIAR([CADENA('Hola')]),
    SIEMPRE([ICONO('corazón'), PAUSA(500), BORRAR, PAUSA(500)]),
]

r01 = pagina(
    'r01', 'Reto 1', 'Hola, micro:bit',
    'Reto 1 de micro:bit: primer programa en MakeCode con al iniciar, para siempre, mostrar '
    'cadena y mostrar ícono. La matriz de 25 LEDs. CyR 1º ESO.',
    'que la placa te salude con tu nombre y después haga parpadear un corazón sin parar. Es tu '
    'primer programa en MakeCode y ya tiene las dos piezas que llevan casi todos: '
    '<strong>al iniciar</strong> y <strong>para siempre</strong>.',
    [
        ('La placa: 25 luces y dos botones',
         placa('.....:.#.#.:.....:#...#:.###.',
               'La matriz de la micro:bit con una cara sonriente encendida',
               pie='Cada cuadrado es un LED. Sólo se encienden en rojo.',
               lado='<p>La micro:bit no tiene pantalla: tiene <strong>25 LEDs</strong> en una '
                    'rejilla de 5 por 5. Con ellos se escriben letras, números y dibujos. '
                    'Debajo tiene los botones <strong>A</strong> y <strong>B</strong>, y dentro '
                    'lleva sensores de luz, temperatura, movimiento y brújula, un micrófono y un '
                    'altavoz. Todo eso lo vas a usar este trimestre.</p>'
                    '<p>Se programa en <strong>MakeCode</strong>, en el navegador, con bloques '
                    'que se encajan igual que en Scratch. Lo que cambia es que el programa no '
                    'corre en el ordenador: se <strong>copia a la placa</strong> y la placa lo '
                    'ejecuta sola, aunque la desconectes del ordenador.</p>')),

        ('Lee este programa',
         caja_varios([[P1[0]], [P1[1]]],
                     'Programa: al iniciar, mostrar cadena Hola; para siempre: mostrar ícono '
                     'corazón, pausa 500 ms, borrar la pantalla, pausa 500 ms',
                     pie='Dos bloques de evento sueltos. En MakeCode no hace falta que estén '
                  'pegados: cada uno arranca por su cuenta.') +
         secuencia([
             '<strong>al iniciar</strong> se ejecuta <em>una sola vez</em>, en cuanto la placa '
             'arranca. Es el sitio de las cosas que sólo pasan al principio.',
             '<strong>mostrar cadena «Hola»</strong> escribe el texto. Como no cabe en 5 LEDs de '
             'ancho, las letras <em>se desplazan</em> de derecha a izquierda, una detrás de otra.',
             '<strong>para siempre</strong> es el <span class="bl">por siempre</span> de '
             'Scratch: lo de dentro se repite sin parar mientras la placa tenga corriente.',
             '<strong>mostrar ícono corazón</strong> enciende los LEDs que forman el dibujo. Hay '
             'cuarenta dibujos ya hechos en el desplegable.',
             '<strong>pausa (ms) 500</strong> espera medio segundo. Los tiempos en MakeCode van '
             'en <strong>milisegundos</strong>: 1000 ms es 1 segundo.',
             '<strong>borrar la pantalla</strong> apaga todos los LEDs, otra pausa, y vuelta '
             'al 4: el corazón parpadea.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Mueves los cuatro bloques de dentro de <em>para siempre</em> a '
                       '<em>al iniciar</em>, debajo del «Hola». ¿Qué hace la placa?',
                  [('igual', 'Lo mismo: el corazón parpadea sin parar',
                    'No. <b>al iniciar</b> se ejecuta una vez y se acaba; nada de lo que hay '
                    'dentro se repite.'),
                   ('una', 'Escribe «Hola», enciende el corazón una vez, lo apaga, y ya no hace '
                    'nada más',
                    'Correcto. Sin <b>para siempre</b> no hay repetición: la placa hace la lista '
                    'de arriba abajo una sola vez y se queda quieta.'),
                   ('nada', 'No enciende nada, porque «mostrar ícono» sólo funciona dentro de '
                    '«para siempre»',
                    'No. Cualquier bloque funciona en cualquier evento. Lo que cambia es cuántas '
                    'veces se ejecuta.')],
                  'una')),

        ('Tu reto',
         pasos([
             'Abre MakeCode y pulsa <strong>Nuevo proyecto</strong>. Verás que <span class="bl">'
             'al iniciar</span> y <span class="bl">para siempre</span> ya están puestos.',
             'Monta el programa. Los bloques azules están en ' + cat('basico', 'Básico') +
             '. Arrastra <span class="bl">mostrar cadena</span> dentro de <span class="bl">al '
             'iniciar</span> y escribe <strong>tu nombre</strong> en vez de «Hola».',
             'Mira el <strong>simulador</strong> de la izquierda: la placa dibujada hace lo mismo '
             'que hará la de verdad.',
             'Cambia el corazón por otro dibujo del desplegable y las pausas por '
             '<strong>200</strong>. ¿Parpadea más rápido o más lento?',
             'Pon el programa en la placa de verdad siguiendo la entrega de abajo. Fíjate en que '
             'sigue funcionando aunque desconectes el USB y la enchufes a la pila.'])),

        ('Lo has conseguido si…',
         logros(['Al arrancar, la placa escribe tu nombre.',
                 'Después, un dibujo parpadea sin parar.',
                 'Sabes decir qué va en <span class="bl">al iniciar</span> y qué va en '
                 '<span class="bl">para siempre</span>.',
                 'Lo has probado en el simulador y en la placa.'])),
    ],
    siguiente=('r02', 'Reto 2 · El corazón que late'))

# ============================================================ R2 · El corazón que late
P2 = [SIEMPRE([ICONO('corazón'), PAUSA(500), ICONO('corazón pequeño'), PAUSA(500)])]
CORAZON_LEDS = [LEDS('.#.#.:#####:#####:.###.:..#..')]

r02 = pagina(
    'r02', 'Reto 2', 'El corazón que late',
    'Reto 2 de micro:bit: animación alternando dos iconos con pausas. Qué pasa sin pausa. '
    'Dibujar con mostrar LEDs. CyR 1º ESO.',
    'un corazón que <strong>late</strong>: se hace grande y pequeño una y otra vez. Es la '
    'misma idea que la animación por disfraces de Scratch, con la pausa como pieza clave.',
    [
        ('Lee este programa',
         caja(P2, 'Programa: para siempre: mostrar ícono corazón, pausa 500 ms, mostrar ícono '
                  'corazón pequeño, pausa 500 ms') +
         secuencia([
             '<strong>mostrar ícono corazón</strong> enciende el corazón grande.',
             '<strong>pausa (ms) 500</strong> lo deja medio segundo en pantalla.',
             '<strong>mostrar ícono corazón pequeño</strong> lo cambia por el pequeño. Los LEDs '
             'que sobran se apagan solos: no hace falta borrar antes.',
             'Otra pausa, y vuelta al 1. Dos dibujos que se alternan es una '
             '<strong>animación</strong>, exactamente como el gato que caminaba en Scratch.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Quitas las dos pausas. ¿Qué se ve en la placa?',
                  [('rapido', 'El corazón late más rápido',
                    'No exactamente. Va tan rápido que ya no se ve latir: la placa cambia de '
                    'dibujo cientos de veces por segundo.'),
                   ('borron', 'Un corazón grande fijo, con los LEDs del borde algo más apagados',
                    'Correcto. Sin pausa, los dos dibujos se alternan tan deprisa que el ojo '
                    'los mezcla. La pausa es lo que convierte el parpadeo en un latido.'),
                   ('nada', 'La placa da error porque un para siempre no puede estar vacío de '
                    'pausas',
                    'No. Es legal. Lo que pasa es que no se ve lo que quieres.')],
                  'borron')),

        ('Tu reto',
         pasos([
             'Monta el programa y compruébalo en el simulador.',
             'Prueba con pausas de <strong>100</strong>, de <strong>500</strong> y de '
             '<strong>1000</strong>. Quédate con el latido que más te guste.',
             'Cambia los dos iconos por <span class="bl">feliz</span> y <span class="bl">'
             'triste</span>: una cara que cambia de humor.',
             'Ahora dibuja tú: sustituye uno de los <span class="bl">mostrar ícono</span> por '
             '<span class="bl">mostrar LEDs</span> y pincha en los cuadrados de la rejilla para '
             'encenderlos. Haz tu propio corazón, una casa o lo que quieras.',
             'Pásalo a la placa y entrégalo.']) +
         caja(CORAZON_LEDS, 'Bloque mostrar LEDs con un corazón dibujado en la rejilla',
              ancho=360, pie='En <span class="bl">mostrar LEDs</span> tú decides qué LED se '
                             'enciende, cuadrado a cuadrado.')),

        ('Lo has conseguido si…',
         logros(['El corazón late: grande, pequeño, grande, pequeño.',
                 'Has probado tres velocidades y sabes cuál es cuál.',
                 'Uno de los dos dibujos lo has hecho tú con <span class="bl">mostrar LEDs</span>.',
                 'Está en la placa y en Moodle.'])),
    ],
    anterior=('r01', 'Reto 1'), siguiente=('r03', 'Reto 3 · Los botones'))

# ============================================================ R3 · Los botones (eventos)
P3 = [
    BOTON('A', [ICONO('corazón')]),
    BOTON('B', [BORRAR]),
]
P3_AB = [BOTON('A+B', [ICONO('feliz')])]

r03 = pagina(
    'r03', 'Reto 3', 'Los botones: un evento para cada uno',
    'Reto 3 de micro:bit: eventos al presionarse el botón A y B. Qué es un evento. Botón A+B. '
    'CyR 1º ESO.',
    'que la placa <strong>te obedezca</strong>: el botón A enciende un corazón y el botón B lo '
    'apaga. Para eso necesitas los <strong>eventos</strong>, que son la forma normal de usar '
    'los botones.',
    [
        ('La idea: un evento es «cuando pase esto, haz esto»',
         '<p>En Scratch tenías <span class="bl">al presionar tecla espacio</span>: un bloque '
         'con la parte de arriba distinta que arranca solo cuando pasa algo. En MakeCode esos '
         'bloques son planos por arriba, sin muesca, y se llaman <strong>eventos</strong>. '
         'Están en ' + cat('entrada', 'Entrada') + ', en morado.</p>'
         '<p>Un evento no está dentro de <span class="bl">para siempre</span> ni de '
         '<span class="bl">al iniciar</span>: va <strong>suelto</strong> en el espacio de '
         'trabajo, y la placa lo vigila todo el rato. Cuando pulsas el botón, se ejecuta lo '
         'que tiene dentro, una vez por pulsación.</p>'),

        ('Lee este programa',
         caja_varios([[P3[0]], [P3[1]]],
                     'Dos eventos sueltos: al presionarse el botón A, mostrar ícono corazón; '
                     'al presionarse el botón B, borrar la pantalla') +
         secuencia([
             'Al arrancar, la placa no hace nada: no hay <span class="bl">al iniciar</span> ni '
             '<span class="bl">para siempre</span>. Se queda esperando.',
             'Pulsas <strong>A</strong> → se ejecuta el primer evento: aparece el corazón. Y se '
             'queda encendido, porque nadie lo apaga.',
             'Pulsas <strong>B</strong> → se ejecuta el segundo: se apaga.',
             'Puedes pulsar en el orden que quieras, las veces que quieras. Cada evento es '
             'independiente de los otros.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Metes el evento <em>al presionarse el botón A</em> dentro de '
                       '<em>para siempre</em>. ¿Qué pasa?',
                  [('mejor', 'Funciona mejor, porque así lo vigila todo el rato',
                    'No. Los eventos no se pueden meter dentro de otros bloques: MakeCode no te '
                    'deja encajarlo. Ya los vigila la placa sin que hagas nada.'),
                   ('noencaja', 'No encaja: los eventos van siempre sueltos',
                    'Correcto. Un bloque plano por arriba no tiene muesca, así que no se puede '
                    'meter dentro de nada. Va suelto, y la placa lo vigila sola.'),
                   ('dos', 'Se ejecuta dos veces por cada pulsación',
                    'No. Ni siquiera llega a encajar.')],
                  'noencaja')),

        ('Tu reto',
         pasos([
             'Borra lo que haya en el espacio de trabajo (arrástralo a la caja de bloques, que '
             'hace de papelera).',
             'Saca dos veces <span class="bl">al presionarse el botón</span> de ' +
             cat('entrada', 'Entrada') + ' y en uno cambia la <strong>A</strong> por '
             '<strong>B</strong> en el desplegable.',
             'Mete en cada uno lo que corresponda y pruébalo en el simulador: los botones del '
             'dibujo se pulsan con el ratón.',
             'Añade un tercer evento con <strong>A+B</strong> (las dos a la vez) que muestre '
             'una cara feliz. Con una mano, es más difícil de lo que parece.',
             'Pásalo a la placa y entrégalo.']) +
         caja(P3_AB, 'Evento al presionarse el botón A+B con mostrar ícono feliz', ancho=380)),

        ('Lo has conseguido si…',
         logros(['A enciende el corazón y B lo apaga, en el orden que sea.',
                 'A+B muestra otro dibujo.',
                 'Sabes explicar por qué un evento va suelto y no dentro de '
                 '<span class="bl">para siempre</span>.'])),
    ],
    anterior=('r02', 'Reto 2'), siguiente=('r04', 'Reto 4 · Coordenadas'))

# ============================================================ R4 · Coordenadas
P4 = [
    BOTON('A', [GRAFICAR(2, 2)]),
    BOTON('B', [OCULTAR(2, 2)]),
]
CRUZ4 = [BOTON('A', [GRAFICAR(2, 2), GRAFICAR(2, 1), GRAFICAR(2, 3), GRAFICAR(1, 2), GRAFICAR(3, 2)])]

r04 = pagina(
    'r04', 'Reto 4', 'Cada LED tiene su dirección',
    'Reto 4 de micro:bit: coordenadas x e y de la matriz, bloques graficar e ocultar de LED. '
    'CyR 1º ESO.',
    'encender y apagar <strong>un LED concreto</strong>, el que tú digas, usando sus '
    'coordenadas. Con eso se dibuja cualquier cosa, LED a LED.',
    [
        ('La idea: x e y, empezando en cero',
         placa(NADA, 'La matriz con las coordenadas x de 0 a 4 arriba e y de 0 a 4 a la '
                     'izquierda; el LED central, x 2 y 2, está señalado',
               coords=True, marcar=[(2, 2)],
               pie='El LED del centro es x=2, y=2.',
               lado='<p>Cada LED tiene dos números: la <strong>x</strong> dice la columna, de '
                    '0 a 4 de izquierda a derecha; la <strong>y</strong> dice la fila, de 0 a 4 '
                    '<strong>de arriba abajo</strong>. Se empieza a contar en <strong>cero</strong>, '
                    'no en uno.</p>'
                    '<p>Ojo con la <strong>y</strong>: en Scratch, subir era sumar. Aquí la fila '
                    '0 es la de <em>arriba</em> y la 4 la de <em>abajo</em>. Es al revés, y es '
                    'el error más típico de todo el trimestre.</p>')),

        ('Lee este programa',
         caja_varios([[P4[0]], [P4[1]]],
                     'Al presionarse el botón A, graficar x 2 y 2; al presionarse el botón B, '
                     'ocultar x 2 y 2') +
         claves([
             ('graficar x 2 y 2', 'enciende el LED de la columna 2, fila 2: el del centro. '
              'Está en ' + cat('led', 'LED') + '. «Graficar» es la palabra que usa el editor '
              'para «encender».'),
             ('ocultar x 2 y 2', 'lo apaga. Sólo ese; los demás no se tocan.'),
             ('invertir x 2 y 2', 'existe también: si estaba encendido lo apaga y si estaba '
              'apagado lo enciende. Con él, un solo botón hace las dos cosas.')])),

        ('Comprueba que lo has entendido',
         pregunta('1', '¿Qué LED enciende <em>graficar x 4 y 0</em>?',
                  [('abi', 'El de la esquina de abajo a la izquierda',
                    'No. x=4 es la última columna, la de la derecha; y=0 es la primera fila, la '
                    'de arriba.'),
                   ('ard', 'El de la esquina de arriba a la derecha',
                    'Correcto. x=4 es la columna de más a la derecha, y=0 la fila de arriba.'),
                   ('abd', 'El de la esquina de abajo a la derecha',
                    'La columna sí es la derecha, pero y=0 es arriba, no abajo. La fila de '
                    'abajo es y=4.')],
                  'ard')),

        ('Tu reto',
         pasos([
             'Monta el programa. <span class="bl">graficar</span> y <span class="bl">ocultar'
             '</span> están en ' + cat('led', 'LED') + '.',
             'Prueba en el simulador con otras coordenadas hasta que aciertes a la primera '
             'qué LED se va a encender.',
             'Cambia el evento de A para que encienda una <strong>cruz</strong>: el LED central '
             'y los cuatro que lo rodean. Son cinco <span class="bl">graficar</span> seguidos.',
             'Haz que B la apague entera (o usa <span class="bl">borrar la pantalla</span>, que '
             'para eso está).',
             'Pásalo a la placa y entrégalo.']) +
         caja(CRUZ4, 'Al presionarse el botón A: graficar x 2 y 2, x 2 y 1, x 2 y 3, x 1 y 2, x 3 y 2',
              ancho=420, pie='La cruz: el centro y sus cuatro vecinos.') +
         amplia(['<a href="a01.html">Ampliación 1 · Dibujar el «1» LED a LED</a>: un número que '
                 'aparece poco a poco y se borra al revés.'])),

        ('Lo has conseguido si…',
         logros(['Dices sin dudar qué LED es x=0, y=4.',
                 'A dibuja la cruz y B la quita.',
                 'No has confundido la fila de arriba con la de abajo (o lo has arreglado).'])),
    ],
    anterior=('r03', 'Reto 3'), siguiente=('r05', 'Reto 5 · Luz automática'))

# ============================================================ R5 · Luz automática
MEDIR5 = [SIEMPRE([NUMERO(LUZ), PAUSA(500)])]
P5 = [SIEMPRE([SINO(compara(LUZ, '<', 25), [LEDS(TODO_ON)], [BORRAR])])]

r05 = pagina(
    'r05', 'Reto 5', 'La luz que se enciende sola',
    'Reto 5 de micro:bit: sensor de luz y condicional si… si no. Medir antes de decidir el '
    'umbral. CyR 1º ESO.',
    'una <strong>luz automática</strong>: cuando la habitación se queda a oscuras, la placa '
    'enciende todos los LEDs; cuando vuelve la luz, los apaga. Hoy usas un sensor por '
    'primera vez y el bloque <strong>si… si no</strong>.',
    [
        ('La idea: un sensor es un número',
         '<p>La micro:bit mide la luz que le llega. No con un ojo aparte: usa los <strong>'
         'propios LEDs</strong> como sensor. Ese valor es un <strong>número de 0 a 255</strong>: '
         '0 es oscuridad total y 255 es un foco encima.</p>'
         '<p>El bloque que lo lee es <span class="bl">nivel de luz</span>, en ' +
         cat('entrada', 'Entrada') + '. Es redondeado: no hace nada solo, sino que '
         '<strong>vale un número</strong>, y se mete en el hueco de otro bloque, igual que '
         '<span class="bl">respuesta</span> en Scratch. Y antes de decidir nada con él, hay que '
         '<strong>mirarlo</strong>.</p>'),

        ('Primero mide',
         caja(MEDIR5, 'Para siempre: mostrar número nivel de luz, pausa 500 ms',
              pie='El programa de medir: enseña el valor cada medio segundo.') +
         '<p>Ponlo en la placa y tapa la matriz con la mano: verás bajar el número. Apunta '
         'cuánto marca con luz y cuánto tapada. El <strong>umbral</strong> del reto (el 25 de '
         'abajo) tiene que estar entre los dos.</p>'),

        ('Lee este programa',
         caja(P5, 'Para siempre: si nivel de luz es menor que 25 entonces mostrar LEDs todos '
                  'encendidos; si no, borrar la pantalla') +
         secuencia([
             'El <strong>para siempre</strong> repite la comprobación sin parar: por eso la luz '
             'reacciona en cuanto tapas el sensor.',
             '<strong>si … entonces … si no</strong> está en ' + cat('logica', 'Lógica') +
             '. En el hueco hexagonal va una pregunta de sí o no.',
             'La pregunta es <strong>nivel de luz &lt; 25</strong>: el bloque de comparar (el '
             'de <span class="bl">0 &lt; 0</span>, también de Lógica) con el sensor metido en '
             'su primer hueco.',
             'Si es verdad (hay poca luz), <strong>mostrar LEDs</strong> con todos los '
             'cuadrados marcados: la placa se convierte en linterna.',
             'Si no, <strong>borrar la pantalla</strong>. Y vuelta a comprobar.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Cambias el <em>&lt;</em> por un <em>&gt;</em> y no tocas nada más. ¿Qué '
                       'hace ahora la placa?',
                  [('igual', 'Lo mismo, porque 25 sigue siendo el umbral',
                    'No. El umbral es el mismo, pero la pregunta es la contraria.'),
                   ('inverso', 'Se enciende cuando hay luz y se apaga a oscuras',
                    'Correcto. Ahora la condición es «hay más luz que 25», así que enciende de '
                    'día y apaga de noche: justo al revés de una luz automática.'),
                   ('siempre', 'Se queda siempre encendida',
                    'No. Sólo si el nivel de luz fuera siempre mayor que 25, y tapando la placa '
                    'baja de ahí.')],
                  'inverso')),

        ('Tu reto',
         pasos([
             'Haz primero el programa de medir y apunta tus dos valores (con luz, tapado).',
             'Monta el programa de la luz automática y pon de umbral un número entre tus dos '
             'valores. Si en tu aula 25 no sirve, cámbialo: el número es tuyo.',
             'Pruébalo tapando la placa con la mano y destapándola.',
             'Cambia la linterna por un dibujo: una luna cuando está oscuro y un sol (o '
             '<span class="bl">mostrar ícono</span> el que sea) cuando hay luz.',
             'Pásalo a la placa y entrégalo.']) +
         ojo('Se enciende y se apaga sola muy deprisa',
             '<p>Si el nivel de luz está justo en el umbral, la placa duda: enciende, y al '
             'encender los LEDs hay más luz, así que apaga, y al apagar hay menos, así que '
             'enciende… Añade una <span class="bl">pausa (ms) 500</span> al final del '
             '<span class="bl">para siempre</span> y se calma.</p>') +
         amplia(['<a href="a02.html">Ampliación 2 · Termostato</a>: lo mismo con la '
                 'temperatura en vez de la luz.',
                 '<a href="a03.html">Ampliación 3 · Brillo al revés</a>: cuanta menos luz, más '
                 'brillan los LEDs, sin ningún «si».',
                 '<a href="a04.html">Ampliación 4 · Termómetro de barras</a>: varias filas '
                 'según la temperatura.'])),

        ('Lo has conseguido si…',
         logros(['Has medido antes de programar y tu umbral sale de esa medida.',
                 'A oscuras se enciende; con luz se apaga.',
                 'Sabes leer en voz alta el bloque <span class="bl">si nivel de luz &lt; 25 '
                 'entonces</span>.'])),
    ],
    anterior=('r04', 'Reto 4'), siguiente=('r06', 'Reto 6 · Contador de turnos'))

# ============================================================ R6 · Contador de turnos
P6 = [
    INICIAR([FIJAR('turno', 0), NUMERO(var('turno'))]),
    BOTON('A', [CAMBIAR('turno', 1), NUMERO(var('turno'))]),
    BOTON('B', [SI(compara(var('turno'), '>', 0), [CAMBIAR('turno', -1)]), NUMERO(var('turno'))]),
]
CERO6 = [BOTON('A+B', [FIJAR('turno', 0), ICONO('triste')])]

r06 = pagina(
    'r06', 'Reto 6', 'El contador de turnos',
    'Reto 6 de micro:bit: variables. Crear una variable, fijar, cambiar por, mostrar número. '
    'Contador que no baja de cero. CyR 1º ESO.',
    'la máquina de turnos de la carnicería: A suma uno, B resta uno y el número nunca baja de '
    'cero. Para recordar el número necesitas una <strong>variable</strong>, la misma idea que '
    'los puntos en Scratch.',
    [
        ('La idea: una caja con nombre',
         '<p>Una variable es una caja donde la placa guarda un número, con un nombre para '
         'encontrarla. Se crea en ' + cat('variables', 'Variables') + ' con el botón '
         '<strong>Crear una variable…</strong>. Ponle <strong>turno</strong>. Al crearla '
         'aparecen tres bloques:</p>' +
         claves([
             ('fijar turno a 0', 'mete un número en la caja, borrando el que hubiera. Es el '
              '<span class="bl">dar a … el valor</span> de Scratch.'),
             ('cambiar turno por 1', 'suma al número que ya hay. Con <strong>-1</strong>, '
              'resta.'),
             ('turno', 'el redondeado: vale lo que hay en la caja, y se mete en huecos de otros '
              'bloques.')])),

        ('Lee este programa',
         caja_varios([[P6[0]], [P6[1]], [P6[2]]],
                     'Al iniciar: fijar turno a 0 y mostrar número turno. Al presionarse el botón '
                     'A: cambiar turno por 1 y mostrar número turno. Al presionarse el botón B: si '
                     'turno es mayor que 0 entonces cambiar turno por -1; mostrar número turno') +
         secuencia([
             '<strong>al iniciar</strong> pone la caja a 0 y lo enseña. Sin este bloque el '
             'contador también empezaría en 0, pero es mejor decirlo: así el programa se lee '
             'solo.',
             'Cada pulsación de <strong>A</strong> suma 1 y vuelve a enseñar el número. Si no '
             'lo enseñas, la caja cambia por dentro pero tú no te enteras.',
             '<strong>B</strong> resta 1, pero <em>sólo si el turno es mayor que 0</em>. Esa '
             'es la condición que evita el −1.',
             'El <strong>mostrar número</strong> de B está <em>fuera</em> del <span class="bl">'
             'si</span>: se enseña el número siempre, haya restado o no.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Sacas el <em>mostrar número</em> de B y lo metes dentro del <em>si</em>, '
                       'debajo de <em>cambiar turno por -1</em>. El turno vale 0 y pulsas B. ¿Qué '
                       'se ve?',
                  [('cero', 'Un 0, igual que antes',
                    'No. Como el turno no es mayor que 0, no se entra en el si, y ahora el '
                    'mostrar número está dentro.'),
                   ('nada', 'Nada cambia en la pantalla: se queda lo que hubiera',
                    'Correcto. El si no se cumple, así que no se ejecuta nada de lo que hay '
                    'dentro, tampoco el mostrar. Por eso estaba fuera.'),
                   ('menos', 'Un −1',
                    'No. La condición sigue protegiendo el cero: no se resta.')],
                  'nada')),

        ('Tu reto',
         pasos([
             'Crea la variable <strong>turno</strong> y monta los tres eventos.',
             'Pruébalo en el simulador: sube, baja, e intenta bajar de cero.',
             'Añade <strong>A+B</strong>: pone el turno a cero y muestra una cara triste '
             '(«no quedan turnos»).',
             'Cambia el programa para que sea el marcador de un partido: A suma 1 a '
             '<strong>local</strong> y B a <strong>visitante</strong>. Necesitas dos '
             'variables. ¿Cómo enseñas los dos números?',
             'Pásalo a la placa y entrégalo.']) +
         caja(CERO6, 'Al presionarse el botón A+B: fijar turno a 0, mostrar ícono triste', ancho=380) +
         ojo('Los números de dos cifras se desplazan',
             '<p>Un 7 cabe en la pantalla, un 12 no: la placa lo hace pasar deslizándose, y '
             'tarda casi un segundo. Es normal. Si pulsas muy rápido, verás que se pierde '
             'alguna pulsación mientras el número pasa.</p>')),

        ('Lo has conseguido si…',
         logros(['A sube, B baja y nunca aparece un número negativo.',
                 'A+B vuelve a cero.',
                 'Sabes cuál es la diferencia entre <span class="bl">fijar</span> y '
                 '<span class="bl">cambiar por</span>.'])),
    ],
    anterior=('r05', 'Reto 5'), siguiente=('r07', 'Reto 7 · El interruptor'))

# ============================================================ R7 · El interruptor
P7 = [
    INICIAR([FIJAR('encendido', FALSO)]),
    BOTON('A', [SINO(var('encendido'),
                     [BORRAR, FIJAR('encendido', FALSO)],
                     [ICONO('corazón'), FIJAR('encendido', VERDADERO)])]),
]

r07 = pagina(
    'r07', 'Reto 7', 'El interruptor: un botón, dos estados',
    'Reto 7 de micro:bit: variable booleana verdadero/falso que guarda el estado. Un solo botón '
    'que enciende y apaga. CyR 1º ESO.',
    'un <strong>interruptor</strong>: el mismo botón enciende el corazón si estaba apagado y lo '
    'apaga si estaba encendido. Para saber en qué estado está, la placa necesita '
    '<strong>acordarse</strong>: una variable que vale verdadero o falso.',
    [
        ('La idea: acordarse de en qué estado estás',
         '<p>En el reto 3, A encendía y B apagaba. Con un solo botón la placa tiene que '
         'decidir qué toca, y para eso guarda el <strong>estado</strong> en una variable: '
         '<strong>encendido</strong>, que vale <span class="bl">verdadero</span> o '
         '<span class="bl">falso</span> (los dos bloques están en ' + cat('logica', 'Lógica') +
         '). A una variable así se la llama <strong>booleana</strong>: sólo tiene dos '
         'valores posibles.</p>'),

        ('Lee este programa',
         caja_varios([[P7[0]], [P7[1]]],
                     'Al iniciar: fijar encendido a falso. Al presionarse el botón A: si encendido '
                     'entonces borrar la pantalla y fijar encendido a falso; si no, mostrar ícono '
                     'corazón y fijar encendido a verdadero') +
         secuencia([
             'Al arrancar, <strong>encendido</strong> vale falso: la pantalla está apagada y la '
             'variable lo dice.',
             'Pulsas A. El <strong>si</strong> mira la variable. Como es falso, entra por el '
             '<strong>si no</strong>: enciende el corazón y <em>apunta</em> que ahora está '
             'encendido.',
             'Pulsas A otra vez. Ahora la variable es verdadero: entra por arriba, borra la '
             'pantalla y apunta que está apagado.',
             'Lo importante: <strong>cada rama termina cambiando la variable</strong>. Si se '
             'te olvida, el interruptor se queda atascado en un estado.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Quitas el <em>fijar encendido a verdadero</em> de la rama del <em>si no'
                       '</em>. ¿Qué hace el botón?',
                  [('igual', 'Lo mismo: la placa ya sabe que el corazón está encendido',
                    'No. La placa no «ve» la pantalla; sólo sabe lo que dice la variable. Y '
                    'nadie la ha cambiado.'),
                   ('solo', 'Enciende el corazón y ya nunca lo apaga',
                    'Correcto. La variable se queda en falso para siempre, así que cada '
                    'pulsación entra por el si no y vuelve a encender. El estado se ha quedado '
                    'atascado.'),
                   ('apaga', 'Apaga el corazón a la primera pulsación',
                    'No. Al arrancar la variable es falso, y con falso se entra por el si no, '
                    'que enciende.')],
                  'solo')),

        ('Tu reto',
         pasos([
             'Crea la variable <strong>encendido</strong> y monta el programa. El bloque '
             '<span class="bl">falso</span> se mete en el hueco de <span class="bl">fijar</span>.',
             'Pruébalo: A, A, A, A. Encendido, apagado, encendido, apagado.',
             'Añade una segunda variable, <strong>veces</strong>, que cuente cuántas veces has '
             'pulsado A (el contador del reto 6), y que B la muestre.',
             'Difícil: tres estados en vez de dos. A pasa de apagado → corazón → cara feliz → '
             'apagado. Pista: ya no vale verdadero/falso; usa un número 0, 1, 2.',
             'Pásalo a la placa y entrégalo.'])),

        ('Lo has conseguido si…',
         logros(['Un solo botón enciende y apaga, alternando.',
                 'B te dice cuántas veces has pulsado A.',
                 'Sabes explicar por qué hace falta la variable: la placa no ve su propia '
                 'pantalla.'])),
    ],
    anterior=('r06', 'Reto 6'), siguiente=('r08', 'Reto 8 · Cronómetro'))

# ============================================================ R8 · Cronómetro
P8 = [
    INICIAR([FIJAR('segundos', 0), FIJAR('corriendo', FALSO)]),
    SIEMPRE([SI(var('corriendo'), [CAMBIAR('segundos', 1), NUMERO(var('segundos')), PAUSA(1000)])]),
    BOTON('A', [FIJAR('corriendo', VERDADERO)]),
    BOTON('B', [FIJAR('corriendo', FALSO)]),
    BOTON('A+B', [FIJAR('segundos', 0), FIJAR('corriendo', FALSO), BORRAR]),
]

r08 = pagina(
    'r08', 'Reto 8', 'El cronómetro',
    'Reto 8 de micro:bit: cronómetro con estado, para siempre y tres eventos de botón. A '
    'arranca, B para, A+B pone a cero. CyR 1º ESO.',
    'un <strong>cronómetro</strong>: A lo arranca, B lo para y A+B lo pone a cero. Junta todo '
    'lo que sabes hasta ahora: un bucle que cuenta, una variable de estado y tres eventos.',
    [
        ('La idea: el bucle cuenta, los botones mandan',
         '<p>Quien cuenta los segundos es el <span class="bl">para siempre</span>: cada vuelta '
         'suma uno y espera un segundo. Pero sólo cuenta <em>si le dejan</em>: mira la variable '
         '<strong>corriendo</strong>, y los botones lo único que hacen es cambiar esa variable. '
         'Los eventos <strong>no cuentan nada</strong>; mandan.</p>'
         '<p>Este reparto, un bucle que trabaja y unos eventos que cambian el estado, es el '
         'patrón de casi todos los programas de micro:bit que van a venir.</p>'),

        ('Lee este programa',
         caja_varios([[P8[0]], [P8[1]], [P8[2]], [P8[3]], [P8[4]]],
                     'Al iniciar: segundos a 0, corriendo a falso. Para siempre: si corriendo, '
                     'cambiar segundos por 1, mostrar número segundos, pausa 1000. Botón A: '
                     'corriendo a verdadero. Botón B: corriendo a falso. Botón A+B: segundos a 0, '
                     'corriendo a falso, borrar la pantalla') +
         secuencia([
             'Al arrancar, los segundos están a 0 y el cronómetro parado: la variable '
             '<strong>corriendo</strong> es falso.',
             'El <strong>para siempre</strong> da vueltas, pero como corriendo es falso no entra '
             'en el si: no pasa nada.',
             'Pulsas <strong>A</strong>: corriendo pasa a verdadero. A la siguiente vuelta del '
             'bucle entra en el si: suma 1, enseña el número y espera un segundo. Y otra vez.',
             '<strong>B</strong> pone corriendo a falso: el bucle sigue dando vueltas, pero ya no '
             'entra en el si. El número se queda en pantalla.',
             '<strong>A+B</strong> lo deja todo como al principio.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Quitas la <em>pausa (ms) 1000</em>. ¿Qué cuenta el cronómetro?',
                  [('igual', 'Segundos, igual que antes: la placa sabe lo que es un segundo',
                    'No. La placa no sabe lo que es un segundo. La pausa es lo único que hace '
                    'que cada vuelta dure un segundo.'),
                   ('rapido', 'Sube a toda velocidad: cada vuelta del bucle suma uno',
                    'Correcto. Sin pausa, el bucle da miles de vueltas por segundo y el número '
                    'se dispara. La pausa es la que convierte «vueltas» en «segundos».'),
                   ('nada', 'Se queda en 0',
                    'No. Sigue sumando, y mucho más deprisa.')],
                  'rapido')),

        ('Tu reto',
         pasos([
             'Crea las dos variables, <strong>segundos</strong> y <strong>corriendo</strong>, y '
             'monta los cinco bloques.',
             'Cronometra algo de verdad: cuánto tarda tu compañero en escribir su nombre en '
             'MakeCode. Compáralo con el reloj del aula.',
             'Cuenta atrás: que empiece en <strong>9</strong>, baje de uno en uno y al llegar a '
             '0 muestre una <span class="bl">mostrar cadena</span> con «FIN». Necesitas un '
             '<span class="bl">si segundos = 0</span> dentro del bucle.',
             'Pásalo a la placa y entrégalo.']) +
         ojo('A partir de 10 se atrasa',
             '<p>Un número de dos cifras no cabe en la pantalla: la placa lo desplaza, y eso '
             'tarda casi un segundo. Así que a partir de 10 tu cronómetro cuenta más despacio '
             'que el reloj. No es un fallo tuyo: es la pantalla. Por eso la cuenta atrás del '
             'reto empieza en 9.</p>')),

        ('Lo has conseguido si…',
         logros(['A arranca, B para y A+B pone a cero, en cualquier orden.',
                 'La cuenta atrás termina en «FIN».',
                 'Sabes decir quién cuenta (el bucle) y quién manda (los botones).'])),
    ],
    anterior=('r07', 'Reto 7'), siguiente=('r09', 'Reto 9 · El bucle para'))


if __name__ == '__main__':
    for n, h in [('r01', r01), ('r02', r02), ('r03', r03), ('r04', r04),
                 ('r05', r05), ('r06', r06), ('r07', r07), ('r08', r08)]:
        escribir(n, h)

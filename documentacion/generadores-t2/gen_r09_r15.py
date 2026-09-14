# -*- coding: utf-8 -*-
"""Retos 9 a 15 del troncal de T2 · micro:bit."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bloques import *                                  # noqa: F401,F403
from plantilla_t2 import (pagina, caja, caja_varios, dos_cajas, placa, cat, bl, amplia,
                          pasos, secuencia, claves, pregunta, pista, ojo, logros, tabla)
from diagramas_t2 import rosa_brujula
from comun_t2 import escribir

# ============================================================ R9 · El bucle para
P9 = [SIEMPRE([PARA('índice', 4, [GRAFICAR(var('índice'), 0), PAUSA(200), OCULTAR(var('índice'), 0)])])]
COL9 = [PARA('índice', 4, [GRAFICAR(0, var('índice')), PAUSA(200)])]

r09 = pagina(
    'r09', 'Reto 9', 'El bucle «para»: una fila que se enciende',
    'Reto 9 de micro:bit: bucle para índice de 0 a 4. La variable índice como coordenada. '
    'Animación de una fila de LEDs. CyR 1º ESO.',
    'que la fila de arriba se encienda LED a LED, de izquierda a derecha, y vuelva a empezar. '
    'Con cinco <span class="bl">graficar</span> se puede; con un <strong>bucle</strong> se '
    'hace con uno solo, y así aprendes el bloque que más trabajo ahorra.',
    [
        ('La idea: un bloque que cuenta por ti',
         '<p>El bloque <span class="bl">para índice de 0 a 4 ejecutar</span>, en ' +
         cat('bucles', 'Bucles') + ', repite lo de dentro <strong>cinco veces</strong>, y en '
         'cada vuelta la variable <strong>índice</strong> vale un número distinto: 0, luego 1, '
         '2, 3 y 4. Tú no la creas ni la cambias: el bucle lo hace solo.</p>'
         '<p>El truco está en usar <strong>índice</strong> como coordenada: '
         '<span class="bl">graficar x índice y 0</span> enciende en cada vuelta un LED distinto '
         'de la misma fila.</p>'),

        ('Lee este programa',
         caja(P9, 'Para siempre: para índice de 0 a 4 ejecutar: graficar x índice y 0, pausa 200 '
                  'ms, ocultar x índice y 0') +
         secuencia([
             'Empieza el <strong>para</strong>: índice vale 0.',
             '<strong>graficar x índice y 0</strong> enciende el LED x=0 de la fila de arriba; '
             '<strong>pausa</strong> 200 ms; <strong>ocultar</strong> lo apaga.',
             'Vuelta siguiente: índice vale 1. Se enciende y apaga el LED x=1. Y así hasta el 4.',
             'Cuando índice ha valido 4, el <strong>para</strong> termina. Como está dentro de '
             '<strong>para siempre</strong>, empieza otra vez desde 0: la luz recorre la fila '
             'sin parar.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Cambias el 4 del bucle por un 2. ¿Cuántos LEDs se encienden en cada '
                       'pasada?',
                  [('dos', 'Dos: el 1 y el 2',
                    'No. El bucle empieza siempre en 0: 0, 1 y 2.'),
                   ('tres', 'Tres: el 0, el 1 y el 2',
                    'Correcto. «De 0 a 2» son tres valores. Es el mismo truco de siempre: se '
                    'empieza a contar en cero.'),
                   ('ninguno', 'Ninguno: un LED con x=2 no existe',
                    'Sí existe: x va de 0 a 4. El 2 es el del centro de la fila.')],
                  'tres')),

        ('Tu reto',
         pasos([
             'Monta el programa. Al sacar el <span class="bl">para</span>, la variable '
             '<strong>índice</strong> aparece sola en ' + cat('variables', 'Variables') +
             '; arrástrala desde ahí a los huecos de la x.',
             'Cámbialo para que recorra la fila de <strong>abajo</strong> (y=4).',
             'Ahora la <strong>columna</strong> de la izquierda, de arriba abajo: índice va en '
             'la y y la x se queda fija en 0.',
             'Quita el <span class="bl">ocultar</span>: la fila se llena en vez de recorrerse. '
             'Añade un <span class="bl">borrar la pantalla</span> al final del '
             '<span class="bl">para siempre</span> para que vuelva a empezar limpia.',
             'Pásalo a la placa y entrégalo.']) +
         caja(COL9, 'Para índice de 0 a 4 ejecutar: graficar x 0 y índice, pausa 200 ms',
              ancho=420, pie='La columna: índice en la y.') +
         amplia(['<a href="a05.html">Ampliación 5 · La fila al revés</a>: de derecha a '
                 'izquierda, con el bucle <span class="bl">mientras</span>.'])),

        ('Lo has conseguido si…',
         logros(['La luz recorre la fila de arriba, luego la de abajo, luego la columna.',
                 'Sabes decir qué valores toma <span class="bl">índice</span> y cuántas vueltas '
                 'da el bucle.',
                 'Has escrito un solo <span class="bl">graficar</span>, no cinco.'])),
    ],
    anterior=('r08', 'Reto 8'), siguiente=('r10', 'Reto 10 · La serpiente'))

# ============================================================ R10 · La serpiente
P10 = [SIEMPRE([
    PARA('fila', 4, [PARA('columna', 4, [GRAFICAR(var('columna'), var('fila')), PAUSA(100)])]),
    PAUSA(500), BORRAR])]

r10 = pagina(
    'r10', 'Reto 10', 'La serpiente: un bucle dentro de otro',
    'Reto 10 de micro:bit: bucles anidados para recorrer toda la matriz LED a LED. Renombrar la '
    'variable del bucle. CyR 1º ESO.',
    'que la luz recorra <strong>los 25 LEDs</strong>, fila a fila, como una serpiente que va '
    'llenando la pantalla. Un bucle recorre una fila; para recorrer todas las filas hace falta '
    'un bucle <strong>dentro</strong> de otro.',
    [
        ('La idea: el de dentro corre, el de fuera cambia de fila',
         '<p>El bucle de dentro es el del reto anterior: recorre las cinco columnas de una '
         'fila. El de fuera cambia de fila. Cada vuelta del de fuera obliga al de dentro a '
         'hacer <em>sus cinco vueltas enteras</em>: 5 filas × 5 columnas = 25 LEDs.</p>'
         '<p>Como hay dos bucles, hacen falta dos variables con nombres distintos. El bloque '
         'trae <strong>índice</strong>; en el desplegable de la variable puedes elegir '
         '<strong>Renombrar la variable…</strong> y llamarlas <strong>fila</strong> y '
         '<strong>columna</strong>. Con nombres que dicen lo que son, el programa se lee solo.</p>'),

        ('Lee este programa',
         caja(P10, 'Para siempre: para fila de 0 a 4 ejecutar: para columna de 0 a 4 ejecutar: '
                   'graficar x columna y fila, pausa 100 ms. Después, pausa 500 ms y borrar la '
                   'pantalla') +
         secuencia([
             '<strong>fila</strong> vale 0. Arranca el bucle de dentro.',
             '<strong>columna</strong> vale 0, 1, 2, 3, 4: se encienden los cinco LEDs de la '
             'fila 0, uno cada 100 ms.',
             'Termina el bucle de dentro. El de fuera pasa a <strong>fila = 1</strong> y el de '
             'dentro vuelve a empezar desde columna 0.',
             'Así hasta la fila 4. Cuando termina el de fuera, la pantalla está llena.',
             '<strong>pausa 500</strong> para verla llena, <strong>borrar la pantalla</strong>, y '
             'el <span class="bl">para siempre</span> lo repite todo.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Intercambias las variables en <em>graficar</em>: pones <em>x fila y '
                       'columna</em>. ¿Qué cambia?',
                  [('nada', 'Nada: se encienden los mismos 25 LEDs',
                    'Se encienden los mismos 25 al final, sí, pero en otro orden. Mira en qué '
                    'orden los va encendiendo.'),
                   ('columnas', 'La serpiente va por columnas, de arriba abajo, en vez de por '
                    'filas',
                    'Correcto. Ahora la que cambia rápido (columna) es la y, así que la luz '
                    'baja por una columna antes de pasar a la siguiente.'),
                   ('error', 'Da error: fila tiene que ir en la y',
                    'No. Para el bloque son dos números; los nombres son para ti.')],
                  'columnas')),

        ('Tu reto',
         pasos([
             'Monta los dos bucles, uno dentro de otro, y renombra las variables.',
             'Hazlo funcionar y mira si el orden es fila a fila, de izquierda a derecha.',
             'Serpiente de verdad: que cada LED se apague justo después de encenderse (añade '
             '<span class="bl">ocultar</span> tras la pausa) y la luz «corra» por toda la '
             'pantalla.',
             'Zigzag: en las filas impares, que vaya de derecha a izquierda. Pista: necesitas '
             'un <span class="bl">si</span> y una resta, <span class="bl">4 − columna</span>, '
             'de ' + cat('matematica', 'Matemática') + '.',
             'Pásalo a la placa y entrégalo.'])),

        ('Lo has conseguido si…',
         logros(['La pantalla se llena fila a fila y se borra.',
                 'Sabes decir cuántas veces se ejecuta <span class="bl">graficar</span> en una '
                 'pasada (25) y por qué.',
                 'Las variables se llaman fila y columna, no índice e índice2.'])),
    ],
    anterior=('r09', 'Reto 9'), siguiente=('r11', 'Reto 11 · El dado'))

# ============================================================ R11 · El dado
P11 = [
    INICIAR([ICONO('cuadrado')]),
    GESTO('agitado', [FIJAR('dado', azar(1, 6)), NUMERO(var('dado'))]),
]
ANIM11 = [GESTO('agitado', [ICONO('cuadrado pequeño'), PAUSA(150), ICONO('cuadrado'), PAUSA(150),
                            FIJAR('dado', azar(1, 6)), NUMERO(var('dado'))])]

r11 = pagina(
    'r11', 'Reto 11', 'El dado: agitar y azar',
    'Reto 11 de micro:bit: evento si agitado y bloque escoger al azar. Dado electrónico. CyR 1º '
    'ESO.',
    'un <strong>dado</strong>: agitas la placa y sale un número del 1 al 6. Dos bloques nuevos: '
    'el evento de <strong>agitar</strong> y el <strong>azar</strong>.',
    [
        ('La idea: la placa nota que la mueves',
         '<p>La micro:bit lleva un <strong>acelerómetro</strong>, el mismo sensor que hace que '
         'el móvil gire la pantalla. Con él sabe si la agitas, si la inclinas o si se cae. En '
         '' + cat('entrada', 'Entrada') + ' está el evento <span class="bl">si agitado</span>: '
         'se lee raro, pero es el «al agitar». En el simulador se prueba con el botón '
         '<strong>SHAKE</strong> que aparece al pasar el ratón por la placa dibujada.</p>'
         '<p>El otro bloque nuevo es <span class="bl">escoger al azar de 1 a 6</span>, en ' +
         cat('matematica', 'Matemática') + ': cada vez que se ejecuta vale un número distinto '
         'entre los dos que le digas. Es el <span class="bl">número aleatorio</span> de '
         'Scratch.</p>'),

        ('Lee este programa',
         caja_varios([[P11[0]], [P11[1]]],
                     'Al iniciar: mostrar ícono cuadrado. Si agitado: fijar dado a escoger al azar '
                     'de 1 a 6, mostrar número dado') +
         secuencia([
             'Al arrancar, un cuadrado: es el dado «en reposo», para que se vea que la placa '
             'está lista.',
             'Agitas. El evento guarda en <strong>dado</strong> un número al azar del 1 al 6.',
             '<strong>mostrar número dado</strong> lo enseña. Se queda hasta que vuelves a '
             'agitar.',
             '¿Por qué guardar el azar en una variable en vez de meterlo directamente en '
             '<span class="bl">mostrar número</span>? Porque en el siguiente reto vas a '
             'necesitar <em>preguntar</em> por ese número, y para eso hay que tenerlo guardado.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Pones <em>escoger al azar de 1 a 6</em> directamente dentro de <em>mostrar '
                       'número</em>, sin variable, y además otro igual dentro de un <em>si</em>. '
                       '¿Son el mismo número?',
                  [('si', 'Sí: el azar se elige una vez por agitada',
                    'No. Cada bloque de azar elige su propio número cada vez que se ejecuta. '
                    'Dos bloques, dos números.'),
                   ('no', 'No: cada bloque de azar saca un número distinto',
                    'Correcto. Por eso se guarda en una variable: se elige una vez y se usa '
                    'las veces que haga falta.'),
                   ('error', 'MakeCode no deja poner dos bloques de azar',
                    'Sí deja. El problema no es que no se pueda, es que no hacen lo que '
                    'quieres.')],
                  'no')),

        ('Tu reto',
         pasos([
             'Crea la variable <strong>dado</strong> y monta el programa. Pruébalo con SHAKE en '
             'el simulador y agitando la placa.',
             'Dale emoción: antes del número, dos iconos rápidos (cuadrado pequeño, cuadrado) '
             'como si el dado rodara.',
             'Haz también que <strong>A</strong> tire el dado, para quien no quiera agitar.',
             'Un dado de <strong>20</strong> para rol: cambia el 6 y fíjate en cómo pasan los '
             'números de dos cifras.',
             'Pásalo a la placa y entrégalo.']) +
         caja(ANIM11, 'Si agitado: mostrar ícono cuadrado pequeño, pausa 150, mostrar ícono '
                      'cuadrado, pausa 150, fijar dado a escoger al azar de 1 a 6, mostrar número '
                      'dado', ancho=460)),

        ('Lo has conseguido si…',
         logros(['Al agitar sale un número del 1 al 6 y se queda en pantalla.',
                 'Hay una pequeña animación antes del número.',
                 'Sabes explicar por qué el azar se guarda en una variable.'])),
    ],
    anterior=('r10', 'Reto 10'), siguiente=('r12', 'Reto 12 · Piedra, papel o tijera'))

# ============================================================ R12 · Piedra, papel o tijera
P12 = [GESTO('agitado', [
    FIJAR('mano', azar(1, 3)),
    CASCADA([(compara(var('mano'), '=', 1), [ICONO('cuadrado pequeño')]),
             (compara(var('mano'), '=', 2), [ICONO('cuadrado')])],
            sino=[ICONO('tijeras')])])]
MARCADOR12 = [
    BOTON('A', [CAMBIAR('yo', 1), NUMERO(var('yo'))]),
    BOTON('B', [CAMBIAR('rival', 1), NUMERO(var('rival'))]),
]

r12 = pagina(
    'r12', 'Reto 12', 'Piedra, papel o tijera',
    'Reto 12 de micro:bit: si… si no, si… si no en cascada para elegir entre tres opciones. '
    'Juego con azar y agitar. CyR 1º ESO.',
    'el clásico: agitas y la placa saca <strong>piedra</strong> (cuadrado pequeño), '
    '<strong>papel</strong> (cuadrado grande) o <strong>tijera</strong>. Es el dado del reto '
    'anterior, pero ahora el número hay que <strong>traducirlo</strong> a un dibujo, y para '
    'tres opciones un solo <span class="bl">si… si no</span> no basta.',
    [
        ('La idea: preguntar en cascada',
         '<p>Con dos opciones bastaba un <span class="bl">si… si no</span>. Con tres hace '
         'falta preguntar otra vez dentro del «si no»: <strong>si no, si…</strong>. El bloque '
         '<span class="bl">si</span> de ' + cat('logica', 'Lógica') + ' tiene un '
         '<strong>+</strong> en la esquina de abajo: cada vez que lo pulsas añade una rama '
         '<span class="bl">si no, si</span>. La última, <span class="bl">si no</span> a secas, '
         'recoge lo que no ha entrado en ninguna de las anteriores.</p>'
         '<p>Se lee de arriba abajo y <strong>sólo entra en una rama</strong>: en cuanto una '
         'condición es verdad, las demás ni se miran.</p>'),

        ('Lee este programa',
         caja(P12, 'Si agitado: fijar mano a escoger al azar de 1 a 3; si mano = 1 entonces mostrar '
                   'ícono cuadrado pequeño; si no, si mano = 2 entonces mostrar ícono cuadrado; si '
                   'no, mostrar ícono tijeras') +
         secuencia([
             'Agitas: <strong>mano</strong> guarda un 1, un 2 o un 3.',
             '<strong>¿mano = 1?</strong> Si sí, piedra, y se acabó: no se mira nada más.',
             'Si no, <strong>¿mano = 2?</strong> Si sí, papel.',
             'Si tampoco, sólo queda una posibilidad: tijera. Por eso la última rama no '
             'pregunta nada.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Cambias el azar a <em>de 1 a 4</em> y no tocas las ramas. Sale un 4. ¿Qué '
                       'se ve?',
                  [('nada', 'Nada: el 4 no está en ninguna rama',
                    'No. El «si no» final no pregunta: recoge todo lo que no ha entrado antes, y '
                    'el 4 no ha entrado en ninguna.'),
                   ('tijera', 'Tijera: el si no final se lleva todo lo que no es 1 ni 2',
                    'Correcto. La rama «si no» no comprueba nada; es la red de seguridad. Por '
                    'eso hay que tener claro qué cae en ella.'),
                   ('error', 'La placa da error porque mano vale 4',
                    'No. Un número es un número. La placa no sabe que sólo esperabas tres.')],
                  'tijera')),

        ('Tu reto',
         pasos([
             'Crea la variable <strong>mano</strong>, monta el programa y añade las ramas con '
             'el <strong>+</strong> del bloque <span class="bl">si</span>.',
             'Juega contra tu pareja: agitáis a la vez y comparáis.',
             'Marcador: dos variables más, <strong>yo</strong> y <strong>rival</strong>. A suma '
             'un punto al que ha ganado tú, B al rival, y cada uno enseña su cuenta.',
             'Difícil: que A+B enseñe los dos marcadores seguidos con una pausa entre medias.',
             'Pásalo a la placa y entrégalo.']) +
         caja_varios([[MARCADOR12[0]], [MARCADOR12[1]]],
                     'Al presionarse el botón A: cambiar yo por 1, mostrar número yo. Al presionarse '
                     'el botón B: cambiar rival por 1, mostrar número rival', ancho=420)),

        ('Lo has conseguido si…',
         logros(['Al agitar sale uno de los tres dibujos, y los tres salen alguna vez.',
                 'El marcador de A y B funciona.',
                 'Sabes explicar qué recoge el <span class="bl">si no</span> final.'])),
    ],
    anterior=('r11', 'Reto 11'), siguiente=('r13', 'Reto 13 · Radio'))

# ============================================================ R13 · Radio
P13 = [
    INICIAR([GRUPO(7), CADENA('OK')]),
    BOTON('A', [ENVIAR(1), ICONO('sí')]),
    RECIBIR([ICONO('corazón'), PAUSA(1000), BORRAR]),
]
CHAT13 = [
    BOTON('B', [ENVIAR(2)]),
    RECIBIR([SINO(compara(RECIBIDO, '=', 1), [ICONO('feliz')], [ICONO('triste')]),
             PAUSA(1000), BORRAR]),
]

r13 = pagina(
    'r13', 'Reto 13', 'Radio: dos placas que se hablan',
    'Reto 13 de micro:bit: radio. Establecer grupo, enviar número, al recibir radio. Dos placas '
    'con el mismo programa. CyR 1º ESO.',
    'que tu placa <strong>mande un mensaje</strong> a la de otra pareja sin cables: pulsas A y '
    'en la otra aparece un corazón. Las dos placas llevan <strong>el mismo programa</strong>.',
    [
        ('La idea: un grupo es un canal',
         '<p>La micro:bit tiene <strong>radio</strong>: puede mandar números y textos a otras '
         'placas a unos metros de distancia. Para no mezclarse con las demás de la clase, '
         'cada pareja de placas se pone en un <strong>grupo</strong>, un número del 0 al 255. '
         'Sólo se oyen las placas del mismo grupo; es como sintonizar la misma emisora.</p>'
         '<p>Este reto se hace <strong>entre dos parejas</strong>: cada una programa su placa '
         'con el mismo programa y el mismo número de grupo, y os ponéis un número que no use '
         'nadie más en el aula. Los bloques están en ' + cat('radio', 'Radio') + '.</p>'),

        ('Lee este programa',
         caja_varios([[P13[0]], [P13[1]], [P13[2]]],
                     'Al iniciar: radio establecer grupo 7, mostrar cadena OK. Al presionarse el '
                     'botón A: radio enviar número 1, mostrar ícono sí. Al recibir radio '
                     'receivedNumber: mostrar ícono corazón, pausa 1000, borrar la pantalla') +
         secuencia([
             '<strong>al iniciar</strong> sintoniza el grupo 7 y escribe «OK» para que sepas que '
             'ha arrancado. Cambiad el 7 por vuestro número.',
             'Pulsas <strong>A</strong>: tu placa <strong>envía el número 1</strong> por radio y '
             'te enseña un tic para que sepas que ha salido.',
             '<strong>al recibir radio</strong> es un evento: se ejecuta en la <em>otra</em> '
             'placa cuando le llega algo. Lo que llega se guarda en '
             '<span class="bl">receivedNumber</span> (el nombre sale en inglés, es así).',
             'La otra placa enseña un corazón un segundo y lo borra. Como las dos llevan el '
             'mismo programa, funciona en los dos sentidos.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Otra pareja del aula ha puesto también el grupo 7. Pulsas A. ¿Quién ve '
                       'el corazón?',
                  [('nadie', 'Nadie: al haber tres placas, la radio se bloquea',
                    'No. La radio no se bloquea; simplemente todas las del grupo oyen.'),
                   ('todas', 'Las dos placas del grupo 7 que no son la tuya',
                    'Correcto. La radio es como hablar en voz alta: lo oye todo el que esté en '
                    'el mismo grupo. Por eso cada dos parejas necesitan un número propio.'),
                   ('una', 'Sólo la placa de tu pareja de radio',
                    'No. La placa no sabe quién es «tu pareja»: envía al grupo entero.')],
                  'todas')),

        ('Tu reto',
         pasos([
             'Acordad con la otra pareja un número de grupo que no use nadie más, y montad las '
             'dos placas con el mismo programa.',
             'Probadlo: A en una, corazón en la otra. Y al revés.',
             'Chat de dos mensajes: <strong>A</strong> envía 1 y <strong>B</strong> envía 2. Al '
             'recibir, si el número es 1 cara feliz, si no cara triste.',
             'Alejaos por el pasillo pulsando A: ¿hasta dónde llega?',
             'Pásalo a la placa y entrégalo.']) +
         caja_varios([[CHAT13[0]], [CHAT13[1]]],
                     'Al presionarse el botón B: radio enviar número 2. Al recibir radio '
                     'receivedNumber: si receivedNumber = 1 entonces mostrar ícono feliz, si no '
                     'mostrar ícono triste; pausa 1000; borrar la pantalla', ancho=520) +
         ojo('El simulador no habla con la placa',
             '<p>En el simulador, cuando usas radio aparece una segunda placa dibujada: sirve '
             'para probar. Pero el simulador no envía nada a una placa de verdad: para eso '
             'hacen falta dos placas reales.</p>') +
         amplia(['<a href="a12.html">Ampliación 12 · Dos jugadores por radio</a>: cada placa '
                 'mueve un punto y, cuando coinciden, las dos muestran un corazón.'])),

        ('Lo has conseguido si…',
         logros(['A en una placa enciende el corazón en la otra, en los dos sentidos.',
                 'El chat distingue el 1 del 2.',
                 'Sabéis explicar qué es el grupo y por qué no puede repetirse.'])),
    ],
    anterior=('r12', 'Reto 12'), siguiente=('r14', 'Reto 14 · La brújula'))

# ============================================================ R14 · La brújula
P14 = [SIEMPRE([
    FIJAR('grados', BRUJULA),
    CASCADA([(O(compara(var('grados'), '<', 45), compara(var('grados'), '>', 315)), [CADENA('N')]),
             (compara(var('grados'), '<', 135), [CADENA('E')]),
             (compara(var('grados'), '<', 225), [CADENA('S')])],
            sino=[CADENA('O')])])]

r14 = pagina(
    'r14', 'Reto 14', 'La brújula',
    'Reto 14 de micro:bit: sensor de brújula, dirección en grados, condiciones con o, cascada '
    'de tramos. Calibración. CyR 1º ESO.',
    'una <strong>brújula</strong>: la placa escribe N, E, S u O según hacia dónde apunte. El '
    'sensor devuelve un ángulo en grados y tú lo conviertes en una letra con una cascada '
    'de <span class="bl">si</span>.',
    [
        ('La idea: un ángulo de 0 a 360',
         '<div class="placa"><figure>' + rosa_brujula() +
         '<figcaption>0° es el Norte y se cuenta hacia la derecha.</figcaption></figure>'
         '<div class="lado"><p>El bloque <span class="bl">dirección de la brújula (°)</span>, en ' +
         cat('entrada', 'Entrada') + ', vale un número de 0 a 360: 0 si la parte de arriba de '
         'la placa apunta al Norte, 90 al Este, 180 al Sur, 270 al Oeste.</p>'
         '<p>Cada punto abarca 90° centrados en él. Con el Norte hay una trampa: va '
         '<strong>de 315 a 45</strong>, pasando por el 0. Por eso su condición es «menor que '
         '45 <strong>o</strong> mayor que 315».</p></div></div>'),

        ('Lee este programa',
         caja(P14, 'Para siempre: fijar grados a dirección de la brújula; si grados < 45 o grados '
                   '> 315 entonces mostrar cadena N; si no, si grados < 135, E; si no, si grados '
                   '< 225, S; si no, O') +
         secuencia([
             'Cada vuelta guarda el ángulo en <strong>grados</strong>. Se guarda una vez y se '
             'pregunta varias: si preguntaras al sensor en cada rama, podría cambiar entre '
             'una y otra.',
             '<strong>¿menos de 45 o más de 315?</strong> Norte. El bloque <span class="bl">o'
             '</span> de Lógica junta dos comparaciones.',
             'Si no, <strong>¿menos de 135?</strong> Ya sabemos que es 45 o más, así que estar '
             'por debajo de 135 es el tramo del Este.',
             'Si no, <strong>¿menos de 225?</strong> Sur. Y lo que queda, de 225 a 315, es el '
             'Oeste: la última rama no pregunta.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Escribes la primera condición sólo como <em>grados &lt; 45</em>, sin el '
                       '«o». Apuntas al Norte y el sensor marca 350. ¿Qué letra sale?',
                  [('n', 'N, porque 350 está casi en el 0',
                    'No. 350 no es menor que 45. La placa no sabe que 350 «está cerca» del 0.'),
                   ('o', 'O: 350 no entra en ninguna rama anterior y cae en el si no',
                    'Correcto. 350 no es menor que 45, ni que 135, ni que 225, así que cae en la '
                    'red de seguridad, que es el Oeste. Por eso el Norte necesita dos condiciones.'),
                   ('nada', 'Nada: 350 no está en el programa',
                    'Siempre entra en alguna rama: la última no pregunta.')],
                  'o')),

        ('Tu reto',
         pasos([
             'Monta el programa. El <span class="bl">o</span> está en ' + cat('logica', 'Lógica') +
             ', y dentro de cada hueco va un bloque de comparar.',
             'Pásalo a la placa. La primera vez, la placa escribe <strong>TILT TO FILL SCREEN</strong>: '
             'inclínala en todas las direcciones hasta encender todos los LEDs. Es la '
             '<strong>calibración</strong>, y hay que hacerla cada vez que se carga un programa '
             'con brújula.',
             'Comprueba las cuatro letras girando sobre ti mismo. Lejos de ordenadores y '
             'radiadores: el hierro engaña a la brújula.',
             'Cambia las letras por <span class="bl">mostrar flecha</span>: Norte, Este, Sur, '
             'Oeste. Ahora la placa señala.',
             'Difícil: ocho direcciones, con NE, SE, SO y NO. Cada tramo pasa a ser de 45°.',
             'Pásalo a la placa y entrégalo.']) +
         ojo('Se calibra en la placa, no en el simulador',
             '<p>En el simulador la brújula se prueba arrastrando el ratón sobre la placa '
             'dibujada. La calibración sólo aparece en la placa real. Si la placa insiste en '
             'pedirla, es que no has llegado a encender todos los LEDs: sigue girándola.</p>')),

        ('Lo has conseguido si…',
         logros(['La placa marca las cuatro direcciones y coincide con una brújula del móvil.',
                 'Has hecho la calibración sin ayuda.',
                 'Sabes explicar por qué el Norte necesita un <span class="bl">o</span>.'])),
    ],
    anterior=('r13', 'Reto 13'), siguiente=('r15', 'Reto 15 · Esquiva enemigos'))

# ============================================================ R15 · Esquiva enemigos
P15 = [
    INICIAR([FIJAR('jugador', SPRITE(2, 4)), FIJAR('enemigo', SPRITE(azar(0, 4), 0))]),
    BOTON('A', [SP_CAMBIAR('jugador', 'x', -1)]),
    BOTON('B', [SP_CAMBIAR('jugador', 'x', 1)]),
    SIEMPRE([
        PAUSA(500),
        SP_CAMBIAR('enemigo', 'y', 1),
        SI(SP_TOCA('enemigo', 'jugador'), [FIN_JUEGO]),
        SI(compara(SP_PROP('enemigo', 'y'), '=', 4), [
            PUNTOS(1),
            SP_ELIMINAR('enemigo'),
            FIJAR('enemigo', SPRITE(azar(0, 4), 0))]),
    ]),
]

r15 = pagina(
    'r15', 'Reto 15', 'Esquiva enemigos: tu primer juego',
    'Reto 15 de micro:bit: juego con la categoría Juego. Sprites, mover con botones, colisión, '
    'puntuación y fin del juego. CyR 1º ESO.',
    'un <strong>juego</strong> de verdad: tú eres un LED en la fila de abajo, te mueves con A y B, '
    'y desde arriba caen enemigos. Si te tocan, se acabó; cada uno que esquivas es un punto. Es '
    'el reto más largo del trimestre: dos clases.',
    [
        ('La idea: los sprites',
         '<p>Podrías hacerlo con coordenadas y variables, como hasta ahora, pero sería un '
         'programa larguísimo. MakeCode tiene la categoría ' + cat('juego', 'Juego') +
         ' (en <strong>Avanzado</strong>, al final de la lista) con la pieza que lo simplifica '
         'todo: el <strong>sprite</strong>, un LED que sabe dónde está y se puede mover, '
         'preguntar si toca a otro, y borrar. Cada sprite se guarda en una variable, igual que '
         'un número.</p>' +
         claves([
             ('crear sprite en x: 2 y: 4', 'nace un LED en esa posición. Se guarda con '
              '<span class="bl">fijar jugador a</span>.'),
             ('jugador cambiar x por -1', 'lo mueve una casilla a la izquierda. No se sale de '
              'la pantalla: en el borde se queda.'),
             ('esta enemigo tocando jugador', 'pregunta de sí o no: ¿están en el mismo LED?'),
             ('agregar puntos a la puntuación actual 1', 'la placa lleva la cuenta sola.'),
             ('fin del juego', 'la animación de «GAME OVER» y la puntuación. Para volver a '
              'jugar, el botón de reinicio de detrás de la placa (o el del simulador).')])),

        ('Lee este programa',
         caja_varios([[P15[0]], [P15[1]], [P15[2]], [P15[3]]],
                     'Al iniciar: fijar jugador a crear sprite en x 2 y 4; fijar enemigo a crear '
                     'sprite en x al azar de 0 a 4, y 0. Botón A: jugador cambiar x por -1. Botón B: '
                     'jugador cambiar x por 1. Para siempre: pausa 500; enemigo cambiar y por 1; si '
                     'esta enemigo tocando jugador entonces fin del juego; si enemigo y = 4 entonces '
                     'agregar 1 punto, eliminar enemigo, fijar enemigo a crear sprite en x al azar y 0') +
         secuencia([
             '<strong>al iniciar</strong> crea los dos sprites: el jugador abajo en el centro y el '
             'enemigo arriba, en una columna al azar.',
             '<strong>A</strong> y <strong>B</strong> mueven al jugador. Son eventos: responden '
             'en cualquier momento, mientras el bucle hace lo suyo. Es el reparto del cronómetro.',
             'El <strong>para siempre</strong> es el juego: cada medio segundo el enemigo baja '
             'una fila.',
             '<strong>¿Toca al jugador?</strong> Fin del juego.',
             '<strong>¿Ha llegado a la fila 4 sin tocarte?</strong> Punto. Se elimina ese '
             'enemigo y se crea otro arriba, en otra columna al azar. Y vuelta a empezar.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Cambias el orden: pones el <em>si … tocando</em> ANTES de <em>enemigo '
                       'cambiar y por 1</em>. ¿Qué cambia en el juego?',
                  [('nada', 'Nada: el enemigo se mueve igual',
                    'Se mueve igual, sí, pero la comprobación mira la posición de antes de '
                    'moverse. Piensa qué pasa en la fila 4.'),
                   ('tarde', 'Puede tocarte y no perder hasta la siguiente vuelta',
                    'Correcto. Se comprueba antes de mover: el enemigo baja a tu fila, y la '
                    'colisión no se mira hasta media vuelta después. Mientras tanto, si es la '
                    'fila 4, hasta te dan el punto. El orden dentro del bucle importa.'),
                   ('rapido', 'El juego va más rápido',
                    'No. La velocidad la marca la pausa, no el orden.')],
                  'tarde')),

        ('Tu reto',
         pasos([
             'Crea las variables <strong>jugador</strong> y <strong>enemigo</strong> y monta el '
             'programa. Los bloques verdes oscuros están en <strong>Avanzado → Juego</strong>.',
             'Juega en el simulador hasta perder y mira cómo se enseña la puntuación.',
             'Que se acelere: guarda la pausa en una variable <strong>espera</strong> que empieza '
             'en 500 y, cada vez que esquivas un enemigo, réstale 20.',
             'Enemigos que parpadean: <span class="bl">enemigo cambiar parpadear por 100</span> '
             'al crearlo. Y a lo mejor una música al perder, de ' + cat('musica', 'Música') + '.',
             'Pásalo a la placa, juega con tu pareja a ver quién aguanta más, y entrégalo.']) +
         pista('¿Por qué eliminar el enemigo y crear otro, en vez de subirlo?',
               '<p>Podrías hacer <span class="bl">enemigo establecer y en 0</span> y cambiarle '
               'la x. Funciona igual. Eliminarlo y crear uno nuevo es más fácil de leer: «este '
               'ya está, viene otro». Cuando tengas varios enemigos a la vez, esa forma de '
               'pensar es la que te va a salvar.</p>') +
         amplia(['<a href="a10.html">Ampliación 10 · Naves</a>: dispara con A+B y destruye '
                 'enemigos.',
                 '<a href="a11.html">Ampliación 11 · Varios enemigos a la vez</a>: dos o tres '
                 'sprites cayendo, cada uno a su ritmo.'])),

        ('Lo has conseguido si…',
         logros(['Te mueves con A y B, los enemigos caen y cuando te tocan sale GAME OVER con '
                 'la puntuación.',
                 'El juego se acelera a medida que esquivas.',
                 'Sabes explicar por qué el orden de los bloques dentro del bucle cambia el '
                 'juego.'])),
    ],
    anterior=('r14', 'Reto 14'),
    nav_extra='<a href="index.html#ampliaciones" class="bc"><span class="bi">🚀</span>'
              '<span class="bk">Ampliaciones</span><span class="bn">Para seguir por tu cuenta</span></a>')


if __name__ == '__main__':
    for n, h in [('r09', r09), ('r10', r10), ('r11', r11), ('r12', r12),
                 ('r13', r13), ('r14', r14), ('r15', r15)]:
        escribir(n, h)

# -*- coding: utf-8 -*-
"""Sesiones 06 a 11 de T1 · Scratch."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scratchsvg import op, var, rep, hexa
from plantilla import pagina, caja, dos_cajas, pasos, pregunta, pista, ojo, logros, tabla
from comun import escribir, CUADERNILLO

BANDERA = ('hat', 'events', ['al hacer clic en', ('icon', 'bandera')])
RESP = rep('sensing', 'respuesta')
BORDE = hexa('sensing', '¿tocando', ('drop', 'borde'), '?')

# ============================================================ S06
P06 = [
    BANDERA,
    ('stack', 'motion', ['fijar estilo de rotación a', ('drop', 'izquierda-derecha')]),
    ('c', 'control', ['por siempre'], [
        ('stack', 'looks', ['siguiente disfraz']),
        ('stack', 'control', ['esperar', ('num', '0.2'), 'segundos']),
        ('stack', 'motion', ['mover', ('num', '10'), 'pasos']),
        ('stack', 'motion', ['si toca un borde, rebotar']),
    ]),
]
DISFRAZ06 = [('stack', 'looks', ['cambiar disfraz a', ('drop', 'costume1')])]

s06 = pagina(
    6, 'Animaciones con disfraces',
    'Sesión 6 de Scratch: siguiente disfraz y esperar para conseguir que un personaje camine. '
    'Animación por cambio de imagen. CyR 1º ESO.',
    'que tu personaje <strong>camine</strong> de verdad, moviendo las patas, en vez de deslizarse '
    'por la pantalla como si patinara.',
    [
        ('La idea: una animación son imágenes que se alternan',
         '<p>Un personaje de Scratch no tiene una sola imagen: tiene varias, y se llaman '
         '<strong>disfraces</strong>. Están en la pestaña <strong>Disfraces</strong>, arriba a la '
         'izquierda, al lado de <strong>Código</strong>.</p>'
         '<p>El gato viene con dos, iguales salvo por la posición de las patas. Si los alternas '
         'deprisa, el cerebro ve movimiento. Es exactamente lo mismo que hacen los dibujos '
         'animados.</p>'),

        ('Lee este programa',
         caja(P06, 'Programa: fijar estilo de rotación a izquierda-derecha y después, por siempre, '
                   'siguiente disfraz, esperar 0.2 segundos, mover 10 pasos y si toca un borde '
                   'rebotar',
              pie='Los cuatro bloques de dentro se repiten sin parar: cambiar de disfraz, esperar '
                  'un poco, avanzar y rebotar si llega al borde.') +
         pasos([
             '<strong>siguiente disfraz</strong> pasa al siguiente dibujo del personaje. Cuando se '
             'acaban, vuelve al primero.',
             'La <strong>espera de 0,2 segundos</strong> es la clave de toda la sesión: sin ella, '
             'el cambio va tan rápido que no se ve un paso, se ve un borrón.',
             '<strong>mover 10 pasos</strong> lo desplaza mientras «camina».',
             '<strong>si toca un borde, rebotar</strong> le da la vuelta al llegar al final.',
             'El <strong>fijar estilo de rotación a (izquierda-derecha)</strong> del principio '
             'hace que al rebotar se dé la vuelta como un espejo, en vez de quedarse cabeza abajo.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Quitas el bloque <em>esperar (0,2) segundos</em> y dejas todo lo demás igual. '
                       '¿Qué se ve?',
                  [('rapido', 'Lo mismo, pero el personaje camina más rápido',
                    'No exactamente. Sí va más rápido, pero el problema es otro: la animación deja '
                    'de leerse como una animación.'),
                   ('borroso', 'El personaje vibra: los disfraces cambian tan deprisa que no se '
                    'distingue ninguno',
                    'Correcto. El bucle da decenas de vueltas por segundo, así que el disfraz '
                    'cambia decenas de veces por segundo. La espera es lo que convierte el '
                    'parpadeo en un paso.'),
                   ('para', 'El personaje deja de cambiar de disfraz',
                    'No. Sigue cambiando, y de hecho más veces que antes: lo que pasa es que no da '
                    'tiempo a verlo.')],
                  'borroso')),

        ('Tu actividad',
         pasos([
             'Monta el programa con el gato y comprueba que camina.',
             'Prueba la espera con <strong>0,05</strong>, con <strong>0,2</strong> y con '
             '<strong>1</strong> segundo. Quédate con el valor que mejor se vea.',
             'Ahora cámbiate de personaje: pulsa el botón del gato (abajo a la derecha) y '
             '<strong>elige uno que tenga varios disfraces</strong>. Antes de decidirte, míralo en '
             'la pestaña Disfraces: los que sólo traen uno no sirven para animar.',
             'Vuelve a ajustar la espera: un personaje con cuatro disfraces necesita una espera '
             'más corta que uno con dos.',
             'Cambia también el fondo para que la escena tenga sentido.']) +
         pista('¿Y si quiero un disfraz concreto y no el siguiente?',
               '<p>Para eso está este otro bloque, que va directamente al disfraz que le digas. '
               'Se usa, por ejemplo, para dejar al personaje quieto en una postura concreta cuando '
               'el programa termina:</p>' +
               caja(DISFRAZ06, 'Bloque cambiar disfraz a costume1', ancho=360)) +
         ojo('Los disfraces se llaman en inglés',
             '<p>Aunque el editor esté en español, los disfraces del gato se llaman '
             '<strong>costume1</strong> y <strong>costume2</strong>. Tu cuadernillo dice '
             '«disfraz1» y «disfraz2», y esos nombres <strong>no existen</strong> en pantalla. '
             'Si quieres, puedes cambiarles el nombre tú desde la pestaña Disfraces.</p>')),

        ('Lo has conseguido si…',
         logros(['El personaje camina: se le ve mover las patas, no deslizarse.',
                 'Rebota en los bordes sin quedarse boca abajo.',
                 'Has probado al menos tres valores distintos de espera y sabes cuál va mejor.',
                 'Has cambiado de personaje y de fondo.'])),
    ],
    cuadernillo=CUADERNILLO[6])

# ============================================================ S07
P07 = [
    BANDERA,
    ('stack', 'sensing', ['preguntar', ('txt', '¿Cómo te llamas?'), 'y esperar']),
    ('stack', 'looks', ['decir', op('unir', ('txt', 'Hola, '), RESP), 'durante', ('num', '2'), 'segundos']),
    ('stack', 'sensing', ['preguntar', ('txt', '¿Cuántos años tienes?'), 'y esperar']),
    ('stack', 'looks', ['decir', op('unir', RESP, ('txt', ' años, ¡qué bien!')), 'durante',
                        ('num', '2'), 'segundos']),
]
FALLO07 = [
    ('stack', 'looks', ['decir', RESP, 'durante', ('num', '2'), 'segundos']),
]

s07 = pagina(
    7, 'Preguntas y respuestas',
    'Sesión 7 de Scratch: preguntar y esperar, el bloque respuesta y el operador unir. '
    'Un diálogo interactivo. CyR 1º ESO.',
    'un diálogo: tu personaje te hace preguntas y <strong>usa lo que tú contestas</strong> en lo '
    'que dice después.',
    [
        ('Un programa que te escucha',
         '<p>Hasta ahora tus programas hacían siempre lo mismo. Da igual quién pulse la bandera: '
         'el gato dice lo mismo y se mueve igual.</p>'
         '<p>El de hoy <strong>cambia según lo que tú escribas</strong>. Es el primero que de '
         'verdad es <em>interactivo</em>, y para eso hacen falta dos piezas nuevas: un bloque que '
         '<strong>pregunta y espera</strong>, y un sitio donde queda guardado lo que has '
         'contestado.</p>'),

        ('Lee este programa',
         caja(P07, 'Programa: preguntar ¿Cómo te llamas? y esperar, decir unir Hola coma con '
                   'respuesta durante 2 segundos, preguntar ¿Cuántos años tienes? y esperar, y '
                   'decir unir respuesta con años qué bien durante 2 segundos',
              pie='El óvalo azul claro que pone <strong>respuesta</strong> no es un bloque que se '
                  'apile: es un bloque <em>informador</em>. Vale lo último que hayas escrito, y se '
                  'arrastra dentro del hueco de otro bloque.') +
         pasos([
             '<strong>preguntar … y esperar</strong> saca un cuadro de texto abajo del escenario y '
             '<em>para el programa</em> hasta que escribes algo y pulsas Intro.',
             'Lo que escribes se guarda en <strong>respuesta</strong>.',
             '<strong>unir</strong> pega dos textos en uno solo. Aquí pega «Hola, » con lo que '
             'hayas contestado, para que el gato salude con tu nombre.',
             'La segunda pregunta hace lo mismo… pero con una trampa que verás ahora.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Al final del todo, después de las dos preguntas, añades este bloque:'
                       '<div style="margin:10px 0">' +
                  caja(FALLO07, 'Bloque decir respuesta durante 2 segundos', ancho=330,
                       fondo='#FFFDF4') +
                  '</div>¿Qué dirá el gato?',
                  [('nombre', 'Mi nombre',
                    'No. Tu nombre estuvo en respuesta, pero sólo hasta que llegó la segunda '
                    'pregunta. En ese momento se sobrescribió.'),
                   ('edad', 'Mi edad',
                    'Correcto, y este es el concepto de la sesión: <b>respuesta sólo guarda lo '
                    'último</b>. Cada pregunta nueva borra lo anterior. Si necesitas conservar un '
                    'dato, hay que guardarlo en otro sitio — eso es la sesión siguiente.'),
                   ('ambas', 'Las dos cosas, una detrás de otra',
                    'No. respuesta es un único hueco: sólo cabe un dato, el más reciente.')],
                  'edad')),

        ('Tu actividad',
         '<p>Construye un <strong>diálogo de tres preguntas</strong>. Después de cada una, el '
         'personaje tiene que contestar usando lo que has escrito.</p>' +
         tabla(['Pregunta', 'Y el personaje responde algo como…'],
               [['¿Cómo te llamas?', '«Encantado, <em>Lucía</em>»'],
                ['¿Cuál es tu color favorito?', '«El <em>verde</em> también me gusta a mí»'],
                ['¿Qué has desayunado?', '«¿<em>Tostadas</em>? Yo prefiero el pescado»']]) +
         '<p>Fíjate en que en cada frase hay <strong>un trozo fijo</strong> y <strong>un trozo que '
         'cambia</strong>. Ese es justo el trabajo del bloque <strong>unir</strong>.</p>' +
         pista('Reto: pegar tres trozos en vez de dos',
               '<p><strong>unir</strong> sólo admite dos huecos. Para juntar tres trozos hay que '
               'meter un <strong>unir</strong> dentro de otro: en el segundo hueco del primero, '
               'colocas otro <strong>unir</strong> completo. Se puede repetir tantas veces como '
               'quieras.</p>') +
         ojo('El texto por defecto no es el del cuadernillo',
             '<p>Cuando coges el bloque de la paleta, ya viene escrito '
             '<strong>¿Cómo te llamas?</strong> Tu cuadernillo dice «¿Cuál es tu nombre?», que no '
             'es lo que verás. Da igual: puedes escribir dentro lo que quieras.</p>')),

        ('Lo has conseguido si…',
         logros(['El personaje hace tres preguntas seguidas y espera respuesta en cada una.',
                 'Cada frase que dice incluye lo que tú acabas de escribir.',
                 'Has usado <em>unir</em> al menos tres veces.',
                 'Sabrías explicar por qué <em>respuesta</em> no se acuerda de la primera pregunta.'])),
    ],
    cuadernillo=CUADERNILLO[7])

# ============================================================ S08
P08 = [
    BANDERA,
    ('stack', 'sensing', ['preguntar', ('txt', 'Dime un número'), 'y esperar']),
    ('stack', 'variables', ['dar a', ('drop', 'num1'), 'el valor', RESP]),
    ('stack', 'sensing', ['preguntar', ('txt', 'Dime otro número'), 'y esperar']),
    ('stack', 'variables', ['dar a', ('drop', 'num2'), 'el valor', RESP]),
    ('stack', 'looks', ['decir', op('unir', ('txt', 'La suma es '),
                                    op(var('num1'), '+', var('num2'))),
                        'durante', ('num', '3'), 'segundos']),
]
RESTA08 = [
    ('stack', 'looks', ['decir', op('unir', ('txt', 'La resta es '),
                                    op(var('num1'), '-', var('num2'))),
                        'durante', ('num', '3'), 'segundos']),
]

s08 = pagina(
    8, 'Variables I',
    'Sesión 8 de Scratch: crear variables y guardar datos con dar a … el valor. Una '
    'calculadora que suma dos números. CyR 1º ESO.',
    'una <strong>calculadora</strong>: le das dos números y te dice la suma, la resta y el '
    'producto.',
    [
        ('Qué es una variable',
         '<p>En la sesión anterior descubriste el problema: <strong>respuesta</strong> sólo guarda '
         'lo último, así que al hacer la segunda pregunta se pierde la primera.</p>'
         '<p>Una <strong>variable</strong> es una caja con nombre donde guardas un dato para '
         'usarlo cuando te haga falta. Tú decides cuántas cajas hay y cómo se llaman.</p>'
         '<p>Se crean en la categoría <strong>Variables</strong> (naranja), con el botón '
         '<strong>Crear una variable</strong>. Al crearla te pregunta el nombre — ponle uno que '
         'diga lo que guarda: <code>num1</code>, <code>Puntos</code>, <code>vidas</code>.</p>'),

        ('Lee este programa',
         caja(P08, 'Programa: preguntar Dime un número y esperar, dar a num1 el valor respuesta, '
                   'preguntar Dime otro número y esperar, dar a num2 el valor respuesta, y decir '
                   'unir La suma es con num1 más num2 durante 3 segundos') +
         pasos([
             'Pregunta el primer número. Se queda en <strong>respuesta</strong>.',
             '<strong>dar a (num1) el valor (respuesta)</strong> copia ese dato a la caja '
             '<code>num1</code>. Ahora está en dos sitios.',
             'Pregunta el segundo número. <strong>respuesta</strong> cambia — pero '
             '<code>num1</code> no, porque es una caja aparte.',
             'El segundo número se copia a <code>num2</code>.',
             'El bloque verde <strong>(num1) + (num2)</strong> es un operador: coge las dos cajas, '
             'las suma, y el resultado se mete dentro del <em>unir</em>.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Si <em>respuesta</em> ya guarda lo que escribe el usuario, ¿para qué sirve '
                       'crear <code>num1</code>?',
                  [('numeros', 'Porque respuesta sólo vale para textos y no para números',
                    'No. respuesta admite números perfectamente; de hecho el programa los suma sin '
                    'problema.'),
                   ('pisa', 'Porque la segunda pregunta machaca respuesta y el primer número se '
                    'perdería',
                    'Correcto. Copiar el dato a una variable es la forma de <b>ponerlo a salvo</b> '
                    'antes de que llegue la siguiente pregunta.'),
                   ('bonito', 'Porque queda más ordenado, pero funcionaría igual sin ella',
                    'No funcionaría: al llegar al final, respuesta valdría el segundo número, y el '
                    'programa sumaría ese número consigo mismo.')],
                  'pisa')),

        ('Tu actividad',
         pasos([
             'Crea las dos variables <code>num1</code> y <code>num2</code> y monta el programa.',
             'Añade la <strong>resta</strong> y la <strong>multiplicación</strong>, cada una en su '
             'propio bocadillo, uno detrás de otro.',
             'Quita las marcas de las casillas de las variables para que no se vean en el '
             'escenario y quede más limpio.',
             '<strong>Reto:</strong> añade la división. Prueba a dividir entre 0 y mira qué '
             'contesta Scratch — no es un fallo tuyo.']) +
         caja(RESTA08, 'Bloque decir unir La resta es con num1 menos num2 durante 3 segundos',
              pie='El bloque de la resta es idéntico al de la suma cambiando el operador verde.') +
         ojo('Este bloque ha cambiado de nombre',
             '<p>Tu cuadernillo lo llama <strong>fijar (num1) a (…)</strong>. En Scratch 3 se '
             'llama <strong>dar a (num1) el valor (…)</strong>. Es exactamente el mismo bloque.</p>'
             '<p style="margin-bottom:0">Al crear una variable te preguntará si es '
             '<em>para todos los objetos</em> o <em>sólo para este objeto</em>. De momento deja '
             'siempre la primera opción.</p>')),

        ('Lo has conseguido si…',
         logros(['Has creado dos variables con nombres que se entienden.',
                 'El programa pide dos números y da suma, resta y producto correctos.',
                 'Funciona bien aunque escribas los números en otro orden.',
                 'Sabrías explicar la diferencia entre <em>respuesta</em> y una variable tuya.'])),
    ],
    cuadernillo=CUADERNILLO[8])

# ============================================================ S09
P09 = [
    BANDERA,
    ('stack', 'variables', ['dar a', ('drop', 'Aciertos'), 'el valor', ('num', '0')]),
    ('stack', 'variables', ['mostrar variable', ('drop', 'a')]),
    ('stack', 'variables', ['mostrar variable', ('drop', 'b')]),
    ('c', 'control', ['repetir', ('num', '5')], [
        ('stack', 'variables', ['dar a', ('drop', 'a'), 'el valor',
                                op('número aleatorio entre', ('num', '1'), 'y', ('num', '10'))]),
        ('stack', 'variables', ['dar a', ('drop', 'b'), 'el valor',
                                op('número aleatorio entre', ('num', '1'), 'y', ('num', '10'))]),
        ('stack', 'sensing', ['preguntar', ('txt', '¿Cuánto suman?'), 'y esperar']),
        ('ce', 'control', ['si', hexa('operators', RESP, '=', op(var('a'), '+', var('b'))), 'entonces'],
         [('stack', 'looks', ['decir', ('txt', '¡Bien!'), 'durante', ('num', '1'), 'segundos']),
          ('stack', 'variables', ['sumar a', ('drop', 'Aciertos'), ('num', '1')])],
         ['si no'],
         [('stack', 'looks', ['decir', ('txt', 'Casi'), 'durante', ('num', '1'), 'segundos'])]),
    ]),
    ('stack', 'looks', ['decir', op('unir', ('txt', 'Aciertos: '), var('Aciertos')),
                        'durante', ('num', '3'), 'segundos']),
]
MAL09 = [('stack', 'variables', ['dar a', ('drop', 'Aciertos'), 'el valor', ('num', '1')])]

s09 = pagina(
    9, 'Variables II, azar y puntuación',
    'Sesión 9 de Scratch: número aleatorio, si… si no y sumar a una variable. Un quiz de '
    'sumas con marcador. CyR 1º ESO.',
    'un <strong>quiz de sumas</strong> con preguntas distintas cada vez y un marcador que cuenta '
    'tus aciertos.',
    [
        ('Tres cosas nuevas',
         pasos([
             '<strong>número aleatorio entre (1) y (10)</strong> — un operador verde que devuelve '
             'un número distinto cada vez. Es lo que hace que el juego no sea siempre igual.',
             '<strong>si … entonces / si no</strong> — como el condicional de la sesión 5, pero '
             'con <em>dos</em> huecos: uno para cuando la respuesta es sí y otro para cuando es no. '
             'Siempre se ejecuta uno de los dos, nunca los dos ni ninguno.',
             '<strong>sumar a (Aciertos) (1)</strong> — añade 1 a lo que ya hubiera. '
             'Es el bloque de contar.'])),

        ('Lee este programa',
         caja(P09, 'Programa del quiz: poner Aciertos a 0, mostrar las variables a y b, y repetir '
                   '5 veces: dar a la variable a un número aleatorio entre 1 y 10, lo mismo para b, '
                   'preguntar cuánto suman, y si la respuesta es igual a a más b decir ¡Bien! y '
                   'sumar 1 a Aciertos, si no decir Casi. Al terminar, decir el total de aciertos.',
              pie='Fíjate en el hexágono verde: <strong>(respuesta) = ((a) + (b))</strong>. '
                  'Dentro de una condición se pueden meter operadores, y dentro de los operadores, '
                  'variables. Se encajan como muñecas rusas.') +
         pasos([
             'El marcador se pone a <strong>0</strong> antes de empezar. Si no lo hicieras, seguiría '
             'con la puntuación de la partida anterior.',
             '<strong>mostrar variable</strong> hace que <code>a</code> y <code>b</code> se vean en '
             'el escenario. Así el jugador sabe qué números tiene que sumar.',
             'Cada vuelta del bucle sortea dos números nuevos y pregunta.',
             'El <strong>si … si no</strong> compara lo que has escrito con la suma verdadera. '
             'Si coincide, felicita y <em>suma uno</em> al marcador. Si no, dice «Casi» y no suma nada.',
             'Al salir del bucle, después de cinco preguntas, anuncia el total.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Por error, en vez de <em>sumar a (Aciertos) (1)</em> pones este otro bloque. '
                       'Aciertas las cinco preguntas. ¿Qué marcador sale al final?'
                       '<div style="margin:10px 0">' +
                  caja(MAL09, 'Bloque dar a Aciertos el valor 1', ancho=340, fondo='#FFFDF4') +
                  '</div>',
                  [('cinco', '5, porque he acertado las cinco',
                    'No. Ese bloque no cuenta: <b>machaca</b>. Cada acierto vuelve a poner el '
                    'marcador en 1, en lugar de añadirle uno a lo que ya había.'),
                   ('uno', '1',
                    'Correcto. <b>dar a … el valor</b> sustituye lo que hubiera; <b>sumar a</b> '
                    'añade. Para contar cosas siempre se usa el segundo. Es el error más común de '
                    'todo el trimestre.'),
                   ('cero', '0, porque el bloque está mal y no hace nada',
                    'El bloque es correcto y sí hace algo: pone el marcador a 1. El problema es '
                    'que lo hace las cinco veces.')],
                  'uno')),

        ('Tu actividad',
         pasos([
             'Crea las tres variables: <code>Aciertos</code>, <code>a</code> y <code>b</code>.',
             'Monta el programa y juega una partida entera.',
             'Cámbialo a <strong>10 preguntas</strong> en vez de 5.',
             'Al final, añade un <strong>si … si no</strong> más: si has sacado más de la mitad, '
             'que diga «¡Aprobado!»; si no, «A repasar».',
             '<strong>Reto:</strong> cambia las sumas por multiplicaciones y baja el rango de los '
             'números aleatorios a <strong>1–5</strong>. Piensa por qué hay que bajarlo.']) +
         ojo('El bloque de contar ha cambiado de nombre',
             '<p>Tu cuadernillo lo llama <strong>cambiar (Aciertos) por (1)</strong>. Ese nombre '
             '<strong>ya no existe</strong>. Hoy se llama <strong>sumar a (Aciertos) (1)</strong> '
             'y está en la categoría Variables, justo debajo de <em>dar a … el valor</em>.</p>')),

        ('Lo has conseguido si…',
         logros(['Cada partida hace preguntas distintas.',
                 'El marcador sube exactamente uno por acierto, y no sube con los fallos.',
                 'Al volver a jugar, el marcador empieza otra vez en 0.',
                 'Al terminar dice si has aprobado.',
                 'Sabrías explicar la diferencia entre <em>dar a … el valor</em> y '
                 '<em>sumar a …</em>'])),
    ],
    cuadernillo=CUADERNILLO[9])

# ============================================================ S10
P10 = [
    BANDERA,
    ('stack', 'motion', ['ir a x:', ('num', '-200'), 'y:', ('num', '60')]),
    ('stack', 'motion', ['apuntar en dirección', ('num', '90')]),
    ('c', 'control', ['repetir hasta que',
                      hexa('operators', rep('motion', 'posición x'), '>', ('num', '200'))], [
        ('stack', 'motion', ['mover', op('número aleatorio entre', ('num', '1'), 'y', ('num', '10')),
                             'pasos']),
    ]),
    ('stack', 'looks', ['decir', ('txt', '¡He ganado!'), 'durante', ('num', '2'), 'segundos']),
    ('cap', 'control', ['detener', ('drop', 'todos')]),
]

s10 = pagina(
    10, 'Juego de carreras',
    'Sesión 10 de Scratch: dos objetos con el mismo programa y avance aleatorio. Un juego de '
    'carreras que no se gana siempre igual. CyR 1º ESO.',
    'una <strong>carrera</strong> entre dos personajes en la que no sabes quién va a ganar hasta '
    'que termina.',
    [
        ('El mismo programa, en dos objetos distintos',
         '<p>Hoy no hay bloques nuevos: hay una <strong>idea</strong> nueva. El programa de esta '
         'sesión es corto, pero va <em>repetido en dos objetos</em>, y cada uno lo ejecuta por su '
         'cuenta a la vez que el otro.</p>'
         '<p>Es la primera vez que dos cosas ocurren <strong>al mismo tiempo</strong> en tus '
         'programas.</p>'),

        ('Lee este programa',
         caja(P10, 'Programa de un corredor: ir a x menos 200 y 60, apuntar en dirección 90, '
                   'repetir hasta que la posición x sea mayor que 200 moviendo un número aleatorio '
                   'entre 1 y 10 pasos, después decir ¡He ganado! durante 2 segundos y detener todos',
              pie='<strong>posición x</strong> es un informador azul de Movimiento: vale lo lejos '
                  'que está el objeto del centro, de −240 a 240. Aquí lo usamos como línea de meta.') +
         pasos([
             'El corredor se coloca en la línea de salida, a la izquierda del todo.',
             'El bucle vigila una condición: <strong>¿ya he pasado de x = 200?</strong> Mientras la '
             'respuesta sea no, avanza.',
             'Cada vuelta avanza <strong>un número de pasos distinto</strong>, entre 1 y 10. Ahí '
             'está toda la gracia del juego.',
             'Cuando cruza la meta, sale del bucle, canta victoria y <strong>detiene todos</strong> '
             'los programas — incluido el del otro corredor, que se queda a medias.'])),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Los dos corredores tienen exactamente el mismo programa. '
                       '¿Por qué no gana siempre el mismo?',
                  [('salida', 'Porque uno sale un poco antes que el otro',
                    'No. Los dos arrancan con la misma bandera verde, a la vez.'),
                   ('azar', 'Porque en cada vuelta cada uno avanza un número de pasos distinto, '
                    'sorteado aparte',
                    'Correcto. El bloque de azar se ejecuta por separado en cada objeto y en cada '
                    'vuelta, así que las dos carreras se van separando poco a poco.'),
                   ('elige', 'Porque Scratch decide un ganador al empezar',
                    'No. Scratch no decide nada por adelantado: el resultado sale de sumar muchos '
                    'sorteos pequeños.')],
                  'azar')),

        ('Tu actividad',
         pasos([
             'Elige dos personajes que puedan competir (dos coches, dos animales…).',
             'Programa el primero con el programa de arriba.',
             'Selecciona el <strong>segundo</strong> objeto y móntale el mismo programa, '
             'cambiando sólo la <strong>y</strong> de la salida para que corran por carriles '
             'distintos.',
             'Píntale al fondo una línea de salida y otra de meta, para que se entienda.',
             '<strong>Reto:</strong> añade un tercer corredor que avance entre 1 y 12 pasos. '
             '¿Gana siempre? Juega diez partidas y cuéntalas.']) +
         ojo('El fallo que va a tener media clase',
             '<p>Los dos programas van en <strong>objetos distintos</strong>. Antes de arrastrar un '
             'bloque, comprueba abajo a la derecha <strong>qué objeto tienes seleccionado</strong>: '
             'si montas los dos programas en el mismo objeto, verás a un solo personaje corriendo '
             'y al otro parado.</p>'
             '<p style="margin-bottom:0">Truco: se puede <strong>arrastrar un programa entero</strong> '
             'desde el área de código hasta el icono del otro objeto, y se copia solo.</p>')),

        ('Lo has conseguido si…',
         logros(['Los dos corredores salen a la vez al pulsar la bandera.',
                 'Cada uno va por su carril.',
                 'Gana unas veces uno y otras veces otro.',
                 'El ganador dice que ha ganado y la carrera se para.',
                 'El fondo tiene salida y meta dibujadas.'])),
    ],
    cuadernillo=CUADERNILLO[10])

# ============================================================ S11
A11 = [
    BANDERA,
    ('stack', 'motion', ['ir a x:', ('num', '-120'), 'y:', ('num', '-60')]),
    ('stack', 'motion', ['apuntar en dirección', ('num', '90')]),
    ('stack', 'control', ['esperar', ('num', '1'), 'segundos']),
    ('stack', 'motion', ['mover', ('num', '60'), 'pasos']),
    ('stack', 'events', ['enviar', ('drop', 'patada')]),
]
C11 = [
    BANDERA,
    ('stack', 'motion', ['ir a x:', ('num', '0'), 'y:', ('num', '-60')]),
    ('stack', 'motion', ['apuntar en dirección', ('num', '90')]),
]
B11 = [
    ('hat', 'events', ['al recibir', ('drop', 'patada')]),
    ('stack', 'sound', ['iniciar sonido', ('drop', 'Pop')]),
    ('c', 'control', ['repetir hasta que', BORDE], [
        ('stack', 'motion', ['mover', ('num', '10'), 'pasos']),
        ('stack', 'motion', ['girar', ('icon', 'giro-d'), ('num', '15'), 'grados']),
    ]),
]

s11 = pagina(
    11, 'Mensajes entre objetos',
    'Sesión 11 de Scratch: enviar y al recibir. Coordinar dos objetos para que uno reaccione '
    'a lo que hace el otro. CyR 1º ESO.',
    'que un personaje <strong>reaccione a lo que hace otro</strong>: el gato chuta y el balón sale '
    'disparado en ese preciso momento.',
    [
        ('El problema: los objetos no se ven entre ellos',
         '<p>En la carrera de la sesión anterior los dos corredores hacían su vida por separado y '
         'daba igual. Pero si el balón tiene que salir <em>justo cuando</em> el gato lo toca, hace '
         'falta que uno le avise al otro.</p>'
         '<p>Para eso están los <strong>mensajes</strong>. Un objeto <strong>envía</strong> un '
         'aviso; cualquier otro que tenga un <strong>al recibir</strong> con ese mismo nombre se '
         'pone en marcha. Es como gritar una palabra en clase: la oye todo el que esté atento.</p>'),

        ('Lee estos dos programas',
         '<p>Son dos programas, en dos objetos distintos. Ninguno de los dos funciona solo.</p>' +
         dos_cajas(('Objeto <strong>Gato</strong>', A11,
                    'Programa del gato: ir a x menos 120 y menos 60, apuntar en dirección 90, '
                    'esperar 1 segundo, mover 60 pasos y enviar el mensaje patada'),
                   ('Objeto <strong>Balón</strong>', B11,
                    'Programa del balón: al recibir el mensaje patada, iniciar el sonido Pop y '
                    'repetir hasta que toque un borde moviendo 10 pasos y girando 15 grados')) +
         '<p>Y el balón necesita además un <strong>segundo programa</strong>, con su propia '
         'bandera verde, que lo devuelva al sitio antes de cada partida:</p>' +
         caja(C11, 'Segundo programa del balón: al hacer clic en la bandera verde, ir a x 0 y '
                   'menos 60 y apuntar en dirección 90',
              pie='Un mismo objeto puede tener varios programas. Este sólo coloca; el otro espera '
                  'el aviso.') +
         pasos([
             'El gato se coloca, espera un segundo y avanza hacia el balón.',
             'Al llegar, <strong>envía (patada)</strong>. Ese bloque no mueve nada: sólo lanza el '
             'aviso, y el gato sigue a lo suyo inmediatamente.',
             'El balón tiene un sombrero <strong>al recibir (patada)</strong>. Estaba esperando '
             'ese aviso, y en cuanto llega arranca su programa.',
             'El balón suena, sale rodando y gira mientras avanza, hasta chocar con un borde.',
             'El segundo programa del balón es el que hace que la <strong>segunda partida sea '
             'igual que la primera</strong>. Sin él, el balón se queda donde acabó —pegado al '
             'borde—, y como <em>repetir hasta que ¿tocando (borde)?</em> ya se cumple de entrada, '
             'no se movería nunca más.',
             'Antes de poder usar el mensaje hay que <strong>crearlo</strong>: en el desplegable '
             'del bloque, opción <strong>Nuevo mensaje</strong>, y le pones nombre. Ponle uno que '
             'signifique algo — «patada», no «mensaje1».'])),

        ('Comprueba que lo has entendido',
         pregunta('1', '¿En qué objeto tiene que estar el bloque <em>al recibir (patada)</em>?',
                  [('gato', 'En el gato, que es quien da la patada',
                    'No. El gato es quien <b>envía</b>. El que necesita el <em>al recibir</em> es '
                    'quien tiene que reaccionar.'),
                   ('balon', 'En el balón, que es quien tiene que salir disparado',
                    'Correcto. <b>enviar</b> va en el que avisa; <b>al recibir</b> va en el que '
                    'reacciona. Pueden reaccionar varios objetos al mismo mensaje a la vez.'),
                   ('fondo', 'En el escenario, que es donde se coordina todo',
                    'No. El escenario también puede recibir mensajes, pero aquí quien se tiene que '
                    'mover es el balón, así que el bloque va en el balón.')],
                  'balon')),

        ('Tu actividad',
         pasos([
             'Elige dos objetos: uno que actúe y otro que reaccione.',
             'Crea el mensaje con un nombre que se entienda.',
             'Monta los programas, cada uno en su objeto. No te olvides del que coloca.',
             'Añade un <strong>cambio de disfraz</strong> al gato justo antes de enviar el mensaje, '
             'para que se vea el gesto de chutar.',
             '<strong>Reto:</strong> añade un <strong>tercer objeto</strong> — un portero, un '
             'marcador, una nube — que también tenga <em>al recibir (patada)</em> y haga algo. '
             'Comprobarás que los dos reaccionan a la vez con un solo aviso.']) +
         ojo('Dos diferencias con tu cuadernillo',
             '<p>El bloque ya <strong>no</strong> se llama «enviar a todos». Hoy es simplemente '
             '<strong>enviar (patada)</strong>, aunque siga avisando a todo el mundo.</p>'
             '<p style="margin-bottom:0">Y ojo: existe otro parecido, '
             '<strong>enviar (patada) y esperar</strong>. Ese <em>sí</em> deja al que envía '
             'parado hasta que los demás terminen. Aquí no lo queremos.</p>')),

        ('Lo has conseguido si…',
         logros(['El balón no se mueve hasta que el gato llega.',
                 'Al pulsar la bandera <strong>dos veces seguidas</strong> pasa exactamente lo '
                 'mismo las dos.',
                 'El mensaje tiene un nombre que explica lo que pasa.',
                 'Los dos programas están cada uno en su objeto.',
                 'Hay un tercer objeto que reacciona al mismo aviso.',
                 'Sabrías explicar la diferencia entre <em>enviar</em> y <em>enviar y esperar</em>.'])),
    ],
    cuadernillo=CUADERNILLO[11])

for n, h in [(6, s06), (7, s07), (8, s08), (9, s09), (10, s10), (11, s11)]:
    escribir(n, h)

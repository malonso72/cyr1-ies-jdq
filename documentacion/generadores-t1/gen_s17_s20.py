# -*- coding: utf-8 -*-
"""Sesiones 17 a 20 de T1 · Scratch: el proyecto final."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scratchsvg import op, var, rep, hexa, tecla
from plantilla import pagina, caja, pasos, pregunta, pista, ojo, logros, tabla
from comun import escribir

BANDERA = ('hat', 'events', ['al hacer clic en', ('icon', 'bandera')])


def si(cond, hijos):
    return ('c', 'control', ['si', cond, 'entonces'], hijos)


# La rubrica del proyecto final: se publica en S17 y se repite en S20.
RUBRICA = [
    ['<strong>Funciona</strong>', 'Se juega de principio a fin sin romperse. Se puede ganar y '
     'perder. Al volver a empezar, empieza bien.', '3'],
    ['<strong>Usa lo aprendido</strong>', 'Bucles, condicionales y al menos una variable. Puntos '
     'extra si hay mensajes entre objetos o azar.', '3'],
    ['<strong>Se entiende solo</strong>', 'Otra persona sabe jugar sin que se lo expliques: hay '
     'instrucciones, marcador visible y se ve cuándo aciertas o fallas.', '2'],
    ['<strong>Lo cuentas bien</strong>', 'En un minuto explicas qué es, cómo se juega y qué te '
     'costó más.', '2'],
]

# ============================================================ S17
FICHA = [
    ('1. Título', 'Cómo se llama tu juego o tu historia.'),
    ('2. Tipo', 'Juego de habilidad, quiz, laberinto, historia con decisiones…'),
    ('3. Personajes', 'Cuántos objetos vas a necesitar y qué hace cada uno.'),
    ('4. Escenario', 'Cuántos fondos y para qué (portada, juego, fin).'),
    ('5. Cómo se juega', 'Qué teclas o qué ratón usa el jugador. En una frase.'),
    ('6. Cómo se gana', 'La condición exacta. «Llegar a 10 puntos», no «hacerlo bien».'),
    ('7. Cómo se pierde', 'La condición exacta. Si no se puede perder, no es un juego.'),
    ('8. Qué voy a reutilizar', 'De qué sesiones vas a copiar los bloques. Sé concreto.'),
    ('9. Si me sobra tiempo', 'Dos mejoras que añadirías. Sólo si acabas lo de arriba.'),
]

IDEAS = [
    ['Esquivar lo que cae', 'S05 flechas · S09 marcador · S12 tocando', '⭐ Fácil'],
    ['Quiz de una asignatura', 'S07 preguntar · S09 marcador y azar', '⭐ Fácil'],
    ['Piedra, papel o tijera al mejor de 5', 'S14 entero · S09 marcador', '⭐ Fácil'],
    ['Cazar al que huye', 'S10 azar · S12 tocando · S13 cronómetro', '⭐ Fácil'],
    ['Laberinto de dos o tres niveles', 'S12 y S13 enteras', '⭐⭐ Media'],
    ['Pong con dificultad creciente', 'S15 y S16 enteras', '⭐⭐ Media'],
    ['Juego de reflejos contra el reloj', 'S13 cronómetro · S06 disfraces', '⭐⭐ Media'],
    ['Historia con decisiones', 'S07 preguntar · S11 mensajes · varios fondos', '⭐⭐ Media'],
]

s17 = pagina(
    17, 'Proyecto final: idea y diseño',
    'Sesión 17 de Scratch: elegir el proyecto final, dimensionarlo bien y escribir la ficha de '
    'diseño antes de programar. CyR 1º ESO.',
    'tu proyecto <strong>decidido y escrito</strong>, antes de tocar un solo bloque. Hoy no se '
    'programa: hoy se piensa.',
    [
        ('Por qué hoy no se programa',
         '<p>Te quedan <strong>tres sesiones</strong> para construirlo, mejorarlo y presentarlo. '
         'Quien empieza a arrastrar bloques sin saber qué está haciendo llega a la última sesión '
         'con un montón de cosas a medias y nada que enseñar.</p>'
         '<p>Media hora pensando hoy te ahorra dos sesiones de líos. Es así en clase y es así en '
         'los trabajos de verdad.</p>'),

        ('Catálogo de ideas',
         '<p>No tienes que elegir de aquí, pero míralo antes de inventarte nada. Cada idea dice '
         '<strong>de qué sesiones puedes copiar los bloques</strong>, que es lo que de verdad '
         'importa: no vas a partir de cero.</p>' +
         tabla(['Idea', 'Se apoya en…', 'Dificultad'], IDEAS) +
         '<p>Si se te ocurre otra cosa, perfecto — pero antes contesta a esto: '
         '<em>¿de qué sesión saco los bloques?</em> Si no sabes contestar, la idea es demasiado '
         'grande.</p>'),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Tres compañeros proponen esto. Para el tiempo que hay (tres sesiones), '
                       '¿cuál está bien dimensionado?',
                  [('grande', 'Un juego de plataformas con cinco niveles, enemigos, tienda de '
                    'objetos y jefe final',
                    'Eso es trabajo de meses, no de tres sesiones. El resultado casi seguro sería '
                    'un primer nivel a medias. Es el error más común: no falta capacidad, sobra '
                    'ambición.'),
                   ('justo', 'Un juego de esquivar objetos que caen, con marcador y tres vidas',
                    'Correcto. Tiene una mecánica clara, se puede ganar y perder, usa cosas que ya '
                    'sabes hacer, y si sobra tiempo se le pueden añadir mejoras. Un proyecto bien '
                    'dimensionado <b>se termina y luego crece</b>.'),
                   ('pequeno', 'Dos personajes que se saludan y se despiden',
                    'Se queda corto: no hay nada que el jugador pueda hacer, así que no hay ni '
                    'condicionales ni variables que enseñar. Eso era la sesión 1.')],
                  'justo')),

        ('Tu actividad: la ficha de diseño',
         '<p>Contesta a los nueve puntos. Escríbelos directamente en la tarea de Moodle. '
         'No hace falta que sea largo: hace falta que sea <strong>concreto</strong>.</p>' +
         tabla(['Punto', 'Qué tienes que escribir'], [[a, b] for a, b in FICHA]) +
         ojo('Las dos preguntas que más cuestan son la 6 y la 7',
             '<p>«Se gana cuando lo haces bien» no sirve. El ordenador no sabe qué es «bien». '
             'Tiene que ser algo que un bloque pueda comprobar: <em>«se gana cuando Puntos llega a '
             '10»</em>, <em>«se pierde cuando Vidas llega a 0»</em>.</p>'
             '<p style="margin-bottom:0">Si consigues escribir esas dos frases así, el proyecto '
             'está prácticamente resuelto: ya sabes qué variables necesitas.</p>') +
         '<h3 id="rubrica">Con qué se te va a evaluar</h3>'
         '<p>No es ningún secreto y no va a cambiar. Ténla delante mientras escribes la ficha: '
         'lo que más puntúa es que el juego <strong>funcione</strong> y que <strong>se entienda '
         'sin que estés al lado</strong>.</p>' +
         tabla(['Criterio', 'Qué se mira', 'Puntos'], RUBRICA) +
         '<p style="margin-bottom:0">«Funciona» y «se entiende solo» suman <strong>5 de los 10 '
         'puntos</strong>. Un juego sencillo y terminado saca mejor nota que uno ambicioso a '
         'medias — por eso la pregunta de arriba tenía la respuesta que tenía.</p>'),

        ('Lo has conseguido si…',
         logros(['Has contestado a los nueve puntos.',
                 'Has leído la rúbrica y sabes qué es lo que más puntúa.',
                 'Las condiciones de ganar y de perder están escritas con números concretos.',
                 'Sabes decir de qué sesiones vas a copiar bloques.',
                 'Un compañero puede leer tu ficha y entender a qué se juega, sin que se lo cuentes.'])),
    ],
    abrir=False,
    entrega='<p style="margin:0 0 10px;">Hoy <strong>no</strong> se entrega un <code>.sb3</code>: '
            'todavía no hay nada que programar.</p><ol>'
            '<li>Escribe los <strong>nueve puntos</strong> de la ficha en la tarea de Moodle de la '
            'sesión 17.</li>'
            '<li>Si has hecho un boceto en papel, hazle una foto y súbela también.</li>'
            '<li>Guarda tu ficha: la vas a necesitar en las tres sesiones siguientes.</li></ol>')

# ============================================================ S18
K1 = [
    BANDERA,
    ('c', 'control', ['por siempre'], [
        si(tecla('flecha derecha'), [('stack', 'motion', ['cambiar x por', ('num', '5')])]),
        si(tecla('flecha izquierda'), [('stack', 'motion', ['cambiar x por', ('num', '-5')])]),
    ]),
]
K2 = [
    ('stack', 'variables', ['dar a', ('drop', 'Puntos'), 'el valor', ('num', '0')]),
    ('stack', 'variables', ['mostrar variable', ('drop', 'Puntos')]),
]
K2b = [('stack', 'variables', ['sumar a', ('drop', 'Puntos'), ('num', '1')])]
K3 = [
    ('stack', 'motion', ['ir a x:', op('número aleatorio entre', ('num', '-200'), 'y', ('num', '200')),
                         'y:', op('número aleatorio entre', ('num', '-140'), 'y', ('num', '140'))]),
]
K4 = [
    si(hexa('sensing', '¿tocando', ('drop', 'Enemigo'), '?'),
       [('stack', 'sound', ['iniciar sonido', ('drop', 'Pop')]),
        ('stack', 'variables', ['sumar a', ('drop', 'Vidas'), ('num', '-1')]),
        ('stack', 'control', ['esperar', ('num', '1'), 'segundos'])]),
]
K5 = [
    ('stack', 'variables', ['dar a', ('drop', 'Tiempo'), 'el valor', ('num', '30')]),
    ('c', 'control', ['repetir hasta que', hexa('operators', var('Tiempo'), '=', ('num', '0'))], [
        ('stack', 'control', ['esperar', ('num', '1'), 'segundos']),
        ('stack', 'variables', ['sumar a', ('drop', 'Tiempo'), ('num', '-1')]),
    ]),
]
K6 = [
    BANDERA,
    ('stack', 'looks', ['cambiar fondo a', ('drop', 'portada')]),
    ('stack', 'looks', ['decir', ('txt', 'Pulsa espacio para empezar'), 'durante', ('num', '2'),
                        'segundos']),
    ('stack', 'control', ['esperar hasta que', tecla('espacio')]),
    ('stack', 'looks', ['cambiar fondo a', ('drop', 'juego')]),
    ('stack', 'events', ['enviar', ('drop', 'empezar')]),
]
K7 = [
    si(hexa('operators', var('Vidas'), '=', ('num', '0')),
       [('stack', 'looks', ['cambiar fondo a', ('drop', 'fin')]),
        ('stack', 'looks', ['decir', op('unir', ('txt', 'Fin. Puntos: '), var('Puntos')),
                            'durante', ('num', '3'), 'segundos']),
        ('cap', 'control', ['detener', ('drop', 'todos')])]),
]
K8 = [
    si(hexa('sensing', '¿tocando', ('drop', 'Jugador'), '?'),
       [('stack', 'looks', ['esconder']),
        ('stack', 'variables', ['sumar a', ('drop', 'Puntos'), ('num', '1')]),
        ('stack', 'control', ['esperar', ('num', '1'), 'segundos']),
        ('stack', 'motion', ['ir a x:',
                             op('número aleatorio entre', ('num', '-200'), 'y', ('num', '200')),
                             'y:', ('num', '140')]),
        ('stack', 'looks', ['mostrar'])]),
]

s18 = pagina(
    18, 'Proyecto final: construcción',
    'Sesión 18 de Scratch: kit de piezas reutilizables del trimestre para montar el proyecto '
    'final. Primera versión jugable. CyR 1º ESO.',
    'la <strong>primera versión jugable</strong> de tu proyecto. Fea, corta y sin pulir, pero que '
    'se pueda jugar de principio a fin.',
    [
        ('La regla de hoy',
         '<p>Al final de la sesión tu juego tiene que <strong>poderse jugar entero</strong>: '
         'empezar, jugar, ganar o perder, y terminar. Aunque sea con un personaje soso y sin '
         'sonidos.</p>'
         '<p>Es mucho mejor tener un juego feo terminado que uno precioso a medias. Lo bonito se '
         'añade en la sesión 19; lo que no se puede añadir el último día es que funcione.</p>'),

        ('Kit de piezas',
         '<p>Casi nada de tu proyecto es nuevo. Estas ocho piezas salen de las sesiones anteriores '
         'y resuelven el 90 % de lo que vas a necesitar. Cópialas y cámbiales los nombres y los '
         'números.</p>'
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">1 · Mover con el teclado</h3>'
         + caja(K1, 'Pieza de mover con el teclado: por siempre, si la flecha derecha está '
                    'presionada cambiar x por 5, si la izquierda cambiar x por menos 5',
                pie='Añade dos condicionales más, con <em>cambiar y por</em>, si también necesitas '
                    'subir y bajar.') +
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">2 · Marcador</h3>'
         + caja(K2, 'Pieza de marcador: dar a Puntos el valor 0 y mostrar la variable Puntos',
                ancho=390, pie='Esto va <strong>al arrancar</strong>. Y este otro, donde quieras '
                               'que sume:') +
         caja(K2b, 'Bloque sumar a Puntos 1', ancho=300) +
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">3 · Aparecer en un sitio al azar</h3>'
         + caja(K3, 'Pieza: ir a una x aleatoria entre menos 200 y 200 y una y aleatoria entre '
                    'menos 140 y 140',
                pie='Para monedas, enemigos, obstáculos… cualquier cosa que tenga que salir por '
                    'sorpresa.') +
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">4 · Chocar y perder vida</h3>'
         + caja(K4, 'Pieza: si está tocando el Enemigo, iniciar sonido Pop, sumar menos 1 a Vidas '
                    'y esperar 1 segundo',
                pie='Fíjate en el <strong>−1</strong>: <em>sumar a</em> también resta. Y la espera '
                    'de un segundo evita perder las tres vidas de golpe, como en el Pong.') +
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">5 · Cuenta atrás</h3>'
         + caja(K5, 'Pieza de cuenta atrás: dar a Tiempo el valor 30 y repetir hasta que Tiempo '
                    'sea 0, esperando 1 segundo y restando 1 cada vez') +
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">6 · Pantalla de inicio</h3>'
         + caja(K6, 'Pieza de pantalla de inicio: cambiar el fondo a portada, decir Pulsa espacio '
                    'para empezar, esperar hasta que se pulse espacio, cambiar el fondo a juego y '
                    'enviar el mensaje empezar',
                pie='Los demás objetos arrancan con <strong>al recibir (empezar)</strong> en vez '
                    'de con la bandera. Así nada se mueve hasta que el jugador está listo.') +
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">7 · Fin de partida</h3>'
         + caja(K7, 'Pieza de fin de partida: si Vidas es 0, cambiar el fondo a fin, decir Fin '
                    'seguido de los puntos durante 3 segundos y detener todos',
                pie='Acuérdate: <strong>detener (todos) siempre el último</strong>.') +
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">8 · Aparecer y desaparecer</h3>'
         + caja(K8, 'Pieza: si está tocando al Jugador, esconder, sumar 1 a Puntos, esperar 1 '
                    'segundo, ir a una x aleatoria con y 140 y volver a mostrarse',
                pie='La moneda que recoges, el meteorito que esquivas, el bicho que cazas: '
                    'desaparece, cuenta, y vuelve a salir por otro sitio. <strong>Pon un '
                    '<em>mostrar</em> también al arrancar</strong>: si la partida anterior acabó '
                    'con el objeto escondido, sin eso no vuelve a aparecer nunca.')),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Tu juego funciona a la primera. Pero al pulsar la bandera verde por '
                       '<em>segunda</em> vez, el marcador sigue donde estaba y el personaje aparece '
                       'donde lo dejaste. ¿Qué le falta?',
                  [('detener', 'Un bloque detener (todos) al final del programa',
                    'No. Eso apaga el juego, pero no deja nada preparado para la partida siguiente: '
                    'el problema aparece justo al <em>volver a empezar</em>.'),
                   ('inicializar', 'Poner en su sitio, nada más arrancar, todo lo que el juego '
                    'cambia: posición, variables, disfraz, tamaño…',
                    'Correcto, y es la lección más útil de esta sesión. Se llama <b>inicializar</b>. '
                    'Regla práctica: por cada cosa que tu juego modifica mientras se juega, tiene '
                    'que haber un bloque debajo de la bandera que la devuelva a su valor de salida.'),
                   ('guardar', 'Guardar el proyecto y volver a cargarlo antes de cada partida',
                    'Eso lo arreglaría por casualidad, pero es inviable: un juego tiene que poder '
                    'jugarse muchas veces seguidas sin recargar nada.')],
                  'inicializar')),

        ('Tu actividad',
         pasos([
             'Saca tu ficha de la sesión 17 y ténla al lado.',
             'Crea los objetos y los fondos que dice la ficha. Sin programar nada todavía.',
             'Monta <strong>primero la mecánica principal</strong>: lo que hace el jugador. Nada más.',
             'Pruébala. Cuando funcione, añade la condición de <strong>ganar</strong>.',
             'Pruébala otra vez. Después la de <strong>perder</strong>.',
             'Repasa la <strong>inicialización</strong>: pulsa la bandera tres veces seguidas y '
             'comprueba que las tres partidas empiezan exactamente igual.',
             'Descarga el <code>.sb3</code> aunque no hayas terminado.']) +
         ojo('Prueba después de cada pieza, no al final',
             '<p>Si montas veinte bloques y luego pruebas, cuando algo falle tendrás veinte '
             'sospechosos. Si pruebas después de cada pieza, sólo tienes uno: el último que has '
             'puesto.</p>')),

        ('Lo has conseguido si…',
         logros(['El juego se puede jugar de principio a fin.',
                 'Se puede ganar y se puede perder.',
                 'Tres partidas seguidas empiezan exactamente igual.',
                 'Has descargado el <code>.sb3</code>.'])),
    ])

# ============================================================ S19
FALLOS = [
    ['No pasa nada al pulsar la bandera',
     'El programa no tiene sombrero, o lo tiene en otro objeto',
     'Haz clic directamente sobre el montón de bloques. Si se ejecuta, el problema es el sombrero'],
    ['El personaje se mueve una sola vez',
     'Falta el <em>por siempre</em> alrededor de los condicionales',
     'Mira si tus condicionales están sueltos debajo de la bandera'],
    ['El marcador sube de golpe',
     'La condición sigue siendo verdad durante varias vueltas del bucle',
     'Añade una espera o aleja los objetos después de sumar (lo viste en el Pong)'],
    ['El marcador no vuelve a 0 al empezar',
     'Falta inicializar la variable debajo de la bandera',
     'Pulsa la bandera dos veces seguidas y compara'],
    ['Dos objetos hacen lo mismo o se pisan',
     'Has montado los dos programas en el mismo objeto',
     'Mira qué objeto tienes seleccionado abajo a la derecha, y luego el otro'],
    ['El sonido no suena',
     'El sonido no está en la lista de <em>ese</em> objeto',
     'Pestaña Sonidos del objeto: si no está, añádelo desde la biblioteca'],
]
PULIDO = [
    ['<strong>Pantalla de inicio</strong> ✱', 'Un fondo de portada con el título y cómo se juega',
     'Pieza 6 de la S18'],
    ['<strong>Pantalla de fin</strong> ✱', 'Un fondo distinto con la puntuación final',
     'Pieza 7 de la S18 · S13'],
    ['Instrucciones', 'Un <em>decir</em> al empezar que explique las teclas', 'S01'],
    ['Sonido', 'Al puntuar, al chocar y al terminar', 'S01 · S11'],
    ['Reacción visible', 'Cambio de disfraz al acertar o al fallar', 'S06'],
    ['Marcador a la vista', 'Variables mostradas, y sólo las que interesan al jugador', 'S08 · S09'],
    ['Aparecer y desaparecer', 'Que lo que recoges o esquivas se esconda y vuelva a salir',
     'Pieza 8 de la S18'],
    ['Dificultad creciente', 'Que se vaya poniendo más difícil según avanzas', 'S16'],
]
DEPURA19 = [
    ('stack', 'looks', ['decir', var('Vidas'), 'durante', ('num', '1'), 'segundos']),
]

s19 = pagina(
    19, 'Proyecto final: mejoras',
    'Sesión 19 de Scratch: depurar el proyecto final y pulirlo. Los seis fallos típicos y cómo '
    'localizarlos. CyR 1º ESO.',
    'que tu juego <strong>no se rompa</strong> y que se entienda sin que tengas que estar al lado '
    'explicándolo.',
    [
        ('Depurar es buscar, no adivinar',
         '<p>Cuando algo falla, la tentación es cambiar bloques a ver si suena la flauta. Casi '
         'nunca sale bien, y de paso rompes lo que iba.</p>'
         '<p>Depurar es otra cosa: <strong>ir quitando sospechosos</strong> hasta que quede uno. '
         'Dos herramientas, las dos dentro de Scratch:</p>' +
         pasos([
             '<strong>Haz clic sobre un montón de bloques.</strong> Se ejecuta ahí mismo, sin la '
             'bandera. Así pruebas una pieza sola.',
             '<strong>Mete un <em>decir</em> donde sospeches.</strong> Te enseña lo que vale una '
             'variable en ese punto. Luego lo quitas.'
         ]) +
         caja(DEPURA19, 'Bloque decir la variable Vidas durante 1 segundo', ancho=340,
              pie='Un espía: cuenta lo que pasa por dentro.')),

        ('Los seis fallos de siempre',
         '<p>Busca aquí tu síntoma antes de tocar nada.</p>' +
         tabla(['Lo que ves', 'Casi siempre es…', 'Cómo lo compruebas'], FALLOS)),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Tu personaje no se mueve y no tienes ni idea de por qué. '
                       '¿Cuál es la primera comprobación que harías?',
                  [('cero', 'Borrar el programa y volver a montarlo desde el principio',
                    'Es lo último, no lo primero. Tardas mucho y lo más probable es que vuelvas a '
                    'cometer el mismo fallo, porque no habrás llegado a saber cuál era.'),
                   ('clic', 'Hacer clic directamente sobre el montón de bloques para ver si '
                    'funciona por sí solo',
                    'Correcto. En dos segundos partes el problema en dos: si al hacer clic el '
                    'personaje se mueve, los bloques están bien y el fallo está en cómo arranca '
                    '(el sombrero, el objeto seleccionado). Si no se mueve, el fallo está dentro. '
                    'Has pasado de veinte sospechosos a diez.'),
                   ('reiniciar', 'Recargar la página o reiniciar el ordenador',
                    'Los fallos de Scratch casi nunca son del ordenador: son del programa. '
                    'Recargar además te haría perder el proyecto si no lo has descargado.')],
                  'clic')),

        ('Tu actividad',
         '<p><strong>Primero arregla, después adorna.</strong> En este orden:</p>' +
         pasos([
             'Juega tres partidas enteras. Apunta en un papel todo lo raro, por pequeño que sea.',
             'Arregla los fallos de arriba abajo. Después de cada arreglo, juega otra partida.',
             'Cuando ya no se rompa nada, y sólo entonces, coge la lista de pulido de abajo.',
             'Haz las <strong>dos marcadas con ✱</strong> y elige <strong>una más</strong>. '
             'Tres bien hechas, no siete a medias. Las dos obligatorias son las que hacen que el '
             'juego se entienda sin ti: 2 puntos de la rúbrica.',
             'Deja que un compañero juegue <strong>sin decirle nada</strong>. Si te pregunta cómo '
             'se juega, te faltan instrucciones.']) +
         tabla(['Mejora', 'En qué consiste', 'De dónde sale'], PULIDO) +
         ojo('La prueba del compañero es la más dura y la más útil',
             '<p>Tú sabes jugar porque lo has hecho tú. Un compañero encuentra en dos minutos '
             'cosas que tú no has visto en tres sesiones. Déjale jugar y <strong>no le '
             'ayudes</strong>: apunta dónde se atasca.</p>')),

        ('Lo has conseguido si…',
         logros(['Has jugado tres partidas enteras sin que aparezca ningún fallo.',
                 'Un compañero ha sabido jugar sin que le expliques nada.',
                 'El juego tiene pantalla de inicio y pantalla de fin.',
                 'Has añadido una tercera mejora de la lista, terminada.',
                 'Has descargado la versión buena del <code>.sb3</code>.'])),
    ])

# ============================================================ S20
s20 = pagina(
    20, 'Presentación de proyectos',
    'Sesión 20 de Scratch: presentar el proyecto final en un minuto, rúbrica de evaluación y '
    'entrega definitiva. CyR 1º ESO.',
    'presentar tu proyecto en <strong>un minuto</strong> y entregarlo. Último día del trimestre.',
    [
        ('Con qué se te va a evaluar',
         '<p>Esto no es ninguna sorpresa: es la misma lista que se publicó en la '
         '<a href="s17.html#rubrica">sesión 17</a>, el día que diseñaste el proyecto. '
         'Léela antes de presentar y comprueba tú mismo por dónde andas.</p>' +
         tabla(['Criterio', 'Qué se mira', 'Puntos'], RUBRICA) +
         '<p>Fíjate en que <strong>«funciona» y «se entiende solo» suman 5 de los 10 puntos</strong>. '
         'Un juego sencillo, terminado y claro saca mejor nota que uno ambicioso a medias. '
         'Lleva siendo así todo el trimestre.</p>'),

        ('El guion del minuto',
         '<p>Un minuto es poco y se pasa volando, así que llévalo pensado. Cuatro frases:</p>' +
         pasos([
             '<strong>Qué es.</strong> «Es un juego de esquivar meteoritos». Una frase, sin rodeos.',
             '<strong>Cómo se juega.</strong> Enséñalo mientras lo dices: mueve el personaje, '
             'marca un punto. No lo cuentes, hazlo.',
             '<strong>Qué fue lo más difícil</strong> y cómo lo resolviste. Esta es la parte que '
             'de verdad interesa, porque es donde se ve lo que has aprendido.',
             '<strong>Qué le añadirías</strong> si tuvieras otra sesión.']) +
         ojo('Dos consejos que valen la nota',
             '<p><strong>Ten el juego ya abierto y probado</strong> antes de que te toque. '
             'Perder treinta segundos buscando el archivo es perder medio minuto de tu tiempo.</p>'
             '<p style="margin-bottom:0">Y si al presentar falla algo, <strong>dilo y sigue</strong>. '
             'Explicar por qué crees que ha fallado suma; quedarse en blanco intentando arreglarlo '
             'delante de todos, no.</p>')),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Te quedan cinco minutos antes de presentar y tu juego funciona pero es '
                       'sencillo. ¿Qué haces?',
                  [('anadir', 'Añadir a toda prisa un segundo nivel para que parezca más completo',
                    'Es la peor opción. Tocar el código cinco minutos antes de presentar es la '
                    'forma más rápida de llegar con un juego que antes funcionaba y ahora no. '
                    'Y «funciona» vale 3 puntos.'),
                   ('probar', 'Jugar una partida entera para comprobar que va, y repasar las cuatro '
                    'frases del guion',
                    'Correcto. Con el juego terminado, lo que queda por ganar está en presentarlo '
                    'bien —2 puntos— y en no romper lo que ya funciona —3 puntos—. Añadir cosas a '
                    'última hora no puntúa y arriesga mucho.'),
                   ('otro', 'Pedirle a un compañero que te enseñe el suyo para copiar alguna idea',
                    'Para aprender está muy bien, pero no ahora: no te da tiempo a implementarla y '
                    'te quedas sin repasar tu presentación.')],
                  'probar')),

        ('Antes de presentar: última comprobación',
         logros(['El <code>.sb3</code> está descargado y sabes en qué carpeta.',
                 'Lo has subido a Moodle. <strong>Ahora, no luego.</strong>',
                 'Has jugado una partida entera hoy mismo, en este ordenador.',
                 'El juego se puede ganar y se puede perder.',
                 'Tienes las cuatro frases del guion pensadas.',
                 'Sabes decir qué fue lo más difícil.'])),
    ],
    abrir=False,
    entrega='<ol>'
            '<li><strong>Archivo → Guardar en tu ordenador.</strong> El <code>.sb3</code> aparece '
            'en <strong>Descargas</strong>.</li>'
            '<li>Cámbiale el nombre a <strong>ProyectoFinal_TuNombre.sb3</strong>.</li>'
            '<li>Súbelo a la tarea de <strong>Moodle</strong> de la sesión 20, junto con un texto '
            'corto: qué es, qué fue lo más difícil y qué le añadirías.</li>'
            '<li>Esta entrega es la del trimestre. Compruébalo antes de irte.</li></ol>')

for n, h in [(17, s17), (18, s18), (19, s19), (20, s20)]:
    escribir(n, h)

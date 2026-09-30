# -*- coding: utf-8 -*-
"""Los apartados de «Tu actividad» de cada sesión de T1 (S01–S17): títulos, objetos y el N.2.

«Tu actividad» tiene tres apartados numerados, con títulos que son órdenes (Manuel, 30-09:
«nada de último paso ni reto… algo más taxativo»):

  N.1  la actividad de siempre, que escriben los gen_s??.py;      título en ORDEN_1
  N.2  el paso siguiente, que nació como «Si te ha sobrado tiempo»; título en ORDEN_2 y
       texto en AMPLIACIONES (este archivo)
  N.3  un programa en seudocódigo que hay que pasar a bloques;     pseudocodigo.py

Las instrucciones son dirigidas: los objetos van por su nombre en la biblioteca de Scratch
(que está en inglés aunque el editor esté en español), para que toda la clase tenga lo mismo;
luego Manuel deja cambiarlos a quien quiera. OBJETOS dice qué objetos tiene el proyecto al
terminar y en qué apartado entra cada uno: la actividad lo dice al empezar y la entrega lo
repite.

La regla del N.2: lo que ya saben más UN bloque nuevo como mucho, y en pasos numerados.
"""


def P(*items):
    """Lista de pasos con la misma marca que plantilla.pasos() (no se importa: la plantilla
    importa este módulo)."""
    return ('<ol class="paso-lista">' + ''.join(
        '<li><span class="p">Paso %d</span><span>%s</span></li>' % (i + 1, t)
        for i, t in enumerate(items)) + '</ol>')


def OJO(titulo, cuerpo):
    return '<div class="aviso-ojo"><h3>⚠️ %s</h3><p>%s</p></div>' % (titulo, cuerpo)


def elige(nombre, busca, que):
    """«botón Elige un objeto, escribe X en el buscador y elige Y»."""
    return ('botón <strong>Elige un objeto</strong> (el del gato, abajo a la derecha), escribe '
            '<strong>%s</strong> en el buscador y elige <strong>%s</strong>, %s' % (busca, nombre, que))


ORDEN_1 = {
    1: 'Monta tu primer programa', 2: 'Completa el cuadrado', 3: 'Recorre las tres figuras',
    4: 'Monta las tres versiones', 5: 'Completa el programa', 6: 'Haz que tus personajes caminen',
    7: 'Construye el diálogo', 8: 'Construye la calculadora', 9: 'Construye el quiz',
    10: 'Monta la carrera', 11: 'Haz que el gato avise a la pelota', 12: 'Construye el laberinto',
    13: 'Añade la meta y el segundo nivel', 14: 'Completa el juego', 15: 'Monta la pelota y la pala',
    16: 'Añade el marcador y el final', 17: 'Arregla los cinco programas',
}
ORDEN_2 = {
    1: 'Haz que el perro conteste al gato', 2: 'Haz que el gato recorra un rectángulo con la tecla R',
    3: 'Dibuja las figuras con el lápiz', 4: 'Añade una cuarta flecha con el operador «o»',
    5: 'Añade un perro que se mueva con W, A, S y D', 6: 'Haz que el oso sólo camine cuando lo mueves',
    7: 'Haz que el gato calcule tu edad dentro de diez años', 8: 'Añade la media y el resto',
    9: 'Añade las vidas', 10: 'Haz que el ganador diga su tiempo', 11: 'Encadena un segundo mensaje',
    12: 'Añade una estrella que dé puntos', 13: 'Guarda el mejor tiempo',
    14: 'Haz que el gato enseñe lo que ha sacado', 15: 'Maneja la pala con teclas y añade otra pelota',
    16: 'Haz que la pelota cambie de color con los puntos', 17: 'Rompe un programa para otra pareja',
}

# num -> [(objeto, apartados)]; un apartado entero k es «N.k»; un texto va tal cual.
OBJETOS = {
    1: [('el gato', [1]), ('el perro', [1, 2]), ('la pelota', [3])],
    2: [('el gato', [1, 2]), ('la mariposa', [3])],
    3: [('el gato', [1, 2]), ('el lápiz', [3])],
    4: [('el gato', [1, 2]), ('el murciélago', [3])],
    5: [('el gato', [1]), ('el perro', [2]), ('el coche', [3])],
    6: [('el gato', [1]), ('el oso', [1, 2]), ('el loro', [3])],
    7: [('el gato', [1, 2]), ('el robot', [3])],
    8: [('el gato', [1, 2]), ('el perro', [3])],
    9: [('el gato', [1, 2]), ('el búho', [3])],
    10: [('el gato', [1, 2]), ('el perro', [1, 2]), ('la rana', [3])],
    11: [('el gato', [1]), ('la pelota', [1, 2]), ('el portero', [2]), ('el árbitro', [3]),
         ('el tambor', [3])],
    12: [('el gato', [1, 2]), ('la estrella', [2]), ('el fantasma', [3])],
    13: [('el gato', [1, 2]), ('la estrella y el fantasma', ['de la sesión 12']), ('la meta', [1]),
         ('la campana', [3])],
    14: [('el gato', [1, 2]), ('el unicornio', [3])],
    15: [('la pelota', [1, 2]), ('la pala', [1, 2]), ('la segunda pelota', [2]), ('el globo', [3])],
    16: [('las dos pelotas, la pala y el globo', ['de la sesión 15']), ('el saltamontes', [3])],
    17: [('los cinco sospechosos', [1]), ('la bailarina', [3])],
}

LOGRO = 'El apartado {n}.2 también está hecho y va en el mismo archivo.'

# num -> lista de (título corto, cuerpo en HTML). Con un solo elemento, el título no se
# muestra (ya lo da ORDEN_2) y el cuerpo va tal cual.
AMPLIACIONES = {
    1: [('', '<p>Ahora el gato y el perro hablan <strong>a la vez</strong> y no se entiende nada. '
             'Haz que el perro espere a que el gato termine y entonces le conteste.</p>' + P(
        'Selecciona el <strong>perro</strong>, abajo a la derecha.',
        'En su programa, justo debajo de <strong>al hacer clic en la bandera</strong>, mete el '
        'bloque <strong>esperar (1) segundos</strong>. Está en Control, el naranja. Cambia el 1 por '
        'un <strong>2</strong>, que es lo que dura el bocadillo del gato.',
        'Cambia el texto del perro por una respuesta: si el gato dice «¡Hola! Soy Sprite1», el '
        'perro puede decir «¡Hola, gato! Yo soy el perro».',
        'Pulsa la bandera: primero habla el gato y, cuando termina, contesta el perro.'))],

    2: [('', '<p>El mismo gato, pero un <strong>segundo programa</strong> que arranca con una tecla '
             'en vez de con la bandera. Los bloques son los del cuadrado; lo que cambia es la forma: '
             'dos lados largos y dos cortos.</p>' + P(
        'Selecciona el gato. En Eventos, coge <strong>al presionar tecla</strong> y elige la '
        '<strong>r</strong> en el desplegable. Déjalo suelto, separado del programa del cuadrado.',
        'Debajo pon <strong>fijar estilo de rotación a (no rotar)</strong> e <strong>ir a x: -100 '
        'y: 50</strong>.',
        'Ahora los cuatro lados: <strong>200 pasos</strong> hacia la derecha (dirección 90), '
        '<strong>100</strong> hacia abajo (180), <strong>200</strong> hacia la izquierda (-90) y '
        '<strong>100</strong> hacia arriba (0). Cada lado es un <em>apuntar en dirección</em> y un '
        '<em>mover</em>, y después de cada uno un <em>esperar 1 segundos</em>.',
        'Pulsa <strong>R</strong>: el gato recorre un rectángulo y acaba en el mismo sitio donde '
        'empezó. Si no acaba ahí, repasa pasos y direcciones lado por lado.'))],

    3: [('', '<p>El gato recorre las figuras, pero no deja rastro. Con la extensión '
             '<strong>Lápiz</strong> se quedan dibujadas.</p>' + P(
        'Pulsa el botón azul de abajo a la izquierda, <strong>Añadir extensión</strong>, y elige '
        '<strong>Lápiz</strong>. Aparece una categoría verde nueva, abajo del todo.',
        'En los tres programas (teclas 1, 2 y 3), justo debajo del sombrero, pon <strong>borrar '
        'todo</strong> y <strong>subir lápiz</strong>.',
        'En los tres, justo después de <em>ir a x: -75 y: 75</em>, pon <strong>bajar '
        'lápiz</strong>.',
        'Pulsa 1, 2 y 3: cada figura se queda dibujada y borra la anterior. Si ves una raya que va '
        'de una figura a otra, te falta el <em>subir lápiz</em> antes del <em>ir a</em>.',
        'La flor: un cuarto programa en el gato con <strong>al presionar tecla 4</strong>: borrar '
        'todo, subir lápiz, ir a x: 0 y: 0, bajar lápiz y <strong>repetir 36</strong> con <em>mover '
        '100 pasos</em> y <em>girar 100 grados</em> dentro, sin espera. Antes de pulsar el 4, '
        'intenta adivinar qué va a salir.'))],

    4: [('', '<p>Tienes una versión que se para con el espacio y otra que se para en el borde. La '
             'cuarta, con la <strong>flecha izquierda</strong>, se para con <strong>lo que pase '
             'antes</strong> de las dos cosas.</p>' + P(
        'Haz clic derecho sobre el sombrero del programa de la <strong>flecha derecha</strong> y '
        'elige <strong>Duplicar</strong>. Suelta la copia en un sitio libre.',
        'En la copia, cambia la tecla del sombrero por <strong>flecha izquierda</strong>.',
        'Saca el <em>¿tocando borde?</em> del hueco del <em>repetir hasta que</em> y déjalo a un '
        'lado. En su sitio pon el operador verde <strong>&lt; &gt; o &lt; &gt;</strong>, que está en '
        'Operadores.',
        'En el hueco izquierdo del <em>o</em> mete un <strong>¿tecla espacio presionada?</strong>; '
        'en el derecho, el <strong>¿tocando borde?</strong> que habías sacado.',
        'Pulsa la flecha izquierda: el gato se para al pulsar espacio <strong>o</strong> al llegar '
        'al borde, lo que pase primero.'))],

    5: [('', '<p>Un <strong>perro</strong> que se mueve igual que el gato, pero con las teclas '
             '<strong>W, A, S y D</strong>. Su programa no se monta otra vez: <strong>se copia el '
             'del gato y se cambia lo que es distinto</strong>.</p>' + P(
        'Añade el perro: ' + elige('Dog2', 'Dog', 'el perro azul.'),
        'Vuelve a seleccionar el <strong>gato</strong>, coge su programa por el bloque de arriba '
        '(la bandera verde) y <strong>arrástralo entero hasta el icono del perro</strong>, en la '
        'lista de objetos de abajo a la derecha. Suéltalo cuando el icono se mueva: eso quiere '
        'decir que lo ha recibido.',
        'Selecciona el perro. El programa ya está ahí, copiado. El gato sigue teniendo el suyo: '
        'no se ha movido, se ha duplicado.',
        'En el programa del perro, cambia sólo las teclas de los desplegables: <strong>flecha '
        'arriba → W</strong>, <strong>flecha abajo → S</strong>, <strong>flecha izquierda → '
        'A</strong>, <strong>flecha derecha → D</strong>.',
        'Pulsa la bandera: el gato se mueve con las flechas y el perro con W, A, S y D.') + OJO(
        'Apréndete este truco',
        'Copiar un programa de un objeto a otro arrastrándolo hasta su icono es de lo que más '
        'vas a usar. En cuanto un juego tiene varios objetos que hacen casi lo mismo —los '
        'corredores de la carrera, las monedas del laberinto, los enemigos de tu proyecto final—, '
        'nadie los monta uno a uno: se hace el primero, se copia y se cambia lo que es distinto.'))],

    6: [('', '<p>El gato y el oso pasean solos. Ahora el oso va a caminar <strong>sólo mientras '
             'mantienes pulsada una flecha</strong>, y a quedarse quieto cuando la sueltas: lo de '
             'hoy junto con lo de la sesión 5.</p>' + P(
        'Selecciona el <strong>oso</strong>.',
        'Saca del <em>por siempre</em> los cuatro bloques de dentro (siguiente disfraz, esperar, '
        'mover y rebotar) y déjalos a un lado: los vas a reutilizar.',
        'Dentro del <em>por siempre</em> pon un <strong>si ¿tecla flecha derecha presionada? '
        'entonces</strong>. Dentro de él: <em>apuntar en dirección 90</em>, <em>siguiente '
        'disfraz</em>, <em>mover 10 pasos</em> y <em>esperar 0.1 segundos</em>.',
        'Debajo, otro <strong>si</strong> igual para la <strong>flecha izquierda</strong>, con '
        '<em>apuntar en dirección -90</em>. Truco: duplica el primero y cambia la tecla y la '
        'dirección.',
        'Tira a la paleta los bloques que te hayan sobrado y pulsa la bandera: el gato sigue '
        'paseando solo y el oso sólo camina mientras mantienes una flecha.'))],

    7: [('', '<p>Una cuarta pregunta, <strong>¿Cuántos años tienes?</strong>, y que el gato '
             'conteste <strong>calculando</strong>, no repitiendo.</p>' + P(
        'Al final del programa del gato, añade <strong>preguntar ¿Cuántos años tienes? y '
        'esperar</strong>.',
        'Debajo, un <strong>decir</strong> con un <strong>unir</strong> dentro. En el primer hueco '
        'del unir escribe <strong>Dentro de diez años tendrás </strong> (con un espacio al '
        'final).',
        'En el segundo hueco del unir mete el operador verde <strong>( ) + ( )</strong>, que está '
        'en Operadores. En su hueco izquierdo, el bloque <strong>respuesta</strong>; en el '
        'derecho, un <strong>10</strong>.',
        'Prueba con 12: tiene que decir «Dentro de diez años tendrás 22».'))],

    8: [('', '<p>Dos cuentas más en la calculadora: la <strong>media</strong> de los dos números y '
             'el <strong>resto</strong> de dividir el primero entre el segundo.</p>' + P(
        'Añade al final un <strong>decir</strong> con un <strong>unir</strong>: «La media es » en '
        'el primer hueco.',
        'En el segundo hueco, el operador <strong>( ) / ( )</strong>. En su hueco izquierdo mete '
        'un <strong>( ) + ( )</strong> con <em>num1</em> y <em>num2</em>; en el derecho, un '
        '<strong>2</strong>. Es la cuenta (num1 + num2) / 2: un operador dentro de otro, como los '
        '<em>unir</em> dentro de <em>unir</em> de la sesión 7.',
        'Otro <strong>decir</strong> con <strong>unir</strong>: «El resto es » y el operador '
        '<strong>( ) módulo ( )</strong> con <em>num1</em> y <em>num2</em>. «Módulo» es como Scratch '
        'llama al resto de una división.',
        'Prueba con 7 y 2: la media es 4.5 y el resto es 1.'))],

    9: [('', '<p>La partida deja de acabar a las diez preguntas: acaba cuando te quedas '
             '<strong>sin vidas</strong>. Esta pieza la vas a volver a usar en el proyecto '
             'final.</p>' + P(
        'Crea la variable <strong>Vidas</strong>.',
        'Al principio del programa, junto a <em>dar a Aciertos el valor 0</em>, pon <strong>dar a '
        'Vidas el valor 3</strong>.',
        'En la parte del <em>si no</em> (cuando fallas), añade <strong>sumar a Vidas -1</strong>. '
        'Para restar se suma un número negativo.',
        'Cambia el <em>repetir 10</em> por un <strong>repetir hasta que</strong> con el operador '
        '<strong>( ) = ( )</strong>: <em>Vidas</em> en un hueco y <strong>0</strong> en el otro. '
        'Pasa los bloques de dentro del uno al otro.',
        'Juega: la partida sigue mientras aciertes y se acaba al tercer fallo.'))],

    10: [('', '<p>El que gana dice <strong>cuánto ha tardado</strong>. En Sensores hay un bloque '
              'redondo, <strong>cronómetro</strong>, que cuenta los segundos desde que se '
              'reinicia.</p>' + P(
        'Selecciona el gato. Justo debajo de la bandera, pon <strong>reiniciar cronómetro</strong> '
        '(Sensores).',
        'Cambia el texto «¡He ganado!» por un <strong>unir</strong>: «He ganado en » en el primer '
        'hueco y el bloque <strong>cronómetro</strong> en el segundo.',
        'Haz lo mismo en el perro.',
        'Juega unas cuantas: el que gana dice su tiempo, y cada vez es distinto. Lo vas a '
        'necesitar en la sesión 13.'))],

    11: [('', '<p>Un mensaje que provoca otro: el gato avisa a la pelota y, cuando la pelota '
              'termina, avisa al <strong>portero</strong>.</p>' + P(
        'Añade el portero: ' + elige('Goalie', 'Goalie', 'el portero. Arrástralo a la derecha del '
                                     'escenario.'),
        'Selecciona la <strong>pelota</strong>. Al final de su programa de <em>al recibir '
        'patada</em>, añade <strong>enviar</strong> y, en su desplegable, <strong>Nuevo '
        'mensaje</strong>: llámalo <strong>gol</strong>.',
        'Selecciona el portero: <strong>al recibir gol</strong>, <strong>decir ¡Noooo! durante 2 '
        'segundos</strong>.',
        'Pulsa la bandera: el gato chuta, la pelota sale y, cuando termina, el portero se lamenta. '
        'Nadie ha pulsado nada para que el portero hable: se lo ha dicho la pelota.'))],

    12: [('', '<p>Una <strong>estrella</strong> dentro del laberinto que da un punto al cogerla y '
              'desaparece.</p>' + P(
        'Añade la estrella: ' + elige('Star', 'Star', 'la estrella amarilla. Ponle tamaño '
                                      '<strong>50</strong> y colócala en un pasillo.'),
        'Crea la variable <strong>Puntos</strong>. En el programa del <strong>gato</strong>, justo '
        'debajo de la bandera, pon <strong>dar a Puntos el valor 0</strong>.',
        'Selecciona la estrella: <strong>al hacer clic en la bandera</strong>, '
        '<strong>mostrar</strong> y un <strong>por siempre</strong> con un <strong>si ¿tocando '
        'Sprite1? entonces</strong> dentro. Sprite1 es el gato.',
        'Dentro del <em>si</em>: <strong>sumar a Puntos 1</strong>, <strong>esconder</strong> y '
        '<strong>detener este programa</strong>. Mostrar y esconder están en Apariencia; el '
        'detener es el de la sesión 4, con «este programa» en el desplegable.',
        'Juega: al pasar por la estrella desaparece y Puntos sube a 1. Sólo a 1: sin el '
        '<em>detener</em>, seguiría sumando mientras la tocas.'))],

    13: [('', '<p>Una variable <strong>MejorTiempo</strong> que guarda el tiempo más bajo de todas '
              'las partidas. Es la primera variable que no se borra al volver a jugar.</p>' + P(
        'Crea la variable <strong>MejorTiempo</strong>.',
        'Arrastra al área de código, suelto, un bloque <strong>dar a MejorTiempo el valor '
        '999</strong>. Haz <strong>un clic</strong> encima (un clic ejecuta un bloque sin '
        'bandera) y comprueba que la variable marca 999. Después tíralo a la paleta.',
        'En el condicional de la meta, justo antes del <em>detener todos</em> que termina el juego, pon un '
        '<strong>si</strong> con el operador <strong>( ) &lt; ( )</strong>: <em>cronómetro</em> a la '
        'izquierda y <em>MejorTiempo</em> a la derecha.',
        'Dentro de ese <em>si</em>: <strong>dar a MejorTiempo el valor (cronómetro)</strong>.',
        'Juega dos partidas: si la segunda es más rápida, MejorTiempo baja; si es más lenta, se '
        'queda como estaba. Al arrancar <strong>no</strong> la pongas a 0, o la siguiente partida '
        'se olvida de las anteriores.'))],

    14: [('', '<p>Que el gato <strong>enseñe</strong> lo que ha sacado, con un dibujo, además de '
              'decirlo.</p>' + P(
        'Selecciona el gato y ve a la pestaña <strong>Disfraces</strong>.',
        'Pinta tres disfraces nuevos (el pincel de abajo a la izquierda, <strong>Pinta</strong>): '
        'una piedra, un papel y unas tijeras. No hace falta que sean bonitos.',
        'Cámbiales el nombre, arriba, exactamente a <strong>piedra</strong>, '
        '<strong>papel</strong> y <strong>tijera</strong>: en minúscula y sin tilde, igual que los '
        'textos de la variable <em>maquina</em>.',
        'Vuelve a Código. Justo después de los tres <em>si</em> del sorteo, pon <strong>cambiar '
        'disfraz a</strong> y mete la variable <strong>maquina</strong> en su hueco: Scratch busca '
        'el disfraz que se llame igual.',
        'Juega: el gato se convierte en lo que ha sacado.'))],

    15: [('', '<p>La pala pasa a moverse con las teclas <strong>A</strong> y <strong>D</strong>, y '
              'entra una segunda pelota.</p>' + P(
        'Selecciona la <strong>pala</strong>. Quita el <em>ir a x: (posición x del ratón) y: '
        '-140</em> de dentro del <em>por siempre</em>.',
        'Antes del <em>por siempre</em>, pon <strong>ir a x: 0 y: -140</strong>.',
        'Dentro del <em>por siempre</em>: <strong>si ¿tecla a presionada? entonces sumar a x '
        '-10</strong> y <strong>si ¿tecla d presionada? entonces sumar a x 10</strong>. Es lo '
        'de la sesión 5.',
        'Haz clic derecho sobre el icono de la <strong>pelota</strong>, abajo a la derecha, y elige '
        '<strong>duplicar</strong>. En el programa de la copia cambia la dirección de salida '
        '<strong>160</strong> por <strong>200</strong>.',
        'Pulsa la bandera: dos pelotas rebotando y una pala que manejas con A y D.'))],

    16: [('', '<p>Cada vez que marcas, la pelota <strong>cambia de color</strong>. Y cuando lo '
              'tengas, que sólo cambie cada 5 puntos.</p>' + P(
        'Selecciona la pelota. En el condicional de la pala, junto a <em>sumar a Puntos 1</em>, '
        'pon <strong>sumar al efecto color 25</strong>, de Apariencia.',
        'Juega: cada punto, un color distinto.',
        'Ahora mete ese bloque dentro de un <strong>si</strong> con el operador <strong>( ) = ( '
        ')</strong>: en un hueco, <strong>( Puntos ) módulo ( 5 )</strong>; en el otro, '
        '<strong>0</strong>.',
        'Juega: el color sólo cambia a los 5, 10, 15… puntos.'))],

    17: [('', '<p>Para romper algo a propósito hay que entenderlo mejor que para arreglarlo.</p>' + P(
        'Abre en otra pestaña un programa tuyo de otra sesión (el Pong vale).',
        'Métele <strong>un solo fallo</strong> de los cinco tipos de hoy, uno que se note al '
        'ejecutar: quita un <em>ir a</em>, un estilo de rotación, un <em>dar a … el valor 0</em>, '
        'cambia un número de un <em>repetir</em> o saca un <em>si</em> de su <em>por '
        'siempre</em>.',
        'Descárgalo como <strong>Roto_TuNombre.sb3</strong>.',
        'Pásaselo a otra pareja que haya terminado (si no hay ninguna, al profesor): tienen que '
        'encontrarlo con el método de hoy y decirte cuál era.',
        'Apunta en tu entrega qué fallo metiste y si te lo encontraron.'))],
}


def caja_ampliacion(num, seccion=4):
    """El apartado N.2 de la sesión `num`, o '' si no tiene."""
    items = AMPLIACIONES.get(num)
    if not items:
        return ''
    if len(items) == 1:
        c = items[0][1]
        cuerpo = c if c.lstrip().startswith('<') else '<p>%s</p>' % c
    else:
        cuerpo = '<ul>%s\n</ul>' % ''.join('\n  <li><b>%s.</b> %s</li>' % (t, c) for t, c in items)
    return ('<h3 class="sub"><span class="subn">%d.2</span>%s</h3>\n%s'
            % (seccion, ORDEN_2[num], cuerpo))

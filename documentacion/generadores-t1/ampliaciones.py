# -*- coding: utf-8 -*-
"""El último paso de la actividad de cada sesión de T1 (S01–S17): la caja «⭐ Último paso».

Nació como ampliación optativa para los que acababan antes («Si te ha sobrado tiempo»), y
a los dos días pasó a ser parte de la actividad: las sesiones se hacían en veinte minutos
y Manuel prefiere que una tarea ocupe más de una clase a tener al grupo media hora sin
nada que hacer. Se entrega en el mismo .sb3 que el resto y cuenta para la nota igual que
los demás pasos.

La regla para escribirlos no cambia: lo que ya saben más UN bloque nuevo como mucho.

plantilla.pagina() coloca la caja al final de «Tu actividad», numerada como el paso
siguiente al último de la lista de pasos (o «Último paso» si la sesión no lleva lista),
y añade a «Lo has conseguido si…» la línea que lo comprueba. Para quitar el paso de una
sesión, se borra su entrada y se regenera.
"""

# Títulos de los apartados de «Tu actividad»: órdenes, no rótulos (Manuel, 30-09: «nada de
# último paso ni reto… algo más taxativo»). 4.1 es la actividad de siempre; 4.2 el paso que
# sigue (AMPLIACIONES, abajo); 4.3 el seudocódigo (pseudocodigo.py).
ORDEN_1 = {
    1: 'Monta tu primer programa', 2: 'Completa el cuadrado', 3: 'Recorre las tres figuras',
    4: 'Monta las tres versiones', 5: 'Completa el programa', 6: 'Haz que tu personaje camine',
    7: 'Construye el diálogo', 8: 'Construye la calculadora', 9: 'Construye el quiz',
    10: 'Monta la carrera', 11: 'Haz que un objeto avise a otro', 12: 'Construye el laberinto',
    13: 'Añade la meta y el segundo nivel', 14: 'Completa el juego', 15: 'Monta la pelota y la pala',
    16: 'Añade el marcador y el final', 17: 'Arregla los cinco programas',
}
ORDEN_2 = {
    1: 'Haz que el segundo personaje conteste', 2: 'Haz que el gato recorra un rectángulo',
    3: 'Dibuja las figuras con el lápiz', 4: 'Añade una cuarta flecha con el operador «o»',
    5: 'Añade un perro que se mueva con W, A, S y D', 6: 'Haz que sólo camine cuando lo mueves',
    7: 'Haz que el personaje calcule tu edad', 8: 'Añade la media y el resto',
    9: 'Añade las vidas', 10: 'Haz que el ganador diga su tiempo', 11: 'Encadena tres mensajes',
    12: 'Añade una moneda que dé puntos', 13: 'Guarda el mejor tiempo',
    14: 'Haz que la máquina enseñe lo que ha sacado', 15: 'Maneja la pala con teclas y añade otra pelota',
    16: 'Haz que la pelota cambie con los puntos', 17: 'Rompe un programa para otra pareja',
}

# Los objetos que tiene que haber en el proyecto al terminar, por apartado: la actividad lo
# dice al empezar y la entrega lo repite. Directos a propósito (Manuel, 30-09: «para que
# todos tengan lo mismo… gato, perro, coche»); luego él deja cambiarlos a quien quiera.
OBJETOS = {
    5: ['el gato', 'el perro', 'el coche'],
}

LOGRO = 'El apartado {n}.2 también está hecho y va en el mismo archivo.'

# num de sesión -> lista de (título corto, cuerpo en HTML)
AMPLIACIONES = {
    1: [('Una conversación de verdad',
         'Ahora tus dos personajes hablan a la vez. Haz que el segundo <strong>espere 2 '
         'segundos</strong> antes de contestar, y que el primero le responda después. El bloque '
         'nuevo es <strong>esperar (1) segundos</strong>, naranja, de Control: se pone delante '
         'del <em>decir</em> y cambias el 1 por un 2.')],

    2: [('Otra figura con los mismos bloques',
         'Haz que el gato recorra un <strong>rectángulo</strong>: dos lados de 200 pasos y dos '
         'de 100. Tiene que acabar donde empezó, igual que el cuadrado. Y si eso te sale, la '
         'primera letra de tu nombre, si es una L, una T, una E o una F (esas no vuelven al '
         'principio, y no pasa nada).')],

    3: [('Que se vea lo que dibuja: la extensión Lápiz',
         'Pulsa el botón azul de abajo a la izquierda, <strong>Añadir extensión</strong>, y elige '
         '<strong>Lápiz</strong>. Aparece una categoría verde nueva. Pon <strong>bajar '
         'lápiz</strong> justo después del <em>ir a x: y:</em> en los tres programas, y '
         '<strong>borrar todo</strong> al principio de cada uno. Pulsa 1, 2 y 3: ahora las '
         'figuras se quedan dibujadas.'),
        ('La flor',
         'Con el lápiz bajado, un cuarto programa con la tecla 4: <strong>repetir 36</strong> con '
         '<em>mover 100 pasos</em> y <em>girar 100 grados</em> dentro, y sin la espera. Antes de '
         'pulsar, intenta adivinar qué va a salir.')],

    4: [('Una cuarta flecha: que se pare por lo que pase primero',
         'Tienes una versión que se para con el espacio y otra que se para en el borde. Júntalas '
         'en un cuarto programa, con la <strong>flecha izquierda</strong>: que se pare por '
         '<strong>cualquiera de las dos cosas</strong>, la que pase antes. El bloque nuevo es el '
         'operador verde <strong>&lt; &gt; o &lt; &gt;</strong>, de Operadores: tiene dos huecos '
         'hexagonales, y en cada uno metes una condición.')],

    5: [('Dos jugadores en el mismo escenario', (
        '<p>Un <strong>perro</strong> que se mueve igual que el gato, pero con las teclas <strong>W, A, S y D</strong>. Su programa no se monta otra vez: <strong>se copia el del gato y se cambia lo que es distinto</strong>.</p>'
        '<ol class="paso-lista"><li><span class="p">Paso 1</span><span>Añade el perro: botón <strong>Elige un objeto</strong> (el del gato, abajo a la derecha), escribe <strong>Dog</strong> en el buscador y elige <strong>Dog2</strong>, el perro azul.</span></li><li><span class="p">Paso 2</span><span>Vuelve a seleccionar el <strong>gato</strong>, coge su programa por el bloque de arriba (la bandera verde) y <strong>arrástralo entero hasta el icono del perro</strong>, en la lista de objetos de abajo a la derecha. Suéltalo cuando el icono se mueva: eso quiere decir que lo ha recibido.</span></li><li><span class="p">Paso 3</span><span>Selecciona el perro. El programa ya está ahí, copiado. El gato sigue teniendo el suyo: no se ha movido, se ha duplicado.</span></li><li><span class="p">Paso 4</span><span>En el programa del perro, cambia sólo las teclas de los desplegables: <strong>flecha arriba → W</strong>, <strong>flecha abajo → S</strong>, <strong>flecha izquierda → A</strong>, <strong>flecha derecha → D</strong>.</span></li><li><span class="p">Paso 5</span><span>Pulsa la bandera: el gato se mueve con las flechas y el perro con W, A, S y D.</span></li></ol>'
        '<div class="aviso-ojo"><h3>⚠️ Apréndete este truco</h3><p>Copiar un programa de un objeto a otro arrastrándolo hasta su icono es de lo que más vas a usar. En cuanto un juego tiene varios objetos que hacen casi lo mismo —los corredores de la carrera, las monedas del laberinto, los enemigos de tu proyecto final—, nadie los monta uno a uno: se hace el primero, se copia y se cambia lo que es distinto.</p></div>'
        ''))],

    6: [('Que sólo camine cuando tú lo mueves',
         'Junta lo de hoy con lo de la sesión 5: mete el <em>siguiente disfraz</em> y la espera '
         '<strong>dentro</strong> del <em>si la tecla flecha derecha está presionada</em>, junto '
         'al <em>mover</em>. Así el personaje camina mientras pulsas y se queda quieto cuando '
         'sueltas. Luego, con las cuatro flechas.')],

    7: [('Un personaje que sabe calcular',
         'Añade una cuarta pregunta, <strong>¿Cuántos años tienes?</strong>, y que responda '
         '«El año que viene tendrás …» con tu edad <strong>más uno</strong>. El bloque nuevo es '
         'el <strong>( ) + ( )</strong> verde, de Operadores: en un hueco va <em>respuesta</em> '
         'y en el otro un 1, y el resultado se mete dentro del <em>unir</em>.')],

    8: [('La media y el resto',
         'Añade la <strong>media</strong> de los dos números. Es (num1 + num2) / 2, así que hay '
         'que meter el bloque de sumar <em>dentro</em> del de dividir, como los <em>unir</em> '
         'dentro de <em>unir</em> de la sesión 7. Y otro operador que no has usado: '
         '<strong>( ) resto de ( )</strong> da lo que sobra al dividir. Prueba con 7 y 2 y '
         'comprueba que dice 1.')],

    9: [('Vidas',
         'Crea una variable <code>Vidas</code> que empiece en <strong>3</strong>. Cada fallo, '
         '<em>sumar a Vidas −1</em> (para restar se suma un número negativo). Y cambia el '
         '<em>repetir</em> por un <strong>repetir hasta que Vidas = 0</strong>: la partida se '
         'acaba cuando te quedas sin vidas, no a las diez preguntas. Esta pieza la vas a volver '
         'a usar en el proyecto final.')],

    10: [('El ganador dice cuánto ha tardado',
          'En Sensores hay un bloque redondo, <strong>cronómetro</strong>, que cuenta los segundos '
          'desde que arranca el programa. Pon <em>reiniciar cronómetro</em> al principio y haz '
          'que el que gana diga «He ganado en … segundos» uniendo el texto con el cronómetro. Lo '
          'vas a necesitar en la sesión 13.')],

    11: [('Un dominó de mensajes',
          'Que un mensaje provoque otro: el gato envía <em>patada</em>; la pelota, <em>al recibir '
          'patada</em>, hace lo suyo y al terminar envía un mensaje nuevo, <em>gol</em>; y un '
          'tercer objeto, <em>al recibir gol</em>, celebra. Tres objetos, dos mensajes, todo en '
          'cadena. La pantalla de inicio del proyecto final funciona exactamente así.')],

    12: [('Una moneda que desaparece',
          'Añade un objeto <strong>Moneda</strong> dentro del laberinto y una variable '
          '<code>Puntos</code>. Programa de la moneda: al arrancar, <strong>mostrar</strong>; y '
          'por siempre, si toca al jugador, <em>sumar a Puntos 1</em>, <strong>esconder</strong> '
          'y <em>detener (este programa)</em>, para que no siga sumando. Mostrar y esconder están '
          'en Apariencia; el detener es el de la sesión 4 con otra opción en el desplegable.')],

    13: [('El mejor tiempo, que no se borra',
          'Una variable <code>MejorTiempo</code> que guarde el tiempo más bajo de todas las '
          'partidas. Al llegar a la meta, antes del <em>detener todos</em>: si <em>cronómetro</em> '
          'es <strong>menor que</strong> <code>MejorTiempo</code>, dar a MejorTiempo el valor del '
          'cronómetro. Lo difícil: al arrancar <strong>no</strong> la pongas a 0, o la siguiente '
          'partida se olvida de la anterior. Para la primerísima vez, haz clic en un bloque '
          'suelto <em>dar a MejorTiempo el valor 999</em> (un clic ejecuta el bloque sin bandera) '
          'y luego tíralo a la paleta.')],

    14: [('Que la máquina enseñe lo que ha sacado',
          'Dibújale al personaje tres disfraces y llámalos exactamente <strong>piedra</strong>, '
          '<strong>papel</strong> y <strong>tijera</strong>. Después del sorteo, pon <em>cambiar '
          'disfraz a</em> con la variable <code>maquina</code> en el hueco: Scratch busca el '
          'disfraz que tenga ese nombre. Sin bloques nuevos.')],

    15: [('La pala con teclas',
          'Cambia el <em>ir a x: (posición x del ratón)</em> por lo de la sesión 5: si la tecla '
          '<strong>A</strong> está presionada, <em>cambiar x por −10</em>; si la '
          '<strong>D</strong>, <em>cambiar x por 10</em>. Cuando en la sesión 16 la pala cuente '
          'puntos, con esto tendrás la mitad de un Pong para dos.'),
         ('Dos pelotas',
          'Clic derecho sobre la pelota, <strong>duplicar</strong>, y a la copia cámbiale la '
          'dirección de salida (por ejemplo 200) y el tamaño. Ningún bloque nuevo, y el escenario '
          'cambia por completo.')],

    16: [('Una pelota que cambia con los puntos',
          'Cada vez que marcas, que la pelota cambie: en el condicional de la pala, junto al '
          '<em>sumar a Puntos 1</em>, pon <strong>cambiar efecto (color) por (25)</strong>, de '
          'Apariencia. ¿Y sólo cada 5 puntos? Con el operador <strong>( ) resto de ( )</strong>: '
          'cambia sólo si el resto de Puntos entre 5 es 0.')],

    17: [('Rompe tú un programa',
          'Coge un programa tuyo de otra sesión (el Pong vale) y métele <strong>un solo '
          'fallo</strong> de los cinco tipos de hoy, uno que se note al ejecutar. Guárdalo como '
          '<code>Roto_TuNombre.sb3</code> y pásaselo a otra pareja que haya terminado (si no hay '
          'ninguna, al profesor): tienen que encontrarlo con el método de hoy y decirte cuál era. '
          'Para romper algo a propósito hay que entenderlo mejor que para arreglarlo.')],
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

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

TITULO = '⭐ %s · Un paso más'   # %s: «Paso N», lo pone la plantilla; sin lista de pasos, «⭐ Último paso»

INTRO = ('Este paso es parte de la actividad, igual que los anteriores: hazlo en el mismo '
         'proyecto y entrégalo todo junto. Si te atascas, entrega lo que tengas y díselo al profesor.')

LOGRO = 'El último paso de la actividad también está hecho y va en el mismo archivo.'

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

    5: [('Dos jugadores en el mismo escenario',
         'Añade un <strong>segundo personaje</strong> y móntale el mismo programa, pero con las '
         'teclas <strong>W, A, S y D</strong> en vez de las flechas. No hay ningún bloque nuevo: '
         'es copiar y cambiar los desplegables. Truco: arrastra el programa entero hasta el '
         'icono del otro objeto, abajo a la derecha, y se copia solo.')],

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


def caja_ampliacion(num, etiqueta='Último paso'):
    """La caja de la sesión `num` con su etiqueta («Paso 6», «Último paso»), o '' si no tiene."""
    items = AMPLIACIONES.get(num)
    if not items:
        return ''
    li = ''.join('\n  <li><b>%s.</b> %s</li>' % (t, c) for t, c in items)
    titulo = (TITULO % etiqueta) if etiqueta.startswith('Paso') else '⭐ ' + etiqueta
    return ('<div class="sobra-tiempo">\n  <h3>%s</h3>\n  <p class="st-intro">%s</p>\n'
            '  <ul>%s\n  </ul>\n</div>' % (titulo, INTRO, li))

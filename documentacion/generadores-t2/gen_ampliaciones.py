# -*- coding: utf-8 -*-
"""Las 12 ampliaciones de T2 (formato ligero: idea, programa, reto, logros, entrega) y las
tres páginas que necesitan servo, que se conservan marcadas y sin bloques."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bloques import *                                  # noqa: F401,F403
from plantilla_t2 import (pagina, caja, caja_varios, placa, cat, bl, amplia,
                          pasos, secuencia, claves, pregunta, pista, ojo, logros, tabla)
from comun_t2 import escribir

TODO_ON = '#####:#####:#####:#####:#####'


def sale_de(reto, texto):
    return ('De dónde sale',
            '<p>Es la continuación de <a href="%s.html">%s</a>. %s</p>' % (reto[0], reto[1], texto))


def amp(arch, n, titulo, desc, consigue, origen, secciones, anterior=None, siguiente=None):
    return pagina(arch, 'Ampliación %d' % n, titulo, desc, consigue,
                  [sale_de(*origen)] + secciones, nivel='a',
                  anterior=anterior, siguiente=siguiente, nombre_hex='Ampliacion%d' % n)


# ============================================================ A1 · Dibujar el «1» LED a LED
UNO = [(2, 0), (1, 1), (2, 1), (2, 2), (2, 3), (1, 4), (2, 4), (3, 4)]
A1 = [
    BOTON('A', sum([[GRAFICAR(x, y), PAUSA(100)] for x, y in UNO], [])),
    BOTON('B', sum([[OCULTAR(x, y), PAUSA(100)] for x, y in reversed(UNO)], [])),
]
a01 = amp('a01', 1, 'Dibujar el «1» LED a LED',
    'Ampliación 1 de micro:bit: dibujar un número encendiendo LEDs por coordenadas con pausas, '
    'y borrarlo en orden inverso. CyR 1º ESO.',
    'que al pulsar A el número <strong>1</strong> aparezca LED a LED, como si alguien lo '
    'escribiera, y que B lo borre en el orden contrario.',
    (('r04', 'Reto 4 · Cada LED tiene su dirección'), 'Aquí no hay nada nuevo: son ocho '
     '<span class="bl">graficar</span> con una pausa entre cada uno. Lo que se entrena es '
     '<strong>planificar</strong> antes de programar.'),
    [
        ('El programa',
         placa('..#..:.##..:..#..:..#..:.###.', 'La matriz con el número 1 encendido',
               coords=True, pie='El 1 son ocho LEDs. Apunta sus coordenadas antes de tocar el editor.') +
         caja_varios([[A1[0]], [A1[1]]],
                     'Al presionarse el botón A: graficar los ocho LEDs del 1 con pausa 100 entre '
                     'cada uno. Al presionarse el botón B: ocultarlos en orden inverso') +
         '<p>Para borrar, el mismo orden al revés: el último que se encendió es el primero que '
         'se apaga.</p>'),
        ('Tu reto',
         pasos(['Dibuja en un papel la rejilla 5×5 y marca los LEDs del 1. Apunta sus '
                'coordenadas (x, y).',
                'Monta el evento de A. Un truco: haz un <span class="bl">graficar</span> con su '
                '<span class="bl">pausa</span>, y duplícalos con el botón derecho.',
                'Monta el de B en orden inverso.',
                'Otro número: el 2 o el 7. ¿Cuál tiene menos LEDs?',
                'Pásalo a la placa y entrégalo.'])),
        ('Lo has conseguido si…',
         logros(['El 1 aparece trazo a trazo con A y desaparece al revés con B.',
                 'Has planificado las coordenadas en papel antes de programar.'])),
    ], siguiente=('a02', 'Ampliación 2'))

# ============================================================ A2 · Termostato
SOL = '#.#.#:.###.:#####:.###.:#.#.#'
A2 = [SIEMPRE([SINO(compara(TEMPERATURA, '>', 26), [LEDS(SOL)], [NUMERO(TEMPERATURA)]), PAUSA(1000)])]
a02 = amp('a02', 2, 'El termostato',
    'Ampliación 2 de micro:bit: sensor de temperatura, mostrar número y un icono a partir de un '
    'umbral. Tramos de temperatura. CyR 1º ESO.',
    'que la placa enseñe la <strong>temperatura</strong> y, cuando pase de un umbral, un sol.',
    (('r05', 'Reto 5 · La luz que se enciende sola'), 'Es el mismo programa con otro sensor: '
     '<span class="bl">temperatura (°C)</span>, también en ' + cat('entrada', 'Entrada') + '.'),
    [
        ('El programa',
         caja(A2, 'Para siempre: si temperatura mayor que 26 entonces mostrar LEDs con un sol; si '
                  'no, mostrar número temperatura; pausa 1000') +
         ojo('La placa mide su propia temperatura',
             '<p>El sensor está dentro del chip, así que marca uno o dos grados más que el aire. '
             'Para probar el umbral, calienta la placa con la mano cerrada un minuto, o ponla '
             'cerca de la rejilla de un ordenador.</p>')),
        ('Tu reto',
         pasos(['Antes de nada, mide: <span class="bl">mostrar número temperatura</span> en un '
                '<span class="bl">para siempre</span>. Apunta el valor del aula.',
                'Pon de umbral dos grados más que eso y monta el programa.',
                'Tres tramos con <span class="bl">si no, si</span>: por debajo de 20, un copo '
                '(dibújalo con <span class="bl">mostrar LEDs</span>); entre 20 y 26, el número; '
                'por encima, el sol.',
                'Pásalo a la placa y entrégalo.'])),
        ('Lo has conseguido si…',
         logros(['Con la mano encima, sale el sol; sin ella, el número.',
                 'Tu umbral sale de haber medido.'])),
    ], anterior=('a01', 'Ampliación 1'), siguiente=('a03', 'Ampliación 3'))

# ============================================================ A3 · Brillo al revés
A3 = [SIEMPRE([BRILLO(opera(255, '-', LUZ)), LEDS(TODO_ON), PAUSA(100)])]
a03 = amp('a03', 3, 'Brillo al revés',
    'Ampliación 3 de micro:bit: ajustar brillo con una operación, 255 menos el nivel de luz. Sin '
    'condicionales. CyR 1º ESO.',
    'que los LEDs brillen <strong>más cuanta menos luz</strong> haya, sin ningún '
    '<span class="bl">si</span>: sólo una resta.',
    (('r05', 'Reto 5 · La luz que se enciende sola'), 'En el reto 5 la luz estaba encendida o '
     'apagada. Aquí hay grados: el brillo va de 0 a 255, igual que el sensor.'),
    [
        ('El programa',
         caja(A3, 'Para siempre: ajustar brillo a 255 menos nivel de luz; mostrar LEDs todos '
                  'encendidos; pausa 100') +
         claves([('ajustar brillo', 'está en LED › más. Un número de 0 (apagado) a 255 (máximo).'),
                 ('255 − nivel de luz', 'el bloque de restar de ' + cat('matematica', 'Matemática') +
                  ' con el sensor en el segundo hueco. Mucha luz (255) da brillo 0; oscuridad '
                  '(0) da brillo 255.')]) +
         ojo('Cuesta verlo',
             '<p>El sensor de luz son los propios LEDs, así que al brillar más se miden a sí '
             'mismos. Tápalo con la mano poco a poco y verás el cambio; con luz de aula el '
             'efecto es suave.</p>')),
        ('Tu reto',
         pasos(['Monta el programa y pruébalo tapando la placa.',
                'Al contrario: que brille más con más luz. Sin la resta.',
                'Pásalo a la placa y entrégalo.'])),
        ('Lo has conseguido si…',
         logros(['A oscuras brilla a tope y con luz casi se apaga.',
                 'Sabes explicar por qué 255 − luz le da la vuelta.'])),
    ], anterior=('a02', 'Ampliación 2'), siguiente=('a04', 'Ampliación 4'))

# ============================================================ A4 · Termómetro de barras
F1 = '.....:.....:.....:.....:#####'
F2 = '.....:.....:.....:#####:#####'
F3 = '.....:.....:#####:#####:#####'
F4 = '.....:#####:#####:#####:#####'
A4 = [SIEMPRE([
    FIJAR('grados', TEMPERATURA),
    CASCADA([(compara(var('grados'), '<', 20), [BORRAR]),
             (compara(var('grados'), '<', 22), [LEDS(F1)]),
             (compara(var('grados'), '<', 24), [LEDS(F2)]),
             (compara(var('grados'), '<', 26), [LEDS(F3)]),
             (compara(var('grados'), '<', 28), [LEDS(F4)])],
            sino=[LEDS(TODO_ON)]),
    PAUSA(1000)])]
a04 = amp('a04', 4, 'Termómetro de barras',
    'Ampliación 4 de micro:bit: cascada de si no, si con cinco tramos de temperatura, cada uno '
    'enciende más filas. CyR 1º ESO.',
    'un termómetro de <strong>barras</strong>: cuantos más grados, más filas encendidas, '
    'como el indicador de batería.',
    (('r05', 'Reto 5 · La luz que se enciende sola'), 'Y de la cascada del '
     '<a href="r12.html">reto 12</a>: aquí hay seis ramas.'),
    [
        ('El programa',
         caja(A4, 'Para siempre: fijar grados a temperatura; si grados < 20 borrar la pantalla; si '
                  'no, si < 22 una fila; si no, si < 24 dos filas; si no, si < 26 tres; si no, si '
                  '< 28 cuatro; si no, todas; pausa 1000') +
         '<p>Los tramos van de dos en dos grados desde 20. Los LEDs son rojos y sólo rojos: no '
         'hay forma de que las barras cambien de color, así que el «frío» es tener pocas filas.</p>'),
        ('Tu reto',
         pasos(['Mide primero la temperatura del aula y coloca los tramos alrededor de ella, si '
                'no siempre saldrán las mismas filas.',
                'Monta la cascada. Cada rama tiene su <span class="bl">mostrar LEDs</span> con '
                'las filas que toquen, contando desde abajo.',
                'Que A muestre el número exacto durante un segundo.',
                'Pásalo a la placa y entrégalo.'])),
        ('Lo has conseguido si…',
         logros(['Con la mano encima suben las filas; al quitarla, bajan.',
                 'Los tramos están pensados para tu aula, no copiados.'])),
    ], anterior=('a03', 'Ampliación 3'), siguiente=('a05', 'Ampliación 5'))

# ============================================================ A5 · La fila al revés
A5 = [SIEMPRE([
    FIJAR('x', 4),
    MIENTRAS(compara(var('x'), '≥', 0), [GRAFICAR(var('x'), 0), PAUSA(200), OCULTAR(var('x'), 0),
                                         CAMBIAR('x', -1)])])]
a05 = amp('a05', 5, 'La fila al revés: el bucle «mientras»',
    'Ampliación 5 de micro:bit: bucle mientras con contador descendente para recorrer la fila '
    'de derecha a izquierda. CyR 1º ESO.',
    'la fila del reto 9 pero <strong>de derecha a izquierda</strong>. El bucle '
    '<span class="bl">para</span> sólo cuenta hacia arriba; para bajar necesitas '
    '<span class="bl">mientras</span> y llevar tú la cuenta.',
    (('r09', 'Reto 9 · El bucle «para»'), 'Es la misma animación con otro bucle.'),
    [
        ('El programa',
         caja(A5, 'Para siempre: fijar x a 4; mientras x mayor o igual que 0 ejecutar: graficar x '
                  'x y 0, pausa 200, ocultar x x y 0, cambiar x por -1') +
         secuencia(['<strong>x</strong> empieza en 4, el LED de la derecha.',
                    '<strong>mientras x ≥ 0</strong>: se repite lo de dentro hasta que x baje de 0.',
                    'Enciende, espera, apaga, y <strong>cambiar x por -1</strong>: ahora vale 3.',
                    'Cuando x llega a −1, el mientras se acaba y el para siempre lo reinicia en 4.']) +
         ojo('Si se te olvida el cambiar x por -1',
             '<p>x se queda en 4 para siempre y el mismo LED parpadea sin fin: el bucle no '
             'termina nunca. En un <span class="bl">para</span> eso no puede pasar; en un '
             '<span class="bl">mientras</span>, es el error número uno.</p>')),
        ('Tu reto',
         pasos(['Monta el programa. El <span class="bl">≥</span> está en el desplegable del '
                'bloque de comparar.',
                'Ping-pong: primero un <span class="bl">para</span> de izquierda a derecha y '
                'después este <span class="bl">mientras</span> de vuelta, dentro del mismo '
                '<span class="bl">para siempre</span>.',
                'Pásalo a la placa y entrégalo.'])),
        ('Lo has conseguido si…',
         logros(['La luz va de derecha a izquierda.',
                 'El ping-pong va y vuelve sin saltos.',
                 'Sabes decir qué pasa si quitas el cambiar x por −1.'])),
    ], anterior=('a04', 'Ampliación 4'), siguiente=('a06', 'Ampliación 6'))

# ============================================================ A6 · Contar sombras
A6 = [
    INICIAR([FIJAR('coches', 0), FIJAR('tapado', FALSO), NUMERO(0)]),
    SIEMPRE([
        SI(Y(compara(LUZ, '<', 30), compara(var('tapado'), '=', FALSO)),
           [CAMBIAR('coches', 1), NUMERO(var('coches')), FIJAR('tapado', VERDADERO)]),
        SI(compara(LUZ, '>', 60), [FIJAR('tapado', FALSO)]),
        PAUSA(100)]),
    BOTON('B', [SI(compara(var('coches'), '>', 0), [CAMBIAR('coches', -1)]), NUMERO(var('coches'))]),
]
a06 = amp('a06', 6, 'El parking: contar sombras',
    'Ampliación 6 de micro:bit: contar cada vez que algo tapa el sensor de luz, una sola vez por '
    'sombra, con una variable de estado. CyR 1º ESO.',
    'un contador de coches para un parking: cada vez que algo <strong>pasa por encima</strong> '
    'del sensor, suma uno. Y sólo uno, aunque se quede parado encima.',
    (('r05', 'Reto 5 · La luz que se enciende sola'), 'Y del interruptor del '
     '<a href="r07.html">reto 7</a>: hace falta acordarse de si ya se ha contado esta sombra.'),
    [
        ('El programa',
         caja_varios([[A6[0]], [A6[1]], [A6[2]]],
                     'Al iniciar: coches a 0, tapado a falso. Para siempre: si nivel de luz < 30 y '
                     'tapado = falso, cambiar coches por 1, mostrar número coches, tapado a '
                     'verdadero; si nivel de luz > 60, tapado a falso; pausa 100. Botón B: resta '
                     'uno si hay coches') +
         secuencia(['Llega una sombra: la luz baja de 30 y <strong>tapado</strong> era falso. '
                    'Se cuenta un coche y se apunta que ya está tapado.',
                    'Mientras la sombra sigue, la luz sigue baja pero tapado es verdadero: no se '
                    'vuelve a contar. Eso es lo que evita contar el mismo coche diez veces.',
                    'La sombra se va: la luz sube de 60 y tapado vuelve a falso. Listo para el '
                    'siguiente.',
                    'Los dos umbrales son distintos a propósito (30 y 60): así una luz que '
                    'tiembla en el borde no cuenta coches fantasma.'])),
        ('Tu reto',
         pasos(['Mide tu luz con y sin la mano y coloca los dos umbrales entre medias, separados.',
                'Monta el programa. El <span class="bl">y</span> está en Lógica.',
                'Lleno: si coches llega a 10, <span class="bl">mostrar cadena</span> «LLENO» y '
                'que A no cuente más.',
                'Pásalo a la placa y entrégalo.'])),
        ('Lo has conseguido si…',
         logros(['Cada pasada de la mano suma exactamente uno.',
                 'Sabes explicar para qué sirve la variable tapado.'])),
    ], anterior=('a05', 'Ampliación 5'), siguiente=('a07', 'Ampliación 7'))

# ============================================================ A7 · Frío o caliente
A7 = [
    INICIAR([FIJAR('objetivo', azar(-60, 60))]),
    SIEMPRE([
        FIJAR('distancia', ABSOLUTO(opera(ROTACION('timbre'), '-', var('objetivo')))),
        CASCADA([(compara(var('distancia'), '<', 10), [ICONO('corazón')]),
                 (compara(var('distancia'), '<', 30), [ICONO('feliz')])],
                sino=[ICONO('triste')]),
        PAUSA(200)]),
    BOTON('A', [FIJAR('objetivo', azar(-60, 60))]),
]
a07 = amp('a07', 7, 'Frío o caliente',
    'Ampliación 7 de micro:bit: inclinación con rotación (°), valor absoluto de una diferencia, '
    'buscar un ángulo escondido. CyR 1º ESO.',
    'un juego de <strong>frío o caliente</strong>: la placa esconde una inclinación y tú la '
    'buscas inclinándola. Triste si estás lejos, feliz si te acercas, corazón si la clavas.',
    (('r11', 'Reto 11 · El dado'), 'El azar esconde el objetivo; el acelerómetro, que ya usaste '
     'para agitar, ahora mide cuánto <em>inclinas</em>.'),
    [
        ('El programa',
         caja_varios([[A7[0]], [A7[1]], [A7[2]]],
                     'Al iniciar: objetivo al azar entre -60 y 60. Para siempre: distancia = '
                     'absoluto de (rotación timbre − objetivo); si distancia < 10 corazón; si no, '
                     'si < 30 feliz; si no triste; pausa 200. Botón A: nuevo objetivo') +
         claves([('rotación (°) timbre', 'en Entrada › más. Cuánto está inclinada la placa '
                  'hacia delante o hacia atrás, de −180 a 180. «Timbre» es una mala traducción '
                  'de <em>pitch</em>; el otro valor, «girar», es la inclinación de lado.'),
                 ('absoluto de', 'en Matemática: quita el signo. La distancia entre tu ángulo y '
                  'el objetivo es la resta sin signo, da igual quién sea mayor.')])),
        ('Tu reto',
         pasos(['Monta el programa y juega: inclina despacio hasta el corazón.',
                'Que B te chive el objetivo con <span class="bl">mostrar número</span>.',
                'Más difícil: el objetivo también en «girar» (de lado), con dos distancias.',
                'Pásalo a la placa y entrégalo.'])),
        ('Lo has conseguido si…',
         logros(['Encuentras el ángulo escondido en menos de diez segundos.',
                 'Sabes explicar por qué hace falta el valor absoluto.'])),
    ], anterior=('a06', 'Ampliación 6'), siguiente=('a08', 'Ampliación 8'))

# ============================================================ A8 · Sonómetro
A8 = [SIEMPRE([
    FIJAR('ruido', SONIDO),
    CASCADA([(compara(var('ruido'), '<', 50), [LEDS(F1)]),
             (compara(var('ruido'), '<', 100), [LEDS(F2)]),
             (compara(var('ruido'), '<', 150), [LEDS(F3)]),
             (compara(var('ruido'), '<', 200), [LEDS(F4)])],
            sino=[LEDS(TODO_ON)]),
    PAUSA(200)])]
BARRAS8 = [SIEMPRE([('stack', 'led', ['trazar gráfico de barras', SONIDO, 'hasta', num(255)])])]
a08 = amp('a08', 8, 'El sonómetro de la clase',
    'Ampliación 8 de micro:bit V2: nivel de sonido del micrófono en barras, cascada de tramos y el '
    'bloque trazar gráfico de barras. CyR 1º ESO.',
    'un <strong>medidor de ruido</strong>: cuanto más jaleo en clase, más filas encendidas. El '
    'micrófono es de la micro:bit V2, la que tenéis.',
    (('r05', 'Reto 5 · La luz que se enciende sola'), 'Otro sensor que vale un número de 0 a 255: '
     '<span class="bl">nivel de sonido</span>. Y la cascada del termómetro de barras.'),
    [
        ('El programa',
         caja(A8, 'Para siempre: fijar ruido a nivel de sonido; si ruido < 50 una fila; si no, si '
                  '< 100 dos; si no, si < 150 tres; si no, si < 200 cuatro; si no, todas; pausa 200') +
         '<p>Y ahora la sorpresa: todo eso lo hace <strong>un solo bloque</strong> de LED › más:</p>' +
         caja(BARRAS8, 'Para siempre: trazar gráfico de barras nivel de sonido hasta 255', ancho=480,
              pie='«hasta 255» es el valor que llena la pantalla. Compara los dos programas: '
                  'hacen lo mismo.')),
        ('Tu reto',
         pasos(['Monta la cascada y pruébala hablando, gritando y en silencio.',
                'Sustitúyela por el bloque de gráfico de barras y comprueba que es lo mismo.',
                'Alerta: si el ruido pasa de 200, una X grande (<span class="bl">mostrar ícono no'
                '</span>) durante un segundo.',
                'Pásalo a la placa y entrégalo.'])),
        ('Lo has conseguido si…',
         logros(['Las barras suben con el ruido.',
                 'Sabes explicar qué hace «hasta 255» en el bloque de barras.'])),
    ], anterior=('a07', 'Ampliación 7'), siguiente=('a09', 'Ampliación 9'))

# ============================================================ A9 · Theremin
A9 = [
    INICIAR([FIJAR('tocando', FALSO)]),
    SIEMPRE([SINO(var('tocando'),
                  [TONO(INTERVALO(LUZ, 0, 255, 200, 2000))],
                  [PARAR_SONIDOS]),
             PAUSA(50)]),
    BOTON('A', [SINO(var('tocando'), [FIJAR('tocando', FALSO)], [FIJAR('tocando', VERDADERO)])]),
]
a09 = amp('a09', 9, 'El theremin: música con la mano',
    'Ampliación 9 de micro:bit V2: instrumento que cambia el tono según la luz, con tono de timbre '
    'y ajustar intervalo. Altavoz de la V2. CyR 1º ESO.',
    'un <strong>instrumento</strong> que se toca sin tocarlo: acercas la mano al sensor de luz y '
    'el sonido cambia de tono. El altavoz es el de la V2; no hace falta conectar nada.',
    (('r05', 'Reto 5 · La luz que se enciende sola'), 'Y del interruptor del '
     '<a href="r07.html">reto 7</a>, que aquí enciende y apaga el sonido.'),
    [
        ('El programa',
         caja_varios([[A9[0]], [A9[1]], [A9[2]]],
                     'Al iniciar: tocando a falso. Para siempre: si tocando, tono de timbre (Hz) '
                     'ajustar intervalo nivel de luz de 0 hasta 255 a intervalo de 200 hasta 2000; '
                     'si no, para todos los sonidos; pausa 50. Botón A: interruptor de tocando') +
         claves([('tono de timbre (Hz)', 'en ' + cat('musica', 'Música') + ': suena a la '
                  'frecuencia que le des, y sigue sonando hasta que lo pares.'),
                 ('ajustar intervalo', 'en Matemática. Traduce un número de un rango a otro: la '
                  'luz va de 0 a 255 y el tono lo queremos de 200 (grave) a 2000 (agudo). Es una '
                  'regla de tres hecha bloque.')])),
        ('Tu reto',
         pasos(['Monta el programa. Busca <span class="bl">ajustar intervalo</span> abajo del '
                'todo de Matemática.',
                'Toca: A para empezar, mueve la mano sobre la placa, A para parar.',
                'Que la pantalla enseñe barras con la luz, como en el sonómetro.',
                'Cambia el rango a 100–500: ¿más grave o más agudo?',
                'Pásalo a la placa y entrégalo.'])),
        ('Lo has conseguido si…',
         logros(['Acercar la mano cambia el tono de forma continua.',
                 'A enciende y apaga el sonido.',
                 'Sabes explicar qué traduce ajustar intervalo.'])),
    ], anterior=('a08', 'Ampliación 8'), siguiente=('a10', 'Ampliación 10'))

# ============================================================ A10 · Naves
A10 = [
    INICIAR([FIJAR('nave', SPRITE(2, 4)), FIJAR('enemigo', SPRITE(azar(0, 4), 0)), FIJAR('disparando', FALSO)]),
    BOTON('A', [SP_CAMBIAR('nave', 'x', -1)]),
    BOTON('B', [SP_CAMBIAR('nave', 'x', 1)]),
    BOTON('A+B', [SI(compara(var('disparando'), '=', FALSO),
                     [FIJAR('bala', SPRITE(SP_PROP('nave', 'x'), 3)), FIJAR('disparando', VERDADERO)])]),
    SIEMPRE([
        PAUSA(300),
        SI(var('disparando'), [
            SP_CAMBIAR('bala', 'y', -1),
            SI(SP_TOCA('bala', 'enemigo'), [
                PUNTOS(1), SP_ELIMINAR('enemigo'), SP_ELIMINAR('bala'), FIJAR('disparando', FALSO),
                FIJAR('enemigo', SPRITE(azar(0, 4), 0))]),
            SI(compara(SP_PROP('bala', 'y'), '=', 0), [SP_ELIMINAR('bala'), FIJAR('disparando', FALSO)])]),
        SP_CAMBIAR('enemigo', 'y', 1),
        SI(SP_TOCA('enemigo', 'nave'), [FIN_JUEGO]),
        SI(compara(SP_PROP('enemigo', 'y'), '=', 4), [SP_ELIMINAR('enemigo'), FIJAR('enemigo', SPRITE(azar(0, 4), 0))]),
    ]),
]
a10 = amp('a10', 10, 'Naves: dispara con A+B',
    'Ampliación 10 de micro:bit: juego de disparos con tres sprites, bala que sube, enemigo que '
    'baja, puntuación y fin del juego. CyR 1º ESO.',
    'el juego del reto 15 con <strong>disparo</strong>: A+B lanza una bala que sube; si alcanza '
    'al enemigo, punto y enemigo nuevo. Si el enemigo te toca, fin.',
    (('r15', 'Reto 15 · Esquiva enemigos'), 'Un sprite más, la bala, y una variable que dice si '
     'está en el aire. Es el programa más largo del trimestre: léelo dos veces antes de montarlo.'),
    [
        ('El programa',
         caja_varios([[A10[0]], [A10[1]], [A10[2]], [A10[3]], [A10[4]]],
                     'Al iniciar: nave en 2,4; enemigo arriba al azar; disparando a falso. A y B '
                     'mueven la nave. A+B: si no está disparando, crear la bala encima de la nave '
                     'y disparando a verdadero. Para siempre: pausa 300; si disparando, la bala '
                     'sube una fila, si toca al enemigo punto y ambos se eliminan, si llega a y=0 '
                     'se elimina; el enemigo baja una fila; si toca la nave, fin del juego; si llega a la '
                     'fila 4 sin tocarla, se elimina y nace otro arriba') +
         secuencia(['Sólo puede haber <strong>una bala</strong> en el aire: por eso A+B pregunta '
                    'antes por <strong>disparando</strong>.',
                    'La bala nace en la fila 3, justo encima de la nave, en la misma columna: '
                    '<span class="bl">nave x</span>.',
                    'Cada vuelta la bala sube. Si toca al enemigo: punto, desaparecen los dos y '
                    'nace otro enemigo. Si llega arriba sin tocar nada, desaparece sin más.',
                    'Después mueve el enemigo, y si te toca, se acabó. Si llega abajo sin tocarte, '
                    'se escapa: desaparece y nace otro, pero ese no da punto.'])),
        ('Tu reto',
         pasos(['Crea las variables nave, enemigo, bala y disparando. Monta primero A, B y el '
                'movimiento del enemigo; cuando funcione, añade el disparo.',
                'Que el enemigo baje sólo una de cada dos vueltas (una variable que cuenta '
                'vueltas), para que la bala sea más rápida que él.',
                'Cuenta atrás de 30 segundos con <span class="bl">iniciar cuenta regresiva</span>: '
                'a ver cuántos puntos haces.',
                'Pásalo a la placa y entrégalo.'])),
        ('Lo has conseguido si…',
         logros(['A+B dispara, la bala sube y los enemigos caen cuando les das.',
                 'No se puede disparar dos balas a la vez.',
                 'Sabes explicar para qué sirve la variable disparando.'])),
    ], anterior=('a09', 'Ampliación 9'), siguiente=('a11', 'Ampliación 11'))

# ============================================================ A11 · Varios enemigos
A11 = [
    INICIAR([FIJAR('jugador', SPRITE(2, 4)), FIJAR('e1', SPRITE(azar(0, 4), 0)),
             FIJAR('e2', SPRITE(azar(0, 4), 0)), FIJAR('espera', 500)]),
    BOTON('A', [SP_CAMBIAR('jugador', 'x', -1)]),
    BOTON('B', [SP_CAMBIAR('jugador', 'x', 1)]),
    SIEMPRE([
        PAUSA(var('espera')),
        SP_CAMBIAR('e1', 'y', 1),
        SI(compara(azar(1, 2), '=', 1), [SP_CAMBIAR('e2', 'y', 1)]),
        SI(O(SP_TOCA('e1', 'jugador'), SP_TOCA('e2', 'jugador')), [FIN_JUEGO]),
        SI(compara(SP_PROP('e1', 'y'), '=', 4), [PUNTOS(1), SP_ELIMINAR('e1'), FIJAR('e1', SPRITE(azar(0, 4), 0))]),
        SI(compara(SP_PROP('e2', 'y'), '=', 4), [PUNTOS(1), SP_ELIMINAR('e2'), FIJAR('e2', SPRITE(azar(0, 4), 0))]),
        SI(compara(var('espera'), '>', 150), [CAMBIAR('espera', -10)]),
    ]),
]
a11 = amp('a11', 11, 'Dos enemigos a la vez',
    'Ampliación 11 de micro:bit: dos sprites enemigos que caen a ritmos distintos, dificultad que '
    'crece, sin listas. CyR 1º ESO.',
    'el esquiva enemigos con <strong>dos</strong> cayendo a la vez, uno más lento que otro, y '
    'cada vez más rápido. Sin listas ni nada raro: dos sprites son dos variables.',
    (('r15', 'Reto 15 · Esquiva enemigos'), 'Cada enemigo es una copia de lo que ya tenías. La '
     'gracia está en que el segundo sólo baja la mitad de las veces.'),
    [
        ('El programa',
         caja_varios([[A11[0]], [A11[1]], [A11[2]], [A11[3]]],
                     'Al iniciar: jugador, e1 y e2 como sprites, espera a 500. A y B mueven al '
                     'jugador. Para siempre: pausa espera; e1 baja; e2 baja sólo si un azar de 1 a 2 '
                     'sale 1; si alguno toca al jugador, fin; cada uno que llega a la fila 4 da un '
                     'punto y renace; si espera > 150, espera baja 10') +
         claves([('e2 baja a medias', 'un azar de 1 a 2 decide en cada vuelta si e2 se mueve: de '
                  'media, la mitad de las veces. Dos enemigos a distinta velocidad sin dos bucles.'),
                 ('espera', 'la pausa ya no es un número fijo sino una variable que baja 10 ms '
                  'por vuelta hasta 150. El juego se acelera solo.')])),
        ('Tu reto',
         pasos(['Parte del reto 15 y añade e2 copiando cada bloque de e1.',
                'Un tercer enemigo, e3, que sólo baje una de cada tres vueltas (azar de 1 a 3).',
                'Que los enemigos parpadeen y el jugador no, para distinguirlos.',
                'Pásalo a la placa y entrégalo.'])),
        ('Lo has conseguido si…',
         logros(['Caen dos enemigos a distinto ritmo y el juego se acelera.',
                 'Sabes explicar el truco del azar para que e2 vaya más lento.'])),
    ], anterior=('a10', 'Ampliación 10'), siguiente=('a12', 'Ampliación 12'))

# ============================================================ A12 · Dos jugadores por radio
A12 = [
    INICIAR([GRUPO(7), FIJAR('yo', SPRITE(2, 2)), FIJAR('otro', SPRITE(0, 2)),
             SP_CAMBIAR('otro', 'parpadear', 200)]),
    BOTON('A', [SP_CAMBIAR('yo', 'x', -1), ENVIAR_VALOR('x', SP_PROP('yo', 'x'))]),
    BOTON('B', [SP_CAMBIAR('yo', 'x', 1), ENVIAR_VALOR('x', SP_PROP('yo', 'x'))]),
    RECIBIR_VALOR([SP_FIJAR('otro', 'x', var('value'))]),
    SIEMPRE([SI(SP_TOCA('yo', 'otro'), [ICONO('corazón'), PAUSA(500)]), PAUSA(100)]),
]
a12 = amp('a12', 12, 'Dos jugadores por radio',
    'Ampliación 12 de micro:bit: dos placas, cada una mueve su sprite y envía su posición por '
    'radio con enviar valor; cuando coinciden, corazón. CyR 1º ESO.',
    'un juego para <strong>dos placas</strong>: cada uno mueve su punto y ve el del otro '
    'parpadeando; cuando los dos coinciden, corazón en las dos pantallas.',
    (('r13', 'Reto 13 · Radio'), 'Y de los sprites del <a href="r15.html">reto 15</a>. En vez de '
     'un número suelto se envía un <strong>valor con nombre</strong>, «x».'),
    [
        ('El programa',
         caja_varios([[A12[0]], [A12[1]], [A12[2]], [A12[3]], [A12[4]]],
                     'Al iniciar: grupo 7; yo en 2,2; otro en 0,2 parpadeando. A y B mueven yo y '
                     'envían por radio el valor x = yo x. Al recibir radio name value: otro '
                     'establecer x en value. Para siempre: si yo toca a otro, corazón medio segundo') +
         claves([('radio enviar valor «x» = …', 'manda un nombre y un número juntos. Al recibir, '
                  'el nombre llega en <span class="bl">name</span> y el número en '
                  '<span class="bl">value</span>. Así, cuando haya más cosas que enviar, se '
                  'distinguen por el nombre.'),
                 ('otro parpadear 200', 'el punto del otro jugador parpadea para que sepas cuál es '
                  'el tuyo. Las dos placas llevan el mismo programa.')])),
        ('Tu reto',
         pasos(['Con otra pareja: mismo programa, mismo grupo, un número que no use nadie más.',
                'Moveos hasta coincidir: corazón en las dos.',
                'Movimiento vertical también: A+B cambia entre mover en x y mover en y (una '
                'variable de modo), y se envían dos valores, «x» e «y».',
                'Pásalo a la placa y entrégalo.'])),
        ('Lo has conseguido si…',
         logros(['Cada placa ve el punto de la otra moverse en tiempo real.',
                 'Al coincidir, las dos muestran el corazón.',
                 'Sabes explicar la diferencia entre enviar número y enviar valor.'])),
    ], anterior=('a11', 'Ampliación 11'))

# ============================================================ M1–M3 · Requieren servo
SERVO_AVISO = ojo('Este reto necesita un servomotor',
                  '<p>El instituto no tiene servos ni pinzas para conectarlos, así que este reto '
                  '<strong>no se hace este curso</strong>. Se conserva por si algún año hay '
                  'material. Si lo tienes en casa, adelante: el cable marrón o negro va a GND, '
                  'el rojo a 3V y el naranja o amarillo al pin P0, con pinzas de cocodrilo.</p>')


def servo(arch, n, titulo, desc, consigue, pseudo, anterior=None, siguiente=None):
    return pagina(arch, 'Sin material %d' % n, titulo, desc, consigue,
                  [(None, SERVO_AVISO),
                   ('El programa, en palabras',
                    '<p>Los bloques del servo están en <strong>Avanzado › Pines</strong> '
                    '(«servo escribir pin P0 a 90»). Como no se puede probar en clase, va en '
                    'pseudocódigo:</p>' + secuencia(pseudo))],
                  nivel='m', abrir=False, anterior=anterior, siguiente=siguiente,
                  entrega='<p>No hay entrega: sin servo no se puede hacer.</p>')


m01 = servo('m01', 1, 'Control de un servomotor',
    'Reto de micro:bit que requiere servomotor: A lo mueve a 0°, B a 180°, A+B a 90°. CyR 1º ESO.',
    'mover un servomotor a tres posiciones con los botones. <strong>Requiere servo.</strong>',
    ['al iniciar: servo en P0 a 90° (centro).',
     'al presionarse el botón A: servo en P0 a 0°, mostrar número 0.',
     'al presionarse el botón B: servo en P0 a 180°, mostrar número 180.',
     'al presionarse A+B: servo en P0 a 90°, mostrar número 90.'],
    siguiente=('m02', 'Sin material 2'))
m02 = servo('m02', 2, 'La barrera de parking',
    'Reto de micro:bit que requiere servomotor: barrera que abre con A y cierra con B, con estado. '
    'CyR 1º ESO.',
    'una barrera que abre con A (servo a 90°) y cierra con B (servo a 0°), con flecha arriba o '
    'abajo según el estado. <strong>Requiere servo.</strong>',
    ['al iniciar: servo a 0°, abierta a falso, mostrar flecha Sur.',
     'al presionarse A: si no está abierta, servo a 90°, abierta a verdadero, flecha Norte.',
     'al presionarse B: si está abierta, servo a 0°, abierta a falso, flecha Sur.'],
    anterior=('m01', 'Sin material 1'), siguiente=('m03', 'Sin material 3'))
m03 = servo('m03', 3, 'La barrera automática con sensor de luz',
    'Reto de micro:bit que requiere servomotor: la barrera abre sola cuando una sombra tapa el '
    'sensor de luz. CyR 1º ESO.',
    'la barrera del reto anterior, pero automática: se abre cuando algo tapa el sensor de luz y se '
    'cierra cuando vuelve la luz. <strong>Requiere servo.</strong>',
    ['al iniciar: servo a 0° (cerrada).',
     'para siempre: si nivel de luz < 50, servo a 90° y flecha Norte; si no, servo a 0° y flecha '
     'Sur; pausa 500.'],
    anterior=('m02', 'Sin material 2'))


if __name__ == '__main__':
    for n, h in [('a01', a01), ('a02', a02), ('a03', a03), ('a04', a04), ('a05', a05), ('a06', a06),
                 ('a07', a07), ('a08', a08), ('a09', a09), ('a10', a10), ('a11', a11), ('a12', a12),
                 ('m01', m01), ('m02', m02), ('m03', m03)]:
        escribir(n, h)

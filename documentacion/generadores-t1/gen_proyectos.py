# -*- coding: utf-8 -*-
"""Las tres bases del proyecto final de T1 · Scratch.

No son juegos sueltos: son los tres puntos de partida entre los que elige el
alumnado en la S17. Todo lo que hay aquí se monta con bloques que ya se han
enseñado en S01-S16 y con las ocho piezas del kit de la S18. No entra ni un
bloque nuevo, y ninguno de extensión.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scratchsvg import op, var, rep, hexa, tecla
from plantilla import (pagina_juego, caja, dos_cajas, pasos, pregunta, pista,
                       ojo, logros, tabla)
from comun import escribir_juego

BANDERA = ('hat', 'events', ['al hacer clic en', ('icon', 'bandera')])
POSX = rep('motion', 'posición x')
POSY = rep('motion', 'posición y')
RATONX = rep('sensing', 'posición x del ratón')


def si(cond, hijos):
    return ('c', 'control', ['si', cond, 'entonces'], hijos)


def tocando(quien):
    return hexa('sensing', '¿tocando', ('drop', quien), '?')


def azar(a, b):
    return op('número aleatorio entre', ('num', a), 'y', ('num', b))


AVISO_GUIA = ('Consulta. Está hecha con Scratch 2: varios bloques no se llaman así')

REUTILIZA = ('<p>Nada de esto es nuevo. Cada pieza sale de una sesión que ya has hecho, '
             'y por eso este juego se puede montar en tres sesiones:</p>')

OJO_DUPLICAR = (
    '<p>Cuando duplicas un objeto, <strong>se copia también su código</strong>. Eso es lo '
    'bueno: no tienes que escribirlo otra vez. Y es lo malo: todas las copias nacen con las '
    '<strong>mismas coordenadas</strong> y se colocan una encima de otra.</p>'
    '<p style="margin-bottom:0">Después de duplicar hay que entrar en cada copia y cambiarle '
    'su <em>ir a x: y:</em>. Es el trabajo más aburrido del juego y el que más se olvida.</p>')


# ============================================================ A · ARKANOID
A_PELOTA = [
    BANDERA,
    ('stack', 'looks', ['fijar tamaño al', ('num', '50'), '%']),
    ('stack', 'variables', ['dar a', ('drop', 'Puntos'), 'el valor', ('num', '0')]),
    ('stack', 'motion', ['ir a x:', ('num', '0'), 'y:', ('num', '-100')]),
    ('stack', 'motion', ['apuntar en dirección', ('num', '45')]),
    ('c', 'control', ['por siempre'], [
        ('stack', 'motion', ['mover', ('num', '8'), 'pasos']),
        ('stack', 'motion', ['si toca un borde, rebotar']),
        si(tocando('Pala'), [
            ('stack', 'sound', ['iniciar sonido', ('drop', 'Pop')]),
            ('stack', 'motion', ['apuntar en dirección', azar('-45', '45')]),
            ('stack', 'motion', ['mover', ('num', '20'), 'pasos'])]),
        si(hexa('operators', POSY, '<', ('num', '-155')), [
            ('stack', 'looks', ['decir', op('unir', ('txt', 'Fin. Puntos: '), var('Puntos')),
                                'durante', ('num', '3'), 'segundos']),
            ('cap', 'control', ['detener', ('drop', 'todos')])]),
    ]),
]
A_REBOTE = [
    ('hat', 'events', ['al recibir', ('drop', 'ladrillo roto')]),
    ('stack', 'motion', ['girar', ('icon', 'giro-d'), azar('150', '210'), 'grados']),
    ('stack', 'motion', ['mover', ('num', '20'), 'pasos']),
]
A_GANAR = [
    BANDERA,
    ('stack', 'control', ['esperar hasta que',
                          hexa('operators', var('Puntos'), '=', ('num', '10'))]),
    ('stack', 'looks', ['decir', ('txt', '¡Has ganado!'), 'durante', ('num', '3'), 'segundos']),
    ('cap', 'control', ['detener', ('drop', 'todos')]),
]
A_PALA = [
    BANDERA,
    ('stack', 'motion', ['fijar estilo de rotación a', ('drop', 'no rotar')]),
    ('c', 'control', ['por siempre'], [
        ('stack', 'motion', ['ir a x:', RATONX, 'y:', ('num', '-140')]),
    ]),
]
A_LADRILLO = [
    BANDERA,
    ('stack', 'motion', ['ir a x:', ('num', '-160'), 'y:', ('num', '120')]),
    ('stack', 'looks', ['mostrar']),
    ('c', 'control', ['por siempre'], [
        si(tocando('Pelota'), [
            ('stack', 'sound', ['iniciar sonido', ('drop', 'Pop')]),
            ('stack', 'variables', ['sumar a', ('drop', 'Puntos'), ('num', '1')]),
            ('stack', 'looks', ['esconder']),
            ('stack', 'events', ['enviar', ('drop', 'ladrillo roto')])]),
    ]),
]

arkanoid = pagina_juego(
    'arkanoid', 'Arkanoid', 'A',
    'Arkanoid en Scratch 3: la base del proyecto final. Rompe los ladrillos con la pelota del '
    'Pong. CyR 1º ESO.',
    'romper todos los ladrillos con una pelota que no puedes dejar caer. Es tu Pong, pero con '
    'algo a lo que apuntar.',
    [
        ('Ya tienes medio juego hecho',
         '<p>Si hiciste el Pong de las sesiones 15 y 16, <strong>abre aquel <code>.sb3</code> y '
         'sigue desde ahí</strong>. La pelota y la pala son las mismas; lo único que añades hoy '
         'son los ladrillos.</p>' + REUTILIZA +
         tabla(['Pieza', 'De dónde sale'], [
             ['La pelota que rebota por la pantalla', 'S15'],
             ['La pala que sigue al ratón', 'S15'],
             ['Sumar un punto al tocar, y despegarse', 'S16'],
             ['Perder cuando se te escapa por abajo', 'S16'],
             ['El ladrillo que se esconde al tocarlo', 'Pieza 8 de la S18'],
             ['El aviso <em>ladrillo roto</em> entre objetos', 'S11'],
             ['Poner el marcador a 0 al arrancar', 'Pieza 2 de la S18'],
         ])),

        ('Los tres objetos',
         '<p>Necesitas <strong>Pelota</strong>, <strong>Pala</strong> y <strong>Ladrillo</strong>. '
         'La pala la dibujas tú: un rectángulo alargado.</p>'
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">Pelota</h3>'
         + caja(A_PELOTA, 'Programa de la pelota: colocarse arriba de la pala apuntando en '
                          'dirección 45 y, por siempre, mover 8 pasos, rebotar en los bordes, '
                          'rebotar hacia arriba al tocar la pala, y terminar la partida si baja '
                          'de menos 155',
                pie='Es el programa del Pong, tal cual. Lo único distinto es que la pelota sale '
                    'apuntando hacia arriba, hacia los ladrillos.') +
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">Pelota · dos programas más</h3>'
         + dos_cajas(('Al romper un ladrillo', A_REBOTE,
                      'Al recibir el mensaje ladrillo roto, girar un número aleatorio de grados '
                      'entre 150 y 210 y mover 20 pasos'),
                     ('Al romperlos todos', A_GANAR,
                      'Al hacer clic en la bandera, esperar hasta que Puntos sea 10, decir ¡Has '
                      'ganado! durante 3 segundos y detener todos')) +
         '<p><strong>Girar unos 180 grados es darse la vuelta.</strong> Al ponerle un número al '
         'azar entre 150 y 210, la pelota rebota hacia atrás pero nunca exactamente igual, y el '
         'juego deja de ser predecible.</p>'
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">Pala</h3>'
         + caja(A_PALA, 'Programa de la pala: fijar estilo de rotación a no rotar y, por siempre, '
                        'ir a la posición x del ratón manteniendo la y en menos 140',
                ancho=470) +
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">Ladrillo</h3>'
         + caja(A_LADRILLO, 'Programa del ladrillo: colocarse, mostrarse y, por siempre, si está '
                            'tocando la pelota iniciar sonido Pop, sumar 1 a Puntos, esconderse y '
                            'enviar el mensaje ladrillo roto',
                pie='Fíjate en que el ladrillo <strong>no</strong> mueve la pelota: sólo avisa. '
                    'Quien cambia de dirección es ella, con su <em>al recibir</em>.') +
         '<p>Cuando el primero funcione, <strong>duplícalo</strong> con el botón derecho hasta '
         'tener diez, y cámbiale a cada uno las coordenadas. Dos filas de cinco quedan bien: '
         '<code>x</code> en −160, −80, 0, 80 y 160; <code>y</code> en 120 y 80.</p>'),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Duplicas el ladrillo hasta tener diez. Al probarlo, <strong>los diez '
                       'desaparecen a la vez</strong> en cuanto la pelota toca uno. ¿Por qué?',
                  [('suma', 'Porque sumar a (Puntos) (1) suma diez de golpe',
                    'No. Cada ladrillo suma el suyo. El problema es que los diez se tocan a la '
                    'vez, y por eso los diez suman a la vez.'),
                   ('coord', 'Porque las diez copias tienen las mismas coordenadas y están una '
                    'encima de otra',
                    'Correcto. Duplicar copia también el código, <em>incluido el ir a x: y:</em>. '
                    'Hasta que no entres en cada copia y le cambies las coordenadas, los diez '
                    'ladrillos son el mismo sitio de la pantalla.'),
                   ('mensaje', 'Porque el mensaje ladrillo roto lo reciben todos los ladrillos',
                    'El mensaje sí lo recibe todo el mundo, pero al ladrillo no lo esconde el '
                    'mensaje: lo esconde su propio bloque <em>esconder</em>.')],
                  'coord') +
         ojo('El fallo de duplicar', OJO_DUPLICAR)),

        ('Tu versión',
         '<p>Hasta aquí es el juego de todos. <strong>A partir de aquí es el tuyo.</strong> '
         'Elige de esta lista o inventa, pero apúntalo en la ficha de la '
         '<a href="../sesiones/s17.html">sesión 17</a> antes de empezar:</p>' +
         tabla(['Idea', 'Qué tienes que tocar'], [
             ['Más ladrillos, o más filas',
              'Duplicar y cambiar coordenadas. <strong>Y el 10</strong> del <em>esperar hasta que</em>'],
             ['Ladrillos de colores que valen distinto',
              'Un disfraz por color y otro número en el <em>sumar a (Puntos)</em>'],
             ['Tres vidas en vez de perder a la primera',
              'Variable <code>Vidas</code>, <em>sumar a (Vidas) (−1)</em> y volver al centro'],
             ['Un ladrillo especial que agranda la pala',
              'Que envíe otro mensaje, y la pala con <em>fijar tamaño al (…) %</em>'],
             ['Segundo nivel al romperlos todos',
              '<em>cambiar fondo a</em> y un <em>al recibir</em> que vuelva a mostrar los ladrillos'],
             ['Que no sean ladrillos: globos, ventanas, marcianos…',
              'Sólo los disfraces. El código es el mismo'],
         ])),

        ('Lo has conseguido si…',
         logros(['La pelota rebota en la pala y no la atraviesa.',
                 'Los ladrillos desaparecen <strong>de uno en uno</strong>, no todos a la vez.',
                 'El marcador sube exactamente uno por ladrillo.',
                 'Al escapársete la pelota, la partida termina y dice la puntuación.',
                 'Al romper el último ladrillo, dice que has ganado.',
                 'Tres partidas seguidas empiezan exactamente igual.',
                 'Tiene algo tuyo que no está en esta página.'])),
    ],
    guia='ejercicio-de-arkanoid.pdf', guia_nota=AVISO_GUIA)
escribir_juego('arkanoid', arkanoid)


# ============================================================ B · SPACE INVADERS
B_NAVE = [
    BANDERA,
    ('stack', 'looks', ['fijar tamaño al', ('num', '50'), '%']),
    ('stack', 'variables', ['dar a', ('drop', 'Puntos'), 'el valor', ('num', '0')]),
    ('stack', 'motion', ['ir a x:', ('num', '0'), 'y:', ('num', '-150')]),
    ('c', 'control', ['por siempre'], [
        si(tecla('flecha derecha'), [('stack', 'motion', ['cambiar x por', ('num', '5')])]),
        si(tecla('flecha izquierda'), [('stack', 'motion', ['cambiar x por', ('num', '-5')])]),
        ('stack', 'variables', ['dar a', ('drop', 'NaveX'), 'el valor', POSX]),
        si(tecla('espacio'), [
            ('stack', 'events', ['enviar', ('drop', 'disparo')]),
            ('stack', 'control', ['esperar', ('num', '0.4'), 'segundos'])]),
    ]),
]
B_RELOJ = [
    BANDERA,
    ('stack', 'variables', ['dar a', ('drop', 'Tiempo'), 'el valor', ('num', '60')]),
    ('c', 'control', ['repetir hasta que',
                      hexa('operators', var('Tiempo'), '=', ('num', '0'))], [
        ('stack', 'control', ['esperar', ('num', '1'), 'segundos']),
        ('stack', 'variables', ['sumar a', ('drop', 'Tiempo'), ('num', '-1')]),
    ]),
    ('stack', 'looks', ['decir', ('txt', 'Se acabó el tiempo'), 'durante', ('num', '3'),
                        'segundos']),
    ('cap', 'control', ['detener', ('drop', 'todos')]),
]
B_GANAR = [
    BANDERA,
    ('stack', 'control', ['esperar hasta que',
                          hexa('operators', var('Puntos'), '=', ('num', '8'))]),
    ('stack', 'looks', ['decir', ('txt', '¡Los has echado a todos!'), 'durante', ('num', '3'),
                        'segundos']),
    ('cap', 'control', ['detener', ('drop', 'todos')]),
]
B_BALA_INI = [
    BANDERA,
    ('stack', 'looks', ['esconder']),
]
B_BALA = [
    ('hat', 'events', ['al recibir', ('drop', 'disparo')]),
    ('stack', 'motion', ['ir a x:', var('NaveX'), 'y:', ('num', '-130')]),
    ('stack', 'looks', ['mostrar']),
    ('c', 'control', ['repetir hasta que',
                      hexa('operators', POSY, '>', ('num', '160'))], [
        ('stack', 'motion', ['cambiar y por', ('num', '12')]),
    ]),
    ('stack', 'looks', ['esconder']),
]
B_MARCIANO = [
    BANDERA,
    ('stack', 'looks', ['fijar tamaño al', ('num', '60'), '%']),
    ('stack', 'motion', ['ir a x:', ('num', '-150'), 'y:', ('num', '120')]),
    ('stack', 'looks', ['mostrar']),
    ('c', 'control', ['por siempre'], [
        si(tocando('Bala'), [
            ('stack', 'sound', ['iniciar sonido', ('drop', 'Pop')]),
            ('stack', 'variables', ['sumar a', ('drop', 'Puntos'), ('num', '1')]),
            ('stack', 'looks', ['esconder'])]),
    ]),
]
B_VAIVEN = [
    BANDERA,
    ('c', 'control', ['por siempre'], [
        ('c', 'control', ['repetir', ('num', '40')],
         [('stack', 'motion', ['cambiar x por', ('num', '3')])]),
        ('c', 'control', ['repetir', ('num', '40')],
         [('stack', 'motion', ['cambiar x por', ('num', '-3')])]),
    ]),
]

space = pagina_juego(
    'space-invaders', 'Space Invaders', 'B',
    'Space Invaders en Scratch 3: la opción más ambiciosa del proyecto final. Nave, bala y una '
    'fila de marcianos, sin clones. CyR 1º ESO.',
    'una nave que dispara y una fila de marcianos que se te escapa de un lado a otro. Tienes un '
    'minuto para echarlos a todos.',
    [
        ('La idea, y la pieza nueva',
         '<p>Es el más ambicioso de los tres, pero no por los bloques: son los mismos de siempre. '
         'Lo que tiene de más son <strong>objetos</strong>: nave, bala y marciano.</p>'
         '<p>Y trae una idea que no has usado todavía, aunque sepas hacerla: <strong>una variable '
         'como recado entre dos objetos</strong>. La bala tiene que salir de donde esté la nave, '
         'pero un objeto no puede mirar dónde está otro. Así que la nave va apuntando su posición '
         'en una variable, <code>NaveX</code>, y la bala la lee cuando sale.</p>' + REUTILIZA +
         tabla(['Pieza', 'De dónde sale'], [
             ['Moverse con las flechas', 'S05 · Pieza 1 de la S18'],
             ['Avisar con un mensaje de que has disparado', 'S11'],
             ['Guardar un dato en una variable para usarlo luego', 'S08'],
             ['Subir la bala hasta arriba', 'S12 · <em>cambiar y por</em>'],
             ['El marciano que se esconde al tocarlo', 'Pieza 8 de la S18'],
             ['La cuenta atrás', 'Pieza 5 de la S18'],
             ['El vaivén de la fila', 'S03 · <em>repetir</em>'],
         ])),

        ('Los tres objetos',
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">Nave · moverse y disparar</h3>'
         + caja(B_NAVE, 'Programa de la nave: colocarse abajo con el marcador a 0 y, por siempre, '
                        'moverse con las flechas, guardar su posición x en la variable NaveX y, si '
                        'se pulsa espacio, enviar el mensaje disparo y esperar 0.4 segundos',
                pie='La <strong>espera de 0.4 segundos</strong> es lo que impide disparar cien '
                    'veces por segundo. Súbela o bájala hasta que el juego te guste.') +
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">Nave · el reloj y la victoria</h3>'
         + dos_cajas(('Se acaba el tiempo', B_RELOJ,
                      'Al hacer clic en la bandera, poner Tiempo a 60 y repetir hasta que sea 0 '
                      'esperando un segundo y restando uno; después decir Se acabó el tiempo y '
                      'detener todos'),
                     ('Los has echado a todos', B_GANAR,
                      'Al hacer clic en la bandera, esperar hasta que Puntos sea 8, decir ¡Los has '
                      'echado a todos! durante 3 segundos y detener todos')) +
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">Bala</h3>'
         + dos_cajas(('Al arrancar', B_BALA_INI,
                      'Al hacer clic en la bandera, esconder la bala'),
                     ('Al disparar', B_BALA,
                      'Al recibir el mensaje disparo, ir a la x que dice NaveX con y menos 130, '
                      'mostrarse, subir de 12 en 12 hasta pasar de 160 y esconderse')) +
         '<p>Fíjate en el <em>ir a x: (NaveX)</em>. Ahí es donde el recado que escribe la nave se '
         'convierte en el sitio del que sale el disparo. Si te olvidas de ese bloque, la bala '
         'saldrá siempre del mismo punto.</p>'
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">Marciano</h3>'
         + dos_cajas(('Que le den', B_MARCIANO,
                      'Al hacer clic en la bandera, colocarse, mostrarse y, por siempre, si está '
                      'tocando la Bala iniciar sonido Pop, sumar 1 a Puntos y esconderse'),
                     ('El vaivén', B_VAIVEN,
                      'Al hacer clic en la bandera, por siempre repetir 40 veces cambiar x por 3 '
                      'y repetir 40 veces cambiar x por menos 3')) +
         '<p>Un marciano escondido <strong>no toca nada</strong>: por eso, una vez le das, deja de '
         'sumar puntos solo, sin tener que pararle el programa.</p>'
         '<p>Cuando el primero funcione, <strong>duplícalo hasta tener ocho</strong> y cámbiale a '
         'cada uno la <code>x</code> del <em>ir a</em>: −150, −100, −50, 0, 50, 100, 150 y 200. '
         'Si quieres dos filas, cambia también la <code>y</code>.</p>'),

        ('Comprueba que lo has entendido',
         pregunta('1', 'La bala sube bien, pero <strong>sale siempre del centro</strong> de la '
                       'pantalla en vez de salir de la nave. ¿Qué falta?',
                  [('flechas', 'Ponerle a la bala los mismos bloques de las flechas que tiene la nave',
                    'Así la bala seguiría a la nave <em>todo el rato</em>, incluso mientras sube. '
                    'Funcionaría a medias y sería más lío que la variable.'),
                   ('variable', 'Que la nave vaya guardando su posición en NaveX y que la bala la '
                    'use en su ir a x:',
                    'Correcto. Un objeto <b>no puede mirar dónde está otro</b>. La variable es el '
                    'recado: la nave la escribe en cada vuelta de su bucle, la bala la lee al '
                    'salir.'),
                   ('mensaje', 'Meter la posición dentro del mensaje disparo',
                    'Los mensajes de Scratch <b>no llevan datos</b>: sólo avisan de que ha pasado '
                    'algo. Justo por eso hace falta la variable.')],
                  'variable')),

        ('Tu versión',
         '<p>Hasta aquí es el juego de todos. <strong>A partir de aquí es el tuyo.</strong> '
         'Elige de esta lista o inventa, pero apúntalo en la ficha de la '
         '<a href="../sesiones/s17.html">sesión 17</a> antes de empezar:</p>' +
         tabla(['Idea', 'Qué tienes que tocar'], [
             ['Dos filas de marcianos',
              'Duplicar y cambiar la <code>y</code>. <strong>Y el 8</strong> del <em>esperar hasta que</em>'],
             ['Que los marcianos bajen un poco en cada vaivén',
              'Un <em>cambiar y por (−10)</em> entre los dos <em>repetir</em>'],
             ['Marcianos de distinto color que valen distinto',
              'Un disfraz por color y otro número en el <em>sumar a (Puntos)</em>'],
             ['Que ellos también disparen',
              'Otro objeto bala, con <em>al recibir</em> y un mensaje que envíe el marciano'],
             ['Un escudo que aguante tres impactos',
              'Variable <code>Escudo</code> y <em>sumar a (Escudo) (−1)</em>'],
             ['Pantalla de inicio con el título',
              'Pieza 6 de la S18'],
         ])),

        ('Lo has conseguido si…',
         logros(['La nave se mueve con las flechas y no se sale de la pantalla.',
                 'La bala sale <strong>de la nave</strong>, no del centro.',
                 'No puedes disparar cien veces por segundo.',
                 'Cada marciano tocado desaparece y suma exactamente un punto.',
                 'La partida termina de las dos maneras: por tiempo y por ganar.',
                 'Tres partidas seguidas empiezan exactamente igual.',
                 'Tiene algo tuyo que no está en esta página.'])),
    ],
    guia='ejercicio-space-invaders.pdf', guia_nota=AVISO_GUIA)
escribir_juego('space-invaders', space)


# ============================================================ C · ESQUIVAR LO QUE CAE
C_JUGADOR = [
    BANDERA,
    ('stack', 'looks', ['fijar tamaño al', ('num', '40'), '%']),
    ('stack', 'variables', ['dar a', ('drop', 'Vidas'), 'el valor', ('num', '3')]),
    ('stack', 'variables', ['dar a', ('drop', 'Puntos'), 'el valor', ('num', '0')]),
    ('stack', 'motion', ['ir a x:', ('num', '0'), 'y:', ('num', '-140')]),
    ('c', 'control', ['por siempre'], [
        si(tecla('flecha derecha'), [('stack', 'motion', ['cambiar x por', ('num', '6')])]),
        si(tecla('flecha izquierda'), [('stack', 'motion', ['cambiar x por', ('num', '-6')])]),
    ]),
]
C_RELOJ = [
    BANDERA,
    ('c', 'control', ['por siempre'], [
        ('stack', 'control', ['esperar', ('num', '1'), 'segundos']),
        ('stack', 'variables', ['sumar a', ('drop', 'Puntos'), ('num', '1')]),
    ]),
]
C_FIN = [
    BANDERA,
    ('stack', 'control', ['esperar hasta que',
                          hexa('operators', var('Vidas'), '=', ('num', '0'))]),
    ('stack', 'looks', ['decir', op('unir', ('txt', 'Fin. Puntos: '), var('Puntos')),
                        'durante', ('num', '3'), 'segundos']),
    ('cap', 'control', ['detener', ('drop', 'todos')]),
]
C_PIEDRA = [
    BANDERA,
    ('stack', 'looks', ['fijar tamaño al', ('num', '40'), '%']),
    ('c', 'control', ['por siempre'], [
        ('stack', 'looks', ['mostrar']),
        ('stack', 'motion', ['ir a x:', azar('-200', '200'), 'y:', ('num', '160')]),
        ('c', 'control', ['repetir hasta que',
                          hexa('operators', POSY, '<', ('num', '-150'))], [
            ('stack', 'motion', ['cambiar y por', ('num', '-8')]),
            si(tocando('Jugador'), [
                ('stack', 'sound', ['iniciar sonido', ('drop', 'Pop')]),
                ('stack', 'variables', ['sumar a', ('drop', 'Vidas'), ('num', '-1')]),
                ('stack', 'looks', ['esconder']),
                ('stack', 'motion', ['ir a x:', ('num', '0'), 'y:', ('num', '-160')])]),
        ]),
    ]),
]
C_MAL = [
    ('stack', 'variables', ['dar a', ('drop', 'Vidas'), 'el valor', ('num', '-1')]),
]

esquivar = pagina_juego(
    'esquivar', 'Esquivar lo que cae', 'C',
    'Esquivar lo que cae, en Scratch 3: la opción más directa del proyecto final. Tres vidas, '
    'un marcador que sube solo y cosas que caen. CyR 1º ESO.',
    'aguantar lo máximo posible debajo de una lluvia de cosas que caen. Tres vidas, y un punto '
    'por cada segundo que sobrevives.',
    [
        ('El más corto de los tres',
         '<p>Dos objetos y cuatro programas. Si vas justo de tiempo o el Pong se te atragantó, '
         'este es el tuyo: <strong>se monta entero con piezas del kit</strong>, sin nada que no '
         'hayas hecho ya.</p>'
         '<p>Y tiene una ventaja para el proyecto: como es corto, te sobra sesión para hacerlo '
         '<em>tuyo</em>, que es lo que de verdad puntúa.</p>' + REUTILIZA +
         tabla(['Pieza', 'De dónde sale'], [
             ['Moverse con las flechas', 'S05 · Pieza 1 de la S18'],
             ['Aparecer arriba en un sitio al azar', 'Pieza 3 de la S18'],
             ['Caer hasta abajo', 'S12 · <em>cambiar y por</em>'],
             ['Chocar y perder una vida', 'Pieza 4 de la S18'],
             ['Esconderse y volver a salir', 'Pieza 8 de la S18'],
             ['Marcador y fin de partida', 'Piezas 2 y 7 de la S18'],
         ])),

        ('Los dos objetos',
         '<p>Necesitas un <strong>Jugador</strong> —el que esquiva— y una <strong>Piedra</strong>, '
         'que luego duplicarás.</p>'
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">Jugador · moverse</h3>'
         + caja(C_JUGADOR, 'Programa del jugador: colocarse abajo con tres vidas y el marcador a '
                           'cero y, por siempre, moverse a derecha e izquierda con las flechas') +
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">Jugador · dos programas más</h3>'
         + dos_cajas(('Un punto por segundo', C_RELOJ,
                      'Al hacer clic en la bandera, por siempre esperar un segundo y sumar un '
                      'punto'),
                     ('Cuando te quedas sin vidas', C_FIN,
                      'Al hacer clic en la bandera, esperar hasta que Vidas sea 0, decir Fin con '
                      'los puntos durante 3 segundos y detener todos')) +
         '<p>El marcador de este juego <strong>no lo sube acertar: lo sube aguantar</strong>. '
         'Cuanto más tardas en perder las tres vidas, más puntos.</p>'
         '<h3 style="margin:18px 0 2px;font-size:1.02rem;color:#1B4F8A">Piedra</h3>'
         + caja(C_PIEDRA, 'Programa de la piedra: por siempre mostrarse, ir a una x al azar arriba '
                          'del todo y bajar de 8 en 8 hasta pasar de menos 150; si por el camino '
                          'toca al Jugador, sonar, restar una vida, esconderse y bajar del todo',
                pie='Cuando la piedra sale por abajo —o te da—, el <em>por siempre</em> la devuelve '
                    'arriba, a otro sitio al azar. Así una sola piedra cae una y otra vez.') +
         '<p>Cuando funcione, <strong>duplícala dos o tres veces</strong>. No hace falta cambiarles '
         'nada: cada copia sortea su propia <code>x</code>. Con más de cuatro o cinco, el juego se '
         'vuelve imposible.</p>'),

        ('Comprueba que lo has entendido',
         pregunta('1', 'Quieres que chocar quite <strong>una</strong> vida. ¿Cuál de estos bloques '
                       'lo hace?' +
                  '<div style="margin:10px 0">' +
                  caja(C_MAL, 'Bloque dar a Vidas el valor menos 1', ancho=330,
                       fondo='#FFFDF4') +
                  '</div>¿Ese, u otro?',
                  [('dar', 'Ese mismo: dar a (Vidas) el valor (−1)',
                    'No. Ese <b>machaca</b> el marcador: te pone las vidas en −1 a la primera, '
                    'sin pasar por 2 y por 1. Es el fallo de la sesión 9 otra vez.'),
                   ('sumar', 'Otro: sumar a (Vidas) (−1)',
                    'Correcto. <b>sumar a</b> también resta, si le pones un número negativo. No '
                    'existe ningún bloque «restar a»: es el mismo con el signo cambiado.'),
                   ('restar', 'Otro: restar a (Vidas) (1)',
                    'Ese bloque no existe en la paleta. Búscalo en Variables y verás que sólo '
                    'están <em>dar a … el valor</em> y <em>sumar a …</em>')],
                  'sumar')),

        ('Tu versión',
         '<p>Este es el que más margen te deja, porque el juego base se monta en una sesión. '
         'Elige de la lista o inventa, pero apúntalo en la ficha de la '
         '<a href="../sesiones/s17.html">sesión 17</a> antes de empezar:</p>' +
         tabla(['Idea', 'Qué tienes que tocar'], [
             ['Monedas que en vez de quitar, suman',
              'Duplicar la piedra, cambiarle el disfraz y poner <em>sumar a (Puntos) (5)</em>'],
             ['Que caigan más rápido cuanto más aguantas',
              '<em>cambiar y por (−8 − Puntos / 10)</em>, como la dificultad del Pong en la S16'],
             ['Un escudo que aguante un golpe',
              'Variable <code>Escudo</code>: si vale 1, en vez de quitar vida se gasta el escudo'],
             ['Que el jugador también salte',
              'Dos condicionales más con <em>cambiar y por</em> y las flechas arriba y abajo'],
             ['Aviso visual al perder una vida',
              'Un <em>cambiar disfraz a</em> del jugador, o un <em>decir (¡Ay!)</em>'],
             ['Meteoritos, gotas de lluvia, exámenes, calcetines…',
              'Sólo los disfraces y el fondo. El código es el mismo'],
         ])),

        ('Lo has conseguido si…',
         logros(['El jugador se mueve con las flechas y las piedras caen desde arriba.',
                 'Chocar quita <strong>una</strong> vida, no todas.',
                 'La misma piedra vuelve a salir arriba después de caer.',
                 'El marcador sube solo mientras aguantas.',
                 'Al llegar a 0 vidas, la partida termina y dice la puntuación.',
                 'Tres partidas seguidas empiezan exactamente igual.',
                 'Tiene algo tuyo que no está en esta página.'])),
    ])
escribir_juego('esquivar', esquivar)


# ============================================================ índice de juegos
# Se regenera entero: cambia de ser una lista de juegos sueltos a ser la página
# donde se elige el proyecto final.
TRES = [
    ('arkanoid', '\U0001F9F1', 'A · Arkanoid',
     'Rompe todos los ladrillos con la pelota del Pong. Si hiciste las sesiones 15 y 16, '
     'ya tienes medio juego montado.'),
    ('space-invaders', '\U0001F47E', 'B · Space Invaders',
     'Una nave que dispara y una fila de marcianos. La más larga de las tres, y la que más '
     'objetos tiene.'),
    ('esquivar', '☄️', 'C · Esquivar lo que cae',
     'Aguanta debajo de una lluvia de cosas, con tres vidas. La más corta: te deja más '
     'sesión para hacerla tuya.'),
]

YA_HECHOS = [
    ('carreras', '\U0001F3CE️', 'Juego de carreras', 'S10'),
    ('laberinto', '\U0001F9E9', 'Laberinto', 'S12 y S13'),
    ('piedra-papel-tijera', '✊', 'Piedra, papel o tijera', 'S14'),
    ('pong', '\U0001F3D3', 'Pong', 'S15 y S16'),
]

AMPLIACION = [
    ('tres-en-raya', '❌', 'Tres en raya', 'Turnos y lógica. La guía monta el tablero pero '
     'no llega a comprobar quién gana: esa parte te toca a ti'),
    ('naves', '\U0001F680', 'Juegos de naves', 'Acción y disparos. Usa clones, que no se ven en '
     'ninguna sesión'),
    ('bomb-jack', '\U0001F4A3', 'Bomb Jack', 'Plataformas y coleccionables. El más largo de todos'),
    ('carrera-autos', '\U0001F697', 'Carrera de autos', 'Otra versión de la carrera de la S10'),
    ('cumpleanos-feliz', '\U0001F3B5', 'Cumpleaños feliz', 'Música y secuencias. Hay que añadir '
     'la extensión Música, que no está en la paleta'),
]


def _tarjeta(href, icono, clave, nota):
    return ('<a href="%s" class="bc">\n<span class="bi">%s</span><span class="bk">%s</span>\n'
            '<span class="bn">%s</span></a>' % (href, icono, clave, nota))


INDICE = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#FF8C1A">
<link rel="icon" type="image/svg+xml" href="../../../favicon.svg">
<title>Juegos · Proyecto final · Scratch · CyR 1º ESO</title>
<meta name="description" content="Las tres bases entre las que se elige el proyecto final de Scratch, y los juegos de ampliación. CyR 1º ESO.">
<link rel="canonical" href="https://cyr1-ies-jdq.malonso72.workers.dev/trimestres/t1-scratch/juegos/index.html">
<meta property="og:title" content="Juegos · Proyecto final · CyR 1º ESO">
<meta property="og:description" content="Las tres bases entre las que se elige el proyecto final de Scratch, y los juegos de ampliación.">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600;700&family=Barlow+Condensed:wght@600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../../assets/css/common.css">
<link rel="stylesheet" href="../../../assets/css/hub.css">
<style>
  .nota-juegos{max-width:900px;margin:0 auto 4px;padding:0 16px;font-size:1.02rem;line-height:1.6;}
  .nota-juegos p{margin:0 0 12px;}
  .nota-pdf{border-left:5px solid #D4700A;background:#FFF6EC;border-radius:0 8px 8px 0;
    padding:12px 16px;margin:16px 0;}
  .nota-pdf p{margin:0;}
</style>
</head>
<body>
<a href="#main-content" class="skip-link">Saltar al contenido principal</a>

<header class="curso-hd">
<a class="curso-lg" href="../../../index.html">CyR 1º ESO</a>
<span class="curso-sb">T1 · Scratch</span>
</header>

<nav class="curso-navcross" role="navigation" aria-label="Navegación del trimestre">
  <a href="../../../index.html"><span>\U0001F3E0</span><span class="nc-lbl">Índice</span></a>
  <span class="nc-sep">·</span>
  <a href="../index.html"><span>\U0001F4CB</span><span class="nc-lbl">Hub T1</span></a>
  <span class="nc-sep">·</span>
  <a href="../sesiones/index.html"><span>\U0001F5D3️</span><span class="nc-lbl">Sesiones</span></a>
  <span class="nc-sep">·</span>
  <span class="nc-current"><span>\U0001F3AE</span><span class="nc-lbl">Juegos</span></span>
</nav>

<div id="main-content">
<section class="unidad-titulo-hero">
  <div class="num">T1 · Scratch</div>
  <h1>\U0001F3AE Elige tu proyecto final</h1>
  <div class="duracion">Tres bases para las sesiones 17 a 20</div>
</section>

<div class="nota-juegos">
<p>El proyecto final es <strong>un juego completo</strong>, y no se parte de cero: eliges una de
estas tres bases y la montas. Cada página trae los programas dibujados bloque a bloque y dice qué
pieza sale de qué sesión.</p>
<p><strong>Pero el proyecto no es copiar el juego.</strong> Copiarlo es el primer día. El proyecto
es <em>tu versión</em>: qué le cambias y qué le añades. Eso lo escribes en la ficha de la
<a href="../sesiones/s17.html">sesión 17</a> antes de tocar un bloque.</p>
</div>

<div class="hub-main">
  <div class="section-title">Las tres opciones</div>
  <div class="bg bg-large">{TRES}</div>

  <div class="section-title">Estos ya los has hecho en clase</div>
  <div class="nota-juegos"><p>No son opciones de proyecto: son sesiones que ya tienes hechas.
  Las páginas siguen aquí por la guía en PDF, por si quieres repetirlos en casa.</p></div>
  <div class="bg bg-large">{YA}</div>

  <div class="section-title">De ampliación, si te sobra tiempo</div>
  <div class="nota-juegos"><p>Ninguno de estos vale como proyecto final: o piden bloques que no
  hemos visto, o se quedan a medias. Están aquí para el que quiera seguir por su cuenta.</p>
  <div class="nota-pdf"><p>⚠️ <strong>Todas las guías en PDF están hechas con
  Scratch 2</strong>, igual que el cuadernillo. Verás <em>al presionar</em> donde hoy pone
  <em>al hacer clic en</em>, o <em>fijar … a</em> donde pone <em>dar a … el valor</em>. La tabla
  de equivalencias la tienes en clase.</p></div></div>
  <div class="bg bg-large">{AMP}</div>
</div>
</div>

<p class="foot">
  IES Jiménez de Quesada · Santa Fe (Granada)<br>
  CyR 1º ESO · Curso 2026-27 · Manuel Alonso Herrera
  <br><a href="https://tecnologia-ies-jdq.malonso72.workers.dev/">\U0001F3DB️ Otras asignaturas del departamento</a>
  <br><span class="version">v1.0.0</span>
</p>
<script src="../../../assets/js/common.js"></script>
<script src="../../../assets/js/header.js"></script>
<script data-goatcounter="https://malonso72.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>
'''

indice = (INDICE
          .replace('{TRES}', ''.join(_tarjeta(sl + '.html', ic, nb, no)
                                     for sl, ic, nb, no in TRES))
          .replace('{YA}', ''.join(_tarjeta(sl + '.html', ic, nb,
                                            'Ya lo hiciste en la <strong>%s</strong>. Aquí tienes '
                                            'la guía en PDF' % ses)
                                   for sl, ic, nb, ses in YA_HECHOS))
          .replace('{AMP}', ''.join(_tarjeta(sl + '.html', ic, nb, no)
                                    for sl, ic, nb, no in AMPLIACION)))
escribir_juego('index', indice)

# -*- coding: utf-8 -*-
"""El apartado N.3 de «Tu actividad» en cada sesión de T1: un programa escrito en seudocódigo,
sin dibujo de bloques, que el alumno tiene que pasar a Scratch.

Es el tercer escalón de la actividad, después de N.1 y N.2: copiar un dibujo no obliga a decidir
qué bloque hace falta; diseñar desde cero es el salto del proyecto final. Aquí se le dice qué
tiene que pasar, línea a línea y en castellano, y él decide qué bloque es cada línea, en qué
categoría está y cómo se encaja. Sin lista de bloques (Manuel, 30-09: «si no, se convierte en un
ensayo y error»).

El seudocódigo se GENERA desde las mismas tuplas con las que scratchsvg.py dibuja los bloques y
sb3.py exporta los .sb3, con la tabla FRASES (patrón del bloque -> frase). Así cada programa se
puede exportar y ejecutar para comprobar que hace lo que dice (`gen_sb3.py --retos` deja uno por
sesión en `_soluciones/sb3/retos/`), y el texto no puede irse de lo que hacen los bloques. Un
bloque sin frase sale con su texto de Scratch tal cual y SIN_FRASE lo apunta.

Reglas para escribir un N.3:
- programa DISTINTO al del ejemplo y a los de N.1 y N.2, y que no se adelante al juego de una
  sesión posterior;
- sólo con bloques de esa sesión y de las anteriores (un bloque nuevo como mucho);
- en su PROPIO objeto de la biblioteca, nombrado (el que dice OBJETOS en ampliaciones.py), y
  arrancado con una tecla que no use nada de N.1 ni de N.2;
- con pasos de preparación explícitos y un «Sabes que está bien si…» con lo que tiene que verse.
"""
from sb3 import _patron
from scratchsvg import rep, op, hexa, tecla, var

INTRO = ('Aquí no hay dibujo: cada línea es un bloque. Tú decides cuál es, en qué categoría '
         'está y dónde se encaja. Lo que va con sangría va <em>dentro</em> de la línea de arriba.')

LOGRO = 'El programa del apartado {n}.3 está montado y hace lo que dice «Sabes que está bien si…».'

DIRECCIONES = {'90': 'hacia la derecha', '-90': 'hacia la izquierda', '0': 'hacia arriba',
               '180': 'hacia abajo'}
NOMBRES = {'Sprite1': 'el gato (Sprite1)'}
COLORES = {'#1A1A1A': 'negro de las paredes'}


def _tecla(k):
    if k.startswith('flecha'):
        return 'la %s' % k
    return 'la tecla %s' % (k.upper() if len(k) == 1 else k)


def _direccion(v):
    return ('mirar %s (dirección %s)' % (DIRECCIONES[v], v)) if v in DIRECCIONES \
        else 'mirar en dirección %s' % v


def _tocando(v):
    if v == 'borde':
        return 'toca el borde'
    if v == 'puntero del ratón':
        return 'toca el puntero del ratón'
    return 'toca a %s' % NOMBRES.get(v, v)


def _detener(v):
    return 'detener todo' if v == 'todos' else 'detener este programa'


def _segundos(v):
    return '%s segundo' % v if v == '1' else '%s segundos' % v


# «si toca el borde» pero «repetir hasta que toque el borde»: las condiciones se escriben en
# indicativo y aquí se pasan a subjuntivo para los bloques que lo piden.
_SUBJ = [('toca ', 'toque '), ('está pulsad', 'esté pulsad'), ('es igual', 'sea igual'),
         ('es menor', 'sea menor'), ('es mayor', 'sea mayor'), ('no se cumple', 'no se cumpla')]


def _subjuntivo(cond):
    for a, b in _SUBJ:
        cond = cond.replace(a, b)
    return cond


# (tipo, patrón) -> frase. {h0}, {h1}… son los huecos por orden; {d0}, {d1}… los desplegables.
# Un valor puede ser una función que recibe la lista de huecos y desplegables ya en texto.
# Los huecos de texto llegan ya entre comillas («…»); los números, tal cual.
FRASES = {
    # eventos
    ('hat', 'al hacer clic en <bandera>'): 'Cuando se pulse la bandera verde:',
    ('hat', 'al presionar tecla []'): lambda h, d: 'Cuando se pulse %s:' % _tecla(d[0]),
    ('hat', 'al recibir []'): 'Cuando llegue el mensaje «{d0}»:',
    ('stack', 'enviar []'): 'enviar el mensaje «{d0}» a todos',
    # control
    ('c', 'por siempre'): 'para siempre:',
    ('c', 'repetir _'): 'repetir {h0} veces:',
    ('c', 'repetir hasta que _'): lambda h, d: 'repetir hasta que %s:' % _subjuntivo(h[0]),
    ('c', 'si _ entonces'): 'si {h0}:',
    ('ce', 'si _ entonces'): 'si {h0}:',
    ('cap', 'detener []'): lambda h, d: _detener(d[0]),
    ('stack', 'esperar _ segundos'): lambda h, d: 'esperar %s' % _segundos(h[0]),
    ('stack', 'esperar hasta que _'): lambda h, d: 'esperar hasta que %s' % _subjuntivo(h[0]),
    # apariencia
    ('stack', 'decir _ durante _ segundos'): lambda h, d: 'decir %s durante %s' % (h[0], _segundos(h[1])),
    ('stack', 'decir _'): 'decir {h0}',
    ('stack', 'cambiar disfraz a []'): 'cambiar al disfraz «{d0}»',
    ('stack', 'cambiar fondo a []'): 'cambiar al fondo «{d0}»',
    ('stack', 'siguiente disfraz'): 'pasar al siguiente disfraz',
    ('stack', 'esconder'): 'esconderse',
    ('stack', 'mostrar'): 'mostrarse',
    ('stack', 'fijar tamaño al _ %'): 'poner el tamaño al {h0} %',
    # movimiento
    ('stack', 'mover _ pasos'): 'avanzar {h0} pasos',
    ('stack', 'girar <giro-d> _ grados'): 'girar {h0} grados hacia la derecha',
    ('stack', 'girar <giro-i> _ grados'): 'girar {h0} grados hacia la izquierda',
    ('stack', 'apuntar en dirección _'): lambda h, d: _direccion(h[0]),
    ('stack', 'ir a x: _ y: _'): 'ir al punto x: {h0}, y: {h1}',
    ('stack', 'sumar a x _'): 'desplazarse {h0} en horizontal (sumar a x)',
    ('stack', 'sumar a y _'): 'desplazarse {h0} en vertical (sumar a y)',
    ('stack', 'si toca un borde, rebotar'): 'si toca un borde, dar la vuelta (rebotar)',
    ('stack', 'fijar estilo de rotación a []'): 'poner el estilo de rotación en «{d0}»',
    ('rep', 'posición en x'): 'la posición en x',
    ('rep', 'posición en y'): 'la posición en y',
    ('rep', 'dirección'): 'la dirección',
    # lápiz
    ('stack', 'borrar todo'): 'borrar todo lo dibujado',
    ('stack', 'bajar lápiz'): 'bajar el lápiz',
    ('stack', 'subir lápiz'): 'subir el lápiz',
    # sensores
    ('stack', 'preguntar _ y esperar'): 'preguntar {h0} y esperar la respuesta',
    ('stack', 'reiniciar cronómetro'): 'poner el cronómetro a cero',
    ('rep', 'respuesta'): 'la respuesta',
    ('rep', 'cronómetro'): 'el cronómetro',
    ('rep', 'posición x del ratón'): 'la posición x del ratón',
    ('rep', 'posición y del ratón'): 'la posición y del ratón',
    ('bool', '¿tecla [] presionada?'): lambda h, d: '%s está pulsada' % _tecla(d[0]),
    ('bool', '¿tocando [] ?'): lambda h, d: _tocando(d[0]),
    ('bool', '¿tocando el color _ ?'): 'toca el color {h0}',
    ('bool', '¿ratón presionado?'): 'el ratón está pulsado',
    # sonido
    ('stack', 'iniciar sonido []'): 'hacer sonar «{d0}»',
    ('stack', 'tocar sonido [] hasta que termine'): 'hacer sonar «{d0}» y esperar a que termine',
    # variables
    ('stack', 'dar a [] el valor _'): 'poner {d0} a {h0}',
    ('stack', 'sumar a [] _'): 'sumar {h0} a {d0}',
    ('stack', 'mostrar variable []'): 'mostrar la variable {d0}',
    ('stack', 'esconder variable []'): 'esconder la variable {d0}',
    # operadores
    ('rep', '_ + _'): '{h0} más {h1}',
    ('rep', '_ - _'): '{h0} menos {h1}',
    ('rep', '_ * _'): '{h0} por {h1}',
    ('rep', '_ / _'): '{h0} entre {h1}',
    ('rep', 'número aleatorio entre _ y _'): 'un número al azar entre {h0} y {h1}',
    ('rep', 'unir _ _'): '{h0} seguido de {h1}',
    ('bool', '_ < _'): '{h0} es menor que {h1}',
    ('bool', '_ = _'): '{h0} es igual a {h1}',
    ('bool', '_ > _'): '{h0} es mayor que {h1}',
    ('bool', '_ y _'): '{h0} y además {h1}',
    ('bool', '_ o _'): '{h0} o bien {h1}',
    ('bool', 'no _'): 'no se cumple que {h0}',
}

SIN_FRASE = []   # patrones que han salido con el texto del bloque: el test los mira


def _es_numero(v):
    try:
        float(str(v))
        return True
    except ValueError:
        return False


def _hueco(h):
    tipo, v = h
    if tipo == 'lit':
        return str(v) if _es_numero(v) else '«%s»' % v
    if tipo == 'color':
        return COLORES.get(v, str(v))
    if tipo in ('rep', 'bool'):
        # una cuenta dentro de otro bloque va entre paréntesis: «seguido de (edad por 7)»
        if tipo == 'rep' and _patron(v[2])[0] in ('_ + _', '_ - _', '_ * _', '_ / _'):
            return '(%s)' % frase(v)
        return frase(v)
    return str(v)


def _pulir(t):
    return t.replace(' a el ', ' al ').replace(' de el ', ' del ')


def frase(b):
    """La frase de un bloque (sin sus hijos)."""
    tipo, cat, partes = b[0], b[1], b[2]
    if tipo == 'rep' and cat == 'variables':
        return 'el valor de %s' % partes[0]
    patron, huecos, drops = _patron(partes)
    h = [_hueco(x) for x in huecos]
    plantilla = FRASES.get((tipo, patron))
    if plantilla is None:
        SIN_FRASE.append((tipo, patron))
        txt = patron
        for x in h:
            txt = txt.replace('_', x, 1)
        for d in drops:
            txt = txt.replace('[]', d, 1)
        return txt.replace('<bandera>', 'bandera verde')
    if callable(plantilla):
        return _pulir(plantilla(h, drops))
    kw = {'h%d' % i: x for i, x in enumerate(h)}
    kw.update({'d%d' % i: x for i, x in enumerate(drops)})
    return _pulir(plantilla.format(**kw))


def lineas(programa, nivel=0):
    """Lista de (nivel de sangría, frase) de un programa. Lo que cuelga de un sombrero va con
    una sangría más, como lo que va dentro de un bucle."""
    out = []
    for b in programa:
        out.append((nivel, frase(b)))
        if b[0] == 'hat':
            nivel += 1
            continue
        if b[0] == 'c':
            out.extend(lineas(b[3], nivel + 1))
        elif b[0] == 'ce':
            out.extend(lineas(b[3], nivel + 1))
            out.append((nivel, 'si no:'))
            out.extend(lineas(b[5], nivel + 1))
    return out


def html_pseudo(programa):
    li = ''.join('\n  <li class="n%d">%s</li>' % (n, f) for n, f in lineas(programa))
    return '<ol class="pseudo">%s\n</ol>' % li


# ------------------------------------------------------------------ ayudas para escribirlos
def K(k):
    return ('hat', 'events', ['al presionar tecla', ('drop', k)])


def S(texto, *args):
    """Bloque de pila a partir de sus partes."""
    return ('stack', 'motion', [texto] + list(args))


def decir(t, s='2'):
    return ('stack', 'looks', ['decir', t if isinstance(t, tuple) and t[0] in ('rep',) else ('txt', t),
                               'durante', ('num', s), 'segundos'])


def esperar(s):
    return ('stack', 'control', ['esperar', ('num', s), 'segundos'])


def mover(n):
    return ('stack', 'motion', ['mover', ('num', n), 'pasos'])


def apuntar(d):
    return ('stack', 'motion', ['apuntar en dirección', ('num', d)])


def ir(x, y):
    return ('stack', 'motion', ['ir a x:', ('num', x), 'y:', ('num', y)])


def rotacion(estilo):
    return ('stack', 'motion', ['fijar estilo de rotación a', ('drop', estilo)])


def dar(v, valor):
    return ('stack', 'variables', ['dar a', ('drop', v), 'el valor', valor])


def sumar(v, n):
    return ('stack', 'variables', ['sumar a', ('drop', v), ('num', n)])


def repetir(n, hijos):
    return ('c', 'control', ['repetir', ('num', n)], hijos)


def hasta(cond, hijos):
    return ('c', 'control', ['repetir hasta que', cond], hijos)


def si(cond, hijos):
    return ('c', 'control', ['si', cond, 'entonces'], hijos)


def sino(cond, a, b):
    return ('ce', 'control', ['si', cond, 'entonces'], a, ['si no'], b)


def preguntar(t):
    return ('stack', 'sensing', ['preguntar', ('txt', t), 'y esperar'])


def elige(nombre, busca, que):
    return ('Añade %s: botón <strong>Elige un objeto</strong> (el del gato, abajo a la derecha), '
            'escribe <strong>%s</strong> en el buscador y elige <strong>%s</strong>.' % (que, busca, nombre))


def selecciona(obj, no):
    return ('<strong>Selecciónalo</strong> abajo a la derecha antes de arrastrar ningún bloque. '
            'Este programa va en %s, <strong>no</strong> en %s.' % (obj, no))


def prueba(k, otros):
    return ('Para probarlo, para todo con el <strong>círculo rojo</strong> y pulsa la tecla '
            '<strong>%s</strong>. No uses la bandera: la bandera arranca %s.' % (k, otros))


RESP = rep('sensing', 'respuesta')
BORDE = ('bool', 'sensing', ['¿tocando', ('drop', 'borde'), '?'])
POSX = rep('motion', 'posición en x')


def unir(a, b):
    return op('unir', a, b)


def txt(t):
    return ('txt', t)


def num(n):
    return ('num', n)


# ------------------------------------------------------------------ los N.3
# num -> dict(objeto, planteamiento, preparar, programas=[(etiqueta, programa)], comprueba,
#             solucion=opcional, objetos_sb3=[nombres]) ; `objeto` completa «Monta … a partir del
# texto». `solucion` sólo si lo que se enseña NO es lo que hay que conseguir (S17).
RETOS = {
    1: dict(
        objeto='la pelota que se presenta',
        planteamiento='Una pelota que se presenta, da dos saltos hacia la derecha y avisa de que '
                      'ha llegado.',
        preparar=[elige('Ball', 'Ball', 'la pelota') + ' Arrástrala con el ratón a la izquierda del '
                  'escenario, para que tenga sitio para avanzar.',
                  selecciona('la pelota', 'el gato ni en el perro'),
                  'La primera línea es un bloque que todavía no has usado: está en '
                  '<strong>Eventos</strong>, el amarillo, y se llama <strong>al presionar '
                  'tecla</strong>. En su desplegable eliges la <strong>b</strong>.',
                  'Monta el programa de abajo, línea a línea.',
                  prueba('B', 'los programas del gato y del perro')],
        programas=[(None, [K('b'), decir('¡Soy la pelota!'), mover('100'), esperar('1'), mover('100'),
                           decir('¡He llegado!')])],
        comprueba='al pulsar B la pelota dice «¡Soy la pelota!», avanza hacia la derecha, se para '
                  'un segundo, vuelve a avanzar y dice «¡He llegado!». El gato y el perro no hablan.'),

    2: dict(
        objeto='la mariposa que baja la escalera',
        planteamiento='Una mariposa que baja una escalera de dos escalones, con una pausa en cada '
                      'tramo.',
        preparar=[elige('Butterfly 1', 'Butterfly', 'la mariposa'),
                  selecciona('la mariposa', 'el gato'),
                  'Monta el programa de abajo, línea a línea.',
                  prueba('M', 'el cuadrado del gato')],
        programas=[(None, [K('m'), rotacion('no rotar'), ir('-150', '100'),
                           apuntar('90'), mover('60'), esperar('1'),
                           apuntar('180'), mover('60'), esperar('1'),
                           apuntar('90'), mover('60'), esperar('1'),
                           apuntar('180'), mover('60'),
                           decir('¡Abajo del todo!')])],
        comprueba='al pulsar M la mariposa aparece arriba a la izquierda y baja dos escalones: '
                  'derecha, abajo, derecha, abajo, parándose un segundo en cada tramo. Al final dice '
                  '«¡Abajo del todo!». No gira ni se pone boca abajo.'),

    3: dict(
        objeto='la estrella de cinco puntas',
        planteamiento='El lápiz de Scratch dibuja una estrella de cinco puntas y vuelve al punto '
                      'de partida.',
        preparar=[elige('Pencil', 'Pencil', 'el lápiz'),
                  selecciona('el lápiz', 'el gato'),
                  'Monta el programa de abajo. Los bloques de lápiz son los de la extensión que has '
                  'añadido en el apartado anterior.',
                  prueba('E', 'nada, pero las teclas 1, 2, 3 y 4 son del gato')],
        programas=[(None, [K('e'), ('stack', 'pen', ['borrar todo']), ('stack', 'pen', ['subir lápiz']),
                           ir('-75', '40'), apuntar('90'), ('stack', 'pen', ['bajar lápiz']),
                           repetir('5', [mover('150'),
                                         ('stack', 'motion', ['girar', ('icon', 'giro-d'), ('num', '144'), 'grados']),
                                         esperar('0.5')]),
                           ('stack', 'pen', ['subir lápiz'])])],
        comprueba='al pulsar E se borra lo que hubiera y aparece, trazo a trazo, una estrella de '
                  'cinco puntas. El lápiz acaba justo donde empezó. Pregunta para pensar: ¿por qué '
                  '144 grados y no 72, como el pentágono?'),

    4: dict(
        objeto='el murciélago que hay que cazar',
        planteamiento='Un murciélago que vuela rebotando por el escenario hasta que lo tocas con el '
                      'puntero del ratón.',
        preparar=[elige('Bat', 'Bat', 'el murciélago'),
                  selecciona('el murciélago', 'el gato'),
                  'Monta el programa de abajo, línea a línea.',
                  prueba('M', 'nada, pero las flechas son del gato')],
        programas=[(None, [K('m'), rotacion('no rotar'), ir('0', '0'), apuntar('45'),
                           hasta(('bool', 'sensing', ['¿tocando', ('drop', 'puntero del ratón'), '?']),
                                 [mover('6'), ('stack', 'motion', ['si toca un borde, rebotar'])]),
                           decir('¡Me has cazado!'),
                           ('cap', 'control', ['detener', ('drop', 'todos')])])],
        comprueba='al pulsar M el murciélago sale del centro en diagonal y rebota en los bordes sin '
                  'parar. En cuanto pones el puntero del ratón encima, dice «¡Me has cazado!» y todo '
                  'se detiene. No hace falta hacer clic: basta con tocarlo.'),

    5: dict(
        objeto='el coche teledirigido',
        planteamiento='Un coche que avanza solo y que tú conduces con las flechas. Si toca el borde '
                      'del escenario, has perdido.',
        preparar=['Añade el coche: botón <strong>Elige un objeto</strong>, escribe <strong>Conv</strong> '
                  'en el buscador y elige <strong>Convertible 2</strong>, el coche verde.',
                  selecciona('el coche', 'el gato ni en el perro'),
                  'Monta el programa de abajo, línea a línea.',
                  prueba('C', 'los programas del gato y del perro')],
        programas=[(None, [K('c'), ir('0', '0'), apuntar('90'),
                           hasta(BORDE, [
                               mover('4'),
                               si(tecla('flecha izquierda'),
                                  [('stack', 'motion', ['girar', ('icon', 'giro-i'), ('num', '10'), 'grados'])]),
                               si(tecla('flecha derecha'),
                                  [('stack', 'motion', ['girar', ('icon', 'giro-d'), ('num', '10'), 'grados'])]),
                           ]),
                           decir('¡Choque!'),
                           ('cap', 'control', ['detener', ('drop', 'todos')])])],
        comprueba='al pulsar C el coche sale del centro hacia la derecha y no se para; con las '
                  'flechas izquierda y derecha va girando mientras avanza; y en cuanto toca el borde '
                  'dice «¡Choque!» y todo se detiene. Si aguantas más de veinte segundos sin chocar, '
                  'conduces bien. Y mientras tanto el gato y el perro no se han movido.'),

    6: dict(
        objeto='el loro que cruza volando',
        planteamiento='Un loro que cruza el cielo de izquierda a derecha batiendo las alas.',
        preparar=[elige('Parrot', 'Parrot', 'el loro'),
                  selecciona('el loro', 'el gato ni en el oso'),
                  'Monta el programa de abajo, línea a línea.',
                  prueba('P', 'los programas del gato y del oso')],
        programas=[(None, [K('p'), rotacion('izquierda-derecha'), ir('-200', '120'), apuntar('90'),
                           repetir('40', [('stack', 'looks', ['siguiente disfraz']), mover('10'),
                                          esperar('0.1')]),
                           decir('¡He cruzado!')])],
        comprueba='al pulsar P el loro aparece arriba a la izquierda y cruza hasta la derecha en '
                  'unos cuatro segundos, abriendo y cerrando las alas. Al llegar dice «¡He '
                  'cruzado!». Si las alas se mueven tan deprisa que no se ven, revisa la espera.'),

    7: dict(
        objeto='el robot eco',
        planteamiento='Un robot que te pide una palabra y te la repite tres veces, como un eco.',
        preparar=[elige('Retro Robot', 'Robot', 'el robot'),
                  selecciona('el robot', 'el gato'),
                  'Monta el programa de abajo, línea a línea.',
                  prueba('R', 'el diálogo del gato')],
        programas=[(None, [K('r'), preguntar('Dime una palabra'),
                           repetir('3', [decir(unir(RESP, txt('...')), '1'), esperar('0.5')]),
                           decir('¡Soy un robot eco!')])],
        comprueba='al pulsar R el robot te pide una palabra. Si escribes «hola», dice «hola...» '
                  'tres veces, con una pausa entre una y otra, y después «¡Soy un robot eco!».'),

    8: dict(
        objeto='la calculadora de años de perro',
        planteamiento='Un perro que te pregunta la edad de tu perro y te la dice en años de persona.',
        preparar=[elige('Dog2', 'Dog', 'el perro'),
                  selecciona('el perro', 'el gato'),
                  'Crea una variable nueva, <strong>edad</strong>, para todos los objetos.',
                  'Monta el programa de abajo, línea a línea.',
                  prueba('D', 'la calculadora del gato')],
        programas=[(None, [K('d'), preguntar('¿Cuántos años tiene tu perro?'), dar('edad', RESP),
                           decir(unir(txt('En años de persona serían '), op(var('edad'), '*', num('7'))), '3'),
                           decir(unir(txt('Y dentro de 5 años tendrá '), op(var('edad'), '+', num('5'))), '3')])],
        comprueba='al pulsar D el perro pregunta. Si contestas 3, dice «En años de persona serían '
                  '21» y luego «Y dentro de 5 años tendrá 8».'),

    9: dict(
        objeto='el búho que piensa un número',
        planteamiento='Un búho que piensa un número del 1 al 10 y te va diciendo si te pasas o te '
                      'quedas corto hasta que lo aciertas.',
        preparar=[elige('Owl', 'Owl', 'el búho'),
                  selecciona('el búho', 'el gato'),
                  'Crea tres variables: <strong>secreto</strong>, <strong>prueba</strong> e '
                  '<strong>intentos</strong>.',
                  'Monta el programa de abajo, línea a línea.',
                  prueba('N', 'el quiz del gato')],
        programas=[(None, [K('n'),
                           dar('secreto', op('número aleatorio entre', num('1'), 'y', num('10'))),
                           dar('prueba', num('0')), dar('intentos', num('0')),
                           hasta(hexa('operators', var('prueba'), '=', var('secreto')), [
                               preguntar('Estoy pensando un número del 1 al 10. ¿Cuál es?'),
                               dar('prueba', RESP),
                               sumar('intentos', '1'),
                               si(hexa('operators', var('prueba'), '>', var('secreto')), [decir('Es más pequeño', '1')]),
                               si(hexa('operators', var('prueba'), '<', var('secreto')), [decir('Es más grande', '1')]),
                           ]),
                           decir(unir(txt('¡Acertaste en '), unir(var('intentos'), txt(' intentos!'))), '3')])],
        comprueba='al pulsar N el búho pregunta un número. Si te pasas dice «Es más pequeño», si te '
                  'quedas corto «Es más grande», y vuelve a preguntar. Cuando aciertas dice en '
                  'cuántos intentos lo has conseguido. Con buena estrategia, nunca hacen falta más '
                  'de cuatro.'),

    10: dict(
        objeto='la rana saltarina',
        planteamiento='Una rana que da diez saltos de largo al azar y dice dónde ha caído.',
        preparar=[elige('Frog', 'Frog', 'la rana'),
                  selecciona('la rana', 'el gato ni en el perro'),
                  'Monta el programa de abajo, línea a línea.',
                  prueba('F', 'la carrera')],
        programas=[(None, [K('f'), ir('-200', '-100'), apuntar('90'),
                           repetir('10', [('stack', 'motion', ['mover', op('número aleatorio entre', num('10'), 'y', num('40')), 'pasos']),
                                          esperar('0.3')]),
                           decir(unir(txt('He llegado a x = '), POSX), '3')])],
        comprueba='al pulsar F la rana va a la izquierda y da diez saltos, unos cortos y otros '
                  'largos. Al final dice su posición, que cada vez es distinta y siempre está entre '
                  '-100 y 200. Pruébalo tres veces y apunta dónde cae.'),

    11: dict(
        objeto='el árbitro y el tambor',
        planteamiento='Dos objetos nuevos: un árbitro que pita y da la señal, y un tambor que '
                      'redobla cuando le llega el aviso.',
        preparar=[elige('Referee', 'Referee', 'el árbitro'),
                  elige('Drum', 'Drum', 'el tambor') + ' Pon cada uno en un sitio distinto del escenario.',
                  'Hay <strong>dos programas</strong>: el primero va en el árbitro y el segundo en el '
                  'tambor. Selecciona cada objeto antes de montar el suyo.',
                  'El mensaje <strong>redoble</strong> lo creas tú, en el desplegable del bloque '
                  '<em>enviar</em>: <strong>Nuevo mensaje</strong>.',
                  prueba('T', 'el gato, la pelota y el portero')],
        programas=[('En el árbitro:', [K('t'), ('stack', 'sound', ['iniciar sonido', ('drop', 'Referee Whistle')]),
                                       decir('¡Que suene el tambor!'),
                                       ('stack', 'events', ['enviar', ('drop', 'redoble')]),
                                       esperar('3'), decir('¡Bravo!')]),
                   ('En el tambor:', [('hat', 'events', ['al recibir', ('drop', 'redoble')]),
                                      repetir('6', [('stack', 'looks', ['siguiente disfraz']),
                                                    ('stack', 'sound', ['tocar sonido', ('drop', 'High Tom'), 'hasta que termine'])])])],
        comprueba='al pulsar T el árbitro pita y dice «¡Que suene el tambor!»; justo cuando termina '
                  'de hablar, el tambor empieza a sonar y a moverse seis veces, él solo. Después el '
                  'árbitro dice «¡Bravo!». El tambor no tiene ninguna tecla: arranca porque le llega '
                  'el mensaje.'),

    12: dict(
        objeto='el fantasma que patrulla',
        planteamiento='Un fantasma que va y viene por un pasillo del laberinto y asusta al gato si '
                      'lo toca.',
        preparar=[elige('Ghost', 'Ghost', 'el fantasma') + ' Arrástralo con el ratón a un pasillo '
                  'largo y recto de tu laberinto.',
                  selecciona('el fantasma', 'el gato ni en la estrella'),
                  'Monta el programa de abajo. El color negro lo coges con el cuentagotas, igual que '
                  'en el programa del gato.',
                  'Para probarlo, pulsa la <strong>bandera</strong> para mover al gato y luego la '
                  'tecla <strong>G</strong> para despertar al fantasma.'],
        programas=[(None, [K('g'), ('stack', 'looks', ['fijar tamaño al', ('num', '40'), '%']),
                           rotacion('izquierda-derecha'), apuntar('90'),
                           ('c', 'control', ['por siempre'], [
                               mover('3'),
                               si(('bool', 'sensing', ['¿tocando el color', ('color', '#1A1A1A'), '?']),
                                  [('stack', 'motion', ['girar', ('icon', 'giro-d'), ('num', '180'), 'grados']), mover('3')]),
                               si(('bool', 'sensing', ['¿tocando', ('drop', 'Sprite1'), '?']),
                                  [decir('¡Buuu!', '1')]),
                           ])])],
        comprueba='al pulsar G el fantasma avanza por el pasillo, choca con la pared, se da la '
                  'vuelta y sigue en sentido contrario, una y otra vez, sin atravesar las paredes. Si '
                  'llevas al gato hasta él, dice «¡Buuu!». Se para con el círculo rojo.'),

    13: dict(
        objeto='la campana de la cuenta atrás',
        planteamiento='Una campana que cuenta 30 segundos hacia atrás y suena cuando se acaba el '
                      'tiempo.',
        preparar=[elige('Bell', 'Bell', 'la campana') + ' Colócala en una esquina, fuera del '
                  'laberinto.',
                  selecciona('la campana', 'el gato, la estrella ni el fantasma'),
                  'Crea la variable <strong>Tiempo</strong>.',
                  'Monta el programa de abajo, línea a línea.',
                  prueba('T', 'el laberinto')],
        programas=[(None, [K('t'), dar('Tiempo', num('30')),
                           ('stack', 'variables', ['mostrar variable', ('drop', 'Tiempo')]),
                           hasta(hexa('operators', var('Tiempo'), '=', num('0')), [esperar('1'), sumar('Tiempo', '-1')]),
                           ('stack', 'sound', ['iniciar sonido', ('drop', 'Bell Toll')]),
                           decir('¡Se acabó el tiempo!'),
                           ('cap', 'control', ['detener', ('drop', 'todos')])])],
        comprueba='al pulsar T aparece el marcador de Tiempo en 30 y va bajando de uno en uno cada '
                  'segundo. Al llegar a 0 suena la campana, dice «¡Se acabó el tiempo!» y todo se '
                  'detiene. Si lo pulsas mientras juegas al laberinto, tienes treinta segundos para '
                  'llegar a la meta. Guárdalo bien: esta cuenta atrás es una de las piezas del kit del '
                  'proyecto final.'),

    14: dict(
        objeto='el unicornio de la montaña rusa',
        planteamiento='Un unicornio que vigila la cola de la montaña rusa: puedes subir si mides '
                      'más de 140 cm o si vienes con una persona adulta.',
        preparar=[elige('Unicorn', 'Unicorn', 'el unicornio'),
                  selecciona('el unicornio', 'el gato'),
                  'Crea la variable <strong>altura</strong>.',
                  'Monta el programa de abajo, línea a línea. La condición del <em>si</em> lleva el '
                  'operador <strong>o</strong> con dos condiciones dentro.',
                  prueba('U', 'el piedra, papel o tijera')],
        programas=[(None, [K('u'), preguntar('¿Cuánto mides, en centímetros?'), dar('altura', RESP),
                           preguntar('¿Vienes con una persona adulta? Escribe si o no'),
                           sino(hexa('operators', hexa('operators', var('altura'), '>', num('140')), 'o',
                                     hexa('operators', RESP, '=', txt('si'))),
                                [decir('¡Puedes subir a la montaña rusa!', '3')],
                                [decir('Lo siento, todavía no puedes subir', '3')])])],
        comprueba='al pulsar U el unicornio pregunta tu altura y si vienes con un adulto. Con 150 y '
                  '«no», puedes subir. Con 120 y «si», también. Con 120 y «no», no puedes. Prueba '
                  'las tres.'),

    15: dict(
        objeto='el globo que se escapa',
        planteamiento='Un globo que sube solo, temblando a los lados, hasta que toca el techo y '
                      'explota.',
        preparar=[elige('Balloon1', 'Balloon', 'el globo'),
                  selecciona('el globo', 'las pelotas ni en la pala'),
                  'Monta el programa de abajo, línea a línea.',
                  prueba('G', 'el Pong')],
        programas=[(None, [K('g'), ('stack', 'looks', ['mostrar']), ir('0', '-100'),
                           hasta(BORDE, [('stack', 'motion', ['sumar a y', ('num', '3')]),
                                         ('stack', 'motion', ['sumar a x', op('número aleatorio entre', num('-3'), 'y', num('3'))])]),
                           decir('¡Pum!', '1'), ('stack', 'looks', ['esconder'])])],
        comprueba='al pulsar G el globo aparece abajo, en el centro, y sube despacio moviéndose un '
                  'poco a izquierda y derecha. Cuando toca el borde de arriba dice «¡Pum!» y '
                  'desaparece. Si vuelves a pulsar G, reaparece abajo.'),

    16: dict(
        objeto='el saltamontes que cuenta sus saltos',
        planteamiento='Un saltamontes que cruza el escenario a saltos y al final dice cuántos ha '
                      'dado.',
        preparar=[elige('Grasshopper', 'Grass', 'el saltamontes'),
                  selecciona('el saltamontes', 'las pelotas, la pala ni el globo'),
                  'Crea la variable <strong>Saltos</strong>.',
                  'Monta el programa de abajo, línea a línea.',
                  prueba('S', 'el Pong')],
        programas=[(None, [K('s'), dar('Saltos', num('0')), ir('-200', '-100'),
                           hasta(hexa('operators', POSX, '>', num('200')), [
                               ('stack', 'motion', ['sumar a y', ('num', '40')]), esperar('0.2'),
                               ('stack', 'motion', ['sumar a y', ('num', '-40')]),
                               ('stack', 'motion', ['sumar a x', ('num', '30')]),
                               sumar('Saltos', '1')]),
                           decir(unir(txt('He dado '), unir(var('Saltos'), txt(' saltos'))), '3')])],
        comprueba='al pulsar S el saltamontes va a la izquierda y cruza a saltos hasta la derecha. '
                  'Al final dice «He dado 14 saltos». Siempre 14: piensa por qué con la cuenta '
                  '(-200 + 30 × 14).'),

    17: dict(
        objeto='la bailarina que no para',
        planteamiento='Una bailarina que tiene que dar cuatro pasos de baile y decir «¡Fin!». '
                      '<strong>El programa, tal y como está escrito, tiene un fallo</strong>: '
                      'móntalo igual, comprueba qué hace, encuentra la línea culpable y arréglalo.',
        preparar=[elige('Ballerina', 'Ballerina', 'la bailarina'),
                  selecciona('la bailarina', 'los cinco sospechosos'),
                  'Crea la variable <strong>Pasos</strong>.',
                  'Monta el programa de abajo tal cual, con el fallo.',
                  prueba('B', 'los cinco sospechosos'),
                  'Arréglalo y apunta en tu entrega qué línea estaba mal y por qué.'],
        programas=[(None, [K('b'), hasta(hexa('operators', var('Pasos'), '=', num('4')), [
                               dar('Pasos', num('0')),
                               ('stack', 'looks', ['siguiente disfraz']), esperar('0.5'),
                               sumar('Pasos', '1')]),
                           decir('¡Fin!')])],
        solucion=[(None, [K('b'), dar('Pasos', num('0')),
                          hasta(hexa('operators', var('Pasos'), '=', num('4')), [
                              ('stack', 'looks', ['siguiente disfraz']), esperar('0.5'),
                              sumar('Pasos', '1')]),
                          decir('¡Fin!')])],
        comprueba='arreglado, al pulsar B la bailarina cambia de postura cuatro veces, una cada '
                  'medio segundo, y dice «¡Fin!». Sin arreglar, baila y baila y no dice nunca '
                  '«¡Fin!»: ¿qué le pasa a la variable Pasos en cada vuelta?'),
}

# Qué objeto de la biblioteca es cada programa, para el .sb3 de soluciones y las pruebas.
SPRITES = {1: ['Ball'], 2: ['Butterfly 1'], 3: ['Pencil'], 4: ['Bat'], 5: ['Convertible 2'],
           6: ['Parrot'], 7: ['Retro Robot'], 8: ['Dog2'], 9: ['Owl'], 10: ['Frog'],
           11: ['Referee', 'Drum'], 12: ['Ghost'], 13: ['Bell'], 14: ['Unicorn'],
           15: ['Balloon1'], 16: ['Grasshopper'], 17: ['Ballerina']}


def caja_reto(num, seccion=4):
    """El apartado N.3 de la sesión `num`, o '' si no tiene."""
    r = RETOS.get(num)
    if not r:
        return ''
    prep = ''.join('\n  <li><span class="p">Paso %d</span><span>%s</span></li>' % (i + 1, t)
                   for i, t in enumerate(r.get('preparar', [])))
    progs = ''.join(('<p class="rp-obj"><b>%s</b></p>\n' % et if et else '') + html_pseudo(p) + '\n'
                    for et, p in r['programas'])
    return ('<h3 class="sub"><span class="subn">%d.3</span>Monta %s a partir del texto</h3>\n'
            '<p>%s</p>\n<ol class="paso-lista">%s\n</ol>\n<p>%s</p>\n%s'
            '<p class="rp-ok"><b>Sabes que está bien si…</b> %s</p>'
            % (seccion, r['objeto'], r['planteamiento'], prep, INTRO, progs, r['comprueba']))

# -*- coding: utf-8 -*-
"""El reto «🧩 Del papel a los bloques» de cada sesión de T1: un programa escrito en
seudocódigo, sin dibujo de bloques, que el alumno tiene que traducir a Scratch.

Es el tercer escalón de la actividad, después de los pasos y del «Paso N · Un paso más»:
copiar un dibujo no obliga a decidir qué bloque hace falta; diseñar desde cero es el salto
del proyecto final. Aquí se le dice qué tiene que pasar, línea a línea y en castellano, y él
decide qué bloque es cada línea, en qué categoría está y cómo se encaja. Sin lista de bloques
(Manuel, 30-09: «si no, se convierte en un ensayo y error»).

El seudocódigo se GENERA desde las mismas tuplas con las que scratchsvg.py dibuja los bloques
y sb3.py exporta los .sb3, con la tabla FRASES (patrón del bloque -> frase). Así el reto tiene
su solución en `_soluciones/sb3/` sin escribirla dos veces, se puede ejecutar para comprobar
que hace lo que dice, y el texto no puede irse de lo que hacen los bloques. Un bloque sin
frase sale con su texto de Scratch tal cual: `test_sesiones.js` avisa si eso pasa.

Reglas para escribir un reto: programa DISTINTO al del ejemplo y al de la actividad, corto
(8-12 líneas), sólo con bloques de esa sesión y de las anteriores, y con un resultado que se
vea, para que el alumno sepa si lo tiene bien sin dibujo con el que comparar.
"""
from sb3 import _patron


INTRO = ('Aquí no hay dibujo: cada línea es un bloque. Tú decides cuál es, en qué categoría '
         'está y dónde se encaja. Lo que va con sangría va <em>dentro</em> de la línea de arriba.')

LOGRO = 'El programa del apartado {n}.3 está montado y hace lo que dice «Sabes que está bien si…».'

DIRECCIONES = {'90': 'hacia la derecha', '-90': 'hacia la izquierda', '0': 'hacia arriba',
               '180': 'hacia abajo'}


def _tecla(k):
    if k.startswith('flecha'):
        return 'la %s' % k
    return 'la tecla %s' % (k.upper() if len(k) == 1 else k)


def _direccion(v):
    return ('mirar %s (dirección %s)' % (DIRECCIONES[v], v)) if v in DIRECCIONES \
        else 'mirar en dirección %s' % v


def _tocando(v):
    return 'toca el borde' if v == 'borde' else 'toca el puntero del ratón' if v == 'puntero del ratón' \
        else 'toca a %s' % v


def _detener(v):
    return 'detener todo' if v == 'todos' else 'detener este programa'


# «si toca el borde» pero «repetir hasta que toque el borde»: las condiciones se escriben
# en indicativo y aquí se pasan a subjuntivo para los bloques que lo piden.
_SUBJ = [('toca ', 'toque '), ('está pulsad', 'esté pulsad'), ('está pulsado', 'esté pulsado'),
         ('es igual', 'sea igual'), ('es menor', 'sea menor'), ('es mayor', 'sea mayor'),
         ('no se cumple', 'no se cumpla')]


def _subjuntivo(cond):
    for a, b in _SUBJ:
        cond = cond.replace(a, b)
    return cond


# (tipo, patrón) -> frase. {h0}, {h1}… son los huecos por orden; {d0}, {d1}… los desplegables.
# Un valor puede ser una función que recibe la lista de huecos y desplegables ya en texto.
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
    ('stack', 'esperar _ segundos'): 'esperar {h0} segundos',
    ('stack', 'esperar hasta que _'): lambda h, d: 'esperar hasta que %s' % _subjuntivo(h[0]),
    # apariencia
    ('stack', 'decir _ durante _ segundos'): 'decir «{h0}» durante {h1} segundos',
    ('stack', 'decir _'): 'decir «{h0}»',
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
    ('stack', 'cambiar x por _'): 'desplazarse {h0} en horizontal (cambiar x)',
    ('stack', 'cambiar y por _'): 'desplazarse {h0} en vertical (cambiar y)',
    ('stack', 'fijar x a _'): 'ponerse en x: {h0}',
    ('stack', 'fijar y a _'): 'ponerse en y: {h0}',
    ('stack', 'si toca un borde, rebotar'): 'si toca un borde, dar la vuelta (rebotar)',
    ('stack', 'fijar estilo de rotación a []'): 'poner el estilo de rotación en «{d0}»',
    ('rep', 'posición x'): 'la posición x',
    ('rep', 'posición y'): 'la posición y',
    ('rep', 'dirección'): 'la dirección',
    # sensores
    ('stack', 'preguntar _ y esperar'): 'preguntar «{h0}» y esperar la respuesta',
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


def _hueco(h):
    tipo, v = h
    if tipo == 'lit':
        return str(v)
    if tipo == 'color':
        return str(v)
    if tipo in ('rep', 'bool'):
        return frase(v)
    return str(v)


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
        # texto del bloque con los valores puestos, para que al menos se entienda
        txt = patron
        for x in h:
            txt = txt.replace('_', x, 1)
        for d in drops:
            txt = txt.replace('[]', d, 1)
        return txt.replace('<bandera>', 'bandera verde')
    if callable(plantilla):
        return plantilla(h, drops)
    kw = {'h%d' % i: x for i, x in enumerate(h)}
    kw.update({'d%d' % i: x for i, x in enumerate(drops)})
    return plantilla.format(**kw)


def lineas(programa, nivel=0):
    """Lista de (nivel de sangría, frase) de un programa. Lo que cuelga de un sombrero va
    con una sangría más, como lo que va dentro de un bucle."""
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


# ------------------------------------------------------------------ los retos
# num -> dict(titulo, planteamiento, programa, comprueba). `programa` son tuplas como las de
# los gen_*.py; gen_sb3.py --retos las exporta a _soluciones/sb3/retos-t1.sb3.
RETOS = {
    5: dict(
        titulo='El coche teledirigido',
        objeto='el coche teledirigido',
        planteamiento='Un coche que avanza solo y que tú conduces con las flechas. Si toca el '
                      'borde del escenario, has perdido.',
        preparar=['Añade el coche: botón <strong>Elige un objeto</strong>, escribe <strong>Conv</strong> en el '
                  'buscador y elige <strong>Convertible 2</strong>, el coche verde.',
                  '<strong>Selecciónalo</strong> abajo a la derecha antes de arrastrar ningún bloque. '
                  'Este programa va en el coche, <strong>no</strong> en el gato ni en el perro.',
                  'Monta el programa de abajo, línea a línea.',
                  'Para probarlo, para todo con el <strong>círculo rojo</strong> y pulsa la tecla '
                  '<strong>C</strong>. No uses la bandera: la bandera arranca los programas del gato y del perro.'],
        programa=[
            ('hat', 'events', ['al presionar tecla', ('drop', 'c')]),
            ('stack', 'motion', ['ir a x:', ('num', '0'), 'y:', ('num', '0')]),
            ('stack', 'motion', ['apuntar en dirección', ('num', '90')]),
            ('c', 'control', ['repetir hasta que',
                              ('bool', 'sensing', ['¿tocando', ('drop', 'borde'), '?'])], [
                ('stack', 'motion', ['mover', ('num', '4'), 'pasos']),
                ('c', 'control', ['si', ('bool', 'sensing', ['¿tecla', ('drop', 'flecha izquierda'), 'presionada?']),
                                  'entonces'], [
                    ('stack', 'motion', ['girar', ('icon', 'giro-i'), ('num', '10'), 'grados'])]),
                ('c', 'control', ['si', ('bool', 'sensing', ['¿tecla', ('drop', 'flecha derecha'), 'presionada?']),
                                  'entonces'], [
                    ('stack', 'motion', ['girar', ('icon', 'giro-d'), ('num', '10'), 'grados'])]),
            ]),
            ('stack', 'looks', ['decir', ('txt', '¡Choque!'), 'durante', ('num', '2'), 'segundos']),
            ('cap', 'control', ['detener', ('drop', 'todos')]),
        ],
        comprueba='al pulsar C el coche sale del centro hacia la derecha y no se para; '
                  'con las flechas izquierda y derecha va girando mientras avanza, como un coche; '
                  'y en cuanto toca el borde dice «¡Choque!» y todo se detiene. Si aguantas más '
                  'de veinte segundos sin chocar, conduces bien. Y mientras tanto el gato y el '
                  'perro no se han movido.'),
}


def caja_reto(num, seccion=4):
    """El apartado N.3 de la sesión `num`, o '' si no tiene."""
    r = RETOS.get(num)
    if not r:
        return ''
    prep = ''.join('\n  <li><span class="p">Paso %d</span><span>%s</span></li>' % (i + 1, t)
                   for i, t in enumerate(r.get('preparar', [])))
    return ('<h3 class="sub"><span class="subn">%d.3</span>Monta %s a partir del texto</h3>\n'
            '<p>%s</p>\n<ol class="paso-lista">%s\n</ol>\n<p>%s</p>\n%s\n'
            '<p class="rp-ok"><b>Sabes que está bien si…</b> %s</p>'
            % (seccion, r['objeto'], r['planteamiento'], prep, INTRO, html_pseudo(r['programa']), r['comprueba']))

# -*- coding: utf-8 -*-
"""Generador de bloques de MakeCode (micro:bit) en SVG.

Es el hermano de `generadores-t1/scratchsvg.py`: mismo modelo de datos, pero con las
formas, los colores y la letra del editor MakeCode en español, medidos en el editor
real (ver `documentacion/COTEJO_MakeCode.md`). El resultado es un <svg> que se
incrusta directamente en el HTML, sin imágenes ni fuentes externas.

Diferencias con Scratch que importan al dibujar:
  - Los bloques de evento («al iniciar», «al presionarse el botón A», «para siempre»)
    son PLANOS por arriba, sin cúpula; sólo se distinguen porque no tienen muesca.
  - La letra es monoespaciada y seminegrita (Consolas/Monaco/Menlo en el editor).
  - Los reporters son píldoras más gordas; los booleanos, hexágonos de punta larga.
  - Los números y textos editables son píldoras blancas con borde gris.
  - Cada bloque lleva un borde más oscuro que su fondo.

Modelo de datos: cada bloque es una tupla
    ('hat',   categoria, partes, [hijos])           # evento: plano arriba, con boca
    ('stack', categoria, partes)                    # apilable
    ('c',     categoria, partes, [hijos])           # con una boca (repetir, si, mientras)
    ('ce',    categoria, partes, [hijos], partes2, [hijos2])   # si … si no
    ('cm',    categoria, [(partes, hijos), (partes, hijos), …]) # si … si no, si … si no
donde `partes` es una lista de:
    'texto llano'
    ('num',  '50')               píldora blanca editable (número)
    ('txt',  '¡Hola!')           píldora blanca editable (texto)
    ('drop', 'A')                desplegable (mismo color, más oscuro, con ▾)
    ('bool', categoria, partes)  entrada hexagonal (encaja un bloque booleano)
    ('rep',  categoria, partes)  reporter (variable, sensor, operación)
    ('grid', '.....:..#..:.....:..#..:.....')   rejilla 5×5 de «mostrar LEDs»
    ('hueco',)                   entrada vacía (hexágono hueco de un «si»)
"""

# ---------------------------------------------------------------- paleta
# (fondo, borde). El borde es el que pinta el editor.
COLOR = {
    'basico':     ('#1E90FF', '#176CBF'),
    'entrada':    ('#D400D4', '#9F009F'),
    'musica':     ('#E63022', '#B0251A'),
    'led':        ('#5C2D91', '#45226D'),
    'radio':      ('#E3008C', '#AA0069'),
    'bucles':     ('#00AA00', '#008000'),
    'logica':     ('#00A4A6', '#007B7D'),
    'variables':  ('#DC143C', '#A50F2D'),
    'matematica': ('#9400D3', '#6F009E'),
    'juego':      ('#007A4B', '#005B38'),
    'imagenes':   ('#7600A8', '#58007E'),
}

# ---------------------------------------------------------------- métrica
# El editor dibuja a 16 px de letra y 48 px de alto de bloque. Aquí se reduce a
# la misma escala que los bloques de Scratch de T1 (letra 13) para que las páginas
# de los dos trimestres pesen lo mismo a la vista.
F = 13            # tamaño de fuente
H = 38            # alto de un bloque apilable
R = 4             # radio de esquina
NX, NW, ND = 10, 10, 3.5   # muesca: x inicial, ancho del fondo, profundidad (rampas de 6)
NR = 6            # rampa de la muesca
PADX = 11         # margen interior
GAP = 7           # separación entre partes
CW = 13           # ancho de la columna izquierda de un bloque C
CFOOT = 20        # alto de la barra inferior de un bloque C
PADR = 10         # margen interior de un reporter
HREP = 30         # alto de un reporter / booleano
HNUM = 24         # alto de una píldora editable
FUENTE = "Consolas,Monaco,Menlo,'Ubuntu Mono','Liberation Mono',monospace"

# Medida real del texto con Liberation Mono Bold (0,6 em por carácter, como Menlo y
# Ubuntu Mono). Consolas es algo más estrecha: `lengthAdjust="spacing"` en cada
# <text> reparte la diferencia entre letras sin deformarlas.
_FUENTE_TTF = '/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf'
try:
    from PIL import ImageFont
    _FONT = ImageFont.truetype(_FUENTE_TTF, F)
except Exception:                                    # sin PIL: 0,6 em por carácter
    _FONT = None


def ancho_texto(t, f=F):
    if _FONT is not None:
        return _FONT.getlength(t) * f / F
    return len(t) * 0.6 * f


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


# ------------------------------------------------ atajos para escribir guiones
def rep(cat, *partes):
    return ('rep', cat, list(partes))


def var(nombre):
    """Reporter de variable (rojo)."""
    return ('rep', 'variables', [nombre])


def num(v):
    return ('num', str(v))


def drop(v):
    return ('drop', str(v))


def hexa(cat, *partes):
    return ('bool', cat, list(partes))


def boton(k='A'):
    """El booleano «botón A presionado» (Entrada)."""
    return ('bool', 'entrada', ['botón', ('drop', k), 'presionado'])


def compara(a, signo, b):
    """«a = b», «a < b», … (Lógica). a y b pueden ser partes o números."""
    def p(v):
        return v if isinstance(v, tuple) else ('num', str(v))
    return ('bool', 'logica', [p(a), ('drop', signo), p(b)])


def opera(a, signo, b):
    """«a + b», «a − b», … (Matemática)."""
    def p(v):
        return v if isinstance(v, tuple) else ('num', str(v))
    return ('rep', 'matematica', [p(a), ('drop', signo), p(b)])


def azar(a, b):
    return ('rep', 'matematica', ['escoger al azar de', ('num', str(a)), 'a', ('num', str(b))])


def sensor(nombre):
    """Reporter de Entrada sin desplegable: «nivel de luz», «temperatura (°C)»…"""
    return ('rep', 'entrada', [nombre])


# ---------------------------------------------------------------- partes
def medir_parte(p):
    if isinstance(p, str):
        return ancho_texto(p)
    tipo = p[0]
    if tipo in ('num', 'txt'):
        return max(28, ancho_texto(p[1]) + 16)
    if tipo == 'drop':
        return ancho_texto(p[1]) + 30
    if tipo == 'bool':
        return medir_partes(p[2]) + 2 * PADR + 2 * 12
    if tipo == 'hueco':
        return 36
    if tipo == 'rep':
        return medir_partes(p[2]) + 2 * PADR
    if tipo == 'grid':
        return 5 * 9 + 4 * 2 + 8
    raise ValueError(tipo)


def medir_partes(partes):
    if not partes:
        return 0
    return sum(medir_parte(p) for p in partes) + GAP * (len(partes) - 1)


def alto_partes(partes):
    """Un bloque con rejilla es más alto que uno normal."""
    if any(isinstance(p, tuple) and p[0] == 'grid' for p in partes):
        return 5 * 9 + 4 * 2 + 16
    return H


def _texto(x, ycen, t, out, clase='mc-t'):
    w = ancho_texto(t)
    out.append('<text x="%.1f" y="%.1f" class="%s" textLength="%.1f" '
               'lengthAdjust="spacing">%s</text>' % (x, ycen + 4.6, clase, w, esc(t)))
    return w


def dibujar_parte(p, x, ycen, cat, out):
    """Dibuja una parte y devuelve su anchura."""
    fondo, borde = COLOR[cat]
    if isinstance(p, str):
        return _texto(x, ycen, p, out)
    tipo = p[0]
    if tipo in ('num', 'txt'):
        w = max(28, ancho_texto(p[1]) + 16)
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" rx="%d" '
                   'fill="#FFFFFF" stroke="#BFBFBF" stroke-width="1"/>'
                   % (x, ycen - HNUM / 2, w, HNUM, HNUM // 2))
        out.append('<text x="%.1f" y="%.1f" class="mc-n">%s</text>'
                   % (x + w / 2, ycen + 4.3, esc(p[1])))
        return w
    if tipo == 'drop':
        w = ancho_texto(p[1]) + 30
        h = 24
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" rx="4" '
                   'fill="%s"/>' % (x, ycen - h / 2, w, h, borde))
        _texto(x + 8, ycen, p[1], out)
        tx = x + w - 14
        out.append('<path d="M%.1f %.1f l4.5 5.5 l4.5 -5.5 z" fill="#FFFFFF"/>'
                   % (tx, ycen - 2.5))
        return w
    if tipo == 'hueco':
        w, h, pk = 36, HREP - 6, 10
        y0 = ycen - h / 2
        out.append('<path d="M%.1f %.1f h%.1f l%d %.1f l-%d %.1f h-%.1f l-%d -%.1f z" '
                   'fill="%s" opacity=".55"/>'
                   % (x + pk, y0, w - 2 * pk, pk, h / 2, pk, h / 2, w - 2 * pk, pk, h / 2, borde))
        return w
    if tipo == 'bool':
        cb, partes = p[1], p[2]
        wi = medir_partes(partes)
        pk = 12                                  # punta del hexágono
        w = wi + 2 * PADR + 2 * pk
        h = HREP
        c2, o2 = COLOR[cb]
        y0 = ycen - h / 2
        out.append('<path d="M%.1f %.1f h%.1f l%d %.1f l-%d %.1f h-%.1f l-%d -%.1f z" '
                   'fill="%s" stroke="%s" stroke-width="1"/>'
                   % (x + pk, y0, w - 2 * pk, pk, h / 2, pk, h / 2, w - 2 * pk, pk, h / 2, c2, o2))
        xx = x + pk + PADR
        for q in partes:
            xx += dibujar_parte(q, xx, ycen, cb, out) + GAP
        return w
    if tipo == 'rep':
        cr, partes = p[1], p[2]
        w = medir_partes(partes) + 2 * PADR
        c2, o2 = COLOR[cr]
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" rx="%d" '
                   'fill="%s" stroke="%s" stroke-width="1"/>'
                   % (x, ycen - HREP / 2, w, HREP, HREP // 2, c2, o2))
        xx = x + PADR
        for q in partes:
            xx += dibujar_parte(q, xx, ycen, cr, out) + GAP
        return w
    if tipo == 'grid':
        return dibujar_grid(p[1], x, ycen, out)
    raise ValueError(tipo)


def dibujar_grid(patron, x, ycen, out, celda=9, sep=2):
    """Rejilla 5×5 dentro de «mostrar LEDs». `patron`: cinco filas separadas por
    ':' con '#' encendido y '.' apagado, como en el propio MakeCode."""
    filas = _filas(patron)
    lado = 5 * celda + 4 * sep
    x0, y0 = x + 4, ycen - lado / 2
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="#1F1F1F"/>'
               % (x0 - 3, y0 - 3, lado + 6, lado + 6))
    for j, fila in enumerate(filas):
        for i, c in enumerate(fila):
            on = c == '#'
            out.append('<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="1.5" fill="%s"/>'
                       % (x0 + i * (celda + sep), y0 + j * (celda + sep), celda, celda,
                          '#FFFFFF' if on else '#4A4A4A'))
    return lado + 8


def _filas(patron):
    filas = [f.strip() for f in patron.replace('\n', ':').split(':') if f.strip()]
    assert len(filas) == 5 and all(len(f) == 5 for f in filas), patron
    return filas


# ---------------------------------------------------------------- siluetas
def _muesca_arriba(x, y):
    return ('L%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f '
            % (x + NX, y, x + NX + NR, y + ND, x + NX + NR + NW, y + ND, x + NX + 2 * NR + NW, y))


def _muesca_abajo(x, y):
    """Borde inferior de derecha a izquierda, con la muesca saliente."""
    return ('L%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f '
            % (x + NX + 2 * NR + NW, y, x + NX + NR + NW, y + ND,
               x + NX + NR, y + ND, x + NX, y, x + R, y))


def silueta_multi(x, y, w, h_top, secciones, h_foot, muesca_arriba=True, muesca_abajo=True):
    """Bloque con cero o varias bocas.

    `secciones`: lista de (alto de la boca, alto de la barra que la sigue), la última
    barra es el pie de alto `h_foot`. Sin secciones es un bloque apilable normal.
    """
    d = ['M%.1f %.1f' % (x, y + R), 'Q%.1f %.1f %.1f %.1f' % (x, y, x + R, y)]
    if muesca_arriba:
        d.append(_muesca_arriba(x, y))
    d.append('L%.1f %.1f Q%.1f %.1f %.1f %.1f' % (x + w - R, y, x + w, y, x + w, y + R))
    cur = y + h_top
    for h_boca, h_bar in secciones:
        y2, y3 = cur, cur + h_boca
        d.append('L%.1f %.1f Q%.1f %.1f %.1f %.1f' % (x + w, y2 - R, x + w, y2, x + w - R, y2))
        # borde interior superior de la boca, con muesca hacia abajo
        d.append('L%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f'
                 % (x + CW + NX + 2 * NR + NW, y2, x + CW + NX + NR + NW, y2 + ND,
                    x + CW + NX + NR, y2 + ND, x + CW + NX, y2, x + CW + R, y2))
        d.append('Q%.1f %.1f %.1f %.1f' % (x + CW, y2, x + CW, y2 + R))
        d.append('L%.1f %.1f Q%.1f %.1f %.1f %.1f' % (x + CW, y3 - R, x + CW, y3, x + CW + R, y3))
        d.append('L%.1f %.1f Q%.1f %.1f %.1f %.1f' % (x + w - R, y3, x + w, y3, x + w, y3 + R))
        cur = y3 + h_bar
    y4 = cur                      # tras la última barra (el pie ya va en `secciones`)
    d.append('L%.1f %.1f Q%.1f %.1f %.1f %.1f' % (x + w, y4 - R, x + w, y4, x + w - R, y4))
    if muesca_abajo:
        d.append(_muesca_abajo(x, y4))
    else:
        d.append('L%.1f %.1f' % (x + R, y4))
    d.append('Q%.1f %.1f %.1f %.1f Z' % (x, y4, x, y4 - R))
    return ' '.join(d)


# ---------------------------------------------------------------- medida
def _secciones(b):
    """[(partes, hijos), …] de cualquier bloque con bocas."""
    if b[0] in ('hat', 'c'):
        return [(b[2], b[3])]
    if b[0] == 'ce':
        return [(b[2], b[3]), (b[4], b[5])]
    if b[0] == 'cm':
        return list(b[2])
    return []


def _hijos(b):
    out = []
    for _, hijos in _secciones(b):
        out += list(hijos)
    return out


def _alto_boca(hijos):
    return sum(alto_bloque(h) for h in hijos) or 22


def alto_bloque(b):
    if b[0] == 'stack':
        return alto_partes(b[2])
    secs = _secciones(b)
    total = 0
    for partes, hijos in secs:
        total += alto_partes(partes) + _alto_boca(hijos)
    return total + CFOOT


def ancho_bloque(b):
    if b[0] == 'stack':
        return medir_partes(b[2]) + 2 * PADX
    secs = _secciones(b)
    propio = max(medir_partes(p) for p, _ in secs) + 2 * PADX
    interior = max([ancho_bloque(h) for h in _hijos(b)], default=80)
    return max(propio, CW + interior + 8)


# ---------------------------------------------------------------- dibujo
def _fila(partes, x, ycen, cat, out):
    xx = x + PADX
    for p in partes:
        xx += dibujar_parte(p, xx, ycen, cat, out) + GAP


def _pila(hijos, x, y, out):
    yy = y
    for i, h in enumerate(hijos):
        yy += dibujar_bloque(h, x, yy, out, ultimo_de_c=(i == len(hijos) - 1))
    return yy


def dibujar_bloque(b, x, y, out, ultimo_de_c=False):
    """Dibuja el bloque en (x, y) y devuelve su altura."""
    tipo, cat = b[0], b[1]
    fondo, borde = COLOR[cat]
    w = ancho_bloque(b)

    if tipo == 'stack':
        h = alto_partes(b[2])
        out.append('<path d="%s" fill="%s" stroke="%s" stroke-width="1"/>'
                   % (silueta_multi(x, y, w, h, [], 0, True, not ultimo_de_c), fondo, borde))
        _fila(b[2], x, y + h / 2, cat, out)
        return h

    secs = _secciones(b)
    h_top = alto_partes(secs[0][0])
    bocas = []
    for i, (partes, hijos) in enumerate(secs):
        h_bar = alto_partes(secs[i + 1][0]) if i + 1 < len(secs) else CFOOT
        bocas.append((_alto_boca(hijos), h_bar))
    out.append('<path d="%s" fill="%s" stroke="%s" stroke-width="1"/>'
               % (silueta_multi(x, y, w, h_top, bocas, CFOOT,
                                muesca_arriba=(tipo != 'hat'),
                                muesca_abajo=(tipo != 'hat') and not ultimo_de_c),
                  fondo, borde))
    yy = y
    for partes, hijos in secs:
        hb = alto_partes(partes)
        _fila(partes, x, yy + hb / 2, cat, out)
        yy += hb
        yy = _pila(hijos, x + CW, yy, out) if hijos else yy + 22
    return alto_bloque(b)


def script_svg(bloques, titulo=None, pad=10, escala=1.0, extra_css=''):
    """Devuelve el <svg> completo de un script (uno o varios bloques sueltos)."""
    def ancho_total(b, base=0):
        m = base + ancho_bloque(b)
        for h in _hijos(b):
            m = max(m, ancho_total(h, base + CW))
        return m
    w = max(ancho_total(b) for b in bloques) + 2 * pad
    h = sum(alto_bloque(b) for b in bloques) + 2 * pad + ND
    out = []
    y = pad
    for b in bloques:
        y += dibujar_bloque(b, pad, y, out)
    css = ('.mc-t{font:600 %dpx %s;fill:#FFFFFF}'
           '.mc-n{font:600 %dpx %s;fill:#2B2B2B;text-anchor:middle}%s'
           % (F, FUENTE, F, FUENTE, extra_css))
    t = ('<title>%s</title>' % esc(titulo)) if titulo else ''
    rol = (' role="img" aria-label="%s"' % esc(titulo)) if titulo else ''
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %.0f %.0f" '
            'width="%.0f" height="%.0f" class="bloques"%s>%s<style>%s</style>%s</svg>'
            % (w, h, w * escala, h * escala, rol, t, css, ''.join(out)))


def scripts_svg(grupos, titulo=None, sep=14, pad=10):
    """Varios scripts independientes, uno debajo de otro, en un solo <svg>.
    `grupos` es una lista de listas de bloques (cada lista, un script)."""
    def ancho_total(b, base=0):
        m = base + ancho_bloque(b)
        for h in _hijos(b):
            m = max(m, ancho_total(h, base + CW))
        return m
    w = max(ancho_total(b) for g in grupos for b in g) + 2 * pad
    h = sum(sum(alto_bloque(b) for b in g) for g in grupos) + sep * (len(grupos) - 1) + 2 * pad + ND
    out = []
    y = pad
    for g in grupos:
        for b in g:
            y += dibujar_bloque(b, pad, y, out)
        y += sep
    css = ('.mc-t{font:600 %dpx %s;fill:#FFFFFF}'
           '.mc-n{font:600 %dpx %s;fill:#2B2B2B;text-anchor:middle}'
           % (F, FUENTE, F, FUENTE))
    t = ('<title>%s</title>' % esc(titulo)) if titulo else ''
    rol = (' role="img" aria-label="%s"' % esc(titulo)) if titulo else ''
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %.0f %.0f" '
            'width="%.0f" height="%.0f" class="bloques"%s>%s<style>%s</style>%s</svg>'
            % (w, h, w, h, rol, t, css, ''.join(out)))


# ---------------------------------------------------------------- la placa
def matriz_svg(patron='.....:.....:.....:.....:.....', titulo=None, coords=False,
               celda=22, sep=8, marcar=None):
    """La matriz 5×5 de la placa, con los LED como en la micro:bit real (rojos).

    `patron`: cinco filas de '#' y '.', separadas por ':'.
    `coords=True` rotula x=0…4 arriba e y=0…4 a la izquierda, como en el editor.
    `marcar`: lista de (x, y) que se rodean con un aro para señalarlos en el texto.
    """
    filas = _filas(patron)
    m = 26 if coords else 0
    lado = 5 * celda + 4 * sep
    W, Hh = lado + 2 * 14 + m, lado + 2 * 14 + m
    out = ['<rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="#2E2E2E"/>' % (m, m, lado + 28, lado + 28)]
    for j, fila in enumerate(filas):
        for i, c in enumerate(fila):
            cx = m + 14 + i * (celda + sep) + celda / 2
            cy = m + 14 + j * (celda + sep) + celda / 2
            on = c == '#'
            if on:
                out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#FF3B3B" opacity=".35"/>'
                           % (cx, cy, celda * 0.72))
            out.append('<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="3" fill="%s"/>'
                       % (cx - celda / 2, cy - celda / 2, celda, celda,
                          '#FF3B3B' if on else '#5A2626'))
            if marcar and (i, j) in marcar:
                out.append('<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="5" fill="none" '
                           'stroke="#FFD166" stroke-width="3"/>'
                           % (cx - celda / 2 - 4, cy - celda / 2 - 4, celda + 8, celda + 8))
    if coords:
        for i in range(5):
            cx = m + 14 + i * (celda + sep) + celda / 2
            out.append('<text x="%.1f" y="%d" class="mx-c">x=%d</text>' % (cx, m - 8, i))
            cy = m + 14 + i * (celda + sep) + celda / 2
            out.append('<text x="%d" y="%.1f" class="mx-c">y=%d</text>' % (m - 13, cy + 4, i))
    css = '.mx-c{font:700 12px %s;fill:#1B4F8A;text-anchor:middle}' % FUENTE
    t = ('<title>%s</title>' % esc(titulo)) if titulo else ''
    rol = (' role="img" aria-label="%s"' % esc(titulo)) if titulo else ''
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
            'class="matriz"%s>%s<style>%s</style>%s</svg>'
            % (W, Hh, W, Hh, rol, t, css, ''.join(out)))

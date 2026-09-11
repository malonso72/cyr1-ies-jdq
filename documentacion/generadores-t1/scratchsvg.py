# -*- coding: utf-8 -*-
"""Generador de bloques de Scratch 3 en SVG.

Dibuja un script de Scratch (sombrero + apilables + bloques C anidados) con las
formas y los colores oficiales de Scratch 3, sin usar imágenes ni fuentes
externas. El resultado es un <svg> que se incrusta directamente en el HTML.

Modelo de datos: cada bloque es una tupla
    ('hat',   categoria, partes)
    ('stack', categoria, partes)
    ('cap',   categoria, partes)                      # sin muesca inferior
    ('c',     categoria, partes, [hijos])             # bloque en C (repetir, si…)
    ('ce',    categoria, partes, [hijos], partes2, [hijos2])   # si … si no
donde `partes` es una lista de:
    'texto llano'
    ('num',  '50')               entrada ovalada blanca
    ('drop', 'espacio')          desplegable (mismo color, más oscuro, con ▾)
    ('bool', categoria, partes)  entrada hexagonal (encaja un bloque booleano)
    ('rep',  categoria, partes)  reporter ovalado (variable, operador, sensor)
    ('color', '#000000')         muestra de color
    ('icon', 'bandera' | 'giro-d' | 'giro-i')
"""

# ---------------------------------------------------------------- paleta
COLOR = {
    'motion':    ('#4C97FF', '#3373CC', '#3373CC'),
    'looks':     ('#9966FF', '#774DCB', '#774DCB'),
    'sound':     ('#CF63CF', '#BD42BD', '#BD42BD'),
    'events':    ('#FFBF00', '#CC9900', '#CC9900'),
    'control':   ('#FFAB19', '#CF8B17', '#CF8B17'),
    'sensing':   ('#5CB1D6', '#2E8EB8', '#2E8EB8'),
    'operators': ('#59C059', '#389438', '#389438'),
    'variables': ('#FF8C1A', '#DB6E00', '#DB6E00'),
}

# ---------------------------------------------------------------- métrica
F = 13            # tamaño de fuente de los bloques
H = 34            # alto de un bloque apilable
R = 6             # radio de esquina
NX, NW, ND = 14, 16, 4   # muesca: x inicial, ancho, profundidad
PADX = 12         # margen interior izquierdo/derecho
GAP = 7           # separación entre partes
CW = 14           # ancho de la columna izquierda de un bloque C
CFOOT = 18        # alto de la barra inferior de un bloque C
HATH = 18         # altura extra de la cúpula del sombrero
PADR = 9          # margen interior de un reporter ovalado
HREP = 24         # alto de un reporter ovalado
FUENTE = "'Helvetica Neue',Helvetica,Arial,'Liberation Sans',sans-serif"

# Medida real del texto. Liberation Sans Bold es métricamente idéntica a Arial,
# que es la fuente con la que el navegador va a componer estos bloques; así el
# ancho calculado aquí coincide con el que se verá en clase. `textLength` en cada
# <text> actúa además de red de seguridad si el navegador usa otra fuente.
_FUENTE_TTF = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
try:
    from PIL import ImageFont
    _FONT = ImageFont.truetype(_FUENTE_TTF, F)
except Exception:                                    # sin PIL: estimación burda
    _FONT = None


def ancho_texto(t, f=F):
    """Anchura del texto en negrita al tamaño f."""
    if _FONT is not None:
        return _FONT.getlength(t) * f / F
    return len(t) * 7.6 * f / 13.0


def esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


# ------------------------------------------------ atajos para escribir guiones
def rep(cat, *partes):
    """Reporter ovalado de la categoría indicada."""
    return ('rep', cat, list(partes))


def var(nombre):
    """Reporter de variable (naranja)."""
    return ('rep', 'variables', [nombre])


def op(*partes):
    """Reporter de operador (verde)."""
    return ('rep', 'operators', list(partes))


def hexa(cat, *partes):
    """Bloque booleano hexagonal."""
    return ('bool', cat, list(partes))


def tecla(k):
    """El booleano ¿tecla (…) presionada? — se usa en media docena de sesiones."""
    return ('bool', 'sensing', ['¿tecla', ('drop', k), 'presionada?'])


# ---------------------------------------------------------------- partes
def medir_parte(p):
    if isinstance(p, str):
        return ancho_texto(p)
    tipo = p[0]
    if tipo in ('num', 'txt'):
        return max(30, ancho_texto(p[1]) + 18)
    if tipo == 'drop':
        return ancho_texto(p[1]) + 32
    if tipo == 'icon':
        return 18
    if tipo == 'color':
        return 26
    if tipo == 'bool':
        return medir_partes(p[2]) + 34
    if tipo == 'rep':
        return medir_partes(p[2]) + 2 * PADR
    raise ValueError(tipo)


def medir_partes(partes):
    if not partes:
        return 0
    return sum(medir_parte(p) for p in partes) + GAP * (len(partes) - 1)


def dibujar_parte(p, x, ycen, cat, out):
    """Dibuja una parte y devuelve su anchura."""
    claro, oscuro, _ = COLOR[cat]
    if isinstance(p, str):
        w = ancho_texto(p)
        out.append('<text x="%.1f" y="%.1f" class="sb-t" textLength="%.1f" '
                   'lengthAdjust="spacingAndGlyphs">%s</text>'
                   % (x, ycen + 4.6, w, esc(p)))
        return w
    tipo = p[0]
    if tipo in ('num', 'txt'):
        w = max(30, ancho_texto(p[1]) + 18)
        h = 20
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" rx="%d" '
                   'fill="#FFFFFF"/>' % (x, ycen - h / 2, w, h, h // 2))
        out.append('<text x="%.1f" y="%.1f" class="sb-n">%s</text>'
                   % (x + w / 2, ycen + 4.3, esc(p[1])))
        return w
    if tipo == 'drop':
        w = ancho_texto(p[1]) + 32
        h = 22
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" rx="4" '
                   'fill="%s"/>' % (x, ycen - h / 2, w, h, oscuro))
        out.append('<text x="%.1f" y="%.1f" class="sb-t" textLength="%.1f" '
                   'lengthAdjust="spacingAndGlyphs">%s</text>'
                   % (x + 9, ycen + 4.4, ancho_texto(p[1]), esc(p[1])))
        tx = x + w - 15
        out.append('<path d="M%.1f %.1f l5 6 l5 -6 z" fill="#FFFFFF"/>'
                   % (tx, ycen - 3))
        return w
    if tipo == 'color':
        out.append('<rect x="%.1f" y="%.1f" width="20" height="20" rx="4" '
                   'fill="%s" stroke="#FFFFFF" stroke-width="2"/>'
                   % (x + 3, ycen - 10, p[1]))
        return 26
    if tipo == 'icon':
        w = 18
        if p[1] == 'bandera':
            out.append('<path d="M%.1f %.1f v14 M%.1f %.1f h11 l-2.5 3.5 l2.5 3.5 '
                       'h-11 z" fill="#4CBF56" stroke="#3EA149" stroke-width="1.2" '
                       'stroke-linejoin="round"/>' % (x + 2, ycen - 7, x + 2, ycen - 7))
        elif p[1] in ('giro-d', 'giro-i'):
            # arco de 270 grados con la punta de flecha en el extremo inferior
            cx, cy, r = x + 9, ycen - 1, 6.5
            if p[1] == 'giro-d':      # sentido de las agujas del reloj
                d = ('M%.1f %.1f A%.1f %.1f 0 1 1 %.1f %.1f'
                     % (cx - r, cy, r, r, cx, cy + r))
                tri = ('M%.1f %.1f L%.1f %.1f L%.1f %.1f z'
                       % (cx + 1.5, cy + r - 4.5, cx + 1.5, cy + r + 4.5, cx - 4, cy + r))
            else:                     # sentido contrario
                d = ('M%.1f %.1f A%.1f %.1f 0 1 0 %.1f %.1f'
                     % (cx + r, cy, r, r, cx, cy + r))
                tri = ('M%.1f %.1f L%.1f %.1f L%.1f %.1f z'
                       % (cx - 1.5, cy + r - 4.5, cx - 1.5, cy + r + 4.5, cx + 4, cy + r))
            out.append('<path d="%s" fill="none" stroke="#FFFFFF" stroke-width="2.2" '
                       'stroke-linecap="round"/>' % d)
            out.append('<path d="%s" fill="#FFFFFF"/>' % tri)
        return w
    if tipo == 'bool':
        cb, partes = p[1], p[2]
        wi = medir_partes(partes)
        w = wi + 34
        h = 24
        c2, o2, _ = COLOR[cb]
        y0 = ycen - h / 2
        # hexágono con las puntas hacia FUERA (así el pico no invade el texto)
        out.append('<path d="M%.1f %.1f l-9 %.1f l9 %.1f h%.1f l9 %.1f l-9 %.1f z" '
                   'fill="%s" stroke="%s" stroke-width="1"/>'
                   % (x + 9, y0, h / 2, h / 2, w - 18, -h / 2, -h / 2, c2, o2))
        xx = x + 17
        for q in partes:
            xx += dibujar_parte(q, xx, ycen, cb, out) + GAP
        return w
    if tipo == 'rep':
        cr, partes = p[1], p[2]
        w = medir_partes(partes) + 2 * PADR
        c2, o2, _ = COLOR[cr]
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" rx="%d" '
                   'fill="%s" stroke="%s" stroke-width="1"/>'
                   % (x, ycen - HREP / 2, w, HREP, HREP // 2, c2, o2))
        xx = x + PADR
        for q in partes:
            xx += dibujar_parte(q, xx, ycen, cr, out) + GAP
        return w
    raise ValueError(tipo)


# ---------------------------------------------------------------- siluetas
def _muesca_abajo(x, y, ancho):
    """Borde inferior de izquierda a derecha, con la muesca saliente."""
    return ('L%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f '
            % (x + NX + NW + 4, y, x + NX + NW, y + ND,
               x + NX + 4, y + ND, x + NX, y, x + R, y))


def silueta_stack(x, y, w, h, con_muesca_arriba=True, con_muesca_abajo=True):
    d = ['M%.1f %.1f' % (x, y + R)]
    d.append('Q%.1f %.1f %.1f %.1f' % (x, y, x + R, y))
    if con_muesca_arriba:
        d.append('L%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f '
                 % (x + NX, y, x + NX + 4, y + ND,
                    x + NX + NW, y + ND, x + NX + NW + 4, y))
    d.append('L%.1f %.1f' % (x + w - R, y))
    d.append('Q%.1f %.1f %.1f %.1f' % (x + w, y, x + w, y + R))
    d.append('L%.1f %.1f' % (x + w, y + h - R))
    d.append('Q%.1f %.1f %.1f %.1f' % (x + w, y + h, x + w - R, y + h))
    if con_muesca_abajo:
        d.append(_muesca_abajo(x, y + h, w))
    else:
        d.append('L%.1f %.1f' % (x + R, y + h))
    d.append('Q%.1f %.1f %.1f %.1f' % (x, y + h, x, y + h - R))
    d.append('Z')
    return ' '.join(d)


def silueta_hat(x, y, w, h):
    """Sombrero: cúpula arriba, muesca abajo. y es el borde superior de la cúpula."""
    yb = y + HATH               # donde empieza el cuerpo recto
    d = ['M%.1f %.1f' % (x, yb + h - R)]
    d.append('L%.1f %.1f' % (x, yb))
    d.append('C%.1f %.1f %.1f %.1f %.1f %.1f'
             % (x, y + 2, x + 26, y - 4, x + 42, y + 6))
    d.append('C%.1f %.1f %.1f %.1f %.1f %.1f'
             % (x + 52, y + 12, x + 60, yb, x + 72, yb))
    d.append('L%.1f %.1f' % (x + w - R, yb))
    d.append('Q%.1f %.1f %.1f %.1f' % (x + w, yb, x + w, yb + R))
    d.append('L%.1f %.1f' % (x + w, yb + h - R))
    d.append('Q%.1f %.1f %.1f %.1f' % (x + w, yb + h, x + w - R, yb + h))
    d.append(_muesca_abajo(x, yb + h, w))
    d.append('Q%.1f %.1f %.1f %.1f' % (x, yb + h, x, yb + h - R))
    d.append('Z')
    return ' '.join(d)


def silueta_multi(x, y, w, secciones, h_foot, con_muesca_abajo=True):
    """Bloque con una o varias bocas.

    `secciones` es una lista de pares (alto de la barra, alto de la boca).
    Un `repetir` tiene una sección; un `si … si no`, dos.
    """
    d = ['M%.1f %.1f' % (x, y + R)]
    d.append('Q%.1f %.1f %.1f %.1f' % (x, y, x + R, y))
    d.append('L%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f '
             % (x + NX, y, x + NX + 4, y + ND,
                x + NX + NW, y + ND, x + NX + NW + 4, y))
    d.append('L%.1f %.1f' % (x + w - R, y))
    d.append('Q%.1f %.1f %.1f %.1f' % (x + w, y, x + w, y + R))
    cur = y
    for h_bar, h_boca in secciones:
        y2 = cur + h_bar                  # inicio del hueco
        y3 = y2 + h_boca                  # fin del hueco
        d.append('L%.1f %.1f' % (x + w, y2 - R))
        d.append('Q%.1f %.1f %.1f %.1f' % (x + w, y2, x + w - R, y2))
        # borde interior superior del hueco (con muesca hacia abajo)
        d.append('L%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f'
                 % (x + CW + NX + NW + 4, y2, x + CW + NX + NW, y2 + ND,
                    x + CW + NX + 4, y2 + ND, x + CW + NX, y2, x + CW + R, y2))
        d.append('Q%.1f %.1f %.1f %.1f' % (x + CW, y2, x + CW, y2 + R))
        d.append('L%.1f %.1f' % (x + CW, y3 - R))
        d.append('Q%.1f %.1f %.1f %.1f' % (x + CW, y3, x + CW + R, y3))
        d.append('L%.1f %.1f' % (x + w - R, y3))
        d.append('Q%.1f %.1f %.1f %.1f' % (x + w, y3, x + w, y3 + R))
        cur = y3
    y4 = cur + h_foot
    d.append('L%.1f %.1f' % (x + w, y4 - R))
    d.append('Q%.1f %.1f %.1f %.1f' % (x + w, y4, x + w - R, y4))
    if con_muesca_abajo:
        d.append(_muesca_abajo(x, y4, w))
    else:
        d.append('L%.1f %.1f' % (x + R, y4))
    d.append('Q%.1f %.1f %.1f %.1f' % (x, y4, x, y4 - R))
    d.append('Z')
    return ' '.join(d)


def silueta_c(x, y, w, h_top, h_cuerpo, h_foot, con_muesca_abajo=True):
    return silueta_multi(x, y, w, [(h_top, h_cuerpo)], h_foot, con_muesca_abajo)


# ---------------------------------------------------------------- medida
def _hijos(b):
    """Todos los bloques hijos de b, en cualquiera de sus bocas."""
    if b[0] == 'c':
        return list(b[3])
    if b[0] == 'ce':
        return list(b[3]) + list(b[5])
    return []


def alto_bloque(b):
    if b[0] == 'hat':
        return HATH + H
    if b[0] in ('stack', 'cap'):
        return H
    if b[0] == 'c':
        cuerpo = sum(alto_bloque(h) for h in b[3]) or 24
        return H + cuerpo + CFOOT
    if b[0] == 'ce':
        c1 = sum(alto_bloque(h) for h in b[3]) or 24
        c2 = sum(alto_bloque(h) for h in b[5]) or 24
        return H + c1 + H + c2 + CFOOT
    raise ValueError(b[0])


def ancho_bloque(b):
    if b[0] == 'ce':
        propio = max(medir_partes(b[2]), medir_partes(b[4])) + 2 * PADX
        interior = max([ancho_bloque(h) for h in _hijos(b)], default=90)
        return max(propio, CW + interior)
    propio = medir_partes(b[2]) + 2 * PADX
    if b[0] == 'c':
        interior = max([ancho_bloque(h) for h in b[3]], default=90)
        return max(propio, CW + interior)
    return propio


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
    tipo, cat, partes = b[0], b[1], b[2]
    claro, oscuro, _ = COLOR[cat]
    w = ancho_bloque(b)

    if tipo == 'hat':
        out.append('<path d="%s" fill="%s"/>' % (silueta_hat(x, y, w, H), claro))
        _fila(partes, x, y + HATH + H / 2, cat, out)
        return HATH + H

    if tipo in ('stack', 'cap'):
        muesca = (tipo == 'stack') and not ultimo_de_c
        out.append('<path d="%s" fill="%s"/>'
                   % (silueta_stack(x, y, w, H, True, muesca), claro))
        _fila(partes, x, y + H / 2, cat, out)
        return H

    if tipo == 'c':
        cuerpo = sum(alto_bloque(h) for h in b[3]) or 24
        out.append('<path d="%s" fill="%s"/>'
                   % (silueta_multi(x, y, w, [(H, cuerpo)], CFOOT,
                                    con_muesca_abajo=not ultimo_de_c), claro))
        _fila(partes, x, y + H / 2, cat, out)
        _pila(b[3], x + CW, y + H, out)
        return H + cuerpo + CFOOT

    if tipo == 'ce':
        hijos1, partes2, hijos2 = b[3], b[4], b[5]
        c1 = sum(alto_bloque(h) for h in hijos1) or 24
        c2 = sum(alto_bloque(h) for h in hijos2) or 24
        out.append('<path d="%s" fill="%s"/>'
                   % (silueta_multi(x, y, w, [(H, c1), (H, c2)], CFOOT,
                                    con_muesca_abajo=not ultimo_de_c), claro))
        _fila(partes, x, y + H / 2, cat, out)
        _pila(hijos1, x + CW, y + H, out)
        _fila(partes2, x, y + H + c1 + H / 2, cat, out)
        _pila(hijos2, x + CW, y + H + c1 + H, out)
        return H + c1 + H + c2 + CFOOT

    raise ValueError(tipo)


def script_svg(bloques, titulo=None, pad=10, escala=1.0, extra_css=''):
    """Devuelve el <svg> completo de un script."""
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

    css = ('.sb-t{font:700 %dpx %s;fill:#FFFFFF}'
           '.sb-n{font:700 %dpx %s;fill:#575E75;text-anchor:middle}%s'
           % (F, FUENTE, F, FUENTE, extra_css))
    t = ('<title>%s</title>' % esc(titulo)) if titulo else ''
    rol = (' role="img" aria-label="%s"' % esc(titulo)) if titulo else ''
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %.0f %.0f" '
            'width="%.0f" height="%.0f" class="bloques"%s>%s<style>%s</style>%s</svg>'
            % (w, h, w * escala, h * escala, rol, t, css, ''.join(out)))

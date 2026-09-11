# -*- coding: utf-8 -*-
"""Diagramas SVG propios (no son bloques de Scratch): mapa del editor y rosa de
direcciones. Dibujados a mano para que se lean a media pantalla y no pesen."""
import math

FUENTE = "'Barlow',Helvetica,Arial,'Liberation Sans',sans-serif"


def _svg(w, h, cuerpo, alt, css=''):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
            'width="%d" height="%d" class="bloques" role="img" aria-label="%s">'
            '<title>%s</title><style>%s</style>%s</svg>'
            % (w, h, w, h, alt, alt, css, cuerpo))


def _gato(cx, cy, r, color='#F0A030'):
    """Silueta mínima de gato, para no depender de que el emoji tenga fuente."""
    def tri(x1, y1, x2, y2, x3, y3):
        return ('<path d="M%.1f %.1f L%.1f %.1f L%.1f %.1f z" fill="%s"/>'
                % (x1, y1, x2, y2, x3, y3, color))
    return (tri(cx - .92 * r, cy - .38 * r, cx - .70 * r, cy - 1.32 * r, cx - .10 * r, cy - .80 * r)
            + tri(cx + .92 * r, cy - .38 * r, cx + .70 * r, cy - 1.32 * r, cx + .10 * r, cy - .80 * r)
            + '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>' % (cx, cy, r, color)
            + '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#3A3A3A"/>' % (cx - .35 * r, cy - .10 * r, max(1.2, .13 * r))
            + '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#3A3A3A"/>' % (cx + .35 * r, cy - .10 * r, max(1.2, .13 * r)))


def mapa_editor():
    """Esquema de la pantalla de Scratch 3 con las cuatro zonas nombradas."""
    css = ('.z{fill:#FFFFFF;stroke:#C7D0DB;stroke-width:1.5}'
           '.lab{font:700 13.5px %s;fill:#1B4F8A}'
           '.sub{font:400 11.5px %s;fill:#5A6675}'
           '.tabon{font:700 11.5px %s;fill:#FFFFFF}'
           '.taboff{font:700 11.5px %s;fill:#3A4552}'
           '.num{font:700 12px %s;fill:#FFFFFF}' % ((FUENTE,) * 5))
    p = []
    a = p.append

    def badge(n, x, y, texto):
        a('<circle cx="%d" cy="%d" r="10" fill="#1B4F8A"/>' % (x, y))
        a('<text x="%d" y="%d" class="num" text-anchor="middle">%d</text>' % (x, y + 4, n))
        a('<text x="%d" y="%d" class="lab">%s</text>' % (x + 16, y + 5, texto))

    a('<rect x="4" y="4" width="692" height="424" rx="10" fill="#EEF2F7" '
      'stroke="#C7D0DB" stroke-width="2"/>')
    # barra de menú
    a('<rect x="14" y="14" width="672" height="30" rx="6" fill="#4C97FF"/>')
    a('<text x="26" y="34" class="tabon">Archivo</text>')
    a('<text x="88" y="34" class="tabon">Editar</text>')
    a('<text x="160" y="33" class="tabon" font-weight="400">'
      'Archivo → Guardar en tu ordenador (así entregas)</text>')
    # pestañas
    a('<rect x="14" y="52" width="86" height="26" rx="6" fill="#1B4F8A"/>')
    a('<text x="57" y="69" class="tabon" text-anchor="middle">Código</text>')
    a('<rect x="104" y="52" width="86" height="26" rx="6" fill="#FFFFFF" stroke="#C7D0DB"/>')
    a('<text x="147" y="69" class="taboff" text-anchor="middle">Disfraces</text>')
    a('<rect x="194" y="52" width="86" height="26" rx="6" fill="#FFFFFF" stroke="#C7D0DB"/>')
    a('<text x="237" y="69" class="taboff" text-anchor="middle">Sonidos</text>')

    # 1 · paleta
    a('<rect x="14" y="86" width="132" height="334" rx="8" class="z"/>')
    badge(1, 32, 106, 'Paleta')
    cats = [('#4C97FF', 'Movimiento'), ('#9966FF', 'Apariencia'), ('#CF63CF', 'Sonido'),
            ('#FFBF00', 'Eventos'), ('#FFAB19', 'Control'), ('#5CB1D6', 'Sensores'),
            ('#59C059', 'Operadores'), ('#FF8C1A', 'Variables'), ('#FF6680', 'Mis bloques')]
    for i, (c, t) in enumerate(cats):
        y = 138 + i * 27
        a('<circle cx="32" cy="%d" r="7" fill="%s"/>' % (y, c))
        a('<text x="46" y="%d" class="sub">%s</text>' % (y + 4, t))
    a('<circle cx="32" cy="399" r="9" fill="#E3E8EF"/>')
    a('<text x="32" y="404" class="lab" text-anchor="middle" font-size="14">+</text>')
    a('<text x="46" y="403" class="sub">Extensiones</text>')

    # 2 · área de código
    a('<rect x="154" y="86" width="244" height="334" rx="8" class="z"/>')
    badge(2, 172, 106, 'Área de código')
    a('<rect x="176" y="136" width="150" height="24" rx="6" fill="#FFBF00"/>')
    a('<rect x="176" y="164" width="118" height="24" rx="6" fill="#4C97FF"/>')
    a('<rect x="176" y="192" width="134" height="24" rx="6" fill="#9966FF"/>')
    a('<text x="176" y="252" class="sub">Aquí arrastras los bloques</text>')
    a('<text x="176" y="270" class="sub">y los encajas unos con otros.</text>')

    # 3 · escenario
    a('<rect x="406" y="86" width="280" height="200" rx="8" class="z"/>')
    badge(3, 424, 106, 'Escenario')
    a('<rect x="418" y="122" width="256" height="152" rx="4" fill="#F7FAFF" stroke="#DCE4EE"/>')
    a(_gato(546, 200, 17))
    a('<path d="M434 134 v14 M434 134 h11 l-2.5 3.5 l2.5 3.5 h-11 z" fill="#4CBF56" '
      'stroke="#3EA149" stroke-width="1.2" stroke-linejoin="round"/>')
    a('<circle cx="462" cy="141" r="7" fill="#EC5B5B"/>')
    a('<text x="478" y="145" class="sub">arrancar / parar</text>')

    # 4 · objetos
    a('<rect x="406" y="296" width="280" height="124" rx="8" class="z"/>')
    badge(4, 424, 316, 'Objetos')
    a('<rect x="418" y="332" width="64" height="66" rx="6" fill="#F0F6FF" '
      'stroke="#4C97FF" stroke-width="2"/>')
    a(_gato(450, 356, 14))
    a('<text x="450" y="390" class="sub" text-anchor="middle" font-size="10.5">Sprite1</text>')
    a('<text x="496" y="356" class="sub">Cada objeto tiene su</text>')
    a('<text x="496" y="372" class="sub">propia área de código.</text>')
    a('<circle cx="660" cy="392" r="16" fill="#4C97FF"/>')
    a(_gato(660, 392, 9, '#FFFFFF'))
    return _svg(700, 432, ''.join(p),
                'Esquema de la pantalla de Scratch: 1 la paleta de bloques con las nueve '
                'categorías, 2 el área de código en el centro, 3 el escenario arriba a la derecha '
                'con la bandera verde, y 4 la lista de objetos debajo, con Sprite1',
                css)


def rosa_direcciones():
    """Rosa de direcciones de Scratch: 0 arriba, 90 derecha, 180 abajo, −90 izquierda."""
    css = ('.d{font:700 15px %s;fill:#1B4F8A}'
           '.q{font:400 12px %s;fill:#5A6675}' % (FUENTE, FUENTE))
    cx, cy, r = 200, 168, 104
    p = []
    a = p.append
    a('<circle cx="%d" cy="%d" r="%d" fill="#F4F6F9" stroke="#C7D0DB" stroke-width="2"/>'
      % (cx, cy, r))
    for ang, etq, dx, dy, nota in [
            (0, '0', 0, -26, 'arriba'), (90, '90', 36, 4, 'derecha'),
            (180, '180', 0, 30, 'abajo'), (-90, '−90', -38, 4, 'izquierda')]:
        rad = math.radians(ang)
        x2 = cx + r * math.sin(rad)
        y2 = cy - r * math.cos(rad)
        a('<line x1="%d" y1="%d" x2="%.1f" y2="%.1f" stroke="#4C97FF" stroke-width="3" '
          'stroke-linecap="round"/>' % (cx, cy, x2, y2))
        a('<circle cx="%.1f" cy="%.1f" r="5" fill="#4C97FF"/>' % (x2, y2))
        a('<text x="%.1f" y="%.1f" class="d" text-anchor="middle">%s</text>'
          % (x2 + dx, y2 + dy, etq))
        a('<text x="%.1f" y="%.1f" class="q" text-anchor="middle">%s</text>'
          % (x2 + dx, y2 + dy + 15, nota))
    a('<circle cx="%d" cy="%d" r="20" fill="#FFFFFF" stroke="#C7D0DB" stroke-width="2"/>'
      % (cx, cy))
    a(_gato(cx, cy, 12))
    return _svg(400, 330, ''.join(p),
                'Rosa de direcciones de Scratch: 0 es hacia arriba, 90 hacia la derecha, '
                '180 hacia abajo y menos 90 hacia la izquierda', css)

# -*- coding: utf-8 -*-
"""Dibujos auxiliares de T2 que no son bloques ni la matriz."""
import math

FUENTE = "'Barlow','Helvetica Neue',Arial,sans-serif"


def rosa_brujula():
    """La brújula: 0° es el Norte, 90° el Este, 180° el Sur y 270° el Oeste, con los
    cuatro sectores que usa el reto (cada uno abarca 90° centrados en su punto)."""
    cx, cy, r = 190, 170, 118
    p = []
    a = p.append
    colores = ['#DCEBFA', '#FDF0D5', '#E4F4E4', '#F3E6F5']
    for i, (etq, ini) in enumerate([('N', 315), ('E', 45), ('S', 135), ('O', 225)]):
        a1, a2 = math.radians(ini - 90), math.radians(ini)   # 90° de arco
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        a('<path d="M%d %d L%.1f %.1f A%d %d 0 0 1 %.1f %.1f Z" fill="%s" stroke="#C7D0DB"/>'
          % (cx, cy, x1, y1, r, r, x2, y2, colores[i]))
    a('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="#9AA7B8" stroke-width="2"/>' % (cx, cy, r))
    for ang, etq in [(0, 'N'), (90, 'E'), (180, 'S'), (270, 'O')]:
        rad = math.radians(ang - 90)
        x, y = cx + (r + 22) * math.cos(rad), cy + (r + 22) * math.sin(rad)
        a('<text x="%.1f" y="%.1f" class="d">%s</text>' % (x, y + 6, etq))
        a('<text x="%.1f" y="%.1f" class="q">%d°</text>'
          % (cx + (r - 22) * math.cos(rad), cy + (r - 22) * math.sin(rad) + 4, ang))
    for ang in (45, 135, 225, 315):
        rad = math.radians(ang - 90)
        a('<line x1="%d" y1="%d" x2="%.1f" y2="%.1f" stroke="#9AA7B8" stroke-dasharray="4 3"/>'
          % (cx, cy, cx + r * math.cos(rad), cy + r * math.sin(rad)))
        a('<text x="%.1f" y="%.1f" class="q">%d°</text>'
          % (cx + (r + 16) * math.cos(rad), cy + (r + 16) * math.sin(rad) + 4, ang))
    # la placa en el centro, apuntando al norte
    a('<rect x="%d" y="%d" width="34" height="28" rx="4" fill="#2E2E2E"/>' % (cx - 17, cy - 14))
    a('<path d="M%d %d l-7 12 h14 z" fill="#FFD166"/>' % (cx, cy - 26))
    css = ('.d{font:700 18px %s;fill:#1B4F8A;text-anchor:middle}'
           '.q{font:400 12px %s;fill:#5A6675;text-anchor:middle}' % (FUENTE, FUENTE))
    alt = ('Rosa de la brújula: Norte 0 grados arriba, Este 90 a la derecha, Sur 180 abajo, '
           'Oeste 270 a la izquierda; cada punto abarca 90 grados centrados en él')
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 350" width="380" height="350" '
            'role="img" aria-label="%s" class="matriz"><title>%s</title><style>%s</style>%s</svg>'
            % (alt, alt, css, ''.join(p)))


def placa_svg():
    """La micro:bit V2 vista de frente, esquemática: matriz, botones, logo, micrófono,
    altavoz (detrás) y la regleta de pines con P0, P1, P2, 3V y GND."""
    p = []
    a = p.append
    W, H = 420, 340
    a('<rect x="10" y="10" width="400" height="300" rx="16" fill="#1F2A30" stroke="#0E1417" stroke-width="3"/>')
    # logo táctil
    a('<ellipse cx="210" cy="48" rx="26" ry="14" fill="none" stroke="#E6B422" stroke-width="4"/>')
    a('<circle cx="198" cy="48" r="4" fill="#E6B422"/><circle cx="222" cy="48" r="4" fill="#E6B422"/>')
    a('<text x="210" y="82" class="e">logo (se toca)</text>')
    # micrófono
    a('<circle cx="300" cy="48" r="5" fill="#8A97A0"/><text x="300" y="70" class="e">micrófono</text>')
    # matriz
    for j in range(5):
        for i in range(5):
            on = (i, j) in [(1, 1), (3, 1), (0, 3), (4, 3), (1, 4), (2, 4), (3, 4)]
            a('<rect x="%d" y="%d" width="18" height="18" rx="3" fill="%s"/>'
              % (152 + i * 29, 100 + j * 29, '#FF3B3B' if on else '#4A2222'))
    a('<text x="210" y="256" class="e">25 LEDs · también miden la luz y la temperatura</text>')
    # botones
    a('<rect x="40" y="140" width="52" height="52" rx="8" fill="#3A464D" stroke="#0E1417" stroke-width="2"/>')
    a('<circle cx="66" cy="166" r="14" fill="#10161A"/><text x="66" y="215" class="b">A</text>')
    a('<rect x="328" y="140" width="52" height="52" rx="8" fill="#3A464D" stroke="#0E1417" stroke-width="2"/>')
    a('<circle cx="354" cy="166" r="14" fill="#10161A"/><text x="354" y="215" class="b">B</text>')
    # pines
    for i, (x, w, etq) in enumerate([(22, 40, 'P0'), (102, 40, 'P1'), (182, 40, 'P2'), (262, 40, '3V'), (342, 40, 'GND')]):
        a('<rect x="%d" y="286" width="%d" height="24" rx="4" fill="#C9A227"/>' % (x, w))
        a('<text x="%d" y="328" class="e">%s</text>' % (x + w / 2, etq))
    a('<text x="210" y="276" class="e">pines: aquí van las pinzas de cocodrilo</text>')
    css = ('.e{font:600 12px %s;fill:#C9D3DA;text-anchor:middle}'
           '.b{font:700 16px %s;fill:#fff;text-anchor:middle}'
           '.d{font:600 11px %s;fill:#2E2E2E;text-anchor:middle}' % (FUENTE, FUENTE, FUENTE))
    alt = ('La placa micro:bit de frente: la matriz de 25 LEDs en el centro, los botones A y B a '
           'los lados, el logo táctil y el micrófono arriba, y la regleta de pines P0, P1, P2, '
           '3V y GND abajo; el acelerómetro, la brújula, la radio y el altavoz van por detrás')
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
            'role="img" aria-label="%s" class="matriz"><title>%s</title><style>%s</style>%s</svg>'
            % (W, H, W, H, alt, alt, css, ''.join(p)))


def mapa_makecode():
    """Esquema de la pantalla de MakeCode: simulador a la izquierda, caja de bloques en el
    centro, área de trabajo a la derecha, y la barra de abajo con Descargar y el nombre."""
    p = []
    a = p.append
    W, H = 760, 430
    a('<rect x="0" y="0" width="%d" height="%d" rx="12" fill="#F4F6F9" stroke="#C7D0DB"/>' % (W, H))
    a('<rect x="0" y="0" width="%d" height="44" rx="12" fill="#4B4F8B"/>' % W)
    a('<text x="20" y="28" class="t" fill="#fff">MakeCode · micro:bit</text>')
    a('<rect x="330" y="10" width="110" height="26" rx="13" fill="#fff"/><text x="385" y="28" class="s" fill="#4B4F8B">Bloques</text>')
    a('<rect x="450" y="10" width="110" height="26" rx="13" fill="#6C70A8"/><text x="505" y="28" class="s" fill="#fff">JavaScript</text>')
    # simulador
    a('<rect x="14" y="58" width="190" height="300" rx="10" fill="#E8ECF2" stroke="#C7D0DB"/>')
    a('<rect x="52" y="90" width="114" height="92" rx="8" fill="#1F2A30"/>')
    for j in range(5):
        for i in range(5):
            a('<rect x="%d" y="%d" width="10" height="10" rx="2" fill="%s"/>' % (86 + i * 12, 106 + j * 12, '#FF3B3B' if (i + j) % 3 == 0 else '#4A2222'))
    a('<circle cx="66" cy="136" r="6" fill="#3A464D"/><circle cx="152" cy="136" r="6" fill="#3A464D"/>')
    a('<text x="109" y="215" class="n">1 · Simulador</text>')
    a('<text x="109" y="236" class="m">la placa dibujada hace</text><text x="109" y="252" class="m">lo mismo que la de verdad</text>')
    # caja de bloques
    a('<rect x="216" y="58" width="150" height="300" rx="10" fill="#fff" stroke="#C7D0DB"/>')
    for i, (c, n) in enumerate([('#1E90FF', 'Básico'), ('#D400D4', 'Entrada'), ('#E63022', 'Música'), ('#5C2D91', 'LED'),
                                ('#E3008C', 'Radio'), ('#00AA00', 'Bucles'), ('#00A4A6', 'Lógica'), ('#DC143C', 'Variables'),
                                ('#9400D3', 'Matemática')]):
        y = 78 + i * 26
        a('<circle cx="236" cy="%d" r="7" fill="%s"/><text x="252" y="%d" class="c">%s</text>' % (y, c, y + 4, n))
    a('<text x="291" y="330" class="n">2 · Caja de bloques</text>')
    a('<text x="291" y="348" class="m">por colores, como en Scratch</text>')
    # área de trabajo
    a('<rect x="378" y="58" width="368" height="300" rx="10" fill="#fff" stroke="#C7D0DB"/>')
    a('<rect x="400" y="80" width="130" height="34" rx="4" fill="#1E90FF"/><text x="412" y="102" class="s" fill="#fff">al iniciar</text>')
    a('<rect x="412" y="114" width="150" height="34" rx="4" fill="#1E90FF"/><text x="424" y="136" class="s" fill="#fff">mostrar ícono</text>')
    a('<rect x="400" y="148" width="130" height="14" rx="4" fill="#1E90FF"/>')
    a('<rect x="400" y="190" width="140" height="34" rx="4" fill="#1E90FF"/><text x="412" y="212" class="s" fill="#fff">para siempre</text>')
    a('<rect x="412" y="224" width="120" height="34" rx="4" fill="#1E90FF"/><text x="424" y="246" class="s" fill="#fff">pausa (ms)</text>')
    a('<rect x="400" y="258" width="140" height="14" rx="4" fill="#1E90FF"/>')
    a('<text x="562" y="330" class="n">3 · Área de trabajo</text>')
    a('<text x="562" y="348" class="m">aquí se encajan los bloques</text>')
    # barra inferior
    a('<rect x="14" y="372" width="190" height="42" rx="8" fill="#4B4F8B"/><text x="109" y="398" class="s" fill="#fff">⬇ Descargar</text>')
    a('<rect x="216" y="372" width="250" height="42" rx="8" fill="#fff" stroke="#C7D0DB"/><text x="230" y="398" class="s" fill="#8A97A0">Reto1_TuNombre</text>')
    a('<text x="600" y="398" class="n">4 · Descargar y el nombre</text>')
    css = ('.t{font:700 15px %s}.s{font:600 13px %s}.n{font:700 14px %s;fill:#1B4F8A;text-anchor:middle}'
           '.m{font:400 12px %s;fill:#5A6675;text-anchor:middle}.c{font:600 12px %s;fill:#333}'
           % (FUENTE, FUENTE, FUENTE, FUENTE, FUENTE))
    alt = ('Esquema de la pantalla de MakeCode: a la izquierda el simulador con la placa dibujada, '
           'en el centro la caja de bloques por colores, a la derecha el área de trabajo con los '
           'bloques encajados, y abajo el botón Descargar y la casilla del nombre del proyecto')
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
            'role="img" aria-label="%s" class="matriz"><title>%s</title><style>%s</style>%s</svg>'
            % (W, H, W, H, alt, alt, css, ''.join(p)))

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

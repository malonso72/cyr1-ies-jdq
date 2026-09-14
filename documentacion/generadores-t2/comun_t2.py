# -*- coding: utf-8 -*-
"""Utilidades compartidas por los generadores de T2 · micro:bit."""
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, '..', '..'))
T2 = os.path.join(REPO, 'trimestres', 't2-microbit') + os.sep
DESTINO = os.path.join(T2, 'retos') + os.sep


def escribir(nombre, html):
    """Escribe retos/<nombre>.html (r01…r15 troncal, a01…a12 ampliación, m01…m03 sin material)."""
    ruta = os.path.join(DESTINO, '%s.html' % nombre)
    os.makedirs(DESTINO, exist_ok=True)
    open(ruta, 'w', encoding='utf-8').write(html)
    print('  %-10s %6d bytes' % (nombre + '.html', len(html)))


def escribir_t2(nombre, html):
    """Escribe una página en la raíz del trimestre (index.html, presentacion.html)."""
    ruta = os.path.join(T2, nombre)
    open(ruta, 'w', encoding='utf-8').write(html)
    print('  %-18s %6d bytes' % (nombre, len(html)))

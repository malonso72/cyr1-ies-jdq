# -*- coding: utf-8 -*-
"""Utilidades compartidas por los generadores de sesiones de T1."""
import os

# Rutas relativas a este archivo: el taller vive en documentacion/generadores-t1/
AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, '..', '..'))
T1 = os.path.join(REPO, 'trimestres', 't1-scratch') + os.sep
DESTINO = os.path.join(T1, 'sesiones') + os.sep

# Página del cuadernillo que corresponde a cada sesión (verificado con pdftotext).
# S12-S20 no tienen equivalente: usan las guías de juegos o son proyecto final.
CUADERNILLO = {1: 4, 2: 7, 3: 9, 4: 10, 5: 11, 6: 12,
               7: 13, 8: 14, 9: 15, 10: 16, 11: 17}

GUIA = '../materiales/guias-juegos/'


def escribir(num, html):
    ruta = os.path.join(DESTINO, 's%02d.html' % num)
    os.makedirs(DESTINO, exist_ok=True)
    open(ruta, 'w', encoding='utf-8').write(html)
    print('  s%02d.html  %6d bytes' % (num, len(html)))


# Las tres bases del proyecto final viven en trimestres/t1-scratch/juegos/
DESTINO_JUEGOS = os.path.join(T1, 'juegos') + os.sep


def escribir_juego(slug, html):
    ruta = os.path.join(DESTINO_JUEGOS, '%s.html' % slug)
    os.makedirs(DESTINO_JUEGOS, exist_ok=True)
    open(ruta, 'w', encoding='utf-8').write(html)
    print('  %-16s %6d bytes' % (slug + '.html', len(html)))

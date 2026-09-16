# -*- coding: utf-8 -*-
"""Arreglos de las páginas de T3 que ha encontrado test_academia.js.
De un solo uso: las páginas de T3 están escritas a mano, no se generan."""
import os
import re
import sys

REPO = sys.argv[1] if len(sys.argv) > 1 else '.'
T3 = os.path.join(REPO, 'trimestres', 't3-ciberseguridad')
SITIO = 'https://cyr1-ies-jdq.malonso72.workers.dev/'
AC = ' Academia Cyber-IES · CyR 1.º ESO · IES Jiménez de Quesada.'

DESCRIPCIONES = {
    's09-reto-piensa.html':
        'Escape room de la sesión 9: seis mensajes sospechosos llegados al instituto, para '
        'identificar en cada uno la técnica psicológica que usa y la frase que lo delata.' + AC,
    's11-reto-wifi.html':
        'Reto de la sesión 11: dos escenarios de wifi público abierto y dos test para decidir '
        'qué se puede hacer en una red así y qué queda al descubierto.' + AC,
    's12-reto-ciberacoso.html':
        'Reto de la sesión 12: acompañar a Marcos en una historia de ciberacoso decidiendo en '
        'cada momento qué hacer —no responder, guardar pruebas, bloquear, contarlo—.' + AC,
    's12alt-reto-dpo.html':
        'Reto alternativo de la sesión 12: un tribunal digital con ocho casos de derecho al '
        'olvido, para decidir si Google debe borrar o no esa información.' + AC,
    's13-reto-lucia.html':
        'Reto de la sesión 13: examinar las publicaciones de Lucía y averiguar cuántos datos '
        'personales se deducen de ellas antes de emitir el veredicto (OSINT).' + AC,
    's14-reto-realfake.html':
        'Torneo de la sesión 14: diez casos de vídeo, audio y foto para votar si son reales o '
        'deepfakes y justificar la decisión con la señal que lo delata.' + AC,
    's15-reto-detective.html':
        'Reto de la sesión 15: la mesa del detective, con las pruebas del caso de Antonio '
        'Hernández, para reconstruir cómo le robaron las credenciales.' + AC,
    's16-reto-vbucks.html':
        'Tienda falsa de V-Bucks: una simulación de clase del IES Jiménez de Quesada, no una '
        'tienda real y sin relación con Epic Games, para aprender a detectar una estafa antes '
        'de picar.' + AC,
    's17-reto-marta.html':
        'Reto de la sesión 17: la carpeta del investigador del caso de Marta Ruiz, una estafa '
        'que encadenó correo falso, suplantación telefónica y voz clonada.' + AC,
    's18-reto-examen.html':
        'Examen del analista, sesión 18: doce preguntas de repaso que recorren todo el bloque '
        'de ciberseguridad, de la sesión 1 a la 17.' + AC,
}

# La tienda falsa de V-Bucks no lleva pie ni se indexa: el pie con el nombre del instituto
# destriparía la simulación, y una página que imita a una tienda real no debe salir en Google.
SIN_PIE = {'s16-reto-vbucks.html'}
PIE = ('<footer style="text-align:center;padding:26px 14px 40px;opacity:.75;font-size:.85rem">'
       'IES Jiménez de Quesada · Santa Fe (Granada) · Manuel Alonso Herrera</footer>\n')

cambios = []


def guardar(ruta, txt, que):
    open(ruta, 'w', encoding='utf-8').write(txt)
    cambios.append('%-34s %s' % (os.path.basename(ruta), que))


def url_de(ruta):
    rel = os.path.relpath(ruta, REPO).replace(os.sep, '/')
    return SITIO + rel


def paginas():
    for base, _, ficheros in os.walk(T3):
        if '_legacy-v2' in base:
            continue
        for f in sorted(ficheros):
            if f.endswith('.html'):
                yield os.path.join(base, f)


for ruta in paginas():
    s = open(ruta, encoding='utf-8').read()
    original = s
    hechos = []
    nombre = os.path.basename(ruta)

    # 1) canonical, detrás del <title>, como en T1 y T2
    if 'rel="canonical"' not in s:
        s = re.sub(r'(</title>)',
                   r'\1\n<link rel="canonical" href="' + url_de(ruta) + '">', s, count=1)
        hechos.append('canonical')

    # 2) descripción de los retos
    if nombre in DESCRIPCIONES and 'name="description"' not in s:
        s = re.sub(r'(<link rel="canonical"[^>]*>)',
                   r'\1\n<meta name="description" content="' + DESCRIPCIONES[nombre] + '">',
                   s, count=1)
        hechos.append('description')

    # 3) la tienda falsa, fuera de los buscadores
    if nombre in SIN_PIE and 'name="robots"' not in s:
        s = re.sub(r'(<link rel="canonical"[^>]*>)',
                   r'\1\n<meta name="robots" content="noindex">', s, count=1)
        hechos.append('noindex')

    # 4) pie en los retos que no lo tenían
    if '/retos/' in ruta.replace(os.sep, '/') and nombre not in SIN_PIE and '<footer' not in s:
        s = s.replace('</body>', PIE + '</body>', 1)
        hechos.append('pie')

    if s != original:
        guardar(ruta, s, ', '.join(hechos))

# 5) etiquetas accesibles de los campos de S01 y S02
ETIQUETAS = [
    (os.path.join(T3, 'sesiones', 's01.html'),
     '<input type="text" id="lab-pwd-input" placeholder',
     '<input type="text" id="lab-pwd-input" aria-label="Tu contraseña de prueba para el laboratorio" placeholder'),
    (os.path.join(T3, 'sesiones', 's02.html'),
     '<input type="text" id="pwd-guardian-input" placeholder',
     '<input type="text" id="pwd-guardian-input" aria-label="Contraseña que propones para Sofía" placeholder'),
    (os.path.join(T3, 'sesiones', 's02.html'),
     '<input type="number" id="num-cuentas" min="0" max="50" placeholder',
     '<input type="number" id="num-cuentas" min="0" max="50" aria-label="Número de cuentas que tienes" placeholder'),
    (os.path.join(T3, 'sesiones', 's02.html'),
     '<input type="number" id="num-reutilizadas" min="0" max="50" placeholder',
     '<input type="number" id="num-reutilizadas" min="0" max="50" aria-label="Número de esas cuentas con la misma contraseña" placeholder'),
    (os.path.join(T3, 'sesiones', 's02.js'),
     "'<input type=\"text\" id=\"pwd-sof-' + i + '\" placeholder",
     "'<input type=\"text\" id=\"pwd-sof-' + i + '\" aria-label=\"Intento ' + i + ' de 5: contraseña que Sofía usaría\" placeholder"),
]
for ruta, viejo, nuevo in ETIQUETAS:
    s = open(ruta, encoding='utf-8').read()
    if nuevo in s:
        continue
    assert s.count(viejo) == 1, 'no encaja una sola vez en %s: %s' % (ruta, viejo)
    guardar(ruta, s.replace(viejo, nuevo), 'aria-label')

# 6) el hub del trimestre no tenía skip-link
hub = os.path.join(T3, 'index.html')
s = open(hub, encoding='utf-8').read()
if 'skip-link' not in s:
    m = re.search(r'<body[^>]*>', s)
    s = (s[:m.end()] + '\n<a href="#main-content" class="skip-link">Saltar al contenido '
         'principal</a>' + s[m.end():])
    guardar(hub, s, 'skip-link')

# 7) la tienda falsa sale del sitemap: no debe indexarse
sitemap = os.path.join(REPO, 'sitemap.xml')
s = open(sitemap, encoding='utf-8').read()
fuera = re.sub(r'\s*<url>(?:(?!</url>).)*s16-reto-vbucks\.html(?:(?!</url>).)*</url>', '', s, flags=re.S)
if fuera != s:
    guardar(sitemap, fuera, 'fuera s16-reto-vbucks (noindex)')

print('\n'.join(cambios) if cambios else 'nada que cambiar')
print('\n%d ficheros tocados' % len(cambios))

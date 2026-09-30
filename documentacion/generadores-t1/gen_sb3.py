# -*- coding: utf-8 -*-
"""Las tres bases del proyecto final como proyectos de Scratch de verdad (.sb3), y una
comprobación de que todos los programas dibujados en las 21 sesiones cargan en Scratch.

    python3 gen_sb3.py            # escribe _soluciones/sb3/{arkanoid,space-invaders,esquivar}.sb3
    python3 gen_sb3.py --todos    # además, /tmp/_todos_los_programas.sb3 para test_sb3.js

Los .sb3 van a `_soluciones/` (privada, no se despliega): son los juegos montados, y es
Manuel quien decide cuándo y a quién se los da (subiéndolos a Moodle, por ejemplo).

Los programas son los mismos que dibujan gen_proyectos.py y gen_s??.py: no se copian, se
importan. Los disfraces son esquemáticos (sb3.py) y los sonidos «Pop» y «Miau» son tonos
sintetizados con esos nombres, porque el taller no tiene acceso a la biblioteca de Scratch.
"""
import copy
import importlib
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comun
import scratchsvg
import plantilla
from sb3 import Objeto, DISFRACES, wav_pop, wav_miau, proyecto, escribir_sb3

# Importar los generadores sin que escriban las páginas ni dibujen nada.
_recogidos = []
_orig_svg = scratchsvg.script_svg


def _espia(bloques, titulo=None, **kw):
    _recogidos.append((titulo, bloques))
    return _orig_svg(bloques, titulo, **kw)


scratchsvg.script_svg = _espia
plantilla.script_svg = _espia
comun.escribir = lambda *a, **k: None
comun.escribir_juego = lambda *a, **k: None
gp = importlib.import_module('gen_proyectos')

POP = wav_pop()
MIAU = wav_miau()


def en_posicion(script, x, y):
    """Copia del script con el primer «ir a x: _ y: _» apuntando a (x, y): así cada
    ladrillo o marciano duplicado arranca en su sitio, que es lo que la página pide hacer
    a mano tras duplicar."""
    s = copy.deepcopy(script)

    def visita(bloques):
        for b in bloques:
            if b[0] == 'stack' and b[2][:1] == ['ir a x:'] and b[2][1][0] == 'num':
                b[2][1] = ('num', str(x))
                b[2][3] = ('num', str(y))
                return True
            for hijos in ([b[3]] if b[0] == 'c' else [b[3], b[5]] if b[0] == 'ce' else []):
                if visita(hijos):
                    return True
        return False
    visita(s)
    return s


def arkanoid():
    ladrillos = []
    n = 0
    for y in (120, 90):
        for x in (-160, -80, 0, 80, 160):
            n += 1
            ladrillos.append(Objeto('Ladrillo%d' % n, [DISFRACES['ladrillo']],
                                    [en_posicion(gp.A_LADRILLO, x, y)], x=x, y=y, sonidos=[POP]))
    objetos = [Objeto('Pelota', [DISFRACES['pelota']], [gp.A_PELOTA, gp.A_REBOTE, gp.A_GANAR],
                      x=0, y=-100, tamano=50, sonidos=[POP]),
               Objeto('Pala', [DISFRACES['pala']], [gp.A_PALA], x=0, y=-140)] + ladrillos
    return proyecto(objetos)


def space_invaders():
    marcianos = []
    for i in range(8):
        x = -150 + i * 43
        marcianos.append(Objeto('Marciano%d' % (i + 1), [DISFRACES['marciano']],
                                [en_posicion(gp.B_MARCIANO, x, 120), gp.B_VAIVEN],
                                x=x, y=120, tamano=60, sonidos=[POP]))
    objetos = [Objeto('Nave', [DISFRACES['nave']], [gp.B_NAVE, gp.B_RELOJ, gp.B_GANAR],
                      x=0, y=-150, tamano=50),
               Objeto('Bala', [DISFRACES['bala']], [gp.B_BALA_INI, gp.B_BALA], x=0, y=-130,
                      visible=False)] + marcianos
    return proyecto(objetos, variables_iniciales={'Tiempo': 60})


def esquivar():
    piedras = [Objeto('Piedra%d' % (i + 1), [DISFRACES['piedra']], [gp.C_PIEDRA],
                      x=-120 + 120 * i, y=160, tamano=40, sonidos=[POP]) for i in range(3)]
    objetos = [Objeto('Jugador', [DISFRACES['jugador']], [gp.C_JUGADOR, gp.C_RELOJ, gp.C_FIN],
                      x=0, y=-140, tamano=40)] + piedras
    return proyecto(objetos, variables_iniciales={'Vidas': 3})


def todos_los_programas():
    """Un proyecto con un objeto por cada programa dibujado en las sesiones y las bases:
    sólo para comprobar que todos cargan en Scratch."""
    for mod in ('gen_s01_s05', 'gen_s06_s11', 'gen_s12_s16', 'gen_s17_depuracion', 'gen_s18_s21'):
        importlib.import_module(mod)
    objetos = []
    for i, (titulo, bloques) in enumerate(_recogidos):
        objetos.append(Objeto('P%02d' % (i + 1), [DISFRACES['gato']], [bloques],
                              sonidos=[POP, MIAU]))
    return proyecto(objetos), len(_recogidos)


def reto(num):
    """El programa del apartado N.3 de la sesión `num` (la versión arreglada, si la hay), en el
    objeto de la biblioteca que dice pseudocodigo.SPRITES. Disfraces y sonidos esquemáticos con
    los nombres que usa el programa. En la S12 van además el gato y una pared negra, porque el
    fantasma los necesita para hacer lo que dice el enunciado."""
    import pseudocodigo as P
    from sb3 import svg_costume, _svg
    r = P.RETOS[num]
    progs = r.get('solucion', r['programas'])
    objetos = []
    for (et, prog), nombre in zip(progs, P.SPRITES[num]):
        sonidos = []
        def visita(bloques):
            for b in bloques:
                for parte in b[2]:
                    if isinstance(parte, tuple) and parte[0] == 'drop' and b[1] == 'sound':
                        if parte[1] not in [x['name'] for x in sonidos]:
                            sonidos.append(wav_pop(parte[1]))
                if b[0] in ('c', 'ce'):
                    visita(b[3])
                if b[0] == 'ce':
                    visita(b[5])
        visita(prog)
        x = {1: -150, 11: -120 if nombre == 'Referee' else 120, 12: 0}.get(num, 0)
        objetos.append(Objeto(nombre, [DISFRACES['pelota'], DISFRACES['piedra']], [copy.deepcopy(prog)],
                              x=x, y=0, sonidos=sonidos))
    if num == 12:
        pared = svg_costume(_svg(20, 200, '<rect width="20" height="200" fill="#1A1A1A"/>'), 'pared', 10, 100)
        objetos.append(Objeto('Pared', [pared], [], x=150, y=0))
        objetos.append(Objeto('Sprite1', [DISFRACES['gato']], [], x=-150, y=0))
    return proyecto(objetos)


if __name__ == '__main__':
    destino = os.path.join(comun.REPO, '_soluciones', 'sb3')
    os.makedirs(destino, exist_ok=True)
    for slug, fn in (('arkanoid', arkanoid), ('space-invaders', space_invaders), ('esquivar', esquivar)):
        pj, assets = fn()
        n = escribir_sb3(os.path.join(destino, slug + '.sb3'), pj, assets)
        print('  %-20s %6d bytes · %d objetos' % (slug + '.sb3', n, len(pj['targets']) - 1))
    if '--todos' in sys.argv:
        (pj, assets), n = todos_los_programas()
        ruta = os.path.join(sys.argv[-1] if os.path.isdir(sys.argv[-1]) else '/tmp', '_todos_los_programas.sb3')
        escribir_sb3(ruta, pj, assets)
        print('  %s · %d programas' % (ruta, n))
    if '--retos' in sys.argv:
        import pseudocodigo as P
        dr = os.path.join(destino, 'retos')
        os.makedirs(dr, exist_ok=True)
        for num in sorted(P.RETOS):
            pj, assets = reto(num)
            escribir_sb3(os.path.join(dr, 's%02d-apartado3.sb3' % num), pj, assets)
        print('  %s · %d programas del apartado N.3' % (dr, len(P.RETOS)))

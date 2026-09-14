# -*- coding: utf-8 -*-
"""Atajos para escribir programas de MakeCode con los nombres exactos del editor
en español (ver documentacion/COTEJO_MakeCode.md). Si un bloque no está aquí, se
busca en el cotejo antes de inventarlo."""
from makecodesvg import num, drop, var, rep, hexa, azar, sensor, compara, opera  # noqa: F401


def _p(v):
    """Un número suelto se convierte en píldora; una parte se deja como está."""
    if isinstance(v, tuple):
        return v
    return ('num', str(v))


# --- Básico ------------------------------------------------------------------
def INICIAR(hijos):
    return ('hat', 'basico', ['al iniciar'], hijos)


def SIEMPRE(hijos):
    return ('hat', 'basico', ['para siempre'], hijos)


def ICONO(nombre):
    return ('stack', 'basico', ['mostrar ícono', drop(nombre)])


def CADENA(texto):
    return ('stack', 'basico', ['mostrar cadena', ('txt', texto)])


def NUMERO(v):
    return ('stack', 'basico', ['mostrar número', _p(v)])


def LEDS(patron):
    return ('stack', 'basico', ['mostrar LEDs', ('grid', patron)])


def PAUSA(ms):
    return ('stack', 'basico', ['pausa (ms)', _p(ms)])


def FLECHA(d):
    return ('stack', 'basico', ['mostrar flecha', drop(d)])


BORRAR = ('stack', 'basico', ['borrar la pantalla'])


# --- Entrada -----------------------------------------------------------------
def BOTON(k, hijos):
    return ('hat', 'entrada', ['al presionarse el botón', drop(k)], hijos)


def GESTO(g, hijos):
    """«si agitado»: así se lee en el editor el evento del acelerómetro."""
    return ('hat', 'entrada', ['si', drop(g)], hijos)


LUZ = sensor('nivel de luz')
TEMPERATURA = sensor('temperatura (°C)')
BRUJULA = sensor('dirección de la brújula (°)')
SONIDO = sensor('nivel de sonido')


def ROTACION(eje='timbre'):
    return ('rep', 'entrada', ['rotación (°)', drop(eje)])


# --- LED ---------------------------------------------------------------------
def GRAFICAR(x, y):
    return ('stack', 'led', ['graficar x', _p(x), 'y', _p(y)])


def OCULTAR(x, y):
    return ('stack', 'led', ['ocultar x', _p(x), 'y', _p(y)])


def INVERTIR(x, y):
    return ('stack', 'led', ['invertir x', _p(x), 'y', _p(y)])


def BRILLO(v):
    return ('stack', 'led', ['ajustar brillo', _p(v)])


# --- Variables ---------------------------------------------------------------
def FIJAR(nombre, valor):
    return ('stack', 'variables', ['fijar', drop(nombre), 'a', _p(valor)])


def CAMBIAR(nombre, valor):
    return ('stack', 'variables', ['cambiar', drop(nombre), 'por', _p(valor)])


# --- Lógica ------------------------------------------------------------------
VERDADERO = ('rep', 'logica', ['verdadero'])
FALSO = ('rep', 'logica', ['falso'])


def SI(cond, hijos):
    return ('c', 'logica', ['si', cond, 'entonces'], hijos)


def SINO(cond, hijos, hijos2):
    return ('ce', 'logica', ['si', cond, 'entonces'], hijos, ['si no'], hijos2)


def CASCADA(ramas, sino=None):
    """si … / si no, si … / si no. `ramas` es [(cond, hijos), …]."""
    secs = []
    for i, (cond, hijos) in enumerate(ramas):
        secs.append((['si' if i == 0 else 'si no, si', cond, 'entonces'], hijos))
    if sino is not None:
        secs.append((['si no'], sino))
    return ('cm', 'logica', secs)


def Y(a, b):
    return ('bool', 'logica', [a, drop('y'), b])


def O(a, b):
    return ('bool', 'logica', [a, drop('o'), b])


# --- Bucles ------------------------------------------------------------------
def PARA(indice, hasta, hijos):
    return ('c', 'bucles', ['para', drop(indice), 'de 0 a', _p(hasta), 'ejecutar'], hijos)


def REPETIR(veces, hijos):
    return ('c', 'bucles', ['repetir', _p(veces), 'veces ejecutar'], hijos)


def MIENTRAS(cond, hijos):
    return ('c', 'bucles', ['mientras', cond, 'ejecutar'], hijos)


# --- Matemática --------------------------------------------------------------
def ABSOLUTO(v):
    return ('rep', 'matematica', ['absoluto de', _p(v)])


def INTERVALO(v, a, b, c, d):
    return ('rep', 'matematica', ['ajustar intervalo', _p(v), 'de', _p(a), 'hasta', _p(b),
                                  'a intervalo de', _p(c), 'hasta', _p(d)])


# --- Radio -------------------------------------------------------------------
def GRUPO(n):
    return ('stack', 'radio', ['radio establecer grupo', _p(n)])


def ENVIAR(n):
    return ('stack', 'radio', ['radio enviar número', _p(n)])


def ENVIAR_VALOR(nombre, v):
    return ('stack', 'radio', ['radio enviar valor', ('txt', nombre), '=', _p(v)])


def RECIBIR(hijos):
    return ('hat', 'radio', ['al recibir radio', var('receivedNumber')], hijos)


def RECIBIR_VALOR(hijos):
    return ('hat', 'radio', ['al recibir radio', var('name'), var('value')], hijos)


RECIBIDO = var('receivedNumber')


# --- Juego -------------------------------------------------------------------
def SPRITE(x, y):
    return ('rep', 'juego', ['crear sprite en x:', _p(x), 'y:', _p(y)])


def SP_CAMBIAR(nombre, prop, v):
    return ('stack', 'juego', [var(nombre), 'cambiar', drop(prop), 'por', _p(v)])


def SP_FIJAR(nombre, prop, v):
    return ('stack', 'juego', [var(nombre), 'establecer', drop(prop), 'en', _p(v)])


def SP_PROP(nombre, prop):
    return ('rep', 'juego', [var(nombre), drop(prop)])


def SP_TOCA(a, b):
    return ('bool', 'juego', ['esta', var(a), 'tocando', var(b)])


def SP_BORDE(nombre):
    return ('bool', 'juego', [var(nombre), 'tocando el borde'])


def SP_ELIMINAR(nombre):
    return ('stack', 'juego', ['eliminar', var(nombre)])


def PUNTOS(v=1):
    return ('stack', 'juego', ['agregar puntos a la puntuación actual', _p(v)])


PUNTUACION = ('rep', 'juego', ['puntuación'])
FIN_JUEGO = ('stack', 'juego', ['fin del juego'])


# --- Música ------------------------------------------------------------------
def TONO(hz):
    return ('stack', 'musica', ['tono de timbre (Hz)', _p(hz)])


PARAR_SONIDOS = ('stack', 'musica', ['para todos los sonidos'])

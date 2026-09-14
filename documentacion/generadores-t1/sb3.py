# -*- coding: utf-8 -*-
"""Exportador a .sb3: convierte los programas escritos como tuplas (los mismos que dibuja
`scratchsvg.py`) en un proyecto de Scratch 3 de verdad.

Un .sb3 es un zip con `project.json` y los archivos de disfraces y sonidos. Aquí se
generan los dos: el JSON a partir de las tuplas, y unos disfraces SVG y un sonido WAV
sintetizado, porque desde el taller no hay acceso a la biblioteca de Scratch.

Modelo de entrada: el de scratchsvg —
    ('hat'|'stack'|'cap', categoria, partes)
    ('c', categoria, partes, [hijos])
    ('ce', categoria, partes, [hijos], partes2, [hijos2])
Un `Objeto` reúne varios scripts, sus disfraces, sus sonidos y su posición inicial.

Cada bloque se reconoce por su texto (con los huecos sustituidos por `_`), así que los
nombres tienen que ser los del COTEJO, igual que para dibujarlos. Si un texto no está en
la tabla TABLA, `compilar` lanza KeyError con el patrón: es a propósito.
"""
import hashlib
import io
import json
import math
import struct
import zipfile

# ---------------------------------------------------------------- tabla de bloques
# patrón → (opcode, [nombres de las entradas en orden], extra)
# Las entradas se emparejan con los huecos del patrón en orden. `extra` describe campos
# fijos, menús-sombra y el tipo de sombra de cada entrada.
N, P, W, A, T = 'num', 'pos', 'whole', 'angle', 'text'   # tipos de sombra numérica/texto

TABLA = {
    # eventos
    ('hat', 'al hacer clic en <bandera>'): ('event_whenflagclicked', [], {}),
    ('hat', 'al recibir []'): ('event_whenbroadcastreceived', [], {'campo_broadcast': 'BROADCAST_OPTION'}),
    ('stack', 'enviar []'): ('event_broadcast', [], {'input_broadcast': 'BROADCAST_INPUT'}),
    # control
    ('c', 'por siempre'): ('control_forever', [], {}),
    ('c', 'repetir _'): ('control_repeat', [('TIMES', W)], {}),
    ('c', 'repetir hasta que _'): ('control_repeat_until', [('CONDITION', 'bool')], {}),
    ('c', 'si _ entonces'): ('control_if', [('CONDITION', 'bool')], {}),
    ('ce', 'si _ entonces'): ('control_if_else', [('CONDITION', 'bool')], {}),
    ('cap', 'detener []'): ('control_stop', [], {'campo': ('STOP_OPTION', {'todos': 'all', 'este programa': 'this script'}),
                                                'mutation': {'tagName': 'mutation', 'children': [], 'hasnext': 'false'}}),
    ('stack', 'esperar _ segundos'): ('control_wait', [('DURATION', P)], {}),
    ('stack', 'esperar hasta que _'): ('control_wait_until', [('CONDITION', 'bool')], {}),
    # apariencia
    ('stack', 'cambiar disfraz a []'): ('looks_switchcostumeto', [], {'menu': ('COSTUME', 'looks_costume', 'COSTUME')}),
    ('stack', 'cambiar fondo a []'): ('looks_switchbackdropto', [], {'menu': ('BACKDROP', 'looks_backdrops', 'BACKDROP')}),
    ('stack', 'siguiente disfraz'): ('looks_nextcostume', [], {}),
    ('stack', 'decir _ durante _ segundos'): ('looks_sayforsecs', [('MESSAGE', T), ('SECS', N)], {}),
    ('stack', 'decir _'): ('looks_say', [('MESSAGE', T)], {}),
    ('stack', 'esconder'): ('looks_hide', [], {}),
    ('stack', 'mostrar'): ('looks_show', [], {}),
    ('stack', 'fijar tamaño al _ %'): ('looks_setsizeto', [('SIZE', N)], {}),
    # movimiento
    ('stack', 'mover _ pasos'): ('motion_movesteps', [('STEPS', N)], {}),
    ('stack', 'girar <giro-d> _ grados'): ('motion_turnright', [('DEGREES', N)], {}),
    ('stack', 'girar <giro-i> _ grados'): ('motion_turnleft', [('DEGREES', N)], {}),
    ('stack', 'apuntar en dirección _'): ('motion_pointindirection', [('DIRECTION', A)], {}),
    ('stack', 'ir a x: _ y: _'): ('motion_gotoxy', [('X', N), ('Y', N)], {}),
    ('stack', 'cambiar x por _'): ('motion_changexby', [('DX', N)], {}),
    ('stack', 'cambiar y por _'): ('motion_changeyby', [('DY', N)], {}),
    ('stack', 'fijar x a _'): ('motion_setx', [('X', N)], {}),
    ('stack', 'fijar y a _'): ('motion_sety', [('Y', N)], {}),
    ('stack', 'si toca un borde, rebotar'): ('motion_ifonedgebounce', [], {}),
    ('stack', 'fijar estilo de rotación a []'): ('motion_setrotationstyle', [], {'campo': ('STYLE', {
        'izquierda-derecha': 'left-right', 'no rotar': "don't rotate", 'en todas direcciones': 'all around'})}),
    ('rep', 'posición x'): ('motion_xposition', [], {}),
    ('rep', 'posición y'): ('motion_yposition', [], {}),
    ('rep', 'dirección'): ('motion_direction', [], {}),
    # sensores
    ('stack', 'preguntar _ y esperar'): ('sensing_askandwait', [('QUESTION', T)], {}),
    ('stack', 'reiniciar cronómetro'): ('sensing_resettimer', [], {}),
    ('rep', 'respuesta'): ('sensing_answer', [], {}),
    ('rep', 'cronómetro'): ('sensing_timer', [], {}),
    ('rep', 'posición x del ratón'): ('sensing_mousex', [], {}),
    ('rep', 'posición y del ratón'): ('sensing_mousey', [], {}),
    ('bool', '¿tecla [] presionada?'): ('sensing_keypressed', [], {'menu': ('KEY_OPTION', 'sensing_keyoptions', 'KEY_OPTION', {
        'espacio': 'space', 'flecha derecha': 'right arrow', 'flecha izquierda': 'left arrow',
        'flecha arriba': 'up arrow', 'flecha abajo': 'down arrow', 'cualquiera': 'any'})}),
    ('bool', '¿tocando [] ?'): ('sensing_touchingobject', [], {'menu': ('TOUCHINGOBJECTMENU', 'sensing_touchingobjectmenu', 'TOUCHINGOBJECTMENU', {
        'borde': '_edge_', 'puntero del ratón': '_mouse_'})}),
    ('bool', '¿tocando el color _ ?'): ('sensing_touchingcolor', [('COLOR', 'color')], {}),
    # sonido
    ('stack', 'iniciar sonido []'): ('sound_play', [], {'menu': ('SOUND_MENU', 'sound_sounds_menu', 'SOUND_MENU')}),
    ('stack', 'tocar sonido [] hasta que termine'): ('sound_playuntildone', [], {'menu': ('SOUND_MENU', 'sound_sounds_menu', 'SOUND_MENU')}),
    # variables
    ('stack', 'dar a [] el valor _'): ('data_setvariableto', [('VALUE', T)], {'campo_var': 'VARIABLE'}),
    ('stack', 'sumar a [] _'): ('data_changevariableby', [('VALUE', N)], {'campo_var': 'VARIABLE'}),
    ('stack', 'mostrar variable []'): ('data_showvariable', [], {'campo_var': 'VARIABLE'}),
    ('stack', 'esconder variable []'): ('data_hidevariable', [], {'campo_var': 'VARIABLE'}),
    # operadores
    ('rep', '_ + _'): ('operator_add', [('NUM1', N), ('NUM2', N)], {}),
    ('rep', '_ - _'): ('operator_subtract', [('NUM1', N), ('NUM2', N)], {}),
    ('rep', '_ * _'): ('operator_multiply', [('NUM1', N), ('NUM2', N)], {}),
    ('rep', '_ / _'): ('operator_divide', [('NUM1', N), ('NUM2', N)], {}),
    ('rep', 'número aleatorio entre _ y _'): ('operator_random', [('FROM', N), ('TO', N)], {}),
    ('rep', 'unir _ _'): ('operator_join', [('STRING1', T), ('STRING2', T)], {}),
    ('bool', '_ < _'): ('operator_lt', [('OPERAND1', T), ('OPERAND2', T)], {}),
    ('bool', '_ = _'): ('operator_equals', [('OPERAND1', T), ('OPERAND2', T)], {}),
    ('bool', '_ > _'): ('operator_gt', [('OPERAND1', T), ('OPERAND2', T)], {}),
    ('bool', '_ y _'): ('operator_and', [('OPERAND1', 'bool'), ('OPERAND2', 'bool')], {}),
    ('bool', '_ o _'): ('operator_or', [('OPERAND1', 'bool'), ('OPERAND2', 'bool')], {}),
    ('bool', 'no _'): ('operator_not', [('OPERAND', 'bool')], {}),
}

SOMBRA = {N: 4, P: 5, W: 6, A: 8, 'color': 9, T: 10}


def _patron(partes):
    """Texto del bloque con los huecos como `_`, los desplegables como `[]`, los iconos
    como `<nombre>` y las muestras de color como `#`. Devuelve también la lista de huecos."""
    trozos, huecos, drops = [], [], []
    for p in partes:
        if isinstance(p, str):
            trozos.append(p)
        elif p[0] in ('num', 'txt'):
            trozos.append('_'); huecos.append(('lit', p[1]))
        elif p[0] == 'drop':
            trozos.append('[]'); drops.append(p[1])
        elif p[0] == 'icon':
            trozos.append('<%s>' % p[1])
        elif p[0] == 'color':
            trozos.append('_'); huecos.append(('color', p[1]))
        elif p[0] in ('rep', 'bool'):
            trozos.append('_'); huecos.append((p[0], p))
        else:
            raise ValueError(p)
    return ' '.join(trozos), huecos, drops


class _Ids:
    def __init__(self):
        self.n = 0

    def __call__(self, pref='b'):
        self.n += 1
        return '%s%d' % (pref, self.n)


class Compilador:
    """Convierte scripts de un objeto en el diccionario `blocks` de Scratch 3."""

    def __init__(self, variables, broadcasts):
        self.variables = variables      # nombre → id (globales, en el escenario)
        self.broadcasts = broadcasts    # nombre → id
        self.ids = _Ids()
        self.blocks = {}

    # ---- entradas
    def _entrada(self, hueco, tipo, parent):
        """Devuelve el valor JSON de una entrada a partir de un hueco."""
        clase, valor = hueco
        if tipo == 'bool':
            if clase != 'bool':
                raise ValueError('hace falta un booleano: %r' % (valor,))
            bid = self._bloque(valor, parent)
            return [2, bid]
        if clase == 'lit':
            return [1, [SOMBRA[tipo], str(valor)]]
        if clase == 'color':
            return [1, [9, valor]]
        # reporter dentro de un hueco con sombra
        sombra = [SOMBRA[tipo], '' if tipo == T else '0']
        if valor[0] == 'rep' and valor[1] == 'variables' and len(valor[2]) == 1 and isinstance(valor[2][0], str):
            nombre = valor[2][0]
            return [3, [12, nombre, self._var(nombre)], sombra]
        bid = self._bloque(valor, parent)
        return [3, bid, sombra]

    def _var(self, nombre):
        if nombre not in self.variables:
            self.variables[nombre] = 'var_' + hashlib.md5(nombre.encode()).hexdigest()[:10]
        return self.variables[nombre]

    def _bc(self, nombre):
        if nombre not in self.broadcasts:
            self.broadcasts[nombre] = 'bc_' + hashlib.md5(nombre.encode()).hexdigest()[:10]
        return self.broadcasts[nombre]

    def _menu(self, parent, spec, valor):
        """Bloque-sombra de menú (disfraz, tecla, objeto tocado, sonido…)."""
        input_name, opcode, field, *mapa = spec
        v = mapa[0].get(valor, valor) if mapa else valor
        mid = self.ids('m')
        self.blocks[mid] = {'opcode': opcode, 'next': None, 'parent': parent, 'inputs': {},
                            'fields': {field: [v, None]}, 'shadow': True, 'topLevel': False}
        return input_name, [1, mid]

    # ---- bloques
    def _bloque(self, b, parent, next_id=None):
        tipo, cat, partes = b[0], b[1], b[2]
        pat, huecos, drops = _patron(partes)
        clave = (tipo, pat)
        if tipo in ('rep', 'bool') and cat == 'variables' and clave not in TABLA:
            raise ValueError('una variable suelta se resuelve en _entrada: %r' % (b,))
        if clave not in TABLA:
            raise KeyError('bloque sin traducir: %r' % (clave,))
        opcode, entradas, extra = TABLA[clave]
        bid = self.ids()
        blk = {'opcode': opcode, 'next': next_id, 'parent': parent, 'inputs': {}, 'fields': {},
               'shadow': False, 'topLevel': parent is None}
        self.blocks[bid] = blk
        # entradas por orden
        hi = 0
        for nombre, t in entradas:
            blk['inputs'][nombre] = self._entrada(huecos[hi], t, bid)
            hi += 1
        # campos y menús
        if 'campo' in extra:
            f, mapa = extra['campo']
            blk['fields'][f] = [mapa.get(drops[0], drops[0]), None]
        if 'campo_var' in extra:
            blk['fields'][extra['campo_var']] = [drops[0], self._var(drops[0])]
        if 'campo_broadcast' in extra:
            blk['fields'][extra['campo_broadcast']] = [drops[0], self._bc(drops[0])]
        if 'input_broadcast' in extra:
            blk['inputs'][extra['input_broadcast']] = [1, [11, drops[0], self._bc(drops[0])]]
        if 'menu' in extra:
            nombre, valor = self._menu(bid, extra['menu'], drops[0])
            blk['inputs'][nombre] = valor
        if 'mutation' in extra:
            blk['mutation'] = extra['mutation']
        # bocas
        if tipo in ('c', 'ce'):
            sub = self._pila(b[3], bid)
            if sub:
                blk['inputs']['SUBSTACK'] = [2, sub]
            if tipo == 'ce':
                sub2 = self._pila(b[5], bid)
                if sub2:
                    blk['inputs']['SUBSTACK2'] = [2, sub2]
        return bid

    def _pila(self, hijos, parent):
        """Encadena una lista de bloques; devuelve el id del primero (o None)."""
        prev = None
        first = None
        for h in hijos:
            bid = self._bloque(h, parent if prev is None else prev)
            if prev is None:
                first = bid
            else:
                self.blocks[prev]['next'] = bid
            prev = bid
        return first

    def script(self, bloques, x=0, y=0):
        """Un script completo: el primero es el sombrero (o un bloque suelto)."""
        first = self._pila(bloques, None)
        if first:
            self.blocks[first]['topLevel'] = True
            self.blocks[first]['x'] = x
            self.blocks[first]['y'] = y
        return first


# ---------------------------------------------------------------- disfraces y sonidos
def _md5(data):
    return hashlib.md5(data).hexdigest()


def svg_costume(svg, nombre, cx, cy):
    """Un disfraz SVG con su centro de rotación (en píxeles del SVG)."""
    data = svg.encode('utf-8')
    return {'name': nombre, 'dataFormat': 'svg', 'assetId': _md5(data), 'md5ext': _md5(data) + '.svg',
            'rotationCenterX': cx, 'rotationCenterY': cy, '_data': data}


def wav_pop(nombre='Pop', dur=0.09, f0=900, f1=300, rate=22050):
    """Un «pop» corto sintetizado: seno que baja de f0 a f1 con envolvente decreciente."""
    n = int(rate * dur)
    frames = bytearray()
    for i in range(n):
        t = i / rate
        f = f0 + (f1 - f0) * (i / n)
        env = (1 - i / n) ** 2
        v = int(0.8 * 32767 * env * math.sin(2 * math.pi * f * t))
        frames += struct.pack('<h', v)
    data = (b'RIFF' + struct.pack('<I', 36 + len(frames)) + b'WAVEfmt ' +
            struct.pack('<IHHIIHH', 16, 1, 1, rate, rate * 2, 2, 16) +
            b'data' + struct.pack('<I', len(frames)) + bytes(frames))
    return {'name': nombre, 'dataFormat': 'wav', 'assetId': _md5(data), 'md5ext': _md5(data) + '.wav',
            'rate': rate, 'sampleCount': n, '_data': data}


def wav_miau(nombre='Miau'):
    """No es un maullido: es un tono doble más largo. Se llama Miau para que el bloque
    «iniciar sonido Miau» de las sesiones lo encuentre."""
    return wav_pop(nombre, dur=0.35, f0=600, f1=450)


# --- disfraces del proyecto final (esquemáticos, a tamaño «100 %») ---
def _svg(w, h, cuerpo):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">%s</svg>'
            % (w, h, w, h, cuerpo))


DISFRACES = {
    'pelota': svg_costume(_svg(40, 40, '<circle cx="20" cy="20" r="19" fill="#FFB000" stroke="#7A5200" stroke-width="2"/>'
                                     '<circle cx="14" cy="13" r="5" fill="#FFE080"/>'), 'pelota', 20, 20),
    'pala': svg_costume(_svg(120, 18, '<rect x="1" y="1" width="118" height="16" rx="8" fill="#4C97FF" stroke="#2C5FA8" stroke-width="2"/>'), 'pala', 60, 9),
    'ladrillo': svg_costume(_svg(60, 24, '<rect x="1" y="1" width="58" height="22" rx="3" fill="#E25B4A" stroke="#8C2E22" stroke-width="2"/>'
                                         '<line x1="30" y1="1" x2="30" y2="23" stroke="#8C2E22" stroke-width="2"/>'), 'ladrillo', 30, 12),
    'nave': svg_costume(_svg(80, 60, '<polygon points="40,2 78,56 40,44 2,56" fill="#59C059" stroke="#2B7A2B" stroke-width="2"/>'
                                     '<circle cx="40" cy="36" r="6" fill="#DFF5DF"/>'), 'nave', 40, 30),
    'bala': svg_costume(_svg(10, 24, '<rect x="2" y="1" width="6" height="22" rx="3" fill="#FFD166" stroke="#9A7500" stroke-width="1.5"/>'), 'bala', 5, 12),
    'marciano': svg_costume(_svg(60, 50, '<ellipse cx="30" cy="28" rx="27" ry="18" fill="#9966FF" stroke="#5A34B0" stroke-width="2"/>'
                                         '<circle cx="20" cy="26" r="5" fill="#fff"/><circle cx="40" cy="26" r="5" fill="#fff"/>'
                                         '<circle cx="21" cy="27" r="2.5" fill="#000"/><circle cx="41" cy="27" r="2.5" fill="#000"/>'
                                         '<line x1="30" y1="10" x2="30" y2="2" stroke="#5A34B0" stroke-width="3"/><circle cx="30" cy="2" r="3" fill="#FF6680"/>'), 'marciano', 30, 25),
    'jugador': svg_costume(_svg(70, 90, '<circle cx="35" cy="20" r="16" fill="#FFCC99" stroke="#8A5A2B" stroke-width="2"/>'
                                        '<rect x="15" y="38" width="40" height="50" rx="10" fill="#5CB1D6" stroke="#2E7FA0" stroke-width="2"/>'), 'jugador', 35, 45),
    'piedra': svg_costume(_svg(70, 60, '<polygon points="10,40 4,22 22,6 48,4 66,20 62,44 40,57 16,54" fill="#8E8E8E" stroke="#4A4A4A" stroke-width="2"/>'
                                       '<polygon points="22,18 40,12 50,24 32,30" fill="#B5B5B5"/>'), 'piedra', 35, 30),
    'fondo': svg_costume(_svg(480, 360, '<rect width="480" height="360" fill="#F4F6F9"/>'), 'fondo1', 240, 180),
    'gato': svg_costume(_svg(90, 80, '<ellipse cx="45" cy="52" rx="32" ry="24" fill="#F0A030" stroke="#8A5A10" stroke-width="2"/>'
                                     '<polygon points="20,32 26,8 40,30" fill="#F0A030" stroke="#8A5A10" stroke-width="2"/>'
                                     '<polygon points="70,32 64,8 50,30" fill="#F0A030" stroke="#8A5A10" stroke-width="2"/>'
                                     '<circle cx="34" cy="46" r="4" fill="#000"/><circle cx="56" cy="46" r="4" fill="#000"/>'
                                     '<path d="M38 58 q7 6 14 0" stroke="#000" stroke-width="2" fill="none"/>'), 'costume1', 45, 40),
}


# ---------------------------------------------------------------- objetos y proyecto
class Objeto:
    def __init__(self, nombre, disfraces, scripts, x=0, y=0, tamano=100, visible=True,
                 sonidos=(), direccion=90):
        self.nombre, self.disfraces, self.scripts = nombre, list(disfraces), scripts
        self.x, self.y, self.tamano, self.visible = x, y, tamano, visible
        self.sonidos, self.direccion = list(sonidos), direccion


def proyecto(objetos, fondos=None, sonidos_fondo=(), scripts_fondo=(), variables_iniciales=None):
    """Devuelve (project.json como dict, {md5ext: bytes})."""
    variables = {}
    broadcasts = {}
    assets = {}
    targets = []

    def _target(nombre, is_stage, scripts, disfraces, sonidos, **kw):
        comp = Compilador(variables, broadcasts)
        for i, sc in enumerate(scripts):
            comp.script(sc, x=40 + 420 * (i % 3), y=40 + 360 * (i // 3))
        cost = []
        for d in disfraces:
            assets[d['md5ext']] = d['_data']
            cost.append({k: v for k, v in d.items() if k != '_data'})
        sons = []
        for s in sonidos:
            assets[s['md5ext']] = s['_data']
            sons.append({k: v for k, v in s.items() if k != '_data'})
        t = {'isStage': is_stage, 'name': nombre, 'variables': {}, 'lists': {}, 'broadcasts': {},
             'blocks': comp.blocks, 'comments': {}, 'currentCostume': 0, 'costumes': cost,
             'sounds': sons, 'volume': 100, 'layerOrder': len(targets)}
        t.update(kw)
        return t

    stage = _target('Stage', True, list(scripts_fondo), fondos or [DISFRACES['fondo']], sonidos_fondo,
                    tempo=60, videoTransparency=50, videoState='on', textToSpeechLanguage=None)
    targets.append(stage)
    for o in objetos:
        targets.append(_target(o.nombre, False, o.scripts, o.disfraces, o.sonidos,
                               visible=o.visible, x=o.x, y=o.y, size=o.tamano, direction=o.direccion,
                               draggable=False, rotationStyle='all around'))
    ini = variables_iniciales or {}
    stage['variables'] = {vid: [nombre, ini.get(nombre, 0)] for nombre, vid in variables.items()}
    stage['broadcasts'] = {bid: nombre for nombre, bid in broadcasts.items()}
    pj = {'targets': targets, 'monitors': [], 'extensions': [],
          'meta': {'semver': '3.0.0', 'vm': '1.0.0', 'agent': 'generadores-t1/sb3.py'}}
    return pj, assets


def escribir_sb3(ruta, pj, assets):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('project.json', json.dumps(pj, ensure_ascii=False))
        for nombre, data in assets.items():
            z.writestr(nombre, data)
    open(ruta, 'wb').write(buf.getvalue())
    return len(buf.getvalue())

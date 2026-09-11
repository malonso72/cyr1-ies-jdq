# Taller de generación de T1 · Scratch

Las 20 páginas de `trimestres/t1-scratch/sesiones/` y las de `t1-scratch/juegos/` **no se editan
a mano**: se generan con estos scripts. Si tocas el HTML directamente, el siguiente que ejecute un
generador te lo pisa.

Esta carpeta está dentro de `documentacion/`, que **no se despliega** (ver `.assetsignore`).

---

## Cómo regenerar

Desde esta misma carpeta:

```
python3 gen_s01_s05.py     # sesiones 01 a 05
python3 gen_s06_s11.py     # sesiones 06 a 11
python3 gen_s12_s16.py     # sesiones 12 a 16
python3 gen_s17_s20.py     # sesiones 17 a 20 (proyecto final)
python3 gen_proyectos.py   # las tres bases del proyecto final + el índice de juegos
python3 gen_presentacion.py # la presentación inicial, para proyectar
python3 gen_indices.py     # índice de sesiones + hub del trimestre
```

Las rutas se calculan solas a partir de la posición de estos archivos, así que funciona desde
cualquier equipo sin tocar nada.

**Es reproducible byte a byte y se puede ejecutar dos veces seguidas sin efectos raros:**
después de regenerar, `git status` tiene que salir limpio si no has cambiado el contenido.
Eso es la comprobación rápida de que no has roto nada.

`fix_presentacion.py` es de un solo uso y **ya no sirve**: la presentación la escribe entera
`gen_presentacion.py`. Se conserva sólo para dejar constancia de qué se arregló en su día
(metadatos, doble `h1`, nombre accesible de las flechas); esos arreglos están incorporados al
generador.

## Cómo comprobar

```
cd /tmp && npm i jsdom          # sólo la primera vez de cada sesión: /tmp se limpia
cd <esta carpeta>
node test_sesiones.js 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
```

Son **678 comprobaciones**: estructura (un solo `h1`, `main`, skip-link, navcross, pie),
metadatos, accesibilidad de los SVG (`role`, `aria-label`, `<title>`, `viewBox`), `rel=noopener`
en los enlaces externos, y que la pregunta de comprensión de cada página corrige bien, se
bloquea tras responder y resalta la opción correcta.

Y además, siempre, los tres verificadores del repo:

```
python3 scripts/verificar_html.py
python3 scripts/comprobar_enlaces.py
python3 scripts/verificar_enlaces.py
```

> **Ojo:** el `node_modules/` que hay comprometido en la raíz del repo está roto —la carpeta
> `jsdom` no tiene ni `package.json`—, así que no sirve para nada. Por eso jsdom se instala en
> `/tmp`. Sigue pendiente sacar ese `node_modules` del control de versiones.

---

## Qué hace cada archivo

| Archivo | Para qué |
|---|---|
| `scratchsvg.py` | **El motor.** Dibuja bloques de Scratch 3 en SVG: colores oficiales, siluetas con muescas, sombreros, bloques C, `si … si no` con dos bocas, informadores ovalados, hexágonos booleanos, desplegables, muestras de color e iconos. |
| `diagramas.py` | Los dos dibujos que no son bloques: el mapa del editor de Scratch (S01) y la rosa de direcciones (S02). |
| `plantilla.py` | La estructura común de toda página de sesión, el CSS y el JS de la pregunta. Aquí se cambia el diseño de las 20 a la vez. `pagina_juego()` reaprovecha ese mismo esqueleto para las páginas de `juegos/`: misma profundidad de rutas, mismo CSS, otro hero y otra navegación. |
| `comun.py` | Rutas y la tabla sesión → página del cuadernillo. |
| `gen_s*.py` | El **contenido** de las sesiones: textos, programas de bloques, preguntas y explicaciones. |
| `gen_proyectos.py` | Las **tres bases del proyecto final** (`juegos/arkanoid.html`, `space-invaders.html`, `esquivar.html`) y el índice de `juegos/`. |
| `gen_presentacion.py` | La **presentación inicial** (`presentacion.html`): 17 diapositivas de visita guiada al editor. Reutiliza el mapa del editor de la S01 y el motor de bloques, y dibuja el escenario con coordenadas. Ni una captura de otra versión de Scratch. |
| `gen_indices.py` | El índice de sesiones y el **hub del trimestre**, que se escribe entero. Antes se parcheaba a base de reemplazos y cada cambio dejaba una entrada más que mantener viva; se abandonó. |
| `test_sesiones.js` | Las 678 comprobaciones. |

---

## Cómo se escribe un programa de bloques

Cada bloque es una tupla:

```python
('hat',   categoria, partes)                    # sombrero (al hacer clic en...)
('stack', categoria, partes)                    # bloque normal
('cap',   categoria, partes)                    # sin muesca abajo (detener todos)
('c',     categoria, partes, [hijos])           # bloque C (repetir, si...)
('ce',    categoria, partes, [hijos], partes2, [hijos2])   # si ... si no
```

Y `partes` es una lista de:

```python
'texto llano'
('num',  '50')                 # entrada numérica, óvalo blanco
('txt',  '¡Hola!')             # entrada de texto, igual pero se lee mejor en el fuente
('drop', 'espacio')            # desplegable
('color', '#1A1A1A')           # muestra de color
('icon', 'bandera')            # también 'giro-d' y 'giro-i'
hexa(cat, ...)                 # booleano hexagonal
rep(cat, ...)  var('Puntos')  op(...)           # informadores ovalados
```

Ejemplo real, de la sesión 9:

```python
('ce', 'control', ['si', hexa('operators', RESP, '=', op(var('a'), '+', var('b'))), 'entonces'],
   [('stack', 'looks',     ['decir', ('txt', '¡Bien!'), 'durante', ('num','1'), 'segundos']),
    ('stack', 'variables', ['sumar a', ('drop', 'Aciertos'), ('num', '1')])],
 ['si no'],
   [('stack', 'looks',     ['decir', ('txt', 'Casi'), 'durante', ('num','1'), 'segundos'])])
```

**Los anchos se miden de verdad**, con PIL y la fuente Liberation Sans Bold, que es
métricamente idéntica a Arial. Por eso el texto nunca se sale del bloque. Si alguna vez no
está PIL, hay una estimación de reserva, pero el resultado será peor.

Para ver un bloque antes de publicarlo: generar el SVG, sustituir la pila de fuentes por
`'Liberation Sans'` y pasarlo por `cairosvg`. Así lo que se ve en la imagen coincide con lo
que se midió.

---

## Reglas del contenido

Fijadas con Manuel y aplicadas en las 20 sesiones:

1. Segunda persona y frases cortas: es 1º de ESO.
2. **Nombres exactos de la paleta de Scratch 3**, verificados contra capturas del editor real:
   `Sprite1`, `costume1`, `Miau`, `¿Cómo te llamas?`, `sumar a`, `dar a … el valor`,
   `si toca un borde, rebotar`. La tabla completa está en
   [`../COTEJO_Cuadernillo_Scratch3.md`](../COTEJO_Cuadernillo_Scratch3.md). Consúltala
   antes de escribir cualquier bloque nuevo.
3. Ningún bloque de extensión (Música, Lápiz) sin decir que hay que añadirla.
4. Bloques en SVG, nunca capturas: se leen a media pantalla y no pesan.
5. Todo SVG con `role="img"`, `aria-label` y `<title>`.
6. Una pregunta de comprensión por sesión, con explicación de **por qué falla cada opción
   incorrecta**, no sólo de cuál es la buena.
7. Entrega siempre igual: Archivo → Guardar en tu ordenador → `SesionNN_TuNombre.sb3` → Moodle.
8. El cuadernillo se enlaza con `#page=` o no se enlaza.
9. **Las tres bases del proyecto final no estrenan ningún bloque.** Todo lo que aparece en
   `juegos/` sale de S01-S16 o de las ocho piezas del kit de la S18. Si al escribir una necesitas
   un bloque nuevo, o lo enseñas antes en una sesión o cambias el diseño del juego.
10. Las guías en PDF de `materiales/guias-juegos/` **están hechas con Scratch 2** y sus bloques son
    capturas, no texto: no se pueden corregir con una nota. Se enlazan como consulta y con aviso,
    nunca como material de trabajo.

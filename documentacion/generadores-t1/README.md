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
node test_sesiones.js 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
```

Son **759 comprobaciones**: estructura (un solo `h1`, `main`, skip-link, navcross, pie),
metadatos, accesibilidad de los SVG (`role`, `aria-label`, `<title>`, `viewBox`), `rel=noopener`
en los enlaces externos, y que la pregunta de comprensión de cada página corrige bien, se
bloquea tras responder y resalta la opción correcta.

Y además, siempre, los tres verificadores del repo:

```
python3 scripts/verificar_html.py
python3 scripts/comprobar_enlaces.py
python3 scripts/verificar_enlaces.py
```

> El `node_modules/` de la raíz del repo ya no está en el control de versiones (está en
> `.gitignore`) y el que queda en disco está roto, así que jsdom y scratch-vm se instalan en `/tmp`.

## Los `.sb3`: las bases como proyectos de Scratch de verdad

```
cd /tmp && npm i scratch-vm       # sólo la primera vez de cada sesión
cd <esta carpeta>
python3 gen_sb3.py --todos        # _soluciones/sb3/{arkanoid,space-invaders,esquivar}.sb3
node test_sb3.js                  # y /tmp/_todos_los_programas.sb3 (62 programas)
```

`sb3.py` traduce las tuplas de bloques a `project.json` **sin duplicar nada**: `gen_sb3.py`
importa `gen_proyectos.py` y las sesiones, así que cualquier cambio en un programa dibujado
cambia también el `.sb3`. Los `.sb3` van a `_soluciones/` porque son los juegos ya montados y
es Manuel quien decide cuándo darlos (Moodle, por ejemplo); no se despliegan. `test_sb3.js`
comprueba que **cargan** en el motor de Scratch y que cada bloque es un bloque que Scratch conoce
—es el equivalente, para Scratch, del cotejo de T2 en MakeCode—, pero no que el juego sea
jugable: sin renderizador no hay «¿tocando…?». Eso hay que probarlo abriendo el `.sb3` en
scratch.mit.edu.

---

## Qué hace cada archivo

| Archivo | Para qué |
|---|---|
| `scratchsvg.py` | **El motor.** Dibuja bloques de Scratch 3 en SVG: colores oficiales, siluetas con muescas, sombreros, bloques C, `si … si no` con dos bocas, informadores ovalados, hexágonos booleanos, desplegables, muestras de color e iconos. |
| `diagramas.py` | Los dos dibujos que no son bloques: el mapa del editor de Scratch (S01) y la rosa de direcciones (S02). |
| `plantilla.py` | La estructura común de toda página de sesión, el CSS y el JS de la pregunta. Aquí se cambia el diseño de las 20 a la vez. `pagina_juego()` reaprovecha ese mismo esqueleto para las páginas de `juegos/`: misma profundidad de rutas, mismo CSS, otro hero y otra navegación. |
| `comun.py` | Rutas y la tabla sesión → página del cuadernillo. |
| `gen_s*.py` | El **contenido** de las sesiones: textos, programas de bloques, preguntas y explicaciones. |
| `gen_s17_depuracion.py` | La **S17**, que es distinta: cinco programas con un fallo plantado. Escribe la página y, con `sb3.py`, los dos `.sb3` —el del alumnado y el arreglado— desde los mismos programas. |
| `gen_proyectos.py` | Las **tres bases del proyecto final** (`juegos/arkanoid.html`, `space-invaders.html`, `esquivar.html`) y el índice de `juegos/`. |
| `gen_presentacion.py` | La **presentación inicial** (`presentacion.html`): 17 diapositivas de visita guiada al editor. Reutiliza el mapa del editor de la S01 y el motor de bloques, y dibuja el escenario con coordenadas. Ni una captura de otra versión de Scratch. |
| `gen_indices.py` | El índice de sesiones y el **hub del trimestre**, que se escribe entero. Antes se parcheaba a base de reemplazos y cada cambio dejaba una entrada más que mantener viva; se abandonó. |
| `test_sesiones.js` | Las 759 comprobaciones. |
| `sb3.py` | **El exportador a Scratch.** Convierte las mismas tuplas que dibuja `scratchsvg.py` en el `project.json` de un `.sb3` de verdad (opcodes de Scratch 3, sombras, variables, mensajes), con disfraces esquemáticos en SVG y los sonidos «Pop» y «Miau» sintetizados. |
| `gen_sb3.py` | Escribe las **tres bases del proyecto como `.sb3`** en `_soluciones/sb3/` (privada) y, con `--todos`, un proyecto de prueba con los 62 programas de las sesiones. |
| `test_sb3.js` | Abre esos `.sb3` en `scratch-vm` (el motor de Scratch sin pantalla) y comprueba que cargan, que todos los bloques existen y que la bandera verde arranca los hilos. |

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
11. **Un número por cada cosa, y sólo donde significa algo.** Ver la sección siguiente.

---

## La regla de la numeración

Había tres numeraciones distintas con la misma pinta en la misma pantalla —el número de sección,
el número de una zona del dibujo y el número de un paso—, y en la S01 llegaban a chocar: la
sección se llamaba **2** y dentro del dibujo había otro **2**. Decir «mirad el dos» no significaba
nada.

Hay **cuatro categorías** y cada una tiene su forma:

| Qué es | Cómo se escribe | Ejemplo |
|---|---|---|
| **Sección** de la página | Número grande en círculo relleno, el estilo actual. Sólo lo usa esto | `3 · Comprueba que lo has entendido` |
| **Acción que hace el alumno** | **`Paso 1`, `Paso 2`…**, con la palabra escrita | Las listas de «Tu actividad» |
| **Secuencia de funcionamiento** de un programa | Número simple, sin la palabra «paso» | «Cómo funciona» |
| **Lista de conceptos, zonas o herramientas** sin orden | **Sin número.** Nombre destacado + explicación | Las cuatro zonas del editor |

Y una excepción, con **prueba objetiva**: un número que **es una referencia** se queda, aunque la
lista no tenga orden. La prueba no es opinable — se busca en el sitio:

```
grep -roih "pieza [0-9]\|punto [0-9]\|paso [0-9]" --include=*.html trimestres/
```

Si algún texto dice «Pieza 6 de la S18» o «el punto 3 de tu ficha», ese número es un enlace entre
páginas y **no se toca**. Hoy pasan la prueba dos listas: las **ocho piezas del kit de la S18** y
los **nueve puntos de la ficha de la S17**. Ninguna otra.

Consecuencias que hay que respetar al escribir:

- **La palabra «paso» queda reservada** para lo que hace el alumno. Por eso el título de sección
  «Qué hace, paso a paso» pasó a llamarse **«Cómo funciona»**.
- **En clase se dice «sección 4, paso 3»**, y eso apunta a un sitio único.
- Una lista numerada **promete un orden**. Si lo que tienes son dos programas que corren a la vez,
  o notas sueltas mezcladas con la ejecución, esa lista está mintiendo: sácalo de la lista.

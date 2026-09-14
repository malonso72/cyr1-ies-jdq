# Taller de generadores de T2 · micro:bit

Las páginas de `trimestres/t2-microbit/retos/` y el hub del trimestre **se generan desde aquí;
no se editan a mano**. Es el hermano del taller de T1 y reutiliza su CSS, su JS de la pregunta
y sus listas (`pasos`, `secuencia`, `claves`) importando `../generadores-t1/plantilla.py`.

## Cómo regenerar

```bash
cd documentacion/generadores-t2
python3 gen_r01_r08.py        # retos troncales 1 a 8
python3 gen_r09_r15.py        # retos troncales 9 a 15
python3 gen_ampliaciones.py   # las 12 ampliaciones (a01…a12) y las 3 sin material (m01…m03)
python3 gen_indices_t2.py     # hub del trimestre + índice de retos
python3 gen_presentacion_t2.py # la presentación inicial, para proyectar (15 diapositivas)
```

Después, los tres verificadores de `scripts/` y la prueba:

```bash
cd /tmp && npm i jsdom        # sólo la primera vez de cada sesión
cd documentacion/generadores-t2 && NODE_PATH=/tmp/node_modules node test_retos.js
```

## Los archivos

- `makecodesvg.py` — dibuja bloques de MakeCode en SVG con las formas, colores y letra del
  editor (medidos en el editor real, ver `../COTEJO_MakeCode.md`), y la matriz 5×5 de la
  placa (`matriz_svg`). Mismo modelo de tuplas que `scratchsvg.py`, con `('cm', …)` para las
  cascadas `si / si no, si / si no` y `('grid', patrón)` para la rejilla de `mostrar LEDs`.
- `bloques.py` — atajos con los nombres exactos del editor: `INICIAR`, `SIEMPRE`, `BOTON`,
  `GESTO`, `GRAFICAR`, `OCULTAR`, `FIJAR`, `CAMBIAR`, `SI`, `SINO`, `CASCADA`, `PARA`,
  `MIENTRAS`, `GRUPO`, `ENVIAR`, `RECIBIR`, `SPRITE`, `SP_*`… **Si un bloque no está aquí, se
  busca en el cotejo antes de inventarlo.**
- `plantilla_t2.py` — la página de reto: hero «Reto N / Ampliación N / Sin material N» con
  su etiqueta de nivel, botón de abrir MakeCode, secciones numeradas, entrega del `.hex`
  (el archivo se llama `microbit-RetoN_TuNombre.hex`), navegación anterior/índice/siguiente.
  Helpers propios: `caja`, `caja_varios` (varios eventos sueltos en una caja), `placa`
  (la matriz con texto al lado), `cat` (etiqueta de categoría con su color), `bl` (nombre
  de bloque en el texto), `amplia` (enlaces a las ampliaciones que salen del reto).
- `diagramas_t2.py` — la rosa de la brújula del reto 14, la placa vista de frente y el esquema
  de la pantalla de MakeCode (los dos, para la presentación).
- `comun_t2.py` — rutas y `escribir()`.

## Reglas

1. Los nombres de bloque son los del `COTEJO_MakeCode.md`, letra por letra: «ocultar x y»,
   «escoger al azar de … a …», «si agitado», «al presionarse el botón A», «fijar … a»,
   «mostrar ícono». Nada de memoria.
2. Cada reto troncal lleva: lo que vas a conseguir, una sección de idea cuando hay un
   concepto nuevo, «Lee este programa» con `secuencia` (cómo funciona) o `claves`
   (bloques sin orden), «Comprueba que lo has entendido» (una pregunta), «Tu reto» con
   `pasos`, «Lo has conseguido si…» y la entrega. Misma regla de numeración que T1.
3. Las ampliaciones son más ligeras: de dónde sale, el programa, tu reto, logros, entrega.
   Sin pregunta.
4. Los eventos van siempre sueltos, en `caja_varios`, nunca apilados en una `caja`: en el
   editor no se pegan.
5. Cada umbral de sensor va precedido de «mide primero»: el alumno decide el número.
6. Los retos que necesitan servo (m01–m03) no llevan bloques ni entrega: sólo el aviso y el
   programa en palabras.

# Pendientes · CyR 1.º ESO

Lo que queda por hacer, a **30 de septiembre de 2026**. Lo que ya está hecho no vive aquí: el
estado del sitio está en `CLAUDE.md`, el porqué de cada decisión en `DECISIONES*.md` y el
historial completo en el log de git.

## De Manuel

- [ ] **Publicar los commits.** Se hacen en local; subirlos a GitHub (y con ello al worker de
  Cloudflare) lo hace Manuel desde GitHub Desktop.
- [ ] **Rehacer los enlaces de Moodle a T2.** Los retos han cambiado de número y de archivo
  (`r01…r15` troncales, `a01…a12` ampliaciones, `m01…m03` sin material): los enlaces antiguos a
  `r16…r29`, `r00`, `teoria.html` y `actividades.html` ya no existen.
- [ ] **Revisar `DECISIONES_T2.md`** (13 puntos) y el punto 31 de `DECISIONES_T1.md`: es lo que
  Claude decidió por su cuenta y lo que conviene mirar con ojo de profesor.
- [ ] **Abrir en scratch.mit.edu y jugar** los tres `.sb3` de `_soluciones/sb3/` antes de darlos
  a nadie. Que carguen está comprobado; que se jueguen bien, no (hace falta un navegador).
- [ ] **Dos preguntas que sólo puede contestar él:** si el título de la S04 de T1 se puede
  cambiar en Moodle («Condicionales I» avisa en la propia página de que ese día no hay ningún
  `si… entonces`), y si el sonido `Pop` que usan S11, S12, S16 y S18 aparece con ese nombre en
  el editor de Scratch en español — el cotejo sólo dejó cerrado `Miau`.
- [ ] **Criterios de evaluación LOMLOE** por trimestre: rellenar el `<details class="criterios">`
  de cada hub con los descriptores de Andalucía.
- [ ] **«Saber / hacer / evaluar»** de los tres hubs: son una primera aproximación; ajustarlos a
  la programación oficial del departamento.

## De la revisión de septiembre (T1), pendientes de que Manuel diga

Propuestas de la tercera revisión que Manuel prefirió **no** aplicar por ahora. Se anotan para
no volver a proponerlas como nuevas:

- Separar mejor el ejemplo de lo que se entrega (una línea fija en «Lo que vas a conseguir» y
  otro pie en la caja del ejemplo). Su criterio: el problema es que no leen, y eso no se arregla
  con más texto.
- La norma «el personaje dice quiénes sois» desde la S01, en vez de insistir en el nombre del
  archivo. Su criterio: si lo del nombre no funciona, es cuestión de insistir.
- Recortes en S07 (dos preguntas en vez de tres), S09 y S14 (el paso 4 como ampliación) y los
  quince minutos de Scratch abierto al final de la S18.
- El `esperar 0.05` en la carrera de la S10: decisión suya viendo la clase.
- **Miau o Meow** en S01, S02, S03, S05 y la presentación: mirar el desplegable en la pantalla
  de un alumno. Y el **título de la S04** («Condicionales I») cuando la cree en Moodle.

## Para revisar el fin de semana (Manuel)

- Las diecisiete sesiones de T1 con «Tu actividad» en N.1/N.2/N.3 (DECISIONES_T1 §35). Lo que no
  convenza se cambia en `ampliaciones.py` (N.2, objetos) o `pseudocodigo.py` (N.3) y se regenera.

## Del material

- [ ] **Materiales auxiliares de T3** (S09, S10, S11, S12, S13, S14, S15, S16, S17, S18): las
  sesiones avisan de que los hay, pero el contenido extra no está en la web. Diez de ellos ya
  son páginas de reto; el resto sigue siendo aviso.
- [ ] **Solucionario del cuadernillo de T3**, si Manuel lo elabora: va a
  `_soluciones/` (privada, no se despliega).
- [ ] **Retos transversales** entre trimestres: están previstos en la plantilla
  (`assets/templates/PLANTILLA_reto.html`) y no se ha escrito ninguno.

## Anotado, sin prisa

- Las **cuatro páginas de juegos de T1 que ya son sesiones** (carreras, laberinto,
  piedra-papel-tijera, pong) siguen siendo las plantillas viejas de 3,7 KB. Se conservan por su
  PDF, y el índice ya avisa de que son sesiones.
- Las **once guías de juegos en PDF** y el **cuadernillo de Scratch** están hechos con Scratch 2
  y sus bloques son capturas: no se arreglan con una nota. Consulta con aviso, nunca material de
  trabajo.
- El **cuadernillo de retos de micro:bit** (`t2-microbit/materiales/retos-microbit.pdf`) usa la
  numeración vieja R0–R29 y ya no lo enlaza ninguna página. Se conserva como documento de
  origen, fuera del despliegue. Está en `DECISIONES_T2.md`.
- `node_modules/` sigue en el disco de Manuel, fuera del repositorio y sin que lo use nada. Se
  puede borrar cuando quiera.

## Hecho, para que no se vuelva a preguntar

El `git init`, el worker de Cloudflare, el contador de visitas, el `node_modules` comprometido,
el `s02.js` cargado dos veces, la caché de un año del CSS y el JS, el aviso de pareja en
ordenadores compartidos, la reescritura entera de T2, el exportador a `.sb3` de T1 y el test de
T3 están todos cerrados. El detalle, en `DECISIONES.md` y en el log de git.

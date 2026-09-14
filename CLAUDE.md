# CLAUDE.md — CyR 1º ESO · IES Jiménez de Quesada
## Lee esto al inicio de cada sesión antes de tocar ningún archivo.

---

## PROYECTO

Sitio web estático de **Computación y Robótica · 1º ESO**. Profesor: Manuel Alonso Herrera. Centro: IES Jiménez de Quesada, Santa Fe (Granada). Curso activo: **2026-27**.

Despliegue: Cloudflare Workers Static Assets vía GitHub (`git push` → producción automática en cyr1-ies-jdq.malonso72.workers.dev).

Para el mapa de carpetas y comandos de despliegue, ver `README.md` en la raíz de este repo — ya está bien documentado y no se duplica aquí.

---

## ESTADO DE ESTE FICHERO

Este CLAUDE.md se creó en agosto de 2026 al portar la infraestructura técnica de verificación desde el sitio hermano **teci2-ies-jdq** (Bachillerato), que lleva dos meses de trabajo iterativo y tiene una filosofía editorial mucho más desarrollada. Este fichero es un punto de partida deliberadamente ligero: documenta la herramienta nueva y deja que la filosofía editorial (qué se amplía, qué no, criterios de auditoría) se vaya fijando en próximas sesiones con Manuel, igual que ocurrió en teci2. No asumas que las convenciones de teci2 aplican aquí sin preguntar — este sitio puede seguir en fase de crecimiento de contenido, a diferencia de teci2.

---

## HERRAMIENTAS DE VERIFICACIÓN (nuevo, ago-2026)

Antes de este cambio, este repo solo tenía scripts de higiene de assets (imágenes huérfanas, archivos pesados) y `comprobar_enlaces.py` (href/src rotos). Se han añadido dos verificadores más, calcados de los usados en teci2:

- `scripts/verificar_html.py` — comprueba que todos los `.html` del sitio parsean sin errores (etiquetas mal formadas, comillas sin cerrar, etc.). Ejecutar: `python3 scripts/verificar_html.py`.
- `scripts/verificar_enlaces.py` — comprueba enlaces internos rotos y anchors `#id` que no existen en el fichero destino y que no haya enlaces entrantes a `_soluciones/` desde páginas públicas. Ejecutar: `python3 scripts/verificar_enlaces.py`.

**Hook de pre-push instalado.** `scripts/hooks/pre-push` ejecuta automáticamente `verificar_html.py`, `verificar_enlaces.py` y `comprobar_enlaces.py` antes de cada `git push`, y bloquea el push si algo falla. Ya está instalado en `.git/hooks/` de este repo (lo hizo esta sesión ejecutando `python3 scripts/instalar_hooks.py`). Si algún día hace falta reinstalarlo (p. ej. tras clonar el repo en otro equipo), basta con volver a ejecutar ese comando. Para saltárselo puntualmente: `git push --no-verify`.

**Resultado de la primera pasada (ago-2026):** ver el informe que te dio Claude en el chat — puede haber incidencias preexistentes (anchors rotos, etc.) que no se han corregido en esta sesión porque el objetivo era solo instalar la herramienta, no auditar contenido. Cuando le toque el turno de trabajo profundo a este sitio, esa lista es un buen punto de partida.

---

## REGLAS PERMANENTES DE TRABAJO CON MANUEL

Valen para este repo y para el hermano `teci2-ies-jdq`. No son negociables salvo que él lo diga.

- **Nunca hagas `git push`.** Manuel publica él desde GitHub Desktop, cuando ha revisado.
  Tú dejas los commits hechos en local y se lo dices.
- **Commit con su autoría:**
  `git -c user.name="Manuel Alonso Herrera" -c user.email="malonso72@gmail.com" commit`
- **Pasa los tres verificadores antes de cada commit** (`verificar_html.py`,
  `comprobar_enlaces.py`, `verificar_enlaces.py`). El hook de pre-push los repite, pero para
  entonces ya es tarde para arreglarlo con calma.
- **Un commit limpio por pieza de trabajo**, con mensaje que explique el porqué, no sólo el qué.
- `_soluciones/`, `documentacion/` y `_academia-v3/` son privadas y no se despliegan.
- Si una decisión es dudosa y él ha dicho que tires adelante, **toma la opción conservadora,
  anótala y sigue**; no pares a preguntar. Las decisiones tomadas así van a un documento aparte
  para que las revise de una vez.

---

## T1 · SCRATCH — ESTADO (sept-2026)

**Reescrito entero y revisado.** Las 20 sesiones dejaron de ser un índice que abría el cuadernillo
completo por la página 1 y son ahora páginas de trabajo autónomas, pensadas para tener Scratch
abierto al lado en media pantalla.

Después de la reescritura se hizo una **revisión pedagógica de las 20** contra el plan y el
cotejo (`REVISION_T1_SESIONES.md`). Salieron cuatro programas que no funcionaban al ejecutarlos
—no al leerlos— y varias promesas que el material no cumplía. Está todo arreglado. Lo que
decidí por mi cuenta al arreglarlo está en `DECISIONES_T1.md`, puntos 12 a 20.

**Dotación real: 2 sesiones semanales.** Las 20 sesiones son unas 10 semanas y el trimestre da
para unas 13. Esas clases de más se van en el **proyecto final**, que no es un juego inventado:
es **uno completo elegido entre tres bases** —Arkanoid, Space Invaders y Esquivar lo que cae—, en
`t1-scratch/juegos/`. Lo que se evalúa no es el juego, es **la versión de cada uno**: la ficha de
la S17 pide tres cambios concretos sobre la base. Así se puede mandar el mismo juego a toda la
clase sin que las presentaciones de la S20 salgan iguales.

### Contexto real de clase — importa para todo lo que escribas

- Scratch **3 en el navegador** (scratch.mit.edu). No se instala nada.
- Ordenadores **Linux**. El Scratch de escritorio no es una opción.
- El alumnado trabaja **sin cuenta**: el proyecto sólo existe en la pestaña. Se entrega
  descargando el `.sb3` y subiéndolo a Moodle. **Nunca escribas «guarda tu proyecto en Scratch».**
- Flujo del alumno: Moodle → página de la sesión → hace el ejercicio → vuelve a Moodle a entregar.
- El **cuadernillo PDF es antiguo** (Scratch 2) y muchos bloques ya no se llaman igual. Es
  consulta opcional, se enlaza con `#page=` y nunca como destino de trabajo.

### Dónde está cada cosa

- La portada del trimestre está en **tres tarjetas** —presentación, abrir Scratch y sesiones—
  porque el alumnado no entra por ahí: entra desde Moodle directo a la sesión. Si se añade algo,
  que sea porque hace falta desde la portada, no porque exista.
- Las páginas: `trimestres/t1-scratch/sesiones/s01..s20.html`
- Las tres bases del proyecto: `trimestres/t1-scratch/juegos/` (`arkanoid`, `space-invaders`,
  `esquivar`, más su índice). El resto de páginas de esa carpeta son las viejas, con su PDF.
- **Se generan, no se editan a mano:** `documentacion/generadores-t1/` (tiene su propio README
  con cómo regenerar, cómo probar y cómo se escribe un programa de bloques).
- **Las guías en PDF de `materiales/guias-juegos/` están hechas con Scratch 2** y sus bloques son
  capturas, así que no se arreglan con una nota como se hizo con el cuadernillo. Son consulta con
  aviso, nunca material de trabajo. Si hace falta un juego nuevo, se redibuja en Scratch 3 con
  `gen_proyectos.py`.
- Documentos de trabajo, en `documentacion/` (privada, no se despliega):
  - `AUDITORIA_CyR_1ESO.md` — auditoría del sitio entero, con notas por área y hallazgos H1–H13.
  - `COTEJO_Cuadernillo_Scratch3.md` — **tabla verificada** de nombres de bloques Scratch 2 → 3,
    transcrita de capturas del editor real. Consúltala antes de escribir cualquier bloque.
  - `COTEJO_MakeCode.md` — lo mismo para **micro:bit**: tipo, forma, color, texto en español y
    desplegables de cada bloque, leídos del Blockly del editor real; más la geometría de los
    bloques. Consúltalo antes de escribir cualquier bloque de T2.
  - `PLAN_T1_SCRATCH.md` — el guion de las 20 sesiones y las reglas de estilo del material.
  - `DECISIONES_T1.md` — lo que Claude decidió por su cuenta, con el porqué. Puntos 1-11 de la
    reescritura; 12-20 de la ronda de arreglos posterior.
  - `REVISION_T1_SESIONES.md` — la revisión pedagógica de las 20 sesiones: qué fallaba, qué se
    arregló y qué queda.

### Lo que queda pendiente en CyR

1. **Dos cosas que sólo puede contestar Manuel:** si el título de la S04 se puede cambiar en
   Moodle («Condicionales I» avisa en la propia página de que hoy no hay ningún `si… entonces`),
   y si el sonido `Pop` que usan S11, S12, S16 y S18 aparece con ese nombre en el editor — el
   `COTEJO` sólo dejó cerrado `Miau`.
2. De las **cuatro decisiones de la auditoría** quedan dos: si T3 converge con el resto del
   sitio, y si se saca `node_modules` del repo. Las otras dos están contestadas — ver el final
   de `AUDITORIA_CyR_1ESO.md`. Ojo: los «🚧 En construcción» de **T2 micro:bit** siguen ahí.
3. ~~`node_modules` comprometido~~ **Hecho (sept-2026):** fuera del repo y del despliegue,
   en `.gitignore`. La carpeta sigue en el disco de Manuel por si quiere borrarla; no la usa nada.
4. ~~`s02.js` se carga dos veces~~ **Hecho (sept-2026)**, junto con los arreglos técnicos de
   los 10 retos de T3 y el **aviso de pareja** de `academia.js`: en ordenadores compartidos, si
   ya hay nombres guardados la sesión pregunta «¿sois vosotros?»; si no, el progreso de la otra
   pareja se archiva en `academia:archivo:<nombres>` y se recupera si vuelven a escribirlos.
5. **Segunda auditoría (14-sept-2026), al final de `AUDITORIA_CyR_1ESO.md`:** diagnóstico
   completo y el orden acordado con Manuel. **T2 está decidido** en `CLASIFICACION_RETOS_T2.md`:
   troncal de 15 en orden nuevo, 12 ampliaciones que se conservan, 3 sin material (servo).
   Sin proyecto final, editor en español, entrega del `.hex`. Aula: 7–8 micro:bit V2 por
   parejas, pinzas de cocodrilo, nada más. El curso pasado llegaron al r19.
6. Las **cuatro páginas de juegos que ya son sesiones** (carreras, laberinto,
   piedra-papel-tijera, pong) siguen siendo las plantillas viejas de 3,7 KB. Se conservan por su
   PDF y el índice ya avisa de que son sesiones, pero si alguna vez estorban, ahí están.

---

## CONVENCIONES CONOCIDAS

- HTML + CSS + JS vanilla, sin frameworks (ver README.md → sección Convenciones si existe).
- `_soluciones/` es privada y no debe enlazarse desde páginas visibles al alumnado (lo comprueba `verificar_enlaces.py`).
- `documentacion/` es privada (PROGRAMACION, DECISIONES, PENDIENTES) — no se despliega públicamente salvo que el `.assetsignore` diga lo contrario; revisa `.assetsignore` antes de asumirlo.

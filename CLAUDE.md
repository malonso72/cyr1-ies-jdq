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

**Reescrito entero.** Las 20 sesiones dejaron de ser un índice que abría el cuadernillo completo
por la página 1 y son ahora páginas de trabajo autónomas, pensadas para tener Scratch abierto al
lado en media pantalla.

### Contexto real de clase — importa para todo lo que escribas

- Scratch **3 en el navegador** (scratch.mit.edu). No se instala nada.
- Ordenadores **Linux**. El Scratch de escritorio no es una opción.
- El alumnado trabaja **sin cuenta**: el proyecto sólo existe en la pestaña. Se entrega
  descargando el `.sb3` y subiéndolo a Moodle. **Nunca escribas «guarda tu proyecto en Scratch».**
- Flujo del alumno: Moodle → página de la sesión → hace el ejercicio → vuelve a Moodle a entregar.
- El **cuadernillo PDF es antiguo** (Scratch 2) y muchos bloques ya no se llaman igual. Es
  consulta opcional, se enlaza con `#page=` y nunca como destino de trabajo.

### Dónde está cada cosa

- Las páginas: `trimestres/t1-scratch/sesiones/s01..s20.html`
- **Se generan, no se editan a mano:** `documentacion/generadores-t1/` (tiene su propio README
  con cómo regenerar, cómo probar y cómo se escribe un programa de bloques).
- Documentos de trabajo, **fuera del repo**, en la carpeta de Manuel `00 ECOSISTEMAS`:
  `AUDITORIA_CyR_1ESO.md`, `COTEJO_Cuadernillo_Scratch3.md` (tabla verificada de nombres de
  bloques Scratch 2 → 3), `PLAN_T1_SCRATCH.md` (el guion de las 20) y `DECISIONES_T1.md`.

### Lo que queda pendiente en CyR

1. **Validación de Manuel** del material nuevo: tono y longitud para 1º de ESO. Sugeridas S09,
   S12 y S18.
2. Las **cuatro decisiones de la auditoría** siguen sin contestar: qué hacer con las páginas
   «🚧 En construcción», si T3 converge con el resto, y si se saca `node_modules` del repo.
3. **`node_modules` está comprometido y además roto** (la carpeta `jsdom` no tiene
   `package.json`). Pendiente `git rm -r --cached` + `.gitignore`.
4. **`s02.js` se carga dos veces** en una página de T3 Ciberseguridad →
   `SyntaxError: Identifier 'SESION_ID' has already been declared`. Diagnosticado, sin arreglar.
   Era el único error real de JavaScript de las 112 páginas del sitio.
5. T2 y T3 sin tocar. Manuel acotó el trabajo a T1.

---

## CONVENCIONES CONOCIDAS

- HTML + CSS + JS vanilla, sin frameworks (ver README.md → sección Convenciones si existe).
- `_soluciones/` es privada y no debe enlazarse desde páginas visibles al alumnado (lo comprueba `verificar_enlaces.py`).
- `documentacion/` es privada (PROGRAMACION, DECISIONES, PENDIENTES) — no se despliega públicamente salvo que el `.assetsignore` diga lo contrario; revisa `.assetsignore` antes de asumirlo.

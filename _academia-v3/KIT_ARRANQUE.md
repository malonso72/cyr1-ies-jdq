# KIT DE ARRANQUE · Web de CyR 1º ESO
> Léeme primero. Te da todo el contexto para trabajar con Manuel sin rediscutir lo ya decidido.
> Última actualización: junio 2026.

## Quién es y contexto
- **Manuel Alonso Herrera**, profesor en el **IES Jiménez de Quesada**, Santa Fe (Granada).
- Asignatura: **Computación y Robótica (CyR) 1º ESO**.
- **El proyecto es la web completa del curso** (repositorio `cyr1-ies-jdq`), organizada por **trimestres**. NO es solo ciberseguridad.
- **Academia Cyber-IES** es únicamente el bloque del **3er trimestre (T3 · Ciberseguridad)**: 18 sesiones interactivas (HTML) autónomas. Es lo que está terminado y lo más reciente; el resto del curso (T1, T2) puede ser trabajo de septiembre en adelante.
- Grupo difícil: no se les puede dar mucha teoría magistral; las actividades deben mantenerlos **ocupados de forma autónoma** (~30 min).

## Cómo prefiere que le hablen
- **Conciso y directo.** Sin relleno ni explicaciones largas. Nada de emojis salvo que él los use.
- Honestidad por encima de complacer: si algo no va a funcionar (p. ej. "esto dura 10 min, no 30"), decírselo claro.
- **Importante:** la IA solo edita archivos en local. Recordarle **siempre** que tiene que hacer **commit + push en GitHub Desktop** para que los cambios lleguen a la web.

## Arquitectura técnica (NO rediscutir)
- Sitio **estático HTML/CSS/JS** servido por **Cloudflare Workers**. Dominio: `https://cyr1-ies-jdq.malonso72.workers.dev`. URLs limpias (`/s12` sirve `s12.html`).
- **DOS copias que hay que mantener sincronizadas en CADA cambio:**
  - `_academia-v3/` = **FUENTE editable** (excluida del deploy vía `.assetsignore`).
  - `trimestres/t3-ciberseguridad/` = **DESPLEGADA** (lo que ve el alumno).
- **Regla de profundidad de rutas:** la fuente está un nivel más arriba que la desplegada. Rutas a la raíz: en la fuente `../` (hub) / `../../` (sesión); en la desplegada `../../` (hub) / `../../../` (sesión). Las rutas internas de la Academia (`../assets/...`, `../index.html`, `../retos/...`, hermanas `sNN.html`) no cambian.
- **Patrón de sesión:** `sesiones/sNN.html` (envoltorio de 6 bloques: misión / teoría / entrenamiento / juego / informe / diploma) + `sNN.js` (arrays CONCEPTOS y FRASES_VF + lógica) + `<iframe>` a `retos/sNN-reto-X.html` (juego autónomo). Excepción: **s01** tiene el JS incrustado en su HTML.
- Helpers compartidos en `assets/js/academia.js` (`Academia.*`): nombres, getSesion/setSesion (localStorage `academia:s:<id>`), marcarCompletada, irABloque, respuestaInformeValida, descargarDiploma/generarDiplomaPNG, codigoFinalizacion.
- **Verificación obligatoria** tras tocar JS: `node --check`. Cuidado: editar ficheros en el mount a veces deja **bytes NUL** al final → limpiar con `tr -d '\000'`.

## Decisiones de diseño ya tomadas (NO rediscutir)
- **Modelo anti-"tuntún" (no clicar al azar):**
  - **Teoría (microquiz) y entrenamiento (V/F): ESTRICTOS** — un solo fallo y vuelves al principio del bloque.
  - En las sesiones con reto-historia (S12), la **historia da 2ª oportunidad**; dos fallos seguidos en la misma decisión → reinicia.
  - **Insignia = racha perfecta** (acertar a la primera). **Diploma siempre** (completar = aprobar).
  - En S12 hay **nota numérica** en el diploma = `max(5, 10 − segundas_oportunidades_usadas)`.
- **Navegación de teoría (arreglada en las 18 sesiones, junio 2026):** sin puntos clicables (no se pueden saltar preguntas), sin botones externos "Anterior/Siguiente"; un único botón que en el último concepto pasa a **"A entrenar ▸"** y avanza.
- **La duración real** de una sesión autónoma de clic es ~10-15 min. La palanca para acercarse a 30 min es **el informe** (escribir y pensar, no reconocer). Por eso S12 y S13 tienen **informe ampliado** (5 preguntas, mínimo 20 palabras, con preguntas de aplicación personal).
- **S12 = Ciberacoso** ("¿Qué harías tú?", la historia de Marcos). El **Tribunal Digital** quedó como **S12-alt** (alternativa).
- Recursos de ayuda en la sesión de ciberacoso: **017** (INCIBE) y **116 111** (Fundación ANAR).

## Documentos clave (en `_academia-v3/`)
- `ESTADO.md` → estado vivo y detallado del proyecto (leer si hace falta histórico).
- `TAREAS-MOODLE.md` → texto listo para pegar en cada Tarea de Moodle (18 sesiones + alt).
- `ENLACES-MOODLE.md` → lista de URLs y cómo montarlas en Moodle.

## Estado actual (junio 2026)
- Las **18 sesiones + S12-alt** están terminadas, desplegadas y con la navegación de teoría arreglada y verificada.
- **Informe ampliado** aplicado SOLO a **S12 y S13** (pendiente de pilotar en clase antes de replicar la dosis al resto).
- Índice (`index.html`) con todas las sesiones **abiertas**. Tiene un control `SESIONES_ACTIVAS` cerca del final: lista vacía `[]` = todas abiertas; `['s13.html']` = solo esa.

## Próximos pasos pendientes (para septiembre)
1. **Pilotar** S12 y S13 con el informe ampliado: cronometrar y ver si llega a ~25-30 min.
2. Si funciona, **replicar el informe ampliado** (5 preguntas · 20 palabras, con preguntas propias por tema) al resto de sesiones.
3. (Opcional, aplazado) Dificultad mayor: que el reto no revele la respuesta al fallar, banco de preguntas con aleatorización. s01 quedó menos estricta a propósito.
4. Mantener siempre los cambios en **las dos copias** y hacer **commit + push**.

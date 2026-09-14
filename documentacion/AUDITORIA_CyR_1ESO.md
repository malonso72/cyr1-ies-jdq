# Auditoría · Computación y Robótica 1º ESO

**Sitio:** `ESO Web/cyr1-ies-jdq` → cyr1-ies-jdq.malonso72.workers.dev
**Fecha:** 10 de septiembre de 2026 · **Estado del repo:** limpio, sincronizado con `origin/main`
**Alcance:** las 112 páginas HTML del sitio, sus hojas de estilo, sus scripts y la configuración de despliegue.
**No se ha modificado ningún archivo.**

---

## 1. Resumen ejecutivo

El sitio está **mucho más completo de lo que aparenta desde la portada**. Hay 20 sesiones de Scratch, 12 fichas de juego, 30 retos de micro:bit, 19 sesiones de ciberseguridad con 10 retos interactivos gamificados y 14 PDFs. La infraestructura técnica es sólida: los tres verificadores pasan en verde, no hay ni un enlace roto sobre 1.137, y el 100 % del HTML parsea bien.

Los problemas no son de solidez, son de **acabado y de coherencia**:

| Área | Nota | Comentario en una línea |
|---|---|---|
| Integridad técnica (HTML, enlaces) | **92** | Todo en verde; un solo defecto real de JS |
| Contenido T3 · Ciberseguridad | **85** | Lo mejor del sitio, con diferencia |
| Contenido T2 · micro:bit | **70** | Bien escrito, pero lleno de restos del generador |
| Accesibilidad | **60** | T1 y T2 correctos; los retos de T3 no |
| Despliegue y mantenimiento | **55** | Se está publicando `node_modules` entero |
| Coherencia entre trimestres | **45** | T3 es, de hecho, otro sitio |
| Contenido T1 · Scratch | **40** | 20 sesiones de 120 palabras, casi clonadas |
| Portada | **35** | Tres tarjetas y poco más |
| **Global** | **≈ 62** | |

**Las tres cosas que arreglaría primero**, por orden de daño que hacen:

1. Los cuatro **"🚧 En construcción"** que cuelgan de la navegación de 73 páginas.
2. Los **restos del generador** en los 30 retos de micro:bit (se ven a simple vista).
3. **`node_modules` publicándose** en producción: 24 MB y 1.760 archivos.

---

## 2. Hallazgos por severidad

### 🔴 Alta

**H1 · Cuatro páginas "En construcción" enlazadas desde toda la navegación.**
`t1-scratch/teoria.html`, `t1-scratch/actividades.html`, `t2-microbit/teoria.html` y `t2-microbit/actividades.html` contienen literalmente *«Esta página estará disponible próximamente»*. No son páginas escondidas: el botón **📖 Teoría** de la barra de navegación transversal aparece en **39 páginas de T1 y 34 de T2**. Es decir, 73 de las 112 páginas del sitio ofrecen a un alumno de 1º ESO un botón que no lleva a ninguna parte.

**H2 · `node_modules/` está en el repositorio y se publica.**
- No existe `.gitignore` en el repo.
- `git ls-files` cuenta 1.937 archivos, de los cuales **1.760 son `node_modules/`** (24 MB): el 91 % del repositorio.
- `wrangler.toml` publica `directory = "./"` y `.assetsignore` **no excluye `node_modules/`**, así que esos 24 MB van a producción en cada despliegue.
- Son 31 paquetes (jsdom y sus dependencias) que ningún script del sitio usa: los verificadores del repo son Python, y de hecho todos ellos ya excluyen `node_modules` explícitamente.
- De paso, `scripts/` (los verificadores) también se publica sin necesidad.

**H3 · Los 10 retos de T3 no son accesibles ni navegables.**
Son las páginas más ricas del sitio (escape room, torneo Real/Fake, Cluedo, caso Marta Ruiz…) y las que peor tratadas están:
- **0 de 10** tienen `<main>` o `#main-content`.
- **0 de 10** tienen enlace "Saltar al contenido".
- **0 de 33** páginas de T3 tienen pie de página.
- **44 controles de formulario sin etiqueta** (`s13-reto-lucia` 12 de 12, `s09-reto-piensa` 8 de 8, `s15-reto-detective` 3 de 3…).
- 2 elementos con `onclick` sin `role` ni `tabindex` (no se pueden usar con teclado).
- Ninguno de los 10 está en el `sitemap.xml`.

### 🟠 Media

**H4 · Restos del generador en los 30 retos de micro:bit.** Todo esto se ve a simple vista:
- **120 badges vacíos** (`<span class='badge'></span>`), unos 4 por reto, en los 30.
- **22 viñetas huérfanas**: frases partidas en dos elementos de lista. Ejemplos: *«ayuda mucho!»*, *«sensor crepuscular!»*, *«control de flujo!»*, *«batería, o velocidad!»*.
- En **29 de los 30**, un *«Consejo: …»* está metido dentro de la lista de autoevaluación como si fuera un criterio evaluable.
- **20 de 30 títulos en Title Case inglés**: «Escribir Y Borrar Un Número», «Animación De Corazón», «Termostato Con Icono».

**H5 · Las 20 sesiones de T1 son casi la misma página.**
- Longitud: entre 118 y 135 palabras. Todas con las mismas cinco secciones.
- El **«🚀 Reto opcional» es literalmente idéntico en las 20**: *«Mejora tu proyecto añadiendo al menos un sonido, un cambio de disfraz o una variable visible en pantalla»*.
- El «Material base» de s17–s20 dice sólo «Proyecto final.».
- Los objetivos y los conceptos clave sí están escritos uno a uno, y son correctos. El problema es que la sesión no es material de trabajo: es un índice hacia el cuadernillo PDF.

Contraste útil: en T2, «Reto extra» y «Ayuda» tienen **30 textos distintos** cada uno. Ahí sí se escribió reto a reto.

**H6 · T3 es un sitio dentro del sitio.**

| | T1 | T2 | T3 |
|---|---|---|---|
| Páginas | 40 | 35 | 33 |
| Con cabecera `curso-hd` | 39 | 34 | **21** |
| Con navegación transversal | 39 | 34 | **21** |
| Con pie de página | 37 | 32 | **0** |
| Usan `hub-main`/`section-title` | 37 | 32 | **0** |
| CSS propio | — | inline en 32 | `academia.css`, 36 KB |
| Peso medio por página | 4 KB | 5 KB | **20 KB** |

T3 tiene su propio lenguaje visual (`paso`, `bloque-hud`, `mi-insignia`, `btn-acad`, `chip`), su propio JS con progreso en `localStorage`, insignias y códigos de finalización. **Funciona muy bien** — pero un alumno que salta de T2 a T3 cambia de sitio web. Hay que decidir si eso es un problema o una decisión.

### 🟡 Baja

**H7 · `s02.html` de T3 carga `s02.js` dos veces.** La segunda copia lanza `SyntaxError: Identifier 'SESION_ID' has already been declared` en la consola. Como es un error de análisis, la segunda copia no llega a ejecutarse y la página funciona; pero es el **único error real de JavaScript de las 112 páginas** y se arregla borrando una línea.

**H8 · Versión incoherente en el pie.** `v1.0.0` en 70 páginas, `v1.1.0` sólo en la portada.

**H9 · Sitemap incompleto.** 97 URLs para 109 páginas publicables: faltan los 10 retos de T3 (las otras 2 ausencias son redirecciones con `noindex`, y ahí está bien que no aparezcan).

**H10 · El buscador está escrito pero no conectado.** Existe `assets/js/search.js`, y las tarjetas de la portada llevan sus `data-keywords` cuidadosamente rellenados… pero **ninguna página del sitio carga ese script**. Es una funcionalidad terminada y sin enchufar.

**H11 · Google Fonts en 98 de las 112 páginas.** Sin conexión, la tipografía cae al respaldo del sistema (que está bien declarado en el CSS: `var(--sans), system-ui, sans-serif`). El impacto es sólo estético. Matiz importante frente a TECI II: **esta asignatura depende de Internet por naturaleza** — 31 enlaces a scratch.mit.edu, 30 a makecode.microbit.org y 31 al Moodle de la Junta. Sin red no hay clase, con o sin fuentes.

**H12 · Documentación desactualizada.** `PENDIENTES.md` afirma que existe `t3-ciberseguridad/moodle.html` (no existe) y habla de 19 sesiones publicadas cuando la portada anuncia 18.

**H13 · El sitio no tiene imágenes.** 112 páginas y 2 imágenes en total (el logo y la fachada, ambas en la portada). Para 1º ESO es un dato a considerar, sobre todo en T2, donde los retos describen patrones de LEDs con texto y coordenadas.

---

## 3. Lo que está bien y conviene no tocar

- **La red de verificación funciona.** Los tres scripts pasan en verde y el hook de pre-push está instalado: 0 enlaces rotos sobre 1.137, 112/112 HTML válidos.
- **La navegación transversal de T1 y T2 es excelente**: cabecera, migas, anterior/siguiente, skip-link. Se nota el patrón bien pensado.
- **T3 es material de primera.** La Academia Cyber-IES, con sus insignias, su progreso persistente y sus 10 retos narrativos, es lo mejor del ecosistema para esta etapa.
- **Los contenidos de T2 están escritos de verdad**, reto a reto, con pseudocódigo propio.
- **Metadatos y curso al día**: 2026-27 coherente en 98 páginas, canonical y Open Graph en la portada, `robots.txt` y `_headers` correctos.
- `.assetsignore` ya protege bien `documentacion/`, `_soluciones/` y `_academia-v3/`.

---

## 4. Plan por tandas propuesto

Ordenadas por relación impacto/coste. Ninguna se ejecuta sin tu visto bueno.

| # | Tanda | Qué incluye | Coste | Riesgo |
|---|---|---|---|---|
| **1** | Higiene de despliegue | `.gitignore`, sacar `node_modules` del repo y del despliegue, excluir `scripts/`, arreglar el `s02.js` duplicado, unificar la versión del pie, completar el sitemap | 45 min | Muy bajo |
| **2** | Limpieza de los 30 retos de T2 | 120 badges vacíos, 22 viñetas partidas, sacar el «Consejo:» de la autoevaluación, 20 títulos a mayúscula inicial | 1,5 h | Bajo |
| **3** | Resolver los "En construcción" | Escribir la teoría real de T1 y T2, **o** retirar esos botones de la navegación | 30 min o 4 h | Bajo / decisión tuya |
| **4** | Accesibilidad de los 10 retos de T3 | `main`, skip-link, pie, etiquetas en los 44 controles, teclado en los 2 `onclick` | 2 h | Bajo |
| **5** | Enriquecer las 20 sesiones de T1 | Reto propio por sesión (fuera el clon ×20), errores típicos, criterio de logro | 3-4 h | Medio |
| **6** | Conectar el buscador | Enchufar `search.js` en la portada y en los hubs | 45 min | Bajo |
| **7** | Portada | Decidir si crece (buscador, acceso directo a sesiones, estado del curso) o se deja | 2-3 h | Medio |
| **8** | Coherencia de T3 | Acercar la Academia al lenguaje del resto, o declararla identidad propia y dejarla | 4 h o 0 | Medio |
| **9** | Google Fonts local | Como se hizo en TECI II | 1 h | Bajo |

Las tandas 1 a 4 son las que más devuelven por lo que cuestan: **unas 5 horas** y se llevan por delante casi todo lo visible.

---

## 5. Lo que necesito que decidas

1. **Los "En construcción"** (H1): ¿escribimos teoría de verdad para T1 y T2, o quitamos esos dos botones de la navegación hasta que la haya? Quitarlos cuesta 30 minutos; escribirla, unas cuatro horas por trimestre.
2. **T3 y su identidad** (H6): ¿la Academia Cyber-IES se acerca al resto del sitio, o la damos por buena como está y asumimos que es un bloque con voz propia?
3. **Las sesiones de T1** (H5): ¿son deliberadamente un índice hacia el cuadernillo PDF, o quieres que se conviertan en material que se sostenga solo?
4. **`node_modules`** (H2): confirmo que puedo sacarlo del repositorio. Es un `git rm -r --cached` más `.gitignore`; no se pierde nada, porque no lo usa ningún script del sitio.

---

## 6. Cómo se ha comprobado todo esto

- Los tres verificadores del repo: `verificar_html.py`, `verificar_enlaces.py`, `comprobar_enlaces.py`.
- Carga de **las 112 páginas en jsdom sin acceso a red**, recogiendo errores de JavaScript e indicadores de estructura y accesibilidad (h1, main, etiquetas de controles, alt, roles, tablas, longitud de texto).
- Análisis estático del HTML: assets compartidos por página, dominios externos, patrones de clase por trimestre, textos repetidos sección a sección.
- Contraste de `sitemap.xml` y de `.assetsignore` con los archivos reales, y de `PENDIENTES.md` con lo publicado.
- Comprobación del sitio en producción (`sitemap.xml` servido correctamente).

---

## Estado de las cuatro decisiones (sept-2026)

1. **Los «En construcción» (H1) — contestada para T1.** `teoria.html` y `actividades.html` de
   T1 se han **borrado**, junto con `proyectos/`, y se ha quitado «Teoría» de la barra de
   navegación de las páginas que lo llevaban. Una página en construcción es peor que no tener
   página. **Las de T2 micro:bit siguen ahí**: el encargo era T1.
2. **T3 y su identidad (H6) — sin contestar.**
3. **Las sesiones de T1 (H5) — contestada.** Se reescribieron enteras: son material autónomo,
   no un índice hacia el PDF. Ver `PLAN_T1_SCRATCH.md` y `REVISION_T1_SESIONES.md`.
4. **`node_modules` (H2) — sin contestar.**

De propina, dos hallazgos más que han salido al trabajar T1 y que la auditoría no recogía:

- **Las once guías en PDF de `materiales/guias-juegos/` están hechas con Scratch 2**, igual que
  el cuadernillo, y sus bloques son capturas: no se pueden corregir con una nota al pie. Por eso
  las tres bases del proyecto final se han redibujado enteras en Scratch 3.
- **Las once páginas de `juegos/` eran plantillas vacías**: la misma frase de «conceptos que
  trabaja» repetida en las once, incluido un «variables, puntuación o mensajes según el juego»
  sin rellenar. Tres se han rehecho; las otras ocho siguen como estaban, ya clasificadas.

---

## Segunda auditoría · 14 de septiembre de 2026

Pasada completa sobre el repositorio y el sitio publicado, después de cerrar T1. Se recorrieron
los 108 HTML con un análisis estático (estructura, etiquetas, sitemap, pie, fuentes), se leyeron
los 30 retos de T2 uno por uno, se probó en el sitio publicado la generación de insignia y código
de T3, y se comprobó qué archivos sirve realmente el despliegue.

### Diagnóstico

El sitio no necesita reconstrucción. T1 está resuelto. T3 es el bloque más trabajado y funciona
(insignia PNG y código de finalización probados en producción). **T2 micro:bit es el hueco, y más
profundo de lo que parecía**: no es sólo que falten dibujos.

### T2 micro:bit

- Los 30 retos y el PDF de `materiales/retos-microbit.pdf` (feb-2026, «1.º ESO A · 2025/26») son
  el mismo texto; el PDF no tiene ni una imagen. **No hay un solo bloque de MakeCode dibujado en
  todo el trimestre.**
- **Secuencia didáctica al revés:** r03 y r05 consultan el botón con «Si botón A pulsado» dentro
  de «Para siempre», y r06 presenta `al presionar botón A` como «tu primer control con botones».
  El hub dice que se evalúa «distinguir cuándo usar eventos». En T1 ya usan las dos formas (la
  pala del Arkanoid va con `¿tecla presionada?` en `por siempre`) y T2 no se apoya en ello.
- **Errores de hecho:** r11 propone «cambiar el color de las filas… necesitarás una micro:bit V2»
  (la matriz de la V2 es roja igual); r18 dice que la placa «vibrará» (no tiene vibrador); r28 se
  presenta como «versión avanzada del Reto 15» (piedra-papel-tijera; el de esquivar es el r17).
- **Fuera de nivel tal como están:** r18 (distancia euclídea con raíz cuadrada sobre el
  acelerómetro), r27 (tres sprites a mano, siete variables), r28 (arrays). r17 y r27 encajan con
  la categoría Juego de MakeCode; r18 se reformula como «frío/caliente» con una sola inclinación
  y valor absoluto; r28 fuera o como reto de proyecto.
- **El hub promete lo que no existe:** «el trimestre culmina con un proyecto en parejas que
  combina sensores y radio» y «la evaluación combina los retos, el cuaderno del alumno y el
  proyecto final». No hay página de proyecto ni definición de ese cuaderno. Teoría y actividades
  siguen «en construcción» en la navegación de los 30 retos.
- Hardware sin declarar (servo r20–r22, dos placas r24 y r29, micrófono V2 r25, altavoz r26,
  LEDs externos en el extra de r22); sólo 2 de 30 dicen qué se entrega; «Entrega Moodle» va al
  login genérico; restos de H4 (insignias vacías, «Consejo» partido, Title Case). Con unas 20
  clases reales, 30 retos al mismo peso no caben.

### T1 Scratch

- **Bug del quiz (corregido en el commit f9a1950):** la explicación se insertaba con
  `textContent` y 30 explicaciones de 14 páginas mostraban `<b>`/`<em>` como texto.
- **Oportunidad:** los programas ya son datos en los generadores. Con esa fuente se pueden
  generar `.sb3` reales: las tres bases funcionando para enseñar el primer día del proyecto o dar
  a quien se queda atrás, y una comprobación mecánica de que cada programa dibujado carga.

### T3 Ciberseguridad

- Técnico: `s02.html` carga `s02.js` dos veces; los 10 retos sin `main`, salto ni pie, con 38
  controles sin etiqueta y 3 `onclick` en `div` sin teclado; no están en el sitemap.
- **Ordenadores compartidos:** identidad y progreso viven en `localStorage`; la pareja siguiente
  abre la sesión con los nombres de la anterior ya escritos y sus insignias en `progreso.html`.
  Hace falta una confirmación de pareja al empezar cada sesión.
- El código de finalización es un hash de nombres|sesión|puntuación|fecha (verificable), pero no
  hay herramienta que lo recalcule: hoy es disuasorio. Sólo merece página de verificación si
  Manuel comprueba códigos al corregir.
- La identidad de la Academia no se toca: es una virtud.

### Transversal

- Se servían públicamente `CLAUDE.md`, `README.md`, `.gitignore`, `node_modules/` (24 MB),
  `scripts/` y `assets/templates/`. Corregido en el commit de higiene (este).
- `.git` pesa 40 MB por el historial de `node_modules`; se queda así.
- Los tests automáticos sólo cubren T1.
- Documentación interna atrasada: `PROGRAMACION.md` dice que T2 está «sin sesiones», describe un
  T3 que ya no existe (v3, cuadernillo v6, `moodle.html`) y lista «cuatro» juegos de ampliación
  con cinco nombres; `PENDIENTES.md` es un historial con infraestructura ya hecha.

### Lo que no se hace

Buscador, fuentes locales, portada, unificar T3, gamificar T1, papel, páginas antiguas de juegos.

### Orden acordado con Manuel (14-sept-2026)

1. Bug del quiz de T1 — **hecho** (f9a1950).
2. Higiene de despliegue — **hecho** (este commit).
3. T3 técnico con alcance contenido + confirmación de pareja. Verificación de códigos, sólo si
   se van a comprobar.
4. Tabla de clasificación de los 30 retos de T2 (`CLASIFICACION_RETOS_T2.md`): bloques nuevos,
   propuesta troncal/ampliación/proyecto/fuera, hardware, problema detectado, entrega. **Antes de
   tocar nada de T2.**
5. Manuel decide troncal (12–14 para ~20 clases) y si hay proyecto final corto en parejas.
6. Cotejo de nombres de bloques en MakeCode en español + `makecodesvg.py` + matriz 5×5.
7. Regenerar sólo el troncal con `documentacion/generadores-t2/` y el esqueleto de T1; errores
   de hecho corregidos; eventos antes que consulta.
8. Ampliaciones en formato ligero; presentación; fuera teoría/actividades; hub sin promesas vacías.
9. Exportador `.sb3` de T1 y tests para T2 y T3. La documentación se corrige en los mismos commits.

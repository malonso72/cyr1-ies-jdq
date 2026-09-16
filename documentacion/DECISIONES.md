# Decisiones de diseño · CyR 1º ESO

Bitácora de decisiones técnicas y editoriales del proyecto.
Formato: `YYYY-MM-DD · Decisión` con justificación.

## 2026-05-10 · Bootstrap del sitio (v1.0.0)

- **Modelo de referencia:** `teci2-ies-jdq` (TECI II, 2º Bach.) y `tyd2-ies-jdq`
  (TyD 2º ESO, hermano construido el mismo día). Misma filosofía vanilla,
  misma tipografía, misma estructura modular de CSS/JS.
- **Paleta verde-cian** (`--principal #1A8A6B` + acento naranja `#D4700A`)
  para diferenciar visualmente del azul TECI y del naranja TyD.
- **Estructura por trimestres**, no por unidades cortas. Cada trimestre cubre
  un bloque temático grande (Scratch / micro:bit / Ciberseguridad). Carpeta
  raíz `trimestres/` (no `unidades/`) y carpeta `retos/` (no `proyectos/`)
  porque encajan mejor con la semántica del curso. Esta decisión se confirmó
  con Manuel el 2026-05-10 tras la Fase B.
- **T3 Ciberseguridad con sub-organización por sesiones**: dado el volumen
  de material existente (cuadernillo v6 + presentación pizarra v3 + 16-17
  sesiones tipo "Opción D" + templates Moodle), se mantiene una estructura
  específica con `presentacion.html`, `cuadernillo.html`, `moodle.html` y
  `sesiones/sNN.html`. T1 y T2 usan la estructura genérica
  `teoria.html` / `actividades.html` igual que las unidades TyD.
- **Presentación pizarra v3 conserva su estética dark**: cuando se integre en
  Fase E, NO se modificará su CSS interno. La presentación es para proyectar
  y su estética es independiente del resto del sitio.
- **Solucionarios privados** en `_soluciones/`, excluido del despliegue vía
  `.assetsignore` (convención TECI).

## Convenciones

- Slug de trimestre: `tN-kebab-case` con un solo dígito (`t1-`, `t2-`, `t3-`).
  Si se añade un T4 hipotético, ningún problema.
- Slug de sesión (Fase E): `sNN.html` con dos dígitos (`s01`, `s02`, ...,
  `s16` o `s17`).
- Commits: español, verbo en imperativo, versión al final entre corchetes.
- Sin frameworks. Sin CDNs salvo Google Fonts y MathJax (cuando aplique).

## 2026-09-16 · T3 tiene por fin su propia red de seguridad

T1 y T2 se generan y cada taller trae su test; T3 se edita a mano y no tenía ninguno. Ahora
está `documentacion/pruebas-t3/test_academia.js` (2120 comprobaciones sobre las 32 páginas y
sobre `academia.js`, con jsdom y un servidor de ficheros falso, porque el navegador simulado
sólo da `localStorage` a un origen `http`). Su README dice qué comprueba.

La primera pasada sacó **55 fallos reales**, todos arreglados:

- **Faltaba el `canonical` en 30 páginas** de T3 —las 18 sesiones, los 10 retos, el hub y
  `progreso.html`—, cuando T1 y T2 lo llevan en todas. Añadido.
- **Los 10 retos no tenían `description`.** Escrita una para cada uno.
- **Tres retos no tenían pie** y el del Tribunal Digital usaba una etiqueta inventada
  (`<footer-legal>`), que no es una región del documento: ahora es `<footer class="legal">`,
  con el mismo aspecto.
- **Nueve campos sin etiqueta accesible** en S01 y S02 (los laboratorios de contraseñas y el
  mapa de cuentas). Resueltos con `aria-label`, no con etiquetas visibles, porque el texto ya
  está en el título del laboratorio y duplicarlo se leería dos veces.
- **El hub del trimestre no tenía skip-link.**

Y dos decisiones que tomé por mi cuenta:

- **La tienda falsa de V-Bucks (`s16-reto-vbucks.html`) pasa a `noindex` y sale del
  `sitemap.xml`** (100 URL). Es una imitación de una tienda real hecha para clase: sirve
  abierta desde la sesión 16, pero no tiene por qué aparecer en un buscador, donde llegaría a
  quien no sabe que es un ejercicio. Es la única página de T3 a la que **no** se le ha puesto
  pie: el nombre del instituto al final destriparía la simulación. Las dos cosas están
  anotadas como excepción dentro del propio test.
- **S12-alt y S13 no se completan con un informe genérico** porque piden palabras clave del
  tema. No es un fallo, es a propósito, así que el test sólo exige que la página diga qué
  falta en vez de quedarse callada.

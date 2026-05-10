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

# Pendientes · CyR 1º ESO

Lista de lo que queda por completar. Se actualiza con cada sprint.

## ✅ v1.1.0 — Integración "scratch integrado" (mayo 2026)

Esta integración (paquete `cyr1-ies-jdq-scratch-integrado.zip`) ha cerrado la
mayor parte de la Fase E del brief y ha publicado material completo para
los tres trimestres.

### T1 · Scratch — publicado
- [x] **Presentación inicial** del bloque (`trimestres/t1-scratch/presentacion.html`).
- [x] **20 sesiones** (s01–s20) en `trimestres/t1-scratch/sesiones/`.
- [x] **12 juegos** (pong, naves, arkanoid, laberinto, space-invaders, etc.)
  en `trimestres/t1-scratch/juegos/`.
- [x] **Proyectos finales** (ideas, checklist, índice) en `trimestres/t1-scratch/proyectos/`.
- [x] **Cuadernillo Scratch parte 1** (PDF, optimizado a 6 MB).
- [x] **Guías de los 11 juegos** (PDFs) en `materiales/guias-juegos/`.
- [x] Badge "Próximamente" eliminado de la tarjeta T1 del index raíz.

### T2 · micro:bit — publicado
- [x] **Presentación inicial** del bloque (`trimestres/t2-microbit/presentacion.html`).
- [x] **30 retos** (r00–r29) en `trimestres/t2-microbit/retos/`.
- [x] **Cuadernillo de retos** (PDF) en `materiales/retos-microbit.pdf`.
- [x] Badge "Próximamente" eliminado de la tarjeta T2 del index raíz.

### T3 · Ciberseguridad — Fase E completada (versión inicial)
- [x] **Presentación pizarra** integrada (`presentacion.html`).
- [x] **Cuadernillo del alumno** (v7) integrado: HTML + PDF imprimible en
  `materiales/cuadernillo-ciberseguridad-1eso-v7.pdf`.
- [x] **19 sesiones** (s01–s19) integradas — el conteo final son 19, no 16-17
  como decía la versión inicial del brief.
- [x] **Moodle**: `trimestres/t3-ciberseguridad/moodle.html` con templates y rúbrica.
- [x] Badges "Pendiente Fase E" eliminados de las 4 tarjetas del hub T3.

### Infraestructura del sitio tras la integración
- [x] **`sitemap.xml`** regenerado con las 100 URLs publicadas.
- [x] **Navegación transversal** ampliada en `teoria.html`/`actividades.html`
  de T1 y T2 para incluir Sesiones, Juegos, Proyectos y Retos.
- [x] **Auditoría de enlaces internos**: 0 enlaces rotos sobre 1.178.
- [x] **Auditoría de imágenes huérfanas**: 0 huérfanas.

## ✅ v2.0.0 — Rework T3 "Bitácora de investigación" (mayo 2026)

Reescritura completa del trimestre de Ciberseguridad a partir del
nuevo cuadernillo (`Cuadernillo_Ciberseguridad_1ESOB_FINAL.pdf`, 62 pp.).

### Cambios estructurales
- [x] **Borrado** del T3 anterior: 19 sesiones (s01–s19), `presentacion.html`,
  `cuadernillo.html` (v6/v7), `moodle.html` y PDF v7. Backup en
  `outputs/t3-backup-pre-rework/`.
- [x] **18 sesiones nuevas** (s01–s18) en formato "Bitácora de investigación":
  cada una con Misión · Herramientas · Pasos · Para pensar.
- [x] **Cuadernillo web nuevo** (`cuadernillo.html`): presentación, normas, índice y descarga.
- [x] **PDF nuevo** en `materiales/cuadernillo-ciberseguridad-1eso.pdf` (62 pp., 2,7 MB).
- [x] **Hub T3 reescrito**: trabajo en parejas, "saber/hacer/evaluar" actualizado a
  vocabulario de investigación (OSINT, deepfakes, ingeniería social…).
- [x] **`sesiones/index.html`** rehecho con las 18 sesiones, indicador de
  materiales auxiliares y enlace al PDF.
- [x] Acceso a Moodle ahora es **enlace externo** directo a la plataforma
  de la Junta (ya no hay página `moodle.html` local).
- [x] **`sitemap.xml`** regenerado con 97 URLs.
- [x] **Auditoría de enlaces**: 0 rotos sobre 1.172.

### Pendientes del nuevo T3
- [ ] **Solucionario** del nuevo cuadernillo (si Manuel lo elabora aparte):
  guardar en `_soluciones/cuadernillo_solucionario_bitacora.html` (privado).
- [ ] Revisar los **materiales auxiliares** referenciados en las sesiones
  S09, S10, S13, S16 y S17: por ahora solo aparece el aviso "incluye material
  auxiliar" en cada sesión. Si se quiere mostrar el contenido extra en la
  página web (capturas, casos), habría que crear secciones específicas o
  páginas adicionales.

## Pendientes de Manuel (no bloqueantes)

- [ ] **Criterios de evaluación LOMLOE concretos** por trimestre. Rellenar el
  `<details class="criterios">` de cada hub.
- [ ] **Bullets de "saber/hacer/evaluar"**: los actuales son una primera
  aproximación. Revisar y ajustar a la programación oficial del departamento.
- [ ] **Duración estimada**: rangos orientativos. Validar con la dotación
  real del curso (depende de cuántas sesiones/semana tenga la asignatura).
- [ ] **Retos transversales**: definir los retos que cruzarán varios
  trimestres y crearlos desde `assets/templates/PLANTILLA_reto.html`.
- [ ] **Herramientas**: añadir editor Scratch online, simulador micro:bit,
  glosario de seguridad, etc.

## Infraestructura

- [ ] **`git init`**: el sistema en el que se generó este repo no tenía
  git instalado. Manuel debe ejecutar al recibirlo:
  ```bash
  cd cyr1-ies-jdq && git init -b main && git add . && \
  git commit -m "Bootstrap del sitio CyR 1º ESO [v1.0.0]"
  ```
- [ ] **Configuración del worker Cloudflare**: crear el subdominio
  `cyr1-ies-jdq.malonso72.workers.dev`. Probar primer deploy con
  `npx wrangler deploy`.
- [ ] **Google Search Console**: añadir verificación si se quiere indexar.
- [ ] **Contador de visitas**: decidir si se añade GoatCounter como en TECI.

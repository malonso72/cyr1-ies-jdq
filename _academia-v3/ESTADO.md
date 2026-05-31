# Estado de la Academia Cyber-IES (v3)

> Documento para retomar el proyecto en una conversación nueva.
> Última actualización: **bloque 18/18 COMPLETO + migrado al sitio principal** (S9 y S11 creadas; Academia v3 ya sirve en `/trimestres/t3-ciberseguridad/`).

## ¿Qué es esto?

Rediseño completo del bloque T3 (Ciberseguridad) de CyR 1º ESO. El objetivo es **eliminar el cuadernillo en papel** y convertir cada sesión en un HTML autónomo de 30-50 min con la misma plantilla pedagógica.

- **Carpeta de trabajo:** `_academia-v3/` (dentro de `cyr1-ies-jdq/`)
- **NO toca aún** la versión anterior del sitio (`trimestres/t3-ciberseguridad/`). La migración es el último paso pendiente.

## Plantilla maestra (6 bloques por sesión)

1. **🎯 Misión** — gancho narrativo emocional
2. **📖 Teoría interactiva** — 4-6 conceptos × 3 sub-pantallas (qué es / cómo lo reconoces / microquiz)
3. **🏋️ Entrenamiento** — 6 frases V/F
4. **🎮 Reto principal** — mecánica DISTINTA en cada sesión (catálogo abajo)
5. **📝 Informe** — 3 preguntas con validación robusta (mínimo 8 palabras de 2+ caracteres y 25 letras)
6. **🏆 Insignia** — diploma PNG generado con canvas

Más detalles: `_academia-v3/PLANTILLA.md`

## Estado de sesiones (18/18 LISTAS ✅)

| Sesión | Estado | Mecánica única |
|---|---|---|
| **S1** Las palabras del oficio | ✅ LISTA | Glosario + 3 impostores creíbles |
| **S2** Contraseñas | ✅ LISTA | Laboratorio "Hackea a Sofía" + ranking + auditoría personal |
| **S3** Caza al phisher | ✅ LISTA | Simulador SOC con cronómetro 15s · 10 URLs |
| **S4** Lo que internet sabe de ti | ✅ LISTA | Launcher HIBP + MyActivity + WhatsMyName |
| **S5** Interland (parte 1) | ✅ LISTA | Launcher Interland Google + 2 mundos |
| **S6** Interland (parte 2) | ✅ LISTA | Launcher Interland + 2 mundos finales |
| **S7** Perfil de riesgo | ✅ LISTA | 5 perfiles ficticios · BAJO/MEDIO/ALTO |
| **S8** Escape Room CCN | ✅ LISTA | Launcher al escape oficial CCN-CERT |
| **S9** Escape PIENSA | ✅ LISTA | Envoltorio + iframe a `retos/s09-reto-piensa.html` · 6 técnicas ingeniería social · código PIENSA |
| **S10** WhatsApp sospechoso | ✅ LISTA | 8 capturas · seguro/sospechoso/estafa |
| **S11** Wifi café trampa | ✅ LISTA | Envoltorio + iframe a `retos/s11-reto-wifi.html` · 5 redes + aventura de Ana |
| **S12** Tribunal Digital (antes "Derecho al Olvido") | ✅ LISTA | Envoltorio + iframe al panel jurídico |
| **S13** Caso Lucía OSINT | ✅ LISTA | Envoltorio + iframe a la investigación |
| **S14** Real / Fake | ✅ LISTA | Envoltorio + iframe al torneo deepfakes |
| **S15** Mesa del Detective | ✅ LISTA | Envoltorio + iframe a la mesa Cluedo |
| **S16** Gaming · V-Bucks | ✅ LISTA | Envoltorio + iframe a la tienda falsa |
| **S17** Caso Marta Ruiz | ✅ LISTA | Envoltorio + iframe a la carpeta del fraude |
| **S18** Examen del Analista | ✅ LISTA (cierre) | Envoltorio + iframe al examen + diploma final |

## Hecho en esta tanda (31/05/2026)

### 1. Sesiones S9 y S11 ✅ (envoltorio + iframe, patrón S12-S18)

- Retos completos copiados desde `Downloads/ciberseguridad/htmls/`:
  - `Escape_Room_S9_v6.html` → `_academia-v3/retos/s09-reto-piensa.html`
  - `Wifi_Trampa_S11_v2.html` → `_academia-v3/retos/s11-reto-wifi.html`
- Envoltorios creados: `s09.html`+`s09.js` y `s11.html`+`s11.js` (CONCEPTOS, FRASES_VF, `marcarRetoHecho`, iframe, insignia PNG).
  - S9: 5 conceptos de ingeniería social + 6 V/F · insignia final "Cortafuegos Humano".
  - S11: 5 conceptos de wifi público + 6 V/F · insignia final "Guardián del Wifi".
- Hub `index.html`: tarjetas S9/S11 ya activas; aviso "prototipo" → "bloque completo".

### 2. Migración al sitio principal ✅ (Academia v3 ya sirve en `/trimestres/t3-ciberseguridad/`)

- Hub, `assets/` (academia.css/js), `sesiones/` (s01-s18 + js) y `retos/` copiados a `trimestres/t3-ciberseguridad/`.
- **Rutas relativas reajustadas a la nueva profundidad**: raíz pasa de `../`→`../../` (hub) y `../../`→`../../../` (sesiones) para favicon, `common.css`, `common.js` e índice del sitio. Las rutas internas de la Academia (`../assets/...academia`, `../index.html`, `../retos/...`) se mantienen.
- `cuadernillo.html` y `sesiones/index.html` convertidos en **redirecciones** (noindex) al nuevo hub. La versión v2 anterior queda archivada en `trimestres/t3-ciberseguridad/_legacy-v2/`.
- PDF del cuadernillo **conservado** en `materiales/` (sigue accesible por URL, ya no enlazado desde el hub).
- `sitemap.xml` regenerado: `lastmod` de S1-S18 + hub T3 a 2026-05-31; eliminadas las entradas de `cuadernillo.html` y `sesiones/` (ahora redirecciones). XML válido (95 URLs).
- `.assetsignore`: excluidos de la publicación `_academia-v3/` (fuente editable) y `_legacy-v2/` (evita contenido duplicado).
- Tarjeta T3 del índice raíz actualizada ("Academia Cyber-IES: 18 sesiones interactivas").
- **Auditoría de enlaces**: 221 enlaces internos del T3 verificados, 0 rotos.

## Pendiente / decisiones con Manuel

- **Validar en el navegador** S9 y S11 (escape PIENSA y aventura de Ana en iframe + descarga de insignia).
- ¿Eliminar definitivamente el PDF del cuadernillo de `materiales/` o dejarlo como referencia legacy? (ahora conservado, sin enlazar).
- ¿Reescribir la presentación de pizarra del T3 con el lenguaje "Academia Cyber-IES"?
- ¿Crear una **página de progreso global** con las 18 insignias del alumno?
- Actualizar `documentacion/PENDIENTES.md` con la versión v3.0.0 (no tocado aún).

## Arquitectura técnica

```
_academia-v3/
├── index.html                  # Hub de la Academia (todas las sesiones)
├── PLANTILLA.md                # Plantilla maestra documentada
├── ESTADO.md                   # Este documento
├── gen_sesiones_nuevas.py      # Generador de plantilla para sesiones
├── gen_sesiones_data.py        # Datos de S4-S8 y S10 + ejecutor
├── adaptar_reto_s12.py         # Script único para reformular reto S12
├── assets/
│   ├── css/academia.css        # CSS de los 6 bloques + simulador SOC
│   └── js/academia.js          # Utilidades: Academia.X (identidad, persistencia, diploma PNG, validación informe)
├── sesiones/
│   ├── s01.html (JS inline)    # S1 (única con JS embebido)
│   ├── s02.html + s02.js       # S2
│   ├── s03.html + s03.js       # S3 (simulador SOC con cronómetro)
│   ├── s04.html + s04.js       # S4
│   ├── s05.html + s05.js       # S5
│   ├── s06.html + s06.js       # S6
│   ├── s07.html + s07.js       # S7 (galería de perfiles)
│   ├── s08.html + s08.js       # S8 (launcher CCN)
│   ├── s10.html + s10.js       # S10 (galería de WhatsApps)
│   ├── s12.html + s12.js       # S12-S18 (envoltorio + iframe)
│   ├── s13.html + s13.js
│   ├── s14.html + s14.js
│   ├── s15.html + s15.js
│   ├── s16.html + s16.js
│   ├── s17.html + s17.js
│   └── s18.html + s18.js
└── retos/                      # HTMLs ORIGINALES (standalone) usados vía iframe
    ├── s09-reto-piensa.html    # ← Escape PIENSA (copiado de Escape_Room_S9_v6.html)
    ├── s11-reto-wifi.html      # ← Wifi-trampa + Ana (copiado de Wifi_Trampa_S11_v2.html)
    ├── s12-reto-dpo.html       # ← este SÍ está editado (Tribunal Digital)
    ├── s13-reto-lucia.html
    ├── s14-reto-realfake.html
    ├── s15-reto-detective.html
    ├── s16-reto-vbucks.html
    ├── s17-reto-marta.html
    └── s18-reto-examen.html
```

> **Nota:** `_academia-v3/` es ahora la **fuente editable** (excluida de la publicación). La versión que sirve Cloudflare vive en `trimestres/t3-ciberseguridad/` (misma estructura, rutas a raíz con un `../` más de profundidad). Para futuros cambios: editar en `_academia-v3/` y volver a copiar con el reajuste de rutas, o editar directamente en `trimestres/t3-ciberseguridad/`.

## Decisiones de diseño importantes

1. **Race condition al cargar:** todas las sesiones (excepto S1) usan `function initSesion() {...}` + `if (document.readyState !== 'loading') initSesion(); else document.addEventListener(...)` en vez del `window.addEventListener('DOMContentLoaded', ...)` clásico, que daba problemas con la carga lazy. **NO ROMPER esto al editar.**

2. **Validación del informe:** `Academia.respuestaInformeValida(texto, 8, 25)` rechaza spam tipo "f f f f f f f f". Mínimo 8 palabras DE 2+ CARACTERES y 25 letras alfabéticas totales.

3. **Reto en iframe (S9, S11, S12-S18):** los retos originales se cargan vía `<iframe src="../retos/sNN-reto-X.html">`. NO hace falta tocar los retos: el envoltorio académico añade misión/teoría/entrenamiento/informe alrededor.

4. **Diploma PNG:** generado dinámicamente con canvas en `Academia.descargarDiploma(opts)`. NO necesita servidor.

5. **Persistencia:** todo en `localStorage` con clave `academia:s:sNN` por sesión y `academia:nombre1/2` para identidad. Sin backend.

6. **Reto S12 modificado in-place:** el HTML del reto DPO se editó para hablar "Tribunal Digital" en vez de "Despacho del DPO". Los demás retos (S13-S18) NO se han tocado.

## Bugs conocidos resueltos en esta versión

- ✅ Race condition de `DOMContentLoaded` (tarjetas no aparecían en S12, S13)
- ✅ Validación informe permitía "f f f f f f f f" como válido
- ✅ Diploma de S2 mostraba solo nombre2 (faltaba nombre1)
- ✅ S12 con vocabulario adulto (DPO, expediente) → reformulada como Tribunal Digital
- ✅ Bug `opc-sit-X` en S1 (contenedor de opciones perdido al reconstruir)

## Cómo arrancar el chat nuevo

El bloque está **completo (18/18) y ya migrado** al sitio principal. Para el siguiente paso, decir algo como:

> Estoy retomando el proyecto Academia Cyber-IES. Lee primero
> `_academia-v3/ESTADO.md` para situarte. El bloque ya está al 100% y servido en
> `/trimestres/t3-ciberseguridad/`. Ahora quiero [validar S9/S11 / crear la página
> de progreso global con las 18 insignias / actualizar la presentación de pizarra / …].

Recordatorio: editar en `_academia-v3/` (fuente) y recopiar a `trimestres/t3-ciberseguridad/` con el reajuste de rutas, o editar directamente la versión publicada.

# CyR 1º ESO · IES Jiménez de Quesada

**Computación y Robótica · 1º ESO · Curso 2025-26**
Profesor: Manuel Alonso Herrera · Santa Fe (Granada)

Sitio estático servido por Cloudflare Workers Static Assets en
[cyr1-ies-jdq.malonso72.workers.dev](https://cyr1-ies-jdq.malonso72.workers.dev).

## Estructura

```
cyr1-ies-jdq/
├── index.html                      Hub principal con los 3 trimestres
├── trimestres/
│   ├── t1-scratch/                 Programación por bloques
│   │   ├── index.html              Hub del trimestre
│   │   ├── teoria.html
│   │   ├── actividades.html
│   │   └── img/
│   ├── t2-microbit/                Computación física
│   │   └── (igual estructura)
│   └── t3-ciberseguridad/          Seguridad digital
│       ├── index.html              Hub
│       ├── presentacion.html       Slides pizarra v3 (Fase E)
│       ├── cuadernillo.html        Cuadernillo v6 (Fase E)
│       ├── moodle.html             Templates + rúbrica (Fase E)
│       ├── sesiones/
│       │   ├── index.html          Listado de las 16-17 sesiones
│       │   └── sNN.html            (se generan en Fase E)
│       └── img/
├── herramientas/                   Editores online, simuladores, glosarios
├── retos/                          Retos transversales
├── _soluciones/                    Privado, NO se despliega
├── img/                            fachadaiesjdq.jpg, logoantiguo.jpg
├── assets/
│   ├── css/                        common, hub, unidad, proyecto
│   ├── js/                         common, header, search
│   └── templates/                  PLANTILLA_*
├── documentacion/                  Privado: PROGRAMACION, DECISIONES, PENDIENTES
└── scripts/                        Auditoría
```

## Despliegue

```bash
# Test local
python3 -m http.server 8000

# Validación pre-push
python3 scripts/comprobar_enlaces.py
python3 scripts/auditar_imagenes_huerfanas.py
python3 scripts/auditar_archivos_pesados.py --umbral 300

# Deploy (Cloudflare)
npx wrangler deploy
```

## Versionado

SemVer. Versión actual visible en pie del index.

- `1.0.X` parche: errata, ajuste menor
- `1.X.0` menor: añadir contenido a un trimestre
- `X.0.0` mayor: añadir o reorganizar trimestres

## Convenciones

- HTML + CSS + JS vanilla. Sin frameworks.
- Tipografía: Barlow + Barlow Condensed + JetBrains Mono.
- Paleta: verde-cian (`--principal #1A8A6B`) con acento naranja (`#D4700A`).
- Accesibilidad: skip-link, focus-visible, alt en imágenes, contraste AA.
- Modo impresión: oculta navegación, expande soluciones.

Modelo de referencia: `teci2-ies-jdq` (TECI II) y `tyd2-ies-jdq` (TyD 2º ESO).

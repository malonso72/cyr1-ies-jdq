# Programación didáctica · CyR 1º ESO

**Curso:** 2026-27 · IES Jiménez de Quesada · Profesor: Manuel Alonso Herrera

## Distribución temporal

CyR de 1º ESO tiene **2 sesiones semanales**. Cada trimestre cubre un bloque
distinto:

| Evaluación | Trimestre | Sesiones escritas |
|---|---|---|
| 1.ª evaluación | T1 Scratch | 20 |
| 2.ª evaluación | T2 micro:bit | — (pendiente) |
| 3.ª evaluación | T3 Ciberseguridad | 18 |

> **Las 20 sesiones no llenan el trimestre, y es a propósito.** A 2 sesiones
> por semana son unas 10 semanas, y el primero da para unas 13. Esas clases de
> más **se cubren con los juegos guiados** de `t1-scratch/juegos/`, que por eso
> no son un extra sino parte de la programación. Y de paso son el colchón de
> las sesiones que se comen dos clases —la S09 del quiz, la S12 del laberinto y
> la S18 de construcción son las candidatas—: no hay que llegar a la S16
> «porque tocaba».

### Los juegos guiados

Once páginas en `t1-scratch/juegos/`, cada una con su guía en PDF en
`t1-scratch/materiales/guias-juegos/`. Están clasificados por nivel en su
índice: obligatorios, intermedio, ampliación, avanzado y extra.

**Ojo con el solape:** cuatro de ellos ya son sesiones completas —carreras es
la S10, laberinto son la S12 y la S13, piedra-papel-tijera es la S14 y pong son
la S15 y la S16—, y esas sesiones ya enlazan su PDF como material de apoyo. Los
que de verdad aportan clases nuevas son los otros siete: Space Invaders,
Arkanoid, Bomb Jack, naves, tres en raya, cumpleaños feliz y carrera de autos.

## Listado de trimestres

| # | Slug | Título | Sesiones | Estado del material |
|---|---|---|---|---|
| T1 | `t1-scratch` | Scratch | 20 | **Completo**: hub, índice, presentación y las 20 sesiones. Se generan desde `generadores-t1/` |
| T2 | `t2-microbit` | micro:bit | — | Hub + placeholders. Sin sesiones |
| T3 | `t3-ciberseguridad` | Ciberseguridad | 18 | Hub «Academia Cyber-IES» + 18 sesiones + retos |

## Estructura interna de T3 Ciberseguridad

Por la cantidad de material existente, T3 es el más estructurado:

- `presentacion.html` — Presentación HTML pizarra v3 (estética dark independiente, no se migra)
- `cuadernillo.html` — Cuadernillo v6 del alumno (DOCX o HTML según origen)
- `sesiones/sNN.html` — 16-17 sesiones tipo "Opción D" (CC cuenta el número exacto antes de generar)
- `moodle.html` — Templates de entrega + rúbrica de 4 criterios
- `_soluciones/cuadernillo_solucionario_v6.html` — privado (NO se despliega)

## Criterios de evaluación

Pendientes de concretar según los descriptores LOMLOE de Andalucía para
Computación y Robótica 1º ESO. Anotar en cada `<details class="criterios">`.

## Estándares y competencias

Competencias clave LOMLOE relacionadas:
- **Competencia digital (CD)** — núcleo de la asignatura
- **Competencia matemática y en STEM** — pensamiento computacional
- **Competencia en aprender a aprender (CAA)** — depuración, autorrevisión
- **Competencia ciudadana (CC)** — privacidad, ética digital, ciberseguridad

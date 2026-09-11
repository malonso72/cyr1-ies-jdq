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

> **El material no llena el trimestre, y es a propósito.** A 2 sesiones por
> semana, las 20 de Scratch son unas 10 semanas y el primer trimestre da para
> más. Ese margen es el colchón: hay sesiones que se van a comer dos clases
> —la S09 del quiz, la S12 del laberinto y la S18 de construcción son las
> candidatas— y no pasa nada, porque no hay que llegar a la S16 «porque
> tocaba». Vale más que entiendan bien variables y condicionales.

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

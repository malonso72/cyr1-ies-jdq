# Programación didáctica · CyR 1º ESO

**Curso:** 2026-27 · IES Jiménez de Quesada · Profesor: Manuel Alonso Herrera

## Distribución temporal

CyR de 1º ESO tiene **2 sesiones semanales**. Cada trimestre cubre un bloque
distinto:

| Evaluación | Trimestre | Sesiones escritas |
|---|---|---|
| 1.ª evaluación | T1 Scratch | 20 |
| 2.ª evaluación | T2 micro:bit | 15 troncales + 12 ampliaciones |
| 3.ª evaluación | T3 Ciberseguridad | 18 |

> **Las 20 sesiones no llenan el trimestre, y es a propósito.** A 2 sesiones
> por semana son unas 10 semanas, y el primero da para unas 13. Esas clases de
> más **se cubren con los juegos guiados** de `t1-scratch/juegos/`, que por eso
> no son un extra sino parte de la programación. Y de paso son el colchón de
> las sesiones que se comen dos clases —la S09 del quiz, la S12 del laberinto y
> la S18 de construcción son las candidatas—: no hay que llegar a la S16
> «porque tocaba».

### El proyecto final y los juegos

Las clases de más se van en el **proyecto final**, que no es un juego inventado
sino **uno completo elegido entre tres bases**, en `t1-scratch/juegos/`:

| Opción | Cuánto cuesta | Se apoya en |
|---|---|---|
| A · Arkanoid | Media | El Pong entero (S15 y S16) |
| B · Space Invaders | La más larga | S05, S08 y S11 |
| C · Esquivar lo que cae | La más corta | Cuatro piezas del kit de la S18 |

Las tres están escritas en Scratch 3 y con el formato de las sesiones. **Lo que
se evalúa no es el juego, es la versión de cada uno**: la ficha de la S17 pide
tres cambios concretos sobre la base. Así se puede mandar el mismo juego a toda
la clase sin que las presentaciones de la S20 sean todas iguales.

En la misma carpeta quedan otros ocho juegos, con sus guías en PDF en
`t1-scratch/materiales/guias-juegos/`:

- **Cuatro ya son sesiones** —carreras es la S10, laberinto la S12 y la S13,
  piedra-papel-tijera la S14 y pong la S15 y la S16— y el índice lo dice.
- **Cuatro son ampliación** para quien quiera seguir por su cuenta: tres en
  raya, naves, bomb-jack, carrera de autos y cumpleaños feliz.

> **Las once guías en PDF están hechas con Scratch 2**, igual que el cuadernillo,
> y sus bloques son capturas: no se pueden corregir con una nota. Se enlazan como
> consulta y con aviso, nunca como material de trabajo.

## Listado de trimestres

| # | Slug | Título | Sesiones | Estado del material |
|---|---|---|---|---|
| T1 | `t1-scratch` | Scratch | 20 | **Completo**: hub, índice, presentación y las 20 sesiones. Se generan desde `generadores-t1/` |
| T2 | `t2-microbit` | micro:bit | 15 (+12) | **Completo**: hub, índice y 30 páginas de reto con bloques dibujados. Se generan desde `generadores-t2/`, presentación incluida |
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

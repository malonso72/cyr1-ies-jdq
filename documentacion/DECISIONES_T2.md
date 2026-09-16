# Decisiones tomadas al reconstruir T2 · micro:bit (septiembre de 2026)

Lo que Claude decidió por su cuenta al pasar los 30 retos en pseudocódigo a páginas generadas
con bloques dibujados, siguiendo `CLASIFICACION_RETOS_T2.md` (que Manuel cerró) y el
`COTEJO_MakeCode.md`. Para que Manuel lo revise de una vez.

1. **Numeración nueva y archivos nuevos.** El troncal son `retos/r01…r15.html` («Reto 1…15»)
   en el orden pedagógico, no en el del PDF; las ampliaciones `a01…a12` («Ampliación N») y
   las de servo `m01…m03` («Sin material N»). Los archivos antiguos `r00`, `r16…r29`,
   `teoria.html` y `actividades.html` se han borrado, y los `r01…r15` tienen ahora otro
   contenido. Un enlace antiguo de Moodle a `r03.html` lleva a un reto válido, aunque otro.
   El PDF `materiales/retos-microbit.pdf` (curso 2025/26) no se enlaza desde ninguna página:
   es el pseudocódigo antiguo y ya no coincide.
2. **Cada página lleva su entrega.** `microbit-RetoN_TuNombre.hex` a Moodle, con el nombre
   escrito en la casilla del proyecto antes de descargar, y cómo copiarlo a la unidad MICROBIT.
3. **Eventos antes que consulta en bucle.** El reto 3 presenta `al presionarse el botón`; en
   todo el troncal no se consulta ningún botón dentro de `para siempre`. El patrón «el bucle
   trabaja, los eventos mandan» se nombra en el reto 8 y se reutiliza en el 15.
4. **Medir antes de decidir un umbral.** El reto 5 y las ampliaciones de sensores obligan a
   mostrar el valor del sensor antes de elegir el número. Los umbrales de las páginas son
   orientativos y se dice.
5. **Errores del PDF corregidos:** la V2 no cambia de color (fuera del termómetro), la placa no
   vibra (fuera de frío/caliente), el termostato usaba un «icono sol» que no existe (ahora es
   un `mostrar LEDs`), «versión avanzada del Reto 15» (era el 17).
6. **Reformulaciones:** frío/caliente con una sola inclinación y `absoluto de` (sin raíz
   cuadrada); naves y varios enemigos con la categoría Juego (sprites), sin arrays; contar
   sombras con una variable de estado y dos umbrales, en vez de «luz anterior/actual»; el
   theremin con `tono de timbre` y `ajustar intervalo`, por el altavoz de la V2.
7. **El cronómetro se atrasa a partir de 10** porque los números de dos cifras se desplazan.
   Se dice en la página y la cuenta atrás del reto empieza en 9, en vez de esconderlo.
8. **Radio entre dos parejas** con un grupo propio por cada dos placas; el programa es el
   mismo en las dos. Se avisa de que el simulador no habla con la placa real.
9. **La calibración de la brújula** («TILT TO FILL SCREEN») se explica como paso del reto,
   no como problema.
10. **Fin del juego:** para volver a jugar, el botón de reinicio de la placa; no se afirma
    nada sobre A+B tras el GAME OVER porque no se ha comprobado.
11. **La presentación es una visita guiada**, como la de T1: quince diapositivas con la placa
    dibujada, el esquema de la pantalla de MakeCode, los nueve cajones, la forma de los
    bloques, un programa de varios eventos, la matriz con coordenadas y el camino
    simulador → Descargar → unidad MICROBIT. Sin capturas: todo sale del motor de bloques.
12. **Hub en tres tarjetas**, como T1, sin las promesas de «proyecto en parejas» ni «cuaderno
    del alumno», que no existían.
13. **Los 27 programas se han comprobado en el editor de MakeCode** (versión JavaScript en
    `generadores-t2/ts/`): compilan todos; r15 y a10 se probaron además en el simulador con
    trazas por serie. En a10 salió un fallo real, un enemigo que llegaba abajo sin tocar la
    nave se quedaba fuera del alcance de la bala para siempre; corregido en el programa y
    en la página (se elimina y nace otro, sin punto).

## 14. El cuadernillo de retos en PDF no se enlaza, pero tampoco se borra

`trimestres/t2-microbit/materiales/retos-microbit.pdf` es el cuadernillo con el que nació T2:
los 30 retos numerados R0–R29. Desde que T2 se rehízo, esa numeración no existe en ninguna
parte —ahora son 15 troncales `r01…r15`, 12 ampliaciones `a01…a12` y 3 sin material—, así que
enlazarlo pondría dos numeraciones distintas delante del mismo alumno, que es justo el lío que
se quería evitar.

Tampoco se borra: es el documento de origen y el que Manuel tiene impreso. Se queda donde
está, **fuera del despliegue** (`.assetsignore`), para que no acabe indexado como PDF suelto
contradiciendo a las páginas. Si algún día se quiere dar, es como el cuadernillo de Scratch:
consulta con aviso, nunca material de trabajo.

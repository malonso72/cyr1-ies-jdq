# Versión en texto (JavaScript de MakeCode) de cada programa de T2

Son los mismos programas que dibujan `gen_r01_r08.py`, `gen_r09_r15.py` y
`gen_ampliaciones.py`, escritos en el JavaScript del editor. Sirven para comprobarlos sin
montar bloques a mano: se pegan en la pestaña JavaScript de makecode.microbit.org (o se
cargan con `monaco.editor.getModels()[0].setValue(...)` desde la consola), el editor
compila, y con «Convertir código a bloques» se ve que salen los mismos bloques que en la
página.

Comprobado el 14-sept-2026 en el editor real: **los 27 compilan sin errores**. Además se
probaron en el simulador, con `serial.writeLine` de apoyo y leyendo «Mostrar datos»:

- r15 (esquiva enemigos): movimiento con A/B, colisión → fin del juego, punto y enemigo
  nuevo al llegar abajo. Correcto.
- a10 (naves): la bala sube y desaparece arriba, el impacto da punto y renueva el enemigo,
  el enemigo que toca la nave termina el juego. **Salió un fallo**: un enemigo que llegaba
  a la fila 4 sin tocar la nave se quedaba ahí para siempre, fuera del alcance de la bala
  (que nace en la fila 3). Arreglado en el programa y en la página: si llega a la fila 4,
  se elimina y nace otro, sin punto.
- r13 (radio): al pulsar A envía y muestra el tic; el simulador abre la segunda placa.
- a09 (theremin): se convierte a bloques sin bloques grises.

Si se cambia un programa en un generador, hay que cambiarlo también aquí, y al revés.

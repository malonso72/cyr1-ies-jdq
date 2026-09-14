# Clasificación de los 30 retos de T2 micro:bit

**Fecha:** 14 de septiembre de 2026 · **Estado:** tercera versión, cerrada con las decisiones de Manuel. No se ha tocado ninguna página de T2. Sale de leer los 30 retos uno por uno
(`retos/r00–r29.html`, que son el mismo texto que `materiales/retos-microbit.pdf`, feb-2026).

## Lo que ha dicho Manuel (14-sept-2026)

- El curso pasado **llegaron hasta el r19 inclusive** con los retos en pseudocódigo: veinte
  retos en un trimestre. Ese es el ritmo real, y cuadra con el troncal de abajo más ampliaciones.
- **Material: 7–8 micro:bit V2**, trabajo **por parejas**, **pinzas de cocodrilo** (las tiene o las
  consigue). **No hay servos ni ningún otro hardware.** Por tanto: micrófono y altavoz sí (son de
  la V2), servo no, LEDs externos no.
- **Se conservan todos los retos que se puedan hacer sólo con la placa**, estén o no en el
  troncal: son la ampliación para cuando el grupo va rápido. Un reto sólo sale del itinerario
  si necesita material que no hay o si no es adecuado para 1.º ESO ni reformulado.
- Radio: con una placa por pareja, los retos de radio se hacen **juntando dos parejas**.
- **Decisiones cerradas:** **sin proyecto final**, sólo retos cortos (r14 y r19 suben al troncal);
  el **editor está en español**; la entrega es **el `.hex`** en Moodle, nada más.

## Punto de partida

- **Dotación real:** el segundo trimestre son unas **20 clases** (dos semanales, de la vuelta de
  Navidad a la semana anterior a Semana Santa, menos el día de Andalucía). Treinta retos al
  mismo peso no caben.
- **Criterio para el troncal:** un reto es troncal si **introduce algo nuevo** (un bloque, una
  idea) que los siguientes necesitan. Si no introduce nada, es ampliación aunque sea bonito.
- **Regla de eventos:** el primer contacto con los botones es `al presionar el botón A`, que es
  el `al presionar tecla` que ya conocen de Scratch. Consultar el botón dentro de `para siempre`
  se introduce sólo cuando un reto lo necesita (mover algo mientras el programa hace otras cosas,
  como la pala del Arkanoid en T1), explicando cuándo cada uno.
- **Hardware:** la columna dice qué hace falta. Lo que necesita servo no se puede hacer este
  curso; se conserva la página, marcada, fuera del itinerario.
- **Nombres de bloques provisionales.** Los que aparecen en la tabla (`graficar x y`, `elegir al
  azar`, `enviar valor`…) son de memoria; el cotejo con el editor real en español es el paso
  siguiente y puede cambiar alguno, igual que pasó con el COTEJO de Scratch.

## Leyenda

- **T** Troncal — lo hace todo el alumnado, en este orden.
- **A** Ampliación — sólo la placa, adecuado para 1.º ESO (a veces reformulado); para quien
  acaba antes o quiere más. Se conservan todos.
- **P** (descartado) — Manuel ha decidido que no hay proyecto final: los retos marcados «A / P»
  son ampliación sin más. El hub deja de prometer «un proyecto en parejas».
- **M** Sin material — necesita servo; la página se conserva, marcada «requiere servo», fuera
  del itinerario de este curso.

## La tabla

| Reto | Qué es | Bloques / ideas **nuevas** que introduce | Propuesta | Hardware | Problema detectado | Qué entrega el alumno |
|---|---|---|---|---|---|---|
| r00 | Hola mundo: «Hola» + corazón en bucle | `al iniciar`, `para siempre`, `mostrar cadena`, `mostrar icono`, `borrar pantalla`; la matriz 5×5 | **T1** | Placa (o simulador) | La tabla de coordenadas es texto: debe ser un dibujo de la matriz | `.hex` |
| r01 | Corazón que late | `pausa (ms)`; alternar dos iconos | **T2** | Placa | — | `.hex` |
| r02 | Termostato con icono de sol (>30 °C) | Sensor `temperatura`, `si… si no`, `mostrar número`, comparar con `>` | **A** (lo mismo que r04, pero peor de probar) | Placa | En clase no se llega a 30 °C sin calentar la placa con el dedo; el pseudocódigo pinta el sol y lo tapa al instante con el número | `.hex` |
| r03 | Encender/apagar el LED central con A y B | Coordenadas (x,y), `graficar x y` / `borrar x y` | **T4** (después de r06) | Placa | Consulta el botón dentro de `para siempre` y el concepto dice «eventos de botones»: **reescribir con eventos** | `.hex` |
| r04 | Luz automática: todo encendido si hay poca luz | Sensor `nivel de luz`, `si… si no`, `brillo` | **T5** | Placa | «Mostrar todos los LEDs» no es un bloque: es `mostrar LEDs` con todo marcado | `.hex` |
| r05 | Dibujar el «1» LED a LED con pausas y borrarlo al revés | Nada nuevo: `graficar` + `pausa`, dieciséis veces | **A** (o reto extra de r03) | Placa | Muy largo para lo que enseña; también consulta el botón en bucle | `.hex` |
| r06 | Corazón con A, apagar con B | **Eventos**: `al presionar el botón A/B` | **T3** — antes que r03 y r05 | Placa | Se presenta como «tu primer control con botones» dos retos después de usarlos | `.hex` |
| r07 | Interruptor con un solo botón | Variable booleana (verdadero/falso), cambiar de estado | **T7** | Placa | — | `.hex` |
| r08 | Contador de turnos (A suma, B resta, nunca negativo) | Variable numérica, `cambiar por`, `dar valor`, límite con `si` | **T6** — antes que r07: contar es más concreto que un booleano | Placa | El `mostrar número` dentro de `para siempre` parpadea; mejor mostrar sólo al pulsar | `.hex` |
| r09 | Cronómetro (A arranca, B para, A+B a cero) | **Síntesis**: estado + `para siempre` + eventos; evento `A+B` | **T8** | Placa | — (es el mejor reto de la serie) | `.hex` |
| r10 | Brillo inverso a la luz (255 − luz) | Una operación aritmética dentro de un bloque | **A** | Placa | Cuesta ver el efecto: el sensor de luz son los propios LEDs | `.hex` |
| r11 | Termómetro de barras (filas según °C) | `si no, si` en cascada (varios tramos) | **A** | Placa | Tramos de 25 a 29 °C imposibles de recorrer en clase; **el reto extra dice que la V2 cambia el color de los LEDs: falso**, la matriz es roja en V1 y V2 | `.hex` |
| r12 | Fila que se enciende de izquierda a derecha | **Bucle `para índice desde 0 hasta 4`** | **T9** | Placa | Declara la variable x y luego usa un `para`: redundante | `.hex` |
| r13 | Lo mismo de derecha a izquierda | `mientras` / contador descendente | **A** (extra de r12) | Placa | Mezcla `mientras` y reinicio manual; no aporta idea nueva imprescindible | `.hex` |
| r14 | Serpiente: toda la matriz LED a LED | **Bucles anidados** | **T10** — cierra los bucles de r12 | Placa | — | `.hex` |
| r15 | Piedra-papel-tijera al agitar | `si no, si` con tres salidas; iconos propios | **T12** (después de r16) | Placa | Es más difícil que r16 y va antes | `.hex` |
| r16 | Dado electrónico al agitar | **`al agitar`**, **`elegir al azar`** | **T11** — antes que r15 | Placa | La propia ayuda dice «es más sencillo que el anterior»: el orden estaba al revés | `.hex` |
| r17 | Esquiva enemigos (LED que cae, A/B para moverse) | **Categoría Juego**: `crear sprite`, `cambiar x`, `si toca`, `fin del juego`; colisión | **T15** — el juego del trimestre, 2 clases | Placa | Está escrito con variables a mano y colisión por coordenadas: con Juego cabe en una página | `.hex` |
| r18 | Encuentra al enemigo invisible inclinando | Acelerómetro como entrada continua | **A**, reformulado como «frío / caliente»: una sola inclinación, `valor absoluto` de la diferencia con un número objetivo | Placa | **«Vibrará»: la micro:bit no tiene vibrador.** Distancia euclídea con raíz cuadrada y dos ejes: fuera de nivel | `.hex` |
| r19 | Brújula digital N/S/E/O | Sensor `dirección de la brújula`, condiciones con `o`, calibración | **T14** — el reto más vistoso, antes del juego | Placa real (la calibración lleva su rato con ocho placas a la vez) | Los tramos en grados hay que explicarlos con un dibujo de la rosa | `.hex` |
| r20 | Servo: A a 0°, B a 180°, A+B a 90° | Pines, `servo escribir` | **M** | **Servo** (no hay) + pinzas | Sin servo no se puede hacer; la nota de alimentación externa sobra para un microservo | — |
| r21 | Barrera de parking con estado | Servo + booleano (nada nuevo si se hizo r07) | **M** | Servo (no hay) | — | — |
| r22 | Barrera automática por luz | Sensor + actuador juntos | **M** | Servo (no hay); el extra pide además LEDs externos | — | — |
| r23 | Contador de coches por sombra | Detección de flanco (luz anterior/actual) | **A** | Placa | La idea de «antes/ahora» es la más abstracta de la serie; sin dibujo no se entiende | `.hex` |
| r24 | Radio: A envía, la otra placa muestra | **Radio**: `grupo de radio`, `enviar número`, `al recibir` | **T13** — juntando dos parejas | Dos placas (dos parejas) | — | `.hex` |
| r25 | Sonómetro de clase | `nivel de sonido` | **A** | Placa V2 (micrófono): la hay | Bien avisado de la V2 | `.hex` |
| r26 | Theremin luminoso | `mapear`, `reproducir tono`, salida de sonido | **A** | Placa V2 (altavoz): la hay | No dice de dónde sale el sonido: en la V2, del altavoz | `.hex` |
| r27 | Naves: moverse, disparar con A+B, enemigos | Tres sprites, disparo, puntuación | **A**, reescrito con Juego | Placa | Siete variables y colisión manual: fuera de nivel tal como está; con la categoría Juego es abordable en 2–3 clases | `.hex` |
| r28 | Esquivar dos o tres enemigos a la vez | Varios sprites a la vez, dificultad progresiva | **A** (la más difícil), reformulado con Juego: cada enemigo es un sprite, sin arrays | Placa | Arrays en 1.º ESO: fuera; con dos sprites enemigos como variables sí cabe. **Dice «versión avanzada del Reto 15» y es del r17** | `.hex` |
| r29 | Dos jugadores por radio: corazón al coincidir | Radio bidireccional, `enviar valor nombre = `, `al recibir nombre valor` | **A** | Dos placas (dos parejas) | Propone enviar «2,3» como texto y trocearlo: con `enviar valor "x" = mi_x` no hace falta | `.hex` |

## El troncal que sale (15 retos, ~18 clases)

| Orden | Reto | Idea que añade | Clases |
|---|---|---|---|
| 1 | r00 Hola mundo | pantalla, iconos, bucle | 1 |
| 2 | r01 Corazón que late | pausa | 1 (misma clase que r00 si el grupo va rápido) |
| 3 | r06 Corazón con A y B | **eventos** | 1 |
| 4 | r03 LED central | coordenadas, graficar/borrar | 1 |
| 5 | r04 Luz automática | sensor + `si… si no` | 1 |
| 6 | r08 Contador de turnos | variable numérica | 1 |
| 7 | r07 Interruptor | variable booleana, estado | 1 |
| 8 | r09 Cronómetro | síntesis de todo lo anterior | 2 |
| 9 | r12 Fila que se enciende | bucle `para` | 1 |
| 10 | r14 Serpiente | bucles anidados | 1 |
| 11 | r16 Dado | agitar, azar | 1 |
| 12 | r15 Piedra-papel-tijera | tres salidas | 1 |
| 13 | r24 Radio | radio, dos parejas juntas | 1 |
| 14 | r19 Brújula | sensor con tramos, calibración | 1 |
| 15 | r17 Esquiva enemigos | Juego: sprites y colisión | 2 |
| | **Total** | | **~17–18** |

Quedan **2–3 clases** para la presentación del primer día y el colchón de las que se pierden.
Cada reto que una pareja termina antes de tiempo se continúa con la ampliación que le toque
(la página del reto troncal enlaza a las suyas: r03 → r05, r04 → r02 y r10, r12 → r13, r16 →
r18, r17 → r27 y r28, r24 → r29, r19 → r23, y r11, r25 y r26 sueltas).

## Las ampliaciones, agrupadas por lo que continúan

Sin proyecto final, estas páginas son la continuación natural de un troncal para quien va rápido:

| Grupo | Retos | Sale de |
|---|---|---|
| **Juego** | r27 (disparar, puntos) → r28 (varios enemigos), con la categoría Juego | r17 |
| **Radio** | r29 (dos jugadores), juntando dos parejas | r24 |
| **Sonido** | r26 (theremin), r25 (sonómetro): altavoz y micrófono de la V2 | r04 / r19 |
| **Sensores** | r02, r10, r11 (temperatura y luz), r23 (contar sombras), r18 (frío/caliente) | r04 / r16 |
| **Pantalla** | r05 (dibujar el 1), r13 (fila al revés) | r03 / r12 |

## Balance: 15 troncales, 12 ampliaciones, 3 sin material

- **Troncal (15):** r00, r01, r06, r03, r04, r08, r07, r09, r12, r14, r16, r15, r24, r19, r17.
- **Ampliación (12), sólo placa:** r02, r05, r10, r11, r13, r18★, r23, r25, r26, r27★, r28★, r29. Las tres con ★ se reformulan (r18 sin raíz cuadrada; r27 y r28 con la categoría
  Juego). Se conservan las 12.
- **Sin material (3):** r20, r21, r22. Se conservan las páginas con el aviso «requiere servo».

## Correcciones de contenido que van sí o sí (sea cual sea la clasificación)

1. r11: quitar la afirmación de que la V2 cambia de color.
2. r18: quitar «vibrará»; reformular sin raíz cuadrada.
3. r28: la referencia es al r17, no al r15 (si el reto sobrevive).
4. r03 y r05: eventos, no consulta en bucle; r06 deja de ser «tu primer control con botones».
5. Hub: fuera «culmina con un proyecto en parejas» y «el cuaderno del alumno»: no existen. La
   evaluación son los retos entregados en `.hex`.

## Decisiones cerradas (14-sept-2026)

Sin proyecto final (r14 y r19 suben al troncal), editor en español, entrega del `.hex`. Con esto
la tabla está cerrada y empieza el trabajo sobre T2: cotejo de nombres de bloques en el MakeCode
en español, motor de dibujo, generadores y regeneración del troncal en su orden nuevo. Lo único
que sigue pesando más que esta tabla es la experiencia de Manuel en el aula: si un reto se
atascó el año pasado, se dice y se mueve.

# Cotejo de bloques de MakeCode para micro:bit (editor en español)

**Fecha:** 14 de septiembre de 2026. **Fuente:** el editor real, `makecode.microbit.org/?lang=es-ES`,
leído desde el propio Blockly del editor (tipo de bloque, forma, color, texto tal como se muestra
y opciones de cada desplegable). No es de memoria: cada línea sale del flyout de su categoría.

**Regla:** antes de escribir un bloque en cualquier página de T2 se busca aquí. Si no está, se
mira en el editor y se añade. Igual que `COTEJO_Cuadernillo_Scratch3.md` para T1.

## Cómo se leen las columnas

`tipo` es el identificador interno de Blockly (útil para el generador; el alumno no lo ve).
`forma`: **stmt** = bloque de pila (muesca arriba y abajo); **hat** = bloque de evento (arranca
un programa; en MakeCode es plano por arriba, sin muesca); **+C** = tiene boca para meter
bloques dentro; **reporter** = redondeado, devuelve un valor; **bool** = hexagonal, devuelve
verdadero/falso. `texto` es lo que se lee en el bloque con sus valores por defecto.

## Colores por categoría (los del editor)

| Categoría | Fondo | Borde |
|---|---|---|
| Básico | `#1e90ff` | `#176cbf` |
| Entrada | `#d400d4` | `#9f009f` |
| Música | `#e63022` | más oscuro |
| LED | `#5c2d91` | más oscuro |
| Radio | `#e3008c` | más oscuro |
| Bucles | `#00aa00` | `#008000` |
| Lógica | `#00a4a6` | más oscuro |
| Variables | `#dc143c` | más oscuro |
| Matemática | `#9400d3` | más oscuro |
| Juego | `#007a4b` | más oscuro |
| Imágenes | `#7600a8` | más oscuro |
| Número/texto (sombra) | `#ffffff` | `#bfbfbf` |

El borde es el fondo oscurecido (aprox. −20 % de luminosidad). Texto blanco, `Consolas, Monaco,
Menlo, monospace`, 16 px, peso 600. Los valores editables (números, textos) van en píldora
blanca con texto oscuro.

## Geometría (medida en el editor, a escala 1)

- Bloque de pila: alto 48 px, esquinas de radio 4, muesca de 4 px de profundidad que empieza en
  x=12 (8 px de bajada, 12 px de fondo, 8 px de subida).
- Bloque de evento (hat): igual pero **sin muesca arriba**: borde superior recto con esquinas
  redondeadas. No tiene el «sombrero» curvo de Scratch.
- Boca (bloques C: `para siempre`, `al iniciar`, `si`, `repetir`…): el interior empieza en x=16,
  mínimo 24 px de alto, y el brazo inferior mide 24 px.
- Reporter: píldora de 40 px de alto, radio 20. Booleano: hexágono de 40 px con puntas de 20 px.
- Sombra numérica: píldora blanca de 32 px de alto, radio 16, borde `#bfbfbf`.

## Básico `#1e90ff`

| tipo | forma | texto | desplegable |
|---|---|---|---|
| `device_show_number` | stmt | mostrar número **0** | |
| `device_show_leds` | stmt | mostrar LEDs **[rejilla 5×5]** | |
| `basic_show_icon` | stmt | mostrar ícono **corazón** | corazón, corazón pequeño, sí, no, feliz, triste, confundido, enojado, dormido, sorprendido, gracioso, fabuloso, meh, camiseta, patines, pato, casa, tortuga, mariposa, hombre de palitos, fantasma, espada, jirafa, calavera, paraguas, serpiente, conejo, vaca, nota negra, octava nota, tridente, objetivo, triángulo, triángulo hacia la izquierda, tablero de ajedrez, diamante, diamante pequeño, cuadrado, cuadrado pequeño, tijeras |
| `device_print_message` | stmt | mostrar cadena **¡Hola!** | |
| `device_clear_display` | stmt | borrar la pantalla | |
| `device_forever` | hat+C | para siempre | |
| `pxt-on-start` | hat+C | al iniciar | |
| `device_pause` | stmt | pausa (ms) **100** | |
| `basic_show_arrow` | stmt | mostrar flecha **Norte** | Norte, Noreste, Este, Sureste, Sur, Suroeste, Oeste, Noroeste |

Ojo: es «mostrar **ícono**» con tilde en la i, como lo escribe el editor. Y «borrar la pantalla»,
no «borrar pantalla».

## Entrada `#d400d4`

| tipo | forma | texto | desplegable |
|---|---|---|---|
| `device_button_event` | hat+C | al presionarse el botón **A** | A, B, A+B |
| `device_gesture_event` | hat+C | si **agitado** | agitado, logotipo hacia arriba, logotipo hacia abajo, pantalla hacia arriba, pantalla hacia abajo, inclinación hacia la izquierda, inclinación hacia la derecha, caída libre, 3g, 6g, 8g |
| `device_pin_event` | hat+C | al presionarse pin **P0** | P0, P1, P2 |
| `device_get_button2` | bool | botón **A** presionado | A, B, A+B |
| `device_acceleration` | reporter | aceleración (mg) **x** | x, y, z, fuerza |
| `device_pin_is_pressed` | bool | pin **P0** está presionado | P0, P1, P2 |
| `device_get_light_level` | reporter | nivel de luz | |
| `device_heading` | reporter | dirección de la brújula (°) | |
| `device_temperature` | reporter | temperatura (°C) | |
| `deviceisgesture` | bool | es un gesto **agitado** | (los mismos gestos) |
| `input_on_sound` | hat+C | al detectar el sonido **alto** | alto, silencioso |
| `input_logo_event` | hat+C | al pulsar el logotipo **pulsar** | pulsar, tocar, soltar, mantener pulsado |
| `input_logo_is_pressed` | bool | el logotipo está pulsado | |
| `device_get_sound_level` | reporter | nivel de sonido | |

Entrada › más: `input_compass_calibrate` stmt «calibrar brújula»; `device_get_magnetic_force`
reporter «fuerza magnética (μT) x»; `device_get_rotation` reporter «rotación (°) **timbre**»
(timbre/girar: son *pitch* y *roll* mal traducidos; para r18 se usa «rotación (°) timbre», que
es la inclinación adelante-atrás, o «girar», izquierda-derecha); `device_get_running_time`
reporter «tiempo de ejecución (ms)»; `device_pin_released`; `device_set_accelerometer_range`;
`input_set_sound_threshold` stmt «establecer el umbral de sonido alto al valor 128».

Ojo: el evento de agitar se lee «**si** agitado», no «al agitar». Y el de botón es «al
presionar**se** el botón A».

## LED `#5c2d91`

| tipo | forma | texto |
|---|---|---|
| `device_plot` | stmt | graficar x **0** y **0** |
| `device_led_toggle` | stmt | invertir x **0** y **0** |
| `device_unplot` | stmt | **ocultar** x **0** y **0** |
| `device_point` | bool | punto x **0** y **0** |
| `device_plot_bar_graph` | stmt | trazar gráfico de barras **0** hasta **0** |

LED › más: `device_plot_brightness` «graficar x 0 y 0 brillo 255»; `device_point_brightness`
«punto x 0 y 0 brillo»; `device_get_brightness` reporter «brillo»; `device_set_brightness` stmt
«**ajustar brillo** 255»; `device_led_enable` «activar leds falso»; `device_stop_animation`
«detener animación»; `led_set_display_mode` «establecer modo de visualización blanco y negro».

Ojo: apagar un LED es «**ocultar** x y», no «borrar» ni «apagar». El brillo se pone con
«ajustar brillo».

## Radio `#e3008c`

| tipo | forma | texto |
|---|---|---|
| `radio_set_group` | stmt | radio establecer grupo **1** |
| `radio_datagram_send` | stmt | radio enviar número **0** |
| `radio_datagram_send_value` | stmt | radio enviar valor **nombre** = **0** |
| `radio_datagram_send_string` | stmt | radio enviar cadena **""** |
| `radio_on_number_drag` | hat+C | al recibir radio **receivedNumber** |
| `radio_on_value_drag` | hat+C | al recibir radio **name** **value** |
| `radio_on_string_drag` | hat+C | al recibir radio **receivedString** |
| `radio_received_packet` | reporter | paquete recibido **intensidad de señal** |

Las variables de los eventos de radio (`receivedNumber`, `name`, `value`, `receivedString`)
salen en inglés en el editor español: se escriben así en las páginas, tal cual.

## Bucles `#00aa00`

| tipo | forma | texto |
|---|---|---|
| `controls_repeat_ext` | stmt+C | repetir **4** veces ejecutar |
| `device_while` | stmt+C | mientras **falso** ejecutar |
| `pxt_controls_for` | stmt+C | para **índice** de 0 a **4** ejecutar |
| `pxt_controls_for_of` | stmt+C | para el elemento **valor** de **lista** ejecutar |
| `every_interval` | hat+C | cada **500** ms |
| `break_keyword` | stmt | salir |
| `continue_keyword` | stmt | continuar |
| `pxt_pause_until` | stmt | pausar hasta **verdadero** |

Los tres bucles con boca llevan la palabra «ejecutar» al final de la primera línea.

## Lógica `#00a4a6`

| tipo | forma | texto |
|---|---|---|
| `controls_if` | stmt+C | si **verdadero** entonces |
| `controls_if` (con si no) | stmt+C | si **verdadero** entonces … si no … |
| `logic_compare` | bool | **0** = **0** (=, ≠, <, ≤, >, ≥) |
| `logic_operation` | bool | ? **y** ? / ? **o** ? |
| `logic_negate` | bool | no ? |
| `logic_boolean` | bool | verdadero / falso |

El «si no, si» se consigue con el «+» del bloque `si` (añade rama *si no, si*). En las páginas se
escribe como lo lee el editor: «si … entonces», «si no, si … entonces», «si no».

## Variables `#dc143c`

| tipo | forma | texto |
|---|---|---|
| `variables_set` | stmt | fijar **puntos** a **0** |
| `variables_change` | stmt | cambiar **puntos** por **1** |
| `variables_get` | reporter | **puntos** |

Es «**fijar** … a», no «establecer» ni «dar valor». El botón «Crear una variable…» está encima.

## Matemática `#9400d3`

| tipo | forma | texto |
|---|---|---|
| `math_arithmetic` | reporter | **0** + **0** (+, −, ×, ÷, **) |
| `math_number` | reporter (sombra blanca) | **0** |
| `math_modulo` | reporter | restante de **0** / **1** |
| `math_op2` | reporter | min de **0** y **0** / max de … |
| `math_op3` | reporter | absoluto de **0** |
| `math_js_op` | reporter | raíz cuadrada **0** (y sin, cos…) |
| `math_js_round` | reporter | redondeo **0** |
| `device_random` | reporter | **escoger al azar de 0 a 10** |
| `math_constrain_value` | reporter | restringir **0** entre **0** y **0** |
| `math_map` | reporter | ajustar intervalo **0** de **0** hasta **1023** a intervalo de **0** hasta **4** |
| `logic_random` | bool | escoge al azar verdadero o falso |

El azar es «**escoger al azar de** 1 **a** 6». El valor absoluto, «absoluto de». El *map* del
theremin es «ajustar intervalo».

## Juego `#007a4b` (Avanzado › Juego)

| tipo | forma | texto |
|---|---|---|
| `game_create_sprite` | reporter | crear sprite en x: **2** y: **2** |
| `game_delete_sprite` | stmt | eliminar **sprite** |
| `game_sprite_is_deleted` | bool | está eliminado **sprite** |
| `game_move_sprite` | stmt | **sprite** desplazar **1** |
| `game_turn_sprite` | stmt | **sprite** girar **derecha** (°) **45** |
| `game_sprite_change_xy` | stmt | **sprite** cambiar **x** por **1** (x, y, dirección, brillo, parpadear) |
| `game_sprite_set_property` | stmt | **sprite** establecer **x** en **0** |
| `game_sprite_property` | reporter | **sprite** **x** |
| `game_sprite_touching_sprite` | bool | esta **sprite** tocando ? |
| `game_sprite_touching_edge` | bool | **sprite** tocando el borde |
| `game_sprite_bounce` | stmt | **sprite** si en el borde, rebotar |
| `game_set_score` / `game_add_score` / `game_score` | stmt / stmt / reporter | establecer puntuación a **0** / agregar puntos a la puntuación actual **1** / puntuación |
| `game_start_countdown` | stmt | iniciar cuenta regresiva (ms) **10000** |
| `game_game_over` | stmt | fin del juego |
| `game_remove_life` / `game_add_life` / `game_set_life` | stmt | remover vida / añadir vida / establecer vida |

Un sprite es un LED con posición y dirección. `crear sprite` se guarda en una variable con
«fijar **jugador** a (crear sprite en x: 2 y: 4)». Es lo que permite reescribir r17, r27 y r28
sin coordenadas a mano ni arrays.

## Imágenes `#7600a8` (Avanzado › Imágenes)

`device_show_image_offset` «mostrar imagen … con intervalo de 0»; `device_scroll_image`
«desplazar imagen … con desplazamiento 1 e intervalo (ms) 200»; `device_build_image` reporter
«crear imagen [rejilla]»; `builtin_image` reporter «imagen de icono corazón». No hacen falta en
el troncal.

## Música `#e63022` (sólo lo que usa T2)

`music_playable_play` stmt «reproduce secuencia tono **Do medio** durante (1 pulso) en modo
hasta que termine»; `device_ring` stmt «**tono de timbre (Hz)** Do medio» (es el que vale para
el theremin: se le mete un número de Hz); `music_stop_all_sounds` stmt «para todos los
sonidos»; `synth_set_volume` «establecer volumen a 127». En la V2 suena por el altavoz de la
placa sin conectar nada.

## Lo que la tabla de clasificación tenía «de memoria» y cambia

| Se escribió | Es | Dónde |
|---|---|---|
| `borrar x y` | **ocultar x y** | r03, r05, r12–r14 |
| `elegir al azar` | **escoger al azar de … a …** | r15, r16 |
| `al agitar` | **si agitado** | r15, r16 |
| `al presionar el botón A` | **al presionarse el botón A** | todos |
| `dar valor` / `establecer` | **fijar … a** | r07, r08, r09 |
| `mapear` | **ajustar intervalo** | r26 |
| `valor absoluto` | **absoluto de** | r18 |
| `mostrar icono` | **mostrar ícono** | r00, r01… |
| `enviar valor nombre =` | **radio enviar valor nombre = 0** | r29 |

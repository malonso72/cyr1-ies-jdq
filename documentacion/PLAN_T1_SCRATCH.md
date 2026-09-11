# Guion del primer trimestre · Scratch · CyR 1º ESO

Documento de trabajo. Fija **qué va en cada una de las 20 sesiones** antes de escribir
ninguna página, para que la sesión 20 salga con el mismo criterio que la sesión 1.

- **Contexto real:** Scratch 3 **en el navegador**, ordenadores **Linux**, alumnado **sin cuenta**.
- **Flujo del alumno:** Moodle → esta página → hace el ejercicio en Scratch → vuelve a Moodle a entregar.
- **El cuadernillo pasa a consulta opcional.** Se enlaza con `#page=` a la página exacta, nunca como
  destino de trabajo. Nombres de bloques verificados en `COTEJO_Cuadernillo_Scratch3.md`.

---

## Esqueleto común de una sesión

Toda página de sesión tiene las mismas piezas y en el mismo orden:

| # | Pieza | Para qué |
|---|---|---|
| — | **Hero** | Sesión NN + título |
| — | **Lo que vas a conseguir** | una frase concreta, en resultado observable |
| — | **Botón «Abrir Scratch»** + consejo de media pantalla | quitar fricción |
| 1 | **Lee este programa** | bloques en SVG, legibles a media pantalla |
| 2 | **Qué hace, paso a paso** | lista numerada, lenguaje de 1º ESO |
| 3 | **Comprueba que lo has entendido** | 1 pregunta de opción múltiple con explicación de cada opción |
| 4 | **Tu actividad** | lo que tiene que construir |
| — | **Pista** (plegada) | bloques de la solución parcial |
| — | **⚠️ Ojo con esto** | el error típico de esa sesión |
| 5 | **Lo has conseguido si…** | checklist de autoevaluación |
| — | **📤 Entrega** | descargar `.sb3` → Descargas → Moodle |
| — | **Navegación** | anterior · índice · siguiente · cuadernillo `#page=` |

La pregunta del punto 3 es la pieza que el cuadernillo no puede tener: **leer código ajeno y
predecir qué hace** antes de escribir el propio.

---

## Las 20 sesiones

Los títulos son **los que ya están en la web y en Moodle. No se tocan.**

### S01 · Introducción a Scratch
- **Consigue:** un proyecto con personaje, fondo y una primera acción.
- **Programa:** `al hacer clic en 🏳` → `decir (¡Hola! Soy Sprite1) durante (2) segundos` → `mover (100) pasos` → `iniciar sonido (Miau)`
- **Extra:** diagrama SVG del editor (escenario, lista de objetos, paleta, área de código, pestañas Código/Disfraces/Sonidos).
- **Comprueba:** cierras la pestaña sin descargar → ¿qué pasa con tu proyecto?
- **Actividad:** cambiar fondo, cambiar el texto, añadir un segundo objeto.
- **Ojo:** sin cuenta, el proyecto vive sólo en la pestaña.

### S02 · Movimiento y direcciones
- **Consigue:** una ruta cerrada que vuelva al punto de partida.
- **Programa:** bandera → `ir a x:(0) y:(0)` → tres tramos `apuntar en dirección` + `mover (100) pasos` + `esperar (1) segundos` → `iniciar sonido (Miau)`
- **Extra:** rosa de direcciones en SVG (0 arriba, 90 derecha, 180 abajo, −90 izquierda).
- **Comprueba:** ¿qué dirección es «hacia arriba»?
- **Ojo:** el cuadernillo dice 270, el editor dice −90. Y `fijar estilo de rotación a (no rotar)` para que el gato no salga boca abajo.
- **Cuadernillo:** p. 7 (contiene la contradicción 315/270/225 vs −90).

### S03 · Bucles
- **Consigue:** dibujar un cuadrado sin escribir cuatro veces lo mismo.
- **Programa:** bandera → `ir a x:(0) y:(0)` → `repetir (4) [ mover (100) pasos · girar ↻ (90) grados ]`
- **Comprueba:** ¿por qué 90 grados y no 100?
- **Actividad:** triángulo (3 × 120) y pentágono (5 × 72). Regla: los giros suman 360.
- **Ojo:** `repetir` frente a `por siempre`.
- **Decisión tomada:** el cuadernillo usaba `tocar tambor … pulsos`, que es de la extensión **Música**. Se sustituye por `iniciar sonido`, que está en la paleta por defecto.

### S04 · Condicionales I
- **Aviso honesto en la página:** aquí todavía **no** hay un `si… entonces`; eso llega en S05. Lo de hoy es `repetir hasta que`.
- **Programa:** bandera → `repetir hasta que <¿tecla (espacio) presionada?> [ mover (10) pasos · si toca un borde, rebotar ]` → `detener (todos)`
- **Comprueba:** ¿qué pasa si no pulsas nunca el espacio?
- **Actividad:** cambiar la condición por `¿ratón presionado?` y por `¿tocando (borde)?`.

### S05 · Condicionales II y teclado *(piloto ya escrito y validado)*
- **Programa:** bandera → `repetir hasta que <espacio>` con dos `si … entonces` dentro (flecha derecha / izquierda) → `iniciar sonido (Miau)` fuera del bucle.
- **Comprueba:** ¿cuándo suena el miau? → sólo al salir del bucle.
- **Actividad:** añadir arriba (dirección 0) y abajo (180).
- **Ojo:** el gato boca abajo → `fijar estilo de rotación a (no rotar)`.
- **Cuadernillo:** `#page=11`.

### S06 · Animaciones con disfraces
- **Programa:** bandera → `por siempre [ siguiente disfraz · esperar (0.2) segundos · mover (10) pasos · si toca un borde, rebotar ]`
- **Comprueba:** ¿qué se ve si quitas el `esperar`?
- **Actividad:** elegir de la biblioteca un personaje con varios disfraces y animarlo.
- **Ojo:** los disfraces se llaman **costume1** y **costume2**, en inglés. El cuadernillo dice «disfraz1» y eso no existe.

### S07 · Preguntas y respuestas
- **Programa:** dos `preguntar (…) y esperar` seguidos, con `decir (unir (Hola, ) (respuesta))` en medio.
- **Comprueba:** si preguntas dos cosas y luego usas `respuesta`, ¿cuál sale? → **la última**. Es el concepto de la sesión.
- **Actividad:** diálogo de tres preguntas.
- **Ojo:** el texto por defecto es `¿Cómo te llamas?`, no «¿Cuál es tu nombre?». Y `respuesta` se machaca en cada pregunta → puente a S08.

### S08 · Variables I
- **Programa:** calculadora. `preguntar` → `dar a (num1) el valor (respuesta)` → `preguntar` → `dar a (num2) el valor (respuesta)` → `decir (unir (La suma es ) ((num1) + (num2))) durante (3) segundos`
- **Comprueba:** por qué hace falta una variable si ya existe `respuesta`.
- **Actividad:** añadir resta y multiplicación.
- **Ojo:** `dar a … el valor` es el antiguo `fijar … a`. Botón **Crear una variable**.

### S09 · Variables II, azar y puntuación
- **Programa:** quiz de multiplicar. `dar a (Aciertos) el valor (0)` → `repetir (5) [ dos aleatorios · preguntar · si <respuesta = a×b> entonces [ ¡Bien! · sumar a (Aciertos) (1) ] si no [ Casi ] ]` → marcador final.
- **Comprueba:** `sumar a (Aciertos) (1)` frente a `dar a (Aciertos) el valor (1)`. **El error clásico.**
- **Ojo:** el bloque **no** se llama `cambiar (Aciertos) por (1)` como dice el cuadernillo, sino **`sumar a (Aciertos) (1)`**.
- **Cuadernillo:** ejercicio 9.

### S10 · Juego de carreras
- **Programa:** el mismo script en **dos objetos**: `ir a x:(-200) y:(…)` → `repetir hasta que <(posición x) > (200)> [ mover (número aleatorio entre (1) y (10)) pasos ]` → `decir (¡He ganado!)`
- **Comprueba:** ¿por qué no gana siempre el mismo?
- **Ojo:** cada objeto tiene su propia área de código. Si programas los dos en el mismo objeto, no funciona.

### S11 · Mensajes entre objetos
- **Programa:** dos scripts, uno al lado del otro. Objeto A: `esperar (1) segundos` → `enviar (mensaje1)`. Objeto B: `al recibir (mensaje1)` → `decir (¡Me han llamado!) durante (2) segundos`.
- **Comprueba:** ¿en qué objeto va el `al recibir`?
- **Ojo:** el bloque es `enviar (mensaje1)`, sin el «a todos» del cuadernillo. Y `enviar y esperar` es distinto.

### S12 · Laberinto I
- **Programa:** movimiento con flechas usando `cambiar x por` / `cambiar y por`, más `si <¿tocando el color (negro)?> entonces [ ir a x:(…) y:(…) ]`.
- **Comprueba:** por qué se vuelve al inicio en vez de «no dejar pasar».
- **Actividad:** pintar el laberinto como **fondo** con la herramienta de dibujo.
- **Ojo:** el color del bloque tiene que ser exactamente el del laberinto → cuentagotas.

### S13 · Laberinto II
- **Añade:** meta (`¿tocando (Meta)?` → `decir` → `detener (todos)`), cronómetro (`reiniciar cronómetro`, `cronómetro`) y segundo nivel con `cambiar fondo a`.
- **Comprueba:** dónde va el `detener (todos)` para que no corte el mensaje de victoria.

### S14 · Piedra, papel o tijera
- **Programa:** `dar a (ordenador) el valor (número aleatorio entre (1) y (3))` → `preguntar` → cadena de `si … entonces / si no`.
- **Comprueba:** ¿cuántos resultados posibles hay? (9) ¿hay que escribir nueve condicionales?
- **Actividad:** marcador a tres partidas.

### S15 · Pong I
- **Programa:** pelota `por siempre [ mover (10) pasos · si toca un borde, rebotar ]`; pala `por siempre [ ir a x:(posición x del ratón) y:(-140) ]`.
- **Comprueba:** por qué la pala usa `ir a x` y no `mover`.
- **Ojo:** dos objetos, dos programas, los dos con `por siempre`.

### S16 · Pong II
- **Añade:** `si <¿tocando (Pala)?> entonces [ apuntar en dirección … · sumar a (Puntos) (1) ]`, fin de partida con `si <(posición y) < (-170)> entonces [ decir (Fin) · detener (todos) ]`, y dificultad creciente.
- **Comprueba:** por qué el marcador sube de golpe muchos puntos y cómo se evita.

### S17 · Proyecto final: idea y diseño
- **Sin bloques.** Ficha de diseño en pantalla: título, tipo (juego / historia), personajes, reglas, qué hace ganar y qué hace perder, boceto.
- **Catálogo de ideas** con dificultad estimada, para que nadie se quede en blanco ni se meta en algo imposible.
- **Entrega:** la ficha rellenada en Moodle, no un `.sb3`.

### S18 · Proyecto final: construcción
- **Kit de piezas:** los ocho scripts más reutilizables del trimestre, dibujados y listos para copiar (mover con flechas, rebotar, marcador, cronómetro, mensajes, aparecer/desaparecer, pantalla de inicio, fin de partida).
- **Entrega:** primera versión jugable.

### S19 · Proyecto final: mejoras
- **Guía de depuración:** los cinco fallos típicos y cómo se localizan (no arranca, se mueve una sola vez, el marcador no sube, dos objetos se pisan, el sonido no suena).
- **Lista de pulido:** sonido, marcador, pantalla de inicio, mensaje de fin, instrucciones.

### S20 · Presentación de proyectos
- **Rúbrica visible** con la que se va a evaluar.
- **Guion de exposición de 60 segundos:** qué es, cómo se juega, qué fue lo más difícil, qué mejorarías.
- **Entrega final:** `.sb3` + ficha.

---

## Reglas de estilo del material

1. **Segunda persona y frases cortas.** Es 1º de ESO.
2. **Nombres exactos de la paleta.** `Sprite1`, `costume1`, `Miau`, `¿Cómo te llamas?`.
3. **Ningún bloque de extensión** (Música, Lápiz) sin decir explícitamente que hay que añadirla.
4. **Los bloques se dibujan en SVG**, nunca capturas de pantalla: se leen a media pantalla y no pesan.
5. **Cada SVG con `role="img"`, `aria-label` y `<title>`.**
6. **Una pregunta de comprensión por sesión**, con explicación de por qué falla cada opción incorrecta.
7. **La entrega siempre igual:** Archivo → Guardar en tu ordenador → `SesionNN_TuNombre.sb3` → Moodle.
8. **El cuadernillo se enlaza con `#page=`** o no se enlaza.

## Decisiones tomadas sin consultar

Se registran en `DECISIONES_T1.md` a medida que aparecen.

# Revisión pedagógica de las 20 sesiones de T1 · Scratch

Revisión de `trimestres/t1-scratch/sesiones/s01–s20.html` contra `PLAN_T1_SCRATCH.md`,
`COTEJO_Cuadernillo_Scratch3.md` y `DECISIONES_T1.md`. Septiembre 2026.

Todo lo que hay aquí está comprobado sobre el HTML publicado, no sobre los generadores.
Las correcciones, cuando toque hacerlas, van en `documentacion/generadores-t1/`, no a mano.

---

## Veredicto corto

El material está bien. El tono acierta —segunda persona, frases cortas, cero paternalismo—,
la pieza de «leer un programa y predecir qué hace» es lo mejor que tiene y es justo lo que
el cuadernillo no puede dar, y los nombres de bloques están limpios: **no queda ni un nombre
de Scratch 2 fuera de los avisos ⚠️ que precisamente advierten del cambio**. Los enlaces
`#page=` del cuadernillo coinciden uno a uno con la tabla de la decisión 4.

Lo que hay que arreglar son **cuatro programas que no funcionan tal y como están escritos**
y un puñado de incoherencias internas. Ninguna obliga a rehacer nada: son retoques.

### Longitud y densidad

| | palabras | palabras/frase |
|---|---|---|
| media de las 20 | 619 | 15,2 |
| más corta (S02) | 510 | 14,6 |
| más larga (S19) | 861 | 20,0 |

15 palabras por frase es exactamente el registro de 1º de ESO, y 600 palabras son unos
4–5 minutos de lectura: cabe de sobra en una sesión. **La S19 se sale**: 861 palabras y
20 palabras por frase, casi el doble de largo que la S02. Es la candidata clara a recortar.

---

## 1. Programas que no funcionan como están escritos

Estos cuatro los va a encontrar el alumnado en clase, no leyendo.

### 1.1 · S13 — la variable `Nivel` no se crea ni se inicializa

La actividad 5 pone `sumar a (Nivel) (1)` y el desplegable dice «con la variable Nivel que
acabas de crear», pero **ningún paso pide crearla** y el arranque
(`reiniciar cronómetro` + `cambiar fondo a nivel1`) **no la pone a 1**. Resultado: la
segunda partida empieza en el nivel que dejaste.

Es, literalmente, el fallo que la S09 pone como «el error más común del trimestre» y que la
S18 convierte en su pregunta de comprensión. Quedarse así en la S13 es el peor sitio posible.

**Arreglo:** añadir `dar a (Nivel) el valor (1)` al programa de arranque de la sección 2,
y un paso en la actividad que diga que hay que crear la variable.

### 1.2 · S11 — el balón no tiene posición de partida

El gato hace `ir a x:(-120) y:(-60)`. El balón arranca en `al recibir (patada)` y rueda con
`repetir hasta que <¿tocando (borde)?>`. La primera vez sale bien; **la segunda vez que se
pulsa la bandera el balón sigue pegado al borde**, la condición se cumple en la primera
vuelta y no se mueve. Media clase va a levantar la mano en el minuto diez.

De paso: ninguno de los dos programas fija la dirección, cuando la S02 dedica una sección
entera a eso y la S10 sí pone `apuntar en dirección (90)`.

**Arreglo:** dar al balón un programa propio con `al hacer clic en 🏳` →
`ir a x:(…) y:(…)` → `apuntar en dirección (90)`, y añadir el mismo `apuntar` al gato.
Es coherente con lo que la S02 explica y con la pieza de inicialización de la S18.

### 1.3 · S16 — el final de partida es frágil, y la alternativa que ofrece no existe

La sección 4 dice: *«cambia `si toca un borde, rebotar` por un rebote que sólo mire los
lados y el techo… o, más sencillo, déjalo como está y añade esta comprobación, que se
dispara antes»*, con `si <(posición y) < (-170)>`.

Dos problemas:

- **Ese «rebote que sólo mire los lados y el techo» no es un bloque.** Hay que montarlo a
  mano con condicionales sobre `posición x` y `posición y`, y eso no se ha enseñado. El
  alumno que elija esa vía se queda tirado.
- **La comprobación de −170 depende del tamaño de la pelota.** Con el rebote puesto,
  Scratch devuelve la pelota dentro del escenario: con la *Ball* al 50 % el centro llega a
  ≈ −174 y sí salta el aviso, pero con una pelota más grande o al 100 % no baja de −170 y
  **la partida no termina nunca**. Y como el alumno elige su pelota en la S15 («la Ball de
  la biblioteca vale»), el resultado depende de a quién le toque.

**Arreglo:** bajar el umbral a `< (-155)` o `< (-160)` —la pala está en −140, así que se
detecta en cuanto la pelota pasa de largo, antes de tocar el borde— y quitar la frase del
rebote selectivo, o sustituirla por el bloque de verdad.

### 1.4 · S09 — el reto final se contradice

*«Reto: cambia las sumas por multiplicaciones y baja el rango de los números aleatorios a
1–10.»* El programa **ya** sortea `número aleatorio entre (1) y (10)`. No hay nada que bajar.

**Arreglo:** «bájalo a 1–5». Y así la razón por la que conviene bajarlo (10 × 10 = 100 de
cabeza es otra liga) se sostiene sola.

---

## 2. Incoherencias entre sesiones

### 2.1 · S20 manda a una rúbrica que no está en ningún sitio

«Esto no es una sorpresa: **es la misma lista que tienes desde la sesión 17**.» No lo es:
la rúbrica no aparece en la S17, ni en la S18, ni en la S19 — sale por primera vez en la
S20, el día de la presentación.

La idea de fondo es buena (que la nota no sea una sorpresa), pero hay que cumplirla: o la
tabla de criterios sube a la S17, junto a la ficha de diseño, o la frase se cambia.
Recomiendo lo primero: la rúbrica al lado de la ficha es lo que hace que los puntos 6 y 7
de la ficha se tomen en serio.

### 2.2 · S19 — la actividad y el checklist se contradicen

La actividad dice «Elige **tres** mejoras. No todas: tres, bien hechas». El checklist exige
«al menos tres mejoras» **y además** «El juego tiene pantalla de inicio y pantalla de fin»,
que son dos de las siete de la lista. Si el alumno elige otras tres, cumple la actividad y
suspende el checklist.

**Arreglo:** o la pantalla de inicio y la de fin salen de la lista opcional y pasan a ser
obligatorias («dos obligatorias y una a elegir»), o el checklist deja de pedirlas.

### 2.3 · S18 — el kit tiene siete piezas y el plan decía ocho

Faltan dos de las previstas y sobra una nueva:

| Plan | Página |
|---|---|
| mover con flechas | ✅ pieza 1 |
| **rebotar** | ❌ no está |
| marcador | ✅ pieza 2 |
| cronómetro | ✅ como cuenta atrás (pieza 5) |
| mensajes | ⚠️ sólo dentro de la pieza 6 |
| **aparecer/desaparecer** | ❌ sustituida por «aparecer en un sitio al azar» |
| pantalla de inicio | ✅ pieza 6 |
| fin de partida | ✅ pieza 7 |
| — | ➕ «chocar y perder vida» (pieza 4), que no estaba |

Lo importante no es el número: es que **`mostrar` y `esconder` de objetos no se enseñan en
ninguna de las 20 sesiones**, y dos de las ocho ideas del catálogo de la S17 —«esquivar lo
que cae» y «cazar al que huye»— las necesitan para que el objeto reaparezca. El alumno que
elija la idea marcada como ⭐ Fácil se encuentra con que le falta una pieza.

**Arreglo:** añadir una pieza corta de `esconder` / `mostrar` (tres bloques), y anotar el
cambio en `DECISIONES_T1.md`, que ahora mismo no lo recoge.

### 2.4 · La numeración de las secciones baila en cuatro sesiones

17 de las 20 van 1–5 con Comprueba = 3 y Tu actividad = 4. Las otras cuatro, no:

| Sesión | Qué pasa |
|---|---|
| **S04** | empieza en el **2**. No hay sección 1: el aviso del título ocupa su sitio sin número |
| **S07** | va 1–4. Comprueba es el 2 y Tu actividad el 3 |
| **S16** | va 1–6, porque «Perder la partida» se cuela como 4. Tu actividad es el 5 |
| **S20** | va 1–4 y no tiene «Lo has conseguido si…» |

En la S20 tiene sentido (no hay nada que construir). En la S04 es un despiste claro: la
sección 1 no existe. En la S07 y la S16 el alumno que oye «mirad el punto 4» mira otra cosa
según la sesión.

**Arreglo:** numerar el aviso de la S04 como sección 1, y revisar S07 y S16 para que
Comprueba caiga siempre en el 3 y Tu actividad en el 4.

### 2.5 · S03 — se habla de «dibujar» cuatro veces y no se dibuja nada

«Lo que vas a conseguir: **dibujar** un cuadrado, un triángulo y un pentágono», «Has
**dibujado** las tres figuras». Sin la extensión **Lápiz** el gato *recorre* el cuadrado
pero no deja ni una línea: en pantalla no hay ninguna figura. El alumno va a pensar que le
falta algo.

Es además la regla de estilo 3 del plan (ningún bloque de extensión sin decirlo).

**Arreglo, a elegir:** cambiar el verbo («que tu gato **recorra** un cuadrado y vuelva al
punto de partida») o añadir la extensión Lápiz con dos frases y `bajar lápiz`. Lo primero
es más barato y encaja con la comprobación que ya usa el checklist («el gato acaba donde
empezó»).

### 2.6 · Detalles menores

- **S05** presenta `fijar estilo de rotación a (no rotar)` como una novedad opcional («Si
  quieres que no le pase…») cuando la **S02 ya lo lleva en el programa principal** y la S06
  usa la variante `izquierda-derecha`. Basta un «como ya viste en la sesión 2».
- **S06** escribe las esperas con coma en el texto (0,05 · 0,2 · 1) y con punto en el
  bloque dibujado (`esperar (0.2) segundos`). En el campo de Scratch hay que escribir
  **punto**. Conviene unificar a punto, que es lo que teclean.
- **S11, S12, S16, S18** usan `iniciar sonido (Pop)`. El `COTEJO` sólo dejó verificado
  **Miau**. Merece una mirada de dos segundos en el editor: si el objeto que elige el
  alumno no trae ese sonido en su pestaña Sonidos, el bloque aparece con otro nombre — que
  es justo el sexto fallo de la tabla de la S19.
- **S15** escribe en prosa «rebotar si toca un borde», con el nombre del bloque del revés
  (`si toca un borde, rebotar`). Es la clase de detalle que el cotejo se tomó la molestia
  de fijar.
- **S13**, actividad 5: al pasar al nivel 2 cambia el fondo pero **el objeto Meta se queda
  donde estaba**, que muy probablemente no es el final del segundo laberinto. Una frase lo
  resuelve.

---

## 3. Lo que está bien y conviene no tocar

- **Las preguntas de «Comprueba que lo has entendido».** Son el mejor material de todo el
  trimestre. La de la S07 (`respuesta` se machaca), la de la S09 (`sumar a` frente a
  `dar a … el valor`) y la de la S16 (el marcador que sube de golpe) enseñan más que el
  ejercicio entero, y las explicaciones de las opciones incorrectas están escritas para que
  el que falla aprenda algo, no para castigarle.
- **La honestidad del aviso de la S04.** La decisión 2 era la dudosa y está bien resuelta:
  tres líneas, sin rodeos y sin romper la numeración de Moodle.
- **Los avisos «⚠️ Ojo con esto» con el cuadernillo delante.** Que el material diga «tu
  cuadernillo dice X y eso ya no existe» en lugar de ignorarlo convierte un problema en una
  lección.
- **La progresión S07 → S08 → S09.** El puente está bien construido: `respuesta` se pierde
  → por eso hacen falta variables → y contar con variables tiene su propia trampa.
- **La S17.** Obligar a escribir «se gana cuando Puntos llega a 10» antes de tocar un
  bloque es lo que separa un proyecto terminado de tres a medias.

---

## 4. Orden sugerido para arreglarlo

1. Los cuatro programas de la sección 1. Son los que dan la cara en clase.
2. La rúbrica a la S17 (2.1) y el checklist de la S19 (2.2).
3. La pieza que falta en el kit de la S18 (2.3) y su nota en `DECISIONES_T1.md`.
4. La numeración de S04, S07 y S16 (2.4).
5. El verbo «dibujar» de la S03 (2.5) y los detalles de 2.6.
6. Recortar la S19: 861 palabras es demasiado para el día en que además hay que jugar,
   depurar y dejar probar a un compañero.

---

## 5. Añadido tras el cruce con la revisión de ChatGPT

Comprobados sobre el repo, no dados por buenos.

### 5.1 · `PROGRAMACION.md` está desfasado *(hallazgo suyo, verificado)*

Sigue diciendo **«T1 Scratch · ~30-36 sesiones · Hub + placeholders»** en las dos tablas,
cuando el material real son **20 sesiones completas**. Es el documento que fija la
distribución temporal del curso, así que conviene que no contradiga a lo que hay.

De paso deja una pregunta abierta que no puedo contestar yo: **¿cuántas horas semanales
tiene CyR?** 20 sesiones en un trimestre sólo caben con 2 h/semana. Con 1 h/semana, el T1
se come medio curso y hay que decidir qué se queda fuera antes de empezar, no en enero.

### 5.2 · El hub del trimestre tiene tres cosas que corregir

Ninguna está en las sesiones: están en `trimestres/t1-scratch/index.html`.

- **«una rúbrica que el alumnado conoce desde la sesión 17»** — mismo problema que la S20
  (punto 2.1): la rúbrica no está en la S17. Son ya **dos sitios** que prometen lo mismo.
- **«12 juegos para construir paso a paso»** — en `juegos/` hay **11**, y el índice de
  juegos enlaza 11. Sobra uno en la cuenta del hub.
- **El bloque «✅ Evaluar» no se parece a la rúbrica de la S20.** El hub promete
  «El proyecto está documentado: qué hace, cómo se usa, créditos» y «Se valoran y comentan
  los proyectos de los compañeros con criterio»; la rúbrica real puntúa Funciona (3) ·
  Usa lo aprendido (3) · Se entiende solo (2) · Lo cuentas bien (2). Lo de comentar los
  proyectos de los compañeros es además un resto del enfoque «comunidad Scratch» que la
  decisión 8 daba por eliminado.

### 5.3 · El panel «Saber / Hacer / Evaluar» — decisión pendiente, no defecto

La objeción de que «hilos paralelos» y «broadcast (mensajes)» son terminología excesiva
para 1º de ESO es razonable, pero el dato que falta para decidir es este: **ese panel es la
plantilla común de T1 y T2 y el T3 —el trimestre terminado— ya no lo usa.** Su hub es la
«Academia Cyber-IES», con otra estructura entera.

Así que la pregunta real no es si el vocabulario es duro, sino **para quién es ese panel**:

- si es la vitrina de los saberes básicos LOMLOE, el vocabulario curricular está bien y lo
  que sobra es que se lo coma la portada del alumno;
- si es lo primero que lee el alumno, hay que reescribirlo en su idioma;
- y si se toca, se toca en T1 **y** en T2, o los dos hubs dejan de parecerse.

### 5.4 · La S04, por segunda vez

Dos lectores independientes se han parado en el mismo sitio. La `DECISIONES_T1.md` ya
ofrecía la alternativa («Condicionales I: repetir hasta que»). El único dato que decide es
**qué pone en Moodle**, y eso no está en el repo: si el título de allí se puede cambiar en
dos minutos, la contradicción deliberada deja de merecer la pena.

---

## 6. Estado: qué se ha arreglado

Todo lo de arriba está aplicado, en los generadores y regenerado, en seis commits locales.
Las decisiones que he tomado por mi cuenta al arreglarlo están en `DECISIONES_T1.md`,
puntos 12 a 20.

| Punto | Estado |
|---|---|
| 1.1 · S13, la variable `Nivel` | ✅ se crea y se inicializa; y se avisa de mover el objeto Meta |
| 1.2 · S11, el balón sin colocar | ✅ segundo programa con bandera verde; el gato también fija dirección |
| 1.3 · S16, el final frágil | ✅ umbral −155; fuera el rebote selectivo que no existía |
| 1.4 · S09, el rango 1–10 | ✅ pasa a 1–5 |
| 2.1 · la rúbrica prometida | ✅ publicada en la S17; la S20 y el hub enlazan a ella |
| 2.2 · S19, actividad ≠ checklist | ✅ dos mejoras obligatorias y una a elegir |
| 2.3 · el kit de siete piezas | ✅ octava pieza: `esconder` / `mostrar` |
| 2.4 · la numeración | ✅ las 20 con Comprueba = 3 y Tu actividad = 4 (S20 aparte, a propósito) |
| 2.5 · S03, «dibujar» | ✅ recorrer, y un aviso de que no queda pintado |
| 2.6 · detalles | ✅ S05, S06 y S15 corregidas |
| 5.1 · `PROGRAMACION.md` | ✅ 20 sesiones, T3 con 18, y la dotación real: **2 h/semana** |
| 5.2 · el hub | ✅ 11 juegos, criterios = rúbrica, y la promesa de la S17 cumplida |
| 5.3 · Saber/Hacer/Evaluar | ✅ reescrito en lenguaje de 1º ESO, sólo en T1 |
| 5.4 · el título de la S04 | ⏸️ **te toca a ti**: depende de qué pone en Moodle |
| 2.6 · `iniciar sonido (Pop)` | ⏸️ **te toca a ti**: dos segundos en el editor |

### La longitud, con la dotación real delante

2 h/semana × ~13 semanas = unas 26 clases en el primer trimestre, y hay 20 sesiones.
Sobran seis, y eso es bueno: son el colchón de las que se comen dos clases. Está anotado
en `PROGRAMACION.md` para que dentro de un año siga teniendo sentido.

### Lo que sigue pendiente, y no es de T1

De la lista de `CLAUDE.md`: las cuatro decisiones de la auditoría, el `node_modules`
comprometido y roto, y el `s02.js` que se carga dos veces en T3 Ciberseguridad.

---

## 7. Lo que vino después: el proyecto final

Esta revisión se hizo sobre las 20 sesiones. Al decidir Manuel que el proyecto final sería
un juego completo elegido entre varias opciones, y que esas opciones serían las de
`juegos/`, apareció una pieza que esta revisión no había mirado: **las once páginas de
juegos eran plantillas vacías** —la misma frase de «conceptos que trabaja» en las once, con
un marcador de posición sin rellenar— **y sus once guías en PDF están hechas con
Scratch 2**.

Eso está resuelto en la tanda siguiente (`DECISIONES_T1.md`, puntos 21 a 26): tres bases
redibujadas en Scratch 3 con el formato de las sesiones, la S17 reescrita alrededor de
ellas, y el índice de juegos separando las tres opciones, las cuatro que ya son sesiones y
las de ampliación.

Queda pendiente de la lista de arriba, sin cambios: el **título de la S04 en Moodle** y el
nombre del **sonido `Pop`** en el editor.

---

## 8. Inventario de numeraciones (sept-2026)

Manuel vio en la S01 que la numeración no se entendía: «se confunden los pasos generales con los
particulares y la numeración de qué es cada cosa». Tenía razón, y no era una manía estética.
En esa pantalla había **tres numeraciones con la misma pinta**: la sección `❷ Lee este programa`,
la zona `❷ Área de código` dentro del dibujo, y los pasos `1, 2, 3…` de tres listas distintas.
La regla que resuelve esto está en el README del taller. Este es el inventario que la aplica.

**32 listas numeradas** en las 20 sesiones y las 3 páginas de juego.

### Sin número · lista de conceptos sin orden (4)

| Dónde | Qué es |
|---|---|
| S01 · 1 · Dónde está cada cosa | Las cuatro zonas del editor |
| S09 · 1 · Tres cosas nuevas | Tres bloques que se estrenan |
| S12 · 1 · Dos bloques nuevos y una idea | Dos bloques y un concepto |
| S19 · 1 · Depurar es buscar, no adivinar | Dos herramientas alternativas |

Ninguna tiene orden: nadie hace «primero la paleta y luego el área de código».

### «Paso N» · acciones del alumno (15)

Las catorce listas de **«Tu actividad»** (S01, S04, S06, S08–S16, S18, S19) y el **guion del
minuto de la S20**.

De propina, esto arregla una referencia que ya existía: la pista de la S13 dice «la variable Nivel
que has creado en el **paso 5**», y hasta ahora el alumno tenía que contar renglones. Ahora el
renglón se llama literalmente «Paso 5».

### Número simple · secuencia de funcionamiento (13)

Las listas que explican qué hace un programa: S01, S02, S03, S04, S05, S06, S07, S08, S09, S10,
S11, S14 y S15, todas en su sección 2.

**Cuatro de ellas prometen un orden que no cumplen**, y eso es contenido, no diseño:

| Sesión | Qué pasa |
|---|---|
| **S06** | El punto 5 explica el `fijar estilo de rotación`, que es **el primer bloque** del programa |
| **S11** | Los puntos 5 y 6 no son ejecución: uno explica por qué hace falta el segundo programa y el otro dice cómo se crea un mensaje |
| **S15** | Son **dos programas que corren a la vez**. No hay un orden único que numerar |
| **S04** | Los puntos 3 y 4 son **las dos ramas** de una decisión, no dos pasos seguidos |

Se arreglan las tres primeras. La S04 se deja: leída como narración de lo que pasa en cada vuelta
del bucle funciona, y tocarla sería reescribir por una regla, no por un problema.

### Identificadores · se quedan con su número (2)

| Dónde | Quién apunta |
|---|---|
| Las **8 piezas del kit** de la S18 | 13 veces desde la S19 y las tres páginas de juego: «Pieza 6 de la S18» |
| Los **9 puntos de la ficha** de la S17 | Desde la S18 («el punto 3 de tu ficha») y desde su propio checklist |

Comprobado buscando en el sitio, no a ojo. Nada más pasa la prueba: **ningún texto apunta a un
número de sección**, así que las secciones son posición pura y se quedan como están.

### Lo único que no es texto

El dibujo del editor de la S01 lleva los números **dentro del SVG** (`diagramas.py`, la función
`badge`). Si la leyenda pierde los números, el dibujo también: pasa a llevar los nombres. Y cae
con ellos la frase «Fíjate en la **1**: los bloques están repartidos por colores», que hay que
reescribir.

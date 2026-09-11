# Decisiones que he tomado por mi cuenta · T1 Scratch

Me dijiste que tirara del tirón y que en caso de duda decidiera yo. Esto es todo lo que he
decidido sin preguntar, para que lo revises de una sentada. Cada una lleva el porqué y, si te
parece mal, lo que costaría deshacerla.

---

## 1. Los títulos de las 20 sesiones no se han tocado

**Qué he hecho:** he reescrito el contenido entero de s01–s20, pero los títulos son
exactamente los que ya tenías.

**Por qué:** no sé qué tienes escrito en Moodle. Cambiar un título rompería la correspondencia
entre lo que el alumno ve allí y lo que ve aquí, y eso es peor que un título mejorable.

**Deshacer:** trivial, es un diccionario en el generador.

## 2. S04 conserva el título «Condicionales I» pero lo desmiente en la propia página

**Qué he hecho:** la sesión empieza con un aviso que dice, con esas palabras, que ahí todavía
no hay ningún `si… entonces`, que lo de hoy es `repetir hasta que` y que el nombre viene del
cuadernillo antiguo.

**Por qué:** es el defecto que encontré en la auditoría —el ejercicio 4 se llama «Condicionales I»
y no tiene ningún condicional— y no quería ni perpetuarlo en silencio ni romperte la
numeración. Decírselo al alumno cuesta tres líneas y le evita la confusión.

**Alternativa si no te convence:** renombrarla «Condicionales I: repetir hasta que».

## 3. El piloto `ejercicios/ej05.html` se ha absorbido dentro de `s05.html` y se ha borrado

**Qué he hecho:** el contenido está íntegro en la sesión 5. La carpeta `ejercicios/` ya no existe.

**Por qué:** mantener las dos habría sido duplicar el mismo material, y al alumno le ahorra un
clic: entra desde Moodle y ya está en la página de trabajo. Nunca llegó a estar en el repo (era
un archivo sin seguimiento), así que no se ha perdido nada del historial.

## 4. El cuadernillo pasa a consulta, con la página exacta

**Qué he hecho:** ninguna sesión abre ya el PDF de 6 MB por la página 1. Las sesiones 01–11
enlazan `#page=N` a su página concreta; las 12–20 no lo enlazan porque no tienen equivalente.

**Cómo he sacado los números de página:** extrayendo el texto del PDF página a página, no a ojo.
La correspondencia es: S01→4, S02→7, S03→9, S04→10, S05→11, S06→12, S07→13, S08→14, S09→15,
S10→16, S11→17.

**En el hub** la tarjeta ya no dice «PDF imprimible para alumnado» sino que avisa de que es
antiguo y de que varios bloques no se llaman así.

## 5. El tambor desaparece

**Qué he hecho:** donde el cuadernillo usaba `tocar tambor (38) durante (2) pulsos` he puesto
`iniciar sonido`.

**Por qué:** el tambor es de la extensión **Música**, que no está en la paleta hasta que la
añades a mano, y además ya no se mide en pulsos sino en compases. Meter una extensión en la
sesión 3, sólo para hacer un ruido, es fricción a cambio de nada.

## 6. El quiz de la S09 suma en vez de multiplicar, y enseña los números con `mostrar variable`

**Qué he hecho:** en vez de construir la pregunta con dos `unir` anidados, el programa muestra
las dos variables en el escenario y pregunta «¿Cuánto suman?».

**Por qué:** el `unir` dentro de `unir` es un salto de dificultad grande para 1º de ESO y
además hacía el bloque tan ancho que no se leía a media pantalla. De paso entra
`mostrar variable`, que está en la paleta y no aparecía en ninguna sesión.

## 7. La entrega de la S17 no es un `.sb3`

**Qué he hecho:** en la sesión de diseño se entrega la ficha de nueve puntos escrita en Moodle.

**Por qué:** ese día no se programa, y pedir un archivo de proyecto obligaría a fabricar algo
vacío sólo para cumplir el trámite.

## 8. Correcciones de coherencia en el hub del trimestre

Tres frases decían cosas que no se corresponden con cómo trabajáis:

| Decía | Dice ahora | Motivo |
|---|---|---|
| «Compartir y comentar proyectos en la comunidad Scratch» | «Descargar el proyecto en un `.sb3` y entregarlo en Moodle» | Trabajáis **sin cuenta**: no hay comunidad a la que subir nada |
| «Variables, listas y mensajes» | «Variables y mensajes entre objetos» | Las listas no se tocan en ninguna de las 20 sesiones |
| «Cada semana se trabaja sobre un mini-reto del cuadernillo» | El flujo real: leer un programa, contestar, hacer la actividad, entregar | El cuadernillo ya no es el material de trabajo |

También he añadido un botón **Abrir Scratch** el primero de los recursos.

## 9. `presentacion.html`: higiene sin tocar el diseño

Era la única página de T1 con dos `h1`, sin `<main>` y sin metadatos. Le he puesto description,
canonical, Open Graph y favicon, he convertido el segundo `h1` en `h2` **con exactamente el mismo
tamaño y aspecto**, la he envuelto en `<main>` y he dado nombre accesible a las flechas de
navegación.

**Lo que no le he puesto, a propósito:** el enlace «saltar al contenido». Es una presentación a
pantalla completa sin navegación repetida, así que no hay nada que saltar, y añadirlo sería
cumplir un checklist en vez de resolver un problema. Es la única marca que queda en la auditoría
de T1 y está ahí a sabiendas.

## 10. No he tocado nada fuera de T1

Ni T2, ni T3, ni el `node_modules` del repo, ni el `s02.js` duplicado de Ciberseguridad.
Me dijiste que sólo lo de Scratch.

## 11. No he hecho push

Los cinco commits están en local. El push lo haces tú desde GitHub Desktop cuando lo hayas visto.

---

# De propina: tres defectos más del cuadernillo

Salieron al extraer el texto para localizar las páginas. No afectan al material nuevo, pero
explican confusiones que habrás visto en clase:

1. **No existe el «ejercicio 3».** La página 9 es el ejercicio 2 y la 10 ya es el ejercicio 4.
   Tu sesión 3 decía «Cuadernillo: ejercicios 2 y 3», y ese ejercicio 3 nunca ha estado ahí.
2. **Hay dos ejercicios distintos numerados como «12».** El de la página 18 (esquivar pelotas
   que caen) y el de la 19 (el fantasma que persigue). Son juegos diferentes con el mismo número.
3. **La numeración de las secciones está mal en tres sitios:** «17 Variables I» donde debería
   poner 7, y dos secciones numeradas «8» seguidas (Variables II y Juegos I).

---

# Qué te toca a ti ahora

1. **Abrir dos o tres sesiones** con Scratch al lado, a media pantalla, y decirme si el tono y la
   longitud te valen para 1º de ESO. Te recomiendo la **S09** (la más densa), la **S12** (la de
   los bloques más largos) y la **S18** (el kit de piezas).
2. **Mirar las cuatro decisiones que más te podrían chirriar:** la 2 (el aviso de S04), la 3
   (borrar `ejercicios/`), la 6 (sumas en vez de multiplicaciones) y la 9 (el skip-link que no he
   puesto).
3. **Hacer push** desde GitHub Desktop si te parece bien.

---

# Segunda tanda · revisión de las 20 sesiones (sept-2026)

Me dijiste otra vez que tirara adelante y aplicara mi criterio. Esto es lo que he
decidido yo, en la ronda que arregla lo que encontró la revisión
(`REVISION_T1_SESIONES.md`). Mismo trato: el porqué, y qué costaría deshacerlo.

## 12. El balón de la S11 gana un segundo programa, no se le mete la colocación dentro del `al recibir`

**Por qué:** si la colocación va dentro del `al recibir (patada)`, el balón da un salto
justo en el momento del chute y se ve feo. Con un `al hacer clic en 🏳` propio, el balón se
coloca antes de empezar y el chute es limpio. De paso el alumno ve que **un objeto puede
tener varios programas**, que es lo que va a necesitar en el proyecto final.

**Deshacer:** trivial, es la lista `C11` del generador.

## 13. El umbral del Pong baja a −155, y desaparece la alternativa del rebote selectivo

**Por qué:** −170 sólo salta si la pelota es pequeña; con una más grande la partida no
acaba nunca. Con la pala en −140, a −155 la pelota ya ha pasado de largo y se detecta
siempre, antes de llegar al borde. Y he quitado lo de «cambia el rebote por uno que sólo
mire los lados y el techo» porque **eso no es un bloque**: montarlo pide condicionales
sobre `posición x` que no se enseñan.

**Si no te convence:** el número está en `FIN16`, en un sitio.

## 14. La rúbrica se publica al final de la ficha de diseño de la S17, no como sección aparte

**Por qué:** como sección propia habría dejado la S17 con seis, y el trimestre entero
acaba de quedar con «Comprueba» en el 3 y «Tu actividad» en el 4. Y donde de verdad sirve
es ahí: el alumno escribe cómo se gana y cómo se pierde con los puntos delante.

## 15. En la S19 la pantalla de inicio y la de fin pasan a ser obligatorias

**Por qué:** la actividad decía «elige tres, no todas» y el checklist exigía esas tres
**más** las dos pantallas. Había que romper el empate por un lado. He elegido hacerlas
obligatorias porque son las dos que sostienen «se entiende solo», que vale 2 puntos.

**Alternativa:** quitarlas del checklist y dejar las tres libres.

## 16. La octava pieza del kit es `esconder` / `mostrar`, y no entran ni «rebotar» ni «mensajes»

El plan hablaba de ocho piezas y había siete. He añadido la que faltaba de verdad:
`esconder` / `mostrar` no aparecía en **ninguna** de las 20 sesiones y la necesitan dos de
las ideas que el catálogo de la S17 marca como fáciles.

**Las otras dos no las he metido a propósito:** `si toca un borde, rebotar` es un bloque
suelto que ya sale en S03, S04, S06 y S15 y no necesita ficha; y los mensajes ya están
dentro de la pieza 6, que es como se usan de verdad en un proyecto.

## 17. La S20 se queda con cuatro secciones

Las otras diecinueve van 1–5. La S20 no tiene nada que construir: su actividad es
presentar. Añadirle un «Tu actividad» de relleno para cuadrar la numeración habría sido
peor que la asimetría. Queda a sabiendas.

## 18. La S03 cambia «dibujar» por «recorrer» en vez de añadir la extensión Lápiz

**Por qué:** la sesión prometía dibujar tres figuras y sin la extensión **Lápiz** no queda
ni una línea en pantalla. Se podía arreglar de dos maneras y he elegido la barata: cambiar
el verbo y avisar de que el camino no se queda pintado. Meter una extensión en la sesión 3
—que es justo lo que la regla de estilo 3 desaconseja— para adornar un ejercicio de bucles
no compensa.

**Si prefieres el lápiz:** son dos bloques (`bajar lápiz` y el botón de extensiones) y una
frase, en `P03`.

## 19. El bloque «Saber» del hub se reescribe sólo en T1

El hub hablaba de *descomposición, abstracción, algoritmia, hilos paralelos y broadcast* en
la portada que ve un niño de doce años. El contenido es el mismo, dicho en su idioma. **T2
comparte la plantilla pero no el texto** —sus contenidos son de micro:bit—, así que nada se
descuadra. El vocabulario curricular sigue donde le corresponde, en `PROGRAMACION.md`.

## 20. `iniciar sonido (Pop)` se queda, pendiente de verificar

Aparece en S11, S12, S16 y S18. El `COTEJO` sólo dejó cerrado **Miau**. No lo he cambiado
porque casi todos los objetos de la biblioteca traen ese sonido, pero **conviene que lo
mires en el editor**: si el objeto que elige el alumno no lo trae, el bloque saldrá con
otro nombre — que es el sexto fallo de la tabla de la S19.

---

## Y una corrección a mi propia revisión

Dije que la S19 era «la candidata clara a recortar» por sus 861 palabras. Medí mal: **300
de esas palabras son las dos tablas de consulta**, que se escanean, no se leen. Su prosa
son 559 palabras, por debajo de la media de las veinte (609). La he aligerado igualmente
—las frases eran largas— pero la alarma estaba inflada. La sesión con más prosa es ahora la
**S11**, con 753, y es a propósito: es la que ha ganado el programa de colocación del balón.

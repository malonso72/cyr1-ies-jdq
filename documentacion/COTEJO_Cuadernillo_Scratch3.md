# Cotejo del cuadernillo de Scratch con Scratch 3

**Cuadernillo:** *Ejercicios Scratch · Lógica de Programación Didáctica*, Prof. Miguel Mejía C. — 20 páginas, 12 ejercicios.
**Versión que usa:** Scratch **2.0** (interfaz gris, paleta en dos columnas, pestaña «Programas»).
**Contexto real de clase:** Scratch **3 en el navegador**, ordenadores **Linux**, alumnado **sin cuenta**.

**Método:** revisión página a página de las 15 páginas con bloques (5–19), y transcripción de las
**ocho paletas reales** del editor a partir de las capturas de Manuel (10 sept 2026). Todos los nombres
de la columna «Scratch 3» están **verificados contra el editor**, no de memoria.

---

## 1. Lo que hace que un alumno se atasque

### 🔴 Bloques que NO están en la paleta

| Cuadernillo | Dónde | Qué pasa hoy |
|---|---|---|
| `tocar tambor (38) durante (2) pulsos` | Ej. 2, 3 y 11 | Es de la extensión **Música**. No aparece hasta añadirla con el botón de extensiones (abajo a la izquierda). Y ya no se mide en «pulsos» sino en **compases**. |
| Categoría **Lápiz** (fija en la paleta) | Pág. 12, captura | En Scratch 3 es una **extensión**. La categoría no existe por defecto. |

Confirmado en las capturas: las categorías son **Movimiento, Apariencia, Sonido, Eventos, Control,
Sensores, Operadores, Variables y Mis bloques**. Ni Música ni Lápiz.

### 🔴 Instrucciones imposibles de seguir

| Cuadernillo | Problema |
|---|---|
| Págs. 3–4: «Descarga e instalación» → *haz clic en descargar* | No hay Scratch de escritorio oficial para Linux, y además trabajáis online. Dos páginas que no llevan a ninguna parte. |
| Pág. 12: «1‑Clic en disfraz, 2‑Escogemos los bloques de apariencia…» | Esa interfaz ya no existe: hoy son iconos redondos en columna y las pestañas son **Código / Disfraces / Sonidos**. |
| Pág. 15: captura con «Nueva variable / Nueva lista / Nuevo objeto» | Hoy son botones **Crear una variable** y **Crear una lista**, y el objeto se añade con el botón flotante del gato. |

### 🟠 Bloques que existen pero se llaman distinto

Todos verificados en el editor:

| Cuadernillo (Scratch 2) | Scratch 3 — nombre exacto | Categoría | Aparece en |
|---|---|---|---|
| `al presionar 🏳` | **`al hacer clic en 🏳`** | Eventos | todos |
| `tocar sonido (miau)` | **`iniciar sonido (Miau)`** | Sonido | ej. 1, 2, 3, 5 |
| *(no existía)* | también hay `tocar sonido (Miau) hasta que termine` | Sonido | — |
| `detener programa` · `detener todo` | **`detener (todos ▾)`** | Control | ej. 1, 10, 11, 12 |
| `cambiar el disfraz a (disfraz1)` | **`cambiar disfraz a (costume2 ▾)`** | Apariencia | ej. 6, 11 |
| `decir (…) por (2) segundos` | **`decir (¡Hola!) durante (2) segundos`** | Apariencia | ej. 7, 8, 9, 12 |
| `pensar (…) por (2) segundos` | **`pensar (Umm...) durante (2) segundos`** | Apariencia | pág. 12 |
| `fijar (num1) a (respuesta)` | **`dar a (num1 ▾) el valor (respuesta)`** | Variables | ej. 8, 9 |
| **`cambiar (Aciertos) por (1)`** | **`sumar a (Aciertos ▾) (1)`** ⚠️ | Variables | ej. 9 |
| `número al azar entre (1) y (10)` | **`número aleatorio entre (1) y (10)`** | Operadores | ej. 9, 10 |
| `si <> / si no` | **`si <> entonces / si no`** | Control | ej. 9 |
| `enviar a todos (patada)` | **`enviar (mensaje1 ▾)`** | Eventos | ej. 11, 12 |
| **`rebotar si está tocando un borde`** | **`si toca un borde, rebotar`** ⚠️ | Movimiento | ej. 12 |
| pestañas `Programas / Disfraces / Sonidos` | **Código / Disfraces / Sonidos** | interfaz | capturas |

⚠️ **Dos correcciones sobre mi primera versión de esta tabla**, ya con la paleta delante:

- `cambiar (variable) por (1)` **sí cambia**: hoy es **`sumar a (variable) (1)`**. Yo lo había dado por
  igual. Es de los bloques que más se usan en el ejercicio 9.
- El de rebotar no es «rebotar si toca un borde» sino **`si toca un borde, rebotar`** — con la condición
  delante y coma incluida.

### 🟡 Nombres por defecto que el alumno ve en pantalla

Esto no es un cambio de bloque, pero despista igual y conviene que el material lo use tal cual:

| El cuadernillo dice | El alumno ve realmente |
|---|---|
| «Objeto1», «Objeto2» | **Sprite1**, Sprite2 |
| «disfraz1», «disfraz2» | **costume1**, **costume2** |
| `preguntar (¿Cuál es tu nombre?)` | el texto por defecto es **`¿Cómo te llamas?`** |
| — | el sonido del gato sí es **Miau** |

Que los disfraces se llamen `costume1` en un editor en español es raro, pero es lo que hay.

### 🟡 Convenio de direcciones

El cuadernillo usa **270, 315, 225**. El editor trabaja en el rango **−180…180**, así que muestra
**−90, −45, −135**. El bloque es `apuntar en dirección (90)` y el valor se escribe directo.
La página 7 del cuadernillo **se contradice sola**: arriba dibuja la rosa con 315/270/225 y justo
debajo enseña el selector con (−90) izquierda.

### ✅ Lo que no ha cambiado nada

`mover (10) pasos` · `girar ↻ (15) grados` · `esperar (1) segundos` · `repetir (10)` · `por siempre` ·
`repetir hasta que <>` · `esperar hasta que <>` · `apuntar en dirección (90)` ·
`preguntar (…) y esperar` · `respuesta` · `unir (manzana) (plátano)` · `mostrar variable` ·
`esconder variable` · `¿tecla (espacio ▾) presionada?` · `¿tocando (…)?` · `siguiente disfraz` ·
`al recibir (…)` · `mostrar` · `esconder` · operadores `+ − * / = > <` · `y` · `o` · `no`

**Recuento final:** ~25 bloques distintos en el cuadernillo. **12 cambian de nombre**,
**2 ya no están en la paleta**, **4 nombres por defecto** distintos de los del texto, y el resto igual.

---

## 2. Defectos del cuadernillo que no tienen que ver con la versión

- **El ejercicio 4 se titula «Condicionales I» y no tiene ningún condicional.** Usa `repetir hasta que`,
  que es un bucle. El primer `si… entonces` real aparece en el ejercicio 5.
- **Numeración repetida:** hay dos secciones «8» (*Variables II* y *Juegos I*).
- **El ejercicio 12 no lo usa ninguna sesión** de la web.
- **El ejercicio 12 usa como fondo una foto de un estadio** de terceros.
- **Progresión por bloques, no por proyectos:** del ejercicio 1 al 9 se coleccionan piezas sueltas.

---

## 3. Lo que el material nuevo debe decir y el cuadernillo no puede

- Se trabaja en **scratch.mit.edu**, en el navegador. No hay nada que instalar.
- **Sin cuenta, el proyecto sólo vive en la pestaña.** Si se cierra sin descargar, se pierde.
- Al terminar: **Archivo → Guardar en tu ordenador** → aparece un `.sb3` en **Descargas** → se sube a Moodle.
- Sin Internet no hay Scratch.

---

## 4. Estado

La columna de Scratch 3 está **cerrada y verificada**. Ya se puede escribir el material de las 20 sesiones
sin riesgo de repetir el problema del cuadernillo.

El piloto del **Ejercicio 5** ya usa todos los nombres correctos —`al hacer clic en`, `repetir hasta que`,
`si … entonces`, `apuntar en dirección`, `mover … pasos`, `iniciar sonido (Miau)` y
`fijar estilo de rotación a (no rotar)`— y se le ha corregido la entrega para reflejar que, sin cuenta,
no se «guarda»: se **descarga**.

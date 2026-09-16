# Pruebas de T3 · Academia Cyber-IES

T1 y T2 se generan desde `documentacion/generadores-t1/` y `generadores-t2/`, y cada taller
trae su propio test. **T3 está escrito a mano**: las 18 sesiones, los 10 retos y el motor
`academia.js` se editan directamente. Esto es lo único que hay para que un cambio no rompa
otra cosa sin que nadie se entere.

```
cd /tmp && npm i jsdom          # sólo la primera vez de cada sesión: /tmp se limpia
cd documentacion/pruebas-t3
node test_academia.js           # las 32 páginas + el motor
node test_academia.js s05 s13   # sólo esas
```

Son **2120 comprobaciones**. Salida esperada: `0 fallos`.

Y además, siempre, los tres verificadores del repo:

```
python3 scripts/verificar_html.py
python3 scripts/comprobar_enlaces.py
python3 scripts/verificar_enlaces.py
```

## Qué comprueba

**Cómo funciona.** Las páginas no se abren con `file://` sino desde un servidor de ficheros
falso (`http://academia.local/`, atendido con el disco del repo). Hacen falta las dos cosas:
un origen `http` para que el navegador simulado dé `localStorage` —donde vive toda la
Academia— y un servidor de verdad para que el CSS y el JS locales se carguen y la página
funcione. La red está cortada: si una página pide algo de fuera, no lo recibe.

**De toda página:** un solo `h1`, una sola región principal (`<main>` o `role="main"`) con
`id="main-content"`, skip-link, pie, `lang="es"`, canonical, `description`, viewport; ningún
error de JavaScript; ningún fichero pedido que no exista; ningún enlace interno roto; cada
campo con etiqueta, cada botón con texto, cada imagen con `alt`, cada SVG etiquetado, y
`rel="noopener"` en los enlaces que abren pestaña.

**De cada sesión:** que están los seis bloques en su orden (`mision`, `teoria`,
`entrenamiento`, `juego`, `informe`, `diploma`), que la barra de progreso los acompaña, que
al abrir sólo está activo el primero, que `SESION_ID` es el que toca, que `irABloque` mueve
el bloque activo y marca el progreso, y —lo importante— **que el informe no acepta respuestas
basura**: se rellena con `f f f f f f f f`, se pulsa, y la sesión no puede darse por
completada. Después se rellena con un texto de verdad y entonces sí: insignia, salto al
bloque del diploma, código con la forma `XXXX-0000` y respuestas guardadas.

**Del motor (`academia.js`):** `respuestaInformeValida` con casos buenos y malos, la clave de
pareja (que ignora mayúsculas y espacios pero no el orden), el código de finalización (misma
forma, estable el mismo día, distinto si cambia la puntuación) y **el archivo de parejas en
ordenadores compartidos**, que es lo más delicado que tiene T3: con nombres ya guardados sale
el aviso «¿sois vosotros?»; «Sí, seguimos» lo quita sin tocar nada; «No, somos otra pareja»
archiva el progreso de la anterior y deja el ordenador limpio; y si esa pareja vuelve a
escribir sus nombres —aunque sea con otras mayúsculas— lo recupera y el archivo se borra para
que no se duplique.

## Dos excepciones, a propósito

- **S12-alt y S13 no se completan con un informe genérico.** Piden además palabras clave del
  tema (los pasos ante un ciberacoso, la idea de interés público, qué datos se deducen de una
  foto). El test lo acepta, pero entonces exige que la página **diga qué falta** en vez de
  quedarse callada. Al final del todo dice cuántas sesiones se completan y cuáles piden más.
- **La tienda falsa de V-Bucks (`s16-reto-vbucks.html`) no lleva pie.** Un pie con el nombre
  del instituto destriparía la simulación antes de que el alumnado descubra la estafa. Por la
  misma razón lleva `noindex` y está fuera del `sitemap.xml`: una página que imita a una
  tienda real no debe salir en un buscador, sólo abrirse desde la sesión 16.

## `arreglos_t3.py`

De un solo uso y **ya no sirve**: es el guion con el que se arreglaron de golpe los 55 fallos
que sacó la primera pasada (canonical en 30 páginas, descripciones de los 10 retos, pies,
`aria-label` de los campos de S01 y S02, skip-link del hub). Se conserva para dejar constancia
de qué se tocó. Las páginas de T3 se editan a mano; esto no es un generador.

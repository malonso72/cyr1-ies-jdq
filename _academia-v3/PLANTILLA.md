# Academia Cyber-IES · Plantilla maestra

Documento técnico-pedagógico que rige las **18 sesiones** del bloque T3
en la versión 3 (curso 2026-27, sin cuadernillo impreso).

---

## 1 · Estructura fija de los 6 bloques

Cada sesión HTML tiene **siempre** estos 6 bloques en este orden. La estructura
no cambia entre sesiones; lo que cambia es el TIPO de reto del bloque 4.

| Nº | Bloque | Min | Función pedagógica |
|---|---|---|---|
| 1 | 🎯 Misión | 3 | Gancho narrativo "La Agencia Cyber-IES necesita…" + identidad |
| 2 | 📖 Teoría interactiva | 8-12 | 6 conceptos máx, en 3 sub-pantallas cada uno, microquiz obligatorio para avanzar |
| 3 | 🏋️ Entrenamiento guiado | 6-8 | Práctica corta antes del reto. Siempre dos niveles (uno fácil, uno con matiz) |
| 4 | 🎮 Reto principal | 10-15 | **VARIABLE — ver catálogo abajo** |
| 5 | 📝 Informe del investigador | 5-6 | 3 textareas con guardado en localStorage. Mínimo 8 palabras por respuesta |
| 6 | 🏆 Insignia | 2 | Diploma PNG vía canvas + código único de finalización |

**Total objetivo: 30-50 min por sesión** (Manuel pidió mínimo 30; aceptamos hasta 50 = una clase completa).

**Decisión de diseño:** mejor sesiones que se ajustan a la clase entera (45-50 min) que sesiones cortas que dejan al alumno sin reto. Los HTMLs incluyen guardado en localStorage: el alumno que no termina en una clase puede continuar en la siguiente.

---

## 2 · Mini-insignias progresivas (4 por sesión)

Cada sesión debe otorgar 4 mini-insignias en este orden:

1. **🎖️ Cadete** — tras completar la teoría (microquiz de los 6 conceptos)
2. **🎖️ Analista** — tras completar el entrenamiento (los 2 niveles)
3. **🎖️ Investigador** — tras completar el reto principal
4. **🏆 Detective/Maestro/etc.** — tras enviar el informe (la insignia que da nombre al diploma final)

El nombre de la 4ª insignia varía por sesión (Detective del Glosario, Centinela de Contraseñas,
Cazador de Phishers, etc.). Las 3 primeras son fijas.

---

## 3 · ⚠️ Catálogo de retos distintos (sesión por sesión)

**La advertencia más importante:** si las 18 sesiones tienen el mismo tipo de reto principal,
el alumno se aburre a partir de la S8. La estructura de 6 bloques se mantiene pero
**el TIPO de juego/reto cambia por sesión** para mantener la sorpresa.

| Sesión | Tema | Tipo de reto principal | Notas |
|---|---|---|---|
| S1 | Glosario · 6 conceptos | **Clasificar** (real/inventado) + situaciones | ✅ ya hecho |
| S2 | Contraseñas | **Laboratorio** (probar contraseñas en vivo) | Inventar 5 para Sofía, ver cuánto tardan en romperlas |
| S3 | Phishing | **Simulador SOC** (cronómetro 15s + análisis) | "URL mortal" — decisión rápida con consecuencias |
| S4 | Huella digital | **Investigación guiada** (HIBP, MyActivity) | Ranking OSINT entre la clase |
| S5 | Interland (parte 1) | **Caso narrativo** + launcher externo | Diario de la misión Be Internet Awesome |
| S6 | Interland (parte 2) | **Continuación del caso** | Cierre con reflexión sobre Interland |
| S7 | Perfil de riesgo redes | **Auditoría de perfiles** (calcular nivel BAJO/MEDIO/ALTO) | 5 perfiles ficticios a analizar |
| S8 | Escape Room CCN-CERT | **Diario + launcher externo** | El reto principal es el del CCN |
| S9 | Ingeniería social | **Escape Room interno** (6 técnicas) | ✅ ya existe HTML completo |
| S10 | WhatsApp sospechoso | **Galería de capturas** (8 casos a juzgar) | Ambigüedades deliberadas |
| S11 | Wifi pública | **Aventura interactiva** (decisiones en café/aeropuerto) | ✅ ya existe HTML completo |
| S12 | Derecho al Olvido | **Panel del DPO** (resolver 8 expedientes jurídicos) | ✅ ya existe HTML completo |
| S13 | Caso Lucía OSINT | **Investigación OSINT** (6 publicaciones, sacar datos) | ✅ ya existe HTML completo |
| S14 | Deepfakes | **Torneo Real/Fake** (vidas + bonus por señal) | ✅ ya existe HTML completo |
| S15 | Ciber Cluedo | **Mesa del detective** (línea temporal + pista falsa) | ✅ ya existe HTML completo |
| S16 | Gaming estafas | **Tienda falsa navegable** + 4 anuncios + caso streamer | Ampliar el HTML actual (que solo cubre la tienda) |
| S17 | Caso Marta | **Carpeta del investigador** (6 evidencias a ordenar + informe auto) | ✅ ya existe HTML completo |
| S18 | Examen + cierre | **Academia final** (12 preguntas + ceremonia con las 18 insignias) | ✅ existe el examen; falta ceremonia |

**Recordatorio:** los 9 HTMLs ya existentes (S9, S11-S15, S16-parcial, S17, S18-examen) hay que
**adaptarlos a los 6 bloques de la plantilla** (añadirles misión, teoría, entrenamiento, informe).
Actualmente solo tienen el reto.

---

## 4 · Continuidad entre sesiones

Algunas respuestas del informe se persisten en `localStorage` con clave `academia:s:sNN` y
se reutilizan como **gancho narrativo** en sesiones posteriores. Reglas iniciales:

| De | A | Qué se recupera |
|---|---|---|
| S1 q3 (compromiso) | S2 | "Tú mismo lo dijiste en S1: prometiste…" |
| S2 (contraseña tipo) | S4 | Comprobar si esa contraseña está en HIBP |
| S7 (perfil de riesgo) | S13 | Comparar el perfil propio con el de Lucía |
| S9 (técnica favorita) | S14, S15 | Reusar la técnica identificada como "tu especialidad" |
| S11 (decisión en café) | S17 | Si tu Ana cayó en el portal cautivo, te lo recuerdan |

Implementación: en cada sesión, al entrar al bloque 1 (Misión), leer
`Academia.getSesion('sNN-1')` y, si existe la respuesta esperada, mostrarla en la
narrativa como cita textual del propio alumno.

---

## 5 · Reglas de redacción (1º ESO)

**Lenguaje:**
- Frases de 12-15 palabras máximo.
- Vocabulario técnico inglés (phishing, malware, etc.) siempre acompañado de su
  explicación en español la primera vez que aparece en cada sesión.
- Tono "investigador" pero sin paternalismo: no "chicos y chicas", no "amiguitos".
- Sin condescendencia. Tratar al alumno como cadete real.

**Densidad:**
- 1 idea por bloque visual. Si un párrafo tiene 2 ideas → partirlo en 2.
- Microquiz de 4 opciones (no más): A, B, C, D.
- En las preguntas de comprensión, **2 de cada 8 deben ser ambiguas**: aprenderá más
  del razonamiento que del recuerdo.

**Recompensa intermedia obligatoria:**
- Toast de insignia tras cada bloque mayor (no esperar al final).
- Fila visible de mini-insignias siempre en pantalla.

---

## 6 · Persistencia y privacidad

- Todo en `localStorage` (clave prefijada `academia:`).
- Sin servidor, sin cuentas, sin cookies de terceros.
- Los nombres se piden UNA VEZ y se reutilizan en las 18 sesiones.
- Cada sesión guarda: respuestas del informe, puntuaciones, código, tiempo y mini-insignias.
- Al final del bloque, una página "Mi Bitácora" agrupa todo y exporta a PDF.
- Evidencia para el profesor: 18 PNGs de diploma + (opcional) PDF de bitácora.

---

## 7 · Catálogo de variantes de mecánica usadas en el bloque

Para distinguir visual y mecánicamente las sesiones (evitar la fatiga de la S8):

- **Drag & drop** (S2, S15, S17): arrastrar elementos a contenedores.
- **Cronómetro** (S3): decisiones bajo presión de tiempo.
- **Diálogo interactivo** (S10, S11): tomar decisiones en una conversación.
- **Mapa / línea temporal** (S15, S17): ordenar eventos.
- **Formulario que se "completa solo"** (S17 informe auto): el sistema redacta a partir de tus decisiones.
- **Cámara forense** (S14): comparar imágenes lado a lado.
- **Galería navegable** (S10, S13): pinchar piezas para ver detalle.
- **Tienda navegable** (S16): explorar una web falsa.
- **Escape room** (S9): puzzle con código que se desbloquea por fases.
- **Panel pseudo-profesional** (S12 DPO, S17 investigador): UI temática de adulto.
- **Examen tipo test** (S18): última sesión, formato académico clásico.

Ninguna mecánica debe repetirse más de **3 veces** en el bloque.

---

## 8 · Cómo añadir una sesión nueva (checklist)

Para que el patrón se mantenga al replicar:

- [ ] Copiar `_academia-v3/sesiones/s01.html` como base para `sNN.html`.
- [ ] Cambiar todos los `SESION_ID = 's01'` por el ID nuevo.
- [ ] Sustituir el array `CONCEPTOS` (máx 6) por los conceptos de la sesión.
- [ ] Sustituir el `FALSOS` (si la mecánica de impostor aplica) o quitar la Parte B.
- [ ] Sustituir el array `PARES` (entrenamiento N1) y `FRASES_VF` (entrenamiento N2).
- [ ] Sustituir `SITUACIONES` (6 fáciles + 2 ambiguas mínimo).
- [ ] Si la sesión tiene un reto distinto al de S1, reemplazar el bloque 4 entero por la nueva mecánica.
- [ ] Cambiar el nombre de la insignia final + frase del diploma.
- [ ] Verificar con `node --check` que el JS inline no tiene errores de sintaxis.
- [ ] Probar el flujo completo manualmente.

---

**Versión del documento:** 1.0 · 30 mayo 2026 · Manuel Alonso Herrera

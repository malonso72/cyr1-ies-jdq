# Pendientes · CyR 1º ESO

Lista de lo que queda por completar. Se actualiza con cada sprint.

## Bloqueante para v1.1.0 (Fase E del brief)

### T3 Ciberseguridad — integración de material existente

- [ ] **Presentación pizarra v3**: copiar a `trimestres/t3-ciberseguridad/presentacion.html`
  SIN modificar su CSS interno (preserva su estética dark independiente).
  Manuel debe indicar la ruta local del archivo.
- [ ] **Cuadernillo v6 del alumno**: convertir a `trimestres/t3-ciberseguridad/cuadernillo.html`.
  Si está en DOCX, conversión cuidadosa preservando estructura por sesiones.
  Si está en HTML, ajustar rutas y CSS al nuevo entorno.
- [ ] **Sesiones (16-17 sesiones tipo "Opción D")**: contar el número exacto
  de archivos de sesión existentes en el material original ANTES de generar.
  Crear `sesiones/sNN.html` para cada una, manteniendo el formato Opción D.
- [ ] **Moodle**: crear `trimestres/t3-ciberseguridad/moodle.html` con la tabla
  de templates de entrega + la rúbrica de 4 criterios.
- [ ] **Solucionario**: copiar a `_soluciones/cuadernillo_solucionario_v6.html`
  (privado, NO se despliega).
- [ ] Quitar el `<span class="pending-badge">Pendiente Fase E</span>` de las
  4 tarjetas del hub T3 cuando su material esté integrado.

> **Nota:** la tarjeta T3 del `index.html` (raíz del sitio) NO tiene badge
> "Próximamente" porque su hub es navegable y completo en cuanto a estructura.
> Las tarjetas T1 y T2 sí tienen el badge porque su material es genérico.

## Pendientes de Manuel (no bloqueantes)

- [ ] **Criterios de evaluación LOMLOE concretos** por trimestre. Rellenar el
  `<details class="criterios">` de cada hub.
- [ ] **Bullets de "saber/hacer/evaluar"**: los actuales son una primera
  aproximación. Revisar y ajustar a la programación oficial del departamento.
- [ ] **Duración estimada**: rangos orientativos. Validar con la dotación
  real del curso (depende de cuántas sesiones/semana tenga la asignatura).
- [ ] **Retos transversales**: definir los retos que cruzarán varios
  trimestres y crearlos desde `assets/templates/PLANTILLA_reto.html`.
- [ ] **Herramientas**: añadir editor Scratch online, simulador micro:bit,
  glosario de seguridad, etc.

## Infraestructura

- [ ] **`git init`**: el sistema en el que se generó este repo no tenía
  git instalado. Manuel debe ejecutar al recibirlo:
  ```bash
  cd cyr1-ies-jdq && git init -b main && git add . && \
  git commit -m "Bootstrap del sitio CyR 1º ESO [v1.0.0]"
  ```
- [ ] **Configuración del worker Cloudflare**: crear el subdominio
  `cyr1-ies-jdq.malonso72.workers.dev`. Probar primer deploy con
  `npx wrangler deploy`.
- [ ] **Google Search Console**: añadir verificación si se quiere indexar.
- [ ] **Contador de visitas**: decidir si se añade GoatCounter como en TECI.

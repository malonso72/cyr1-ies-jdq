#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Adapta el reto interno de S12 (originalmente "Despacho DPO") al nuevo lenguaje "Tribunal Digital".

Sustituye SOLO texto visible (entre tags HTML). Evita:
  - Clases CSS (.expediente, .fundamento, .dictamen)
  - IDs (#expediente-actual, etc.)
  - Variables y funciones JS (expedienteActual, fundamentosAplicados...)
  - onclick handlers

Estrategia: sustituciones de cadenas LITERALES y específicas, no por palabras sueltas.
"""
from pathlib import Path

RETO = Path('/sessions/cool-gallant-cray/mnt/cyr1-ies-jdq/_academia-v3/retos/s12-reto-dpo.html')
html = RETO.read_text(encoding='utf-8')

# Sustituciones de cadenas LITERALES (orden importa — primero las más largas)
SUSTITUCIONES = [
    # Título principal y subtítulos
    ('Panel del Delegado de Protección de Datos · Sesión 12 · v1',
     'Tribunal Digital · Sesión 12'),
    ('Despacho del Delegado de Protección de Datos',
     'Tribunal Digital'),
    ('Reglamento General de Protección de Datos · UE 2016/679',
     'Reglas europeas del Derecho al Olvido'),

    # Acreditación e introducción
    ('Por la presente, se les acredita formalmente como <b>Delegados de Protección de Datos</b> (DPO) en prácticas para la resolución de los 8 expedientes que se les remiten a continuación.',
     'Te acreditamos como <b>juez digital en formación</b>. Vas a juzgar los 8 casos que te llegan: ciudadanos que piden borrar información sobre ellos en Google.'),
    ('Su función será examinar cada solicitud de <em>Derecho al Olvido</em> presentada por un ciudadano y emitir resolución motivada conforme al RGPD y a la Ley Orgánica 3/2018 de Protección de Datos Personales y Garantía de los Derechos Digitales.',
     'Tu trabajo: leer cada caso, aplicar las 4 reglas del Derecho al Olvido y decidir si <b>SE BORRA</b> o <b>NO SE BORRA</b> la información de Google.'),
    ('Antes de resolver expedientes',
     'Antes de juzgar los casos'),
    ('Hoja de Fundamentos Jurídicos',
     'Hoja de las 4 reglas'),
    ('hoja de fundamentos',
     'hoja de las reglas'),
    ('hoja de las hoja de las reglas',  # por si algún replace genera duplicado
     'hoja de las reglas'),
    ('que les remite el despacho. Sin esa lectura no podrán dictar resoluciones.',
     'que te explica cuándo SÍ y cuándo NO se borra. Sin leerla no podrás juzgar.'),
    ('Recibir hoja de fundamentos',
     'Leer las 4 reglas del juez'),

    # Casos: titulares de bloques
    ('A. Casos en los que la solicitud SÍ procede',
     'A. Cuándo SÍ se borra'),
    ('B. Casos en los que la solicitud NO procede',
     'B. Cuándo NO se borra'),
    ('— Fin de la hoja de fundamentos —',
     '— Fin de las reglas —'),

    # Cierre / acreditación final
    ('III. Resolución del Despacho',
     'III. Sentencia final'),
    ('Concluida la resolución de los 8 expedientes asignados, se les hace entrega del <b>nombramiento oficial</b> como Delegados de Protección de Datos.',
     'Has juzgado los 8 casos. Aquí tienes tu acreditación como <b>Juez Digital</b> y <b>Guardián de la Privacidad</b>.'),
    ('como Delegados de Protección de Datos en prácticas, por haber resuelto correctamente los expedientes que se les encomendaron conforme a los fundamentos del RGPD y de la LOPDGDD.',
     'como <b>Juez Digital</b>, por haber juzgado los 8 casos del Tribunal aplicando correctamente las reglas del Derecho al Olvido.'),
    ('Fecha de resolución:',
     'Fecha de la sentencia:'),
    ('Fundamentos jurídicos aplicados:',
     'Reglas aplicadas:'),

    # Botones y etiquetas visibles
    ('▸ Recibir hoja de fundamentos',
     '▸ Leer las 4 reglas del juez'),

    # Diploma HTML preview
    ('Delegado/a de Protección de Datos · Promoción 2026',
     'Juez Digital · Promoción 2026'),
    ('El Despacho de Protección de Datos del IES Jiménez de Quesada acredita a',
     'El Tribunal Digital del IES Jiménez de Quesada acredita a'),

    # Canvas (diploma PNG generado)
    ("ctx.fillText('Delegado/a de Protecci�
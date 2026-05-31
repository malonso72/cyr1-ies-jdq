#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Datos de las 6 sesiones nuevas (S4, S5, S6, S7, S8, S10) y ejecutor."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from gen_sesiones_nuevas import build, ROOT

# Reto tipo "launcher externo" (enlaces a sitios + diario + marcar como hecho)
def reto_launcher(intro_texto, enlaces, instrucciones):
    """Genera el HTML del bloque 4 para una sesión tipo launcher externo."""
    enlaces_html = ''.join(f'<a href="{url}" target="_blank" rel="noopener" class="btn-acad oro" style="margin:6px">{label} ↗</a>'
                            for label, url in enlaces)
    return (
        '<div class="reto-externo"><div class="barra-reto"><div class="izq">🛠️ Herramientas externas</div></div>'
        f'<div style="padding:18px;background:#FFF8E1">{intro_texto}<div style="margin:14px 0">{enlaces_html}</div>'
        f'<div style="background:#FFF;border:1px solid var(--bd);border-radius:6px;padding:14px;margin-top:10px"><strong>📋 Pasos:</strong><ol style="margin-left:20px;line-height:1.7">{instrucciones}</ol></div></div></div>'
        '<div class="confirma-reto"><div class="txt"><span class="et">✓ Cuando termines</span>Marca aquí para desbloquear el informe.</div>'
        '<button class="btn-acad verde" id="btn-reto-hecho" onclick="marcarRetoHecho()">✓ He terminado</button></div>'
    )

# Reto tipo "galería con clasificación" (cards con elementos a evaluar)
def reto_galeria(intro_texto, contenedor_id='zona-galeria'):
    return (
        f'<div class="pista">{intro_texto}</div>'
        f'<div id="{contenedor_id}"></div>'
        '<div class="confirma-reto" id="confirma-galeria" style="display:none"><div class="txt"><span class="et">✓ Has terminado</span>Marca aquí para desbloquear el informe.</div>'
        '<button class="btn-acad verde" id="btn-reto-hecho" onclick="marcarRetoHecho()">✓ He terminado</button></div>'
    )


# ── S4 · Lo que internet sabe de ti ─────────────────────────────
S4 = {
    'num': 4,
    'INSIGNIA_FINAL': 'Auditor de Huella Digital',
    'INSIGNIA_NOMBRES': {'cadete': 'Cadete', 'analista': 'Investigador', 'investigador': 'Auditor Junior', 'detective': 'Auditor de Huella Digital'},
    'FRASE_DIPLOMA': 'Lo que pones en internet hoy, te encontrará dentro de 10 años',
    'NOMBRE_ARCHIVO': 'S04-huella-digital',
    'html_vars': {
        'TITULO_CORTO': 'Lo que internet sabe de ti',
        'TITULO_NAV': 'Huella digital',
        'EMOJI': '🔎',
        'TITULO': 'Lo que internet sabe de ti',
        'SUBTITULO': 'Tu email, tus contraseñas, tu actividad… ¿cuánto se sabe de ti en internet? Hoy lo auditas tú mismo.',
        'INS_1': 'Cadete', 'INS_2': 'Investigador', 'INS_3': 'Auditor Junior', 'INS_FINAL_CORTO': 'Auditor',
        'LABEL_JUEGO': 'Investigación',
        'TITULO_MISION': 'Audita tu propia huella digital',
        'GANCHO_EMOCIONAL': '<strong>🎬 Imagínate esto:</strong> tu email aparece en una filtración de hace 5 años. Hoy un atacante ha probado esa contraseña en TODAS tus cuentas. Cae Instagram. Cae Gmail. Cae el banco. <strong>¿Cómo lo evitas? Sabiendo qué hay sobre ti en internet ANTES que ellos.</strong>',
        'NARRATIVA': 'Hoy te conviertes en auditor de tu propia huella digital. Vas a usar las mismas herramientas que usan los profesionales (HIBP, Google MyActivity, WhatsMyName) para investigar QUÉ se sabe de ti.',
        'OBJETIVO_HOY': 'Aprender qué es la huella digital y 3 herramientas clave. Entrenar con 6 V/F. Auditar tu propia presencia online: ¿tu email está filtrado?, ¿qué guarda Google de ti?, ¿qué nombres de usuario tuyos hay sueltos por internet?',
        'CHIP_RETO': '🔎 3 herramientas',
        'BOTON_INICIO': 'Empezar la auditoría',
        'TITULO_TEORIA': '4 conceptos sobre huella digital',
        'INTRO_TEORIA': 'La huella digital es todo lo que internet sabe de ti. Y casi siempre es mucho más de lo que crees.',
        'TITULO_RETO': '🔎 Auditoría guiada',
        'INTRO_RETO': 'Vas a usar 3 herramientas REALES para auditar tu propia presencia digital. Sigue los 5 pasos: te llevará 10-15 minutos.',
        'ZONA_RETO': reto_launcher(
            '<p>Abre las herramientas y completa la investigación. Toma notas mentales para el informe final.</p>',
            [('🔓 Have I Been Pwned', 'https://haveibeenpwned.com/'),
             ('🗂️ Google My Activity', 'https://myactivity.google.com/'),
             ('🌐 WhatsMyName', 'https://whatsmyname.app/')],
            '<li>Entra a <strong>haveibeenpwned.com</strong> y mete tu email principal. ¿Aparece en filtraciones? ¿De qué webs?</li>'
            '<li>Entra a <strong>myactivity.google.com</strong> (con tu cuenta de Google). Mira qué historial guarda de ti: búsquedas, vídeos, ubicaciones.</li>'
            '<li>Entra a <strong>whatsmyname.app</strong> y busca un nombre de usuario tuyo (puede ser de Insta, TikTok). ¿En cuántas otras webs aparece?</li>'
            '<li><strong>Anota mentalmente las 3 cosas que más te han sorprendido.</strong> Las usarás en el informe.</li>'
            '<li>Si encuentras filtraciones tuyas en HIBP: <strong>cambia esas contraseñas YA</strong> en las webs afectadas.</li>'
        ),
        'Q1': '¿Cuál de las 3 herramientas te ha SORPRENDIDO más? ¿Por qué?', 'Q1_AYUDA': 'Sé concreto: nombra la herramienta y qué encontraste.',
        'Q2': '¿Tu email aparece en alguna filtración de HIBP? Si sí, ¿qué vas a hacer esta semana?', 'Q2_AYUDA': 'Si sale, cambia esa contraseña en TODAS las cuentas donde la usabas.',
        'Q3': 'Después de hoy, ¿qué vas a CAMBIAR en cómo gestionas tu presencia en internet?', 'Q3_AYUDA': 'Algo concreto: "voy a poner mi Insta privado", "voy a borrar mi historial de Google", etc.',
        'TEXTO_DIPLOMA': 'por haber auditado su propia huella digital con HIBP, Google MyActivity y WhatsMyName, y haber comprendido el rastro que internet guarda de cada uno de nosotros.',
        'PROXIMO_PASO': 'La Sesión 5 te lleva a Interland, el mundo de Google sobre ciudadanía digital (parte 1).',
        'NEXT_HREF': 's05.html', 'NEXT_LABEL': 'Sesión 5 · Interland (1)',
    },
    'CONCEPTOS': [
        {'nombre': '¿Qué es la huella digital?',
         'queEs': 'Todo lo que internet "sabe" sobre ti: tus cuentas, tu nombre, tus comentarios, tus fotos, tus contraseñas filtradas, tu historial de búsquedas… Mucho de eso lo dejas TÚ sin querer.',
         'ejemplo': {'tipo': 'peligroso', 'texto': '⚠️ Buscas tu nombre en Google y aparece: una foto antigua, un comentario en YouTube de hace 3 años, tu cuenta de TikTok pública, tu email asociado a un foro de hace 5 años. Todo eso es huella digital.'},
         'senales': ['Es la suma de TODO lo que has subido a internet (y de lo que han subido sobre ti).',
                     'Se acumula: cada año hay más, y casi nunca disminuye.',
                     'Otros pueden investigarla (OSINT) y construir un perfil tuyo.'],
         'quiz': {'p': '¿Qué NO es parte de tu huella digital?', 'opciones': ['Tu cuenta de Instagram', 'Una contraseña tuya filtrada en una web vieja', 'Tu altura', 'Tu historial de búsquedas en Google'], 'correcta': 2,
                  'explica': 'Tu altura es un dato físico, no digital. Lo demás (cuentas, contraseñas filtradas, historial) sí está en tu huella.'}},
        {'nombre': 'Have I Been Pwned (HIBP)',
         'queEs': 'haveibeenpwned.com es una web gratis que te dice si tu email o tu contraseña han aparecido en filtraciones públicas. Si salen → cambia esa contraseña en todas las cuentas donde la usabas.',
         'ejemplo': {'tipo': 'bueno', 'texto': '✅ Metes tu email y te dice "apareciste en la filtración de LinkedIn 2021". Vas a LinkedIn, cambias contraseña, activas 2FA y compruebas dónde más usabas esa misma contraseña.'},
         'senales': ['Te dice EN QUÉ webs apareció (LinkedIn, Adobe, Dropbox…) y CUÁNDO.',
                     'Te dice QUÉ datos se filtraron: email, contraseña, número de teléfono…',
                     'Si tu contraseña aparece: nunca la vuelvas a usar en ningún sitio.'],
         'quiz': {'p': 'HIBP te dice que tu email apareció en una filtración con contraseña. ¿Qué haces?', 'opciones': ['Nada, es de hace mucho tiempo', 'Cambio esa contraseña en TODAS las cuentas donde la usaba y activo 2FA', 'Cierro mi email', 'Llamo a la policía'], 'correcta': 1,
                  'explica': 'Cambia la contraseña filtrada en TODAS las cuentas donde la reutilizabas (por eso no hay que reutilizar). Y activa 2FA.'}},
        {'nombre': 'Google My Activity',
         'queEs': 'myactivity.google.com es donde Google guarda TODO lo que haces con tu cuenta: búsquedas, vídeos vistos, sitios visitados, ubicaciones. Puedes ver lo que tiene de ti y borrarlo.',
         'ejemplo': {'tipo': 'bueno', 'texto': '✅ Entras y ves que Google sabe que el martes a las 16:30 buscaste "regalo cumple amigo" y luego "Amazon zapatillas". Lo borras todo o ajustas cuánto tiempo guarda Google ese historial.'},
         'senales': ['Te muestra una línea temporal de toda tu actividad con Google.',
                     'Puedes borrar entradas concretas o todo a la vez.',
                     'Puedes configurar que Google deje de guardar este historial.'],
         'quiz': {'p': '¿Por qué interesa mirar Google My Activity?', 'opciones': ['Para denunciar a Google', 'Para ver qué guarda de ti y decidir si quieres borrarlo', 'Para subir más datos', 'Para cambiar tu email'], 'correcta': 1,
                  'explica': 'Es tu derecho ver y borrar el historial. Mucha gente no sabe siquiera que existe.'}},
        {'nombre': 'WhatsMyName',
         'queEs': 'whatsmyname.app busca un nombre de usuario tuyo (ej. tu @ de Insta) en cientos de webs y te dice EN CUÁLES existe ese mismo usuario. Te enseña tu rastro multiplataforma.',
         'ejemplo': {'tipo': 'bueno', 'texto': '✅ Buscas tu @luciagarcia2012 y descubres que ese mismo nombre existe en TikTok, Twitch, GitHub, foros antiguos… Algunas ni te acuerdas de haber creado.'},
         'senales': ['Usar el MISMO nombre en muchas webs crea un rastro fácil de seguir.',
                     'Cada web encontrada es un punto de entrada para alguien que te investigue.',
                     'Si quieres ser anónimo: usa nombres DISTINTOS en cada cuenta.'],
         'quiz': {'p': '¿Cuál es el mayor riesgo de usar SIEMPRE el mismo nombre de usuario en todas las redes?', 'opciones': ['Que se te olvide', 'Que cualquiera te localice en todas las webs cruzando ese nombre', 'Que no funcione', 'Ningún riesgo'], 'correcta': 1,
                  'explica': 'Es el principio del OSINT: con un nombre único de usuario, un investigador (o un acosador) puede mapear toda tu vida online.'}},
    ],
    'FRASES_VF': [
        {'texto': 'Tu huella digital se acumula con los años y casi nunca disminuye.', 'correcta': True, 'explica': 'Verdadero. Lo que subes hoy puede seguir ahí en 10 años.'},
        {'texto': 'Have I Been Pwned (HIBP) es una web fiable que te dice si tu email ha aparecido en filtraciones.', 'correcta': True, 'explica': 'Verdadero. Es gratis, conocida y usada también por profesionales de seguridad.'},
        {'texto': 'Google MyActivity es donde Google guarda secretamente tu historial sin que puedas verlo.', 'correcta': False, 'explica': 'Falso. Puedes ENTRAR cuando quieras, ver QUÉ guarda y borrarlo. Es tu derecho.'},
        {'texto': 'Usar el mismo nombre de usuario en todas las redes facilita que cualquiera te encuentre y construya tu perfil.', 'correcta': True, 'explica': 'Verdadero. Es la primera técnica de OSINT.'},
        {'texto': 'Si HIBP dice 0 resultados, mi email NUNCA se filtrará en el futuro.', 'correcta': False, 'explica': 'Falso. HIBP solo conoce filtraciones públicas pasadas. Mañana puede haber una nueva.'},
        {'texto': 'Lo que publico en internet con 12 años puede afectarme cuando busque trabajo con 22.', 'correcta': True, 'explica': 'Verdadero. La huella digital persiste. Lo que parece "una tontería" puede llegar a empresas, universidades, futuras parejas.'},
    ],
}


# ── S5 · Misión Interland (parte 1) ─────────────────────────────
S5 = {
    'num': 5,
    'INSIGNIA_FINAL': 'Explorador de Interland',
    'INSIGNIA_NOMBRES': {'cadete': 'Cadete', 'analista': 'Aprendiz', 'investigador': 'Aventurero', 'detective': 'Explorador de Interland'},
    'FRASE_DIPLOMA': 'En Interland, como en internet, ser amable es la primera regla de seguridad',
    'NOMBRE_ARCHIVO': 'S05-interland-p1',
    'html_vars': {
        'TITULO_CORTO': 'Misión Interland (parte 1)',
        'TITULO_NAV': 'Interland 1',
        'EMOJI': '🌍',
        'TITULO': 'Misión Interland · parte 1',
        'SUBTITULO': 'Google ha construido un mundo virtual para enseñarte ciudadanía digital. Hoy entras.',
        'INS_1': 'Cadete', 'INS_2': 'Aprendiz', 'INS_3': 'Aventurero', 'INS_FINAL_CORTO': 'Explorador',
        'LABEL_JUEGO': 'Interland',
        'TITULO_MISION': 'Bienvenido a Interland',
        'GANCHO_EMOCIONAL': '<strong>🎮 Imagínate esto:</strong> un videojuego diseñado por GOOGLE para enseñarte ciberseguridad. Sin meterte la chapa: jugando. Eso existe. Se llama <strong>Interland</strong>. Hoy entras a sus 2 primeros mundos.',
        'NARRATIVA': 'Interland es parte de "Be Internet Awesome", el programa de Google para ciudadanía digital. Tiene 4 mundos (hoy juegas los 2 primeros): Mindful Mountain (comparte con cabeza), Reality River (detecta fake news y phishing). Cada mundo dura unos 10-15 min.',
        'OBJETIVO_HOY': 'Aprender los 4 principios de Be Internet Awesome. Entrenar con 6 V/F. Jugar los 2 primeros mundos de Interland. Anotar en el informe lo que te enseñó cada uno.',
        'CHIP_RETO': '🎮 2 mundos · 25 min',
        'BOTON_INICIO': 'Entrar a Interland',
        'TITULO_TEORIA': 'Be Internet Awesome: los 4 principios',
        'INTRO_TEORIA': 'Google identificó 4 principios para ser un buen ciudadano digital. Hoy ves los 2 primeros (los otros 2 los harás en S6).',
        'TITULO_RETO': '🎮 Juega los 2 primeros mundos',
        'INTRO_RETO': 'Abre Interland en pestaña nueva. Juega el orden recomendado: primero Mindful Mountain, después Reality River. Tarda unos 25 minutos en total.',
        'ZONA_RETO': reto_launcher(
            '<p><strong>Interland</strong> es el videojuego oficial de Google sobre ciudadanía digital. Está en español y es gratis. No necesitas cuenta.</p>',
            [('🎮 Abrir Interland', 'https://beinternetawesome.withgoogle.com/es_es/interland')],
            '<li><strong>Pulsa "Empezar a explorar Interland"</strong> en la web de Google.</li>'
            '<li>Juega <strong>Mindful Mountain</strong> (compartir con cabeza). Dura ~12 min.</li>'
            '<li>Cuando lo termines, vuelve al mapa y juega <strong>Reality River</strong> (detección de bulos). Otros ~12 min.</li>'
            '<li>Cuando hayas completado los 2 mundos, vuelve aquí y rellena el informe.</li>'
            '<li><strong>Pista:</strong> los otros 2 mundos (Kind Kingdom y Tower of Treasure) son para la S6. NO los hagas hoy.</li>'
        ),
        'Q1': '¿Cuál de los 2 mundos (Mindful Mountain o Reality River) te ha gustado MÁS? ¿Por qué?', 'Q1_AYUDA': 'Cuenta algo concreto que te haya enseñado o sorprendido.',
        'Q2': 'En Mindful Mountain enseñan a pensar ANTES de compartir. ¿Has compartido alguna vez algo de lo que te hayas arrepentido después? (No tienes que dar detalles.)', 'Q2_AYUDA': 'Solo sí/no y por qué crees que pasó.',
        'Q3': 'En Reality River enseñan a detectar bulos. ¿Qué señal te ha parecido la MÁS útil para no caer?', 'Q3_AYUDA': 'Ejemplo: "verificar la fuente", "no compartir lo que te enfurece sin comprobarlo"…',
        'TEXTO_DIPLOMA': 'por haber completado los 2 primeros mundos de Interland (Mindful Mountain y Reality River) y comprendido los principios de "Comparte con cabeza" y "No caigas en la trampa".',
        'PROXIMO_PASO': 'La Sesión 6 te lleva a los OTROS 2 mundos de Interland: Kind Kingdom y Tower of Treasure.',
        'NEXT_HREF': 's06.html', 'NEXT_LABEL': 'Sesión 6 · Interland (2)',
    },
    'CONCEPTOS': [
        {'nombre': 'Principio 1 — Comparte con cabeza',
         'queEs': 'Antes de subir algo a internet, pregúntate: ¿lo enseñaría a mis padres? ¿a mi profesor? ¿al jefe del trabajo que tendré en 10 años? Si NO → no lo subas.',
         'ejemplo': {'tipo': 'bueno', 'texto': '✅ Vas a subir una foto graciosa de un amigo sin pedirle permiso. Antes de pulsar "publicar" piensas: "¿le gustaría a él que la subiera?". Si dudas → le preguntas. Si dice no → no la subes.'},
         'senales': ['Lo que subes hoy puede verse para SIEMPRE.', 'Puede afectar a OTRAS personas que aparecen.', 'En caliente (enfadado, eufórico) NUNCA es buen momento para publicar.'],
         'quiz': {'p': 'Antes de publicar algo en redes, lo más importante es preguntarse:', 'opciones': ['¿Tendrá muchos likes?', '¿Lo enseñaría a alguien de confianza fuera de las redes?', '¿Está bien iluminado?', '¿Se ve mi cara?'], 'correcta': 1,
                  'explica': 'Si solo lo enseñarías a un grupo MUY limitado, mejor no lo subas a una red pública.'}},
        {'nombre': 'Principio 2 — No caigas en la trampa',
         'queEs': 'Internet está lleno de bulos, fake news y phishing. Aprende a detectarlos: comprueba la fuente, busca el mismo dato en medios serios, sospecha de lo que te enfurece o asusta.',
         'ejemplo': {'tipo': 'peligroso', 'texto': '⚠️ Tu primo te manda por WhatsApp un vídeo "filtrado" donde un famoso dice algo escandaloso. Antes de reenviarlo: ¿de dónde sale? ¿lo dicen otros medios? ¿es un deepfake?'},
         'senales': ['El titular te indigna o te asusta MUCHO.', 'Te llega por WhatsApp/redes pero no aparece en ningún medio serio.', 'Te piden compartirlo "antes de que lo borren".'],
         'quiz': {'p': 'Te llega por WhatsApp un vídeo "escandaloso". ¿Qué haces ANTES de compartir?', 'opciones': ['Lo reenvío rápido a mi grupo', 'Verifico que aparezca también en un medio serio (RTVE, El País, BBC)', 'Lo comparto solo a familia', 'Espero a ver si alguien lo borra'], 'correcta': 1,
                  'explica': 'Si no aparece en medios serios, casi seguro es bulo. Compartirlo te convierte en cómplice del bulo.'}},
        {'nombre': 'Las reacciones rápidas son el truco',
         'queEs': 'Tanto los bulos como el phishing dependen de que actúes RÁPIDO sin pensar. Si te piden compartir/pinchar/responder YA, casi siempre es trampa.',
         'ejemplo': {'tipo': 'peligroso', 'texto': '⚠️ "Comparte este vídeo en 24 horas o lo borrarán". "Tu cuenta se cierra si no verificas YA". La urgencia es la pista número 1 del engaño.'},
         'senales': ['Plazo corto ("en X horas", "antes de mañana").', 'Apelación emocional fuerte (miedo, rabia, codicia).', 'Pedido de compartir/pinchar inmediato.'],
         'quiz': {'p': 'Lo que tienen en común el phishing, los bulos y las estafas en redes es:', 'opciones': ['Llegan por email', 'Te meten prisa para que actúes sin pensar', 'Vienen de gente desconocida', 'Tienen errores de ortografía'], 'correcta': 1,
                  'explica': 'La URGENCIA es el truco número uno. La calma es tu defensa.'}},
        {'nombre': 'El silencio también es una opción',
         'queEs': 'No tienes que opinar de todo. No tienes que reaccionar a cada provocación. Pasar de un comentario tóxico es una habilidad: en internet, el SILENCIO es a veces la respuesta más fuerte.',
         'ejemplo': {'tipo': 'bueno', 'texto': '✅ Alguien te insulta en un comentario de TikTok. En vez de responder y enfadarte, lo BLOQUEAS y sigues con tu vida. Le quitas todo el poder.'},
         'senales': ['Responder a un trol le da más visibilidad y energía.', 'Bloquear/silenciar es siempre legítimo.', 'No tienes que justificar a nadie por qué bloqueas.'],
         'quiz': {'p': 'Un desconocido te deja un comentario insultante en TikTok. ¿Qué haces?', 'opciones': ['Le respondo con otro insulto', 'Lo bloqueo y sigo a lo mío', 'Pido a mis amigos que también le insulten', 'Borro mi cuenta'], 'correcta': 1,
                  'explica': 'Bloquear lo silencia para ti y le quita la atención que buscaba. Es la respuesta más eficaz.'}},
    ],
    'FRASES_VF': [
        {'texto': 'Lo que subes a internet con 12 años puede verlo todavía un futuro jefe cuando tengas 25.', 'correcta': True, 'explica': 'Verdadero. La huella digital persiste años. Por eso "compartir con cabeza" importa.'},
        {'texto': 'Si un bulo te lo manda un amigo de confianza, es seguro reenviarlo.', 'correcta': False, 'explica': 'Falso. Tu amigo puede haberse equivocado. Verifica TÚ la fuente antes de propagarlo.'},
        {'texto': 'La urgencia ("comparte AHORA antes de que lo borren") es la señal número 1 de bulo o estafa.', 'correcta': True, 'explica': 'Verdadero. La urgencia bloquea el pensamiento crítico. Es la trampa más usada.'},
        {'texto': 'Si te insultan en redes, lo MÁS eficaz es responder con otro insulto para defenderte.', 'correcta': False, 'explica': 'Falso. Responder alimenta al trol. Bloquear/silenciar es más eficaz.'},
        {'texto': 'Compartir algo que NO has verificado te convierte en cómplice de su difusión si resulta ser falso.', 'correcta': True, 'explica': 'Verdadero. Cuando compartes asumes parte de la responsabilidad.'},
        {'texto': 'Bloquear a alguien en redes requiere justificar por qué lo haces.', 'correcta': False, 'explica': 'Falso. Es tu derecho. No tienes que explicarte ante nadie.'},
    ],
}

# ── S6 · Misión Interland (parte 2) ─────────────────────────────
S6 = {
    'num': 6,
    'INSIGNIA_FINAL': 'Maestro de Interland',
    'INSIGNIA_NOMBRES': {'cadete': 'Cadete', 'analista': 'Aprendiz', 'investigador': 'Aventurero', 'detective': 'Maestro de Interland'},
    'FRASE_DIPLOMA': 'Ser amable en internet es ser fuerte en internet',
    'NOMBRE_ARCHIVO': 'S06-interland-p2',
    'html_vars': {
        'TITULO_CORTO': 'Misión Interland (parte 2)',
        'TITULO_NAV': 'Interland 2',
        'EMOJI': '🌍',
        'TITULO': 'Misión Interland · parte 2',
        'SUBTITULO': 'Última visita a Interland. Quedan 2 mundos: Kind Kingdom (amabilidad) y Tower of Treasure (contraseñas).',
        'INS_1': 'Cadete', 'INS_2': 'Aprendiz', 'INS_3': 'Aventurero', 'INS_FINAL_CORTO': 'Maestro',
        'LABEL_JUEGO': 'Interland',
        'TITULO_MISION': 'Vuelta a Interland',
        'GANCHO_EMOCIONAL': '<strong>🎮 Recuerda:</strong> en la S5 jugaste Mindful Mountain y Reality River. Hoy completas tu travesía con los 2 últimos mundos: <strong>Kind Kingdom</strong> (cómo combatir el ciberacoso) y <strong>Tower of Treasure</strong> (cómo proteger tus cuentas con buenas contraseñas).',
        'NARRATIVA': 'Cierras Interland con los 2 mundos finales. Después del informe, recibes la insignia de Maestro de Interland.',
        'OBJETIVO_HOY': 'Aprender los 2 últimos principios de Be Internet Awesome (Ser amable + Asegurar tus cuentas). Entrenar con 6 V/F. Jugar Kind Kingdom + Tower of Treasure. Cerrar la trilogía Interland.',
        'CHIP_RETO': '🎮 2 mundos · 25 min',
        'BOTON_INICIO': 'Volver a Interland',
        'TITULO_TEORIA': 'Los 2 principios que faltaban',
        'INTRO_TEORIA': 'Cerramos los 4 principios de Be Internet Awesome.',
        'TITULO_RETO': '🎮 Juega Kind Kingdom + Tower of Treasure',
        'INTRO_RETO': 'Vuelve a Interland y completa los 2 mundos que dejaste para hoy.',
        'ZONA_RETO': reto_launcher(
            '<p>Cierra los 2 mundos que faltan: amabilidad y contraseñas.</p>',
            [('🎮 Abrir Interland', 'https://beinternetawesome.withgoogle.com/es_es/interland')],
            '<li>Abre Interland desde el botón.</li>'
            '<li>Juega <strong>Kind Kingdom</strong> (cómo ser amable y combatir el ciberacoso). ~12 min.</li>'
            '<li>Vuelve al mapa y juega <strong>Tower of Treasure</strong> (cómo crear contraseñas fuertes). ~12 min.</li>'
            '<li>Cuando completes los 2, vuelve aquí y rellena el informe.</li>'
        ),
        'Q1': 'En Kind Kingdom enseñan a NO ser un trol. ¿Has visto/sufrido ciberacoso en redes? ¿Qué pasó?', 'Q1_AYUDA': 'Si no quieres dar detalles, di solo "sí" o "no" y qué aprendiste.',
        'Q2': 'En Tower of Treasure enseñan a crear contraseñas fuertes. Después de los juegos, ¿hay alguna contraseña tuya que pasaría las pruebas del juego? ¿Y cuál no?', 'Q2_AYUDA': 'No escribas la contraseña: solo si era fuerte o no, sin detalles.',
        'Q3': 'Has terminado Interland. ¿Qué 1 idea te llevas para SIEMPRE de los 4 mundos?', 'Q3_AYUDA': 'Una sola idea, la que más te ha marcado.',
        'TEXTO_DIPLOMA': 'por haber completado los 4 mundos de Interland y comprendido los 4 principios de Be Internet Awesome: comparte con cabeza, no caigas en la trampa, sé amable y asegura tus cuentas.',
        'PROXIMO_PASO': 'La Sesión 7 te lleva a auditar 5 perfiles de redes sociales y calcular su nivel de riesgo.',
        'NEXT_HREF': 's07.html', 'NEXT_LABEL': 'Sesión 7 · Perfil de riesgo',
    },
    'CONCEPTOS': [
        {'nombre': 'Principio 3 — Sé amable',
         'queEs': 'En internet hay troles, ciberacosadores, gente cruel. Tu mejor defensa NO es ser igual: es bloquear, denunciar, no responder, y no convertirte tú en uno de ellos.',
         'ejemplo': {'tipo': 'bueno', 'texto': '✅ Un compañero te insulta en un grupo. NO le respondes con otro insulto. Sales del grupo, lo bloqueas si insiste, y se lo cuentas a un adulto.'},
         'senales': ['Ser cruel desde un teclado es MÁS fácil que cara a cara (el "efecto desinhibición").',
                     'Un trol busca reacción: si no la das, pierde poder.',
                     'Si TÚ eres el agresor: nunca es "broma" si la otra persona no se ríe.'],
         'quiz': {'p': 'Un compañero de clase recibe burlas constantes en redes. ¿Qué haces TÚ?', 'opciones': ['Me río con los demás para no quedar mal', 'Le hablo en privado para apoyarlo y reporto las burlas en la red', 'Me callo y miro', 'Comparto las burlas'], 'correcta': 1,
                  'explica': 'No ser cómplice + apoyo en privado + reporte a la plataforma. Las víctimas necesitan UN aliado.'}},
        {'nombre': 'Principio 4 — Asegura tus cuentas',
         'queEs': 'Cada cuenta tuya merece una contraseña FUERTE y ÚNICA. Y el 2FA donde se pueda. Eso te protege contra el 95% de los hackeos.',
         'ejemplo': {'tipo': 'bueno', 'texto': '✅ En Instagram pones una frase de paso ("caballo-mesa-luna-puente-7") + activas el 2FA por SMS. Aunque te roben la contraseña, sin tu móvil no entran.'},
         'senales': ['Contraseña LARGA (15+ caracteres) es mejor que corta con símbolos.',
                     'CADA cuenta importante: contraseña ÚNICA.',
                     'Activa 2FA en email, banco, redes sociales.'],
         'quiz': {'p': 'La mejor defensa contra que te hackeen una cuenta es:', 'opciones': ['Cambiar de teléfono', 'Contraseña ÚNICA y FUERTE + 2FA', 'No usar internet', 'Tener antivirus caro'], 'correcta': 1,
                  'explica': 'Contraseña única + 2FA bloquean la mayoría de ataques. Sin esto, todo lo demás vale menos.'}},
        {'nombre': 'Denunciar también es responsabilidad',
         'queEs': 'Las plataformas (Insta, TikTok, YouTube) tienen botones de DENUNCIA. Úsalos. Si todos denunciamos lo tóxico, las plataformas lo retiran más rápido.',
         'ejemplo': {'tipo': 'bueno', 'texto': '✅ Ves un comentario racista o de acoso a alguien. En Instagram: 3 puntos → Denunciar → Acoso. Tarda 5 segundos y ayuda.'},
         'senales': ['Toda red social tiene botón de denuncia (los 3 puntos del post/comentario).',
                     'Las denuncias son anónimas: el agresor no sabe quién lo denunció.',
                     'Cuanta más gente denuncie un contenido, más rápido lo retira la plataforma.'],
         'quiz': {'p': 'Ves un comentario de acoso a un compañero en Instagram. ¿Qué haces?', 'opciones': ['Lo ignoro, no es asunto mío', 'Pulso los 3 puntos del comentario y lo denuncio por acoso', 'Lo comparto', 'Comento riéndome'], 'correcta': 1,
                  'explica': 'Denunciar es anónimo, rápido y útil. Si todos lo hacemos, las plataformas actúan.'}},
        {'nombre': 'Pedir ayuda NO es cobardía',
         'queEs': 'Si alguien te acosa, te chantajea, te amenaza o se te escapa de las manos: HABLA con un adulto de confianza (padres, profesores, INCIBE 017). Pedir ayuda es lo MÁS fuerte que puedes hacer.',
         'ejemplo': {'tipo': 'bueno', 'texto': '✅ Te chantajean con una foto. En vez de pagar o seguir respondiendo, HABLAS con tu padre/madre o llamas al 017 (línea de ayuda en ciberseguridad de INCIBE). Es gratuito y anónimo.'},
         'senales': ['Adultos de confianza: padres, profesor, orientador del cole, familia.',
                     'INCIBE 017: línea gratuita y anónima de ayuda en ciberseguridad.',
                     'Nunca pagues a un chantajista: aunque pagues, te volverá a pedir más.'],
         'quiz': {'p': 'Si recibes una amenaza o chantaje online, lo MEJOR es:', 'opciones': ['Pagar lo que piden', 'Responder con amenazas', 'Hablar con un adulto de confianza y/o llamar al 017 de INCIBE', 'Borrar la cuenta y no decir nada'], 'correcta': 2,
                  'explica': 'Pedir ayuda no es cobardía: es lo más inteligente. El 017 es gratis y anónimo.'}},
    ],
    'FRASES_VF': [
        {'texto': 'Responder a un trol con otro insulto le quita poder.', 'correcta': False, 'explica': 'Falso. Responder le da más visibilidad y satisfacción. Bloquear/denunciar es más eficaz.'},
        {'texto': 'Una contraseña LARGA con palabras corrientes es más fuerte que una corta con muchos símbolos raros.', 'correcta': True, 'explica': 'Verdadero. La longitud es el factor más importante.'},
        {'texto': 'Las denuncias en redes sociales son anónimas: el agresor no sabe quién le denunció.', 'correcta': True, 'explica': 'Verdadero. Denunciar es seguro para ti.'},
        {'texto': 'Si te chantajean online, pagar es la forma más rápida de quitárselo de encima.', 'correcta': False, 'explica': 'Falso. Si pagas, te volverán a pedir más. Habla con un adulto y/o llama al 017 (INCIBE).'},
        {'texto': 'El 017 es una línea GRATUITA y ANÓNIMA de INCIBE para ayuda en ciberseguridad.', 'correcta': True, 'explica': 'Verdadero. Atienden en español, 9-21h. Y NO te van a juzgar.'},
        {'texto': 'Si un compañero sufre ciberacoso, lo mejor es callarse para no meterse en líos.', 'correcta': False, 'explica': 'Falso. Las víctimas necesitan aliados. Apoyo en privado + reportar las burlas + hablar con un profesor.'},
    ],
}


# ── S7 · Perfil de riesgo en redes ──────────────────────────────
S7 = {
    'num': 7,
    'INSIGNIA_FINAL': 'Auditor de Perfiles',
    'INSIGNIA_NOMBRES': {'cadete': 'Cadete', 'analista': 'Analista', 'investigador': 'Auditor Junior', 'detective': 'Auditor de Perfiles'},
    'FRASE_DIPLOMA': 'Tu perfil dice más de ti que tú mismo. Asegúrate de que dice lo justo',
    'NOMBRE_ARCHIVO': 'S07-perfil-riesgo',
    'html_vars': {
        'TITULO_CORTO': 'Perfil de riesgo en redes',
        'TITULO_NAV': 'Perfil riesgo',
        'EMOJI': '📊',
        'TITULO': 'Perfil de riesgo en redes',
        'SUBTITULO': 'Te paso 5 perfiles ficticios de Instagram. Tú calculas el nivel de riesgo de cada uno: BAJO / MEDIO / ALTO.',
        'INS_1': 'Cadete', 'INS_2': 'Analista', 'INS_3': 'Auditor Junior', 'INS_FINAL_CORTO': 'Auditor',
        'LABEL_JUEGO': 'Auditoría',
        'TITULO_MISION': 'Auditoría de 5 perfiles',
        'GANCHO_EMOCIONAL': '<strong>📊 Imagínate esto:</strong> tu hermana pequeña abre Instagram por primera vez. Antes de dejarle, ¿sabrías mirarle el perfil y decirle "esto está bien, esto NO"? Hoy aprendes a hacerlo.',
        'NARRATIVA': 'Te paso <strong>5 perfiles ficticios</strong>. Para cada uno verás: foto de perfil, bio, configuración (público/privado), publicaciones típicas, etiquetas. Tu trabajo: aplicar la checklist de seguridad y asignar nivel de riesgo. BAJO, MEDIO o ALTO.',
        'OBJETIVO_HOY': 'Aprender los 5 indicadores clave de riesgo en un perfil. Entrenar con 6 V/F. Auditar 5 perfiles ficticios calculando su nivel de riesgo y explicando por qué.',
        'CHIP_RETO': '📊 5 perfiles a auditar',
        'BOTON_INICIO': 'Empezar auditoría',
        'TITULO_TEORIA': 'Los 5 indicadores de un perfil de riesgo',
        'INTRO_TEORIA': '¿Qué hace que un perfil sea de RIESGO ALTO? No es UN solo factor: es la combinación.',
        'TITULO_RETO': '📊 Audita los 5 perfiles',
        'INTRO_RETO': 'Para cada uno de los 5 perfiles, lee la info, marca el nivel de riesgo y verás si has acertado.',
        'ZONA_RETO': reto_galeria('<strong>Para cada perfil:</strong> léelo entero, decide BAJO/MEDIO/ALTO y pulsa. Verás el análisis correcto.', 'zona-perfiles'),
        'Q1': 'De los 5 perfiles auditados, ¿cuál te ha sorprendido MÁS por su nivel de riesgo? ¿Por qué?', 'Q1_AYUDA': 'Identifica el perfil concreto y qué dato lo hacía vulnerable.',
        'Q2': 'Mira mentalmente TU PROPIO perfil de Instagram (o TikTok). ¿Qué nivel de riesgo te pondrías? ¿Por qué?', 'Q2_AYUDA': 'Sé honesto. Sólo tú lo lees.',
        'Q3': '¿Qué 2 cambios concretos vas a hacer ESTA semana en tu perfil para bajar tu nivel de riesgo?', 'Q3_AYUDA': 'Ejemplos: "poner cuenta privada", "quitar el cole de la bio", "borrar fotos con el escudo del IES"…',
        'TEXTO_DIPLOMA': 'por haber auditado 5 perfiles de redes sociales aplicando los 5 indicadores de riesgo y reflexionado honestamente sobre la propia exposición digital.',
        'PROXIMO_PASO': 'La Sesión 8 te lleva a resolver el Escape Room oficial del CCN-CERT.',
        'NEXT_HREF': 's08.html', 'NEXT_LABEL': 'Sesión 8 · Escape CCN',
    },
    'CONCEPTOS': [
        {'nombre': 'Indicador 1 — Cuenta pública vs privada',
         'queEs': 'Una cuenta PÚBLICA cualquiera puede verla. Una PRIVADA solo tus seguidores aprobados. Es la decisión número 1 que define tu riesgo.',
         'ejemplo': {'tipo': 'peligroso', 'texto': '⚠️ Cuenta de Instagram pública de una chica de 14 años, con 8 publicaciones de "estoy SOLA en casa este finde". Cualquiera del mundo puede verlas. Riesgo ALTO.'},
         'senales': ['Pública = el mundo entero la puede ver, incluidos desconocidos.', 'Privada = solo seguidores aprobados por ti.', 'Lo demás (bio, fotos) importa MUCHO más en una cuenta pública.'],
         'quiz': {'p': '¿Cuándo tiene sentido tener Instagram PÚBLICO?', 'opciones': ['Para tener más seguidores', 'Si eres un negocio, marca o profesional que quiere visibilidad', 'Para que te encuentren tus amigos', 'Siempre'], 'correcta': 1,
                  'explica': 'Para particulares (sobre todo menores), PRIVADA es lo seguro. Pública solo si eres una marca o creador profesional.'}},
        {'nombre': 'Indicador 2 — Datos personales en la bio',
         'queEs': 'La bio que dice "Lucía · 13 · Granada · IES Lorca · 1ºESO B" es un manual para acosadores: edad, ciudad, instituto, clase. TODO ahí.',
         'ejemplo': {'tipo': 'peligroso', 'texto': '⚠️ Bio típica de menor: nombre real + edad + ciudad + colegio. Riesgo ALTO. Cualquiera puede ir a la puerta del colegio a buscarte.'},
         'senales': ['Nombre real + edad + ciudad = perfil identificable.', 'Mencionar el instituto/clase es exponerse a desconocidos.', 'Iniciales o apodo es más seguro que nombre real.'],
         'quiz': {'p': '¿Cuál de estas bios es MENOS arriesgada para una chica de 13 años?', 'opciones': ['"Lucía García · 13 años · Granada · IES Lorca 1ºB"', '"L. · K-pop fan · 📍 Andalucía"', '"Lucía 2012 · cumpleañera el 12 de marzo"', '"Lucía García López"'], 'correcta': 1,
                  'explica': 'Iniciales + interés general + ubicación amplia. Sin nombre completo, sin edad, sin colegio.'}},
        {'nombre': 'Indicador 3 — Geolocalización y rutinas',
         'queEs': 'Publicar la ubicación de tus posts o subir siempre desde el mismo sitio a la misma hora REVELA tu rutina. Y la rutina es lo más útil para alguien que quiera encontrarte.',
         'ejemplo': {'tipo': 'peligroso', 'texto': '⚠️ Subes una foto cada miércoles a las 18:00 desde el mismo centro comercial, con ubicación etiquetada. Riesgo ALTO: cualquiera sabe dónde estarás el próximo miércoles.'},
         'senales': ['Ubicación etiquetada en CADA post → rutina mapeable.', 'Mismo lugar + misma hora en muchos posts.', 'Casa, instituto, gimnasio… las 3 ubicaciones MÁS sensibles.'],
         'quiz': {'p': '¿Qué tipo de ubicación NUNCA deberías etiquetar en tus posts?', 'opciones': ['Un monumento turístico al que vas de visita', 'Tu casa, tu instituto, tu gimnasio (sitios que frecuentas)', 'Un restaurante donde fuiste una vez', 'Un país al que viajas'], 'correcta': 1,
                  'explica': 'Los sitios donde estás repetidamente. Etiquetar un sitio turístico puntual no es lo mismo que etiquetar tu casa.'}},
        {'nombre': 'Indicador 4 — Etiquetas y conexiones',
         'queEs': 'Aunque tu cuenta sea privada, las personas a las que etiquetas (con cuenta pública) pueden hacer visible tu información. Tu privacidad depende también de la de tus amigos.',
         'ejemplo': {'tipo': 'peligroso', 'texto': '⚠️ Tu cuenta es privada, pero etiquetas a tu novio Diego (cuenta pública) en una foto. La foto sale en el feed de Diego → cualquiera la puede ver y saber que estáis juntos.'},
         'senales': ['Etiquetar a cuentas públicas hace VISIBLE tu contenido.', 'Hashtags muy específicos (#IESLorca, #1ESOB) reúnen contenido de tu grupo.', 'Etiquetar a familia menor de edad puede comprometerla.'],
         'quiz': {'p': 'Si tu cuenta es PRIVADA pero etiquetas a tu mejor amiga que tiene cuenta PÚBLICA, ¿qué pasa con la foto?', 'opciones': ['Sigue solo en tu privado', 'Aparece también en el feed PÚBLICO de tu amiga, visible para todos', 'Desaparece', 'Se hace privada para los dos'], 'correcta': 1,
                  'explica': 'La etiqueta lleva la foto al feed del etiquetado. Si esa cuenta es pública, tu foto se hace pública aunque tu cuenta no lo sea.'}},
        {'nombre': 'Indicador 5 — Contraseñas y 2FA de la cuenta',
         'queEs': 'Da igual lo bien que cuides la apariencia: si tu contraseña es débil o no tienes 2FA, te pueden hackear y desde dentro el atacante hace lo que quiera con tu perfil.',
         'ejemplo': {'tipo': 'bueno', 'texto': '✅ Tu cuenta tiene contraseña larga ÚNICA + 2FA por SMS activado. Aunque te roben la contraseña, sin tu móvil no entran.'},
         'senales': ['Contraseña fuerte (15+ caracteres) y ÚNICA de esa cuenta.', '2FA activado (SMS, app autenticadora o huella).', 'Revisión periódica de dispositivos conectados en "ajustes de seguridad".'],
         'quiz': {'p': 'Tienes Instagram con cuenta privada, bio limpia, sin geolocalización… pero contraseña "lucia2012" y SIN 2FA. ¿Es seguro?', 'opciones': ['Sí, la cuenta privada lo protege todo', 'No: si te hackean la contraseña, todo lo demás no sirve', 'Solo medianamente', 'Da igual'], 'correcta': 1,
                  'explica': 'La privacidad de la cuenta solo importa si la cuenta NO está hackeada. Contraseña + 2FA son el cimiento.'}},
    ],
    'FRASES_VF': [
        {'texto': 'Tener Instagram público multiplica el riesgo, sobre todo en menores.', 'correcta': True, 'explica': 'Verdadero. Las cuentas públicas exponen tu contenido al mundo entero, incluyendo desconocidos.'},
        {'texto': 'Si tu cuenta es privada, ya estás 100% protegido aunque etiquetes a amigos con cuenta pública.', 'correcta': False, 'explica': 'Falso. Si etiquetas a alguien de cuenta pública, tu foto aparece en su feed visible.'},
        {'texto': 'Poner en la bio "1ºESO B del IES Lorca" facilita a un acosador encontrarte físicamente.', 'correcta': True, 'explica': 'Verdadero. Dar tu instituto + clase es dar tu ubicación cada día de la semana.'},
        {'texto': 'Etiquetar la ubicación REAL de tus posts no es peligroso si lo haces solo de vez en cuando.', 'correcta': False, 'explica': 'Falso. Una sola ubicación de tu casa o instituto ya basta para localizarte.'},
        {'texto': 'El 2FA en Instagram se activa en menos de 1 minuto y bloquea el 95% de los intentos de hackeo.', 'correcta': True, 'explica': 'Verdadero. Está en Ajustes → Seguridad. Tarda menos que verse un TikTok.'},
        {'texto': 'Una cuenta es totalmente segura si tiene buena contraseña, aunque sea pública y publique la dirección de casa.', 'correcta': False, 'explica': 'Falso. La seguridad de la cuenta NO te protege de lo que publicas voluntariamente.'},
    ],
    'JS_EXTRA': '''
// 5 perfiles ficticios para auditar
const PERFILES = [
  { nombre: '@LuciaGarcia2012', riesgo: 'ALTO',
    info: 'Cuenta pública. Bio: "Lucía García · 13 · IES Lorca 1ºB · K-pop fan ❤️". 200 fotos: instituto, casa, parque (con geo). Etiqueta a su novio cada semana. Contraseña: lucia2012.',
    explica: 'Riesgo ALTO. Pública + nombre real + edad + instituto + clase + geolocalización + contraseña obvia. Casi todos los indicadores en rojo.' },
  { nombre: '@solofotos.gatos', riesgo: 'BAJO',
    info: 'Cuenta privada. Bio: "Mis gatos 🐱". Solo fotos de mascotas. Sin etiquetas a personas. Solo 30 seguidores conocidos. Contraseña fuerte + 2FA.',
    explica: 'Riesgo BAJO. Privada + sin datos personales + temática neutra + contraseña fuerte + 2FA.' },
  { nombre: '@manu_skater_gr', riesgo: 'MEDIO',
    info: 'Cuenta pública. Bio: "Manu · 14 · Skater 🛹 Granada". 80 fotos de skate en distintos parques de Granada, algunas con geo. NO menciona instituto. Contraseña: skate-7-rambla.',
    explica: 'Riesgo MEDIO. Pública + nombre y edad reales + ciudad. PERO no instituto + sin etiquetas problemáticas + contraseña razonable. Bajaría a riesgo BAJO si la pusiera privada.' },
  { nombre: '@anita.viajera.eu', riesgo: 'BAJO',
    info: 'Cuenta privada. Bio: "✈️ Trips · 📷 Film". Fotos de paisajes europeos, sin gente en primer plano. Contraseña fuerte, 2FA activo, dispositivos conectados revisados.',
    explica: 'Riesgo BAJO. Privada + foto temática (paisajes, no rostros) + sin datos identificativos + seguridad completa.' },
  { nombre: '@PabloMartinez_BBVA', riesgo: 'ALTO',
    info: 'Cuenta pública. Bio: "Pablo Martínez · BBVA Granada · Director de Oficina · 📧 pmartinez@bbva.es". Etiqueta sus oficinas, comparte capturas internas. Contraseña reutilizada en LinkedIn.',
    explica: 'Riesgo ALTO. Pública + datos profesionales identificables + email del trabajo expuesto + contenido interno (capturas de oficina) + reutilización de contraseñas. Candidato típico a phishing dirigido.' },
];

let perfilesAuditados = 0;
function renderPerfiles() {
  const cont = document.getElementById('zona-perfiles');
  cont.innerHTML = PERFILES.map(function(p, i) {
    return '<div class="situacion" data-idx="' + i + '">' +
      '<span class="num-situacion">PERFIL ' + (i+1) + ' / 5</span>' +
      '<div class="texto-situacion"><strong>' + p.nombre + '</strong><br>' + p.info + '</div>' +
      '<div class="opciones-sit" id="opc-perfil-' + i + '">' +
        '<button onclick="responderPerfil(' + i + ',\\'BAJO\\')">🟢 BAJO</button>' +
        '<button onclick="responderPerfil(' + i + ',\\'MEDIO\\')">🟡 MEDIO</button>' +
        '<button onclick="responderPerfil(' + i + ',\\'ALTO\\')">🔴 ALTO</button>' +
      '</div>' +
      '<div class="explica-sit" id="exp-perfil-' + i + '"></div>' +
    '</div>';
  }).join('');
}
const perfilesContestados = new Set();
function responderPerfil(idx, eleccion) {
  if (perfilesContestados.has(idx)) return;
  perfilesContestados.add(idx);
  const p = PERFILES[idx];
  const acertado = (eleccion === p.riesgo);
  const botones = document.querySelectorAll('#opc-perfil-' + idx + ' button');
  botones.forEach(function(b) {
    b.disabled = true;
    if (b.textContent.includes(p.riesgo)) b.classList.add('correcta');
    else if (b.textContent.includes(eleccion) && !acertado) b.classList.add('incorrecta');
  });
  const exp = document.getElementById('exp-perfil-' + idx);
  exp.innerHTML = (acertado ? '✅ Correcto. ' : '❌ Era ' + p.riesgo + '. ') + p.explica;
  exp.dataset.activo = 'true';
  perfilesAuditados++;
  if (perfilesAuditados >= PERFILES.length) {
    document.getElementById('confirma-galeria').style.display = 'flex';
  }
}
// Hook initSesion para incluir renderPerfiles
const _initOriginal = typeof initSesion === 'function' ? initSesion : null;
function initSesion() { if (_initOriginal) _initOriginal(); renderPerfiles(); }
'''
}

# ── S8 · Escape Room CCN-CERT ───────────────────────────────────
S8 = {
    'num': 8,
    'INSIGNIA_FINAL': 'Cadete CCN-CERT',
    'INSIGNIA_NOMBRES': {'cadete': 'Cadete', 'analista': 'Aprendiz', 'investigador': 'Operador', 'detective': 'Cadete CCN-CERT'},
    'FRASE_DIPLOMA': 'El mejor entrenamiento es el que viene de profesionales que defienden a un país',
    'NOMBRE_ARCHIVO': 'S08-escape-ccn',
    'html_vars': {
        'TITULO_CORTO': 'Escape Room CCN-CERT',
        'TITULO_NAV': 'Escape CCN',
        'EMOJI': '🔐',
        'TITULO': 'Escape Room CCN-CERT',
        'SUBTITULO': 'Es el escape room oficial del Centro Criptológico Nacional. Hoy lo resuelves tú.',
        'INS_1': 'Cadete', 'INS_2': 'Aprendiz', 'INS_3': 'Operador', 'INS_FINAL_CORTO': 'CCN',
        'LABEL_JUEGO': 'Escape CCN',
        'TITULO_MISION': 'Misión: salir del escape room del CCN',
        'GANCHO_EMOCIONAL': '<strong>🛡️ Esto es real:</strong> el <strong>CCN-CERT</strong> es el equipo que protege la ciberseguridad de las administraciones públicas de España. El mismo que defiende ministerios y embajadas. Han hecho un escape room para que aprendas con sus retos. Hoy lo juegas tú.',
        'NARRATIVA': 'El Escape Room "Ángeles del CCN" mezcla 5 retos de ciberseguridad: contraseñas, phishing, malware, redes WiFi y privacidad. Tarda unos 25-30 minutos. Al terminar te dan un diploma oficial.',
        'OBJETIVO_HOY': 'Repasar los 4 conceptos clave del CCN (CCN-CERT, ciberataque, ciberresiliencia, INCIBE). Entrenar con 6 V/F. Resolver el escape room oficial del CCN-CERT. Subir tu diploma a la entrega.',
        'CHIP_RETO': '🔐 Escape · 25-30 min',
        'BOTON_INICIO': 'Activar misión CCN',
        'TITULO_TEORIA': '4 cosas sobre el CCN y los profesionales que protegen España',
        'INTRO_TEORIA': 'Antes de entrar al escape, conoce a quien te entrena.',
        'TITULO_RETO': '🔐 Resuelve el Escape Room',
        'INTRO_RETO': 'Abre el escape room del CCN-CERT en pestaña nueva y resuelve los 5 retos. Tarda unos 25-30 minutos.',
        'ZONA_RETO': reto_launcher(
            '<p>Es un escape room oficial del <strong>Centro Criptológico Nacional</strong> (CCN-CERT). Es el organismo que protege la ciberseguridad de las administraciones del Estado español. Tu reto: salir.</p>',
            [('🔐 Abrir Escape Room CCN', 'https://www.ccn-cert.cni.es/comunicacion-eventos/eventos/escape-room.html')],
            '<li>Pulsa el botón para abrir el escape room oficial del CCN.</li>'
            '<li>Si pide nombre/email, usa un email tuyo válido para recibir el diploma.</li>'
            '<li>Resuelve los 5 retos (contraseñas, phishing, malware, WiFi, privacidad). Tarda 25-30 min.</li>'
            '<li>Al terminar, descarga el diploma que te envía el CCN.</li>'
            '<li>Vuelve aquí y rellena el informe.</li>'
        ),
        'Q1': '¿Cuál de los 5 retos del escape room te ha gustado MÁS? ¿Por qué?', 'Q1_AYUDA': 'Identifica el reto y qué te enseñó.',
        'Q2': '¿Qué reto del escape room te ha costado MÁS? ¿Cómo lo resolviste al final?', 'Q2_AYUDA': 'Describe la dificultad y cómo la superaste.',
        'Q3': 'Conociendo ahora el CCN-CERT y sus retos, ¿qué crees que diferencia a un buen ciberanalista de uno mediocre?', 'Q3_AYUDA': 'Una idea concreta: paciencia, observación, no actuar sin pensar, etc.',
        'TEXTO_DIPLOMA': 'por haber completado el Escape Room oficial del CCN-CERT y comprendido cómo trabajan los equipos profesionales que protegen las administraciones públicas de España.',
        'PROXIMO_PASO': 'La Sesión 9 te lleva al Escape Room PIENSA (ingeniería social) que ya está en el sitio.',
        'NEXT_HREF': 's09.html', 'NEXT_LABEL': 'Sesión 9 · Ingeniería social',
    },
    'CONCEPTOS': [
        {'nombre': 'CCN-CERT — el equipo que protege España',
         'queEs': 'El CCN-CERT es la "Unidad de Respuesta a Incidentes" del Centro Criptológico Nacional. Es decir: el equipo de élite que defiende las administraciones públicas españolas (ministerios, embajadas, agencias) de ciberataques.',
         'ejemplo': {'tipo': 'bueno', 'texto': '✅ Si un ministerio español sufre un ataque, el CCN-CERT entra a investigar y a defender. Son los "bomberos" de la ciberseguridad estatal.'},
         'senales': ['Depende del Centro Nacional de Inteligencia (CNI).', 'Coordina la respuesta a ciberincidentes graves.', 'Publica guías y formación abierta para todos (como este escape room).'],
         'quiz': {'p': '¿De qué se encarga principalmente el CCN-CERT?', 'opciones': ['Vender antivirus', 'Defender las administraciones públicas españolas de ciberataques', 'Hacer videojuegos', 'Investigar phishings en bancos privados'], 'correcta': 1,
                  'explica': 'Son la unidad pública de respuesta a incidentes de ciberseguridad del Estado.'}},
        {'nombre': 'Ciberataque vs ciberincidente',
         'queEs': 'CIBERATAQUE: alguien intenta dañar/robar a propósito. CIBERINCIDENTE: cualquier evento de seguridad (puede ser un ataque, un error, una fuga…).',
         'ejemplo': {'tipo': 'peligroso', 'texto': '⚠️ Hackeo deliberado a un ministerio → ciberataque (y también incidente). Empleado que pierde un USB con datos → incidente (no ataque).'},
         'senales': ['Ataque = intención maliciosa.', 'Incidente = cualquier suceso de seguridad relevante.', 'Todo ataque es un incidente, pero no todo incidente es un ataque.'],
         'quiz': {'p': 'Un empleado del ministerio pierde un USB con documentos en la calle. ¿Qué es?', 'opciones': ['Ciberataque', 'Ciberincidente (no es ataque pero sí afecta a la seguridad)', 'No es nada', 'Cibercrimen organizado'], 'correcta': 1,
                  'explica': 'Es un incidente de seguridad (fuga accidental), no un ataque dirigido. El CCN-CERT también gestiona estos casos.'}},
        {'nombre': 'Ciberresiliencia: caer y levantarse',
         'queEs': 'No se trata solo de NUNCA caer (imposible). Se trata de PODER LEVANTARSE rápido y aprender. La ciberresiliencia es la capacidad de seguir funcionando incluso bajo ataque y recuperarse después.',
         'ejemplo': {'tipo': 'bueno', 'texto': '✅ Un hospital sufre ransomware. Pero TIENE BACKUPS recientes y un plan de actuación. En 8 horas restauran todo y siguen atendiendo. Eso es ciberresiliencia.'},
         'senales': ['Hacer copias de seguridad regulares (backups).', 'Tener un plan de actuación ANTES de la crisis.', 'Practicar simulacros de ciberincidente.'],
         'quiz': {'p': '¿Qué es ciberresiliencia?', 'opciones': ['Ser invulnerable a los ataques', 'La capacidad de seguir funcionando bajo ataque y recuperarse rápido', 'Tener el antivirus más caro', 'Cambiar siempre de empresa'], 'correcta': 1,
                  'explica': 'No se trata de evitar todos los ataques (imposible). Se trata de aguantar y levantarse rápido.'}},
        {'nombre': 'INCIBE — para empresas y ciudadanos',
         'queEs': 'INCIBE es el "primo" del CCN para empresas privadas y ciudadanos. Tiene una línea gratuita: 017. Tienen guías para todo y ayudan en casos de ciberacoso, fraude, sextorsión, etc.',
         'ejemplo': {'tipo': 'bueno', 'texto': '✅ Te chantajean por internet. Llamas al 017 (gratis, anónimo). Te asesoran qué hacer paso a paso. Sin juzgarte.'},
         'senales': ['INCIBE = Instituto Nacional de Ciberseguridad.', 'Línea 017: gratuita, anónima, 9-21h.', 'Web incibe.es con guías para padres, menores, empresas, etc.'],
         'quiz': {'p': 'Te están chantajeando por internet con fotos. ¿Qué número llamas?', 'opciones': ['112 (emergencias)', '017 (línea INCIBE de ayuda en ciberseguridad)', '060 (administración)', '091 (policía)'], 'correcta': 1,
                  'explica': 'El 017 de INCIBE: gratis, anónimo, especializado. Pueden ayudarte a denunciar y a protegerte. Si hay delito grave, ELLOS te ayudan a llegar a la policía.'}},
    ],
    'FRASES_VF': [
        {'texto': 'El CCN-CERT es un organismo público español que protege las administraciones del Estado de ciberataques.', 'correcta': True, 'explica': 'Verdadero. Es la unidad de respuesta del Centro Criptológico Nacional.'},
        {'texto': 'Todo ciberincidente es siempre un ciberataque deliberado.', 'correcta': False, 'explica': 'Falso. Un incidente puede ser también un error humano, un fallo técnico, una fuga accidental.'},
        {'texto': 'Tener backups regulares es una de las claves de la ciberresiliencia.', 'correcta': True, 'explica': 'Verdadero. Sin backups, un ransomware te puede destruir. Con backups recientes, te recuperas.'},
        {'texto': 'INCIBE (017) solo atiende a grandes empresas, no a ciudadanos particulares.', 'correcta': False, 'explica': 'Falso. El 017 está pensado también para particulares (especialmente jóvenes y mayores).'},
        {'texto': 'La ciberseguridad perfecta existe: con suficiente dinero, ninguna empresa es vulnerable.', 'correcta': False, 'explica': 'Falso. NO existe seguridad 100%. Por eso importa la ciberresiliencia: aguantar y recuperarse.'},
        {'texto': 'El CCN publica formación abierta y gratuita (como este escape room) porque la seguridad de todos beneficia a todos.', 'correcta': True, 'explica': 'Verdadero. Su misión incluye divulgar buenas prácticas a la sociedad.'},
    ],
}

# ── S10 · WhatsApp bajo sospecha ────────────────────────────────
S10 = {
    'num': 10,
    'INSIGNIA_FINAL': 'Inspector de Mensajería',
    'INSIGNIA_NOMBRES': {'cadete': 'Cadete', 'analista': 'Analista', 'investigador': 'Inspector Junior', 'detective': 'Inspector de Mensajería'},
    'FRASE_DIPLOMA': 'En WhatsApp, lo que parece de un amigo a veces es de un estafador',
    'NOMBRE_ARCHIVO': 'S10-whatsapp',
    'html_vars': {
        'TITULO_CORTO': 'WhatsApp bajo sospecha',
        'TITULO_NAV': 'WhatsApp',
        'EMOJI': '💬',
        'TITULO': 'WhatsApp bajo sospecha',
        'SUBTITULO': 'Tienes 8 capturas de WhatsApp. Tu trabajo: decidir si cada una es SEGURA, SOSPECHOSA o ESTAFA.',
        'INS_1': 'Cadete', 'INS_2': 'Analista', 'INS_3': 'Inspector Junior', 'INS_FINAL_CORTO': 'Inspector',
        'LABEL_JUEGO': 'Inspector',
        'TITULO_MISION': 'Analiza 8 conversaciones de WhatsApp',
        'GANCHO_EMOCIONAL': '<strong>💬 Imagínate esto:</strong> tu abuela recibe un WhatsApp: "Hola hijo, es mi nuevo número, ¿me haces un Bizum?". Le contesta. Pierde 800€. <strong>¿Habrías sabido detectarlo?</strong> Hoy entrenas el ojo: 8 capturas reales, tú decides.',
        'NARRATIVA': 'Recibes <strong>8 capturas de WhatsApp</strong>. Algunas son normales. Otras tienen señales clarísimas de fraude. Y otras son AMBIGUAS, como en la vida real. Para cada una decides: <strong>SEGURO · SOSPECHOSO · ESTAFA</strong>.',
        'OBJETIVO_HOY': 'Aprender las 5 señales de un WhatsApp fraudulento. Entrenar con 6 V/F. Analizar 8 capturas y emitir veredicto. Aprender a explicar por qué te ha hecho dudar.',
        'CHIP_RETO': '💬 8 capturas',
        'BOTON_INICIO': 'Empezar análisis',
        'TITULO_TEORIA': '5 señales de un WhatsApp fraudulento',
        'INTRO_TEORIA': 'WhatsApp es el canal favorito de los estafadores en España. Aprende a reconocer las pistas.',
        'TITULO_RETO': '💬 8 capturas para analizar',
        'INTRO_RETO': 'Lee cada captura, decide y verás la explicación.',
        'ZONA_RETO': reto_galeria('<strong>Para cada captura:</strong> lee, decide SEGURO/SOSPECHOSO/ESTAFA, y verás el análisis.', 'zona-mensajes'),
        'Q1': 'De las 8 capturas, ¿cuál te ha hecho dudar MÁS entre seguro y sospechoso? ¿Por qué?', 'Q1_AYUDA': 'Identifica la captura más ambigua y explica qué te confundía.',
        'Q2': '¿Has recibido tú (o alguien de tu familia) alguna vez un WhatsApp parecido a los de la práctica? ¿Qué pasó?', 'Q2_AYUDA': 'Si no, di "no" y por qué crees que no has caído.',
        'Q3': 'Si tu abuelo te enseña un WhatsApp sospechoso, ¿qué le dirías PASO A PASO antes de que conteste?', 'Q3_AYUDA': 'Sé concreto: "No contestes. Llama TÚ al número de SIEMPRE. No mandes dinero. Si es estafa, denuncia al 017".',
        'TEXTO_DIPLOMA': 'por haber analizado 8 conversaciones de WhatsApp y aprendido a distinguir entre mensajes legítimos, sospechosos y fraudulentos, protegiendo así a su familia.',
        'PROXIMO_PASO': 'La Sesión 11 te lleva al café trampa: cuidado con las wifis públicas.',
        'NEXT_HREF': 's11.html', 'NEXT_LABEL': 'Sesión 11 · Wifi café',
    },
    'CONCEPTOS': [
        {'nombre': 'Señal 1 — Número desconocido pidiendo dinero o datos',
         'queEs': 'Si te llega un mensaje de un número que no tienes en la agenda diciendo "soy fulanito" y pidiendo cualquier cosa, sospecha SIEMPRE. Los estafadores se hacen pasar por hijos, sobrinos, jefes…',
         'ejemplo': {'tipo': 'peligroso', 'texto': '⚠️ "Hola mamá, este es mi nuevo número (perdí el móvil), ¿me puedes hacer un Bizum urgente de 300€?". Estafa clásica de "hijo en apuros". En España, miles de víctimas al mes.'},
         'senales': ['Número que NO tienes en agenda.', 'Se hace pasar por familiar/amigo cercano.', 'Pide dinero/datos con urgencia (Bizum, transferencia, código de un SMS).'],
         'quiz': {'p': 'Te llega de un número desconocido: "Mamá, perdí el móvil, este es mi nuevo número, mándame 200€ por Bizum". ¿Qué haces?', 'opciones': ['Mando el dinero, mi hijo me necesita', 'Llamo TÚ al número HABITUAL de mi hijo para verificar antes de hacer nada', 'Respondo pidiendo más datos', 'Bloqueo sin hacer nada más'], 'correcta': 1,
                  'explica': 'Verificación cruzada: llama al número de SIEMPRE de tu hijo por el canal de SIEMPRE. La estafa se desmonta en 30 segundos.'}},
        {'nombre': 'Señal 2 — Enlaces sospechosos',
         'queEs': 'Cualquier enlace en WhatsApp puede llevar a una web falsa. Las marcas reales NO suelen mandar enlaces por WhatsApp para verificar cuentas o reclamar premios.',
         'ejemplo': {'tipo': 'peligroso', 'texto': '⚠️ "Has ganado un iPhone 15 por ser nuestro cliente número 1000000 🎉 Recógelo aquí: bit.ly/premio-apple". 100% estafa. Apple no funciona así.'},
         'senales': ['URLs acortadas (bit.ly, tinyurl) que ocultan el dominio real.', 'Promesas exageradas (premios, descuentos imposibles).', 'Urgencia: "tienes que pinchar antes de 24h".'],
         'quiz': {'p': 'Te llega por WhatsApp: "🎁 Has ganado 5000€ de Amazon, pincha aquí: bit.ly/regalo-am". ¿Qué haces?', 'opciones': ['Pincho rápido antes de que se acabe', 'Lo borro y bloqueo. Es estafa segura', 'Reenvío a mi grupo para que ganen ellos también', 'Le contesto pidiendo más info'], 'correcta': 1,
                  'explica': 'Premios imposibles + URL acortada + urgencia = estafa segura. Nunca pinches, nunca reenvíes.'}},
        {'nombre': 'Señal 3 — Pedir códigos de verificación',
         'queEs': 'Si alguien te pide el código de SMS que has recibido (de WhatsApp, banco, Insta…), es un INTENTO DE HACKEAR TU CUENTA. Los códigos son SOLO para ti.',
         'ejemplo': {'tipo': 'peligroso', 'texto': '⚠️ "Hola, soy del soporte de WhatsApp. Acabamos de mandarte un SMS con un código de 6 dígitos. Pásamelo, por favor". JAMÁS. Quieren robarte WhatsApp.'},
         'senales': ['Te piden el código de un SMS que has recibido.', 'Se hacen pasar por soporte de la app o servicio.', 'Si das el código → te roban la cuenta inmediatamente.'],
         'quiz': {'p': 'Alguien por WhatsApp te dice: "soy del soporte de WhatsApp, dame el código de 6 dígitos que te ha llegado". ¿Qué haces?', 'opciones': ['Se lo doy, parece oficial', 'NUNCA doy códigos a nadie. Los códigos son SOLO para mí', 'Solo si pone que es urgente', 'Lo pregunto a mis amigos primero'], 'correcta': 1,
                  'explica': 'Los códigos NUNCA se dan a nadie. WhatsApp, bancos y servicios JAMÁS te los piden por mensaje o llamada.'}},
        {'nombre': 'Señal 4 — Cuentas verificadas y "soporte"',
         'queEs': 'WhatsApp NO tiene un canal de soporte que te escriba directamente. Las cuentas REALES de empresas (Amazon, banco) en WhatsApp Business tienen un check verde. SIN ese check, sospecha.',
         'ejemplo': {'tipo': 'peligroso', 'texto': '⚠️ Te escribe "Soporte BBVA Oficial" sin check verde. Es FALSO. El BBVA real tiene check verde o no te escribe por WhatsApp.'},
         'senales': ['Cuentas oficiales de empresas tienen check verde en WhatsApp Business.', 'Sin check verde = NO es la cuenta oficial.', 'Las empresas reales casi nunca inician conversaciones por WhatsApp.'],
         'quiz': {'p': '¿Cómo distingues una cuenta REAL de empresa en WhatsApp?', 'opciones': ['Por el nombre que ponen', 'Por el check VERDE de WhatsApp Business verificado', 'Por la foto de perfil', 'Por cuántos minutos lleva en línea'], 'correcta': 1,
                  'explica': 'Solo el check verde garantiza que es una cuenta oficial verificada. Cualquiera puede ponerse "Soporte BBVA Oficial" como nombre.'}},
        {'nombre': 'Señal 5 — La regla universal: verificación cruzada',
         'queEs': 'Ante cualquier mensaje sospechoso, la regla mágica es VERIFICAR POR OTRO CANAL. Si dice ser tu hijo → llamas a tu hijo al número de siempre. Si dice ser tu banco → entras a la app del banco TÚ mismo.',
         'ejemplo': {'tipo': 'bueno', 'texto': '✅ Te llega un WhatsApp del "banco" sobre un cargo raro. CIERRAS WhatsApp. ABRES la app oficial del banco directamente. Si hay algo, ahí lo verás. Si no, era estafa.'},
         'senales': ['Nunca uses los enlaces o teléfonos del propio mensaje sospechoso.', 'Llama TÚ al número oficial (detrás de tu tarjeta) o entra a la app TÚ mismo.', 'Si es real, la persona/empresa no se enfada: lo agradece.'],
         'quiz': {'p': 'La regla más potente contra los fraudes por WhatsApp es:', 'opciones': ['Tener un antivirus', 'Verificar por OTRO canal antes de actuar', 'Bloquear todos los desconocidos', 'No usar WhatsApp'], 'correcta': 1,
                  'explica': 'La verificación cruzada funciona contra TODOS los engaños sociales (WhatsApp, llamadas, email, deepfakes).'}},
    ],
    'FRASES_VF': [
        {'texto': 'Un familiar tuyo escribiéndote desde un número desconocido pidiendo dinero urgente es señal CLARA de estafa.', 'correcta': True, 'explica': 'Verdadero. Verifica SIEMPRE llamando al número HABITUAL antes de hacer nada.'},
        {'texto': 'Si un mensaje de WhatsApp tiene check verde de verificación, es una cuenta oficial.', 'correcta': True, 'explica': 'Verdadero. El check verde garantiza cuenta oficial verificada por WhatsApp Business.'},
        {'texto': 'WhatsApp tiene un equipo de soporte que te escribe por mensaje cuando hay problemas con tu cuenta.', 'correcta': False, 'explica': 'Falso. WhatsApp NO te escribe nunca por mensaje. Quien diga ser "soporte WhatsApp" es estafador.'},
        {'texto': 'Dar el código de 6 dígitos que te ha llegado por SMS a alguien que lo pide es seguro si dice ser del soporte.', 'correcta': False, 'explica': 'Falso. Los códigos son SOLO para ti. Darlos = perder tu cuenta.'},
        {'texto': 'Las URLs acortadas (bit.ly, tinyurl) son sospechosas porque ocultan el dominio real al que llevan.', 'correcta': True, 'explica': 'Verdadero. Por eso los estafadores las usan: para que no veas que vas a una web falsa.'},
        {'texto': 'La forma más segura de comprobar un mensaje del banco es responder al mismo mensaje pidiendo más datos.', 'correcta': False, 'explica': 'Falso. NUNCA respondas. Entra TÚ a la app del banco o llama al teléfono detrás de tu tarjeta.'},
    ],
    'JS_EXTRA': '''
// 8 capturas ficticias de WhatsApp
const MENSAJES = [
  { de: '+34 612 33 78 91 (sin agenda)', veredicto: 'estafa',
    texto: '"Hola mamá, perdí el móvil. Este es mi nuevo número. Necesito que me hagas un Bizum URGENTE de 300€ para arreglarlo. Por favor, sin contárselo a papá. Te quiero ❤️"',
    explica: 'ESTAFA CLÁSICA del "hijo en apuros". Número desconocido + se hace pasar por hijo + urgencia + dinero + pide secretismo. Cinco banderas rojas en un solo mensaje.' },
  { de: 'Mamá (en agenda)', veredicto: 'seguro',
    texto: '"Hola cariño, ¿qué tal el día? ¿A qué hora vienes a casa? Hay pizza esta noche 🍕"',
    explica: 'SEGURO. Número de tu agenda real + tono y contenido normales de tu madre + sin pedir nada urgente. Ningún indicador de fraude.' },
  { de: '+34 600 12 34 56 (sin agenda)', veredicto: 'estafa',
    texto: '"🎉 ¡FELICIDADES! Has sido seleccionado por Amazon como cliente del mes. Has ganado un iPhone 15 Pro 📱. Pincha en este enlace en las próximas 24h para reclamar tu premio: bit.ly/amzn-premio-2026"',
    explica: 'ESTAFA. Premio imposible + urgencia + URL acortada + número desconocido. Amazon nunca regala iPhones por WhatsApp.' },
  { de: 'Pedro (en agenda) - compañero clase', veredicto: 'sospechoso',
    texto: '"¡Mira este test super divertido que dice a qué famoso te pareces! 😎 https://famoso-tu-cara.online/test"',
    explica: 'SOSPECHOSO. Aunque el número es de tu amigo, el enlace lleva a una URL rara (.online). Su cuenta puede estar hackeada o suplantada. Pregúntale POR OTRO CANAL antes de pinchar.' },
  { de: 'BBVA Soporte Oficial (sin check verde)', veredicto: 'estafa',
    texto: '"Estimado cliente, hemos detectado movimientos sospechosos en su cuenta. Para evitar el bloqueo, verifique sus datos en https://bbva-verificar.es/cliente"',
    explica: 'ESTAFA. Sin check verde de WhatsApp Business + enlace a dominio raro (bbva-verificar.es no es el real). Los bancos NO funcionan así por WhatsApp. Entra a la app del banco TÚ mismo.' },
  { de: 'Lucía (en agenda) - prima', veredicto: 'seguro',
    texto: '"Tía, ¿te acuerdas de la receta de los buñuelos que hace abuela? Quiero hacerlos este finde 🍩"',
    explica: 'SEGURO. Número conocido, contenido coherente con tu familia, sin urgencias ni enlaces ni petición de dinero.' },
  { de: '+34 690 22 88 77 (sin agenda)', veredicto: 'estafa',
    texto: '"Hola, soy del soporte de WhatsApp. Hemos detectado que tu cuenta ha sido comprometida. Por favor pásanos el código de 6 dígitos que acabas de recibir por SMS para protegerla."',
    explica: 'ESTAFA CRÍTICA. WhatsApp NUNCA te escribe directamente. Si das el código → te roban WhatsApp inmediatamente y empezarán a estafar a tus contactos haciéndose pasar por ti.' },
  { de: 'Ana (en agenda) - mejor amiga', veredicto: 'sospechoso',
    texto: '"Ey, ¿me prestas 50€ por Bizum? Te los devuelvo el viernes. Es urgente porfa, no te lo pediría si no fuera importante"',
    explica: 'SOSPECHOSO. Aunque el número es real, una petición urgente de dinero sin contexto puede ser que le hayan hackeado WhatsApp. LLÁMALA por teléfono primero para confirmar que es ella de verdad. 30 segundos de verificación.' },
];

let msgsContestados = new Set();
let msgsAciertos = 0;
function renderMensajes() {
  const cont = document.getElementById('zona-mensajes');
  cont.innerHTML = MENSAJES.map(function(m, i) {
    return '<div class="situacion" data-idx="' + i + '">' +
      '<span class="num-situacion">CAPTURA ' + (i+1) + ' / 8</span>' +
      '<div class="texto-situacion"><strong>De:</strong> ' + m.de + '<br><br><em>' + m.texto + '</em></div>' +
      '<div class="opciones-sit" id="opc-msg-' + i + '">' +
        '<button onclick="responderMsg(' + i + ',\\'seguro\\')">🟢 SEGURO</button>' +
        '<button onclick="responderMsg(' + i + ',\\'sospechoso\\')">🟡 SOSPECHOSO</button>' +
        '<button onclick="responderMsg(' + i + ',\\'estafa\\')">🔴 ESTAFA</button>' +
      '</div>' +
      '<div class="explica-sit" id="exp-msg-' + i + '"></div>' +
    '</div>';
  }).join('');
}
function responderMsg(idx, eleccion) {
  if (msgsContestados.has(idx)) return;
  msgsContestados.add(idx);
  const m = MENSAJES[idx];
  const acertado = (eleccion === m.veredicto);
  if (acertado) msgsAciertos++;
  const botones = document.querySelectorAll('#opc-msg-' + idx + ' button');
  const etiquetas = { seguro: 'SEGURO', sospechoso: 'SOSPECHOSO', estafa: 'ESTAFA' };
  botones.forEach(function(b) {
    b.disabled = true;
    if (b.textContent.includes(etiquetas[m.veredicto])) b.classList.add('correcta');
    else if (b.textContent.includes(etiquetas[eleccion]) && !acertado) b.classList.add('incorrecta');
  });
  const exp = document.getElementById('exp-msg-' + idx);
  exp.innerHTML = (acertado ? '✅ Correcto. ' : '❌ Era ' + etiquetas[m.veredicto] + '. ') + m.explica;
  exp.dataset.activo = 'true';
  if (msgsContestados.size >= MENSAJES.length) {
    document.getElementById('confirma-galeria').style.display = 'flex';
  }
}
const _initOriginal = typeof initSesion === 'function' ? initSesion : null;
function initSesion() { if (_initOriginal) _initOriginal(); renderMensajes(); }
'''
}


# Generar las 6
SESIONES = [S4, S5, S6, S7, S8, S10]

for s in SESIONES:
    html, js = build(s)
    num = f"{s['num']:02d}"
    html_path = ROOT / f's{num}.html'
    js_path = ROOT / f's{num}.js'
    html_path.write_text(html, encoding='utf-8')
    js_path.write_text(js, encoding='utf-8')
    print(f"  ✓ s{num}.html ({len(html)//1024} KB) + s{num}.js ({len(js)//1024} KB)")

print(f"\n{len(SESIONES)} sesiones generadas.")

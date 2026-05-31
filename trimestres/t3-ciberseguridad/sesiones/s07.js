/* S07 · Perfil de riesgo en redes · Academia Cyber-IES */
const SESION_ID = 's07';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    "nombre": "Indicador 1 — Cuenta pública vs privada",
    "queEs": "Una cuenta PÚBLICA cualquiera puede verla. Una PRIVADA solo tus seguidores aprobados. Es la decisión número 1 que define tu riesgo.",
    "ejemplo": {
      "tipo": "peligroso",
      "texto": "⚠️ Cuenta de Instagram pública de una chica de 14 años, con 8 publicaciones de \"estoy SOLA en casa este finde\". Cualquiera del mundo puede verlas. Riesgo ALTO."
    },
    "senales": [
      "Pública = el mundo entero la puede ver, incluidos desconocidos.",
      "Privada = solo seguidores aprobados por ti.",
      "Lo demás (bio, fotos) importa MUCHO más en una cuenta pública."
    ],
    "quiz": {
      "p": "¿Cuándo tiene sentido tener Instagram PÚBLICO?",
      "opciones": [
        "Para tener más seguidores",
        "Si eres un negocio, marca o profesional que quiere visibilidad",
        "Para que te encuentren tus amigos",
        "Siempre"
      ],
      "correcta": 1,
      "explica": "Para particulares (sobre todo menores), PRIVADA es lo seguro. Pública solo si eres una marca o creador profesional."
    }
  },
  {
    "nombre": "Indicador 2 — Datos personales en la bio",
    "queEs": "La bio que dice \"Lucía · 13 · Granada · IES Lorca · 1ºESO B\" es un manual para acosadores: edad, ciudad, instituto, clase. TODO ahí.",
    "ejemplo": {
      "tipo": "peligroso",
      "texto": "⚠️ Bio típica de menor: nombre real + edad + ciudad + colegio. Riesgo ALTO. Cualquiera puede ir a la puerta del colegio a buscarte."
    },
    "senales": [
      "Nombre real + edad + ciudad = perfil identificable.",
      "Mencionar el instituto/clase es exponerse a desconocidos.",
      "Iniciales o apodo es más seguro que nombre real."
    ],
    "quiz": {
      "p": "¿Cuál de estas bios es MENOS arriesgada para una chica de 13 años?",
      "opciones": [
        "\"Lucía García · 13 años · Granada · IES Lorca 1ºB\"",
        "\"L. · K-pop fan · 📍 Andalucía\"",
        "\"Lucía 2012 · cumpleañera el 12 de marzo\"",
        "\"Lucía García López\""
      ],
      "correcta": 1,
      "explica": "Iniciales + interés general + ubicación amplia. Sin nombre completo, sin edad, sin colegio."
    }
  },
  {
    "nombre": "Indicador 3 — Geolocalización y rutinas",
    "queEs": "Publicar la ubicación de tus posts o subir siempre desde el mismo sitio a la misma hora REVELA tu rutina. Y la rutina es lo más útil para alguien que quiera encontrarte.",
    "ejemplo": {
      "tipo": "peligroso",
      "texto": "⚠️ Subes una foto cada miércoles a las 18:00 desde el mismo centro comercial, con ubicación etiquetada. Riesgo ALTO: cualquiera sabe dónde estarás el próximo miércoles."
    },
    "senales": [
      "Ubicación etiquetada en CADA post → rutina mapeable.",
      "Mismo lugar + misma hora en muchos posts.",
      "Casa, instituto, gimnasio… las 3 ubicaciones MÁS sensibles."
    ],
    "quiz": {
      "p": "¿Qué tipo de ubicación NUNCA deberías etiquetar en tus posts?",
      "opciones": [
        "Un monumento turístico al que vas de visita",
        "Tu casa, tu instituto, tu gimnasio (sitios que frecuentas)",
        "Un restaurante donde fuiste una vez",
        "Un país al que viajas"
      ],
      "correcta": 1,
      "explica": "Los sitios donde estás repetidamente. Etiquetar un sitio turístico puntual no es lo mismo que etiquetar tu casa."
    }
  },
  {
    "nombre": "Indicador 4 — Etiquetas y conexiones",
    "queEs": "Aunque tu cuenta sea privada, las personas a las que etiquetas (con cuenta pública) pueden hacer visible tu información. Tu privacidad depende también de la de tus amigos.",
    "ejemplo": {
      "tipo": "peligroso",
      "texto": "⚠️ Tu cuenta es privada, pero etiquetas a tu novio Diego (cuenta pública) en una foto. La foto sale en el feed de Diego → cualquiera la puede ver y saber que estáis juntos."
    },
    "senales": [
      "Etiquetar a cuentas públicas hace VISIBLE tu contenido.",
      "Hashtags muy específicos (#IESLorca, #1ESOB) reúnen contenido de tu grupo.",
      "Etiquetar a familia menor de edad puede comprometerla."
    ],
    "quiz": {
      "p": "Si tu cuenta es PRIVADA pero etiquetas a tu mejor amiga que tiene cuenta PÚBLICA, ¿qué pasa con la foto?",
      "opciones": [
        "Sigue solo en tu privado",
        "Aparece también en el feed PÚBLICO de tu amiga, visible para todos",
        "Desaparece",
        "Se hace privada para los dos"
      ],
      "correcta": 1,
      "explica": "La etiqueta lleva la foto al feed del etiquetado. Si esa cuenta es pública, tu foto se hace pública aunque tu cuenta no lo sea."
    }
  },
  {
    "nombre": "Indicador 5 — Contraseñas y 2FA de la cuenta",
    "queEs": "Da igual lo bien que cuides la apariencia: si tu contraseña es débil o no tienes 2FA, te pueden hackear y desde dentro el atacante hace lo que quiera con tu perfil.",
    "ejemplo": {
      "tipo": "bueno",
      "texto": "✅ Tu cuenta tiene contraseña larga ÚNICA + 2FA por SMS activado. Aunque te roben la contraseña, sin tu móvil no entran."
    },
    "senales": [
      "Contraseña fuerte (15+ caracteres) y ÚNICA de esa cuenta.",
      "2FA activado (SMS, app autenticadora o huella).",
      "Revisión periódica de dispositivos conectados en \"ajustes de seguridad\"."
    ],
    "quiz": {
      "p": "Tienes Instagram con cuenta privada, bio limpia, sin geolocalización… pero contraseña \"lucia2012\" y SIN 2FA. ¿Es seguro?",
      "opciones": [
        "Sí, la cuenta privada lo protege todo",
        "No: si te hackean la contraseña, todo lo demás no sirve",
        "Solo medianamente",
        "Da igual"
      ],
      "correcta": 1,
      "explica": "La privacidad de la cuenta solo importa si la cuenta NO está hackeada. Contraseña + 2FA son el cimiento."
    }
  }
];

const FRASES_VF = [
  {
    "texto": "Tener Instagram público multiplica el riesgo, sobre todo en menores.",
    "correcta": true,
    "explica": "Verdadero. Las cuentas públicas exponen tu contenido al mundo entero, incluyendo desconocidos."
  },
  {
    "texto": "Si tu cuenta es privada, ya estás 100% protegido aunque etiquetes a amigos con cuenta pública.",
    "correcta": false,
    "explica": "Falso. Si etiquetas a alguien de cuenta pública, tu foto aparece en su feed visible."
  },
  {
    "texto": "Poner en la bio \"1ºESO B del IES Lorca\" facilita a un acosador encontrarte físicamente.",
    "correcta": true,
    "explica": "Verdadero. Dar tu instituto + clase es dar tu ubicación cada día de la semana."
  },
  {
    "texto": "Etiquetar la ubicación REAL de tus posts no es peligroso si lo haces solo de vez en cuando.",
    "correcta": false,
    "explica": "Falso. Una sola ubicación de tu casa o instituto ya basta para localizarte."
  },
  {
    "texto": "El 2FA en Instagram se activa en menos de 1 minuto y bloquea el 95% de los intentos de hackeo.",
    "correcta": true,
    "explica": "Verdadero. Está en Ajustes → Seguridad. Tarda menos que verse un TikTok."
  },
  {
    "texto": "Una cuenta es totalmente segura si tiene buena contraseña, aunque sea pública y publique la dirección de casa.",
    "correcta": false,
    "explica": "Falso. La seguridad de la cuenta NO te protege de lo que publicas voluntariamente."
  }
];


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
        '<button onclick="responderPerfil(' + i + ',\'BAJO\')">🟢 BAJO</button>' +
        '<button onclick="responderPerfil(' + i + ',\'MEDIO\')">🟡 MEDIO</button>' +
        '<button onclick="responderPerfil(' + i + ',\'ALTO\')">🔴 ALTO</button>' +
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

// ── TEORÍA ──────────────────────────────────────────────────────
let tarjetaActual = 0;
const microquizContestados = new Set();
const microquizAciertos = new Set();

function reiniciarTeoria() {
  microquizContestados.clear();
  microquizAciertos.clear();
  var bf = document.getElementById('barra-fin-teoria'); if (bf) bf.style.display = 'none';
  tarjetaActual = 0;
  renderTarjetas();
  irATarjeta(0);
  window.scrollTo({ top: 0, behavior: 'smooth' });
}
function reiniciarVF() {
  vfContestadas.clear();
  vfAciertos = 0;
  var a = document.getElementById('vf-aciertos'); if (a) a.textContent = '0';
  var r = document.getElementById('vf-restantes'); if (r) r.textContent = FRASES_VF.length;
  renderVF();
  var z = document.getElementById('zona-frases-vf'); if (z) z.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function renderTarjetas() {
  const cont = document.getElementById('tarjetas-teoria');
  cont.innerHTML = CONCEPTOS.map(function(c, i) {
    return '<article class="tarjeta-teoria" data-idx="' + i + '" data-activa="' + (i === 0 ? 'true' : 'false') + '">' +
      '<div><span class="concepto-num">CONCEPTO ' + (i + 1) + ' / ' + CONCEPTOS.length + '</span>' +
      '<span class="concepto-fase" id="fase-' + i + '">PANTALLA 1 / 3</span></div>' +
      '<h3>' + c.nombre + '</h3>' +
      '<div class="subtarjeta" data-sub="0" data-activa="true">' +
        '<p class="que-es">' + c.queEs + '</p>' +
        '<div class="ej ' + c.ejemplo.tipo + '"><span class="et">' +
        (c.ejemplo.tipo === 'bueno' ? '✅ Ejemplo' : '⚠️ Ejemplo') + '</span>' + c.ejemplo.texto + '</div>' +
      '</div>' +
      '<div class="subtarjeta" data-sub="1">' +
        '<div class="reconocer-titulo">🔍 Cómo lo reconoces</div>' +
        '<div class="senales">' +
          c.senales.map(function(s, j) { return '<div class="senal"><b>Señal ' + (j+1) + '</b>' + s + '</div>'; }).join('') +
        '</div>' +
      '</div>' +
      '<div class="subtarjeta" data-sub="2">' +
        '<div class="microquiz" data-tarjeta="' + i + '">' +
          '<div class="pregunta-mq">🧠 ' + c.quiz.p + '</div>' +
          '<div class="opciones-mq" id="opcionesMq-' + i + '">' +
            c.quiz.opciones.map(function(op, j) { return '<button onclick="responderMicroquiz(' + i + ',' + j + ')">' + String.fromCharCode(65+j) + '. ' + op + '</button>'; }).join('') +
          '</div>' +
          '<div class="feedback-mq" id="fb-mq-' + i + '"></div>' +
        '</div>' +
      '</div>' +
      '<div class="nav-sub">' +
        '<button class="btn-acad secundario" onclick="navSub(' + i + ',-1)" id="btn-sub-prev-' + i + '" disabled>◂ Atrás</button>' +
        '<div class="ind"><span class="activa" data-sub="0"></span><span data-sub="1"></span><span data-sub="2"></span></div>' +
        '<button class="btn-acad" onclick="navSub(' + i + ',1)" id="btn-sub-next-' + i + '">Continuar ▸</button>' +
      '</div>' +
    '</article>';
  }).join('');
  document.getElementById('puntos-tarjetas').innerHTML = CONCEPTOS.map(function(_, i) { return '<div class="punto ' + (i === 0 ? 'activo' : '') + '" onclick="irATarjeta(' + i + ')"></div>'; }).join('');
}
function navSub(idx, delta) {
  const t = document.querySelector('.tarjeta-teoria[data-idx="' + idx + '"]');
  const subs = t.querySelectorAll('.subtarjeta');
  let actual = -1; subs.forEach(function(s, i) { if (s.dataset.activa === 'true') actual = i; });
  const nuevo = actual + delta;
  if (nuevo < 0) return;
  if (nuevo > 2) { if (microquizContestados.has(idx)) navTarjeta(1); return; }
  subs.forEach(function(s) { s.dataset.activa = 'false'; });
  subs[nuevo].dataset.activa = 'true';
  const inds = t.querySelectorAll('.nav-sub .ind span');
  inds.forEach(function(ind, i) { ind.classList.remove('activa','completada'); if (i === nuevo) ind.classList.add('activa'); else if (i < nuevo) ind.classList.add('completada'); });
  document.getElementById('fase-' + idx).textContent = 'PANTALLA ' + (nuevo + 1) + ' / 3';
  document.getElementById('btn-sub-prev-' + idx).disabled = nuevo === 0;
  const btnN = document.getElementById('btn-sub-next-' + idx);
  if (nuevo === 2) { btnN.textContent = microquizContestados.has(idx) ? 'Siguiente concepto ▸' : '🔒 Responde el microquiz'; btnN.disabled = !microquizContestados.has(idx); }
  else { btnN.textContent = 'Continuar ▸'; btnN.disabled = false; }
}
function navTarjeta(delta) { irATarjeta(tarjetaActual + delta); }
function irATarjeta(idx) {
  if (idx < 0 || idx >= CONCEPTOS.length) return;
  document.querySelectorAll('.tarjeta-teoria').forEach(function(t) { t.dataset.activa = 'false'; });
  document.querySelector('.tarjeta-teoria[data-idx="' + idx + '"]').dataset.activa = 'true';
  tarjetaActual = idx;
  const t = document.querySelector('.tarjeta-teoria[data-idx="' + idx + '"]');
  t.querySelectorAll('.subtarjeta').forEach(function(s, i) { s.dataset.activa = (i === 0 ? 'true' : 'false'); });
  t.querySelectorAll('.nav-sub .ind span').forEach(function(ind, i) { ind.classList.remove('activa','completada'); if (i === 0) ind.classList.add('activa'); });
  document.getElementById('fase-' + idx).textContent = 'PANTALLA 1 / 3';
  document.getElementById('btn-sub-prev-' + idx).disabled = true;
  document.getElementById('btn-sub-next-' + idx).textContent = 'Continuar ▸';
  document.getElementById('btn-sub-next-' + idx).disabled = false;
  document.querySelectorAll('.puntos-tarjetas .punto').forEach(function(p, i) { p.classList.remove('activo','visto'); if (i === idx) p.classList.add('activo'); else if (microquizContestados.has(i)) p.classList.add('visto'); });
  document.getElementById('btn-anterior').disabled = idx === 0;
  document.getElementById('btn-siguiente').disabled = !microquizContestados.has(idx);
  if (idx === CONCEPTOS.length - 1 && microquizContestados.has(idx)) { document.getElementById('barra-fin-teoria').style.display = 'flex'; otorgarInsignia('cadete'); }
}
function responderMicroquiz(idx, idxOp) {
  if (microquizContestados.has(idx)) return;
  const c = CONCEPTOS[idx].quiz;
  const fb = document.getElementById('fb-mq-' + idx);
  const botones = document.querySelectorAll('#opcionesMq-' + idx + ' button');
  if (idxOp !== c.correcta) {
    botones.forEach(function(b){ b.disabled = true; });
    botones[idxOp].classList.add('incorrecta');
    fb.innerHTML = '❌ Has fallado. Para la insignia hay que acertar los ' + CONCEPTOS.length + ' microquiz SEGUIDOS: vuelves al primer concepto.';
    fb.dataset.activo = 'true';
    setTimeout(reiniciarTeoria, 1700);
    return;
  }
  microquizContestados.add(idx);
  microquizAciertos.add(idx);
  botones.forEach(function(b, i) { b.disabled = true; if (i === c.correcta) b.classList.add('correcta'); });
  fb.innerHTML = '✅ ' + c.explica;
  fb.dataset.activo = 'true';
  const btnN = document.getElementById('btn-sub-next-' + idx);
  btnN.textContent = idx === CONCEPTOS.length - 1 ? '✓ Microquiz hecho' : 'Siguiente concepto ▸';
  btnN.disabled = false;
  document.getElementById('btn-siguiente').disabled = false;
  document.querySelectorAll('.puntos-tarjetas .punto').forEach(function(p, i) { if (i === idx) p.classList.add('visto'); });
  if (idx === CONCEPTOS.length - 1) {
    document.getElementById('barra-fin-teoria').style.display = 'flex';
    otorgarInsignia('cadete');
  }
}

// V/F
let vfActuales = []; let vfAciertos = 0, vfFallos = 0; const vfContestadas = new Set();
function renderVF() {
  vfActuales = FRASES_VF.slice().sort(function() { return Math.random() - 0.5; });
  const cont = document.getElementById('zona-frases-vf');
  cont.innerHTML = vfActuales.map(function(f, i) {
    return '<div class="frase-vf" data-idx="' + i + '">' +
      '<div class="texto-frase">' + (i + 1) + '. ' + f.texto + '</div>' +
      '<div class="vf-botones">' +
        '<button onclick="responderVF(' + i + ',true)">✓ Verdadero</button>' +
        '<button onclick="responderVF(' + i + ',false)">✗ Falso</button>' +
      '</div>' +
      '<div class="explica-vf" id="exp-vf-' + i + '"></div>' +
    '</div>';
  }).join('');
}
function responderVF(idx, valor) {
  if (vfContestadas.has(idx)) return;
  const f = vfActuales[idx];
  const acertado = (valor === f.correcta);
  const cont = document.querySelector('.frase-vf[data-idx="' + idx + '"]');
  const botones = cont.querySelectorAll('.vf-botones button');
  const exp = document.getElementById('exp-vf-' + idx);
  if (!acertado) {
    vfFallos++;
    document.getElementById('vf-fallos').textContent = vfFallos;
    botones.forEach(function(b){ b.disabled = true; });
    exp.innerHTML = '❌ Fallaste. ' + f.explica + ' <b>Hay que acertar las ' + FRASES_VF.length + ' SEGUIDAS: vuelves a la primera.</b>';
    exp.dataset.activo = 'true';
    setTimeout(reiniciarVF, 1900);
    return;
  }
  vfContestadas.add(idx);
  vfAciertos++;
  botones.forEach(function(b, i) {
    b.disabled = true;
    const esCorrectaBtn = (i === 0 && f.correcta) || (i === 1 && !f.correcta);
    if (esCorrectaBtn) b.classList.add('correcta');
  });
  exp.innerHTML = '✅ ' + f.explica;
  exp.dataset.activo = 'true';
  document.getElementById('vf-aciertos').textContent = vfAciertos;
  document.getElementById('vf-restantes').textContent = FRASES_VF.length - vfContestadas.size;
  if (vfContestadas.size === FRASES_VF.length) {
    document.getElementById('btn-al-reto').disabled = false;
    otorgarInsignia('analista');
  }
}

// Marcar reto como hecho (lanzado por el código específico del reto)
function marcarRetoHecho() {
  const btn = document.getElementById('btn-reto-hecho');
  if (btn) { btn.disabled = true; btn.textContent = '✓ Reto completado'; }
  document.getElementById('barra-fin-juego').style.display = 'flex';
  otorgarInsignia('investigador');
  Academia.setSesion(SESION_ID, { retoHecho: true });
}

// INSIGNIAS
const insigniasGanadas = new Set();
function otorgarInsignia(nombre) {
  if (insigniasGanadas.has(nombre)) return;
  insigniasGanadas.add(nombre);
  const el = document.querySelector('.mi-insignia[data-mi="' + nombre + '"]');
  if (el) el.dataset.ganada = 'true';
  const nombres = {"cadete": "Cadete", "analista": "Analista", "investigador": "Auditor Junior", "detective": "Auditor de Perfiles"};
  const emojis = { cadete: '🎖️', analista: '🎖️', investigador: '🎖️', detective: '🏆' };
  mostrarToast('Has ganado', emojis[nombre] + ' ' + nombres[nombre]);
  Academia.setSesion(SESION_ID, { ['insignia_' + nombre]: true });
}
function mostrarToast(t, n) {
  const e = document.createElement('div'); e.className = 'toast-insignia';
  e.innerHTML = '<div class="emoji">🏅</div><div><div class="titulo">' + t + '</div><div class="nombre">' + n + '</div></div>';
  document.body.appendChild(e);
  setTimeout(function() { e.remove(); }, 4200);
}

// INFORME
function contarPalabras(t) { return (t.trim().match(/\S+/g) || []).length; }
function finalizarInforme() {
  const q1 = document.getElementById('inf-q1').value.trim();
  const q2 = document.getElementById('inf-q2').value.trim();
  const q3 = document.getElementById('inf-q3').value.trim();
  const v1 = Academia.respuestaInformeValida(q1);
  const v2 = Academia.respuestaInformeValida(q2);
  const v3 = Academia.respuestaInformeValida(q3);
  if (!v1.ok || !v2.ok || !v3.ok) {
    let detalle = '';
    if (!v1.ok) detalle += '<br>· Pregunta 1: ' + v1.motivo + '.';
    if (!v2.ok) detalle += '<br>· Pregunta 2: ' + v2.motivo + '.';
    if (!v3.ok) detalle += '<br>· Pregunta 3: ' + v3.motivo + '.';
    Academia.mostrarFeedback(document.getElementById('fb-informe'), 'mal', '<span class="et">❌ Informe incompleto</span>Necesitas responder de verdad, no con letras sueltas.' + detalle);
    return;
  }
  Academia.marcarCompletada(SESION_ID, microquizAciertos.size + vfAciertos, CONCEPTOS.length + FRASES_VF.length);
  Academia.setSesion(SESION_ID, { q1: q1, q2: q2, q3: q3, informeCompletado: true, tiempoMin: Math.round((Date.now() - tInicio) / 60000) });
  document.getElementById('res-teoria').textContent = microquizAciertos.size + ' / ' + CONCEPTOS.length + ' microquiz';
  document.getElementById('res-entrenamiento').textContent = vfAciertos + ' / ' + FRASES_VF.length + ' V/F';
  document.getElementById('res-tiempo').textContent = (Math.round((Date.now() - tInicio) / 60000)) + ' min';
  const cod = Academia.codigoFinalizacion(SESION_ID, microquizAciertos.size + vfAciertos);
  document.getElementById('cod-final').textContent = 'CÓDIGO: ' + cod;
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'Auditor de Perfiles' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}
function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'Auditor de Perfiles',
    subtitulo: 'Sesión 7 · Perfil de riesgo en redes · Promoción 2026',
    icono: '📊',
    insignia: 'Auditor de Perfiles',
    nombres: [n1, n2],
    sesionNum: 'SESION7',
    score: microquizAciertos.size + vfAciertos,
    total: CONCEPTOS.length + FRASES_VF.length,
    codigo: datos.codigo,
    frase: 'Tu perfil dice más de ti que tú mismo. Asegúrate de que dice lo justo'
  }, 'S07-perfil-riesgo-' + n1.replace(/\s/g, '_') + '.png');
}

function initSesion() {
  renderTarjetas();
  renderVF();
  const datos = Academia.getSesion(SESION_ID);
  ['q1','q2','q3'].forEach(function(q) {
    if (datos[q]) {
      const ta = document.getElementById('inf-' + q);
      if (ta) { ta.value = datos[q]; document.getElementById('cnt-' + q).textContent = contarPalabras(datos[q]) + ' palabras'; }
    }
  });
  document.querySelectorAll('.informe-pregunta textarea').forEach(function(ta) {
    ta.addEventListener('input', function() {
      document.getElementById('cnt-' + ta.dataset.q).textContent = contarPalabras(ta.value) + ' palabras';
      Academia.setSesion(SESION_ID, { [ta.dataset.q]: ta.value });
    });
  });
}
if (document.readyState !== 'loading') initSesion();
else document.addEventListener('DOMContentLoaded', initSesion);

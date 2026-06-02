/* S10 · WhatsApp bajo sospecha · Academia Cyber-IES */
const SESION_ID = 's10';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    "nombre": "Señal 1 — Número desconocido pidiendo dinero o datos",
    "queEs": "Si te llega un mensaje de un número que no tienes en la agenda diciendo \"soy fulanito\" y pidiendo cualquier cosa, sospecha SIEMPRE. Los estafadores se hacen pasar por hijos, sobrinos, jefes…",
    "ejemplo": {
      "tipo": "peligroso",
      "texto": "⚠️ \"Hola mamá, este es mi nuevo número (perdí el móvil), ¿me puedes hacer un Bizum urgente de 300€?\". Estafa clásica de \"hijo en apuros\". En España, miles de víctimas al mes."
    },
    "senales": [
      "Número que NO tienes en agenda.",
      "Se hace pasar por familiar/amigo cercano.",
      "Pide dinero/datos con urgencia (Bizum, transferencia, código de un SMS)."
    ],
    "quiz": {
      "p": "Te llega de un número desconocido: \"Mamá, perdí el móvil, este es mi nuevo número, mándame 200€ por Bizum\". ¿Qué haces?",
      "opciones": [
        "Mando el dinero, mi hijo me necesita",
        "Llamo TÚ al número HABITUAL de mi hijo para verificar antes de hacer nada",
        "Respondo pidiendo más datos",
        "Bloqueo sin hacer nada más"
      ],
      "correcta": 1,
      "explica": "Verificación cruzada: llama al número de SIEMPRE de tu hijo por el canal de SIEMPRE. La estafa se desmonta en 30 segundos."
    }
  },
  {
    "nombre": "Señal 2 — Enlaces sospechosos",
    "queEs": "Cualquier enlace en WhatsApp puede llevar a una web falsa. Las marcas reales NO suelen mandar enlaces por WhatsApp para verificar cuentas o reclamar premios.",
    "ejemplo": {
      "tipo": "peligroso",
      "texto": "⚠️ \"Has ganado un iPhone 15 por ser nuestro cliente número 1000000 🎉 Recógelo aquí: bit.ly/premio-apple\". 100% estafa. Apple no funciona así."
    },
    "senales": [
      "URLs acortadas (bit.ly, tinyurl) que ocultan el dominio real.",
      "Promesas exageradas (premios, descuentos imposibles).",
      "Urgencia: \"tienes que pinchar antes de 24h\"."
    ],
    "quiz": {
      "p": "Te llega por WhatsApp: \"🎁 Has ganado 5000€ de Amazon, pincha aquí: bit.ly/regalo-am\". ¿Qué haces?",
      "opciones": [
        "Pincho rápido antes de que se acabe",
        "Lo borro y bloqueo. Es estafa segura",
        "Reenvío a mi grupo para que ganen ellos también",
        "Le contesto pidiendo más info"
      ],
      "correcta": 1,
      "explica": "Premios imposibles + URL acortada + urgencia = estafa segura. Nunca pinches, nunca reenvíes."
    }
  },
  {
    "nombre": "Señal 3 — Pedir códigos de verificación",
    "queEs": "Si alguien te pide el código de SMS que has recibido (de WhatsApp, banco, Insta…), es un INTENTO DE HACKEAR TU CUENTA. Los códigos son SOLO para ti.",
    "ejemplo": {
      "tipo": "peligroso",
      "texto": "⚠️ \"Hola, soy del soporte de WhatsApp. Acabamos de mandarte un SMS con un código de 6 dígitos. Pásamelo, por favor\". JAMÁS. Quieren robarte WhatsApp."
    },
    "senales": [
      "Te piden el código de un SMS que has recibido.",
      "Se hacen pasar por soporte de la app o servicio.",
      "Si das el código → te roban la cuenta inmediatamente."
    ],
    "quiz": {
      "p": "Alguien por WhatsApp te dice: \"soy del soporte de WhatsApp, dame el código de 6 dígitos que te ha llegado\". ¿Qué haces?",
      "opciones": [
        "Se lo doy, parece oficial",
        "NUNCA doy códigos a nadie. Los códigos son SOLO para mí",
        "Solo si pone que es urgente",
        "Lo pregunto a mis amigos primero"
      ],
      "correcta": 1,
      "explica": "Los códigos NUNCA se dan a nadie. WhatsApp, bancos y servicios JAMÁS te los piden por mensaje o llamada."
    }
  },
  {
    "nombre": "Señal 4 — Cuentas verificadas y \"soporte\"",
    "queEs": "WhatsApp NO tiene un canal de soporte que te escriba directamente. Las cuentas REALES de empresas (Amazon, banco) en WhatsApp Business tienen un check verde. SIN ese check, sospecha.",
    "ejemplo": {
      "tipo": "peligroso",
      "texto": "⚠️ Te escribe \"Soporte BBVA Oficial\" sin check verde. Es FALSO. El BBVA real tiene check verde o no te escribe por WhatsApp."
    },
    "senales": [
      "Cuentas oficiales de empresas tienen check verde en WhatsApp Business.",
      "Sin check verde = NO es la cuenta oficial.",
      "Las empresas reales casi nunca inician conversaciones por WhatsApp."
    ],
    "quiz": {
      "p": "¿Cómo distingues una cuenta REAL de empresa en WhatsApp?",
      "opciones": [
        "Por el nombre que ponen",
        "Por el check VERDE de WhatsApp Business verificado",
        "Por la foto de perfil",
        "Por cuántos minutos lleva en línea"
      ],
      "correcta": 1,
      "explica": "Solo el check verde garantiza que es una cuenta oficial verificada. Cualquiera puede ponerse \"Soporte BBVA Oficial\" como nombre."
    }
  },
  {
    "nombre": "Señal 5 — La regla universal: verificación cruzada",
    "queEs": "Ante cualquier mensaje sospechoso, la regla mágica es VERIFICAR POR OTRO CANAL. Si dice ser tu hijo → llamas a tu hijo al número de siempre. Si dice ser tu banco → entras a la app del banco TÚ mismo.",
    "ejemplo": {
      "tipo": "bueno",
      "texto": "✅ Te llega un WhatsApp del \"banco\" sobre un cargo raro. CIERRAS WhatsApp. ABRES la app oficial del banco directamente. Si hay algo, ahí lo verás. Si no, era estafa."
    },
    "senales": [
      "Nunca uses los enlaces o teléfonos del propio mensaje sospechoso.",
      "Llama TÚ al número oficial (detrás de tu tarjeta) o entra a la app TÚ mismo.",
      "Si es real, la persona/empresa no se enfada: lo agradece."
    ],
    "quiz": {
      "p": "La regla más potente contra los fraudes por WhatsApp es:",
      "opciones": [
        "Tener un antivirus",
        "Verificar por OTRO canal antes de actuar",
        "Bloquear todos los desconocidos",
        "No usar WhatsApp"
      ],
      "correcta": 1,
      "explica": "La verificación cruzada funciona contra TODOS los engaños sociales (WhatsApp, llamadas, email, deepfakes)."
    }
  }
];

const FRASES_VF = [
  {
    "texto": "Un familiar tuyo escribiéndote desde un número desconocido pidiendo dinero urgente es señal CLARA de estafa.",
    "correcta": true,
    "explica": "Verdadero. Verifica SIEMPRE llamando al número HABITUAL antes de hacer nada."
  },
  {
    "texto": "Si un mensaje de WhatsApp tiene check verde de verificación, es una cuenta oficial.",
    "correcta": true,
    "explica": "Verdadero. El check verde garantiza cuenta oficial verificada por WhatsApp Business."
  },
  {
    "texto": "WhatsApp tiene un equipo de soporte que te escribe por mensaje cuando hay problemas con tu cuenta.",
    "correcta": false,
    "explica": "Falso. WhatsApp NO te escribe nunca por mensaje. Quien diga ser \"soporte WhatsApp\" es estafador."
  },
  {
    "texto": "Dar el código de 6 dígitos que te ha llegado por SMS a alguien que lo pide es seguro si dice ser del soporte.",
    "correcta": false,
    "explica": "Falso. Los códigos son SOLO para ti. Darlos = perder tu cuenta."
  },
  {
    "texto": "Las URLs acortadas (bit.ly, tinyurl) son sospechosas porque ocultan el dominio real al que llevan.",
    "correcta": true,
    "explica": "Verdadero. Por eso los estafadores las usan: para que no veas que vas a una web falsa."
  },
  {
    "texto": "La forma más segura de comprobar un mensaje del banco es responder al mismo mensaje pidiendo más datos.",
    "correcta": false,
    "explica": "Falso. NUNCA respondas. Entra TÚ a la app del banco o llama al teléfono detrás de tu tarjeta."
  }
];


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
        '<button onclick="responderMsg(' + i + ',\'seguro\')">🟢 SEGURO</button>' +
        '<button onclick="responderMsg(' + i + ',\'sospechoso\')">🟡 SOSPECHOSO</button>' +
        '<button onclick="responderMsg(' + i + ',\'estafa\')">🔴 ESTAFA</button>' +
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
}
function navSub(idx, delta) {
  const t = document.querySelector('.tarjeta-teoria[data-idx="' + idx + '"]');
  const subs = t.querySelectorAll('.subtarjeta');
  let actual = -1; subs.forEach(function(s, i) { if (s.dataset.activa === 'true') actual = i; });
  const nuevo = actual + delta;
  if (nuevo < 0) return;
  if (nuevo > 2) { if (microquizContestados.has(idx)) { if (idx === CONCEPTOS.length - 1) Academia.irABloque('entrenamiento'); else navTarjeta(1); } return; }
  subs.forEach(function(s) { s.dataset.activa = 'false'; });
  subs[nuevo].dataset.activa = 'true';
  const inds = t.querySelectorAll('.nav-sub .ind span');
  inds.forEach(function(ind, i) { ind.classList.remove('activa','completada'); if (i === nuevo) ind.classList.add('activa'); else if (i < nuevo) ind.classList.add('completada'); });
  document.getElementById('fase-' + idx).textContent = 'PANTALLA ' + (nuevo + 1) + ' / 3';
  document.getElementById('btn-sub-prev-' + idx).disabled = nuevo === 0;
  const btnN = document.getElementById('btn-sub-next-' + idx);
  if (nuevo === 2) { btnN.textContent = !microquizContestados.has(idx) ? '🔒 Responde el microquiz' : (idx === CONCEPTOS.length - 1 ? 'A entrenar ▸' : 'Siguiente concepto ▸'); btnN.disabled = !microquizContestados.has(idx); }
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
  if (idx === CONCEPTOS.length - 1 && microquizContestados.has(idx)) { otorgarInsignia('cadete'); }
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
  btnN.textContent = idx === CONCEPTOS.length - 1 ? 'A entrenar ▸' : 'Siguiente concepto ▸';
  btnN.disabled = false;
  document.querySelectorAll('.puntos-tarjetas .punto').forEach(function(p, i) { if (i === idx) p.classList.add('visto'); });
  if (idx === CONCEPTOS.length - 1) {
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
  const nombres = {"cadete": "Cadete", "analista": "Analista", "investigador": "Inspector Junior", "detective": "Inspector de Mensajería"};
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
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'Inspector de Mensajería' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}
function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'Inspector de Mensajería',
    subtitulo: 'Sesión 10 · WhatsApp bajo sospecha · Promoción 2026',
    icono: '💬',
    insignia: 'Inspector de Mensajería',
    nombres: [n1, n2],
    sesionNum: 'SESION10',
    score: microquizAciertos.size + vfAciertos,
    total: CONCEPTOS.length + FRASES_VF.length,
    codigo: datos.codigo,
    frase: 'En WhatsApp, lo que parece de un amigo a veces es de un estafador'
  }, 'S10-whatsapp-' + n1.replace(/\s/g, '_') + '.png');
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

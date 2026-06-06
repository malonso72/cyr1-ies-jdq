/* ════════════════════════════════════════════════════════════════
   SESIÓN 2 · Contraseñas: el laboratorio
   Academia Cyber-IES · CyR 1º ESO · IES Jiménez de Quesada
   ════════════════════════════════════════════════════════════════ */

const SESION_ID = 's02';
const tInicio = Date.now();

// ── BLOQUE 2: 6 CONCEPTOS ───────────────────────────────────────
const CONCEPTOS = [
  {
    nombre: "Longitud > complejidad",
    queEs: "Lo que de verdad hace fuerte una contraseña es su LONGITUD, no los símbolos raros. Cada carácter extra multiplica el tiempo que tardarían en romperla. Un símbolo @ o # añade poco, una palabra entera añade muchísimo.",
    ejemplo: { tipo: 'bueno', texto: "✅ 'caballo-mesa-luna-puente-83' (28 caracteres, palabras corrientes) tardaría MILLONES de años en romperse. 'P@ss1!' tardaría segundos." },
    senales: [
      "Tienes 15+ caracteres en tu contraseña (cuantos más, mejor).",
      "Aunque solo uses minúsculas, si es larga, es FUERTE.",
      "Los símbolos raros (@#$%) son menos importantes que la longitud."
    ],
    quiz: {
      p: "¿Cuál de estas contraseñas es MÁS fuerte?",
      opciones: ["P@ss1!", "Lucia2012!", "caballo-mesa-luna-puente-83", "MiPerro7"],
      correcta: 2,
      explica: "La 3ª: 28 caracteres aunque solo use palabras corrientes. Romperla por fuerza bruta llevaría millones de años. La longitud manda."
    }
  },
  {
    nombre: "Frase de paso (passphrase)",
    queEs: "Una contraseña que NO es una palabra: es una FRASE que UNES con guiones o espacios. Por ejemplo 'mi-pez-azul-baila-en-jueves'. Fácil de recordar para ti, imposible de adivinar para nadie.",
    ejemplo: { tipo: 'bueno', texto: "✅ 'rosquilla-tractor-domingo-azul' es perfectamente memorable. Visualizas una rosquilla en un tractor un domingo azul y ya está." },
    senales: [
      "Está compuesta por 3-5 palabras unidas (con guiones, puntos o espacios).",
      "Te resulta IMPOSIBLE de olvidar (no de recordar).",
      "Las palabras son corrientes pero la combinación es absurda y única."
    ],
    quiz: {
      p: "¿Por qué una frase de paso es fácil de recordar Y difícil de adivinar?",
      opciones: [
        "Porque tiene muchas vocales",
        "Porque combina palabras corrientes en un orden absurdo: tu cerebro la memoriza fácil pero un atacante no la encuentra en diccionarios comunes",
        "Porque incluye tu nombre",
        "Porque tiene símbolos raros"
      ],
      correcta: 1,
      explica: "Las frases de paso aprovechan tu memoria visual (imaginas la escena) sin caer en lo predecible. Los ataques por diccionario fallan porque tu combinación no está en ningún diccionario."
    }
  },
  {
    nombre: "Reutilización (la trampa silenciosa)",
    queEs: "Usar la MISMA contraseña en varias cuentas multiplica el riesgo. Si UNA web se filtra, las demás cuentas con esa misma contraseña caen automáticamente. Cada cuenta importante necesita una contraseña ÚNICA.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Usas la misma contraseña en Insta, TikTok, Gmail y un foro de Minecraft. El foro se filtra (cosa frecuente). Ahora un atacante prueba tu email + esa contraseña en Insta, TikTok y Gmail. Caen las 4 cuentas." },
    senales: [
      "Si te olvidas la contraseña, sabes que es 'la misma de siempre' → señal de reutilización.",
      "Sentirte tranquilo porque 'mi contraseña es muy buena' NO es excusa si la usas en 10 sitios.",
      "Una sola filtración (HIBP te avisará) te obliga a cambiarla en TODAS las cuentas donde la usabas."
    ],
    quiz: {
      p: "Tu contraseña 'super-segura-2025' aparece en una filtración de un foro pequeño. ¿Qué pasa?",
      opciones: [
        "Solo se ve afectado ese foro",
        "Los atacantes prueban tu email + esa contraseña en cientos de webs (credential stuffing): cada cuenta donde la reutilizaras cae",
        "Nada, si la contraseña es buena no pueden hacer nada",
        "Te llega un email automático y se cambia sola"
      ],
      correcta: 1,
      explica: "Esto es credential stuffing: ataques automatizados prueban combos email+contraseña filtrados en miles de webs en minutos. La fuerza de tu contraseña no importa: el problema es la REUTILIZACIÓN."
    }
  },
  {
    nombre: "Gestor de contraseñas",
    queEs: "Un programa que GUARDA todas tus contraseñas únicas detrás de UNA contraseña maestra. Puedes tener 50 contraseñas distintas y solo recordar una. Te las rellena automáticamente al iniciar sesión.",
    ejemplo: { tipo: 'bueno', texto: "✅ Bitwarden (gratis), KeePass (gratis), 1Password (de pago). Te genera contraseñas tipo 'xK9#mP2!qL8wV3$' que TÚ no tienes que recordar." },
    senales: [
      "Recuerdas SOLO UNA contraseña (la maestra) y el resto las tienes en el gestor.",
      "Te sale un botón para 'autocompletar' al entrar en Insta, banco, Gmail…",
      "Tu contraseña maestra es una frase de paso súper larga (no es 'gestor123')."
    ],
    miniReto: {
      titulo: "Pruébalo: ¿qué hace tu amigo bien y qué hace mal?",
      opciones: [
        { html: "🗒️ <b>Roberto</b>: tiene un papel pegado en el portátil con todas sus contraseñas porque 'así no se le olvidan'.", correcta: false, explica: "MAL. Cualquiera que mire su pantalla las ve. Un papel es lo PEOR que puede hacer." },
        { html: "🔐 <b>Marta</b>: usa Bitwarden con una frase de paso de 25 caracteres como contraseña maestra.", correcta: true, explica: "PERFECTO. Una sola contraseña memorable + un gestor que guarda el resto. Cero papeles, cero reutilización." },
        { html: "📱 <b>Carlos</b>: guarda todas sus contraseñas en una nota del móvil llamada 'contraseñas'.", correcta: false, explica: "MAL. Si alguien le roba el móvil o se le sincronizan las notas en otro dispositivo, perderá todo. Hay que usar un GESTOR, no las notas." }
      ]
    },
    quiz: {
      p: "¿Por qué un gestor es MÁS seguro que un papel?",
      opciones: [
        "Porque está cifrado y solo tú puedes abrirlo con la maestra",
        "Porque tiene colores",
        "Porque es más moderno",
        "Porque los hackers no usan ordenador"
      ],
      correcta: 0,
      explica: "El gestor cifra tu base de contraseñas. Aunque te roben el archivo, sin tu maestra es ilegible. Un papel lo lee cualquiera que pase por al lado."
    }
  },
  {
    nombre: "Have I Been Pwned",
    queEs: "haveibeenpwned.com es una web GRATIS que te dice si tu email o tu contraseña han aparecido en filtraciones públicas. Si salen → cambia esa contraseña EN TODAS las cuentas donde la usabas, YA.",
    ejemplo: { tipo: 'bueno', texto: "✅ Metes tu email en HIBP y te dice: 'Apareciste en la filtración de LinkedIn 2021'. Vas a LinkedIn, cambias contraseña, activas 2FA y compruebas dónde más usabas esa misma." },
    senales: [
      "Te avisa de qué webs (LinkedIn, Adobe, MyFitnessPal…) filtraron tus datos y CUÁNDO.",
      "Te dice qué datos se filtraron: solo email, también contraseña, también número de tarjeta…",
      "Te recomienda activar 2FA y cambiar la contraseña en los servicios afectados."
    ],
    miniReto: {
      titulo: "Pruébalo: HIBP te devuelve un resultado. ¿Qué haces?",
      opciones: [
        { html: "🔴 <b>Resultado:</b> Tu email + contraseña aparecen en la filtración de Adobe (2013).", correcta: true, explica: "ACTÚA YA. Cambia esa contraseña en Adobe Y en cualquier OTRA cuenta donde la reutilizaras. Activa 2FA donde puedas." },
        { html: "🟢 <b>Resultado:</b> 0 brechas conocidas para tu email.", correcta: false, explica: "Bien, pero no es garantía total: solo significa que no has aparecido en filtraciones PÚBLICAS conocidas. Sigue usando contraseñas únicas y 2FA." },
        { html: "🟡 <b>Resultado:</b> Tu email aparece pero solo se filtró el correo (no la contraseña).", correcta: false, explica: "Es buena señal pero recibirás MÁS spam y phishing dirigidos a ti. No tienes que cambiar contraseña, pero desconfía de emails 'urgentes' que recibas." }
      ]
    },
    quiz: {
      p: "Si HIBP dice que tu email apareció en una filtración con contraseña, ¿qué haces PRIMERO?",
      opciones: [
        "Cambio esa contraseña EN TODAS las cuentas donde la usaba",
        "Cierro la cuenta del email",
        "Llamo a la policía",
        "Espero a ver si me pasa algo"
      ],
      correcta: 0,
      explica: "Cambiar la contraseña filtrada en TODAS las cuentas donde la reutilizabas (por eso es importante no reutilizar). Y activar 2FA donde se pueda."
    }
  },
  {
    nombre: "2FA: la segunda llave",
    queEs: "El 2FA pide una SEGUNDA prueba además de la contraseña: un código por SMS, una app autenticadora, una huella o una llave física. Aunque te roben la contraseña, sin tu móvil no entran.",
    ejemplo: { tipo: 'bueno', texto: "✅ Activas 2FA en Instagram. Un atacante prueba tu contraseña filtrada → la cuenta pide un código que SOLO está en tu móvil → fracaso del atacante." },
    senales: [
      "Lo activas en 'Seguridad' o 'Cuenta' de Insta, Gmail, TikTok, Snapchat, banco…",
      "Las opciones más comunes: SMS, app (Google Authenticator, Authy), huella.",
      "El 2FA por app es MÁS seguro que por SMS (los SMS se pueden interceptar), pero CUALQUIER 2FA es mejor que ninguno."
    ],
    quiz: {
      p: "Tu amigo dice: 'Yo no necesito 2FA porque mi contraseña es muy buena'. ¿Qué le dices?",
      opciones: [
        "Tiene razón, si la contraseña es fuerte es suficiente",
        "Tu contraseña por buena que sea puede acabar filtrada (HIBP). El 2FA es el plan B y se activa en 1 minuto",
        "El 2FA es solo para gente paranoica",
        "Solo lo necesitas para el banco"
      ],
      correcta: 1,
      explica: "El 2FA NO sustituye a una buena contraseña: la complementa. Es el plan B cuando la contraseña falla (porque se filtra, porque te la observan, porque te engañan…). Y se activa en 1 minuto en cada cuenta."
    }
  }
];

// ── DATOS DE SOFÍA (palabras clave que NO debería usar) ─────────
// Cada entrada: [palabra clave, etiqueta del tipo de dato]
// El laboratorio detecta TODOS — incluso los menos obvios (Alba, París, Pelusa, Madrid)
// porque pedagógicamente importante: CUALQUIER dato personal es vulnerabilidad.
const DATOS_SOFIA = [
  // Identidad
  ['sofia', 'nombre'], ['sofía', 'nombre'], ['garcia', 'apellido'], ['garcía', 'apellido'], ['lopez', 'apellido'], ['lópez', 'apellido'],
  // Lugar
  ['granada', 'ciudad'], ['lorca', 'instituto'], ['paris', 'ciudad soñada'], ['parís', 'ciudad soñada'],
  // Familia
  ['alba', 'hermana'], ['diego', 'novio'], ['lucia', 'amiga'], ['lucía', 'amiga'],
  // Mascotas (actual y antigua)
  ['coco', 'perro'], ['pelusa', 'mascota anterior'],
  // Gustos actuales y antiguos
  ['bts', 'grupo favorito'], ['jungkook', 'ídolo'], ['kpop', 'género musical'], ['k-pop', 'género musical'],
  ['onedirection', 'gusto antiguo'], ['one-direction', 'gusto antiguo'], ['harry', 'gusto antiguo'], ['styles', 'gusto antiguo'],
  ['roblox', 'videojuego'], ['manga', 'afición'],
  // Datos clave
  ['2012', 'año nacimiento'], ['marzo', 'mes nacimiento'], ['rosa', 'color favorito'],
  // Otros del perfil
  ['madrid', 'equipo del padre'], ['realmadrid', 'equipo del padre'], ['real-madrid', 'equipo del padre'],
  ['pizza', 'comida favorita'], ['pedro', 'profesor favorito']
];

function tieneDatoSofia(pwd) {
  const low = pwd.toLowerCase();
  return DATOS_SOFIA.some(function(d) { return low.includes(d[0]); });
}

function datosSofiaEncontrados(pwd) {
  const low = pwd.toLowerCase();
  const encontrados = [];
  DATOS_SOFIA.forEach(function(d) {
    if (low.includes(d[0]) && !encontrados.some(function(e) { return e[0] === d[0]; })) encontrados.push(d);
  });
  return encontrados;
}

// ── ESTADO DE TEORÍA ────────────────────────────────────────────
let tarjetaActual = 0;
const microquizContestados = new Set();
const microquizAciertos = new Set();
const miniRetoContestados = new Set();

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
      '<div><span class="concepto-num">CONCEPTO ' + (i + 1) + ' / 6</span>' +
      '<span class="concepto-fase" id="fase-' + i + '">PANTALLA 1 / 3</span></div>' +
      '<h3>' + c.nombre + '</h3>' +
      // Sub-pantalla 1: qué es
      '<div class="subtarjeta" data-sub="0" data-activa="true">' +
        '<p class="que-es">' + c.queEs + '</p>' +
        '<div class="ej ' + c.ejemplo.tipo + '"><span class="et">' +
        (c.ejemplo.tipo === 'bueno' ? '✅ Ejemplo de uso correcto' : '⚠️ Ejemplo peligroso') +
        '</span>' + c.ejemplo.texto + '</div>' +
      '</div>' +
      // Sub-pantalla 2: cómo lo reconoces + miniReto si lo hay
      '<div class="subtarjeta" data-sub="1">' +
        '<div class="reconocer-titulo">🔍 Cómo lo reconoces</div>' +
        '<div class="senales">' +
          c.senales.map(function(s, j) { return '<div class="senal"><b>Señal ' + (j+1) + '</b>' + s + '</div>'; }).join('') +
        '</div>' +
        (c.miniReto ? renderMiniReto(i, c.miniReto) : '') +
      '</div>' +
      // Sub-pantalla 3: microquiz
      '<div class="subtarjeta" data-sub="2">' +
        '<div class="microquiz" data-tarjeta="' + i + '">' +
          '<div class="pregunta-mq">🧠 Comprobación rápida — ' + c.quiz.p + '</div>' +
          '<div class="opciones-mq" id="opcionesMq-' + i + '">' +
            c.quiz.opciones.map(function(op, j) {
              return '<button onclick="responderMicroquiz(' + i + ',' + j + ')">' + String.fromCharCode(65 + j) + '. ' + op + '</button>';
            }).join('') +
          '</div>' +
          '<div class="feedback-mq" id="fb-mq-' + i + '"></div>' +
        '</div>' +
      '</div>' +
      // Navegación interna
      '<div class="nav-sub">' +
        '<button class="btn-acad secundario" onclick="navSub(' + i + ',-1)" id="btn-sub-prev-' + i + '" disabled>◂ Atrás</button>' +
        '<div class="ind"><span class="activa" data-sub="0"></span><span data-sub="1"></span><span data-sub="2"></span></div>' +
        '<button class="btn-acad" onclick="navSub(' + i + ',1)" id="btn-sub-next-' + i + '">Continuar ▸</button>' +
      '</div>' +
    '</article>';
  }).join('');

}

function renderMiniReto(i, mr) {
  return '<div class="mini-reto-teoria" data-tarjeta="' + i + '">' +
    '<div class="titulo-mr">🎯 ' + mr.titulo + '</div>' +
    '<div class="opciones-mr">' +
      mr.opciones.map(function(op, j) {
        return '<button class="opcion-mr" onclick="responderMiniReto(' + i + ',' + j + ')">' + op.html + '</button>';
      }).join('') +
    '</div>' +
    '<div class="feedback-mr" id="fb-mr-' + i + '"></div>' +
  '</div>';
}

function navSub(tarjetaIdx, delta) {
  const tarjeta = document.querySelector('.tarjeta-teoria[data-idx="' + tarjetaIdx + '"]');
  const subs = tarjeta.querySelectorAll('.subtarjeta');
  let actual = -1;
  subs.forEach(function(s, i) { if (s.dataset.activa === 'true') actual = i; });
  const nuevo = actual + delta;
  if (nuevo < 0) return;
  if (nuevo > 2) {
    if (microquizContestados.has(tarjetaIdx)) { if (tarjetaIdx === CONCEPTOS.length - 1) Academia.irABloque('entrenamiento'); else navTarjeta(1); }
    return;
  }
  subs.forEach(function(s) { s.dataset.activa = 'false'; });
  subs[nuevo].dataset.activa = 'true';
  const inds = tarjeta.querySelectorAll('.nav-sub .ind span');
  inds.forEach(function(ind, i) {
    ind.classList.remove('activa', 'completada');
    if (i === nuevo) ind.classList.add('activa');
    else if (i < nuevo) ind.classList.add('completada');
  });
  document.getElementById('fase-' + tarjetaIdx).textContent = 'PANTALLA ' + (nuevo + 1) + ' / 3';
  document.getElementById('btn-sub-prev-' + tarjetaIdx).disabled = nuevo === 0;
  const btnNext = document.getElementById('btn-sub-next-' + tarjetaIdx);
  if (nuevo === 2) {
    btnNext.textContent = !microquizContestados.has(tarjetaIdx) ? '🔒 Responde el microquiz' : (tarjetaIdx === CONCEPTOS.length - 1 ? 'A entrenar ▸' : 'Siguiente concepto ▸');
    btnNext.disabled = !microquizContestados.has(tarjetaIdx);
  } else {
    btnNext.textContent = 'Continuar ▸';
    btnNext.disabled = false;
  }
}

function navTarjeta(delta) { irATarjeta(tarjetaActual + delta); }

function irATarjeta(idx) {
  if (idx < 0 || idx >= CONCEPTOS.length) return;
  document.querySelectorAll('.tarjeta-teoria').forEach(function(t) { t.dataset.activa = 'false'; });
  document.querySelector('.tarjeta-teoria[data-idx="' + idx + '"]').dataset.activa = 'true';
  tarjetaActual = idx;
  const tarjeta = document.querySelector('.tarjeta-teoria[data-idx="' + idx + '"]');
  const subs = tarjeta.querySelectorAll('.subtarjeta');
  subs.forEach(function(s, i) { s.dataset.activa = (i === 0 ? 'true' : 'false'); });
  const inds = tarjeta.querySelectorAll('.nav-sub .ind span');
  inds.forEach(function(ind, i) { ind.classList.remove('activa', 'completada'); if (i === 0) ind.classList.add('activa'); });
  document.getElementById('fase-' + idx).textContent = 'PANTALLA 1 / 3';
  document.getElementById('btn-sub-prev-' + idx).disabled = true;
  document.getElementById('btn-sub-next-' + idx).textContent = 'Continuar ▸';
  document.getElementById('btn-sub-next-' + idx).disabled = false;
  document.querySelectorAll('.puntos-tarjetas .punto').forEach(function(p, i) {
    p.classList.remove('activo', 'visto');
    if (i === idx) p.classList.add('activo');
    else if (microquizContestados.has(i)) p.classList.add('visto');
  });
  if (idx === CONCEPTOS.length - 1 && microquizContestados.has(idx)) {
    otorgarInsignia('cadete');
  }
  document.querySelector('.tarjetas-teoria').scrollIntoView({ behavior: 'smooth', block: 'start' });
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

function responderMiniReto(idxTarjeta, idxOp) {
  if (miniRetoContestados.has(idxTarjeta)) return;
  miniRetoContestados.add(idxTarjeta);
  const c = CONCEPTOS[idxTarjeta];
  if (!c.miniReto) return;
  const op = c.miniReto.opciones[idxOp];
  const botones = document.querySelectorAll('.mini-reto-teoria[data-tarjeta="' + idxTarjeta + '"] .opcion-mr');
  botones.forEach(function(b, i) {
    b.disabled = true;
    if (c.miniReto.opciones[i].correcta) b.classList.add('correcta');
    else if (i === idxOp) b.classList.add('incorrecta');
  });
  const fb = document.getElementById('fb-mr-' + idxTarjeta);
  fb.className = 'feedback-mr ' + (op.correcta ? 'bien' : 'mal');
  fb.innerHTML = (op.correcta ? '✅ ' : '❌ ') + op.explica;
  fb.dataset.activo = 'true';
}

// ── BLOQUE 3 NIVEL 1: EMPAREJAR ─────────────────────────────────
const PARES = [
  { t: "Usar la misma contraseña en Insta, TikTok y Gmail", d: "Reutilización (mala práctica)" },
  { t: "Activar el SMS de verificación en Discord", d: "2FA (buena práctica)" },
  { t: "Comprobar tu email en haveibeenpwned.com", d: "Verificación de filtración (buena práctica)" },
  { t: "Tener un papel pegado al portátil con todas tus contraseñas", d: "Lugar inseguro (mala práctica)" },
  { t: "Usar 'caballo-mesa-luna-puente-83'", d: "Frase de paso (buena práctica)" },
  { t: "Usar 'lucia2012' (nombre + año)", d: "Datos personales (mala práctica)" }
];

let entSeleccionado = null;
let entAciertos = 0, entFallos = 0;
const entResueltos = new Set();

function renderEntrenamiento() {
  const terminos = PARES.map(function(p, i) { return Object.assign({}, p, { idx: i }); }).sort(function() { return Math.random() - 0.5; });
  const defs = PARES.map(function(p, i) { return Object.assign({}, p, { idx: i }); }).sort(function() { return Math.random() - 0.5; });
  document.getElementById('col-terminos').innerHTML = terminos.map(function(p) {
    return '<button class="item-ent" data-tipo="termino" data-idx="' + p.idx + '" onclick="elegirEnt(this)" style="width:100%;text-align:left;margin-bottom:6px;padding:11px 14px;font-family:var(--sans);font-size:.88rem;background:#fff;border:1px solid var(--bd);border-radius:6px;cursor:pointer;color:var(--texto);line-height:1.4;transition:.15s">' + p.t + '</button>';
  }).join('');
  document.getElementById('col-definiciones').innerHTML = defs.map(function(p) {
    return '<button class="item-ent" data-tipo="def" data-idx="' + p.idx + '" onclick="elegirEnt(this)" style="width:100%;text-align:left;margin-bottom:6px;padding:11px 14px;font-family:var(--cond);font-size:.92rem;background:#fff;border:1px solid var(--bd);border-radius:6px;cursor:pointer;letter-spacing:.5px;color:var(--acad-azul-mar);font-weight:600;transition:.15s">' + p.d + '</button>';
  }).join('');
  document.getElementById('ent-aciertos').textContent = '0';
  document.getElementById('ent-fallos').textContent = '0';
  document.getElementById('ent-restantes').textContent = PARES.length;
  document.getElementById('btn-a-nivel2').disabled = true;
}

function elegirEnt(btn) {
  if (btn.classList.contains('resuelto')) return;
  const tipo = btn.dataset.tipo;
  const idx = parseInt(btn.dataset.idx);
  if (entSeleccionado && entSeleccionado.btn === btn) {
    resetEstilo(btn);
    entSeleccionado = null;
    return;
  }
  if (!entSeleccionado) {
    marcarSeleccionado(btn);
    entSeleccionado = { tipo: tipo, idx: idx, btn: btn };
    return;
  }
  if (entSeleccionado.tipo === tipo) {
    resetEstilo(entSeleccionado.btn);
    marcarSeleccionado(btn);
    entSeleccionado = { tipo: tipo, idx: idx, btn: btn };
    return;
  }
  if (entSeleccionado.idx === idx) {
    entAciertos++;
    entResueltos.add(idx);
    [entSeleccionado.btn, btn].forEach(function(b) {
      b.style.background = 'var(--acad-verde-cl)';
      b.style.color = 'var(--acad-verde)';
      b.style.borderColor = 'var(--acad-verde)';
      b.classList.add('resuelto');
      b.style.cursor = 'default';
    });
    Academia.mostrarFeedback(document.getElementById('fb-entrenamiento'), 'bien',
      '<span class="et">✅ Bien</span>Has emparejado "<strong>' + PARES[idx].t + '</strong>" con su concepto.');
  } else {
    entFallos++;
    const a = entSeleccionado.btn, b = btn;
    [a, b].forEach(function(x) {
      x.style.background = '#FCEAE7';
      x.style.color = 'var(--acad-rojo)';
      x.style.borderColor = 'var(--acad-rojo)';
    });
    setTimeout(function() {
      [a, b].forEach(function(x) { if (!x.classList.contains('resuelto')) resetEstilo(x); });
    }, 1100);
    Academia.mostrarFeedback(document.getElementById('fb-entrenamiento'), 'mal',
      '<span class="et">❌ No es ese par</span>Lee con calma y vuelve a probar.');
  }
  entSeleccionado = null;
  document.getElementById('ent-aciertos').textContent = entAciertos;
  document.getElementById('ent-fallos').textContent = entFallos;
  document.getElementById('ent-restantes').textContent = PARES.length - entAciertos;
  if (entAciertos === PARES.length) {
    Academia.mostrarFeedback(document.getElementById('fb-entrenamiento'), 'bien',
      '<span class="et">🎉 Nivel 1 completado</span>' + PARES.length + ' pares con ' + entFallos + ' fallos. Vamos al nivel 2.');
    document.getElementById('btn-a-nivel2').disabled = false;
  }
}

function resetEstilo(btn) { btn.style.background = ''; btn.style.color = ''; btn.style.borderColor = ''; }
function marcarSeleccionado(btn) { btn.style.background = 'var(--acad-violeta)'; btn.style.color = '#fff'; btn.style.borderColor = 'var(--acad-violeta)'; }

// ── BLOQUE 3 NIVEL 2: V/F ───────────────────────────────────────
const FRASES_VF = [
  { texto: "Si una contraseña tiene símbolos raros (@#$%), ya es segura por sí sola.", correcta: false,
    explica: "Falso. La LONGITUD es lo que más importa. 'P@ss1!' cae en segundos. 'caballo-mesa-luna-puente' tarda millones de años aunque solo use minúsculas." },
  { texto: "Usar la MISMA contraseña en varias cuentas multiplica el riesgo si una se filtra.", correcta: true,
    explica: "Verdadero. Si una se filtra, los atacantes prueban tu email + esa contraseña en cientos de webs (credential stuffing). Cada cuenta que la reutilice cae." },
  { texto: "Un gestor de contraseñas como Bitwarden es MENOS seguro que apuntarlas en un papel.", correcta: false,
    explica: "Falso. El gestor cifra tu base con tu maestra; el papel lo lee cualquiera. Además el gestor te genera contraseñas únicas que tú no tienes que recordar." },
  { texto: "El 2FA por SMS es mejor que NO tener 2FA.", correcta: true,
    explica: "Verdadero. El SMS no es lo ideal (se puede interceptar) pero CUALQUIER 2FA es mejor que ninguno. Las apps tipo Authy o Google Authenticator son aún mejores." },
  { texto: "Si HIBP dice '0 resultados', mi contraseña es segura para siempre.", correcta: false,
    explica: "Falso. Solo significa que NO has aparecido en filtraciones PÚBLICAS conocidas. Mañana puede aparecer una nueva. Sigue usando contraseñas únicas y 2FA." },
  { texto: "Una frase de 5 palabras corrientes unidas con guiones es más fuerte que 'P@ss1!'.", correcta: true,
    explica: "Verdadero. La longitud manda. 'naranja-tractor-luna-puente-violeta' tarda miles de millones de años. 'P@ss1!' cae en segundos." }
];
let vfActuales = [];
let vfAciertos = 0, vfFallos = 0;
const vfContestadas = new Set();

function mostrarNivel2() {
  document.getElementById('zona-nivel1').style.display = 'none';
  document.getElementById('zona-nivel2').style.display = 'block';
  if (vfActuales.length === 0) renderNivel2();
}
function volverANivel1() {
  document.getElementById('zona-nivel2').style.display = 'none';
  document.getElementById('zona-nivel1').style.display = 'block';
}
function renderNivel2() {
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

// ── BLOQUE 4 PARTE A0: RANKING DE CONTRASEÑAS (CALENTAMIENTO) ───
const PWD_RANKING = [
  { pwd: "Sofia2012", explica: "PEOR. Solo 9 caracteres y contiene nombre + año de nacimiento. Cae en menos de 1 segundo." },
  { pwd: "Diego7", explica: "Casi igual de mal. 6 caracteres + nombre del novio + número favorito. Un atacante que la conozca la prueba la primera." },
  { pwd: "CocoRoblox!", explica: "Algo mejor (11 chars + símbolo) pero sigue usando datos suyos (nombre del perro + videojuego favorito). Vulnerable a ataque dirigido." },
  { pwd: "Luna-tren-rio-cielo-42", explica: "BIEN. 22 caracteres, frase de paso sin datos personales. Tardaría siglos en romperse por fuerza bruta." },
  { pwd: "planeta-silla-radar-88-violeta", explica: "MEJOR. 30 caracteres, palabras corrientes sin relación entre sí, sin datos personales. Prácticamente imposible." }
];
let ordenRanking = []; // índices originales en el orden actual
let rankingValidado = false;

function renderRanking() {
  // Empezamos con un orden aleatorio
  ordenRanking = PWD_RANKING.map(function(_, i) { return i; }).sort(function() { return Math.random() - 0.5; });
  rankingValidado = false;
  pintarRanking();
  document.getElementById('btn-comprobar-rank').disabled = false;
  document.getElementById('resultado-ranking').dataset.activo = 'false';
  document.getElementById('resultado-ranking').innerHTML = '';
  document.getElementById('barra-fin-rank').style.display = 'none';
}

function pintarRanking() {
  const cont = document.getElementById('lista-ranking');
  cont.innerHTML = ordenRanking.map(function(idx, pos) {
    const item = PWD_RANKING[idx];
    return '<div class="item-ranking" data-idx="' + idx + '">' +
      '<div class="pos">' + (pos + 1) + '</div>' +
      '<div class="pwd-rank">' + item.pwd + '</div>' +
      '<div class="botones-mover">' +
        '<button onclick="moverRanking(' + pos + ',-1)" ' + (pos === 0 || rankingValidado ? 'disabled' : '') + ' title="Subir">▲</button>' +
        '<button onclick="moverRanking(' + pos + ',1)" ' + (pos === ordenRanking.length - 1 || rankingValidado ? 'disabled' : '') + ' title="Bajar">▼</button>' +
      '</div>' +
    '</div>';
  }).join('');
}

function moverRanking(pos, delta) {
  const nueva = pos + delta;
  if (nueva < 0 || nueva >= ordenRanking.length) return;
  const tmp = ordenRanking[pos];
  ordenRanking[pos] = ordenRanking[nueva];
  ordenRanking[nueva] = tmp;
  pintarRanking();
}

function comprobarRanking() {
  rankingValidado = true;
  // El orden correcto es 0,1,2,3,4 (PWD_RANKING ya está en orden de peor a mejor)
  let correctos = 0;
  ordenRanking.forEach(function(idx, pos) {
    if (idx === pos) correctos++;
  });

  // Marcar visualmente
  const items = document.querySelectorAll('.item-ranking');
  items.forEach(function(el, pos) {
    const idx = parseInt(el.dataset.idx);
    el.classList.add(idx === pos ? 'correcto-orden' : 'incorrecto-orden');
  });

  // Mostrar explicación del orden correcto
  const res = document.getElementById('resultado-ranking');
  const titulo = correctos === 5
    ? '🏆 ¡Orden perfecto! Has captado lo esencial: longitud > datos personales.'
    : correctos >= 3
      ? '✅ Cerca: ' + correctos + ' / 5 en su sitio. Mira el orden correcto:'
      : '⚠️ Vuelve a leer la teoría sobre longitud y datos personales. ' + correctos + ' / 5 en su sitio.';

  let html = '<h4 style="font-family:var(--cond);color:var(--acad-azul-mar);margin-bottom:10px">' + titulo + '</h4>';
  html += '<p style="font-size:.9rem;color:var(--texto2);margin-bottom:10px"><strong>Orden correcto de peor a mejor:</strong></p>';
  PWD_RANKING.forEach(function(item, i) {
    html += '<div class="item-explica ' + (i < 3 ? 'mal' : 'bien') + '"><b>' + (i + 1) + '. ' + item.pwd + '</b><br>' + item.explica + '</div>';
  });
  res.innerHTML = html;
  res.dataset.activo = 'true';
  document.getElementById('btn-comprobar-rank').disabled = true;
  document.getElementById('barra-fin-rank').style.display = 'flex';
  // Deshabilitar botones de mover
  pintarRanking();

  Academia.setSesion(SESION_ID, { rankingCorrectos: correctos });
}

function reiniciarRanking() {
  renderRanking();
}

function mostrarParteA() {
  document.getElementById('zona-parteA0').style.display = 'none';
  document.getElementById('zona-parteA').style.display = 'block';
}

// ── BLOQUE 4 PARTE A: HACKEA A SOFÍA ────────────────────────────
const COMUNES = ['123456','12345678','password','qwerty','111111','abc123','fortnite','iloveyou','hola','admin','contraseña'];
let pwdSofProbadas = 0;
let puntosVulnerabilidad = 0;
const pwdSofiaResultados = [];

function renderPwdSofia() {
  const cont = document.getElementById('zona-pwd-sofia');
  let html = '';
  for (let i = 1; i <= 5; i++) {
    html += '<div class="mini-lab-teoria" style="margin-top:10px" data-num="' + i + '">' +
      '<div class="titulo-ml">Intento ' + i + ' / 5 — Inventa una contraseña que Sofía usaría</div>' +
      '<div class="input-pwd">' +
        '<input type="text" id="pwd-sof-' + i + '" placeholder="Una contraseña que Sofía PROBABLEMENTE usaría...">' +
        '<button class="btn-comprobar-pwd" onclick="probarPwdSofia(' + i + ')">Probar</button>' +
      '</div>' +
      '<div class="resultado-pwd" id="pwd-sof-res-' + i + '"></div>' +
    '</div>';
  }
  cont.innerHTML = html;
}

function probarPwdSofia(num) {
  const input = document.getElementById('pwd-sof-' + num);
  const pwd = input.value.trim();
  if (pwd.length === 0) return;
  if (pwdSofiaResultados[num - 1]) return;
  const cont = document.getElementById('pwd-sof-res-' + num);
  const datosEncontrados = datosSofiaEncontrados(pwd);
  const datoSofia = datosEncontrados.length > 0;
  const esComun = COMUNES.some(function(c) { return pwd.toLowerCase().includes(c); });
  const esCorta = pwd.length < 12;
  const soloLetras = /^[a-zA-Z]+$/.test(pwd);
  const soloNumeros = /^[0-9]+$/.test(pwd);

  // ─ Badges de vulnerabilidad ─
  const vulns = [];
  if (datosEncontrados.length > 0) {
    datosEncontrados.forEach(function(d) {
      vulns.push('🚨 ' + d[1].toUpperCase() + ' (' + d[0] + ')');
    });
  }
  if (esComun) vulns.push('🚨 Contraseña común');
  if (esCorta) vulns.push('🚨 Demasiado corta');
  if (soloLetras) vulns.push('🚨 Solo letras');
  if (soloNumeros) vulns.push('🚨 Solo números');

  // ─ Tiempo de craqueo ─
  let alfabeto = 0;
  if (/[a-z]/.test(pwd)) alfabeto += 26;
  if (/[A-Z]/.test(pwd)) alfabeto += 26;
  if (/[0-9]/.test(pwd)) alfabeto += 10;
  if (/[^a-zA-Z0-9]/.test(pwd)) alfabeto += 32;
  if (alfabeto === 0) alfabeto = 26;
  const combinaciones = Math.pow(alfabeto, pwd.length) / 2;
  let segundos = combinaciones / 1e11;
  if (esComun) segundos = 0.001;
  if (datoSofia) segundos = Math.min(segundos, 60);

  let tiempoTexto;
  if (segundos < 60) tiempoTexto = (segundos < 1 ? 'Menos de 1 segundo' : Math.round(segundos) + ' segundos');
  else if (segundos < 3600) tiempoTexto = Math.round(segundos / 60) + ' minutos';
  else if (segundos < 86400) tiempoTexto = Math.round(segundos / 3600) + ' horas';
  else if (segundos < 86400 * 365) tiempoTexto = Math.round(segundos / 86400) + ' días';
  else if (segundos < 86400 * 365 * 100) tiempoTexto = Math.round(segundos / 86400 / 365) + ' años';
  else tiempoTexto = 'miles de años';

  // ─ Puntuación ─
  let puntos = 0;
  let veredicto, comentario;
  if (datoSofia && segundos < 60) {
    puntos = 1;
    veredicto = '🎯 +1 punto — VULNERABILIDAD CONFIRMADA';
    comentario = 'Sofía PROBABLEMENTE usaría esto (contiene datos suyos) Y un atacante que la conoce la rompería en segundos.';
  } else if (datoSofia) {
    puntos = 0.5;
    veredicto = '🟡 +0.5 puntos — Vulnerabilidad parcial';
    comentario = 'Sofía podría usarlo (contiene datos suyos) pero tardarías ' + tiempoTexto + ' en romperlo.';
  } else if (esComun) {
    puntos = 1;
    veredicto = '🎯 +1 punto — Contraseña comunísima';
    comentario = 'No contiene datos de Sofía pero es una contraseña SUPER común. Cualquier atacante la probaría la primera.';
  } else {
    puntos = 0;
    veredicto = '❌ 0 puntos — Esto no es algo que Sofía usaría';
    comentario = 'No contiene NADA de su vida (BTS, Coco, Diego, Granada, 2012, Alba, París…). Sofía no la habría puesto.';
  }
  puntosVulnerabilidad += puntos;
  pwdSofiaResultados[num - 1] = { pwd: pwd, puntos: puntos, tiempo: tiempoTexto, vulns: vulns };

  // ─ Render ─
  const badgesHtml = vulns.length > 0
    ? '<div class="badges-vuln">' + vulns.map(function(v) { return '<span class="badge-vuln">' + v + '</span>'; }).join('') + '</div>'
    : '<div class="badges-vuln"><span class="badge-vuln ok">✅ Sin vulnerabilidades obvias</span></div>';

  cont.innerHTML =
    '<h4 style="font-family:var(--cond);color:var(--acad-azul-mar);margin-bottom:8px">' + veredicto + '</h4>' +
    '<p style="font-size:.92rem;color:var(--texto);margin-bottom:8px">' + comentario + '</p>' +
    '<div style="font-size:.82rem;color:var(--t2);font-family:var(--cond);text-transform:uppercase;letter-spacing:1px;margin-bottom:4px">Vulnerabilidades detectadas:</div>' +
    badgesHtml +
    '<div class="tiempo-pwd" style="margin-top:8px">⏱ Tiempo estimado para romperla: <b>' + tiempoTexto + '</b></div>';
  cont.dataset.activo = 'true';
  input.disabled = true;

  pwdSofProbadas++;
  document.getElementById('pwd-sof-actual').textContent = pwdSofProbadas;
  document.getElementById('hud-vuln').textContent = puntosVulnerabilidad;
  if (pwdSofProbadas === 5) {
    document.getElementById('btn-a-parteB').disabled = false;
  }
}

// ── BLOQUE 4 PARTE B: TU CONTRASEÑA PARA SOFÍA ──────────────────
let parteB_completada = false;

function alternarVisibilidadGuardian() {
  const input = document.getElementById('pwd-guardian-input');
  if (!input) return;
  input.type = input.type === 'password' ? 'text' : 'password';
}

function comprobarPwdGuardian() {
  const input = document.getElementById('pwd-guardian-input');
  const pwd = input.value.trim();
  if (pwd.length === 0) return;
  const cont = document.getElementById('pwd-guardian-resultado');
  const longitud = pwd.length;
  const checkLong = longitud >= 15;
  const datoSofia = tieneDatoSofia(pwd);
  const esComun = COMUNES.some(function(c) { return pwd.toLowerCase().includes(c); });
  const checkPersonal = !datoSofia;
  const checkComun = !esComun;

  let alfabeto = 0;
  if (/[a-z]/.test(pwd)) alfabeto += 26;
  if (/[A-Z]/.test(pwd)) alfabeto += 26;
  if (/[0-9]/.test(pwd)) alfabeto += 10;
  if (/[^a-zA-Z0-9]/.test(pwd)) alfabeto += 32;
  if (alfabeto === 0) alfabeto = 26;
  const segundos = Math.pow(alfabeto, longitud) / 2 / 1e11;
  const checkTiempo = segundos > 86400 * 365 * 100; // > 100 años

  let tiempoTexto;
  if (segundos < 60) tiempoTexto = 'Menos de 1 minuto';
  else if (segundos < 3600) tiempoTexto = Math.round(segundos / 60) + ' minutos';
  else if (segundos < 86400) tiempoTexto = Math.round(segundos / 3600) + ' horas';
  else if (segundos < 86400 * 365) tiempoTexto = Math.round(segundos / 86400) + ' días';
  else if (segundos < 86400 * 365 * 100) tiempoTexto = Math.round(segundos / 86400 / 365) + ' años';
  else if (segundos < 86400 * 365 * 1e6) tiempoTexto = 'miles de años';
  else tiempoTexto = 'más tiempo del que existe el universo';

  const checks = [checkLong, checkPersonal, checkComun, checkTiempo].filter(Boolean).length;
  const nivel = Math.min(5, checks + 1);
  const todosPasan = checks === 4;

  if (todosPasan) parteB_completada = true;

  cont.innerHTML =
    '<h4 style="font-family:var(--cond);color:' + (todosPasan ? 'var(--acad-verde)' : 'var(--acad-rojo)') + ';margin-bottom:8px">' +
    (todosPasan ? '🛡️ ¡PERFECTA! Sofía estaría a salvo.' : '⚠️ Aún no es suficiente. Mira qué falta.') + '</h4>' +
    '<div class="barra-fuerza"><div class="relleno" data-nivel="' + nivel + '"></div></div>' +
    '<div class="check-pwd ' + (checkLong ? 'pasa' : 'falla') + '"><span class="icon"></span> Longitud: <b>' + longitud + ' caracteres</b> ' + (checkLong ? '(perfecto)' : '(necesita 15+)') + '</div>' +
    '<div class="check-pwd ' + (checkPersonal ? 'pasa' : 'falla') + '"><span class="icon"></span> No contiene datos de Sofía ' + (!checkPersonal ? '(¡tiene algo suyo!)' : '') + '</div>' +
    '<div class="check-pwd ' + (checkComun ? 'pasa' : 'falla') + '"><span class="icon"></span> No es una contraseña común</div>' +
    '<div class="check-pwd ' + (checkTiempo ? 'pasa' : 'falla') + '"><span class="icon"></span> Tarda más de 100 años en romperse</div>' +
    '<div class="tiempo-pwd">⏱ Un atacante tardaría: <b>' + tiempoTexto + '</b></div>' +
    (todosPasan
      ? '<p style="font-size:.88rem;color:var(--acad-verde);margin-top:10px;font-weight:600">🎉 Has diseñado una contraseña que protegería a Sofía DURANTE TODA SU VIDA. Pasa al modo auditoría personal.</p>'
      : '<p style="font-size:.85rem;color:var(--t2);margin-top:10px">Vuelve a intentarlo. Recuerda: 15+ caracteres, frase memorable PARA ELLA pero sin sus datos públicos, y poco común.</p>');
  cont.dataset.activo = 'true';

  if (todosPasan) {
    document.getElementById('btn-a-parteC').disabled = false;
    Academia.setSesion(SESION_ID, { pwd_guardian_ok: true, pwd_guardian_intentos: (Academia.getSesion(SESION_ID).pwd_guardian_intentos || 0) + 1 });
  } else {
    Academia.setSesion(SESION_ID, { pwd_guardian_intentos: (Academia.getSesion(SESION_ID).pwd_guardian_intentos || 0) + 1 });
  }
}

function mostrarParteB() {
  document.getElementById('zona-parteA').style.display = 'none';
  document.getElementById('zona-parteB').style.display = 'block';
  document.getElementById('zona-parteC').style.display = 'none';
}
function volverAParteA() {
  document.getElementById('zona-parteA').style.display = 'block';
  document.getElementById('zona-parteB').style.display = 'none';
}
function mostrarParteC() {
  document.getElementById('zona-parteA').style.display = 'none';
  document.getElementById('zona-parteB').style.display = 'none';
  document.getElementById('zona-parteC').style.display = 'block';
}

// ── BLOQUE 4 PARTE C: AUDITORÍA PERSONAL ────────────────────────
function auditarMisCuentas() {
  const n = parseInt(document.getElementById('num-cuentas').value);
  const r = parseInt(document.getElementById('num-reutilizadas').value);
  if (isNaN(n) || isNaN(r) || n < 0 || r < 0) return;
  if (r > n) { alert('No puede haber más cuentas reutilizadas que cuentas totales.'); return; }
  const cont = document.getElementById('audit-resultado');
  const porcentaje = n > 0 ? Math.round((r / n) * 100) : 0;
  // 4 niveles tipo semáforo
  let nivelClase, emoji, badge, titulo, descripcion, accion;
  if (porcentaje <= 10) {
    nivelClase = 'verde'; emoji = '🛡️'; badge = 'Nivel Verde';
    titulo = 'Excelente higiene digital';
    descripcion = 'Casi todas tus cuentas son únicas. Tienes una de las mejores prácticas posibles.';
    accion = 'Sigue así. Si todavía no usas un gestor (Bitwarden, KeePass), considera instalarlo: te facilitará seguir teniendo contraseñas únicas a medida que crezca el número de cuentas.';
  } else if (porcentaje <= 30) {
    nivelClase = 'amarillo'; emoji = '🟡'; badge = 'Nivel Amarillo';
    titulo = 'Bien, pero con margen';
    descripcion = 'La mayoría de tus cuentas son únicas, pero hay unas pocas reutilizadas. Una filtración en una de ellas afectaría a varias.';
    accion = 'Identifica esas ' + r + ' cuentas y dales contraseña única esta semana. Empieza por las MÁS importantes (email principal, banco, Insta).';
  } else if (porcentaje <= 50) {
    nivelClase = 'naranja'; emoji = '🟠'; badge = 'Nivel Naranja';
    titulo = 'Cuidado: riesgo medio';
    descripcion = 'Usas la misma contraseña en una proporción significativa de tus cuentas. Si UNA se filtra, ' + r + ' cuentas tuyas caerían automáticamente.';
    accion = 'Plan en 3 pasos: (1) comprueba tu email en haveibeenpwned.com, (2) cambia la contraseña del email principal y del banco, (3) instala un gestor para no caer otra vez.';
  } else {
    nivelClase = 'rojo'; emoji = '🔴'; badge = 'Nivel Rojo';
    titulo = '¡Acción urgente!';
    descripcion = 'La mayoría de tus cuentas comparten contraseña. Si UNA se filtra (cosa que pasa cada mes en alguna web grande), un atacante entra en ' + r + ' cuentas tuyas en minutos.';
    accion = 'Esta semana, sin falta: (1) instala Bitwarden o un gestor similar, (2) cambia la contraseña del email principal, (3) cambia la del banco si tienes, (4) activa 2FA en ambas. Después, ve cambiando el resto con calma.';
  }

  cont.innerHTML =
    '<p style="font-size:.95rem;color:var(--texto);margin-bottom:10px">Tienes <b>' + n + '</b> cuentas. Reutilizas la misma contraseña en <b>' + r + '</b> (' + porcentaje + '%).</p>' +
    '<div class="nivel-riesgo ' + nivelClase + '">' +
      '<div class="nivel-emoji">' + emoji + '</div>' +
      '<div class="nivel-texto">' +
        '<span class="nivel-badge">' + badge + '</span>' +
        '<h4>' + titulo + '</h4>' +
        '<p>' + descripcion + '</p>' +
      '</div>' +
    '</div>' +
    '<div class="tiempo-pwd">💡 <b>Plan de acción concreto:</b> ' + accion + '</div>';
  cont.dataset.activo = 'true';

  Academia.setSesion(SESION_ID, {
    cuentas: n, reutilizadas: r, porcentaje: porcentaje,
    puntosVulnerabilidad: puntosVulnerabilidad,
    pwdSofProbadas: pwdSofProbadas, parteB_completada: parteB_completada,
    entAciertos: entAciertos, entFallos: entFallos,
    vfAciertos: vfAciertos, vfFallos: vfFallos,
    microquizAciertos: microquizAciertos.size, microquizTotal: CONCEPTOS.length,
    tiempoMin: Math.round((Date.now() - tInicio) / 60000)
  });
  document.getElementById('barra-fin-juego').style.display = 'flex';
  otorgarInsignia('investigador');
}

// MINI-INSIGNIAS
const insigniasGanadas = new Set();
function otorgarInsignia(nombre) {
  if (insigniasGanadas.has(nombre)) return;
  insigniasGanadas.add(nombre);
  const el = document.querySelector('.mi-insignia[data-mi="' + nombre + '"]');
  if (el) el.dataset.ganada = 'true';
  const nombres = { cadete: 'Cadete', analista: 'Analista', investigador: 'Investigador', detective: 'Centinela' };
  const emojis = { cadete: '🎖️', analista: '🎖️', investigador: '🎖️', detective: '🏆' };
  mostrarToast('Has ganado la insignia', emojis[nombre] + ' ' + nombres[nombre]);
  Academia.setSesion(SESION_ID, { ['insignia_' + nombre]: true });
}
function mostrarToast(titulo, nombre) {
  const t = document.createElement('div');
  t.className = 'toast-insignia';
  t.innerHTML = '<div class="emoji">🏅</div><div><div class="titulo">' + titulo + '</div><div class="nombre">' + nombre + '</div></div>';
  document.body.appendChild(t);
  setTimeout(function() { t.remove(); }, 4200);
}

// INFORME
function contarPalabras(texto) { return (texto.trim().match(/\S+/g) || []).length; }

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
    Academia.mostrarFeedback(document.getElementById('fb-informe'), 'mal',
      '<span class="et">❌ Informe incompleto</span>Necesitas responder de verdad, no con letras sueltas.' + detalle);
    return;
  }
  const datos = Academia.getSesion(SESION_ID);
  const totalPuntos = (datos.puntosVulnerabilidad || 0) + (datos.parteB_completada ? 5 : 0);
  const totalPosible = 10;
  Academia.marcarCompletada(SESION_ID, totalPuntos, totalPosible);
  Academia.setSesion(SESION_ID, { q1: q1, q2: q2, q3: q3, informeCompletado: true });

  document.getElementById('res-teoria').textContent = (datos.microquizAciertos || 0) + ' / ' + (datos.microquizTotal || 6) + ' microquiz';
  document.getElementById('res-entrenamiento').textContent = (datos.entAciertos || 0) + ' pares · ' + (datos.vfAciertos || 0) + ' V/F';
  document.getElementById('res-reto').textContent = totalPuntos + ' / ' + totalPosible + ' puntos';
  document.getElementById('res-tiempo').textContent = (datos.tiempoMin || 0) + ' min';
  const porcentaje = Math.round((totalPuntos / totalPosible) * 100);
  const calif = porcentaje >= 80 ? '🏆 Excelente' : porcentaje >= 60 ? '⭐ Notable' : porcentaje >= 40 ? '👍 Suficiente' : '📚 A repasar';
  document.getElementById('res-calif').textContent = calif;
  document.getElementById('insignia-texto').textContent = 'Centinela de Contraseñas';
  const cod = Academia.codigoFinalizacion(SESION_ID, totalPuntos);
  document.getElementById('cod-final').textContent = 'CÓDIGO: ' + cod;
  Academia.setSesion(SESION_ID, { codigo: cod, calificacion: calif, insignia: 'Centinela de Contraseñas' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}

function descargarInsignia() {
  const datos = Academia.getSesion(SESION_ID);
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const totalPuntos = (datos.puntosVulnerabilidad || 0) + (datos.parteB_completada ? 5 : 0);
  Academia.descargarDiploma({
    titulo: 'Centinela de Contraseñas',
    subtitulo: 'Sesión 2 · Contraseñas · Promoción 2026',
    icono: '🔐',
    nombres: [n1, n2],
    sesionNum: 'S2',
    score: totalPuntos,
    total: 10,
    codigo: datos.codigo,
    frase: 'La cerradura no protege si la llave está en el felpudo'
  }, 'S02-contrasenas-' + n1.replace(/\s/g, '_') + '.png');
}

// INICIALIZACIÓN
window.addEventListener('DOMContentLoaded', function() {
  renderTarjetas();
  renderEntrenamiento();
  renderRanking();
  renderPwdSofia();

  // Continuidad S1 -> S2
  const s1 = Academia.getSesion('s01');
  if (s1 && s1.q3 && s1.q3.trim().length > 0) {
    document.getElementById('cita-s1').textContent = '"' + s1.q3 + '"';
    document.getElementById('continuidad-s1').style.display = 'block';
  }

  // Restaurar informe
  const datos = Academia.getSesion(SESION_ID);
  ['q1', 'q2', 'q3'].forEach(function(q) {
    if (datos[q]) {
      const ta = document.getElementById('inf-' + q);
      if (ta) {
        ta.value = datos[q];
        document.getElementById('cnt-' + q).textContent = contarPalabras(datos[q]) + ' palabras';
      }
    }
  });

  document.querySelectorAll('.informe-pregunta textarea').forEach(function(ta) {
    ta.addEventListener('input', function() {
      const palabras = contarPalabras(ta.value);
      document.getElementById('cnt-' + ta.dataset.q).textContent = palabras + ' palabras';
      Academia.setSesion(SESION_ID, { [ta.dataset.q]: ta.value });
    });
  });
});

/* S03 · Caza al phisher · Simulador SOC con cronómetro */
const SESION_ID = 's03';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    nombre: "Señal 1 — Mira el DOMINIO, no el contenido",
    queEs: "Lo único que importa de una URL es el DOMINIO: la parte entre 'https://' y el primer '/'. Si el dominio no es el oficial de la marca (ej. paypal.com), TODO LO DEMÁS es decoración para engañarte.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ https://paypal.com-seguridad-cliente.es-pagos.online/verificar → el DOMINIO real es 'es-pagos.online', NO paypal.com. Truco: meten 'paypal' como subdominio para confundir." },
    senales: [
      "El dominio real es lo de ANTES del primer '/' (después de https://).",
      "Confunden añadiendo la marca como subdominio.",
      "Extensiones raras (.tk, .online, .top, .xyz) son señal de alerta."
    ],
    quiz: {
      p: "¿Cuál es el dominio REAL de 'https://bbva.security-update.tk/login'?",
      opciones: [
        "bbva (la primera palabra)",
        "bbva.security-update",
        "security-update.tk",
        "bbva.com"
      ],
      correcta: 2,
      explica: "El dominio es 'security-update.tk'. 'bbva' es solo un SUBDOMINIO inventado. Es la trampa más típica del phishing."
    }
  },
  {
    nombre: "Señal 2 — HTTPS NO garantiza nada",
    queEs: "HTTPS y candado verde SOLO significan que la comunicación está cifrada. NO garantiza que la web sea de la empresa que dice ser. Cualquiera puede sacar HTTPS gratis para un dominio falso.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ https://amazon-ofertas-flash.tk tiene HTTPS y candado verde, pero NO es Amazon. Es FALSA. El candado solo cifra." },
    senales: [
      "El candado verde NO certifica quién es el dueño de la web.",
      "Los phishers usan HTTPS desde 2018 (Let's Encrypt es gratis).",
      "Mira el dominio, no el candado."
    ],
    quiz: {
      p: "Una web tiene HTTPS y candado verde. ¿Eso garantiza que es segura para meter tu tarjeta?",
      opciones: [
        "Sí, el candado lo garantiza",
        "Solo si la URL tiene buen aspecto",
        "No: el candado solo cifra. Mira el DOMINIO antes de meter datos"
      ],
      correcta: 2,
      explica: "El candado = cifrado, no = legitimidad. Lo que importa es el dominio real."
    }
  },
  {
    nombre: "Señal 3 — Texto del enlace ≠ URL real",
    queEs: "En un email, el enlace puede DECIR 'www.bbva.es' pero llevar a otro sitio. Pasa el ratón por encima (en ordenador) o mantén pulsado (en móvil) para ver la URL REAL antes de pinchar.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Email del 'BBVA': 'Pincha aquí: www.bbva.es'. Pero al pasar el ratón ves que el enlace lleva a 'http://bbva-fake.tk/login'. Lo que se ve NO es lo que es." },
    senales: [
      "En ordenador: pasa el ratón por encima del enlace SIN pinchar.",
      "En móvil: mantén pulsado el enlace para ver la URL real.",
      "Si lo que dice el enlace ≠ a donde lleva, es phishing."
    ],
    quiz: {
      p: "Cómo compruebas a dónde lleva un enlace de un email SIN pincharlo.",
      opciones: [
        "Pincho y miro qué pasa",
        "Paso el ratón por encima (ordenador) o lo mantengo pulsado (móvil)",
        "Le pregunto a un amigo",
        "Lo reenvío a más gente para confirmar"
      ],
      correcta: 1,
      explica: "Pasar el ratón por encima muestra la URL real abajo del navegador. Esa es la URL a la que IRÁS realmente."
    }
  },
  {
    nombre: "Señal 4 — Urgencia + amenaza = casi siempre estafa",
    queEs: "El phishing necesita que actúes SIN PENSAR. Por eso casi siempre te mete urgencia ('en 24 horas') o amenaza ('te bloqueamos la cuenta'). Empresas reales nunca te tratan así por email.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ 'ALERTA · Tu cuenta de Instagram será CERRADA en 1 hora si no verificas tu contraseña pinchando aquí'. Empresas reales no funcionan así." },
    senales: [
      "Plazo corto: 'en 24 horas', 'antes de hoy', 'ahora mismo'.",
      "Amenaza: 'bloquearemos tu cuenta', 'avisaremos a la policía', 'perderás tus datos'.",
      "Te piden datos por enlace (un banco real NUNCA lo hace por email)."
    ],
    quiz: {
      p: "Un email del 'banco' dice: 'En 24 horas bloquearemos tu cuenta si no verificas'. ¿Qué haces?",
      opciones: [
        "Pincho rápido por si acaso",
        "Llamo al banco al número del email",
        "Cierro el email y entro a la app del banco POR MI CUENTA",
        "Reenvío el email a mi familia"
      ],
      correcta: 2,
      explica: "Verificación por OTRO canal. NUNCA uses los enlaces o teléfonos del propio mensaje sospechoso."
    }
  }
];

// V/F entrenamiento
const FRASES_VF = [
  { texto: "Si una URL tiene HTTPS y candado verde, es 100% segura para meter tu contraseña.",
    correcta: false, explica: "Falso. HTTPS solo cifra. NO garantiza quién es el dueño. Mira el dominio." },
  { texto: "El dominio real de una URL es la parte entre 'https://' y el primer '/'.",
    correcta: true, explica: "Verdadero. Esa parte (ej: 'amazon.com') es el dueño. Lo demás son rutas, parámetros, etc." },
  { texto: "Si el enlace en un email dice 'www.bbva.es', seguro que va a BBVA.",
    correcta: false, explica: "Falso. El texto del enlace puede MENTIR. Pasa el ratón por encima para ver la URL real." },
  { texto: "Un dominio con extensión .tk, .online, .top o .xyz es siempre sospechoso para una web bancaria o de marca conocida.",
    correcta: true, explica: "Verdadero. Las marcas serias usan .com, .es, etc. Las extensiones gratuitas son típicas de fraudes." },
  { texto: "Si un email del banco te da 24 horas para verificar tu cuenta, conviene actuar rápido.",
    correcta: false, explica: "Falso. La urgencia es la trampa. Empresas reales no funcionan así por email." },
  { texto: "La forma correcta de comprobar si hay realmente un problema con tu cuenta del banco es ENTRAR A LA APP DEL BANCO por tu cuenta.",
    correcta: true, explica: "Verdadero. Verificación cruzada por tu canal habitual. Es la regla universal." }
];

// 10 URLs del SOC
const URLS_SOC = [
  { url: "https://www.amazon.es/orders/12345", veredicto: "legit",
    contexto: "📧 Email: 'Tu pedido #12345 ha sido enviado.' Adjunta seguimiento.",
    explica: "LEGÍTIMA. Dominio amazon.es (oficial). HTTPS. Sin urgencia. Sin pedir datos." },
  { url: "http://paypal-security-update.tk/verify-account",
    veredicto: "malic",
    contexto: "📧 Email: 'URGENTE · Verifica tu cuenta PayPal en 24h o será BLOQUEADA.'",
    explica: "MALICIOSA. Dominio FALSO (.tk no es PayPal). HTTP (sin candado). Urgencia + amenaza + pide datos. Las 4 señales rojas." },
  { url: "https://accounts.google.com/signin",
    veredicto: "legit",
    contexto: "🔗 Te llega un email de Google diciendo 'inicio de sesión desde un dispositivo nuevo'. Te lleva aquí.",
    explica: "LEGÍTIMA. Dominio google.com. HTTPS. Es la página real de Google." },
  { url: "https://bbva.security-update-cliente.es-pagos.online/login",
    veredicto: "malic",
    contexto: "📧 Email: 'Compra sospechosa de 738€ detectada · Pincha para confirmar.'",
    explica: "MALICIOSA. Dominio real es 'es-pagos.online'. 'bbva' está metido como subdominio para engañar. Extensión .online + urgencia." },
  { url: "https://www.netflix.com/account",
    veredicto: "legit",
    contexto: "🔗 Vas a tu cuenta de Netflix desde el navegador.",
    explica: "LEGÍTIMA. Dominio netflix.com. HTTPS. Página real." },
  { url: "https://instagrarn-security.com/help",
    veredicto: "malic",
    contexto: "📧 Email: 'Tu cuenta de Instagram tiene actividad sospechosa.'",
    explica: "MALICIOSA. Mira bien: 'instagrarn' con 'rn' en vez de 'm'. Es un truco visual clásico (typosquatting)." },
  { url: "https://www.spotify.com/es/premium",
    veredicto: "legit",
    contexto: "🔗 Vas a contratar Spotify Premium desde la web oficial.",
    explica: "LEGÍTIMA. Dominio spotify.com. Página real de upgrade." },
  { url: "https://microsoft.com.servicio-cuenta.top/login",
    veredicto: "malic",
    contexto: "📧 Email: 'Tu Office 365 expira mañana · renueva aquí.'",
    explica: "MALICIOSA. Dominio real es 'servicio-cuenta.top'. 'microsoft.com' es solo un subdominio. Extensión .top típica de fraudes." },
  { url: "https://educacionadistancia.juntadeandalucia.es/centros/granada/login",
    veredicto: "legit",
    contexto: "🔗 Acceso al Moodle de la Junta de Andalucía (sí, este es el de tu Moodle real).",
    explica: "LEGÍTIMA. Dominio juntadeandalucia.es (oficial)." },
  { url: "https://shop-fortnite-vbucks-promo.online/buy",
    veredicto: "malic",
    contexto: "📧 SMS: '5000 V-Bucks gratis si pinchas aquí en los próximos 10 min.'",
    explica: "MALICIOSA. Dominio random + urgencia + oferta imposible (V-Bucks oficiales solo en Fortnite o epicgames.com)." }
];

// ── TEORÍA (versión compacta común) ─────────────────────────────
let tarjetaActual = 0;
const microquizContestados = new Set();
const microquizAciertos = new Set();

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
  document.getElementById('puntos-tarjetas').innerHTML = CONCEPTOS.map(function(_, i) {
    return '<div class="punto ' + (i === 0 ? 'activo' : '') + '" onclick="irATarjeta(' + i + ')"></div>';
  }).join('');
}

function navSub(idx, delta) {
  const t = document.querySelector('.tarjeta-teoria[data-idx="' + idx + '"]');
  const subs = t.querySelectorAll('.subtarjeta');
  let actual = -1;
  subs.forEach(function(s, i) { if (s.dataset.activa === 'true') actual = i; });
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
  if (nuevo === 2) {
    btnN.textContent = microquizContestados.has(idx) ? 'Siguiente concepto ▸' : '🔒 Responde el microquiz';
    btnN.disabled = !microquizContestados.has(idx);
  } else { btnN.textContent = 'Continuar ▸'; btnN.disabled = false; }
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
  microquizContestados.add(idx);
  if (idxOp === c.correcta) microquizAciertos.add(idx);
  document.querySelectorAll('#opcionesMq-' + idx + ' button').forEach(function(b, i) { b.disabled = true; if (i === c.correcta) b.classList.add('correcta'); else if (i === idxOp) b.classList.add('incorrecta'); });
  const fb = document.getElementById('fb-mq-' + idx);
  fb.innerHTML = (idxOp === c.correcta ? '✅ ' : '❌ Correcta: ' + String.fromCharCode(65 + c.correcta) + '. ') + c.explica;
  fb.dataset.activo = 'true';
  const btnN = document.getElementById('btn-sub-next-' + idx);
  btnN.textContent = idx === CONCEPTOS.length - 1 ? '✓ Microquiz hecho' : 'Siguiente concepto ▸';
  btnN.disabled = false;
  document.getElementById('btn-siguiente').disabled = false;
  document.querySelectorAll('.puntos-tarjetas .punto').forEach(function(p, i) { if (i === idx) p.classList.add('visto'); });
  if (idx === CONCEPTOS.length - 1) { document.getElementById('barra-fin-teoria').style.display = 'flex'; otorgarInsignia('cadete'); }
}

// ── V/F ─────────────────────────────────────────────────────────
let vfActuales = [];
let vfAciertos = 0, vfFallos = 0;
const vfContestadas = new Set();

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
  vfContestadas.add(idx);
  const f = vfActuales[idx];
  const acertado = (valor === f.correcta);
  if (acertado) vfAciertos++; else vfFallos++;
  const cont = document.querySelector('.frase-vf[data-idx="' + idx + '"]');
  const botones = cont.querySelectorAll('.vf-botones button');
  botones.forEach(function(b, i) {
    b.disabled = true;
    const esCorrectaBtn = (i === 0 && f.correcta) || (i === 1 && !f.correcta);
    if (esCorrectaBtn) b.classList.add('correcta');
    else if ((i === 0 && valor) || (i === 1 && !valor)) b.classList.add('incorrecta');
  });
  const exp = document.getElementById('exp-vf-' + idx);
  exp.innerHTML = (acertado ? '✅ ' : '❌ ') + f.explica;
  exp.dataset.activo = 'true';
  document.getElementById('vf-aciertos').textContent = vfAciertos;
  document.getElementById('vf-fallos').textContent = vfFallos;
  document.getElementById('vf-restantes').textContent = FRASES_VF.length - vfContestadas.size;
  if (vfContestadas.size === FRASES_VF.length) { document.getElementById('btn-al-reto').disabled = false; otorgarInsignia('analista'); }
}

// ── SIMULADOR SOC ───────────────────────────────────────────────
let socIdx = 0, socAciertos = 0, socFallos = 0, socCrono = null;
const socResultados = [];

function iniciarSOC() {
  socIdx = 0; socAciertos = 0; socFallos = 0; socResultados.length = 0;
  document.getElementById('hud-acierto').textContent = '0';
  document.getElementById('hud-fallo').textContent = '0';
  document.getElementById('resultado-soc').style.display = 'none';
  document.getElementById('barra-fin-juego').style.display = 'none';
  mostrarURL();
}

function mostrarURL() {
  if (socIdx >= URLS_SOC.length) return cerrarSOC();
  const u = URLS_SOC[socIdx];
  document.getElementById('num-url').textContent = socIdx + 1;
  const z = document.getElementById('zona-soc');
  z.innerHTML =
    '<div class="soc-panel">' +
      '<div class="soc-hud">' +
        '<div class="soc-caso">⚡ Caso ' + (socIdx + 1) + ' / 10</div>' +
        '<div class="soc-cronos" id="soc-cronos">15</div>' +
      '</div>' +
      '<div class="soc-contexto">' + u.contexto + '</div>' +
      '<div class="soc-url">' + u.url + '</div>' +
      '<div class="soc-botones">' +
        '<button class="legit" onclick="responderSOC(\'legit\')">✓ Legítimo</button>' +
        '<button class="susp" onclick="responderSOC(\'susp\')">⚠ Sospechoso</button>' +
        '<button class="malic" onclick="responderSOC(\'malic\')">✗ Malicioso</button>' +
      '</div>' +
      '<div class="soc-veredicto" id="soc-veredicto"></div>' +
    '</div>';
  let t = 15;
  if (socCrono) clearInterval(socCrono);
  socCrono = setInterval(function() {
    t--;
    const c = document.getElementById('soc-cronos');
    if (!c) { clearInterval(socCrono); return; }
    c.textContent = t;
    c.classList.toggle('urgente', t <= 8 && t > 4);
    c.classList.toggle('critico', t <= 4);
    if (t <= 0) { clearInterval(socCrono); responderSOC('timeout'); }
  }, 1000);
}

function responderSOC(eleccion) {
  if (socCrono) clearInterval(socCrono);
  const u = URLS_SOC[socIdx];
  const acertado = (eleccion === u.veredicto);
  if (acertado) socAciertos++; else socFallos++;
  socResultados.push({ idx: socIdx, eleccion: eleccion, correcto: u.veredicto, acertado: acertado, url: u.url, explica: u.explica });

  const v = document.getElementById('soc-veredicto');
  let mensaje;
  if (eleccion === 'timeout') {
    mensaje = '⏰ <strong>Se acabó el tiempo</strong>. La URL era <strong>' +
      (u.veredicto === 'legit' ? 'LEGÍTIMA' : u.veredicto === 'susp' ? 'SOSPECHOSA' : 'MALICIOSA') + '</strong>. ' + u.explica;
  } else if (acertado) {
    mensaje = '✅ <strong>Acertado</strong>. ' + u.explica;
  } else {
    mensaje = '❌ <strong>Fallaste</strong>. La URL era <strong>' +
      (u.veredicto === 'legit' ? 'LEGÍTIMA' : u.veredicto === 'susp' ? 'SOSPECHOSA' : 'MALICIOSA') + '</strong>. ' + u.explica;
  }
  v.className = 'soc-veredicto ' + (acertado ? 'acierto' : 'fallo');
  v.innerHTML = mensaje + '<br><br><button class="btn-acad oro" onclick="siguienteSOC()">' + (socIdx + 1 >= URLS_SOC.length ? '🏁 Ver resultado final' : 'Siguiente caso ▸') + '</button>';
  v.dataset.activo = 'true';
  document.querySelectorAll('.soc-botones button').forEach(function(b) { b.disabled = true; });
  document.getElementById('hud-acierto').textContent = socAciertos;
  document.getElementById('hud-fallo').textContent = socFallos;
}

function siguienteSOC() {
  socIdx++;
  if (socIdx >= URLS_SOC.length) cerrarSOC();
  else mostrarURL();
}

function cerrarSOC() {
  document.getElementById('zona-soc').innerHTML = '';
  const res = document.getElementById('resultado-soc');
  const calif = socAciertos >= 9 ? '🏆 Analista experto' : socAciertos >= 7 ? '⭐ Buen analista' : socAciertos >= 5 ? '👍 Analista en formación' : '📚 A repasar';
  res.innerHTML =
    '<div class="puntuacion-final">' + socAciertos + ' / 10</div>' +
    '<p style="text-align:center;margin-bottom:14px;font-family:var(--cond);font-size:1.1rem;color:var(--acad-violeta)">' + calif + '</p>' +
    '<h3 style="font-family:var(--cond);margin-bottom:10px">📊 Resumen del turno</h3>' +
    socResultados.map(function(r) {
      return '<div class="item-correcciones ' + (r.acertado ? 'acierto' : 'fallo') + '">' +
        '<strong>Caso ' + (r.idx + 1) + ':</strong> ' + (r.acertado ? '✓' : '✗') + ' — ' +
        '<span style="font-family:var(--mono);font-size:.85rem">' + r.url + '</span><br>' +
        '<span style="font-size:.85rem">' + r.explica + '</span>' +
      '</div>';
    }).join('');
  res.style.display = 'block';
  document.getElementById('barra-fin-juego').style.display = 'flex';
  Academia.setSesion(SESION_ID, { socAciertos: socAciertos, socFallos: socFallos, socResultados: socResultados });
  otorgarInsignia('investigador');
}

// ── INSIGNIAS ───────────────────────────────────────────────────
const insigniasGanadas = new Set();
function otorgarInsignia(nombre) {
  if (insigniasGanadas.has(nombre)) return;
  insigniasGanadas.add(nombre);
  const el = document.querySelector('.mi-insignia[data-mi="' + nombre + '"]');
  if (el) el.dataset.ganada = 'true';
  const nombres = { cadete: 'Cadete', analista: 'Analista Junior', investigador: 'SOC Operator', detective: 'Analista SOC' };
  const emojis = { cadete: '🎖️', analista: '🎖️', investigador: '🎖️', detective: '🏆' };
  mostrarToast('Has ganado', emojis[nombre] + ' ' + nombres[nombre]);
  Academia.setSesion(SESION_ID, { ['insignia_' + nombre]: true });
}
function mostrarToast(t, n) {
  const e = document.createElement('div');
  e.className = 'toast-insignia';
  e.innerHTML = '<div class="emoji">🏅</div><div><div class="titulo">' + t + '</div><div class="nombre">' + n + '</div></div>';
  document.body.appendChild(e);
  setTimeout(function() { e.remove(); }, 4200);
}

// ── INFORME ─────────────────────────────────────────────────────
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
    Academia.mostrarFeedback(document.getElementById('fb-informe'), 'mal',
      '<span class="et">❌ Informe incompleto</span>Necesitas responder de verdad, no con letras sueltas.' + detalle);
    return;
  }
  const datos = Academia.getSesion(SESION_ID);
  Academia.marcarCompletada(SESION_ID, socAciertos, URLS_SOC.length);
  Academia.setSesion(SESION_ID, { q1: q1, q2: q2, q3: q3, informeCompletado: true, tiempoMin: Math.round((Date.now() - tInicio) / 60000) });
  document.getElementById('res-teoria').textContent = microquizAciertos.size + ' / ' + CONCEPTOS.length + ' microquiz';
  document.getElementById('res-entrenamiento').textContent = vfAciertos + ' / ' + FRASES_VF.length + ' V/F';
  document.getElementById('res-reto').textContent = socAciertos + ' / ' + URLS_SOC.length;
  document.getElementById('res-tiempo').textContent = (Math.round((Date.now() - tInicio) / 60000)) + ' min';
  const cod = Academia.codigoFinalizacion(SESION_ID, socAciertos);
  document.getElementById('cod-final').textContent = 'CÓDIGO: ' + cod;
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'Analista SOC' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}

function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'Analista SOC',
    subtitulo: 'Sesión 3 · Caza al phisher · Promoción 2026',
    icono: '🎣',
    insignia: 'Analista SOC',
    nombres: [n1, n2],
    sesionNum: 'S3',
    score: socAciertos,
    total: URLS_SOC.length,
    codigo: datos.codigo,
    frase: '15 segundos te separan de un click que arruina una semana'
  }, 'S03-cazaphisher-' + n1.replace(/\s/g, '_') + '.png');
}

// ── INIT (con arranque robusto) ─────────────────────────────────
function initSesion() {
  renderTarjetas();
  renderVF();
  iniciarSOC();
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

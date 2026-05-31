/* S08 · Escape Room CCN-CERT · Academia Cyber-IES */
const SESION_ID = 's08';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    "nombre": "CCN-CERT — el equipo que protege España",
    "queEs": "El CCN-CERT es la \"Unidad de Respuesta a Incidentes\" del Centro Criptológico Nacional. Es decir: el equipo de élite que defiende las administraciones públicas españolas (ministerios, embajadas, agencias) de ciberataques.",
    "ejemplo": {
      "tipo": "bueno",
      "texto": "✅ Si un ministerio español sufre un ataque, el CCN-CERT entra a investigar y a defender. Son los \"bomberos\" de la ciberseguridad estatal."
    },
    "senales": [
      "Depende del Centro Nacional de Inteligencia (CNI).",
      "Coordina la respuesta a ciberincidentes graves.",
      "Publica guías y formación abierta para todos (como este escape room)."
    ],
    "quiz": {
      "p": "¿De qué se encarga principalmente el CCN-CERT?",
      "opciones": [
        "Vender antivirus",
        "Defender las administraciones públicas españolas de ciberataques",
        "Hacer videojuegos",
        "Investigar phishings en bancos privados"
      ],
      "correcta": 1,
      "explica": "Son la unidad pública de respuesta a incidentes de ciberseguridad del Estado."
    }
  },
  {
    "nombre": "Ciberataque vs ciberincidente",
    "queEs": "CIBERATAQUE: alguien intenta dañar/robar a propósito. CIBERINCIDENTE: cualquier evento de seguridad (puede ser un ataque, un error, una fuga…).",
    "ejemplo": {
      "tipo": "peligroso",
      "texto": "⚠️ Hackeo deliberado a un ministerio → ciberataque (y también incidente). Empleado que pierde un USB con datos → incidente (no ataque)."
    },
    "senales": [
      "Ataque = intención maliciosa.",
      "Incidente = cualquier suceso de seguridad relevante.",
      "Todo ataque es un incidente, pero no todo incidente es un ataque."
    ],
    "quiz": {
      "p": "Un empleado del ministerio pierde un USB con documentos en la calle. ¿Qué es?",
      "opciones": [
        "Ciberataque",
        "Ciberincidente (no es ataque pero sí afecta a la seguridad)",
        "No es nada",
        "Cibercrimen organizado"
      ],
      "correcta": 1,
      "explica": "Es un incidente de seguridad (fuga accidental), no un ataque dirigido. El CCN-CERT también gestiona estos casos."
    }
  },
  {
    "nombre": "Ciberresiliencia: caer y levantarse",
    "queEs": "No se trata solo de NUNCA caer (imposible). Se trata de PODER LEVANTARSE rápido y aprender. La ciberresiliencia es la capacidad de seguir funcionando incluso bajo ataque y recuperarse después.",
    "ejemplo": {
      "tipo": "bueno",
      "texto": "✅ Un hospital sufre ransomware. Pero TIENE BACKUPS recientes y un plan de actuación. En 8 horas restauran todo y siguen atendiendo. Eso es ciberresiliencia."
    },
    "senales": [
      "Hacer copias de seguridad regulares (backups).",
      "Tener un plan de actuación ANTES de la crisis.",
      "Practicar simulacros de ciberincidente."
    ],
    "quiz": {
      "p": "¿Qué es ciberresiliencia?",
      "opciones": [
        "Ser invulnerable a los ataques",
        "La capacidad de seguir funcionando bajo ataque y recuperarse rápido",
        "Tener el antivirus más caro",
        "Cambiar siempre de empresa"
      ],
      "correcta": 1,
      "explica": "No se trata de evitar todos los ataques (imposible). Se trata de aguantar y levantarse rápido."
    }
  },
  {
    "nombre": "INCIBE — para empresas y ciudadanos",
    "queEs": "INCIBE es el \"primo\" del CCN para empresas privadas y ciudadanos. Tiene una línea gratuita: 017. Tienen guías para todo y ayudan en casos de ciberacoso, fraude, sextorsión, etc.",
    "ejemplo": {
      "tipo": "bueno",
      "texto": "✅ Te chantajean por internet. Llamas al 017 (gratis, anónimo). Te asesoran qué hacer paso a paso. Sin juzgarte."
    },
    "senales": [
      "INCIBE = Instituto Nacional de Ciberseguridad.",
      "Línea 017: gratuita, anónima, 9-21h.",
      "Web incibe.es con guías para padres, menores, empresas, etc."
    ],
    "quiz": {
      "p": "Te están chantajeando por internet con fotos. ¿Qué número llamas?",
      "opciones": [
        "112 (emergencias)",
        "017 (línea INCIBE de ayuda en ciberseguridad)",
        "060 (administración)",
        "091 (policía)"
      ],
      "correcta": 1,
      "explica": "El 017 de INCIBE: gratis, anónimo, especializado. Pueden ayudarte a denunciar y a protegerte. Si hay delito grave, ELLOS te ayudan a llegar a la policía."
    }
  }
];

const FRASES_VF = [
  {
    "texto": "El CCN-CERT es un organismo público español que protege las administraciones del Estado de ciberataques.",
    "correcta": true,
    "explica": "Verdadero. Es la unidad de respuesta del Centro Criptológico Nacional."
  },
  {
    "texto": "Todo ciberincidente es siempre un ciberataque deliberado.",
    "correcta": false,
    "explica": "Falso. Un incidente puede ser también un error humano, un fallo técnico, una fuga accidental."
  },
  {
    "texto": "Tener backups regulares es una de las claves de la ciberresiliencia.",
    "correcta": true,
    "explica": "Verdadero. Sin backups, un ransomware te puede destruir. Con backups recientes, te recuperas."
  },
  {
    "texto": "INCIBE (017) solo atiende a grandes empresas, no a ciudadanos particulares.",
    "correcta": false,
    "explica": "Falso. El 017 está pensado también para particulares (especialmente jóvenes y mayores)."
  },
  {
    "texto": "La ciberseguridad perfecta existe: con suficiente dinero, ninguna empresa es vulnerable.",
    "correcta": false,
    "explica": "Falso. NO existe seguridad 100%. Por eso importa la ciberresiliencia: aguantar y recuperarse."
  },
  {
    "texto": "El CCN publica formación abierta y gratuita (como este escape room) porque la seguridad de todos beneficia a todos.",
    "correcta": true,
    "explica": "Verdadero. Su misión incluye divulgar buenas prácticas a la sociedad."
  }
];


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
  const nombres = {"cadete": "Cadete", "analista": "Aprendiz", "investigador": "Operador", "detective": "Cadete CCN-CERT"};
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
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'Cadete CCN-CERT' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}
function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'Cadete CCN-CERT',
    subtitulo: 'Sesión 8 · Escape Room CCN-CERT · Promoción 2026',
    icono: '🔐',
    insignia: 'Cadete CCN-CERT',
    nombres: [n1, n2],
    sesionNum: 'SESION8',
    score: microquizAciertos.size + vfAciertos,
    total: CONCEPTOS.length + FRASES_VF.length,
    codigo: datos.codigo,
    frase: 'El mejor entrenamiento es el que viene de profesionales que defienden a un país'
  }, 'S08-escape-ccn-' + n1.replace(/\s/g, '_') + '.png');
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

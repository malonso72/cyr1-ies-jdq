/* S15 · Mesa del Detective · Caso Sr. Hernández */
const SESION_ID = 's15';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    nombre: "Fase 1 — Reconocimiento",
    queEs: "Antes del email, el atacante INVESTIGA a su víctima durante días o semanas. Mira LinkedIn, la web del IES, redes sociales del secretario, noticias del centro. Cuanto más sepa, más creíble será el cebo.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ El atacante busca 'IES Jiménez de Quesada secretario' en Google. Encuentra el nombre del Sr. Hernández, su email del centro, y que justo es periodo de evaluaciones. Ya tiene contexto." },
    senales: [
      "Tu información profesional pública (LinkedIn, web del centro) puede usarse contra ti.",
      "Cuanto más activo sea tu rastro digital, más fácil personalizar un ataque.",
      "Por eso los ataques DIRIGIDOS son mucho más peligrosos que los masivos."
    ],
    quiz: {
      p: "¿Qué tipo de ataque suele venir PRECEDIDO de varios días/semanas de investigación?",
      opciones: ["Phishing masivo (mismo email a millones)", "Phishing dirigido (un email personalizado a UNA persona)", "Ransomware automático", "Spam comercial"],
      correcta: 1,
      explica: "El phishing dirigido (spear phishing) personaliza el ataque a UNA persona. Investigan antes para hacerlo creíble. Es el que cayó al Sr. Hernández."
    }
  },
  {
    nombre: "Fase 2 — Cebo personalizado",
    queEs: "El atacante envía un email que contiene DATOS REALES del centro: nombre del director, fecha de la próxima evaluación, logo del IES. Eso lo hace creíble. Pero la URL del enlace NO es la oficial.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ 'Estimado Sr. Hernández, en preparación de la evaluación del próximo viernes 16, le ruego revise el acceso al sistema desde aquí: https://intranet-iesjdq-acceso.online/login'" },
    senales: [
      "El email contiene datos reales que te hacen pensar que es legítimo.",
      "Tiene urgencia o contexto que justifica actuar rápido.",
      "El enlace parece oficial pero el dominio NO es el de la organización (mira con atención)."
    ],
    quiz: {
      p: "¿Por qué un phishing dirigido es MÁS peligroso que el masivo?",
      opciones: [
        "Llega a más gente",
        "Está personalizado con datos reales que lo hacen creíble",
        "Tiene mejor diseño gráfico",
        "Viene cifrado"
      ],
      correcta: 1,
      explica: "La personalización con datos reales DESACTIVA la sospecha. Por eso un buen detective siempre comprueba la URL ANTES de hacer click, no importa cuán creíble parezca el contenido."
    }
  },
  {
    nombre: "Fase 3 — Credenciales y movimiento lateral",
    queEs: "El secretario pincha, mete usuario+contraseña en una web FALSA que imita la real. El atacante captura esas credenciales y las usa para entrar al sistema REAL. Si no hay 2FA, acceso directo. Después, intenta moverse a otros sistemas.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ El atacante usa las credenciales del Sr. Hernández para entrar al sistema de notas. Como el secretario tiene permisos amplios, accede a expedientes de alumnos, plantilla de profesores, datos del centro." },
    senales: [
      "Sin 2FA, una contraseña filtrada = acceso total inmediato.",
      "El movimiento lateral aprovecha que las víctimas tienen permisos amplios.",
      "Muchas veces el atacante actúa POR LA NOCHE para no ser detectado."
    ],
    quiz: {
      p: "¿Qué medida HABRÍA EVITADO probablemente el ataque al Sr. Hernández?",
      opciones: [
        "Un firewall más caro",
        "Tener 2FA activado en el correo del centro",
        "Más cámaras de seguridad",
        "Cambiar el sistema operativo"
      ],
      correcta: 1,
      explica: "El 2FA. Aunque el atacante tuviera la contraseña, sin el código del móvil del secretario no podría entrar. Es la barrera más efectiva."
    }
  },
  {
    nombre: "Fase 4 — Encubrimiento y pista falsa",
    queEs: "Los atacantes profesionales DESPISTAN deliberadamente: borran logs, dejan rastros falsos, crean usuarios señuelo. En la investigación posterior, hay que distinguir las evidencias reales de los rastros plantados.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ En la mesa del detective aparece un USB encontrado en el aparcamiento del IES. ¿Es del atacante? ¿O lo dejó allí a propósito para que la investigación se desvíe? Cuidado: las pistas obvias suelen ser FALSAS." },
    senales: [
      "Una pista demasiado fácil/obvia debe levantar sospecha.",
      "Cruzar tiempos y lugares descarta las pistas falsas.",
      "Lo importante son los RASTROS DIGITALES (logs, IPs), no los objetos físicos."
    ],
    quiz: {
      p: "Encuentras un USB sospechoso con el logo del IES en el suelo del aparcamiento un día después del ataque. ¿Qué piensas como detective?",
      opciones: [
        "Es la prueba clave: lo metemos al ordenador a ver",
        "Es probablemente una pista falsa o un USB envenenado, NO lo conectamos",
        "Lo guardo como recuerdo",
        "Lo tiro a la papelera"
      ],
      correcta: 1,
      explica: "Conectar un USB desconocido es uno de los errores más graves: puede contener malware. Y demasiado conveniente = sospechoso. Lo mandas al perito sin conectarlo."
    }
  }
];

// Entrenamiento V/F (6 frases sobre detective forense)
const FRASES_VF = [
  { texto: "Un atacante dedicado puede pasar DÍAS o SEMANAS investigando antes de enviar el primer email.", correcta: true,
    explica: "Verdadero. El reconocimiento es la fase 1 del ataque. Cuanto más investigan, más creíble es el cebo." },
  { texto: "Si un email contiene datos reales del centro (nombre del director, fecha real), es seguro confiar en él.", correcta: false,
    explica: "Falso. Esos datos son PÚBLICOS y los atacantes los usan precisamente para hacerlo creíble. Comprueba siempre la URL antes de pinchar." },
  { texto: "Una vez has metido tu contraseña en una web falsa, no se puede hacer nada.", correcta: false,
    explica: "Falso. CAMBIA la contraseña en la web REAL inmediatamente. Y activa 2FA. Cuanto antes lo hagas, menos tiempo tendrá el atacante." },
  { texto: "El 2FA habría evitado probablemente el ataque al Sr. Hernández.", correcta: true,
    explica: "Verdadero. Aunque robaran su contraseña, sin el código del móvil del secretario no podrían entrar. Es la medida más eficaz." },
  { texto: "Encontrar un USB sospechoso con el logo del centro es la prueba clave del ataque.", correcta: false,
    explica: "Falso. Las pistas físicas demasiado convenientes suelen ser FALSAS o señuelos. Y conectar un USB desconocido puede instalar malware. Lo importante son los rastros digitales: logs e IPs." },
  { texto: "Los ataques dirigidos solo van contra grandes empresas o bancos.", correcta: false,
    explica: "Falso. Institutos, ayuntamientos, despachos pequeños son víctimas frecuentes porque tienen menos protección y muchos datos." }
];

// ── TEORÍA (versión compacta) ───────────────────────────────────
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
            c.quiz.opciones.map(function(op, j) {
              return '<button onclick="responderMicroquiz(' + i + ',' + j + ')">' + String.fromCharCode(65 + j) + '. ' + op + '</button>';
            }).join('') +
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
  document.querySelectorAll('.puntos-tarjetas .punto').forEach(function(p, i) {
    p.classList.remove('activo','visto');
    if (i === idx) p.classList.add('activo'); else if (microquizContestados.has(i)) p.classList.add('visto');
  });
  document.getElementById('btn-anterior').disabled = idx === 0;
  document.getElementById('btn-siguiente').disabled = !microquizContestados.has(idx);
  if (idx === CONCEPTOS.length - 1 && microquizContestados.has(idx)) {
    document.getElementById('barra-fin-teoria').style.display = 'flex';
    otorgarInsignia('cadete');
  }
}

function responderMicroquiz(idx, idxOp) {
  if (microquizContestados.has(idx)) return;
  const c = CONCEPTOS[idx].quiz;
  microquizContestados.add(idx);
  if (idxOp === c.correcta) microquizAciertos.add(idx);
  document.querySelectorAll('#opcionesMq-' + idx + ' button').forEach(function(b, i) {
    b.disabled = true;
    if (i === c.correcta) b.classList.add('correcta');
    else if (i === idxOp) b.classList.add('incorrecta');
  });
  const fb = document.getElementById('fb-mq-' + idx);
  fb.innerHTML = (idxOp === c.correcta ? '✅ ' : '❌ Correcta: ' + String.fromCharCode(65 + c.correcta) + '. ') + c.explica;
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

// ── ENTRENAMIENTO V/F ───────────────────────────────────────────
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
        '<button onclick="responderVF(' + i + ',true)">✓ SÍ procede / Verdadero</button>' +
        '<button onclick="responderVF(' + i + ',false)">✗ NO procede / Falso</button>' +
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
  if (vfContestadas.size === FRASES_VF.length) {
    document.getElementById('btn-al-reto').disabled = false;
    otorgarInsignia('analista');
  }
}

// ── RETO (iframe) — marcar como hecho ───────────────────────────
function marcarRetoHecho() {
  const btn = document.getElementById('btn-reto-hecho');
  btn.disabled = true;
  btn.textContent = '✓ Reto completado';
  document.getElementById('barra-fin-juego').style.display = 'flex';
  otorgarInsignia('investigador');
  Academia.setSesion(SESION_ID, { retoHecho: true });
}

// ── INSIGNIAS ───────────────────────────────────────────────────
const insigniasGanadas = new Set();
function otorgarInsignia(nombre) {
  if (insigniasGanadas.has(nombre)) return;
  insigniasGanadas.add(nombre);
  const el = document.querySelector('.mi-insignia[data-mi="' + nombre + '"]');
  if (el) el.dataset.ganada = 'true';
  const nombres = { cadete: 'Cadete', analista: 'Analista', investigador: 'Detective', detective: 'Detective Forense' };
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
  if (contarPalabras(q1) < 8 || contarPalabras(q2) < 8 || contarPalabras(q3) < 8) {
    Academia.mostrarFeedback(document.getElementById('fb-informe'), 'mal',
      '<span class="et">❌ Informe incompleto</span>Cada respuesta debe tener al menos 8 palabras.');
    return;
  }
  const datos = Academia.getSesion(SESION_ID);
  Academia.marcarCompletada(SESION_ID, microquizAciertos.size + vfAciertos, CONCEPTOS.length + FRASES_VF.length);
  Academia.setSesion(SESION_ID, { q1: q1, q2: q2, q3: q3, informeCompletado: true, tiempoMin: Math.round((Date.now() - tInicio) / 60000) });
  document.getElementById('res-teoria').textContent = microquizAciertos.size + ' / ' + CONCEPTOS.length + ' microquiz';
  document.getElementById('res-entrenamiento').textContent = vfAciertos + ' / ' + FRASES_VF.length + ' V/F';
  document.getElementById('res-tiempo').textContent = (Math.round((Date.now() - tInicio) / 60000)) + ' min';
  const cod = Academia.codigoFinalizacion(SESION_ID, microquizAciertos.size + vfAciertos);
  document.getElementById('cod-final').textContent = 'CÓDIGO: ' + cod;
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'Detective Forense' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}

function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'Detective Forense',
    subtitulo: 'Sesión 15 · Mesa del Detective · Promoción 2026',
    icono: '🕵️',
    insignia: 'Detective Forense',
    nombres: [n1, n2],
    sesionNum: 'S15',
    score: microquizAciertos.size + vfAciertos,
    total: CONCEPTOS.length + FRASES_VF.length,
    codigo: datos.codigo,
    frase: 'El detective no es el que adivina; es el que separa la señal del ruido'
  }, 'S15-detective-' + n1.replace(/\s/g, '_') + '.png');
}

// ── INIT ────────────────────────────────────────────────────────
window.addEventListener('DOMContentLoaded', function() {
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
});

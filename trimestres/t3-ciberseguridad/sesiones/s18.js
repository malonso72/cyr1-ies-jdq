/* S18 · Examen del Analista · Cierre del bloque */
const SESION_ID = 's18';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    nombre: "Regla universal 1 — Verifica por OTRO canal",
    queEs: "La regla más potente de todo el bloque. Si te llega algo por email, SMS o llamada pidiendo actuar, NO uses los datos del mensaje. Verifica por TU canal habitual (la app oficial, el teléfono detrás de tu tarjeta, llamar a la persona al número de siempre).",
    ejemplo: { tipo: 'bueno', texto: "✅ Te llega un email del 'banco'. En vez de pinchar, abres la app del banco DIRECTAMENTE. Si hay algo real, ahí lo verás. Si no, era estafa." },
    senales: [
      "Funciona contra phishing, vishing, deepfakes y suplantación de identidad.",
      "Si la persona/empresa es real, NUNCA se enfadará: lo agradecerá.",
      "Si te piden no verificar 'por confidencialidad', es ESTAFA segura."
    ],
    quiz: {
      p: "Recibes un mensaje urgente que parece del banco. ¿Qué haces?",
      opciones: [
        "Pulso el enlace para verificar rápido",
        "Llamo al teléfono que viene en el mensaje",
        "Entro a la app del banco POR MI CUENTA o llamo al número detrás de mi tarjeta",
        "Reenvío a mi familia para que opinen"
      ],
      correcta: 2,
      explica: "Verificación cruzada por TU canal habitual. La única regla que neutraliza casi cualquier ataque social."
    }
  },
  {
    nombre: "Regla universal 2 — Si te meten prisa, PARA",
    queEs: "Todas las estafas comparten un truco: te meten urgencia. 'Solo hoy', 'caduca en 1 hora', 'tu cuenta se bloquea'. La urgencia bloquea tu cerebro racional. La calma es tu mejor antivirus.",
    ejemplo: { tipo: 'bueno', texto: "✅ Cualquier oferta o aviso con cuenta atrás → respira, deja pasar 5 minutos, verifica. Si era real, sigue siendo real. Si era trampa, se desinfla." },
    senales: [
      "Cuenta atrás visible en la página.",
      "Palabras: 'AHORA', 'YA', 'ÚLTIMA OPORTUNIDAD', 'SOLO HOY'.",
      "Amenazas inmediatas: 'bloqueamos tu cuenta', 'avisamos a la policía'."
    ],
    quiz: {
      p: "Una oferta 'caduca en 5 minutos'. ¿Qué dice la regla universal?",
      opciones: [
        "Date prisa, no te quedes sin ella",
        "Para, respira y verifica. Si era real, seguirá siendo real",
        "Compártela rápido por WhatsApp",
        "Compra y luego decides si devolver"
      ],
      correcta: 1,
      explica: "La urgencia es el truco número 1 de las estafas. Si te meten prisa, sospecha. La calma es tu mejor defensa."
    }
  },
  {
    nombre: "Regla universal 3 — Comprueba el DOMINIO, no el candado",
    queEs: "HTTPS y candado solo significan que la comunicación está cifrada. NO significan que la web sea legítima. Cualquiera puede comprar un certificado HTTPS para un dominio falso. Lo que importa es el DOMINIO (lo que aparece ANTES del primer '/').",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ 'https://paypal-security.tk' tiene HTTPS y candado, pero el dominio NO es paypal.com. Es FALSA. El candado no garantiza nada sobre quién es el dueño." },
    senales: [
      "El dominio REAL es la parte entre 'https://' y el primer '/'.",
      "Confunden añadiendo la marca como subdominio: 'paypal.security-update.tk'.",
      "Extensiones raras (.tk, .online, .top, .xyz) son señal de alerta."
    ],
    quiz: {
      p: "Una web tiene HTTPS y candado verde. ¿Eso garantiza que es segura para meter tu tarjeta?",
      opciones: [
        "Sí, el candado lo garantiza",
        "No: el candado solo cifra. Mira el DOMINIO antes de meter datos",
        "Solo si tiene buen diseño gráfico",
        "Sí, mientras no haya errores de ortografía"
      ],
      correcta: 1,
      explica: "El candado = cifrado, no = legitimidad. Lo que importa es el dominio real. Si no es el oficial de la marca, NO metas datos."
    }
  },
  {
    nombre: "Regla universal 4 — La seguridad es un HÁBITO",
    queEs: "No existe el '100% seguro'. La ciberseguridad es como lavarse los dientes: lo haces TODOS los días, en pequeñas cosas. 2FA en cada app. Contraseñas únicas. Verificar antes de actuar. Si lo conviertes en rutina, el 90% de los ataques se desvían solos.",
    ejemplo: { tipo: 'bueno', texto: "✅ Un alumno acaba la Academia y CADA semana revisa sus contraseñas, mira si su email aparece en HIBP, activa 2FA en una app nueva. No es paranoico: es responsable. Y casi nunca caerá." },
    senales: [
      "No es un cambio de un día: es una rutina mantenida.",
      "Pequeños hábitos: 2FA, contraseñas únicas, verificar siempre.",
      "Compartir lo aprendido con familia/amigos multiplica tu protección."
    ],
    quiz: {
      p: "¿Cuál de estas frases es CORRECTA tras este bloque?",
      opciones: [
        "Ya estoy 100% protegido contra cualquier ataque",
        "La ciberseguridad es un hábito diario, no un estado conseguido",
        "Mientras no compre online, no tengo riesgo",
        "Los hackers solo van contra empresas grandes"
      ],
      correcta: 1,
      explica: "La seguridad es como el deporte o la higiene: se mantiene CADA día. Y conviene compartirlo: tu abuela también necesita saberlo."
    }
  }
];

// Entrenamiento V/F (6 frases integradoras del bloque entero)
const FRASES_VF = [
  { texto: "La regla más eficaz contra cualquier ataque social (phishing, vishing, deepfake) es VERIFICAR POR OTRO CANAL.", correcta: true,
    explica: "Verdadero. Cambias tú el canal por uno que ya sabes que es auténtico. Funciona en TODOS los casos del bloque." },
  { texto: "Una contraseña larga sin símbolos raros es más fuerte que una corta con muchos símbolos.", correcta: true,
    explica: "Verdadero. La longitud manda. 'caballo-mesa-luna-puente' es más fuerte que 'P@ss1!'" },
  { texto: "Si una web tiene HTTPS y candado, es completamente segura para meter tu tarjeta.", correcta: false,
    explica: "Falso. El candado solo cifra; no garantiza quién es el dueño. Comprueba siempre el DOMINIO." },
  { texto: "Las fake news, los deepfakes y el phishing comparten un mismo truco: la URGENCIA emocional.", correcta: true,
    explica: "Verdadero. Te meten prisa o te emocionan para que actúes antes de pensar. La calma es la defensa." },
  { texto: "OSINT (investigación con fuentes abiertas) solo lo usan los criminales.", correcta: false,
    explica: "Falso. También lo usan periodistas, peritos, policía y empresas de seguridad. Lo importante es saber QUÉ información tuya está abierta." },
  { texto: "Después de este bloque ya estoy 100% protegido contra cualquier ciberataque.", correcta: false,
    explica: "Falso. La ciberseguridad es un HÁBITO diario, no un estado conseguido. Mantén las rutinas y compártelas con tu familia." }
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
  const nombres = { cadete: 'Cadete', analista: 'Analista', investigador: 'Examinado', detective: 'Analista Sénior' };
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
  Academia.marcarCompletada(SESION_ID, microquizAciertos.size + vfAciertos, CONCEPTOS.length + FRASES_VF.length);
  Academia.setSesion(SESION_ID, { q1: q1, q2: q2, q3: q3, informeCompletado: true, tiempoMin: Math.round((Date.now() - tInicio) / 60000) });
  document.getElementById('res-teoria').textContent = microquizAciertos.size + ' / ' + CONCEPTOS.length + ' microquiz';
  document.getElementById('res-entrenamiento').textContent = vfAciertos + ' / ' + FRASES_VF.length + ' V/F';
  document.getElementById('res-tiempo').textContent = (Math.round((Date.now() - tInicio) / 60000)) + ' min';
  const cod = Academia.codigoFinalizacion(SESION_ID, microquizAciertos.size + vfAciertos);
  document.getElementById('cod-final').textContent = 'CÓDIGO: ' + cod;
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'Analista Sénior' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}

function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'Analista Sénior',
    subtitulo: 'Diploma Final · Academia Cyber-IES · Promoción 2026',
    icono: '🎓',
    insignia: 'Analista Sénior',
    nombres: [n1, n2],
    sesionNum: 'S18 · FINAL',
    score: microquizAciertos.size + vfAciertos,
    total: CONCEPTOS.length + FRASES_VF.length,
    codigo: datos.codigo,
    frase: 'El analista no es el que nunca duda; es el que sabe cuándo parar y comprobar'
  }, 'DIPLOMA-FINAL-academia-cyberies-' + n1.replace(/\s/g, '_') + '.png');
}

// ── INIT ────────────────────────────────────────────────────────
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

// Arranque robusto: si DOM ya está listo, ejecutar; si no, esperar a DOMContentLoaded
if (document.readyState !== 'loading') {
  initSesion();
} else {
  document.addEventListener('DOMContentLoaded', initSesion);
}


/* S18 · Examen del Analista · Cierre del bloque */
const SESION_ID = 's18';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    nombre: "¿Qué es el Derecho al Olvido?",
    queEs: "Es el derecho a pedir a Google (u otros buscadores) que NO muestre resultados sobre ti cuando alguien busca tu nombre, en ciertos casos. No borra la información del origen, pero la 'deja de indexar'.",
    ejemplo: { tipo: 'bueno', texto: "✅ Una persona que cometió un delito menor hace 20 años pide que la noticia ya no salga al buscar su nombre. Si ya no hay interés público actual, suele proceder." },
    senales: [
      "Es un derecho RECONOCIDO en la Unión Europea (sentencia Google Spain, 2014).",
      "Se solicita rellenando un formulario en Google: ellos deciden caso a caso.",
      "Si Google deniega, puedes recurrir a la Agencia Española de Protección de Datos (AEPD)."
    ],
    quiz: {
      p: "¿Qué hace exactamente el Derecho al Olvido?",
      opciones: [
        "Borra la información de internet por completo",
        "Hace que Google deje de mostrar esa información al buscar tu nombre",
        "Te paga una indemnización automática",
        "Sustituye los datos por otros"
      ],
      correcta: 1,
      explica: "Solo el buscador deja de indexar el resultado al buscar TU nombre. La información sigue existiendo donde se publicó originalmente."
    }
  },
  {
    nombre: "Regla 1 — Información antigua sin interés público actual",
    queEs: "SÍ procede normalmente: información antigua, sin interés público actual, que te perjudica hoy. Especialmente si fue publicada por terceros sin tu permiso.",
    ejemplo: { tipo: 'bueno', texto: "✅ Hace 12 años, una amiga subió una foto tuya en la playa que aún sale en Google Imágenes. Pides Derecho al Olvido → suele proceder." },
    senales: [
      "Han pasado años desde la publicación.",
      "Ya no hay interés periodístico / social en la información.",
      "Te perjudica en tu vida actual (trabajo, relaciones)."
    ],
    quiz: {
      p: "Hace 8 años, Pablo (entonces 19 años) escribió un comentario violento en un foro. Hoy busca trabajo y le sale al buscar su nombre. ¿Procede?",
      opciones: ["Sí procede: información antigua sin interés público actual", "No procede: la cometió él voluntariamente", "Solo si pide perdón a la víctima"],
      correcta: 0,
      explica: "Procede. Hace 8 años + comentario menor + le perjudica en su búsqueda de trabajo. Caso clásico de la Regla 1."
    }
  },
  {
    nombre: "Regla 2 — NO procede: interés público actual o cargo público",
    queEs: "NO procede: información veraz de interés público actual, o datos sobre personas con cargos públicos en el ejercicio de su función.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Un alcalde EN EJERCICIO pide que se borren tweets suyos de cuando era candidato hablando de su programa. NO procede: hay interés público en saber qué dijo." },
    senales: [
      "La persona ejerce un cargo público (alcalde, ministro, diputado).",
      "La información se refiere al ejercicio de ese cargo.",
      "Existe un interés legítimo de la ciudadanía en conocerla."
    ],
    quiz: {
      p: "Manuel es CEO de una empresa importante. Una web publica que ganó 480.000€ (dato veraz del Registro Mercantil, que es público). Pide Derecho al Olvido. ¿Procede?",
      opciones: ["Sí procede: es información personal", "No procede: dato veraz, de fuente pública y con interés social", "Solo si la empresa quiebra"],
      correcta: 1,
      explica: "No procede. El Registro Mercantil es público por ley, el dato es veraz, y un CEO tiene proyección pública. Caso clásico de la Regla 2."
    }
  },
  {
    nombre: "Regla 3 — Sentencias firmes recientes",
    queEs: "Las sentencias firmes recientes que mantengan interés social NO se pueden borrar. Las antiguas (delitos menores, ya cumplida la pena) sí pueden proceder.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Carlos fue CONDENADO en sentencia firme por estafa hace 2 años. Pide borrar la noticia. NO procede: sentencia firme reciente con interés social." },
    senales: [
      "Cuánto tiempo ha pasado desde la sentencia.",
      "La gravedad del delito.",
      "Si todavía hay interés social/preventivo en que la información sea accesible."
    ],
    quiz: {
      p: "Lucía fue ABSUELTA de un delito en 2019, pero al buscar su nombre sale la noticia ANTIGUA de cuando fue acusada. ¿Procede?",
      opciones: [
        "Sí procede: fue absuelta y la noticia sigue dañándola",
        "No procede: fue noticia pública en su día",
        "Solo si paga una tasa"
      ],
      correcta: 0,
      explica: "Procede claramente. Fue ABSUELTA y la noticia inicial sigue perjudicándola. El interés público desapareció con la absolución."
    }
  }
];

// Entrenamiento V/F (6 casos)
const FRASES_VF = [
  { texto: "El Derecho al Olvido borra la información de internet por completo.", correcta: false,
    explica: "Falso. Solo hace que el BUSCADOR deje de indexarla. La información sigue donde se publicó originalmente." },
  { texto: "Un alcalde en activo NO puede pedir borrar tweets sobre su gestión política.", correcta: true,
    explica: "Verdadero. Hay interés público actual en su actividad política." },
  { texto: "Una información FALSA sobre ti se borra por Derecho al Olvido.", correcta: false,
    explica: "Falso. La información falsa se persigue por OTRAS vías (rectificación, denuncia por difamación). El Derecho al Olvido es para información VERAZ que ya no tiene interés." },
  { texto: "Una foto tuya en la playa que subió una amiga hace 12 años puede borrarse.", correcta: true,
    explica: "Verdadero. Antigua + sin permiso tuyo + sin interés público → caso típico de Regla 1." },
  { texto: "Una sentencia firme de estafa hace 6 meses se puede borrar sin más.", correcta: false,
    explica: "Falso. Es reciente, hay interés social (proteger a futuros clientes). Habría que esperar bastante tiempo." },
  { texto: "Los datos del Registro Mercantil sobre el sueldo de un CEO se pueden borrar por Derecho al Olvido.", correcta: false,
    explica: "Falso. El Registro Mercantil es PÚBLICO POR LEY. Existe un interés legítimo en que sea consultable." }
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
  const nombres = { cadete: 'Cadete', analista: 'Analista', investigador: 'Jurista', detective: 'DPO' };
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
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'Delegado de Protección de Datos' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}

function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'Delegado de Protección de Datos',
    subtitulo: 'Sesión 12 · Derecho al Olvido · Promoción 2026',
    icono: '⚖️',
    insignia: 'Delegado de Protección de Datos',
    nombres: [n1, n2],
    sesionNum: 'S12',
    score: microquizAciertos.size + vfAciertos,
    total: CONCEPTOS.length + FRASES_VF.length,
    codigo: datos.codigo,
    frase: 'La privacidad protege a la persona; el interés público a la comunidad'
  }, 'S12-derecho-olvido-' + n1.replace(/\s/g, '_') + '.png');
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

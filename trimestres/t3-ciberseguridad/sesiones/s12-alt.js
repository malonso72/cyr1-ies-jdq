/* S12 · Tribunal Digital · Academia Cyber-IES */
const SESION_ID = 's12alt';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    nombre: "¿Qué es el Derecho al Olvido?",
    queEs: "Es tu poder para pedir a Google (u otros buscadores) que YA NO MUESTRE ciertas cosas sobre ti cuando alguien busca tu nombre. La información NO desaparece de internet del todo: sigue donde se publicó, pero Google deja de enseñártela en los resultados.",
    ejemplo: { tipo: 'bueno', texto: "✅ Buscas tu nombre en Google y aparece un vídeo ridículo tuyo de cuando tenías 9 años. Pides Derecho al Olvido. Google evalúa tu caso y, si procede, deja de mostrar ese vídeo al buscar tu nombre." },
    senales: [
      "Es un derecho que existe en toda la Unión Europea desde 2014.",
      "Lo pides rellenando un formulario en Google: ellos deciden caso a caso.",
      "Si Google te dice NO, puedes recurrir a la AEPD (la agencia que protege tus datos)."
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
      explica: "Solo el buscador deja de mostrar el resultado al buscar TU nombre. La información sigue existiendo donde se publicó. Pero deja de encontrarte."
    }
  },
  {
    nombre: "✅ Cuándo SÍ se borra",
    queEs: "Cuando la información es ANTIGUA, te perjudica HOY y ya no le importa a nadie más. Especialmente si la subió otra persona sin tu permiso. La regla mental es: si han pasado años, no hay interés público actual y solo te hace daño a ti → suele borrarse.",
    ejemplo: { tipo: 'bueno', texto: "✅ Hace 8 años, tú con 9 años saliste haciendo el tonto en un vídeo que subió un compañero a YouTube. Hoy buscas trabajo de monitor de campamento y el vídeo te perjudica. SE BORRA." },
    senales: [
      "Han pasado años desde que se publicó.",
      "Ya no hay interés periodístico actual.",
      "Te perjudica en tu vida actual (estudios, relaciones, trabajo)."
    ],
    quiz: {
      p: "Hace 8 años, Pablo (con 19 años) puso un comentario violento en un foro. Hoy busca trabajo. ¿Se borra?",
      opciones: ["SÍ se borra: información antigua sin interés actual", "NO se borra: la puso él voluntariamente", "Solo si pide perdón a la víctima"],
      correcta: 0,
      explica: "SÍ. Hace 8 años + comentario menor + le perjudica hoy. Caso clásico de borrado."
    }
  },
  {
    nombre: "❌ Cuándo NO se borra",
    queEs: "Cuando la información es VERAZ, ACTUAL e interesa a la comunidad. Sobre todo si la persona tiene cargo público (alcalde, ministro, famoso) y la información es sobre lo que hace en su cargo. Aquí pesa más el derecho de la gente a saber que el deseo personal de borrar.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Un alcalde EN ACTIVO pide borrar tweets suyos hablando de su programa político. NO SE BORRA: hay interés público en saber qué dijo y qué hace alguien que nos representa." },
    senales: [
      "La persona tiene proyección pública (alcalde, famoso, CEO).",
      "La información es sobre lo que hace EN PÚBLICO (no su vida privada).",
      "Existe interés legítimo de la gente en conocerla."
    ],
    quiz: {
      p: "Manuel es CEO de una empresa grande. Una web publica que ganó 480.000€ el año pasado (dato VERAZ del Registro Mercantil, que es público). Pide borrar el dato. ¿Se borra?",
      opciones: ["SÍ se borra: es su vida privada", "NO se borra: dato veraz, de fuente pública y con interés social", "Solo si la empresa quiebra"],
      correcta: 1,
      explica: "NO se borra. El Registro Mercantil es PÚBLICO por ley, el dato es VERDAD y un CEO tiene proyección pública. La gente tiene derecho a saberlo."
    }
  },
  {
    nombre: "⚠️ Casos especiales: lo falso no se 'olvida'",
    queEs: "El Derecho al Olvido es para información VERAZ que ya no merece estar. Si la información es FALSA (un bulo, una mentira), no se va por Derecho al Olvido: se va por otro camino: denuncia por difamación, rectificación, o directamente borrarlo de la web original.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Una web publica una mentira sobre ti: 'María copió en el examen' cuando NO copiaste. Esto NO es Derecho al Olvido (porque la información es FALSA). Es DIFAMACIÓN: se denuncia y se exige rectificación." },
    senales: [
      "Si lo que dicen sobre ti es VERDAD pero ya no debería estar → Derecho al Olvido.",
      "Si lo que dicen sobre ti es MENTIRA → es difamación, otro camino legal.",
      "Las sentencias firmes recientes también NO se borran: protegen a futuras víctimas."
    ],
    quiz: {
      p: "Una web publica una mentira sobre ti: dice que te suspendieron por copiar, cuando no es verdad. ¿Es Derecho al Olvido?",
      opciones: [
        "Sí, basta con pedir a Google que lo borre",
        "No: lo falso no se olvida, se rectifica o denuncia (difamación)",
        "Solo si tienes pruebas escritas"
      ],
      correcta: 1,
      explica: "Lo falso NO se va por Derecho al Olvido. Para mentiras hay otra ruta: pedir rectificación, denunciar por difamación, o exigir a la web que lo borre del origen."
    }
  }
];

// Mini-casos del juez (6 frases V/F · ¿SE BORRA o NO SE BORRA?)
const FRASES_VF = [
  { texto: "Pedro pide borrar un vídeo suyo bailando de hace 10 años (cuando tenía 7) que subió su prima sin permiso. Hoy le da vergüenza.",
    correcta: true,
    explica: "SE BORRA. Antiguo + lo subió otra persona sin su permiso + sin interés público actual. Caso clásico." },
  { texto: "Una alcaldesa EN ACTIVO pide borrar tweets suyos donde hablaba de su programa político como candidata.",
    correcta: false,
    explica: "NO SE BORRA. Hay interés público actual: la gente tiene derecho a saber qué dijo alguien que la representa." },
  { texto: "Una web publica una MENTIRA sobre ti: dice que te suspendieron por copiar (cosa que no es cierta). Pides Derecho al Olvido.",
    correcta: false,
    explica: "NO SE BORRA por Derecho al Olvido. Lo FALSO no se 'olvida': se denuncia por difamación o se pide rectificación a la web. Otro camino." },
  { texto: "Una foto tuya de la playa con 5 años, que subió una tía sin pedir permiso a tus padres, sigue saliendo en Google Imágenes. Pides borrarla.",
    correcta: true,
    explica: "SE BORRA. Antigua + sin permiso + dato personal sin interés público. Caso típico." },
  { texto: "Carlos fue CONDENADO por estafa hace 6 meses (sentencia firme reciente). Pide borrar la noticia.",
    correcta: false,
    explica: "NO SE BORRA. Es reciente, hay interés social (proteger a futuros clientes y avisar a la comunidad). Habría que esperar bastante tiempo." },
  { texto: "El sueldo de un CEO de una empresa importante aparece en el Registro Mercantil (que es público por ley). Él pide borrarlo de Google.",
    correcta: false,
    explica: "NO SE BORRA. El Registro Mercantil es PÚBLICO por ley. La gente tiene derecho a consultarlo." }
];

// ── TEORÍA (versión compacta) ───────────────────────────────────
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
  const nombres = { cadete: 'Ayudante', analista: 'Juez Junior', investigador: 'Juez Digital', detective: 'Guardián de la Privacidad' };
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

function _norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');}
function _tieneMin(texto, lista, min){var t=_norm(texto);var n=0;for(var i=0;i<lista.length;i++){if(t.indexOf(_norm(lista[i]))>=0)n++;}return n>=min;}

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
  // Validación por palabras clave (evita respuestas fuera de tema)
  var _kwFail = [];
  if (!_tieneMin(q2, ['hablar','pedir','borrar','denunciar','plataforma','google','permiso','quitar','reportar'], 2)) _kwFail.push('Pregunta 2: nombra pasos concretos (hablar con tu amigo, pedirle que lo borre, reportar a la plataforma/Google, denunciar…).');
  if (!_tieneMin(q3, ['interes publico','cargo','alcalde','ciudadano','privacidad','informacion','representa','publico'], 1)) _kwFail.push('Pregunta 3: usa la idea de "interés público" o el cargo público (alcalde) frente a un ciudadano normal.');
  if (_kwFail.length) {
    Academia.mostrarFeedback(document.getElementById('fb-informe'), 'mal',
      '<span class="et">✍️ Casi: concreta un poco más</span>Tu respuesta vale en longitud, pero falta nombrar las ideas clave.<br>· ' + _kwFail.join('<br>· '));
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
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'Guardián de la Privacidad' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}

function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'Guardián de la Privacidad',
    subtitulo: 'Sesión 12 · Tribunal Digital · Promoción 2026',
    icono: '⚖️',
    insignia: 'Guardián de la Privacidad',
    nombres: [n1, n2],
    sesionNum: 'S12',
    score: microquizAciertos.size + vfAciertos,
    total: CONCEPTOS.length + FRASES_VF.length,
    codigo: datos.codigo,
    frase: 'Lo que se borra en Google no desaparece de internet — pero deja de encontrarte'
  }, 'S12-tribunal-' + n1.replace(/\s/g, '_') + '.png');
}

// ── INIT ────────────────────────────────────────────────────────
function initSesion() {
  (function(){
    var b=document.getElementById('btn-reto-hecho');
    if(!b) return;
    var key='academia:reto:'+SESION_ID+':done';
    function unlock(){ if(b.dataset.locked==='1'){ b.disabled=false; b.dataset.locked='0'; b.textContent=b.dataset.label||'✓ He terminado'; } }
    try{ if(localStorage.getItem(key)==='1') unlock(); }catch(e){}
    window.addEventListener('message', function(ev){ if(ev&&typeof ev.data==='string'&&ev.data.indexOf('academia:reto-completado')===0) unlock(); });
    window.addEventListener('focus', function(){ try{ if(localStorage.getItem(key)==='1') unlock(); }catch(e){} });
    setInterval(function(){ try{ if(localStorage.getItem(key)==='1') unlock(); }catch(e){} }, 1500);
  })();
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


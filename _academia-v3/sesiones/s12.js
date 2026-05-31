/* S12-alt · Ciberacoso: qué hacer si te pasa · Academia Cyber-IES */
const SESION_ID = 's12';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    nombre: "Qué es el ciberacoso (y cómo se reconoce)",
    queEs: "Es usar el móvil o internet para hacer daño a alguien de forma REPETIDA: insultar, reírse, EXCLUIR a propósito, difundir rumores o fotos sin permiso, crear cuentas falsas para humillar (suplantación) o amenazar. Lo más duro es que no para al salir del instituto: te sigue al móvil, a todas horas. No es 'una broma': hace daño de verdad.",
    ejemplo: { tipo: 'peligroso', texto: "\u26a0\ufe0f En el grupo de clase varios empiezan a llamar 'pringado' a un compañero por una foto, otros la reenvían y se ríen. Y alguien crea una cuenta falsa con su nombre. Todo eso es ciberacoso." },
    senales: [
      "Es REPETIDO en el tiempo y busca hacer daño o humillar.",
      "Toma muchas formas: insultos, exclusión, rumores, fotos sin permiso, cuentas falsas.",
      "Ocurre por chats, redes o juegos online… y no da tregua ni en casa."
    ],
    quiz: {
      p: "¿Cuál de estas situaciones es ciberacoso?",
      opciones: [
        "Discrepar con un amigo una vez y luego arreglarlo",
        "Crear una cuenta falsa con la foto de un compañero para reírse de él",
        "Que te ganen en un videojuego online",
        "No contestar un mensaje porque estabas dormido"
      ],
      correcta: 1,
      explica: "El ciberacoso es repetido y busca dañar o humillar (aquí, suplantar a alguien con una cuenta falsa). No es una 'broma'."
    }
  },
  {
    nombre: "Qué hacer: PARA · GUARDA · BLOQUEA · CUENTA",
    queEs: "Si te pasa a ti, este es el plan: 1) PARA: no respondas al que acosa (responder es lo que busca). 2) GUARDA: haz capturas con fecha y nombre de usuario (son la prueba). 3) BLOQUEA y REPORTA a la persona/cuenta en la app. 4) CUENTA: habla con un adulto de confianza. Pedir ayuda NO es chivarse: es lo valiente.",
    ejemplo: { tipo: 'bueno', texto: "✅ Te llegan mensajes crueles de un desconocido. No respondes, haces capturas, bloqueas el número y se lo cuentas a tu tutora. Eso es actuar bien." },
    senales: [
      "PARA: no contestes ni te vengues; eso suele alargar el acoso.",
      "GUARDA pruebas antes de borrar nada.",
      "BLOQUEA, REPORTA a la app y CUÉNTASELO a un adulto de confianza."
    ],
    quiz: {
      p: "Recibes mensajes de acoso de un número desconocido. ¿Cuál es el primer paso?",
      opciones: [
        "Responder enfadado/a para que vea que no te callas",
        "No responder, guardar capturas, bloquear y contárselo a un adulto",
        "Reenviarlo a tus amigos para que opinen",
        "Borrarlo todo y no decir nada"
      ],
      correcta: 1,
      explica: "PARA · GUARDA · BLOQUEA · CUENTA. Responder da fuerza al acosador; borrar elimina las pruebas que necesitas."
    }
  },
  {
    nombre: "El testigo que ayuda (tú puedes parar esto)",
    queEs: "La mayoría de las veces hay testigos: gente que LO VE. Si los testigos se ríen o reenvían, el acoso crece. Si los testigos no reenvían, apoyan a la víctima y avisan a un adulto, el acoso suele PARAR. No hace falta ser un héroe: basta con no seguir la corriente y tender una mano.",
    ejemplo: { tipo: 'bueno', texto: "✅ Ves que se meten con un compañero en el grupo. No reenvías, le escribes en privado '¿estás bien?' y avisas a un profe. Has hecho de Escudo." },
    senales: [
      "No te rías ni reenvíes: eso alimenta el acoso.",
      "Apoya a quien lo sufre (aunque sea en privado).",
      "Avisa a un adulto: un testigo que actúa puede pararlo."
    ],
    quiz: {
      p: "Ves que en el grupo se ríen y reenvían burlas de un compañero. ¿Qué es lo mejor?",
      opciones: [
        "Reenviarlo también, total ya lo hacen todos",
        "No reenviar, apoyar al compañero y avisar a un adulto",
        "Reírte para no quedar mal con el grupo",
        "Mirar sin hacer nada"
      ],
      correcta: 1,
      explica: "El testigo que NO reenvía, apoya y avisa es clave: ahí es donde más casos de ciberacoso se frenan."
    }
  }
];

const FRASES_VF = [
  { texto: "El ciberacoso es repetido y busca hacer daño; por eso no es 'solo una broma'.",
    correcta: true,
    explica: "Verdadero. Es repetido y busca humillar o dañar. Llamarlo 'broma' quita importancia a algo que hace daño real." },
  { texto: "Si te acosan por mensajes, lo mejor es responder con otro insulto para que vean que no te callas.",
    correcta: false,
    explica: "Falso. Responder es lo que busca el acosador y suele alargarlo. El primer paso es PARAR: no responder." },
  { texto: "Antes de bloquear o borrar, conviene hacer capturas de los mensajes como prueba.",
    correcta: true,
    explica: "Verdadero. GUARDA las pruebas (capturas con fecha y usuario) antes de borrar: hacen falta para denunciar y pedir ayuda." },
  { texto: "Contarle a un adulto que están acosando a alguien es 'de chivatos'.",
    correcta: false,
    explica: "Falso. Pedir ayuda ante un acoso NO es chivarse: es protegerte (o proteger a otra persona) y es lo valiente." },
  { texto: "Crear una cuenta falsa con la foto de un compañero para humillarlo es una forma de ciberacoso.",
    correcta: true,
    explica: "Verdadero. Es suplantación de identidad, una forma de ciberacoso. Se reporta a la plataforma y se avisa a un adulto." },
  { texto: "Si soy testigo, reírme y reenviar las burlas no afecta a la víctima.",
    correcta: false,
    explica: "Falso. Reírse y reenviar hace MÁS daño y anima al acosador. El testigo que apoya y avisa es quien ayuda a parar el acoso." },
  { texto: "Bloquear a quien te acosa es 'de cobardes'.",
    correcta: false,
    explica: "Falso. Bloquear es una herramienta válida y recomendable: te quita de encima al acosador y no es ninguna cobardía." },
  { texto: "La mayoría del ciberacoso ocurre entre personas que se conocen (clase, instituto), no entre desconocidos.",
    correcta: true,
    explica: "Verdadero. Casi siempre el acoso viene de gente del entorno. Por eso cuesta tanto contarlo… y por eso es tan importante hacerlo." },
  { texto: "Reenviar una captura humillante 'solo a un amigo' también es participar en el acoso.",
    correcta: true,
    explica: "Verdadero. Cada reenvío amplía el daño. No difundir ya es ayudar." },
  { texto: "Si alguien sube una foto tuya sin permiso para burlarse, puedes pedir que la borren y reportarla a la app.",
    correcta: true,
    explica: "Verdadero. Tienes derecho a tu imagen: puedes exigir que la quiten, reportarla y avisar a un adulto." }
];

// ── TEORÍA ───────────────────────────────────────────────────────
let tarjetaActual = 0;
const microquizContestados = new Set();
const microquizAciertos = new Set();
let segTeoria = 0, segVF = 0, segReto = 0;
let mqFalladas = new Set(), vfFalladas = new Set(), retoCompletado = false;
function finTeoria(){ if (segTeoria === 0) otorgarInsignia('cadete'); }
function finVF(){ if (segVF === 0) otorgarInsignia('analista'); }

function reiniciarTeoria() {
  microquizContestados.clear();
  microquizAciertos.clear();
  segTeoria = 0; mqFalladas.clear();
  var bf = document.getElementById('barra-fin-teoria'); if (bf) bf.style.display = 'none';
  tarjetaActual = 0;
  renderTarjetas();
  irATarjeta(0);
  window.scrollTo({ top: 0, behavior: 'smooth' });
}
function reiniciarVF() {
  vfContestadas.clear();
  vfAciertos = 0;
  segVF = 0; vfFalladas.clear();
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
    finTeoria();
  }
}

function responderMicroquiz(idx, idxOp) {
  if (microquizContestados.has(idx)) return;
  const c = CONCEPTOS[idx].quiz;
  const fb = document.getElementById('fb-mq-' + idx);
  const botones = document.querySelectorAll('#opcionesMq-' + idx + ' button');
  if (idxOp === c.correcta) {
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
      finTeoria();
    }
    return;
  }
  // Teoría estricta: cualquier fallo vuelve al primer concepto (sin segunda oportunidad)
  botones.forEach(function(b){ b.disabled = true; });
  botones[idxOp].classList.add('incorrecta');
  fb.innerHTML = '❌ Fallaste. ' + c.explica + ' <b>En la teoría, un fallo y vuelves al PRIMER concepto.</b>';
  fb.dataset.activo = 'true';
  setTimeout(reiniciarTeoria, 1900);
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
        '<button onclick="responderVF(' + i + ',true)">✓ Verdadero</button>' +
        '<button onclick="responderVF(' + i + ',false)">✗ Falso</button>' +
      '</div>' +
      '<div class="explica-vf" id="exp-vf-' + i + '"></div>' +
    '</div>';
  }).join('');
  document.getElementById('vf-restantes').textContent = FRASES_VF.length;
}

function responderVF(idx, valor) {
  if (vfContestadas.has(idx)) return;
  const f = vfActuales[idx];
  const acertado = (valor === f.correcta);
  const cont = document.querySelector('.frase-vf[data-idx="' + idx + '"]');
  const botones = cont.querySelectorAll('.vf-botones button');
  const exp = document.getElementById('exp-vf-' + idx);
  if (acertado) {
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
      finVF();
    }
    return;
  }
  // En V/F (solo 2 opciones) no hay segunda oportunidad: cualquier fallo vuelve a la primera frase
  vfFallos++;
  document.getElementById('vf-fallos').textContent = vfFallos;
  botones.forEach(function(b){ b.disabled = true; });
  exp.innerHTML = '❌ Fallaste. ' + f.explica + ' <b>En el entrenamiento, un fallo y vuelves a la PRIMERA frase.</b>';
  exp.dataset.activo = 'true';
  setTimeout(reiniciarVF, 1900);
}

// ── RETO (iframe) ───────────────────────────────────────────────
function marcarRetoHecho() {
  const btn = document.getElementById('btn-reto-hecho');
  btn.disabled = true;
  btn.textContent = '✓ Reto completado';
  document.getElementById('barra-fin-juego').style.display = 'flex';
  Academia.setSesion(SESION_ID, { retoHecho: true });
}

// ── INSIGNIAS ───────────────────────────────────────────────────
const insigniasGanadas = new Set();
const INSIGNIA_NOMBRES = { cadete: 'Aliado/a', analista: 'Defensor/a', investigador: 'Escudo en acción', detective: 'Escudo Digital' };
const INSIGNIA_EMOJIS = { cadete: '🎖️', analista: '🎖️', investigador: '🎖️', detective: '🏆' };
function otorgarInsignia(nombre) {
  if (insigniasGanadas.has(nombre)) return;
  insigniasGanadas.add(nombre);
  const el = document.querySelector('.mi-insignia[data-mi="' + nombre + '"]');
  if (el) el.dataset.ganada = 'true';
  mostrarToast('Has ganado', INSIGNIA_EMOJIS[nombre] + ' ' + INSIGNIA_NOMBRES[nombre]);
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
  var totalSeg = segTeoria + segVF + segReto;
  var nota = Math.max(5, 10 - totalSeg);
  window._notaFinal = nota; window._segTotal = totalSeg;
  Academia.marcarCompletada(SESION_ID, nota, 10);
  Academia.setSesion(SESION_ID, { q1: q1, q2: q2, q3: q3, informeCompletado: true, nota: nota, segundas: totalSeg, tiempoMin: Math.round((Date.now() - tInicio) / 60000) });
  document.getElementById('res-teoria').textContent = (segTeoria === 0 ? 'Teoría: perfecta 🎖️' : 'Teoría: con ayuda (-' + segTeoria + ')');
  document.getElementById('res-entrenamiento').textContent = (segVF === 0 ? 'Entrenamiento: perfecto 🎖️' : 'Entrenamiento: con ayuda (-' + segVF + ')');
  document.getElementById('res-tiempo').textContent = (Math.round((Date.now() - tInicio) / 60000)) + ' min';
  const cod = Academia.codigoFinalizacion(SESION_ID, nota);
  document.getElementById('cod-final').textContent = 'CALIFICACIÓN: ' + nota + ' / 10  ·  ' + cod;
  Academia.setSesion(SESION_ID, { codigo: cod });
  var insEl = document.querySelector('.diploma-preview .insignia');
  if (insEl) insEl.textContent = (totalSeg === 0 ? 'Escudo Digital 🏆 (¡partida perfecta!)' : 'Diploma de participación · sin insignia (' + totalSeg + ' fallo' + (totalSeg===1?'':'s') + ')');
  Academia.rellenarIdentidad();
  if (totalSeg === 0) otorgarInsignia('detective');
  Academia.irABloque('diploma');
}

function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  var nota = (datos.nota != null) ? datos.nota : 10;
  var perfecto = (datos.segundas === 0);
  Academia.descargarDiploma({
    titulo: 'Escudo Digital',
    subtitulo: 'Sesión 12 (alt) · Ciberacoso · Promoción 2026',
    icono: '🛡️',
    insignia: perfecto ? 'Escudo Digital' : undefined,
    nombres: [n1, n2],
    sesionNum: 'S12',
    score: nota,
    total: 10,
    codigo: datos.codigo,
    frase: perfecto ? '¡Partida perfecta! Pedir ayuda no es chivarse: es lo valiente' : 'Misión completada. Nota: ' + nota + '/10'
  }, 'S12alt-escudo-' + n1.replace(/\s/g, '_') + '.png');
}

// ── INIT ────────────────────────────────────────────────────────
function initSesion() {
  (function(){
    var b=document.getElementById('btn-reto-hecho');
    if(!b) return;
    var key='academia:reto:'+SESION_ID+':done';
    var keySeg='academia:reto:'+SESION_ID+':seg';
    function unlock(){ if(b.dataset.locked==='1'){ b.disabled=false; b.dataset.locked='0'; b.textContent=b.dataset.label||'✓ He terminado'; } }
    function lsCheck(){ try{ if(localStorage.getItem(key)==='1'){ var s=parseInt(localStorage.getItem(keySeg),10); if(!isNaN(s)){ segReto=s; if(s===0) otorgarInsignia('investigador'); } retoCompletado=true; unlock(); } }catch(e){} }
    lsCheck();
    window.addEventListener('message', function(ev){ if(ev&&typeof ev.data==='string'&&ev.data.indexOf('academia:reto-completado')===0){ var parts=ev.data.split(':'); var n=parseInt(parts[3],10); if(!isNaN(n)) segReto=n; retoCompletado=true; if(segReto===0) otorgarInsignia('investigador'); unlock(); } });
    window.addEventListener('focus', lsCheck);
    setInterval(lsCheck, 1500);
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
if (document.readyState !== 'loading') initSesion();
else document.addEventListener('DOMContentLoaded', initSesion);

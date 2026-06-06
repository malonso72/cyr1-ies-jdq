/* S14 · IA, deepfakes y voces falsas · Academia Cyber-IES */
const SESION_ID = 's14';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    nombre: "¿Qué es un deepfake?",
    queEs: "Vídeo, imagen o audio creado por IA que parece real pero NO lo es. Antes hacían falta semanas y equipos profesionales. Hoy una app gratuita lo hace en minutos.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Un vídeo viral muestra al alcalde de tu ciudad diciendo cosas que NUNCA dijo. La cara y la voz parecen suyas. Solo lo delatan los bordes raros de la cara y los ojos que casi no parpadean." },
    senales: [
      "Aparece una persona conocida diciendo algo extraño o controvertido.",
      "Promete dinero, urgencia o premios sospechosos.",
      "El vídeo se difunde MUY rápido por WhatsApp/TikTok sin fuente oficial."
    ],
    quiz: {
      p: "Hoy en día, ¿cuánto cuesta crear un deepfake básico de un familiar tuyo?",
      opciones: [
        "Miles de euros y un equipo de profesionales",
        "Menos de 5 euros al mes con una app online",
        "Es imposible para una persona normal",
        "Solo lo pueden hacer empresas grandes"
      ],
      correcta: 1,
      explica: "Apps de IA generativa cuestan 3-5€/mes y crean deepfakes pasables con solo unas fotos tuyas y 30-60 segundos de audio. Por eso esta sesión importa."
    }
  },
  {
    nombre: "Voces clonadas",
    queEs: "Una IA puede CLONAR tu voz con solo 30-60 segundos de audio (un story de Instagram, un audio de WhatsApp, un TikTok). Después puede hacer que 'digas' cualquier cosa.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Estafadores tomaron 40 segundos de un vídeo público de Marcos en Instagram. Con esa muestra, una IA generó audios nuevos. Llamaron a su abuela llorando: 'Abuela, he chocado, mándame 3.000€'. Funcionó." },
    senales: [
      "Te llama un familiar 'llorando' pidiendo dinero urgente.",
      "La voz suena 'un poco rara' pero el contexto emocional justifica la rareza.",
      "Te pide NO contar nada a nadie ('no se lo digas a papá')."
    ],
    quiz: {
      p: "Tu abuelo recibe una llamada de tu primo 'llorando' pidiendo 3.000€. ¿Qué le aconsejas?",
      opciones: [
        "Que envíe el dinero rápido, por si acaso",
        "Que cuelgue y llame él al número HABITUAL del primo para confirmar",
        "Que pase la llamada a sus padres",
        "Que grabe la llamada para denunciar"
      ],
      correcta: 1,
      explica: "REGLA DE ORO: nunca confíes en el canal que te contacta. Verifica por el canal de SIEMPRE. Si es realmente tu primo, lo confirmarás en 30 segundos."
    }
  },
  {
    nombre: "Las 6 señales que delatan un deepfake",
    queEs: "Por muy bueno que sea, un deepfake casi siempre tiene pistas: ojos, bordes de la cara, sincronización labios-voz, iluminación incoherente, voz monótona, contexto sospechoso.",
    ejemplo: { tipo: 'bueno', texto: "✅ En un vídeo viral del 'alcalde' anunciando algo raro, te fijas: parpadea solo 2 veces en 30 segundos (las personas reales parpadean cada 4-5 segundos). DEEPFAKE." },
    senales: [
      "Ojos: parpadean menos o de forma rara.",
      "Bordes de la cara: líneas raras donde se une al pelo o cuello.",
      "Sincronización labios-voz: los labios no encajan del todo con lo que dice."
    ],
    quiz: {
      p: "¿Cuál de estas NO es una señal de deepfake?",
      opciones: [
        "Los ojos casi no parpadean",
        "El audio tiene música de fondo",
        "Las sombras de la cara no coinciden con la luz",
        "La voz suena monótona, sin emoción"
      ],
      correcta: 1,
      explica: "La música de fondo es normal en muchos vídeos. Las 6 señales reales: ojos, bordes, sincronización, iluminación, voz monótona y contexto sospechoso (te pide dinero/urgencia)."
    }
  },
  {
    nombre: "¿Por qué nos engañan?",
    queEs: "Los deepfakes funcionan no porque sean perfectos, sino porque atacan en momentos EMOCIONALES (urgencia, miedo, alegría). El cerebro emocional bloquea al cerebro racional. Por eso usan llamadas 'llorando' o noticias 'escandalosas'.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Doña Encarna (78 años) reconoce que la voz 'sonaba un poco rara', pero 'estaba llorando, claro'. La urgencia + la emoción + el contexto familiar le hicieron pagar antes de verificar." },
    senales: [
      "Te meten URGENCIA: 'tienes que actuar AHORA'.",
      "Activan EMOCIÓN fuerte: miedo, amor, alegría, vergüenza.",
      "Te piden SECRETISMO: 'no se lo digas a nadie'."
    ],
    quiz: {
      p: "El deepfake más efectivo NO es el más realista, es el que…",
      opciones: [
        "Tiene mejor calidad de imagen",
        "Te pilla en un momento emocional (miedo, urgencia, alegría)",
        "Usa famosos",
        "Es más largo"
      ],
      correcta: 1,
      explica: "La emoción bloquea el pensamiento crítico. Por eso la regla práctica más útil es: si te meten prisa o te emocionan, PARA y verifica. La calma es tu mejor antivirus."
    }
  }
];

// Entrenamiento V/F (6 frases sobre deepfakes)
const FRASES_VF = [
  { texto: "Para clonar la voz de alguien por IA hacen falta varias HORAS de audio.", correcta: false,
    explica: "Falso. Bastan 30-60 segundos de audio público (un story de Instagram, un TikTok). Por eso publicar muchos vídeos hablando a cámara es un riesgo." },
  { texto: "Los deepfakes perfectos ya existen y son imposibles de detectar a ojo.", correcta: false,
    explica: "Falso. Aunque mejoran cada año, casi siempre dejan pistas: ojos, bordes, sincronización, iluminación, voz monótona. Y sobre todo el CONTEXTO sospechoso." },
  { texto: "Si un familiar te llama 'llorando' pidiendo dinero, ANTES de pagar deberías llamar tú al número de SIEMPRE de esa persona.", correcta: true,
    explica: "Verdadero. Es la regla de oro contra voces clonadas: verifica por el canal habitual, no por el que te llamó." },
  { texto: "Las apps para crear deepfakes son ilegales y muy caras.", correcta: false,
    explica: "Falso. Muchas son gratuitas o cuestan 3-5€/mes. Y el USO ético (entretenimiento, parodia con consentimiento) es legal; lo ilegal es suplantar identidad para estafar." },
  { texto: "Subir vídeos largos hablando a cámara en TikTok aumenta el riesgo de que clonen tu voz.", correcta: true,
    explica: "Verdadero. Cuanto más audio tuyo público haya, más fácil para una IA reproducir tu voz." },
  { texto: "Los deepfakes funcionan porque son técnicamente perfectos.", correcta: false,
    explica: "Falso. Funcionan porque atacan en momentos EMOCIONALES (urgencia, miedo). La calma es tu mejor defensa: si te meten prisa, sospecha." }
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
}

function navSub(idx, delta) {
  const t = document.querySelector('.tarjeta-teoria[data-idx="' + idx + '"]');
  const subs = t.querySelectorAll('.subtarjeta');
  let actual = -1;
  subs.forEach(function(s, i) { if (s.dataset.activa === 'true') actual = i; });
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
  if (nuevo === 2) {
    btnN.textContent = !microquizContestados.has(idx) ? '🔒 Responde el microquiz' : (idx === CONCEPTOS.length - 1 ? 'A entrenar ▸' : 'Siguiente concepto ▸');
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
  if (idx === CONCEPTOS.length - 1 && microquizContestados.has(idx)) {
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
  btnN.textContent = idx === CONCEPTOS.length - 1 ? 'A entrenar ▸' : 'Siguiente concepto ▸';
  btnN.disabled = false;
  document.querySelectorAll('.puntos-tarjetas .punto').forEach(function(p, i) { if (i === idx) p.classList.add('visto'); });
  if (idx === CONCEPTOS.length - 1) {
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
  const nombres = { cadete: 'Cadete', analista: 'Analista', investigador: 'Forense', detective: 'Cazador de Deepfakes' };
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
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'Cazador de Deepfakes' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}

function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'Cazador de Deepfakes',
    subtitulo: 'Sesión 14 · IA, deepfakes y voces falsas · Promoción 2026',
    icono: '🎬',
    insignia: 'Cazador de Deepfakes',
    nombres: [n1, n2],
    sesionNum: 'S14',
    score: microquizAciertos.size + vfAciertos,
    total: CONCEPTOS.length + FRASES_VF.length,
    codigo: datos.codigo,
    frase: 'Si te promete dinero fácil o te mete prisa, mira por qué tiene tanta prisa'
  }, 'S14-realfake-' + n1.replace(/\s/g, '_') + '.png');
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


/* S17 · Caso Marta Ruiz · Fraude bancario */
const SESION_ID = 's17';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    nombre: "Phishing por email + smishing por SMS",
    queEs: "La estafa empieza con un email del 'banco' avisando de una operación sospechosa. A los minutos llega un SMS con un código 'para verificar'. Ambos son señuelos: el email te asusta, el SMS te da credibilidad.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Marta recibió: 'BBVA · Detectamos una compra de 738€ en Amazon UK. Si no eres tú, contacta INMEDIATAMENTE'. Pinchó. Una página IDÉNTICA a la del BBVA le pidió usuario y clave." },
    senales: [
      "El email crea PÁNICO con una operación inexistente.",
      "El SMS llega justo después para dar 'autenticidad'.",
      "El enlace lleva a una URL similar pero NO IGUAL a la del banco real."
    ],
    quiz: {
      p: "Recibes un email del banco diciendo que hay una compra sospechosa con tu tarjeta. ¿Qué haces PRIMERO?",
      opciones: [
        "Pincho el enlace del email para verificar",
        "Cuelgo (si es llamada) o cierro el email, y entro a la app del banco POR MI CUENTA",
        "Reenvío el email a un amigo para que opine",
        "Llamo al número de teléfono que aparece en el email"
      ],
      correcta: 1,
      explica: "NUNCA uses los enlaces o teléfonos del propio mensaje sospechoso: pueden llevarte a webs/llamadas falsas. Entra a tu banco por TU ruta de siempre (app, web bookmarkeada, teléfono detrás de tu tarjeta)."
    }
  },
  {
    nombre: "Vishing — la estafa por llamada",
    queEs: "Vishing = Voice + phishing. El estafador llama haciéndose pasar por tu gestor del banco. Usa tu nombre real (lo sacó de la web falsa) y datos que parecen internos. La llamada da SENSACIÓN DE OFICIALIDAD.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ A los 30 minutos del email, llaman a Marta. 'Soy Pedro Sánchez, su gestor del BBVA de Granada. Hemos detectado el intento de fraude. Para protegerla vamos a hacer una transferencia inversa…'. Voz tranquila, profesional, sabe su nombre." },
    senales: [
      "Te llaman ELLOS (no llamas tú).",
      "Conocen tu nombre y algún dato (porque te los acabas de dar en el email).",
      "Tono profesional pero CON URGENCIA: tienes que actuar AHORA."
    ],
    quiz: {
      p: "Tu 'gestor del banco' te llama pidiéndote autorizar una operación para 'proteger tu cuenta'. ¿Qué haces?",
      opciones: [
        "Le obedezco porque suena oficial",
        "Cuelgo y llamo YO al número oficial del banco (el que aparece detrás de mi tarjeta) para verificar",
        "Le pido que me llame mi padre",
        "Le digo que me lo mande por email"
      ],
      correcta: 1,
      explica: "REGLA DE ORO: nunca confíes en el canal que te contacta. Cuelga, busca el número oficial (detrás de tu tarjeta) y llama TÚ. Tu banco real no se ofende: te lo agradecerá."
    }
  },
  {
    nombre: "Aislamiento — 'no se lo diga a nadie'",
    queEs: "Los estafadores te piden NO contar nada a tu familia 'para no asustarlos' o 'porque es confidencial bancario'. Es manipulación pura: te aíslan para que nadie te frene. Si te piden secretismo, ES estafa con 99% de probabilidad.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ 'Por favor, no se lo cuente a su hija durante la operación: cualquier interrupción reinicia el protocolo de seguridad y tendríamos que empezar de cero'. Marta no llamó a nadie. Si lo hubiera hecho, se hubiera dado cuenta." },
    senales: [
      "Te piden no contar nada (a familia, pareja, amigos).",
      "Justifican el secretismo con excusas técnicas o legales.",
      "Te dicen que cualquier interrupción 'estropea el proceso'."
    ],
    quiz: {
      p: "El gestor te dice 'no le cuente esto a su familia hasta que terminemos'. ¿Qué pensar?",
      opciones: [
        "Tiene razón, mejor no preocupar a nadie",
        "Es señal CLARÍSIMA de estafa. Un banco real NUNCA te pide eso",
        "Voy a guardar el secreto solo media hora",
        "Le digo que sí pero llamo a mi padre igualmente"
      ],
      correcta: 1,
      explica: "Es regla de oro: si te piden SECRETISMO, es estafa. Los bancos reales prefieren que su cliente verifique con su familia. Quien te aísla es quien quiere engañarte."
    }
  },
  {
    nombre: "Verificación cruzada — la mejor defensa",
    queEs: "Cuelga. Respira. Llama TÚ al número OFICIAL del banco. Es la única regla que funciona contra TODOS los tipos de estafa (vishing, suplantación, deepfakes, urgencia). Si la persona real era de verdad tu banco, no se enfadará: te felicitará por la prudencia.",
    ejemplo: { tipo: 'bueno', texto: "✅ Si Marta hubiera colgado y llamado al número oficial del BBVA (detrás de su tarjeta), el banco real le habría dicho 'no, no hay ninguna operación sospechosa' y la estafa se habría detenido en 2 minutos." },
    senales: [
      "El número oficial del banco está en TU tarjeta, en TU app, en TU contrato.",
      "NUNCA confíes en el número que te llama o que te aparece en pantalla (se puede falsificar).",
      "5 minutos verificando salvan 4.800€."
    ],
    quiz: {
      p: "¿Cuál es la regla más eficaz contra el vishing y la suplantación bancaria?",
      opciones: [
        "Grabar la llamada para denunciar",
        "Colgar y llamar TÚ al número oficial del banco para verificar",
        "Hablar con el estafador para sacarle información",
        "Cambiar de cuenta bancaria por si acaso"
      ],
      correcta: 1,
      explica: "La verificación cruzada. Es la única regla que neutraliza prácticamente cualquier ataque social: cambiar tú el canal por uno que YA conoces como auténtico."
    }
  }
];

// Entrenamiento V/F (6 frases sobre fraude bancario)
const FRASES_VF = [
  { texto: "Un banco real puede llamarte y pedirte tu PIN completo, tu CVV o tu clave de operaciones por teléfono.", correcta: false,
    explica: "Falso. Los bancos reales NUNCA piden esos datos por teléfono. Si te los piden, es estafa segura." },
  { texto: "El número de teléfono de quien te llama puede ser FALSIFICADO para que parezca el del banco (caller ID spoofing).", correcta: true,
    explica: "Verdadero. Los estafadores pueden hacer que en tu pantalla aparezca el número oficial del banco aunque ellos no llamen desde ahí. No te fíes del número que ves." },
  { texto: "Si una persona del banco te pide NO contarle nada a tu familia 'por confidencialidad', es señal clarísima de estafa.", correcta: true,
    explica: "Verdadero. Los bancos reales prefieren que verifiques con tu familia. El secretismo es manipulación pura para aislarte." },
  { texto: "Las transferencias por Bizum se pueden cancelar fácilmente si llamas al banco a tiempo.", correcta: false,
    explica: "Falso. Bizum son INMEDIATAS e irreversibles. Por eso los estafadores las usan: una vez pulsas, el dinero ya no es tuyo." },
  { texto: "La regla más efectiva contra el vishing es: COLGAR y llamar TÚ al número oficial del banco.", correcta: true,
    explica: "Verdadero. Cambias tú el canal por uno auténtico. Es la regla de oro." },
  { texto: "Solo las personas mayores caen en estafas tipo vishing; los jóvenes están a salvo.", correcta: false,
    explica: "Falso. Cualquiera puede caer bajo presión emocional. La edad protege menos que conocer las reglas y verificar siempre." }
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
  const nombres = { cadete: 'Cadete', analista: 'Analista', investigador: 'Investigador', detective: 'Investigador de Fraudes' };
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
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'Investigador de Fraudes' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}

function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'Investigador de Fraudes',
    subtitulo: 'Sesión 17 · Caso Marta Ruiz · Promoción 2026',
    icono: '📁',
    insignia: 'Investigador de Fraudes',
    nombres: [n1, n2],
    sesionNum: 'S17',
    score: microquizAciertos.size + vfAciertos,
    total: CONCEPTOS.length + FRASES_VF.length,
    codigo: datos.codigo,
    frase: 'El banco que te llama no es el banco. El banco al que tú llamas, sí'
  }, 'S17-marta-' + n1.replace(/\s/g, '_') + '.png');
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


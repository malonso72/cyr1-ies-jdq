/* S04 · Lo que internet sabe de ti · Academia Cyber-IES */
const SESION_ID = 's04';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    "nombre": "¿Qué es la huella digital?",
    "queEs": "Todo lo que internet \"sabe\" sobre ti: tus cuentas, tu nombre, tus comentarios, tus fotos, tus contraseñas filtradas, tu historial de búsquedas… Mucho de eso lo dejas TÚ sin querer.",
    "ejemplo": {
      "tipo": "peligroso",
      "texto": "⚠️ Buscas tu nombre en Google y aparece: una foto antigua, un comentario en YouTube de hace 3 años, tu cuenta de TikTok pública, tu email asociado a un foro de hace 5 años. Todo eso es huella digital."
    },
    "senales": [
      "Es la suma de TODO lo que has subido a internet (y de lo que han subido sobre ti).",
      "Se acumula: cada año hay más, y casi nunca disminuye.",
      "Otros pueden investigarla (OSINT) y construir un perfil tuyo."
    ],
    "quiz": {
      "p": "¿Qué NO es parte de tu huella digital?",
      "opciones": [
        "Tu cuenta de Instagram",
        "Una contraseña tuya filtrada en una web vieja",
        "Tu altura",
        "Tu historial de búsquedas en Google"
      ],
      "correcta": 2,
      "explica": "Tu altura es un dato físico, no digital. Lo demás (cuentas, contraseñas filtradas, historial) sí está en tu huella."
    }
  },
  {
    "nombre": "Have I Been Pwned (HIBP)",
    "queEs": "haveibeenpwned.com es una web gratis que te dice si tu email o tu contraseña han aparecido en filtraciones públicas. Si salen → cambia esa contraseña en todas las cuentas donde la usabas.",
    "ejemplo": {
      "tipo": "bueno",
      "texto": "✅ Metes tu email y te dice \"apareciste en la filtración de LinkedIn 2021\". Vas a LinkedIn, cambias contraseña, activas 2FA y compruebas dónde más usabas esa misma contraseña."
    },
    "senales": [
      "Te dice EN QUÉ webs apareció (LinkedIn, Adobe, Dropbox…) y CUÁNDO.",
      "Te dice QUÉ datos se filtraron: email, contraseña, número de teléfono…",
      "Si tu contraseña aparece: nunca la vuelvas a usar en ningún sitio."
    ],
    "quiz": {
      "p": "HIBP te dice que tu email apareció en una filtración con contraseña. ¿Qué haces?",
      "opciones": [
        "Nada, es de hace mucho tiempo",
        "Cambio esa contraseña en TODAS las cuentas donde la usaba y activo 2FA",
        "Cierro mi email",
        "Llamo a la policía"
      ],
      "correcta": 1,
      "explica": "Cambia la contraseña filtrada en TODAS las cuentas donde la reutilizabas (por eso no hay que reutilizar). Y activa 2FA."
    }
  },
  {
    "nombre": "Google My Activity",
    "queEs": "myactivity.google.com es donde Google guarda TODO lo que haces con tu cuenta: búsquedas, vídeos vistos, sitios visitados, ubicaciones. Puedes ver lo que tiene de ti y borrarlo.",
    "ejemplo": {
      "tipo": "bueno",
      "texto": "✅ Entras y ves que Google sabe que el martes a las 16:30 buscaste \"regalo cumple amigo\" y luego \"Amazon zapatillas\". Lo borras todo o ajustas cuánto tiempo guarda Google ese historial."
    },
    "senales": [
      "Te muestra una línea temporal de toda tu actividad con Google.",
      "Puedes borrar entradas concretas o todo a la vez.",
      "Puedes configurar que Google deje de guardar este historial."
    ],
    "quiz": {
      "p": "¿Por qué interesa mirar Google My Activity?",
      "opciones": [
        "Para denunciar a Google",
        "Para ver qué guarda de ti y decidir si quieres borrarlo",
        "Para subir más datos",
        "Para cambiar tu email"
      ],
      "correcta": 1,
      "explica": "Es tu derecho ver y borrar el historial. Mucha gente no sabe siquiera que existe."
    }
  },
  {
    "nombre": "WhatsMyName",
    "queEs": "whatsmyname.app busca un nombre de usuario tuyo (ej. tu @ de Insta) en cientos de webs y te dice EN CUÁLES existe ese mismo usuario. Te enseña tu rastro multiplataforma.",
    "ejemplo": {
      "tipo": "bueno",
      "texto": "✅ Buscas tu @luciagarcia2012 y descubres que ese mismo nombre existe en TikTok, Twitch, GitHub, foros antiguos… Algunas ni te acuerdas de haber creado."
    },
    "senales": [
      "Usar el MISMO nombre en muchas webs crea un rastro fácil de seguir.",
      "Cada web encontrada es un punto de entrada para alguien que te investigue.",
      "Si quieres ser anónimo: usa nombres DISTINTOS en cada cuenta."
    ],
    "quiz": {
      "p": "¿Cuál es el mayor riesgo de usar SIEMPRE el mismo nombre de usuario en todas las redes?",
      "opciones": [
        "Que se te olvide",
        "Que cualquiera te localice en todas las webs cruzando ese nombre",
        "Que no funcione",
        "Ningún riesgo"
      ],
      "correcta": 1,
      "explica": "Es el principio del OSINT: con un nombre único de usuario, un investigador (o un acosador) puede mapear toda tu vida online."
    }
  }
];

const FRASES_VF = [
  {
    "texto": "Tu huella digital se acumula con los años y casi nunca disminuye.",
    "correcta": true,
    "explica": "Verdadero. Lo que subes hoy puede seguir ahí en 10 años."
  },
  {
    "texto": "Have I Been Pwned (HIBP) es una web fiable que te dice si tu email ha aparecido en filtraciones.",
    "correcta": true,
    "explica": "Verdadero. Es gratis, conocida y usada también por profesionales de seguridad."
  },
  {
    "texto": "Google MyActivity es donde Google guarda secretamente tu historial sin que puedas verlo.",
    "correcta": false,
    "explica": "Falso. Puedes ENTRAR cuando quieras, ver QUÉ guarda y borrarlo. Es tu derecho."
  },
  {
    "texto": "Usar el mismo nombre de usuario en todas las redes facilita que cualquiera te encuentre y construya tu perfil.",
    "correcta": true,
    "explica": "Verdadero. Es la primera técnica de OSINT."
  },
  {
    "texto": "Si HIBP dice 0 resultados, mi email NUNCA se filtrará en el futuro.",
    "correcta": false,
    "explica": "Falso. HIBP solo conoce filtraciones públicas pasadas. Mañana puede haber una nueva."
  },
  {
    "texto": "Lo que publico en internet con 12 años puede afectarme cuando busque trabajo con 22.",
    "correcta": true,
    "explica": "Verdadero. La huella digital persiste. Lo que parece \"una tontería\" puede llegar a empresas, universidades, futuras parejas."
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
}
function navSub(idx, delta) {
  const t = document.querySelector('.tarjeta-teoria[data-idx="' + idx + '"]');
  const subs = t.querySelectorAll('.subtarjeta');
  let actual = -1; subs.forEach(function(s, i) { if (s.dataset.activa === 'true') actual = i; });
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
  if (nuevo === 2) { btnN.textContent = !microquizContestados.has(idx) ? '🔒 Responde el microquiz' : (idx === CONCEPTOS.length - 1 ? 'A entrenar ▸' : 'Siguiente concepto ▸'); btnN.disabled = !microquizContestados.has(idx); }
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
  if (idx === CONCEPTOS.length - 1 && microquizContestados.has(idx)) { otorgarInsignia('cadete'); }
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
  const nombres = {"cadete": "Cadete", "analista": "Investigador", "investigador": "Auditor Junior", "detective": "Auditor de Huella Digital"};
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
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'Auditor de Huella Digital' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}
function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'Auditor de Huella Digital',
    subtitulo: 'Sesión 4 · Lo que internet sabe de ti · Promoción 2026',
    icono: '🔎',
    insignia: 'Auditor de Huella Digital',
    nombres: [n1, n2],
    sesionNum: 'SESION4',
    score: microquizAciertos.size + vfAciertos,
    total: CONCEPTOS.length + FRASES_VF.length,
    codigo: datos.codigo,
    frase: 'Lo que pones en internet hoy, te encontrará dentro de 10 años'
  }, 'S04-huella-digital-' + n1.replace(/\s/g, '_') + '.png');
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

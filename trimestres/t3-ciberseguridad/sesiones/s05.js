/* S05 · Misión Interland (parte 1) · Academia Cyber-IES */
const SESION_ID = 's05';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    "nombre": "Principio 1 — Comparte con cabeza",
    "queEs": "Antes de subir algo a internet, pregúntate: ¿lo enseñaría a mis padres? ¿a mi profesor? ¿al jefe del trabajo que tendré en 10 años? Si NO → no lo subas.",
    "ejemplo": {
      "tipo": "bueno",
      "texto": "✅ Vas a subir una foto graciosa de un amigo sin pedirle permiso. Antes de pulsar \"publicar\" piensas: \"¿le gustaría a él que la subiera?\". Si dudas → le preguntas. Si dice no → no la subes."
    },
    "senales": [
      "Lo que subes hoy puede verse para SIEMPRE.",
      "Puede afectar a OTRAS personas que aparecen.",
      "En caliente (enfadado, eufórico) NUNCA es buen momento para publicar."
    ],
    "quiz": {
      "p": "Antes de publicar algo en redes, lo más importante es preguntarse:",
      "opciones": [
        "¿Tendrá muchos likes?",
        "¿Lo enseñaría a alguien de confianza fuera de las redes?",
        "¿Está bien iluminado?",
        "¿Se ve mi cara?"
      ],
      "correcta": 1,
      "explica": "Si solo lo enseñarías a un grupo MUY limitado, mejor no lo subas a una red pública."
    }
  },
  {
    "nombre": "Principio 2 — No caigas en la trampa",
    "queEs": "Internet está lleno de bulos, fake news y phishing. Aprende a detectarlos: comprueba la fuente, busca el mismo dato en medios serios, sospecha de lo que te enfurece o asusta.",
    "ejemplo": {
      "tipo": "peligroso",
      "texto": "⚠️ Tu primo te manda por WhatsApp un vídeo \"filtrado\" donde un famoso dice algo escandaloso. Antes de reenviarlo: ¿de dónde sale? ¿lo dicen otros medios? ¿es un deepfake?"
    },
    "senales": [
      "El titular te indigna o te asusta MUCHO.",
      "Te llega por WhatsApp/redes pero no aparece en ningún medio serio.",
      "Te piden compartirlo \"antes de que lo borren\"."
    ],
    "quiz": {
      "p": "Te llega por WhatsApp un vídeo \"escandaloso\". ¿Qué haces ANTES de compartir?",
      "opciones": [
        "Lo reenvío rápido a mi grupo",
        "Verifico que aparezca también en un medio serio (RTVE, El País, BBC)",
        "Lo comparto solo a familia",
        "Espero a ver si alguien lo borra"
      ],
      "correcta": 1,
      "explica": "Si no aparece en medios serios, casi seguro es bulo. Compartirlo te convierte en cómplice del bulo."
    }
  },
  {
    "nombre": "Las reacciones rápidas son el truco",
    "queEs": "Tanto los bulos como el phishing dependen de que actúes RÁPIDO sin pensar. Si te piden compartir/pinchar/responder YA, casi siempre es trampa.",
    "ejemplo": {
      "tipo": "peligroso",
      "texto": "⚠️ \"Comparte este vídeo en 24 horas o lo borrarán\". \"Tu cuenta se cierra si no verificas YA\". La urgencia es la pista número 1 del engaño."
    },
    "senales": [
      "Plazo corto (\"en X horas\", \"antes de mañana\").",
      "Apelación emocional fuerte (miedo, rabia, codicia).",
      "Pedido de compartir/pinchar inmediato."
    ],
    "quiz": {
      "p": "Lo que tienen en común el phishing, los bulos y las estafas en redes es:",
      "opciones": [
        "Llegan por email",
        "Te meten prisa para que actúes sin pensar",
        "Vienen de gente desconocida",
        "Tienen errores de ortografía"
      ],
      "correcta": 1,
      "explica": "La URGENCIA es el truco número uno. La calma es tu defensa."
    }
  },
  {
    "nombre": "El silencio también es una opción",
    "queEs": "No tienes que opinar de todo. No tienes que reaccionar a cada provocación. Pasar de un comentario tóxico es una habilidad: en internet, el SILENCIO es a veces la respuesta más fuerte.",
    "ejemplo": {
      "tipo": "bueno",
      "texto": "✅ Alguien te insulta en un comentario de TikTok. En vez de responder y enfadarte, lo BLOQUEAS y sigues con tu vida. Le quitas todo el poder."
    },
    "senales": [
      "Responder a un trol le da más visibilidad y energía.",
      "Bloquear/silenciar es siempre legítimo.",
      "No tienes que justificar a nadie por qué bloqueas."
    ],
    "quiz": {
      "p": "Un desconocido te deja un comentario insultante en TikTok. ¿Qué haces?",
      "opciones": [
        "Le respondo con otro insulto",
        "Lo bloqueo y sigo a lo mío",
        "Pido a mis amigos que también le insulten",
        "Borro mi cuenta"
      ],
      "correcta": 1,
      "explica": "Bloquear lo silencia para ti y le quita la atención que buscaba. Es la respuesta más eficaz."
    }
  }
];

const FRASES_VF = [
  {
    "texto": "Lo que subes a internet con 12 años puede verlo todavía un futuro jefe cuando tengas 25.",
    "correcta": true,
    "explica": "Verdadero. La huella digital persiste años. Por eso \"compartir con cabeza\" importa."
  },
  {
    "texto": "Si un bulo te lo manda un amigo de confianza, es seguro reenviarlo.",
    "correcta": false,
    "explica": "Falso. Tu amigo puede haberse equivocado. Verifica TÚ la fuente antes de propagarlo."
  },
  {
    "texto": "La urgencia (\"comparte AHORA antes de que lo borren\") es la señal número 1 de bulo o estafa.",
    "correcta": true,
    "explica": "Verdadero. La urgencia bloquea el pensamiento crítico. Es la trampa más usada."
  },
  {
    "texto": "Si te insultan en redes, lo MÁS eficaz es responder con otro insulto para defenderte.",
    "correcta": false,
    "explica": "Falso. Responder alimenta al trol. Bloquear/silenciar es más eficaz."
  },
  {
    "texto": "Compartir algo que NO has verificado te convierte en cómplice de su difusión si resulta ser falso.",
    "correcta": true,
    "explica": "Verdadero. Cuando compartes asumes parte de la responsabilidad."
  },
  {
    "texto": "Bloquear a alguien en redes requiere justificar por qué lo haces.",
    "correcta": false,
    "explica": "Falso. Es tu derecho. No tienes que explicarte ante nadie."
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
  const nombres = {"cadete": "Cadete", "analista": "Aprendiz", "investigador": "Aventurero", "detective": "Explorador de Interland"};
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
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'Explorador de Interland' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}
function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'Explorador de Interland',
    subtitulo: 'Sesión 5 · Misión Interland (parte 1) · Promoción 2026',
    icono: '🌍',
    insignia: 'Explorador de Interland',
    nombres: [n1, n2],
    sesionNum: 'SESION5',
    score: microquizAciertos.size + vfAciertos,
    total: CONCEPTOS.length + FRASES_VF.length,
    codigo: datos.codigo,
    frase: 'En Interland, como en internet, ser amable es la primera regla de seguridad'
  }, 'S05-interland-p1-' + n1.replace(/\s/g, '_') + '.png');
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

/* S06 · Misión Interland (parte 2) · Academia Cyber-IES */
const SESION_ID = 's06';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    "nombre": "Principio 3 — Sé amable",
    "queEs": "En internet hay troles, ciberacosadores, gente cruel. Tu mejor defensa NO es ser igual: es bloquear, denunciar, no responder, y no convertirte tú en uno de ellos.",
    "ejemplo": {
      "tipo": "bueno",
      "texto": "✅ Un compañero te insulta en un grupo. NO le respondes con otro insulto. Sales del grupo, lo bloqueas si insiste, y se lo cuentas a un adulto."
    },
    "senales": [
      "Ser cruel desde un teclado es MÁS fácil que cara a cara (el \"efecto desinhibición\").",
      "Un trol busca reacción: si no la das, pierde poder.",
      "Si TÚ eres el agresor: nunca es \"broma\" si la otra persona no se ríe."
    ],
    "quiz": {
      "p": "Un compañero de clase recibe burlas constantes en redes. ¿Qué haces TÚ?",
      "opciones": [
        "Me río con los demás para no quedar mal",
        "Le hablo en privado para apoyarlo y reporto las burlas en la red",
        "Me callo y miro",
        "Comparto las burlas"
      ],
      "correcta": 1,
      "explica": "No ser cómplice + apoyo en privado + reporte a la plataforma. Las víctimas necesitan UN aliado."
    }
  },
  {
    "nombre": "Principio 4 — Asegura tus cuentas",
    "queEs": "Cada cuenta tuya merece una contraseña FUERTE y ÚNICA. Y el 2FA donde se pueda. Eso te protege contra el 95% de los hackeos.",
    "ejemplo": {
      "tipo": "bueno",
      "texto": "✅ En Instagram pones una frase de paso (\"caballo-mesa-luna-puente-7\") + activas el 2FA por SMS. Aunque te roben la contraseña, sin tu móvil no entran."
    },
    "senales": [
      "Contraseña LARGA (15+ caracteres) es mejor que corta con símbolos.",
      "CADA cuenta importante: contraseña ÚNICA.",
      "Activa 2FA en email, banco, redes sociales."
    ],
    "quiz": {
      "p": "La mejor defensa contra que te hackeen una cuenta es:",
      "opciones": [
        "Cambiar de teléfono",
        "Contraseña ÚNICA y FUERTE + 2FA",
        "No usar internet",
        "Tener antivirus caro"
      ],
      "correcta": 1,
      "explica": "Contraseña única + 2FA bloquean la mayoría de ataques. Sin esto, todo lo demás vale menos."
    }
  },
  {
    "nombre": "Denunciar también es responsabilidad",
    "queEs": "Las plataformas (Insta, TikTok, YouTube) tienen botones de DENUNCIA. Úsalos. Si todos denunciamos lo tóxico, las plataformas lo retiran más rápido.",
    "ejemplo": {
      "tipo": "bueno",
      "texto": "✅ Ves un comentario racista o de acoso a alguien. En Instagram: 3 puntos → Denunciar → Acoso. Tarda 5 segundos y ayuda."
    },
    "senales": [
      "Toda red social tiene botón de denuncia (los 3 puntos del post/comentario).",
      "Las denuncias son anónimas: el agresor no sabe quién lo denunció.",
      "Cuanta más gente denuncie un contenido, más rápido lo retira la plataforma."
    ],
    "quiz": {
      "p": "Ves un comentario de acoso a un compañero en Instagram. ¿Qué haces?",
      "opciones": [
        "Lo ignoro, no es asunto mío",
        "Pulso los 3 puntos del comentario y lo denuncio por acoso",
        "Lo comparto",
        "Comento riéndome"
      ],
      "correcta": 1,
      "explica": "Denunciar es anónimo, rápido y útil. Si todos lo hacemos, las plataformas actúan."
    }
  },
  {
    "nombre": "Pedir ayuda NO es cobardía",
    "queEs": "Si alguien te acosa, te chantajea, te amenaza o se te escapa de las manos: HABLA con un adulto de confianza (padres, profesores, INCIBE 017). Pedir ayuda es lo MÁS fuerte que puedes hacer.",
    "ejemplo": {
      "tipo": "bueno",
      "texto": "✅ Te chantajean con una foto. En vez de pagar o seguir respondiendo, HABLAS con tu padre/madre o llamas al 017 (línea de ayuda en ciberseguridad de INCIBE). Es gratuito y anónimo."
    },
    "senales": [
      "Adultos de confianza: padres, profesor, orientador del cole, familia.",
      "INCIBE 017: línea gratuita y anónima de ayuda en ciberseguridad.",
      "Nunca pagues a un chantajista: aunque pagues, te volverá a pedir más."
    ],
    "quiz": {
      "p": "Si recibes una amenaza o chantaje online, lo MEJOR es:",
      "opciones": [
        "Pagar lo que piden",
        "Responder con amenazas",
        "Hablar con un adulto de confianza y/o llamar al 017 de INCIBE",
        "Borrar la cuenta y no decir nada"
      ],
      "correcta": 2,
      "explica": "Pedir ayuda no es cobardía: es lo más inteligente. El 017 es gratis y anónimo."
    }
  }
];

const FRASES_VF = [
  {
    "texto": "Responder a un trol con otro insulto le quita poder.",
    "correcta": false,
    "explica": "Falso. Responder le da más visibilidad y satisfacción. Bloquear/denunciar es más eficaz."
  },
  {
    "texto": "Una contraseña LARGA con palabras corrientes es más fuerte que una corta con muchos símbolos raros.",
    "correcta": true,
    "explica": "Verdadero. La longitud es el factor más importante."
  },
  {
    "texto": "Las denuncias en redes sociales son anónimas: el agresor no sabe quién le denunció.",
    "correcta": true,
    "explica": "Verdadero. Denunciar es seguro para ti."
  },
  {
    "texto": "Si te chantajean online, pagar es la forma más rápida de quitárselo de encima.",
    "correcta": false,
    "explica": "Falso. Si pagas, te volverán a pedir más. Habla con un adulto y/o llama al 017 (INCIBE)."
  },
  {
    "texto": "El 017 es una línea GRATUITA y ANÓNIMA de INCIBE para ayuda en ciberseguridad.",
    "correcta": true,
    "explica": "Verdadero. Atienden en español, 9-21h. Y NO te van a juzgar."
  },
  {
    "texto": "Si un compañero sufre ciberacoso, lo mejor es callarse para no meterse en líos.",
    "correcta": false,
    "explica": "Falso. Las víctimas necesitan aliados. Apoyo en privado + reportar las burlas + hablar con un profesor."
  }
];


// ── TEORÍA ──────────────────────────────────────────────────────
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
  microquizContestados.add(idx);
  if (idxOp === c.correcta) microquizAciertos.add(idx);
  document.querySelectorAll('#opcionesMq-' + idx + ' button').forEach(function(b, i) { b.disabled = true; if (i === c.correcta) b.classList.add('correcta'); else if (i === idxOp) b.classList.add('incorrecta'); });
  const fb = document.getElementById('fb-mq-' + idx);
  fb.innerHTML = (idxOp === c.correcta ? '✅ ' : '❌ Correcta: ' + String.fromCharCode(65 + c.correcta) + '. ') + c.explica;
  fb.dataset.activo = 'true';
  const btnN = document.getElementById('btn-sub-next-' + idx);
  btnN.textContent = idx === CONCEPTOS.length - 1 ? '✓ Microquiz hecho' : 'Siguiente concepto ▸';
  btnN.disabled = false;
  document.getElementById('btn-siguiente').disabled = false;
  document.querySelectorAll('.puntos-tarjetas .punto').forEach(function(p, i) { if (i === idx) p.classList.add('visto'); });
  if (idx === CONCEPTOS.length - 1) { document.getElementById('barra-fin-teoria').style.display = 'flex'; otorgarInsignia('cadete'); }
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
  vfContestadas.add(idx);
  const f = vfActuales[idx]; const acertado = (valor === f.correcta);
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
  if (vfContestadas.size === FRASES_VF.length) { document.getElementById('btn-al-reto').disabled = false; otorgarInsignia('analista'); }
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
  const nombres = {"cadete": "Cadete", "analista": "Aprendiz", "investigador": "Aventurero", "detective": "Maestro de Interland"};
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
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'Maestro de Interland' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}
function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'Maestro de Interland',
    subtitulo: 'Sesión 6 · Misión Interland (parte 2) · Promoción 2026',
    icono: '🌍',
    insignia: 'Maestro de Interland',
    nombres: [n1, n2],
    sesionNum: 'SESION6',
    score: microquizAciertos.size + vfAciertos,
    total: CONCEPTOS.length + FRASES_VF.length,
    codigo: datos.codigo,
    frase: 'Ser amable en internet es ser fuerte en internet'
  }, 'S06-interland-p2-' + n1.replace(/\s/g, '_') + '.png');
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

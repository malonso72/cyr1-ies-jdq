/* S13 · Caso Lucía OSINT · Academia Cyber-IES */
const SESION_ID = 's13';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    nombre: "¿Qué es OSINT?",
    queEs: "OSINT = Open Source Intelligence (inteligencia de fuentes abiertas). Investigar a alguien con información PÚBLICA: redes sociales, prensa, registros, Google. No es hackear: es OBSERVAR lo que la persona ha publicado.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Un acosador que solo lee tu Instagram público puede averiguar tu ciudad, instituto, horarios y cuándo estás sola en casa. Sin tocar tu móvil, sin contraseñas." },
    senales: [
      "Solo usa fuentes públicas: NO requiere intrusión ni contraseñas.",
      "Combina pequeños datos para sacar conclusiones grandes.",
      "Cualquier red pública es OSINT fácil: Insta, TikTok, X, Snapchat."
    ],
    quiz: {
      p: "¿Cuál de estas NO es una técnica OSINT?",
      opciones: [
        "Buscar tu nombre en Google",
        "Mirar tus fotos públicas en Instagram",
        "Hackear tu contraseña de Gmail",
        "Comprobar tu email en haveibeenpwned.com"
      ],
      correcta: 2,
      explica: "Hackear es ataque informático, no OSINT. OSINT solo usa fuentes públicas: lo que TÚ has hecho público sin querer o aposta."
    }
  },
  {
    nombre: "Geolocalización indirecta",
    queEs: "Una foto puede revelar dónde estás SIN que tú etiquetes la ubicación: un cartel al fondo, el escudo del instituto, una calle reconocible, el paisaje. Un investigador combina pistas para situarte.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Lucía sube una foto 'random' en la puerta de su instituto. El cartel del edificio dice 'IES Federico García Lorca · 1º ESO B'. Ya sabemos su centro y su clase." },
    senales: [
      "Carteles, logos, escudos visibles al fondo.",
      "Ropa con el escudo del centro o del equipo deportivo.",
      "Paisaje reconocible: monumentos, calles, montañas."
    ],
    quiz: {
      p: "Subes una foto SIN etiquetar ubicación. ¿Qué puede delatar tu ciudad?",
      opciones: [
        "Un cartel de tienda local al fondo",
        "Un monumento famoso visible",
        "Una matrícula de coche aparcado",
        "Todas las anteriores"
      ],
      correcta: 3,
      explica: "Todas. Un investigador OSINT combina detalles del fondo para localizarte sin que hayas marcado nada explícito."
    }
  },
  {
    nombre: "Rutinas y patrones",
    queEs: "Lo que publicas revela tu día a día. Si subes el mismo café los miércoles a las 18:00, ya saben que ese día estás allí. Si dices 'mis padres en Madrid hasta el viernes', anuncias 5 días sin adultos en casa.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ 'Todos los miércoles después de clase un ratito en el Nevada Shopping con las amigas 💖' → un acosador sabe exactamente dónde y cuándo encontrarte." },
    senales: [
      "Publicas la misma actividad en el mismo día/hora.",
      "Anuncias ausencias familiares ('mis padres están fuera').",
      "Cuentas tu horario semanal sin darte cuenta."
    ],
    quiz: {
      p: "Tu amiga publica: 'Mis padres en Madrid hasta el viernes 🍕'. ¿Qué riesgo principal hay?",
      opciones: [
        "Que la critiquen sus padres",
        "Que cualquier conocido sepa que está sola en casa 5 días",
        "Que se le acabe el dinero",
        "Ninguno, es solo un post"
      ],
      correcta: 1,
      explica: "Información SENSIBLE: 'estoy sola en casa toda la semana'. Cualquier conocido tiene 5 días seguros para actuar."
    }
  },
  {
    nombre: "Datos de los demás",
    queEs: "Las etiquetas, menciones y hashtags filtran información sobre OTRAS personas. Aunque TU cuenta sea privada, si etiquetas a un amigo de cuenta pública, esa foto sale en SU feed → cualquier desconocido puede verla.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Tu cuenta es privada, pero etiquetas a tu novio Diego en una foto. Diego tiene cuenta pública. La foto sale en su feed → cualquier desconocido puede verla y saber que sois pareja." },
    senales: [
      "Etiquetas a personas con cuenta PÚBLICA: la foto puede llegar a desconocidos.",
      "Hashtags muy específicos (#IESLorca, #1ESOB) reúnen tu contenido con el de tus compañeros.",
      "Tu nombre puede aparecer en stories y posts de otros, fuera de tu control."
    ],
    quiz: {
      p: "Tu cuenta es PRIVADA pero etiquetas a un amigo de cuenta PÚBLICA. ¿Qué pasa?",
      opciones: [
        "La foto solo la ven tus seguidores",
        "La foto aparece en el feed PÚBLICO de tu amigo → cualquiera puede verla",
        "Tu cuenta deja de ser privada automáticamente",
        "Instagram te avisa antes"
      ],
      correcta: 1,
      explica: "La etiqueta lleva la foto al feed del amigo. Si su cuenta es pública, la foto se hace pública aunque la tuya no. Tu privacidad depende de la de los demás."
    }
  }
];

// Entrenamiento V/F (6 frases)
const FRASES_VF = [
  { texto: "Si mi cuenta de Instagram es PRIVADA, nadie de fuera puede saber NADA de mí.", correcta: false,
    explica: "Falso. Si tus amigos tienen cuentas públicas, una etiqueta o mención tuya en sus posts ya filtra información sobre ti. Además, tu nombre, foto y bio pueden ser visibles igualmente." },
  { texto: "No etiquetar la ubicación en Instagram es suficiente para que nadie sepa dónde estoy.", correcta: false,
    explica: "Falso. Carteles, escudos, ropa de equipo, monumentos del fondo… delatan la ubicación aunque no la etiquetes. La geolocalización indirecta funciona casi siempre." },
  { texto: "Publicar 'mis padres están fuera hasta el viernes' es una información peligrosa.", correcta: true,
    explica: "Verdadero. Anuncias varios días sin adultos en casa a TODOS tus seguidores (incluyendo desconocidos). Es uno de los avisos OSINT más usados por acosadores." },
  { texto: "Los hashtags muy específicos como #IESLorca o #1ESOB no dan información útil.", correcta: false,
    explica: "Falso. Reúnen el contenido de TI y de TUS COMPAÑEROS bajo una etiqueta común. Cualquiera puede ver quién va a tu instituto y a qué clase." },
  { texto: "Subir la misma foto todos los miércoles desde el mismo sitio revela tu rutina semanal.", correcta: true,
    explica: "Verdadero. Las publicaciones recurrentes en el mismo día/hora/lugar forman un patrón perfecto para alguien que quiera encontrarte sin que lo veas." },
  { texto: "OSINT requiere herramientas profesionales caras y conocimientos avanzados.", correcta: false,
    explica: "Falso. La mayoría del OSINT se hace con Google + Instagram + sentido común. Cualquier persona puede hacerlo. Por eso lo que publicas importa tanto." }
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
  const nombres = { cadete: 'Cadete', analista: 'Analista', investigador: 'Investigador', detective: 'Detective OSINT' };
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
  if (!_tieneMin(q2, ['ubicacion','instituto','amigos','horario','familia','mascota','rutina','colegio','barrio','casa','novio'], 1)) _kwFail.push('Pregunta 2: di qué DATOS se sacan (ubicación, instituto, horarios, familia, mascota, rutina…).');
  if (!_tieneMin(q3, ['privada','ubicacion','seguidores','horario','instituto','casa','publicar','fotos','etiqueta','permiso'], 2)) _kwFail.push('Pregunta 3: da consejos concretos (cuenta privada, no dar ubicación ni instituto, revisar seguidores, no publicar horarios…).');
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
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'Detective OSINT' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}

function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'Detective OSINT',
    subtitulo: 'Sesión 13 · Caso Lucía · Promoción 2026',
    icono: '🔍',
    insignia: 'Detective OSINT',
    nombres: [n1, n2],
    sesionNum: 'S13',
    score: microquizAciertos.size + vfAciertos,
    total: CONCEPTOS.length + FRASES_VF.length,
    codigo: datos.codigo,
    frase: 'Lo que publicas en abierto, vive en abierto'
  }, 'S13-caso-lucia-' + n1.replace(/\s/g, '_') + '.png');
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


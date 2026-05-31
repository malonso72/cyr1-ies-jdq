/* S9 · Escape PIENSA · El ataque psicológico · Academia Cyber-IES */
const SESION_ID = 's09';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    nombre: "¿Qué es la ingeniería social?",
    queEs: "Es el arte de HACKEAR PERSONAS en vez de máquinas. El atacante no rompe tu contraseña: te convence a TI de que se la des. Para lograrlo usa trucos psicológicos que llevan siglos funcionando, porque atacan cómo siente el cerebro, no cómo piensa.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Llega un correo: 'Tu cuenta de Instagram se cerrará en 30 minutos. Pulsa AQUÍ para salvarla.' No hace falta saber programar para caer: basta con sentir prisa y miedo. Eso es ingeniería social." },
    senales: [
      "El ataque va dirigido a una EMOCIÓN (prisa, miedo, codicia, vergüenza), no a tu ordenador.",
      "Te piden una acción rápida: pinchar, pagar, dar datos, descargar.",
      "Si te paras a pensar 10 segundos, el truco casi siempre se cae."
    ],
    quiz: {
      p: "¿Qué 'hackea' realmente la ingeniería social?",
      opciones: [
        "El antivirus del ordenador",
        "A la persona, aprovechando sus emociones",
        "El router de casa",
        "La contraseña por fuerza bruta"
      ],
      correcta: 1,
      explica: "No rompe máquinas: te manipula a TI para que entregues lo que el atacante quiere. Por eso la mejor defensa eres tú mismo."
    }
  },
  {
    nombre: "Prisa: urgencia y escasez",
    queEs: "Dos técnicas gemelas que te roban el tiempo de pensar. La URGENCIA te mete prisa ('en 30 minutos', 'AHORA'). La ESCASEZ te dice que queda poquísimo ('solo 2 plazas', 'últimas unidades'). Las dos buscan lo mismo: que decidas con el corazón acelerado y no con la cabeza.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ '¡SORTEO! Quedan solo 2 móviles gratis y el contador acaba en 5 minutos. Rellena tus datos YA.' Prisa + poco disponible = clásico de manual." },
    senales: [
      "Plazos cortísimos: 'en X minutos', 'antes de medianoche', 'AHORA'.",
      "Cantidades mínimas: 'solo quedan 2', 'últimas plazas'.",
      "Te empujan a actuar antes de comprobar nada."
    ],
    quiz: {
      p: "'¡Solo 2 plazas y el contador acaba en 5 minutos!' ¿Qué dos técnicas se mezclan?",
      opciones: [
        "Autoridad y miedo",
        "Escasez (pocas plazas) y urgencia (contador)",
        "Reciprocidad y prueba social",
        "Ninguna, es una oferta normal"
      ],
      correcta: 1,
      explica: "Pocas plazas = escasez. Contador a cero = urgencia. Juntas te impiden pararte a pensar."
    }
  },
  {
    nombre: "Quien manda y la mayoría: autoridad y prueba social",
    queEs: "La AUTORIDAD imita a quien tiene poder (un ministerio, la policía, el director) para que obedezcas sin preguntar. La PRUEBA SOCIAL te dice que 'todo el mundo ya lo hace' para que tú también lo hagas. Las dos apagan tu juicio propio: una por respeto al jefe, otra por seguir al rebaño.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ 'Departamento de Inspección del Ministerio: debe verificar sus datos.' o 'El 80% de tus compañeros ya usa esta app, ¿a qué esperas?' Suenan fiables… y casi siempre son inventados." },
    senales: [
      "Se presentan como organismo importante (ministerio, banco, policía, soporte).",
      "Usan el 'todo el mundo lo hace' o cifras de popularidad inventadas.",
      "Buscan que obedezcas o imites sin verificar quién está detrás."
    ],
    quiz: {
      p: "'El 80% de los alumnos del instituto ya se ha descargado esta app.' ¿Qué técnica es?",
      opciones: [
        "Autoridad",
        "Prueba social: 'si lo hacen muchos, será bueno'",
        "Escasez",
        "Reciprocidad"
      ],
      correcta: 1,
      explica: "Es prueba social. El cerebro asume que lo que hace la mayoría es seguro. El dato casi siempre está inventado para presionarte."
    }
  },
  {
    nombre: "Pánico y el regalo trampa: miedo y reciprocidad",
    queEs: "El MIEDO bloquea la razón con una amenaza ('llamaré a la policía y a tus padres') para que pagues o actúes en pánico. La RECIPROCIDAD es la más sutil: primero te regalan algo ('un filtro premium gratis') para que te sientas en deuda y luego te pidan algo a cambio. Si alguien que no conoces te regala algo, no es generosidad: es una trampa preparada.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ 'Tengo fotos tuyas. Paga 50€ o se las enseño a todos.' (miedo) · 'Te he regalado 100 monedas del juego, ahora solo dime tu usuario y clave.' (reciprocidad)." },
    senales: [
      "Amenazas que provocan pánico ('la policía', 'tus padres', 'se borrará todo').",
      "Un 'regalo' inesperado de un desconocido seguido de una petición.",
      "Nunca se paga a un chantajista: si pagas, volverán a pedir más."
    ],
    quiz: {
      p: "Alguien que no conoces te 'regala' un objeto del videojuego y luego te pide tu contraseña. ¿Qué técnica usa?",
      opciones: [
        "Urgencia",
        "Reciprocidad: el regalo crea sensación de deuda",
        "Autoridad",
        "Prueba social"
      ],
      correcta: 1,
      explica: "Es reciprocidad. El regalo no es generosidad: busca que te sientas obligado a devolver el favor (tu clave). La más sutil de las seis."
    }
  },
  {
    nombre: "Tu defensa: PARA · DUDA · VERIFICA",
    queEs: "Contra las 6 técnicas no hay antivirus: hay un hábito. PARA (no actúes en caliente, respira 10 segundos), DUDA (¿por qué tengo tanta prisa o miedo?, ¿de quién es esto de verdad?) y VERIFICA por otro canal (llama al banco por su teléfono oficial, pregunta a un adulto, escribe tú la web a mano). El que se para, gana.",
    ejemplo: { tipo: 'bueno', texto: "✅ Te llega 'tu paquete está retenido, paga 1,99€ aquí'. PARAS. DUDAS (no esperabas ningún paquete). VERIFICAS entrando tú a la web de Correos a mano. Era falso. No has perdido ni un céntimo." },
    senales: [
      "Ante prisa o miedo repentinos: para y respira antes de tocar nada.",
      "Verifica SIEMPRE por otro canal distinto al del mensaje.",
      "Ante la duda, no pinches, no pagues y pregunta a alguien de confianza."
    ],
    quiz: {
      p: "Recibes un SMS urgente de 'tu banco' con un enlace. ¿Qué es lo más seguro?",
      opciones: [
        "Pinchar el enlace para resolverlo rápido",
        "Parar, no pinchar y entrar tú a la web/app del banco por tu cuenta",
        "Reenviarlo a tus amigos por si acaso",
        "Responder al SMS pidiendo más datos"
      ],
      correcta: 1,
      explica: "PARA, DUDA, VERIFICA: nunca uses el enlace del mensaje. Entra tú al banco por el canal oficial que ya conoces."
    }
  }
];

// Entrenamiento: 6 frases V/F sobre ingeniería social
const FRASES_VF = [
  { texto: "Un correo que dice 'tu cuenta se cerrará en 30 minutos, pulsa aquí' está usando la técnica de la URGENCIA.",
    correcta: true,
    explica: "Verdadero. El plazo cortísimo busca que pinches sin pensar: urgencia de manual." },
  { texto: "Si un mensaje dice ser del 'Ministerio' o de 'la policía', es seguro obedecer sin comprobar nada.",
    correcta: false,
    explica: "Falso. Eso es la técnica de la AUTORIDAD: cualquiera puede DECIR que es un ministerio. Verifica por el canal oficial antes de obedecer." },
  { texto: "Cuando un desconocido te regala algo y justo después te pide tu contraseña, está usando la RECIPROCIDAD.",
    correcta: true,
    explica: "Verdadero. El 'regalo' crea sensación de deuda para que devuelvas el favor. La técnica más sutil de las seis." },
  { texto: "Si te chantajean con 'paga o lo cuento', lo mejor es pagar rápido para que el problema desaparezca.",
    correcta: false,
    explica: "Falso. NUNCA se paga a un chantajista: si pagas, volverán a pedir más. Hay que guardar pruebas y contarlo a un adulto/denunciar." },
  { texto: "'Solo quedan 2 plazas' y 'el 80% ya lo usa' son la misma técnica exacta.",
    correcta: false,
    explica: "Falso. 'Solo quedan 2' es ESCASEZ; 'el 80% ya lo usa' es PRUEBA SOCIAL. Son dos técnicas distintas aunque a veces vayan juntas." },
  { texto: "Pararse 10 segundos a pensar y verificar por otro canal desactiva la mayoría de los ataques psicológicos.",
    correcta: true,
    explica: "Verdadero. PARA, DUDA, VERIFICA: el ataque necesita que reacciones en caliente. Si te paras, casi siempre se cae." }
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
const INSIGNIA_NOMBRES = { cadete: 'Aprendiz', analista: 'Detector de Trampas', investigador: 'Escapista PIENSA', detective: 'Cortafuegos Humano' };
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
  const datos = Academia.getSesion(SESION_ID);
  Academia.marcarCompletada(SESION_ID, microquizAciertos.size + vfAciertos, CONCEPTOS.length + FRASES_VF.length);
  Academia.setSesion(SESION_ID, { q1: q1, q2: q2, q3: q3, informeCompletado: true, tiempoMin: Math.round((Date.now() - tInicio) / 60000) });
  document.getElementById('res-teoria').textContent = microquizAciertos.size + ' / ' + CONCEPTOS.length + ' microquiz';
  document.getElementById('res-entrenamiento').textContent = vfAciertos + ' / ' + FRASES_VF.length + ' V/F';
  document.getElementById('res-tiempo').textContent = (Math.round((Date.now() - tInicio) / 60000)) + ' min';
  const cod = Academia.codigoFinalizacion(SESION_ID, microquizAciertos.size + vfAciertos);
  document.getElementById('cod-final').textContent = 'CÓDIGO: ' + cod;
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'Cortafuegos Humano' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}

function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'Cortafuegos Humano',
    subtitulo: 'Sesión 9 · Escape PIENSA · Promoción 2026',
    icono: '🛡️',
    insignia: 'Cortafuegos Humano',
    nombres: [n1, n2],
    sesionNum: 'S9',
    score: microquizAciertos.size + vfAciertos,
    total: CONCEPTOS.length + FRASES_VF.length,
    codigo: datos.codigo,
    frase: 'El que se para a pensar, no cae en la trampa'
  }, 'S9-piensa-' + n1.replace(/\s/g, '_') + '.png');
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

/* S11 · Wifi café trampa · Academia Cyber-IES */
const SESION_ID = 's11';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    nombre: "Wifi pública = red compartida",
    queEs: "En casa la wifi tiene contraseña y solo la conocéis tu familia y tu router. En un bar, un aeropuerto o un centro comercial hay DECENAS de personas conectadas a la vez a la misma red. Y entre ellas puede haber alguien con conocimientos espiando lo que hacen los demás. La wifi pública no es 'mala', pero sí es un sitio donde no estás solo.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Estás en una cafetería y entras a tu correo por la wifi gratis. Otra persona sentada cerca, conectada a la misma red, puede intentar 'escuchar' lo que viaja si la conexión no va cifrada." },
    senales: [
      "La red es abierta o la contraseña la sabe todo el local.",
      "Hay mucha gente conectada a la vez que no conoces.",
      "No controlas quién más está en esa red ni qué hace."
    ],
    quiz: {
      p: "¿Por qué una wifi pública es más arriesgada que la de tu casa?",
      opciones: [
        "Porque va más lenta",
        "Porque hay muchas personas desconocidas en la misma red y alguien puede espiar",
        "Porque gasta más batería",
        "Porque no tiene contraseña nunca"
      ],
      correcta: 1,
      explica: "El riesgo es compartir la red con desconocidos: cualquiera de ellos podría intentar ver lo que haces si no va protegido."
    }
  },
  {
    nombre: "Redes gemelas: la trampa del nombre",
    queEs: "Cualquiera puede crear con su móvil una wifi y ponerle el nombre que quiera. Un atacante en el Starbucks crea una red llamada 'Starbucks_Free', la deja abierta y espera. Tú ves el nombre familiar, te conectas… pero esa wifi NO es la del Starbucks: es la del atacante, y todo lo que haces pasa por su equipo. Es la 'red gemela' o 'evil twin': mismo nombre, falsa identidad.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Ves dos redes: 'AEROPUERTO_WIFI' y 'AEROPUERTO_WIFI_GRATIS_5G'. La segunda suena mejor… y puede ser la trampa de alguien. El nombre bonito no garantiza nada." },
    senales: [
      "Nombres que imitan al local pero con añadidos ('_FREE', '_GRATIS', '_5G').",
      "Dos redes con nombres casi iguales: una puede ser falsa.",
      "Una red abierta con nombre 'demasiado perfecto' para ser verdad."
    ],
    quiz: {
      p: "¿Qué es una 'red gemela' (evil twin)?",
      opciones: [
        "Una wifi con doble velocidad",
        "Una wifi falsa que copia el nombre de una real para engañarte",
        "Dos routers de la misma marca",
        "La wifi de invitados del local"
      ],
      correcta: 1,
      explica: "Mismo nombre, falsa identidad: el atacante copia el nombre de una red de confianza para que te conectes a la suya."
    }
  },
  {
    nombre: "HTTPS y el candado",
    queEs: "Mira la barra del navegador. Si pone 'https://' con un candado 🔒, la información viaja CIFRADA: aunque haya un atacante en la wifi, no puede leer lo que escribes. Si pone solo 'http://' sin candado, lo lee TODO en claro. Ojo: las páginas FALSAS también pueden poner candado, así que el candado ayuda pero no garantiza que la web sea de verdad quien dice ser.",
    ejemplo: { tipo: 'bueno', texto: "✅ Vas a entrar en tu correo y compruebas que pone https:// con candado. La wifi pública ya no puede leer tu contraseña: viaja cifrada hasta el servidor." },
    senales: [
      "https:// + candado = el contenido viaja cifrado.",
      "http:// sin candado = todo viaja en claro, evítalo para datos sensibles.",
      "El candado protege el 'viaje', pero no demuestra que la web sea auténtica."
    ],
    quiz: {
      p: "Vas a escribir tu contraseña en una web por wifi pública. ¿Qué miras primero?",
      opciones: [
        "Que la web tenga muchos colores",
        "Que la dirección sea https:// con candado",
        "Que cargue rápido",
        "Que tenga publicidad"
      ],
      correcta: 1,
      explica: "https:// con candado significa que tus datos viajan cifrados. Sin candado, cualquiera en la wifi podría leerlos."
    }
  },
  {
    nombre: "La VPN: el túnel (y las VPN trampa)",
    queEs: "Una VPN es un 'túnel' que cifra TODO tu tráfico, incluso si la wifi es trampa. El atacante ve que estás conectado, pero no puede leer NADA. Suena perfecto, pero ojo: hay VPN gratis que en realidad SON la trampa (venden tus datos o son del propio atacante). Las buenas suelen ser de pago o las que pone tu instituto/empresa. Una VPN mala es PEOR que no tener ninguna.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Una app te ofrece 'VPN gratis ilimitada para siempre'. ¿De qué vive esa empresa entonces? Muchas veces, de vender lo que tú haces. Gratis no siempre significa regalo." },
    senales: [
      "La VPN cifra todo tu tráfico: útil en wifi pública.",
      "Desconfía de VPN gratis y desconocidas: pueden ser la propia trampa.",
      "Mejores opciones: VPN de pago con buena fama o la de tu centro/empresa."
    ],
    quiz: {
      p: "¿Por qué una VPN gratis y desconocida puede ser peligrosa?",
      opciones: [
        "Porque va siempre lentísima",
        "Porque la empresa detrás puede vender tus datos o ser el propio atacante",
        "Porque ocupa mucho espacio",
        "Porque no funciona en el móvil"
      ],
      correcta: 1,
      explica: "Si nadie paga el servicio, a menudo el producto eres tú: tus datos. Una VPN mala puede ser peor que no usar ninguna."
    }
  },
  {
    nombre: "Las 4 reglas de oro del wifi público",
    queEs: "Resumen práctico para tu vida real: 1) Para el banco, comprar online o cosas importantes usa SIEMPRE los datos móviles del teléfono, NUNCA wifi público. 2) Si el navegador avisa de 'certificado no confiable', vuelve atrás y no continúes. 3) En los portales cautivos ('mete tu email para acceder') da los mínimos datos posibles. 4) Cuando termines, olvida la red para no reconectarte solo.",
    ejemplo: { tipo: 'bueno', texto: "✅ Ana, en el aeropuerto, va a entrar en su banco. En vez de usar la wifi del aeropuerto, desactiva la wifi y usa los datos móviles del teléfono. Operación importante = datos móviles." },
    senales: [
      "Cosas importantes (banco, pagos) → datos móviles, no wifi pública.",
      "Aviso de 'certificado no confiable' → atrás, no continúes.",
      "Portal cautivo → da los mínimos datos; al acabar, olvida la red."
    ],
    quiz: {
      p: "Ana necesita entrar en su banco mientras espera en el aeropuerto. ¿Qué debería hacer?",
      opciones: [
        "Usar la wifi gratis del aeropuerto, es más cómodo",
        "Desactivar la wifi y usar los datos móviles del teléfono",
        "Pedir la contraseña wifi a otro pasajero",
        "Conectarse a la red con nombre más bonito"
      ],
      correcta: 1,
      explica: "Regla de oro nº1: para el banco y pagos, datos móviles SIEMPRE, nunca wifi público."
    }
  }
];

// Entrenamiento: 6 frases V/F sobre wifi público
const FRASES_VF = [
  { texto: "Conectarse a una wifi pública llamada 'Cafetería_GRATIS' es siempre seguro porque tiene el nombre de la cafetería.",
    correcta: false,
    explica: "Falso. Cualquiera puede poner ese nombre a su red. Es la trampa de la 'red gemela': mismo nombre, falsa identidad." },
  { texto: "Si una web muestra https:// con candado, lo que escribo viaja cifrado aunque la wifi sea pública.",
    correcta: true,
    explica: "Verdadero. El candado significa que el contenido viaja cifrado de tu móvil al servidor. Eso sí, no garantiza que la web sea auténtica." },
  { texto: "Para entrar en mi banco desde el aeropuerto, lo mejor es usar la wifi gratuita del aeropuerto.",
    correcta: false,
    explica: "Falso. Para banco y pagos, datos móviles SIEMPRE, nunca wifi público. Es la primera regla de oro." },
  { texto: "Una VPN gratis y desconocida siempre es mejor que no usar ninguna VPN.",
    correcta: false,
    explica: "Falso. Una VPN mala puede vender tus datos o ser del propio atacante: puede ser PEOR que no usar ninguna." },
  { texto: "Si el navegador avisa de 'certificado no confiable', lo correcto es volver atrás y no continuar.",
    correcta: true,
    explica: "Verdadero. Ese aviso es una señal de alarma: puede haber alguien interceptando la conexión. No continúes." },
  { texto: "Una VPN buena crea un 'túnel' que cifra todo tu tráfico, incluso si la wifi es una trampa.",
    correcta: true,
    explica: "Verdadero. Esa es la idea de la VPN: aunque la wifi sea del atacante, no puede leer lo que va por el túnel cifrado." }
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
const INSIGNIA_NOMBRES = { cadete: 'Aprendiz', analista: 'Rastreador de Redes', investigador: 'Copiloto de Ana', detective: 'Guardián del Wifi' };
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
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'Guardián del Wifi' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}

function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'Guardián del Wifi',
    subtitulo: 'Sesión 11 · Wifi café trampa · Promoción 2026',
    icono: '📶',
    insignia: 'Guardián del Wifi',
    nombres: [n1, n2],
    sesionNum: 'S11',
    score: microquizAciertos.size + vfAciertos,
    total: CONCEPTOS.length + FRASES_VF.length,
    codigo: datos.codigo,
    frase: 'La wifi gratis nunca es del todo gratis: el precio puede ser tu seguridad'
  }, 'S11-wifi-' + n1.replace(/\s/g, '_') + '.png');
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

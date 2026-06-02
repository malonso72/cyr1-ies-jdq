/* S16 · Gaming: estafas en videojuegos */
const SESION_ID = 's16';
const tInicio = Date.now();

const CONCEPTOS = [
  {
    nombre: "V-Bucks, skins y FOMO",
    queEs: "FOMO = Fear Of Missing Out (miedo a perdértelo). Los gamers son víctimas fáciles porque las ofertas siempre son 'limitadas' y 'urgentes'. Tu cerebro emocional pincha antes de pensar.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ 'SOLO HOY · 5.000 V-Bucks gratis · quedan 12 minutos'. Tu cerebro entra en modo pánico y olvida que Epic Games NUNCA regala V-Bucks así." },
    senales: [
      "El anuncio te mete urgencia ('caduca en X', 'últimas unidades').",
      "El precio es DEMASIADO bueno comparado con la tienda oficial.",
      "Apela a tu deseo emocional (skin rara, exclusiva, sólo de jugadores VIP)."
    ],
    quiz: {
      p: "¿Cuántos V-Bucks reales valen 4,99€ en la tienda OFICIAL de Epic Games?",
      opciones: [
        "5.000 V-Bucks",
        "Aproximadamente 500 V-Bucks (1.000 cuestan 9,99€)",
        "10.000 V-Bucks",
        "100.000 V-Bucks"
      ],
      correcta: 1,
      explica: "Aproximadamente 500. Si alguien te ofrece 5.000 por ese precio, te están vendiendo 10 veces más por el mismo dinero. Eso es físicamente imposible: el negocio sería ruinoso para Epic. Es estafa SEGURO."
    }
  },
  {
    nombre: "Las 8 señales de una tienda falsa",
    queEs: "Aunque la web parezca profesional, casi siempre tiene 8 señales delatoras: URL extraña, http sin candado, precios imposibles, contador falso de urgencia, sello de seguridad falso, métodos de pago raros, formulario que pide contraseña del juego, y dominio impostado.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Una tienda de 'V-Bucks' con la URL 'vbucks-epic-store-spain.com.es-promo.online'. Suena oficial pero ese dominio NO es de Epic. El dominio real sería 'epicgames.com'." },
    senales: [
      "Mira la URL: el dominio real (lo de ANTES del primer '/') tiene que ser de la marca.",
      "Mira el candado: si no aparece, los datos viajan sin cifrar.",
      "Mira el precio: si es ridículamente bajo, es trampa."
    ],
    quiz: {
      p: "Una tienda 'oficial' de V-Bucks te pide tu USUARIO Y CONTRASEÑA de Epic Games para enviarte los V-Bucks. ¿Qué piensas?",
      opciones: [
        "Es lógico, así me los mandan a mi cuenta",
        "Es PHISHING. Una tienda real cobra con tarjeta, NUNCA pide tu contraseña del juego",
        "Solo es problema si tu cuenta tiene mucho dinero",
        "Es seguro si la URL tiene HTTPS"
      ],
      correcta: 1,
      explica: "PHISHING. Una tienda legítima cobra con tarjeta/PayPal y SABE en qué cuenta darte los V-Bucks porque tú se lo dirás POR el formulario de compra, NO con tu contraseña."
    }
  },
  {
    nombre: "El streamer que 'regala' cuentas",
    queEs: "Un perfil con foto de streamer famoso te escribe por DM: 'Soy XXX, hago un sorteo de 10 cuentas con skins, dame tu user y password para preparártela'. La regla: los streamers NO usan DMs para regalar cuentas. JAMÁS.",
    ejemplo: { tipo: 'peligroso', texto: "⚠️ Te escribe '@Ninja_oficial_es' (con foto de Ninja, el streamer famoso). Te dice que has sido seleccionado para un sorteo. Te pide credenciales. En realidad es una cuenta falsa creada con el nombre y la foto de Ninja." },
    senales: [
      "Cuentas con pocas seguidores pero con foto de famoso.",
      "Te contactan por DM (no por anuncio público con normas claras).",
      "Te piden datos personales o credenciales."
    ],
    quiz: {
      p: "Un perfil con foto del streamer Auronplay te escribe por DM ofreciéndote V-Bucks gratis. ¿Qué haces?",
      opciones: [
        "Le doy mi usuario, total no le doy contraseña",
        "Lo bloqueo: los streamers reales NUNCA regalan cuentas por DM",
        "Le pido que me llame para confirmar",
        "Acepto si tiene check azul"
      ],
      correcta: 1,
      explica: "Los streamers reales NO usan DMs para regalar cuentas. Si organizan algo, lo anuncian públicamente con normas claras. Cualquier DM ofreciendo regalos es estafa."
    }
  },
  {
    nombre: "Solo la tienda OFICIAL",
    queEs: "Epic Games SOLO vende V-Bucks dentro del propio Fortnite (en tu PS5, PC, Switch…) o en epicgames.com. Cualquier OTRA web que diga vender V-Bucks oficiales es FALSA. Sin excepciones.",
    ejemplo: { tipo: 'bueno', texto: "✅ Quieres comprar 1.000 V-Bucks. Abres Fortnite en tu PS5 → Tienda → V-Bucks → pagas con la tarjeta familiar registrada en PlayStation. Único método seguro." },
    senales: [
      "Sólo dentro del juego o en epicgames.com.",
      "Cualquier web externa diciendo ser 'tienda oficial' es FALSA.",
      "Esta regla aplica IGUAL a Roblox (Robux), CS:GO (skins), Brawl Stars (gemas)…"
    ],
    quiz: {
      p: "¿Dónde compras V-Bucks de forma SEGURA?",
      opciones: [
        "En cualquier web que aparezca al buscar 'V-Bucks baratos' en Google",
        "Solo dentro de Fortnite o en epicgames.com",
        "En redes sociales si tienen muchos seguidores",
        "En webs con HTTPS y candado verde"
      ],
      correcta: 1,
      explica: "Solo dentro del juego o en epicgames.com. Cualquier otra cosa es estafa. El HTTPS solo significa cifrado, NO legitimidad."
    }
  }
];

// Entrenamiento V/F (6 frases sobre estafas gaming)
const FRASES_VF = [
  { texto: "Epic Games vende V-Bucks oficialmente en webs externas con descuentos del 80%.", correcta: false,
    explica: "Falso. Epic SÓLO vende V-Bucks dentro de Fortnite y en epicgames.com. Cualquier 'descuento del 80%' externo es estafa." },
  { texto: "Una tienda con HTTPS y candado siempre es segura.", correcta: false,
    explica: "Falso. El HTTPS solo significa que la comunicación está cifrada. NO significa que la web sea legítima. Mira siempre el DOMINIO." },
  { texto: "Si un streamer famoso te ofrece V-Bucks gratis por DM, es porque ha sido elegido en un sorteo.", correcta: false,
    explica: "Falso. Los streamers reales NO usan DMs para regalar cuentas. Si organizan algo, lo hacen público con normas claras. Cualquier DM ofreciendo regalos es estafa." },
  { texto: "Los contadores de 'oferta caduca en X minutos' suelen ser scripts falsos que se reinician al recargar la página.", correcta: true,
    explica: "Verdadero. Son trucos de presión psicológica. Recarga la página y verás cómo el contador vuelve a empezar." },
  { texto: "Dar tu usuario y contraseña de Epic Games a una web 'para recibir V-Bucks' es phishing puro.", correcta: true,
    explica: "Verdadero. Una tienda real NUNCA pide tu contraseña del juego. Cobra con tarjeta. El que pide credenciales del juego es estafador." },
  { texto: "Si el precio de unos V-Bucks es demasiado bueno para ser cierto, probablemente no lo es.", correcta: true,
    explica: "Verdadero. Es la regla de oro contra estafas: si una oferta parece imposible, lo es. Comprueba la tienda oficial siempre." }
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
  const nombres = { cadete: 'Cadete', analista: 'Analista', investigador: 'Gamer Seguro', detective: 'Cazador de Estafas Gaming' };
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
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'Cazador de Estafas Gaming' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}

function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'Cazador de Estafas Gaming',
    subtitulo: 'Sesión 16 · Gaming · Promoción 2026',
    icono: '🎮',
    insignia: 'Cazador de Estafas Gaming',
    nombres: [n1, n2],
    sesionNum: 'S16',
    score: microquizAciertos.size + vfAciertos,
    total: CONCEPTOS.length + FRASES_VF.length,
    codigo: datos.codigo,
    frase: 'Si el precio es demasiado bueno, el precio eres tú'
  }, 'S16-gaming-' + n1.replace(/\s/g, '_') + '.png');
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


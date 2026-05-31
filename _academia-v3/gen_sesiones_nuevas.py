#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera las 6 sesiones nuevas (S4, S5, S6, S7, S8, S10) a partir de:
- Una plantilla HTML común (PLANTILLA_HTML)
- Una plantilla JS común (PLANTILLA_JS)
- Datos específicos por sesión (CONCEPTOS, FRASES_VF, mecánica del reto)

S5+S6 y S8 son "launcher externo": el reto es un enlace a sitio externo + diario propio.
S4, S7 y S10 son "galería": cards con elementos a decidir.
"""

from pathlib import Path
import json

ROOT = Path('/sessions/cool-gallant-cray/mnt/cyr1-ies-jdq/_academia-v3/sesiones')

# ── PLANTILLA HTML ──────────────────────────────────────────────
PLANTILLA_HTML = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#5B3D9B">
<link rel="icon" type="image/svg+xml" href="../../favicon.svg">
<title>S{NUM} · {TITULO_CORTO} · Academia Cyber-IES</title>
<meta name="description" content="Sesión {NUM} · {TITULO_CORTO} · Academia Cyber-IES · CyR 1º ESO.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600;700&family=Barlow+Condensed:wght@600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../assets/css/common.css">
<link rel="stylesheet" href="../assets/css/academia.css">
</head>
<body>
<a href="#main-content" class="skip-link">Saltar al contenido principal</a>
<header class="curso-hd"><span class="curso-sb">Academia Cyber-IES · Sesión {NUM}</span></header>
<nav class="curso-navcross" role="navigation">
  <a href="../../index.html"><span>🏠</span><span class="nc-lbl">Índice</span></a>
  <span class="nc-sep">·</span>
  <a href="../index.html"><span>🎓</span><span class="nc-lbl">Academia</span></a>
  <span class="nc-sep">·</span>
  <span class="nc-current"><span>{EMOJI}</span><span class="nc-lbl">S{NUM} · {TITULO_NAV}</span></span>
</nav>
<main id="main-content">
<section class="acad-hero">
  <div class="acad-num">SESIÓN {NUM} · 40-50 MIN</div>
  <h1>{TITULO}</h1>
  <p class="acad-sub">{SUBTITULO}</p>
</section>
<div class="acad-progreso">
  <div class="paso activo" data-bloque="mision"><div class="num">1</div><span>Misión</span></div>
  <div class="paso" data-bloque="teoria"><div class="num">2</div><span>Teoría</span></div>
  <div class="paso" data-bloque="entrenamiento"><div class="num">3</div><span>Entrenar</span></div>
  <div class="paso" data-bloque="juego"><div class="num">4</div><span>{LABEL_JUEGO}</span></div>
  <div class="paso" data-bloque="informe"><div class="num">5</div><span>Informe</span></div>
  <div class="paso" data-bloque="diploma"><div class="num">6</div><span>Insignia</span></div>
</div>
<div class="acad-insignias-fila">
  <div class="mi-insignia" data-mi="cadete" data-ganada="false"><div class="emoji">🎖️</div><div class="nom">{INS_1}</div><div class="et">tras teoría</div></div>
  <div class="mi-insignia" data-mi="analista" data-ganada="false"><div class="emoji">🎖️</div><div class="nom">{INS_2}</div><div class="et">tras entrenar</div></div>
  <div class="mi-insignia" data-mi="investigador" data-ganada="false"><div class="emoji">🎖️</div><div class="nom">{INS_3}</div><div class="et">tras reto</div></div>
  <div class="mi-insignia" data-mi="detective" data-ganada="false"><div class="emoji">🏆</div><div class="nom">{INS_FINAL_CORTO}</div><div class="et">final</div></div>
</div>
<div class="acad-main">

<section class="bloque acad-mision" data-bloque="mision" data-activo="true">
  <div class="titulo-bloque">▸ Bloque 1 · Misión</div>
  <h2>{EMOJI} {TITULO_MISION}</h2>
  <div class="narrativa" style="background:#FFF8E1;border-left:4px solid var(--acad-oro);padding:12px 14px;border-radius:0 6px 6px 0">{GANCHO_EMOCIONAL}</div>
  <div class="narrativa">{NARRATIVA}</div>
  <div class="objetivo"><strong>Qué vas a hacer hoy</strong><p>{OBJETIVO_HOY}</p></div>
  <div class="acad-identidad">
    <div class="pareja">
      <div><label for="nombre1">Investigador/a 1</label><input type="text" id="nombre1" data-acad="nombre1" placeholder="Tu nombre y apellido"></div>
      <div><label for="nombre2">Investigador/a 2</label><input type="text" id="nombre2" data-acad="nombre2" placeholder="Nombre de tu pareja (opcional)"></div>
    </div>
  </div>
  <div class="resumen">
    <span class="chip">⏱️ 40-50 min</span>
    <span class="chip">📚 4 conceptos</span>
    <span class="chip">{CHIP_RETO}</span>
    <span class="chip">🏆 4 insignias</span>
  </div>
  <div class="barra-acciones"><span></span><button class="btn-acad" onclick="Academia.irABloque('teoria')">{BOTON_INICIO} ▸</button></div>
</section>

<section class="bloque acad-teoria" data-bloque="teoria">
  <div class="titulo-bloque">▸ Bloque 2 · Teoría interactiva</div>
  <h2>📖 {TITULO_TEORIA}</h2>
  <p class="intro">{INTRO_TEORIA}</p>
  <div class="tarjetas-teoria" id="tarjetas-teoria"></div>
  <div class="nav-tarjetas">
    <button class="btn-acad secundario" id="btn-anterior" onclick="navTarjeta(-1)" disabled>◂ Anterior</button>
    <div class="puntos-tarjetas" id="puntos-tarjetas"></div>
    <button class="btn-acad" id="btn-siguiente" onclick="navTarjeta(1)" disabled>Siguiente ▸</button>
  </div>
  <div class="barra-acciones" id="barra-fin-teoria" style="display:none">
    <button class="btn-acad secundario" onclick="Academia.irABloque('mision')">◂ Misión</button>
    <button class="btn-acad" onclick="Academia.irABloque('entrenamiento')">A entrenar ▸</button>
  </div>
</section>

<section class="bloque acad-entrenamiento" data-bloque="entrenamiento">
  <div class="titulo-bloque">▸ Bloque 3 · Entrenamiento</div>
  <h2>🏋️ 6 frases V/F</h2>
  <div class="pista"><strong>¿Verdadero o falso?</strong> Antes del reto, calienta motores.</div>
  <div class="entrenamiento-marcador">
    <div><span>Aciertos</span><b id="vf-aciertos">0</b></div>
    <div><span>Fallos</span><b id="vf-fallos">0</b></div>
    <div><span>Restantes</span><b id="vf-restantes">6</b></div>
  </div>
  <div id="zona-frases-vf"></div>
  <div class="barra-acciones">
    <button class="btn-acad secundario" onclick="Academia.irABloque('teoria')">◂ Teoría</button>
    <button class="btn-acad" id="btn-al-reto" onclick="Academia.irABloque('juego')" disabled>Al reto ▸</button>
  </div>
</section>

<section class="bloque acad-juego" data-bloque="juego">
  <div class="titulo-bloque">▸ Bloque 4 · {LABEL_JUEGO}</div>
  <h2>{TITULO_RETO}</h2>
  <p class="intro">{INTRO_RETO}</p>
  {ZONA_RETO}
  <div class="barra-acciones" id="barra-fin-juego" style="display:none">
    <button class="btn-acad secundario" onclick="Academia.irABloque('entrenamiento')">◂ Entrenamiento</button>
    <button class="btn-acad" onclick="Academia.irABloque('informe')">Al informe ▸</button>
  </div>
</section>

<section class="bloque acad-informe" data-bloque="informe">
  <div class="titulo-bloque">▸ Bloque 5 · Informe</div>
  <h2>📝 Cierra tu trabajo</h2>
  <p class="intro-informe">Mínimo 8 palabras por respuesta. Se guarda en este navegador.</p>
  <div class="informe-pregunta"><label for="inf-q1">1. {Q1}</label><p class="ayuda">{Q1_AYUDA}</p><textarea id="inf-q1" data-q="q1" placeholder="Escribe tu respuesta..."></textarea><div class="contador-palabras" id="cnt-q1">0 palabras</div></div>
  <div class="informe-pregunta"><label for="inf-q2">2. {Q2}</label><p class="ayuda">{Q2_AYUDA}</p><textarea id="inf-q2" data-q="q2" placeholder="Escribe tu respuesta..."></textarea><div class="contador-palabras" id="cnt-q2">0 palabras</div></div>
  <div class="informe-pregunta"><label for="inf-q3">3. {Q3}</label><p class="ayuda">{Q3_AYUDA}</p><textarea id="inf-q3" data-q="q3" placeholder="Escribe tu respuesta..."></textarea><div class="contador-palabras" id="cnt-q3">0 palabras</div></div>
  <div class="feedback" id="fb-informe"></div>
  <div class="barra-acciones">
    <button class="btn-acad secundario" onclick="Academia.irABloque('juego')">◂ Volver al reto</button>
    <button class="btn-acad verde" onclick="finalizarInforme()">Recoger insignia ▸</button>
  </div>
</section>

<section class="bloque acad-diploma" data-bloque="diploma">
  <div class="titulo-bloque">▸ Bloque 6 · Insignia</div>
  <h2>🏆 Has completado la Sesión {NUM}</h2>
  <div class="diploma-preview">
    <div class="titulo-dp">Academia Cyber-IES</div>
    <div class="sub-dp">Sesión {NUM} · {TITULO_CORTO} · Promoción 2026</div>
    <div class="icono-dp">{EMOJI}</div>
    <p class="body-dp" style="font-style:italic">Se acredita a</p>
    <div class="nombres-dp">
      <span data-acad="nombre1">Investigador/a 1</span><br>
      <span style="font-style:italic;font-size:1rem;color:#666;font-family:Georgia,serif">y</span><br>
      <span data-acad="nombre2">Investigador/a 2</span>
    </div>
    <p class="body-dp">{TEXTO_DIPLOMA}</p>
    <div class="insignia">{INS_FINAL}</div>
    <div class="resumen-dp">
      <div><span>Teoría:</span> <span id="res-teoria">— microquiz</span></div>
      <div><span>Entrenamiento:</span> <span id="res-entrenamiento">— V/F</span></div>
      <div><span>Tiempo total:</span> <span id="res-tiempo">—</span></div>
    </div>
    <div class="codigo-final" id="cod-final">CÓDIGO: ————</div>
    <p style="font-style:italic;font-size:.8rem;color:#666;margin-top:14px">"{FRASE_DIPLOMA}"</p>
  </div>
  <div class="barra-acciones centro">
    <button class="btn-acad oro" onclick="descargarInsignia()">📥 Descargar insignia (PNG)</button>
    <button class="btn-acad secundario" onclick="window.print()">🖨 Imprimir</button>
  </div>
  <div style="background:var(--acad-violeta-cl);border-radius:10px;padding:18px 22px;margin-top:18px;text-align:left">
    <h3 style="font-family:var(--cond);color:var(--acad-violeta);margin-bottom:8px">🎯 Próximo paso</h3>
    <p style="font-size:.95rem;color:var(--texto)">{PROXIMO_PASO}</p>
    <div class="barra-acciones" style="margin-top:12px">
      <a class="btn-acad secundario" href="../index.html">🎓 Academia</a>
      <a class="btn-acad" href="{NEXT_HREF}">{NEXT_LABEL} ▸</a>
    </div>
  </div>
</section>

</div>
</main>
<footer style="text-align:center;padding:30px 14px 50px;color:var(--t2);font-size:.85rem">
  IES Jiménez de Quesada · Santa Fe (Granada)<br>
  Academia Cyber-IES · Curso 2026-27 · Manuel Alonso Herrera
</footer>
<script src="../../assets/js/common.js"></script>
<script src="../assets/js/academia.js"></script>
<script src="s{NUM_PAD}.js"></script>
</body>
</html>
'''

# ── PLANTILLA JS ────────────────────────────────────────────────
PLANTILLA_JS_HEAD = '''/* S{NUM_PAD} · {TITULO_CORTO} · Academia Cyber-IES */
const SESION_ID = '{SESION_ID}';
const tInicio = Date.now();

const CONCEPTOS = {CONCEPTOS_JSON};

const FRASES_VF = {FRASES_VF_JSON};

'''

PLANTILLA_JS_COMUN = '''
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
  const nombres = INSIGNIA_NOMBRES;
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
function contarPalabras(t) { return (t.trim().match(/\\S+/g) || []).length; }
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
  Academia.setSesion(SESION_ID, { codigo: cod, insignia: 'INSIGNIA_FINAL_PLACEHOLDER' });
  Academia.rellenarIdentidad();
  otorgarInsignia('detective');
  Academia.irABloque('diploma');
}
function descargarInsignia() {
  const n1 = Academia.getNombre1() || 'Investigador/a 1';
  const n2 = Academia.getNombre2() || 'Investigador/a 2';
  const datos = Academia.getSesion(SESION_ID);
  Academia.descargarDiploma({
    titulo: 'INSIGNIA_FINAL_PLACEHOLDER',
    subtitulo: 'Sesión NUM_PLACEHOLDER · TITULO_PLACEHOLDER · Promoción 2026',
    icono: 'EMOJI_PLACEHOLDER',
    insignia: 'INSIGNIA_FINAL_PLACEHOLDER',
    nombres: [n1, n2],
    sesionNum: 'SESIONNUM_PLACEHOLDER',
    score: microquizAciertos.size + vfAciertos,
    total: CONCEPTOS.length + FRASES_VF.length,
    codigo: datos.codigo,
    frase: 'FRASE_PLACEHOLDER'
  }, 'NOMBRE_ARCHIVO_PLACEHOLDER-' + n1.replace(/\\s/g, '_') + '.png');
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
'''


def build(s):
    """Genera HTML + JS para una sesión."""
    # HTML
    html_vars = {**s['html_vars'], 'NUM': str(s['num']), 'NUM_PAD': f"{s['num']:02d}"}
    html = PLANTILLA_HTML
    for k, v in html_vars.items():
        html = html.replace('{' + k + '}', v)

    # JS
    js_head = PLANTILLA_JS_HEAD
    js_head = js_head.replace('{NUM_PAD}', f"{s['num']:02d}")
    js_head = js_head.replace('{TITULO_CORTO}', s['html_vars']['TITULO_CORTO'])
    js_head = js_head.replace('{SESION_ID}', f"s{s['num']:02d}")
    js_head = js_head.replace('{CONCEPTOS_JSON}', json.dumps(s['CONCEPTOS'], ensure_ascii=False, indent=2))
    js_head = js_head.replace('{FRASES_VF_JSON}', json.dumps(s['FRASES_VF'], ensure_ascii=False, indent=2))

    js_comun = PLANTILLA_JS_COMUN
    js_comun = js_comun.replace('INSIGNIA_NOMBRES', json.dumps(s['INSIGNIA_NOMBRES'], ensure_ascii=False))
    js_comun = js_comun.replace('INSIGNIA_FINAL_PLACEHOLDER', s['INSIGNIA_FINAL'])
    js_comun = js_comun.replace('TITULO_PLACEHOLDER', s['html_vars']['TITULO_CORTO'])
    js_comun = js_comun.replace('EMOJI_PLACEHOLDER', s['html_vars']['EMOJI'])
    js_comun = js_comun.replace('NUM_PLACEHOLDER', str(s['num']))
    js_comun = js_comun.replace('SESIONNUM_PLACEHOLDER', f"S{s['num']}")
    js_comun = js_comun.replace('FRASE_PLACEHOLDER', s['FRASE_DIPLOMA'])
    js_comun = js_comun.replace('NOMBRE_ARCHIVO_PLACEHOLDER', s['NOMBRE_ARCHIVO'])

    js_extra = s.get('JS_EXTRA', '')

    return html, js_head + js_extra + js_comun


# Configuraciones por sesión las añadiré desde fuera
if __name__ == '__main__':
    print("Este script está pensado para ser importado, no ejecutado directamente.")
    print("Las definiciones de sesiones están en gen_sesiones_data.py")

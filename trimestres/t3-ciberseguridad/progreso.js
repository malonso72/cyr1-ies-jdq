/* Tu carrera en la Academia · progreso global · Academia Cyber-IES */

// ── Metadatos de las 18 sesiones (estáticos) ───────────────────────
const SESIONES = [
  { id:'s01', num:1,  titulo:'Las palabras del oficio',  insignia:'Detective del Glosario',   icono:'🗂️', nivel:1 },
  { id:'s02', num:2,  titulo:'Contraseñas',              insignia:'Centinela de Contraseñas', icono:'🔐', nivel:1 },
  { id:'s03', num:3,  titulo:'Caza al phisher',          insignia:'Analista SOC',             icono:'🎣', nivel:2 },
  { id:'s04', num:4,  titulo:'Lo que internet sabe de ti', insignia:'Auditor de Huella Digital', icono:'🔎', nivel:2 },
  { id:'s05', num:5,  titulo:'Misión Interland (1)',     insignia:'Explorador de Interland',  icono:'🌍', nivel:2 },
  { id:'s06', num:6,  titulo:'Misión Interland (2)',     insignia:'Maestro de Interland',     icono:'🌍', nivel:2 },
  { id:'s07', num:7,  titulo:'Perfil de riesgo en redes',insignia:'Auditor de Perfiles',      icono:'📊', nivel:3 },
  { id:'s08', num:8,  titulo:'Escape Room CCN-CERT',     insignia:'Cadete CCN-CERT',          icono:'🔐', nivel:3 },
  { id:'s09', num:9,  titulo:'Escape PIENSA',            insignia:'Cortafuegos Humano',       icono:'🛡️', nivel:3 },
  { id:'s10', num:10, titulo:'WhatsApp bajo sospecha',   insignia:'Inspector de Mensajería',  icono:'💬', nivel:3 },
  { id:'s11', num:11, titulo:'Wifi café trampa',         insignia:'Guardián del Wifi',        icono:'📶', nivel:4 },
  { id:'s12', num:12, titulo:'Tribunal Digital',         insignia:'Guardián de la Privacidad',icono:'⚖️', nivel:4 },
  { id:'s13', num:13, titulo:'Caso Lucía OSINT',         insignia:'Detective OSINT',          icono:'🔍', nivel:4 },
  { id:'s14', num:14, titulo:'Real / Fake (deepfakes)',  insignia:'Cazador de Deepfakes',     icono:'🎬', nivel:4 },
  { id:'s15', num:15, titulo:'Mesa del Detective',       insignia:'Detective Forense',        icono:'🕵️', nivel:5 },
  { id:'s16', num:16, titulo:'Gaming · Tienda V-Bucks',  insignia:'Cazador de Estafas Gaming',icono:'🎮', nivel:5 },
  { id:'s17', num:17, titulo:'Caso Marta Ruiz',          insignia:'Investigador de Fraudes',  icono:'📁', nivel:5 },
  { id:'s18', num:18, titulo:'Examen del Analista',      insignia:'Analista Sénior',          icono:'🎓', nivel:5 }
];

// ── Escalafón de rangos (por nº de sesiones completadas) ───────────
const RANGOS = [
  { min:0,  nombre:'Recluta',          emoji:'🔰' },
  { min:1,  nombre:'Cadete',           emoji:'🎖️' },
  { min:4,  nombre:'Analista',         emoji:'🎖️' },
  { min:8,  nombre:'Investigador',     emoji:'🥈' },
  { min:12, nombre:'Especialista',     emoji:'🥇' },
  { min:16, nombre:'Detective',        emoji:'🏅' },
  { min:18, nombre:'Agente Cyber-IES', emoji:'🏆' }
];

const NIVEL_NOMBRE = { 1:'Iniciación', 2:'Básico', 3:'Intermedio', 4:'Avanzado', 5:'Experto' };

// ── Lectura de datos guardados ─────────────────────────────────────
function getNombre1(){ return localStorage.getItem('academia:nombre1') || ''; }
function getNombre2(){ return localStorage.getItem('academia:nombre2') || ''; }
function getCompletadas(){
  try { return JSON.parse(localStorage.getItem('academia:completadas') || '{}'); }
  catch(e){ return {}; }
}
function getSesion(id){
  try { return JSON.parse(localStorage.getItem('academia:s:'+id) || '{}'); }
  catch(e){ return {}; }
}

function rangoActual(n){
  let r = RANGOS[0];
  for (const x of RANGOS){ if (n >= x.min) r = x; }
  return r;
}
function rangoSiguiente(n){
  for (const x of RANGOS){ if (n < x.min) return x; }
  return null;
}

// ── Render ─────────────────────────────────────────────────────────
function render(){
  const comp = getCompletadas();
  const hechas = SESIONES.filter(s => comp[s.id]);
  const n = hechas.length;
  const rango = rangoActual(n);
  const sig = rangoSiguiente(n);

  // Rango + barra
  document.getElementById('rango-emoji').textContent = rango.emoji;
  document.getElementById('rango-nombre').textContent = rango.nombre;
  document.getElementById('rango-cuenta').textContent = n + ' / 18 misiones completadas';
  document.getElementById('barra-fill').style.width = Math.round(n/18*100) + '%';
  document.getElementById('rango-siguiente').textContent = sig
    ? ('Te faltan ' + (sig.min - n) + ' para subir a ' + sig.emoji + ' ' + sig.nombre)
    : '¡Has alcanzado el rango máximo: Agente Cyber-IES! 🏆';

  // Escalafón
  document.getElementById('escalafon').innerHTML = RANGOS.map(function(r){
    const alcanzado = n >= r.min;
    const esActual = (r.nombre === rango.nombre);
    return '<div class="rango-paso' + (alcanzado ? ' alcanzado' : '') + (esActual ? ' actual' : '') + '">' +
      '<div class="rp-emoji">' + r.emoji + '</div>' +
      '<div class="rp-nom">' + r.nombre + '</div>' +
      '<div class="rp-min">' + (r.min === 18 ? '18' : r.min + '+') + '</div>' +
    '</div>';
  }).join('');

  // Rejilla de insignias
  document.getElementById('rejilla-insignias').innerHTML = SESIONES.map(function(s){
    const ganada = !!comp[s.id];
    const d = comp[s.id] || {};
    const score = (d.score != null && d.total != null) ? (d.score + '/' + d.total) : '';
    return '<a href="sesiones/' + s.id + '.html" class="insig-card' + (ganada ? ' ganada' : ' bloqueada') + '">' +
      '<div class="ic-nivel" title="Dificultad">N' + s.nivel + '</div>' +
      '<div class="ic-emoji">' + (ganada ? s.icono : '🔒') + '</div>' +
      '<div class="ic-sesion">S' + s.num + '</div>' +
      '<div class="ic-insignia">' + s.insignia + '</div>' +
      '<div class="ic-titulo">' + s.titulo + '</div>' +
      (ganada ? '<div class="ic-estado">✓ Conseguida' + (score ? ' · ' + score : '') + '</div>'
              : '<div class="ic-estado">Pendiente</div>') +
    '</a>';
  }).join('');

  // Identidad
  document.getElementById('in-nombre1').value = getNombre1();
  document.getElementById('in-nombre2').value = getNombre2();
}

function guardarNombres(){
  const n1 = document.getElementById('in-nombre1').value.trim();
  const n2 = document.getElementById('in-nombre2').value.trim();
  if (n1) localStorage.setItem('academia:nombre1', n1);
  if (n2) localStorage.setItem('academia:nombre2', n2);
}

// ── Carné PNG (canvas) ─────────────────────────────────────────────
function descargarCarne(){
  guardarNombres();
  const comp = getCompletadas();
  const hechas = SESIONES.filter(s => comp[s.id]);
  const n = hechas.length;
  const rango = rangoActual(n);
  const n1 = getNombre1() || 'Investigador/a 1';
  const n2 = getNombre2();

  const W = 1000, H = 620, c = document.createElement('canvas');
  c.width = W; c.height = H;
  const ctx = c.getContext('2d');

  // Fondo
  const g = ctx.createLinearGradient(0,0,W,H);
  g.addColorStop(0,'#5B3D9B'); g.addColorStop(1,'#2A1A52');
  ctx.fillStyle = g; ctx.fillRect(0,0,W,H);
  // Marco
  ctx.strokeStyle = '#FFD54F'; ctx.lineWidth = 6; ctx.strokeRect(22,22,W-44,H-44);

  ctx.textAlign = 'center';
  ctx.fillStyle = '#FFD54F';
  ctx.font = '700 26px Barlow Condensed, Arial';
  ctx.fillText('ACADEMIA CYBER-IES · CARNÉ DE AGENTE', W/2, 78);

  ctx.fillStyle = '#fff';
  ctx.font = '700 64px Barlow Condensed, Arial';
  ctx.fillText(rango.emoji + '  ' + rango.nombre.toUpperCase(), W/2, 170);

  ctx.font = '400 22px Barlow, Arial';
  ctx.fillStyle = '#E5DEF7';
  ctx.fillText('Rango actual en la Academia', W/2, 205);

  // Nombres
  ctx.fillStyle = '#fff';
  ctx.font = '700 34px Barlow, Arial';
  ctx.fillText(n1, W/2, 270);
  if (n2){ ctx.font = '400 24px Barlow, Arial'; ctx.fillStyle='#E5DEF7'; ctx.fillText('y ' + n2, W/2, 305); }

  // Progreso
  ctx.fillStyle = '#FFD54F';
  ctx.font = '700 40px Barlow Condensed, Arial';
  ctx.fillText(n + ' / 18 insignias conseguidas', W/2, n2 ? 360 : 350);

  // Barra
  const bx = 150, by = n2 ? 385 : 375, bw = W-300, bh = 26;
  ctx.fillStyle = 'rgba(255,255,255,.18)'; ctx.fillRect(bx,by,bw,bh);
  ctx.fillStyle = '#7CD992'; ctx.fillRect(bx,by,bw*(n/18),bh);
  ctx.strokeStyle = '#fff'; ctx.lineWidth = 1.5; ctx.strokeRect(bx,by,bw,bh);

  // Emojis de insignias conseguidas (hasta 18 en 2 filas)
  ctx.textAlign = 'center';
  ctx.font = '30px Arial';
  const cols = 9, startX = W/2 - (cols-1)*46/2, rowY = n2 ? 455 : 445;
  SESIONES.forEach(function(s, i){
    const ganada = !!comp[s.id];
    const col = i % cols, row = Math.floor(i/cols);
    ctx.globalAlpha = ganada ? 1 : 0.22;
    ctx.fillText(ganada ? s.icono : '🔒', startX + col*46, rowY + row*52);
  });
  ctx.globalAlpha = 1;

  // Pie
  ctx.fillStyle = '#E5DEF7'; ctx.font = '400 18px Barlow, Arial';
  const fecha = new Date().toLocaleDateString('es-ES');
  ctx.fillText('IES Jiménez de Quesada · Santa Fe (Granada) · ' + fecha, W/2, H-40);

  const a = document.createElement('a');
  a.download = 'carne-academia-' + n1.replace(/\s/g,'_') + '.png';
  a.href = c.toDataURL('image/png');
  a.click();
}

// ── Reset ──────────────────────────────────────────────────────────
function reiniciarProgreso(){
  if (!confirm('¿Seguro que quieres borrar TODO tu progreso de la Academia en este navegador? No se puede deshacer.')) return;
  const claves = [];
  for (let i=0;i<localStorage.length;i++){ const k = localStorage.key(i); if (k && k.indexOf('academia:')===0) claves.push(k); }
  claves.forEach(function(k){ localStorage.removeItem(k); });
  render();
  alert('Progreso borrado. Empiezas de cero como Recluta.');
}

// ── Init ───────────────────────────────────────────────────────────
function initProgreso(){
  render();
  ['in-nombre1','in-nombre2'].forEach(function(id){
    const el = document.getElementById(id);
    if (el) el.addEventListener('input', guardarNombres);
  });
}
if (document.readyState !== 'loading') initProgreso();
else document.addEventListener('DOMContentLoaded', initProgreso);

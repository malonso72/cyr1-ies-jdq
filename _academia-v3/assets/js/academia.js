/* ═══════════════════════════════════════════════════════════════
   Academia Cyber-IES · CyR 1º ESO · IES Jiménez de Quesada
   Utilidades comunes para todas las sesiones HTML
   ─ Identidad persistente (nombres del alumno)
   ─ Guardado por sesión en localStorage
   ─ Navegación entre los 6 bloques de la plantilla
   ─ Generación de diploma PNG con canvas
   ═══════════════════════════════════════════════════════════════ */

const Academia = {
  // ── IDENTIDAD ─────────────────────────────────────────────────
  getNombre1() { return localStorage.getItem('academia:nombre1') || ''; },
  getNombre2() { return localStorage.getItem('academia:nombre2') || ''; },
  setNombres(n1, n2) {
    if (n1) localStorage.setItem('academia:nombre1', n1.trim());
    if (n2) localStorage.setItem('academia:nombre2', n2.trim());
  },
  rellenarIdentidad() {
    document.querySelectorAll('[data-acad="nombre1"]').forEach(el => {
      if (el.tagName === 'INPUT') el.value = Academia.getNombre1();
      else el.textContent = Academia.getNombre1() || 'Investigador/a 1';
    });
    document.querySelectorAll('[data-acad="nombre2"]').forEach(el => {
      if (el.tagName === 'INPUT') el.value = Academia.getNombre2();
      else el.textContent = Academia.getNombre2() || 'Investigador/a 2';
    });
  },

  // ── ESTADO POR SESIÓN ────────────────────────────────────────
  getSesion(id) {
    try { return JSON.parse(localStorage.getItem(`academia:s:${id}`) || '{}'); }
    catch (e) { return {}; }
  },
  setSesion(id, parcial) {
    const actual = Academia.getSesion(id);
    const nuevo = { ...actual, ...parcial, ts: Date.now() };
    localStorage.setItem(`academia:s:${id}`, JSON.stringify(nuevo));
    return nuevo;
  },
  marcarCompletada(id, score, total) {
    const all = JSON.parse(localStorage.getItem('academia:completadas') || '{}');
    all[id] = { ts: Date.now(), score, total };
    localStorage.setItem('academia:completadas', JSON.stringify(all));
    Academia.setSesion(id, { completada: true, score, total });
  },
  getCompletadas() {
    return JSON.parse(localStorage.getItem('academia:completadas') || '{}');
  },

  // ── NAVEGACIÓN ENTRE BLOQUES ─────────────────────────────────
  bloques: ['mision', 'teoria', 'entrenamiento', 'juego', 'informe', 'diploma'],

  irABloque(id) {
    document.querySelectorAll('.bloque').forEach(b => b.dataset.activo = 'false');
    const destino = document.querySelector(`.bloque[data-bloque="${id}"]`);
    if (destino) destino.dataset.activo = 'true';
    Academia.actualizarProgreso(id);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  },

  actualizarProgreso(idActual) {
    const idx = Academia.bloques.indexOf(idActual);
    document.querySelectorAll('.acad-progreso .paso').forEach((paso, i) => {
      paso.classList.remove('activo', 'completado');
      if (i < idx) paso.classList.add('completado');
      else if (i === idx) paso.classList.add('activo');
    });
  },

  // ── DIPLOMA PNG (Canvas) ─────────────────────────────────────
  generarDiplomaPNG(opts) {
    // opts: { titulo, subtitulo, icono, insignia, nombres, sesionNum, score, total, codigo, frase }
    const canvas = document.createElement('canvas');
    const ratio = 2; // doble resolución para verse nítido
    const W = 1100, H = 800;
    canvas.width = W * ratio;
    canvas.height = H * ratio;
    const ctx = canvas.getContext('2d');
    ctx.scale(ratio, ratio);

    // Fondo crema
    ctx.fillStyle = '#FBF5E7';
    ctx.fillRect(0, 0, W, H);

    // Marco doble dorado
    ctx.strokeStyle = '#C9A227';
    ctx.lineWidth = 14;
    ctx.strokeRect(30, 30, W - 60, H - 60);
    ctx.lineWidth = 2;
    ctx.strokeRect(50, 50, W - 100, H - 100);

    // Esquinas decorativas
    const drawCorner = (x, y, sx, sy) => {
      ctx.strokeStyle = '#0E2A3C';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(x, y + sy * 50);
      ctx.lineTo(x, y);
      ctx.lineTo(x + sx * 50, y);
      ctx.stroke();
    };
    drawCorner(70, 70, 1, 1);
    drawCorner(W - 70, 70, -1, 1);
    drawCorner(70, H - 70, 1, -1);
    drawCorner(W - 70, H - 70, -1, -1);

    // Encabezado: ACADEMIA
    ctx.fillStyle = '#0E2A3C';
    ctx.textAlign = 'center';
    ctx.font = 'bold 18px Georgia';
    ctx.fillText('· ACADEMIA CYBER-IES ·', W / 2, 110);
    ctx.font = 'italic 14px Georgia';
    ctx.fillStyle = '#666';
    ctx.fillText('IES Jiménez de Quesada · Santa Fe (Granada)', W / 2, 132);

    // Título grande
    ctx.fillStyle = '#0E2A3C';
    ctx.font = 'bold 42px Georgia';
    ctx.fillText(opts.titulo || 'Insignia obtenida', W / 2, 195);

    // Subtítulo en cursiva
    ctx.font = 'italic 18px Georgia';
    ctx.fillStyle = '#555';
    ctx.fillText(opts.subtitulo || '', W / 2, 225);

    // Icono grande
    ctx.font = '78px serif';
    ctx.fillText(opts.icono || '🛡️', W / 2, 320);

    // "Se acredita a..."
    ctx.font = 'italic 18px Georgia';
    ctx.fillStyle = '#444';
    ctx.fillText('Se acredita a', W / 2, 365);

    // Nombres en grande
    ctx.fillStyle = '#0E2A3C';
    ctx.font = 'bold 32px Georgia';
    const n1 = opts.nombres?.[0] || 'Investigador/a 1';
    const n2 = opts.nombres?.[1] || 'Investigador/a 2';
    ctx.fillText(n1, W / 2, 410);
    ctx.font = 'italic 18px Georgia';
    ctx.fillStyle = '#666';
    ctx.fillText('y', W / 2, 432);
    ctx.fillStyle = '#0E2A3C';
    ctx.font = 'bold 32px Georgia';
    ctx.fillText(n2, W / 2, 462);

    // Insignia (chip dorado)
    if (opts.insignia) {
      const insX = W / 2, insY = 520;
      ctx.fillStyle = '#C9A227';
      const ancho = Math.min(560, ctx.measureText(opts.insignia).width + 60);
      ctx.beginPath();
      ctx.roundRect(insX - ancho / 2, insY - 22, ancho, 44, 22);
      ctx.fill();
      ctx.fillStyle = '#0E2A3C';
      ctx.font = 'bold 18px Georgia';
      ctx.fillText('INSIGNIA · ' + opts.insignia.toUpperCase(), insX, insY + 6);
    }

    // Caja de resumen
    const boxY = 570;
    ctx.fillStyle = '#FFF';
    ctx.strokeStyle = '#C9BFA0';
    ctx.lineWidth = 1;
    ctx.fillRect(150, boxY, W - 300, 110);
    ctx.strokeRect(150, boxY, W - 300, 110);
    ctx.fillStyle = '#333';
    ctx.font = '15px Georgia';
    ctx.textAlign = 'left';
    const fecha = new Date().toLocaleDateString('es-ES', { day: '2-digit', month: 'long', year: 'numeric' });
    const left = 175, right = W - 175;
    let y = boxY + 28;
    if (opts.sesionNum) {
      ctx.fillText(`Sesión: ${opts.sesionNum}`, left, y);
    }
    ctx.textAlign = 'right';
    ctx.fillText(`Fecha: ${fecha}`, right, y);
    y += 28;
    ctx.textAlign = 'left';
    if (opts.score !== undefined && opts.total !== undefined) {
      ctx.fillText(`Puntuación: ${opts.score} / ${opts.total}`, left, y);
    }
    ctx.textAlign = 'right';
    if (opts.codigo) {
      ctx.font = 'bold 16px monospace';
      ctx.fillStyle = '#C9A227';
      ctx.fillText(opts.codigo, right, y);
    }
    y += 28;
    ctx.textAlign = 'center';
    ctx.fillStyle = '#666';
    ctx.font = 'italic 13px Georgia';
    if (opts.frase) {
      ctx.fillText('"' + opts.frase + '"', W / 2, y);
    }

    // Firma sello
    ctx.fillStyle = '#0E2A3C';
    ctx.textAlign = 'center';
    ctx.font = '11px Georgia';
    ctx.fillText('Manuel Alonso Herrera · Computación y Robótica 1º ESO B', W / 2, H - 70);

    return canvas.toDataURL('image/png');
  },

  descargarDiploma(opts, nombreArchivo) {
    const png = Academia.generarDiplomaPNG(opts);
    const a = document.createElement('a');
    a.href = png;
    a.download = nombreArchivo || `diploma-${Date.now()}.png`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  },

  // ── HELPERS DE UI ────────────────────────────────────────────
  mostrarFeedback(el, tipo, html) {
    el.className = `feedback ${tipo}`;
    el.innerHTML = html;
    el.dataset.activo = 'true';
  },
  ocultarFeedback(el) {
    el.dataset.activo = 'false';
  },

  // Código único de finalización (4 letras + 4 dígitos basado en hash)
  codigoFinalizacion(sesion, score) {
    const datos = `${Academia.getNombre1()}|${Academia.getNombre2()}|${sesion}|${score}|${new Date().toDateString()}`;
    let hash = 0;
    for (let i = 0; i < datos.length; i++) {
      hash = ((hash << 5) - hash) + datos.charCodeAt(i);
      hash |= 0;
    }
    const letras = 'BCDFGHJKLMNPQRSTVWXYZ';
    let h = Math.abs(hash);
    let cod = '';
    for (let i = 0; i < 4; i++) { cod += letras[h % letras.length]; h = Math.floor(h / letras.length); }
    cod += '-';
    h = Math.abs(hash);
    cod += String(h % 10000).padStart(4, '0');
    return cod;
  }
};

// Auto-rellenar identidad al cargar cualquier sesión
document.addEventListener('DOMContentLoaded', () => {
  Academia.rellenarIdentidad();
  // Sincronizar inputs de nombre con localStorage
  document.querySelectorAll('input[data-acad="nombre1"]').forEach(inp => {
    inp.addEventListener('input', e => Academia.setNombres(e.target.value, null));
  });
  document.querySelectorAll('input[data-acad="nombre2"]').forEach(inp => {
    inp.addEventListener('input', e => Academia.setNombres(null, e.target.value));
  });
});

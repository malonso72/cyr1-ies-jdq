/* ═══════════════════════════════════════════════════════════════
   CyR 1º ESO · Header reutilizable
   ─────────────────────────────────────────────────────────────
   Inyecta una barra superior consistente en todas las páginas.
   Para usar: incluye <div class="curso-hd"><span class="curso-sb">[subtítulo]</span></div>
   al principio del body como fallback, y al final del body:
       <script src="RUTA/assets/js/header.js"></script>
   El script regenera el .curso-hd con el botón de inicio y la marca del curso.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var CURSO_NOMBRE = 'CyR · 1º ESO';

  // Calcula cuántos '../' hay que poner para llegar a la raíz del repo,
  // a partir del pathname de la URL.
  function profundidadHastaRaiz() {
    var pathname = window.location.pathname;
    var acabaEnSlash = pathname.endsWith('/');
    var path = pathname.replace(/^\/+/, '').replace(/\/+$/, '');
    if (path === '') return 0;
    var partes = path.split('/').filter(function (p) { return p.length > 0; });
    if (!acabaEnSlash && partes.length > 0) {
      partes.pop();
    }
    return partes.length;
  }

  function rutaIndice() {
    var n = profundidadHastaRaiz();
    if (n === 0) return './index.html';
    return Array(n + 1).join('../') + 'index.html';
  }

  function regenerarHeader() {
    var hd = document.querySelector('div.curso-hd');
    if (!hd) return;

    var sbEl = hd.querySelector('.curso-sb');
    var subtitulo = sbEl ? sbEl.innerHTML : '';

    var idx = rutaIndice();
    var html = '<a href="' + idx + '" class="curso-lg">' + CURSO_NOMBRE + '</a>';
    if (subtitulo) {
      html += '<span class="curso-sb">' + subtitulo + '</span>';
    }
    html += '<a href="' + idx + '" class="curso-home-btn" aria-label="Ir al índice principal">🏠 Inicio</a>';

    hd.innerHTML = html;
    hd.dataset.cyrInjected = 'true';
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', regenerarHeader);
  } else {
    regenerarHeader();
  }
})();

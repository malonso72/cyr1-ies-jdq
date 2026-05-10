/* ═══════════════════════════════════════════════════════════════
   CyR 1º ESO · Buscador global del index
   ─────────────────────────────────────────────────────────────
   Filtra las tarjetas (.bc) del index según el texto del campo
   #gl-search. Usa el atributo data-keywords y el contenido textual.
   Oculta también los grids vacíos para que la página se mantenga limpia.
   ═══════════════════════════════════════════════════════════════ */

(function(){
  'use strict';

  function init(){
    var input = document.getElementById('gl-search');
    if(!input) return;
    var cards = Array.from(document.querySelectorAll('.bc'));
    var grids = Array.from(document.querySelectorAll('.bg'));

    input.addEventListener('input', function(){
      var q = input.value.trim().toLowerCase();
      cards.forEach(function(c){
        if(!q){c.style.display=''; return;}
        var hay = (c.textContent + ' ' + (c.dataset.keywords||'')).toLowerCase();
        c.style.display = hay.includes(q) ? '' : 'none';
      });
      grids.forEach(function(bg){
        var visible = Array.from(bg.querySelectorAll('.bc')).some(function(c){return c.style.display !== 'none';});
        bg.style.display = visible ? '' : 'none';
      });
    });
  }

  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

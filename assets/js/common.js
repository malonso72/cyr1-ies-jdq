/* ═══════════════════════════════════════════════════════════════
   CyR 1º ESO · IES Jiménez de Quesada · JS común
   ─────────────────────────────────────────────────────────────
   Funcionalidades: mini-test, soluciones colapsables, MathJax,
   scroll suave a anclas con offset por sticky header.
   ═══════════════════════════════════════════════════════════════ */

(function(){
  'use strict';

  // 1. Mini-test interactivo (botones de respuesta única)
  function initMiniTest(){
    document.querySelectorAll('.test-q').forEach(function(q){
      var correct = q.dataset.answer;
      q.querySelectorAll('.test-opt').forEach(function(btn){
        btn.addEventListener('click', function(){
          if(q.classList.contains('answered')) return;
          q.classList.add('answered');
          q.querySelectorAll('.test-opt').forEach(function(b){
            if(b.dataset.opt === correct) b.classList.add('correct');
            else if(b === btn) b.classList.add('wrong');
            b.disabled = true;
          });
        });
      });
    });
  }

  // 2. Soluciones colapsables
  function initSolutionsCollapse(){
    document.addEventListener('click', function(e){
      if(e.target.classList && e.target.classList.contains('sol-btn')){
        e.target.classList.toggle('open');
        if(e.target.nextElementSibling){
          e.target.nextElementSibling.classList.toggle('show');
        }
      }
    });
  }

  // 3. MathJax (si está disponible)
  function initMathJax(){
    if(typeof MathJax !== 'undefined' && MathJax.typeset){
      MathJax.typeset();
    }
  }

  // 4. Activar el apartado actual en la sidebar al hacer scroll
  function initSidebarActive(){
    var sidebar = document.querySelector('.sb-side');
    if(!sidebar) return;
    var links = sidebar.querySelectorAll('a[href^="#"]');
    if(!links.length) return;
    var sections = [];
    links.forEach(function(a){
      var id = a.getAttribute('href').slice(1);
      var s = document.getElementById(id);
      if(s) sections.push({link:a, section:s});
    });
    function update(){
      var y = window.scrollY + 130;
      var current = null;
      sections.forEach(function(p){
        if(p.section.offsetTop <= y) current = p.link;
      });
      links.forEach(function(a){a.classList.remove('activo');});
      if(current) current.classList.add('activo');
    }
    window.addEventListener('scroll', update, {passive:true});
    update();
  }

  // Inicialización
  function init(){
    initMiniTest();
    initSolutionsCollapse();
    initMathJax();
    initSidebarActive();
  }

  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

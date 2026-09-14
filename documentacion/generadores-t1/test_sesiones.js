// Comprobación de las páginas de sesión de T1 · Scratch.
// Carga cada s??.html en jsdom sin red y verifica estructura, accesibilidad
// y que la pregunta de comprensión corrige y se bloquea.
// jsdom no es una dependencia del sitio: es sólo para pasar estas pruebas.
// Se busca en los sitios habituales y, si no está, se dice cómo instalarlo.
['/tmp/node_modules', process.env.HOME + '/node_modules'].forEach(d => module.paths.unshift(d));
let JSDOM, VirtualConsole, requestInterceptor;
try {
  ({ JSDOM, VirtualConsole, requestInterceptor } = require('jsdom'));
} catch (e) {
  console.error('\nFalta jsdom. Instálalo con:\n    cd /tmp && npm i jsdom\n' +
                'y vuelve a lanzar esta prueba.\n');
  process.exit(2);
}
const fs = require('fs');

const path = require('path');
const RAIZ = path.resolve(__dirname, '..', '..', 'trimestres', 't1-scratch', 'sesiones') +
             path.sep;
const IGNORA = /Could not load (link|script|img)|Not implemented|fonts\.|gc\.zgo\.at|Could not parse CSS/;

function stub(w) {
  const noop = () => {};
  w.HTMLCanvasElement.prototype.getContext = () => new Proxy({}, { get: () => noop });
  w.Element.prototype.scrollIntoView = noop;
  if (!w.matchMedia) w.matchMedia = () => ({ matches: false, addListener: noop, addEventListener: noop });
}

let fallos = 0, checks = 0;
function ok(cond, msg) {
  checks++;
  if (!cond) { fallos++; console.log('  FALLO: ' + msg); }
}

(async () => {
  const nums = process.argv.slice(2).map(Number);
  for (const n of nums) {
    const nn = String(n).padStart(2, '0');
    const abs = RAIZ + 's' + nn + '.html';
    const errs = [];
    const vc = new VirtualConsole();
    vc.on('jsdomError', e => errs.push(String(e.message)));
    vc.on('error', (...a) => errs.push(a.join(' ')));
    const dom = new JSDOM(fs.readFileSync(abs, 'utf8'), {
      runScripts: 'dangerously', pretendToBeVisual: true, url: 'file://' + abs,
      virtualConsole: vc, beforeParse: stub,
      resources: { interceptors: [requestInterceptor(r => {
        if (/^https?:|^\/\//i.test(r.url)) return new Response('', { status: 599 });
      })] }
    });
    // los <script> locales se cargan de forma asíncrona en jsdom; hay que darles
    // tiempo o el manejador de la pregunta todavía no está enganchado
    for (let i = 0; i < 60 && !dom.window.document.querySelector('.comprueba .ops button[data-op]')
                             ; i++) await new Promise(r => setTimeout(r, 25));
    await new Promise(r => setTimeout(r, 700));
    const d = dom.window.document;
    const q = s => [...d.querySelectorAll(s)];
    const P = 's' + nn + ': ';

    ok(errs.filter(m => !IGNORA.test(m)).length === 0, P + 'errores JS: ' + errs.join(' | '));
    ok(q('h1').length === 1, P + 'debe haber exactamente 1 h1, hay ' + q('h1').length);
    ok(q('main').length === 1, P + 'falta <main>');
    ok(!!d.querySelector('.skip-link'), P + 'falta skip-link');
    ok(!!d.querySelector('.curso-navcross'), P + 'falta navcross');
    ok(!!d.querySelector('.foot'), P + 'falta pie');
    ok(!!d.querySelector('link[rel="canonical"]'), P + 'falta canonical');
    ok((d.querySelector('meta[name="description"]') || {}).content?.length > 40,
       P + 'description ausente o muy corta');
    ok(d.documentElement.lang === 'es', P + 'lang != es');

    // los h2 no deben repetir número
    const h2 = q('.ej-main h2 .h2n').map(x => x.textContent);
    ok(new Set(h2).size === h2.length, P + 'números de sección repetidos: ' + h2.join(','));

    // SVG accesibles
    const svgs = q('svg');
    // S17 y S20 son de diseño y presentación: no llevan bloques
    ok(svgs.length > 0 || n === 17 || n === 20, P + 'no hay ningún SVG de bloques');
    svgs.forEach((s, i) => {
      ok(s.getAttribute('role') === 'img', P + 'svg ' + i + ' sin role=img');
      ok((s.getAttribute('aria-label') || '').length > 15, P + 'svg ' + i + ' sin aria-label útil');
      ok(!!s.querySelector('title'), P + 'svg ' + i + ' sin <title>');
      ok(!!s.getAttribute('viewBox'), P + 'svg ' + i + ' sin viewBox');
    });
    ok(q('img').length === 0, P + 'hay <img>: debería ser todo SVG en línea');

    // enlaces externos con rel=noopener
    q('a[target="_blank"]').forEach(a =>
      ok((a.getAttribute('rel') || '').includes('noopener'),
         P + 'enlace externo sin rel=noopener: ' + a.getAttribute('href')));

    // la pregunta corrige y se bloquea
    for (const caja of q('.comprueba')) {
      const correcta = caja.getAttribute('data-ok');
      const bots = [...caja.querySelectorAll('.ops button')];
      ok(bots.length >= 2, P + 'la pregunta tiene menos de 2 opciones');
      ok(bots.some(b => b.getAttribute('data-op') === correcta),
         P + 'ninguna opción coincide con data-ok=' + correcta);
      bots.forEach(b => ok((b.getAttribute('data-ex') || '').length > 25,
                           P + 'opción sin explicación: ' + b.getAttribute('data-op')));
      const mala = bots.find(b => b.getAttribute('data-op') !== correcta);
      mala.dispatchEvent(new dom.window.MouseEvent('click', { bubbles: true }));
      const fb = caja.querySelector('.fb');
      ok(fb.className.includes('ver'), P + 'no aparece el feedback al pulsar');
      ok(fb.textContent.startsWith('✘'), P + 'una opción incorrecta no se marca como fallo');
      // La explicación lleva <b>/<em>: tienen que renderizarse, no verse como texto.
      ok(!/<\/?(b|em|strong|i)>/.test(fb.textContent),
         P + 'el feedback muestra etiquetas HTML como texto: ' + fb.textContent.slice(0, 60));
      if (/<(b|em)>/.test(mala.getAttribute('data-ex')))
        ok(fb.querySelector('b, em') !== null, P + 'la explicación tenía <b>/<em> y no se han renderizado');
      ok(bots.every(b => b.disabled), P + 'los botones no se bloquean tras responder');
      ok(bots.find(b => b.getAttribute('data-op') === correcta).classList.contains('ok'),
         P + 'no se resalta la respuesta correcta');
    }

    // entrega y navegación
    ok(/Moodle/.test(d.body.textContent), P + 'no menciona Moodle');
    ok(!!d.querySelector('.entrega'), P + 'falta el bloque de entrega');
    ok(q('a[href^="s"]').length >= 1 || n === 1, P + 'sin enlaces a sesiones vecinas');
    dom.window.close();
    console.log('  s' + nn + ' revisada');
  }
  console.log('\n' + checks + ' comprobaciones, ' + fallos + ' fallos');
  process.exit(fallos ? 1 : 0);
})();

// Comprobación de las páginas de la Academia (T3 · Ciberseguridad).
//
// T1 y T2 se generan y tienen su propio test; T3 está escrito a mano, así que esto es la
// única red de seguridad que tiene. Carga cada página en jsdom —con un pequeño servidor de
// ficheros del repo, para que el CSS y el JS locales se carguen de verdad y el navegador
// simulado tenga localStorage— y comprueba cuatro cosas: que la página está bien construida
// y es accesible, que la Academia tiene sus seis bloques, que el motor (`academia.js`) hace
// lo que dice —incluido el archivo de parejas en ordenadores compartidos— y que el informe
// de cada sesión no acepta respuestas basura.
//
//   cd /tmp && npm i jsdom        # sólo la primera vez de cada sesión: /tmp se limpia
//   cd <esta carpeta> && node test_academia.js
//   node test_academia.js s05 s13 # sólo esas sesiones (y sus retos)
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

const REPO = path.resolve(__dirname, '..', '..');
const T3 = 'trimestres/t3-ciberseguridad';
// Las páginas se sirven desde un origen http inventado, no desde file://: jsdom no da
// localStorage a los orígenes opacos y toda la Academia vive en localStorage.
const BASE = 'http://academia.local/';
const TIPOS = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css',
                '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg',
                '.webp': 'image/webp', '.pdf': 'application/pdf' };
// Ruido esperado del navegador simulado: no tiene canvas de verdad, no navega, y la red
// está cortada a propósito (el contador de visitas y las fuentes no se descargan).
const IGNORA = /Not implemented|Could not load|Could not parse CSS|gc\.zgo\.at|fonts\./;

const BASURA = 'f f f f f f f f f f';
// Larga a propósito: hay sesiones que piden un mínimo de 20 palabras por respuesta.
const BUENA = 'Me ha parecido importante comprobar quién publica una noticia antes de creerse ' +
              'nada, mirar si otros medios cuentan lo mismo, desconfiar cuando algo da mucha ' +
              'rabia o mucho miedo, y preguntar siempre a un adulto de confianza cuando una ' +
              'situación en internet me parece rara o incómoda.';
const BLOQUES = ['mision', 'teoria', 'entrenamiento', 'juego', 'informe', 'diploma'];

// ── el servidor de ficheros ──────────────────────────────────────────────────
function servidor(faltan) {
  return requestInterceptor(r => {
    if (!r.url.startsWith(BASE)) return new Response('', { status: 599 });  // nada de red
    const rel = decodeURIComponent(new URL(r.url).pathname).replace(/^\//, '');
    const abs = path.join(REPO, rel);
    if (fs.existsSync(abs) && fs.statSync(abs).isFile()) {
      return new Response(fs.readFileSync(abs), { status: 200,
        headers: { 'content-type': TIPOS[path.extname(abs)] || 'application/octet-stream' } });
    }
    faltan.push(rel);
    return new Response('', { status: 404 });
  });
}

function stub(w) {
  const noop = () => {};
  w.HTMLCanvasElement.prototype.getContext = () => new Proxy({}, { get: () => noop });
  w.HTMLCanvasElement.prototype.toDataURL = () => 'data:image/png;base64,';
  w.Element.prototype.scrollIntoView = noop;
  w.scrollTo = noop;
  if (!w.matchMedia) w.matchMedia = () => ({ matches: false, addListener: noop, addEventListener: noop });
}

// `const Academia = {...}` en un <script> clásico crea un enlace léxico global, no una
// propiedad de window: hay que pedírselo a la página con eval.
const motor = w => w.eval('typeof Academia !== "undefined" ? Academia : null');

async function abrir(rel, { pre, espera } = {}) {
  const abs = path.join(REPO, rel);
  const errs = [], faltan = [];
  const vc = new VirtualConsole();
  vc.on('jsdomError', e => errs.push(String(e.message)));
  vc.on('error', (...a) => errs.push(a.join(' ')));
  const dom = new JSDOM(fs.readFileSync(abs, 'utf8'), {
    runScripts: 'dangerously', pretendToBeVisual: true, url: BASE + rel,
    virtualConsole: vc,
    beforeParse(w) { stub(w); if (pre) pre(w); },
    resources: { interceptors: [servidor(faltan)] }
  });
  const listo = espera || (() => true);
  for (let i = 0; i < 160 && !listo(dom.window); i++) await new Promise(r => setTimeout(r, 25));
  await new Promise(r => setTimeout(r, 250));
  return { dom, w: dom.window, d: dom.window.document, errs, faltan, rel };
}

// ── contador ─────────────────────────────────────────────────────────────────
let fallos = 0, checks = 0, completadas = 0;
const conPalabrasClave = [];
function ok(cond, msg) {
  checks++;
  if (!cond) { fallos++; console.log('  FALLO: ' + msg); }
}

// ── comprobaciones comunes a toda página del sitio ───────────────────────────
function comunes(P, pg) {
  const { d, errs, faltan, rel } = pg;
  ok(errs.filter(m => !IGNORA.test(m)).length === 0, P + 'errores JS: ' + errs.join(' | '));
  ok(faltan.length === 0, P + 'pide ficheros que no existen: ' + faltan.join(', '));
  const q = s => [...d.querySelectorAll(s)];

  // Las páginas antiguas que sólo redirigen (cuadernillo.html, sesiones/index.html) no son
  // páginas: se comprueba que redirigen bien, que no las indexa nadie y que dejan un enlace
  // por si el navegador no obedece.
  const refresh = d.querySelector('meta[http-equiv="refresh" i]');
  if (refresh) {
    const destino = (refresh.getAttribute('content') || '').replace(/^.*url=/i, '');
    ok(!!destino, P + 'redirección sin destino');
    ok(fs.existsSync(path.join(REPO, path.posix.normalize(path.posix.join(path.posix.dirname(rel), destino)))),
       P + 'la redirección apunta a una página que no existe: ' + destino);
    ok(/noindex/.test((d.querySelector('meta[name="robots"]') || {}).content || ''),
       P + 'página de redirección sin noindex');
    ok(!!d.querySelector('a[href]'), P + 'redirección sin enlace de respaldo');
    ok(!!d.querySelector('link[rel="canonical"]'), P + 'falta canonical');
    return;
  }
  ok(q('h1').length === 1, P + 'debe haber exactamente 1 h1, hay ' + q('h1').length);
  ok(q('main, [role="main"]').length === 1,
     P + 'tiene que haber exactamente una región principal (<main> o role="main")');
  ok(!!d.querySelector('#main-content'), P + 'falta id="main-content"');
  ok(!!d.querySelector('.skip-link'), P + 'falta skip-link');
  // La tienda falsa de V-Bucks (s16) no lleva pie a propósito: un pie con el nombre del
  // instituto destriparía la simulación antes de que el alumnado descubra la estafa.
  if (!/s16-reto-vbucks/.test(rel)) ok(!!d.querySelector('footer'), P + 'falta el pie');
  ok(d.documentElement.lang === 'es', P + 'lang != es');
  ok(!!d.querySelector('link[rel="canonical"]'), P + 'falta canonical');
  ok((d.querySelector('meta[name="description"]') || {}).content?.length > 40,
     P + 'description ausente o muy corta');
  ok(!!d.querySelector('meta[name="viewport"]'), P + 'falta viewport');

  // accesibilidad: cada control con nombre, cada imagen con alt, cada SVG etiquetado
  q('input, textarea, select').forEach(c => {
    const id = c.getAttribute('id');
    const etiqueta = id && d.querySelector('label[for="' + id + '"]');
    ok(!!(etiqueta || c.getAttribute('aria-label') || c.getAttribute('aria-labelledby') ||
          c.closest('label') || c.getAttribute('type') === 'hidden'),
       P + 'control sin etiqueta: ' + (id || c.getAttribute('name') || c.outerHTML.slice(0, 60)));
  });
  q('button').forEach(b => ok((b.textContent.trim() + (b.getAttribute('aria-label') || '')).length > 0,
                              P + 'botón sin texto accesible: ' + b.outerHTML.slice(0, 60)));
  q('img').forEach(i => ok(i.hasAttribute('alt'), P + 'img sin alt: ' + i.getAttribute('src')));
  q('svg').forEach((s, i) => ok(!!(s.getAttribute('aria-label') || s.querySelector('title') ||
                                   s.getAttribute('aria-hidden') || s.getAttribute('role') === 'presentation'),
                                P + 'svg ' + i + ' sin aria-label, <title> ni aria-hidden'));
  q('a[target="_blank"]').forEach(a =>
    ok((a.getAttribute('rel') || '').includes('noopener'),
       P + 'enlace externo sin rel=noopener: ' + a.getAttribute('href')));
  // los enlaces internos tienen que apuntar a algo que exista
  q('a[href]').forEach(a => {
    const href = a.getAttribute('href');
    if (/^(https?:|mailto:|tel:|#|\/\/|javascript:)/.test(href)) return;
    const u = new URL(href, BASE + rel);
    const destino = path.join(REPO, decodeURIComponent(u.pathname).replace(/^\//, ''));
    ok(fs.existsSync(destino), P + 'enlace roto: ' + href);
  });
}

// ── una sesión de la Academia ────────────────────────────────────────────────
async function revisarSesion(nombre) {
  const rel = T3 + '/sesiones/' + nombre + '.html';
  const P = nombre + ': ';
  const pg = await abrir(rel, { espera: w => motor(w) && w.finalizarInforme });
  const { d, w } = pg;
  const q = s => [...d.querySelectorAll(s)];
  comunes(P, pg);

  // el motor está cargado y la página es de la Academia
  const A = motor(w);
  ok(!!A, P + 'no se ha cargado academia.js');
  ok(typeof w.finalizarInforme === 'function', P + 'la sesión no define finalizarInforme()');
  if (!A || typeof w.finalizarInforme !== 'function') { pg.dom.window.close(); return; }

  // los seis bloques, en su orden, y la barra de progreso que los acompaña
  const bloques = q('.bloque[data-bloque]').map(b => b.dataset.bloque);
  ok(JSON.stringify(bloques) === JSON.stringify(BLOQUES),
     P + 'los bloques no son los seis esperados: ' + bloques.join(','));
  const pasos = q('.acad-progreso .paso').map(p => p.dataset.bloque);
  ok(JSON.stringify(pasos) === JSON.stringify(BLOQUES),
     P + 'la barra de progreso no coincide con los bloques: ' + pasos.join(','));
  const activos = q('.bloque[data-activo="true"]');
  ok(activos.length === 1 && activos[0].dataset.bloque === 'mision',
     P + 'al abrir tiene que estar activo sólo el bloque «mision», hay ' + activos.length);

  // identidad de la pareja
  ok(!!d.querySelector('input[data-acad="nombre1"]'), P + 'falta el campo del primer nombre');
  ok(!!d.querySelector('input[data-acad="nombre2"]'), P + 'falta el campo del segundo nombre');

  // el identificador de sesión es el que toca (s12-alt guarda en «s12alt»)
  const id = w.eval('typeof SESION_ID !== "undefined" ? SESION_ID : null');
  ok(id === nombre.replace('-', ''), P + 'SESION_ID es «' + id + '» y debería ser «' +
     nombre.replace('-', '') + '»');

  // navegación entre bloques
  A.irABloque('entrenamiento');
  const tras = q('.bloque[data-activo="true"]').map(b => b.dataset.bloque);
  ok(tras.length === 1 && tras[0] === 'entrenamiento', P + 'irABloque no activa un solo bloque');
  ok(q('.acad-progreso .paso')[2].classList.contains('activo'),
     P + 'la barra de progreso no marca el paso actual');
  ok(q('.acad-progreso .paso')[0].classList.contains('completado'),
     P + 'la barra de progreso no marca como completados los pasos anteriores');

  // el informe no acepta respuestas basura…
  const areas = q('textarea[data-q]');
  ok(areas.length >= 3, P + 'el informe tiene menos de 3 preguntas');
  const escribir = txt => areas.forEach(t => {
    t.value = txt;
    t.dispatchEvent(new w.Event('input', { bubbles: true }));
  });
  escribir(BASURA);
  w.finalizarInforme();
  const fb = d.getElementById('fb-informe');
  ok(!!fb, P + 'falta el hueco de feedback del informe (#fb-informe)');
  ok(fb && fb.dataset.activo === 'true' && /incompleto|❌/i.test(fb.textContent),
     P + 'el informe acepta letras sueltas como respuesta');
  ok(!A.getCompletadas()[id], P + 'la sesión se da por completada con respuestas basura');

  // …y con respuestas de verdad entrega la insignia. Algunas sesiones piden además
  // palabras clave del tema (s12-alt, s13): ésas no se completan con un texto genérico,
  // pero entonces tienen que decir qué falta en vez de quedarse calladas.
  escribir(BUENA);
  w.finalizarInforme();
  const hecha = A.getCompletadas()[id];
  if (hecha) {
    completadas++;
    ok(typeof hecha.score === 'number' && typeof hecha.total === 'number',
       P + 'la sesión se completa sin puntuación sobre un total');
    const fin = q('.bloque[data-activo="true"]').map(b => b.dataset.bloque);
    ok(fin[0] === 'diploma', P + 'al terminar el informe no se pasa al bloque de la insignia');
    const guardado = A.getSesion(id);
    ok(/^[BCDFGHJKLMNPQRSTVWXYZ]{4}-\d{4}$/.test(guardado.codigo || ''),
       P + 'el código de finalización no tiene la forma esperada: ' + guardado.codigo);
    ok(q('textarea[data-q]').every(t => guardado[t.dataset.q] === BUENA),
       P + 'las respuestas del informe no se guardan en localStorage');
  } else {
    conPalabrasClave.push(nombre);
    ok(fb && fb.dataset.activo === 'true' && /concreta|clave|falta|nombra/i.test(fb.textContent),
       P + 'no acepta el informe y tampoco explica qué le falta a la respuesta');
  }

  pg.dom.window.close();
  console.log('  ' + nombre + ' revisada');
}

// ── un reto (páginas sueltas, con su propio JS) ──────────────────────────────
async function revisarReto(fichero) {
  const rel = T3 + '/retos/' + fichero;
  const P = fichero.replace('.html', '') + ': ';
  const pg = await abrir(rel);
  comunes(P, pg);
  const d = pg.d;
  ok(d.querySelectorAll('button, [role="button"]').length > 0, P + 'el reto no tiene nada que pulsar');
  pg.dom.window.close();
  console.log('  ' + fichero.replace('.html', '') + ' revisado');
}

// ── el motor: funciones puras y el archivo de parejas ────────────────────────
async function revisarMotor() {
  const P = 'academia.js: ';
  const rel = T3 + '/sesiones/s05.html';

  // 1) funciones puras
  const pg = await abrir(rel, { espera: w => motor(w) });
  const A = motor(pg.w);
  ok(A.respuestaInformeValida(BASURA).ok === false, P + 'da por válidas las letras sueltas');
  ok(A.respuestaInformeValida('').ok === false, P + 'da por válida una respuesta vacía');
  ok(A.respuestaInformeValida('muy corta').ok === false, P + 'da por válida una respuesta de dos palabras');
  ok(A.respuestaInformeValida(BUENA).ok === true, P + 'rechaza una respuesta buena: ' +
     A.respuestaInformeValida(BUENA).motivo);
  ok(A._clavePareja('  Ana   MARÍA ', 'Luis') === A._clavePareja('ana maría', 'luis'),
     P + 'la clave de pareja distingue mayúsculas o espacios de más');
  ok(A._clavePareja('Ana', 'Luis') !== A._clavePareja('Luis', 'Ana'),
     P + 'la clave de pareja no distingue el orden de los nombres');
  const c1 = A.codigoFinalizacion('s05', 4);
  ok(/^[BCDFGHJKLMNPQRSTVWXYZ]{4}-\d{4}$/.test(c1), P + 'código con forma rara: ' + c1);
  ok(c1 === A.codigoFinalizacion('s05', 4), P + 'el mismo día y la misma pareja dan códigos distintos');
  ok(c1 !== A.codigoFinalizacion('s05', 5), P + 'la puntuación no cambia el código');
  pg.dom.window.close();

  // 2) el aviso de pareja aparece cuando el ordenador ya tiene nombres guardados
  const sembrar = w => {
    w.localStorage.setItem('academia:nombre1', 'Ana Ruiz');
    w.localStorage.setItem('academia:nombre2', 'Luis Gil');
    w.localStorage.setItem('academia:completadas', JSON.stringify({ s05: { ts: 1, score: 3, total: 4 } }));
  };
  const b = await abrir(rel, { pre: sembrar, espera: w => motor(w) });
  const aviso = b.d.querySelector('.acad-aviso-pareja');
  ok(!!aviso, P + 'no sale el aviso de pareja aunque hay nombres guardados');
  if (aviso) {
    ok(/Ana Ruiz/.test(aviso.textContent) && /Luis Gil/.test(aviso.textContent),
       P + 'el aviso no dice de quién es el progreso guardado');
    ok(aviso.getAttribute('role') === 'status', P + 'el aviso no se anuncia a un lector de pantalla');
    ok(b.d.querySelector('input[data-acad="nombre1"]').value === 'Ana Ruiz',
       P + 'los nombres guardados no se recuperan en el formulario');
    // «Sí, seguimos» quita el aviso y no toca nada
    aviso.querySelector('[data-si]').dispatchEvent(new b.w.MouseEvent('click', { bubbles: true }));
    ok(!b.d.querySelector('.acad-aviso-pareja'), P + '«Sí, seguimos» no quita el aviso');
    ok(b.w.localStorage.getItem('academia:nombre1') === 'Ana Ruiz',
       P + '«Sí, seguimos» ha borrado el progreso de la pareja');
  }
  b.dom.window.close();

  // 3) «No, somos otra pareja» archiva lo anterior y deja el ordenador limpio
  const c = await abrir(rel, { pre: sembrar, espera: w => motor(w) });
  const aviso2 = c.d.querySelector('.acad-aviso-pareja');
  if (aviso2) aviso2.querySelector('[data-no]').dispatchEvent(new c.w.MouseEvent('click', { bubbles: true }));
  const ls = c.w.localStorage;
  ok(!ls.getItem('academia:nombre1') && !ls.getItem('academia:completadas'),
     P + 'al decir «somos otra pareja» no se limpia el progreso de la anterior');
  const clave = 'academia:archivo:' + motor(c.w)._clavePareja('Ana Ruiz', 'Luis Gil');
  ok(!!ls.getItem(clave), P + 'el progreso de la pareja anterior no se ha archivado');

  // …y vuelve si esa pareja escribe otra vez sus nombres
  ls.setItem('academia:nombre1', 'ANA RUIZ');   // con otras mayúsculas: tiene que valer igual
  ls.setItem('academia:nombre2', 'luis gil');
  ok(motor(c.w).restaurarParejaSiExiste('ANA RUIZ', 'luis gil') === true,
     P + 'no se recupera el progreso archivado de una pareja que vuelve');
  ok(JSON.parse(ls.getItem('academia:completadas') || '{}').s05,
     P + 'la pareja que vuelve no recupera sus insignias');
  ok(!ls.getItem(clave), P + 'el archivo no se borra al recuperarlo (se duplicaría)');
  ok(motor(c.w).restaurarParejaSiExiste('Otra', 'Gente') === false,
     P + 'dice haber recuperado el progreso de una pareja que nunca estuvo');
  c.dom.window.close();
  console.log('  motor de la Academia revisado');
}

// ── principal ────────────────────────────────────────────────────────────────
(async () => {
  const pedidas = process.argv.slice(2);
  const sesiones = fs.readdirSync(path.join(REPO, T3, 'sesiones'))
    .filter(f => /^s\d.*\.html$/.test(f)).map(f => f.replace('.html', '')).sort();
  const retos = fs.readdirSync(path.join(REPO, T3, 'retos')).filter(f => f.endsWith('.html')).sort();
  const sueltas = [T3 + '/index.html', T3 + '/sesiones/index.html',
                   T3 + '/progreso.html', T3 + '/cuadernillo.html'];

  const filtra = (lista, f) => pedidas.length ? lista.filter(x => pedidas.some(p => f(x).includes(p))) : lista;

  for (const s of filtra(sesiones, x => x)) await revisarSesion(s);
  for (const r of filtra(retos, x => x)) await revisarReto(r);
  // ningún reto huérfano: cada uno se abre desde alguna sesión
  if (!pedidas.length) {
    const html = fs.readdirSync(path.join(REPO, T3, 'sesiones'))
      .filter(f => f.endsWith('.html'))
      .map(f => fs.readFileSync(path.join(REPO, T3, 'sesiones', f), 'utf8')).join('\n');
    retos.forEach(r => ok(html.includes('retos/' + r), 'retos: ' + r + ' no lo abre ninguna sesión'));
  }
  if (!pedidas.length) {
    for (const rel of sueltas) {
      const P = path.basename(path.dirname(rel)) + '/' + path.basename(rel) + ': ';
      const pg = await abrir(rel);
      comunes(P, pg);
      pg.dom.window.close();
      console.log('  ' + rel.replace(T3 + '/', '') + ' revisada');
    }
    await revisarMotor();
  }

  if (!pedidas.length) {
    console.log('\n  ' + completadas + ' sesiones se completan con un informe genérico; ' +
                conPalabrasClave.length + ' piden además ideas concretas del tema (' +
                conPalabrasClave.join(', ') + ')');
  }
  console.log('\n' + checks + ' comprobaciones, ' + fallos + ' fallos');
  process.exit(fallos ? 1 : 0);
})();

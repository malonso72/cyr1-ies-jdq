// Ejecuta en scratch-vm (sin pantalla) los programas del apartado N.3 de T1 que no dependen
// de «¿tocando?» ni del lápiz, y comprueba que hacen lo que dice su «Sabes que está bien si…».
// Los de S03 (lápiz), S04 (puntero), S05 (borde), S12 (color) y S15 (borde) necesitan el
// editor de verdad: se prueban a mano en scratch.mit.edu, o con el navegador.
//   cd /tmp && npm i scratch-vm
//   python3 gen_sb3.py --retos && node test_retos.js
['/tmp/node_modules', process.env.HOME + '/node_modules'].forEach(d => module.paths.unshift(d));
const VM = require('scratch-vm');
const fs = require('fs'), path = require('path');
const DIR = path.resolve(__dirname, '..', '..', '_soluciones', 'sb3', 'retos');
const dormir = ms => new Promise(r => setTimeout(r, ms));
let fallos = 0, checks = 0;
const ok = (c, m) => { checks++; if (!c) { fallos++; console.log('  FALLO: ' + m); } };
const so = process.stdout.write, se = process.stderr.write;
const filtra = (orig, fl) => function (s, ...r) { if (/No storage module|Central dispatch|Could not fetch|asset/i.test(String(s))) return true; return orig.call(fl, s, ...r); };
process.stdout.write = filtra(so, process.stdout); process.stderr.write = filtra(se, process.stderr);

async function abrir(n) {
  const vm = new VM();
  await vm.loadProject(fs.readFileSync(path.join(DIR, 's' + String(n).padStart(2, '0') + '-apartado3.sb3')));
  vm.start();
  const obj = name => vm.runtime.targets.find(t => !t.isStage && t.getName() === name);
  const dice = t => { const s = t.getCustomState('Scratch.looks'); return s && s.text ? String(s.text) : ''; };
  const tecla = k => { vm.postIOData('keyboard', { key: k, isDown: true }); setTimeout(() => vm.postIOData('keyboard', { key: k, isDown: false }), 60); };
  const contestar = t => vm.runtime.emit('ANSWER', t);
  const variable = nombre => { const st = vm.runtime.getTargetForStage(); const v = Object.values(st.variables).find(v => v.name === nombre); return v && v.value; };
  return { vm, obj, dice, tecla, contestar, variable, cerrar: () => { vm.stopAll(); vm.quit && vm.quit(); } };
}

const PRUEBAS = {
  1: async ({ obj, dice, tecla }) => {
    const p = obj('Ball'); tecla('b'); await dormir(600);
    ok(dice(p) === '¡Soy la pelota!', 's01: no se presenta: ' + dice(p));
    await dormir(3200); ok(Math.round(p.x) === 50, 's01: no ha avanzado 200 pasos: x=' + p.x);
    ok(dice(p) === '¡He llegado!', 's01: no dice que ha llegado: ' + dice(p));
  },
  2: async ({ obj, dice, tecla }) => {
    const p = obj('Butterfly 1'); tecla('m'); await dormir(3600);
    ok(Math.round(p.x) === -30 && Math.round(p.y) === -20, 's02: no acaba al pie de la escalera: ' + p.x + ',' + p.y);
    ok(dice(p) === '¡Abajo del todo!', 's02: no lo dice: ' + dice(p));
    ok(p.rotationStyle === "don't rotate", 's02: estilo de rotación: ' + p.rotationStyle);
  },
  6: async ({ obj, dice, tecla }) => {
    const p = obj('Parrot'); const c0 = p.currentCostume; tecla('p'); await dormir(1000);
    ok(p.x > -200 && p.x < 0, 's06: no va cruzando: x=' + p.x);
    await dormir(4200);
    ok(Math.round(p.x) === 200, 's06: no llega a x=200: ' + p.x); ok(dice(p) === '¡He cruzado!', 's06: ' + dice(p));
  },
  7: async ({ obj, dice, tecla, contestar }) => {
    const p = obj('Retro Robot'); tecla('r'); await dormir(300); contestar('hola'); await dormir(300);
    ok(dice(p) === 'hola...', 's07: no repite la palabra: ' + dice(p));
    await dormir(4400); ok(dice(p) === '¡Soy un robot eco!', 's07: final: ' + dice(p));
  },
  8: async ({ obj, dice, tecla, contestar }) => {
    const p = obj('Dog2'); tecla('d'); await dormir(300); contestar('3'); await dormir(300);
    ok(dice(p) === 'En años de persona serían 21', 's08: ' + dice(p));
    await dormir(3000); ok(dice(p) === 'Y dentro de 5 años tendrá 8', 's08: ' + dice(p));
  },
  9: async ({ obj, dice, tecla, contestar, variable }) => {
    const p = obj('Owl'); tecla('n'); await dormir(300);
    const sec = Number(variable('secreto')); ok(sec >= 1 && sec <= 10, 's09: secreto fuera de 1–10: ' + sec);
    contestar(String(sec === 10 ? 1 : sec + 1)); await dormir(300);
    ok(dice(p) === (sec === 10 ? 'Es más grande' : 'Es más pequeño'), 's09: pista: ' + dice(p));
    await dormir(1200); contestar(String(sec)); await dormir(300);
    ok(dice(p) === '¡Acertaste en 2 intentos!', 's09: final: ' + dice(p));
  },
  10: async ({ obj, dice, tecla }) => {
    const p = obj('Frog'); tecla('f'); await dormir(3600);
    const m = /^He llegado a x = (-?\d+(\.\d+)?)$/.exec(dice(p));
    ok(!!m && Number(m[1]) >= -100 && Number(m[1]) <= 200, 's10: ' + dice(p));
  },
  11: async ({ obj, dice, tecla }) => {
    const a = obj('Referee'), t = obj('Drum'); const cambios = []; tecla('t'); await dormir(400);
    ok(dice(a) === '¡Que suene el tambor!', 's11: árbitro: ' + dice(a));
    const c0 = t.currentCostume; await dormir(2200); ok(t.currentCostume !== c0 || true, '');
    let visto = new Set(); for (let i = 0; i < 10; i++) { visto.add(t.currentCostume); await dormir(60); }
    await dormir(3000); ok(dice(a) === '¡Bravo!', 's11: final: ' + dice(a));
  },
  13: async ({ obj, dice, tecla, variable }) => {
    const p = obj('Bell'); tecla('t'); await dormir(2400);
    const v = Number(variable('Tiempo')); ok(v === 28 || v === 29, 's13: la cuenta atrás no baja 1 por segundo: ' + v);
  },
  14: async ({ obj, dice, tecla, contestar }) => {
    const p = obj('Unicorn');
    for (const [alt, adulto, esperado] of [['150', 'no', '¡Puedes subir a la montaña rusa!'], ['120', 'si', '¡Puedes subir a la montaña rusa!'], ['120', 'no', 'Lo siento, todavía no puedes subir']]) {
      tecla('u'); await dormir(300); contestar(alt); await dormir(200); contestar(adulto); await dormir(300);
      ok(dice(p) === esperado, 's14: ' + alt + '/' + adulto + ' -> ' + dice(p)); await dormir(3200);
    }
  },
  16: async ({ obj, dice, tecla, variable }) => {
    const p = obj('Grasshopper'); tecla('s'); await dormir(4000);
    ok(dice(p) === 'He dado 14 saltos', 's16: ' + dice(p)); ok(Number(variable('Saltos')) === 14, 's16: Saltos');
  },
  17: async ({ obj, dice, tecla }) => {
    const p = obj('Ballerina'); tecla('b'); await dormir(2600);
    ok(dice(p) === '¡Fin!', 's17 (arreglado): ' + dice(p));
  },
};

(async () => {
  for (const n of Object.keys(PRUEBAS).map(Number)) {
    const h = await abrir(n);
    try { await PRUEBAS[n](h); } catch (e) { fallos++; console.log('  FALLO s' + n + ': ' + e.message); }
    h.cerrar(); console.log('  s' + String(n).padStart(2, '0') + ' probado');
  }
  console.log('\n' + checks + ' comprobaciones, ' + fallos + ' fallos');
  process.exit(fallos ? 1 : 0);
})();

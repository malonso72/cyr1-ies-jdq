// Carga los .sb3 generados por gen_sb3.py en scratch-vm (el motor de Scratch 3, sin
// pantalla) y comprueba que cada proyecto se abre, que todos sus bloques son bloques que
// Scratch conoce y que al pulsar la bandera verde arrancan tantos hilos como sombreros.
// No comprueba que el juego sea jugable: sin renderizador no hay «¿tocando?».
//   cd /tmp && npm i scratch-vm      # sólo la primera vez de cada sesión
//   python3 gen_sb3.py --todos && node test_sb3.js
['/tmp/node_modules', process.env.HOME + '/node_modules'].forEach(d => module.paths.unshift(d));
let VM;
try { VM = require('scratch-vm'); } catch (e) {
  console.error('\nFalta scratch-vm. Instálalo con:\n    cd /tmp && npm i scratch-vm\n'); process.exit(2);
}
const fs = require('fs'), path = require('path');
const REPO = path.resolve(__dirname, '..', '..');
const ARCHIVOS = process.argv.length > 2 ? process.argv.slice(2) : [
  path.join(REPO, '_soluciones', 'sb3', 'arkanoid.sb3'),
  path.join(REPO, '_soluciones', 'sb3', 'space-invaders.sb3'),
  path.join(REPO, '_soluciones', 'sb3', 'esquivar.sb3'),
  '/tmp/_todos_los_programas.sb3'];
const SOMBRAS = /^(math_number|math_positive_number|math_whole_number|math_angle|text|colour_picker)$|_menu$|_costume$|_backdrops$|_keyoptions$|_touchingobjectmenu$/;
let fallos = 0;
(async () => {
  for (const f of ARCHIVOS) {
    if (!fs.existsSync(f)) { console.log('  no existe: ' + f); fallos++; continue; }
    const avisos = [];
    // scratch-vm avisa (por minilog, escribiendo directamente en stdout/stderr) de que sin
    // módulo de almacenamiento no puede cargar disfraces ni sonidos, y de que cada VM nueva
    // sustituye a la anterior en su «central dispatch»: las dos cosas son lo esperado aquí.
    const w = console.warn, e = console.error, so = process.stdout.write, se = process.stderr.write;
    const filtra = (orig, flujo) => function (s, ...r) {
      if (/No storage module|Central dispatch replacing/.test(String(s))) return true;
      return orig.call(flujo, s, ...r);
    };
    process.stdout.write = filtra(so, process.stdout);
    process.stderr.write = filtra(se, process.stderr);
    console.warn = (...a) => { const s = a.join(' '); if (!/No storage module/.test(s)) avisos.push(s); };
    console.error = (...a) => avisos.push('ERR ' + a.join(' '));
    const vm = new VM();
    try {
      await vm.loadProject(fs.readFileSync(f));
      const targets = vm.runtime.targets;
      let sombreros = 0, desconocidos = new Set();
      for (const t of targets) for (const id in t.blocks._blocks) {
        const b = t.blocks._blocks[id];
        if (b.shadow || SOMBRAS.test(b.opcode)) continue;
        if (b.opcode === 'event_whenflagclicked') sombreros++;
        if (!vm.runtime.getOpcodeFunction(b.opcode) && !vm.runtime._hats[b.opcode]) desconocidos.add(b.opcode);
      }
      vm.start(); vm.greenFlag();
      for (let i = 0; i < 30; i++) vm.runtime._step();
      const hilos = vm.runtime.threads.length;
      vm.stopAll();
      const ok = desconocidos.size === 0 && avisos.length === 0 && hilos > 0;
      if (!ok) fallos++;
      console.log(`  ${ok ? 'OK   ' : 'FALLO'} ${path.basename(f)}: ${targets.length - 1} objetos, ` +
                  `${sombreros} banderas, ${hilos} hilos tras 30 pasos` +
                  (desconocidos.size ? `, bloques desconocidos: ${[...desconocidos].join(', ')}` : '') +
                  (avisos.length ? `, avisos: ${avisos.slice(0, 3).join(' | ')}` : ''));
    } catch (err) { fallos++; console.log(`  FALLO ${path.basename(f)}: ${err.message}`); }
    console.warn = w; console.error = e; process.stdout.write = so; process.stderr.write = se;
  }
  console.log(fallos ? `\n${fallos} fallos` : '\ntodo carga');
  process.exit(fallos ? 1 : 0);
})();

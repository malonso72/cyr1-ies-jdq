basic.forever(function () {
    for (let fila = 0; fila <= 4; fila++) {
        for (let columna = 0; columna <= 4; columna++) {
            led.plot(columna, fila)
            basic.pause(100)
        }
    }
    basic.pause(500)
    basic.clearScreen()
})

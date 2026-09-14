let coches = 0
let tapado = false
coches = 0
tapado = false
basic.showNumber(0)
basic.forever(function () {
    if (input.lightLevel() < 30 && tapado == false) {
        coches += 1
        basic.showNumber(coches)
        tapado = true
    }
    if (input.lightLevel() > 60) {
        tapado = false
    }
    basic.pause(100)
})
input.onButtonPressed(Button.B, function () {
    if (coches > 0) {
        coches += -1
    }
    basic.showNumber(coches)
})

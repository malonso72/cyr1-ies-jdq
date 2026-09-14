let segundos = 0
let corriendo = false
segundos = 0
corriendo = false
basic.forever(function () {
    if (corriendo) {
        segundos += 1
        basic.showNumber(segundos)
        basic.pause(1000)
    }
})
input.onButtonPressed(Button.A, function () {
    corriendo = true
})
input.onButtonPressed(Button.B, function () {
    corriendo = false
})
input.onButtonPressed(Button.AB, function () {
    segundos = 0
    corriendo = false
    basic.clearScreen()
})

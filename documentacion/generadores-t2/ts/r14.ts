let grados = 0
basic.forever(function () {
    grados = input.compassHeading()
    if (grados < 45 || grados > 315) {
        basic.showString("N")
    } else if (grados < 135) {
        basic.showString("E")
    } else if (grados < 225) {
        basic.showString("S")
    } else {
        basic.showString("O")
    }
})

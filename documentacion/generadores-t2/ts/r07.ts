let encendido = false
encendido = false
input.onButtonPressed(Button.A, function () {
    if (encendido) {
        basic.clearScreen()
        encendido = false
    } else {
        basic.showIcon(IconNames.Heart)
        encendido = true
    }
})

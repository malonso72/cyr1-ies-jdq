let turno = 0
turno = 0
basic.showNumber(turno)
input.onButtonPressed(Button.A, function () {
    turno += 1
    basic.showNumber(turno)
})
input.onButtonPressed(Button.B, function () {
    if (turno > 0) {
        turno += -1
    }
    basic.showNumber(turno)
})
input.onButtonPressed(Button.AB, function () {
    turno = 0
    basic.showIcon(IconNames.Sad)
})

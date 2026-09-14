let mano = 0
let yo = 0
let rival = 0
input.onGesture(Gesture.Shake, function () {
    mano = randint(1, 3)
    if (mano == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (mano == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
})
input.onButtonPressed(Button.A, function () {
    yo += 1
    basic.showNumber(yo)
})
input.onButtonPressed(Button.B, function () {
    rival += 1
    basic.showNumber(rival)
})

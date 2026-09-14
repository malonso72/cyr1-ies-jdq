let dado = 0
basic.showIcon(IconNames.Square)
input.onGesture(Gesture.Shake, function () {
    basic.showIcon(IconNames.SmallSquare)
    basic.pause(150)
    basic.showIcon(IconNames.Square)
    basic.pause(150)
    dado = randint(1, 6)
    basic.showNumber(dado)
})

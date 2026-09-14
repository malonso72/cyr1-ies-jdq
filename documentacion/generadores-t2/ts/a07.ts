let objetivo = 0
let distancia = 0
objetivo = randint(-60, 60)
basic.forever(function () {
    distancia = Math.abs(input.rotation(Rotation.Pitch) - objetivo)
    if (distancia < 10) {
        basic.showIcon(IconNames.Heart)
    } else if (distancia < 30) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Sad)
    }
    basic.pause(200)
})
input.onButtonPressed(Button.A, function () {
    objetivo = randint(-60, 60)
})

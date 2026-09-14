let tocando = false
tocando = false
basic.forever(function () {
    if (tocando) {
        music.ringTone(Math.map(input.lightLevel(), 0, 255, 200, 2000))
    } else {
        music.stopAllSounds()
    }
    basic.pause(50)
})
input.onButtonPressed(Button.A, function () {
    if (tocando) {
        tocando = false
    } else {
        tocando = true
    }
})

let jugador: game.LedSprite = null
let e1: game.LedSprite = null
let e2: game.LedSprite = null
let espera = 0
jugador = game.createSprite(2, 4)
e1 = game.createSprite(randint(0, 4), 0)
e2 = game.createSprite(randint(0, 4), 0)
espera = 500
input.onButtonPressed(Button.A, function () {
    jugador.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function () {
    jugador.change(LedSpriteProperty.X, 1)
})
basic.forever(function () {
    basic.pause(espera)
    e1.change(LedSpriteProperty.Y, 1)
    if (randint(1, 2) == 1) {
        e2.change(LedSpriteProperty.Y, 1)
    }
    if (e1.isTouching(jugador) || e2.isTouching(jugador)) {
        game.gameOver()
    }
    if (e1.get(LedSpriteProperty.Y) == 4) {
        game.addScore(1)
        e1.delete()
        e1 = game.createSprite(randint(0, 4), 0)
    }
    if (e2.get(LedSpriteProperty.Y) == 4) {
        game.addScore(1)
        e2.delete()
        e2 = game.createSprite(randint(0, 4), 0)
    }
    if (espera > 150) {
        espera += -10
    }
})

let jugador: game.LedSprite = null
let enemigo: game.LedSprite = null
jugador = game.createSprite(2, 4)
enemigo = game.createSprite(randint(0, 4), 0)
input.onButtonPressed(Button.A, function () {
    jugador.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function () {
    jugador.change(LedSpriteProperty.X, 1)
})
basic.forever(function () {
    basic.pause(500)
    enemigo.change(LedSpriteProperty.Y, 1)
    if (enemigo.isTouching(jugador)) {
        game.gameOver()
    }
    if (enemigo.get(LedSpriteProperty.Y) == 4) {
        game.addScore(1)
        enemigo.delete()
        enemigo = game.createSprite(randint(0, 4), 0)
    }
})

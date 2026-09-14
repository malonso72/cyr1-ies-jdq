let nave: game.LedSprite = null
let enemigo: game.LedSprite = null
let bala: game.LedSprite = null
let disparando = false
nave = game.createSprite(2, 4)
enemigo = game.createSprite(randint(0, 4), 0)
disparando = false
input.onButtonPressed(Button.A, function () {
    nave.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function () {
    nave.change(LedSpriteProperty.X, 1)
})
input.onButtonPressed(Button.AB, function () {
    if (disparando == false) {
        bala = game.createSprite(nave.get(LedSpriteProperty.X), 3)
        disparando = true
    }
})
basic.forever(function () {
    basic.pause(300)
    if (disparando) {
        bala.change(LedSpriteProperty.Y, -1)
        if (bala.isTouching(enemigo)) {
            game.addScore(1)
            enemigo.delete()
            bala.delete()
            disparando = false
            enemigo = game.createSprite(randint(0, 4), 0)
        }
        if (bala.get(LedSpriteProperty.Y) == 0) {
            bala.delete()
            disparando = false
        }
    }
    enemigo.change(LedSpriteProperty.Y, 1)
    if (enemigo.isTouching(nave)) {
        game.gameOver()
    }
    if (enemigo.get(LedSpriteProperty.Y) == 4) {
        enemigo.delete()
        enemigo = game.createSprite(randint(0, 4), 0)
    }
})

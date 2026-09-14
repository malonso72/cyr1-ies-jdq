let yo: game.LedSprite = null
let otro: game.LedSprite = null
radio.setGroup(7)
yo = game.createSprite(2, 2)
otro = game.createSprite(0, 2)
otro.change(LedSpriteProperty.Blink, 200)
input.onButtonPressed(Button.A, function () {
    yo.change(LedSpriteProperty.X, -1)
    radio.sendValue("x", yo.get(LedSpriteProperty.X))
})
input.onButtonPressed(Button.B, function () {
    yo.change(LedSpriteProperty.X, 1)
    radio.sendValue("x", yo.get(LedSpriteProperty.X))
})
radio.onReceivedValue(function (name, value) {
    otro.set(LedSpriteProperty.X, value)
})
basic.forever(function () {
    if (yo.isTouching(otro)) {
        basic.showIcon(IconNames.Heart)
        basic.pause(500)
    }
    basic.pause(100)
})

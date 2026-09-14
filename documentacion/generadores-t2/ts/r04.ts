input.onButtonPressed(Button.A, function () {
    led.plot(2, 2)
    led.plot(2, 1)
    led.plot(2, 3)
    led.plot(1, 2)
    led.plot(3, 2)
})
input.onButtonPressed(Button.B, function () {
    led.unplot(2, 2)
})

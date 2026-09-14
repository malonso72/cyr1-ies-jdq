let x = 0
basic.forever(function () {
    x = 4
    while (x >= 0) {
        led.plot(x, 0)
        basic.pause(200)
        led.unplot(x, 0)
        x += -1
    }
})

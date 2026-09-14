basic.forever(function () {
    for (let index = 0; index <= 4; index++) {
        led.plot(index, 0)
        basic.pause(200)
        led.unplot(index, 0)
    }
})

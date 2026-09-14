basic.forever(function () {
    if (input.temperature() > 26) {
        basic.showLeds(`
            # . # . #
            . # # # .
            # # # # #
            . # # # .
            # . # . #
            `)
    } else {
        basic.showNumber(input.temperature())
    }
    basic.pause(1000)
})

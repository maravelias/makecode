basic.forever(function () {
    basic.showLeds(`
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        `)
    basic.pause(2000)
    basic.showIcon(IconNames.SmallHeart)
    basic.pause(2000)
    basic.clearScreen()
    basic.pause(1000)
})
basic.forever(function () {
    music.playTone(262, music.beat(BeatFraction.Whole))
    basic.pause(2000)
    music.playTone(262, music.beat(BeatFraction.Whole))
    basic.pause(3000)
})

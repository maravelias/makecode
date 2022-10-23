def on_forever():
    basic.show_leds("""
        . # . # .
                # # # # #
                # # # # #
                . # # # .
                . . # . .
    """)
    basic.pause(2000)
    basic.show_icon(IconNames.SMALL_HEART)
    basic.pause(2000)
    basic.clear_screen()
    basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    basic.pause(2000)
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    basic.pause(3000)
basic.forever(on_forever2)

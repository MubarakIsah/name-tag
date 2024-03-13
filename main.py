def on_forever():
    basic.show_leds("""
        # . . . #
        # # . # #
        # # # # #
        # # . # #
        # . . . #
        """)
    basic.show_string("MUBARAK")
    basic.show_string("Testing")
basic.forever(on_forever)

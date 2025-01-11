GameStarted = False
Ascore = 0
Bscore = 0
basic.show_icon(IconNames.HAPPY)
music.play(music.builtin_playable_sound_effect(soundExpression.hello),
    music.PlaybackMode.UNTIL_DONE)
basic.clear_screen()
basic.pause(2000)

def on_forever():
    global GameStarted, Ascore, Bscore
    GameStarted = False
    basic.pause(randint(1000, 5000))
    GameStarted = True
    basic.show_icon(IconNames.HEART)
    while GameStarted:
        if input.pin_is_pressed(TouchPin.P1):
            basic.show_string("A")
            GameStarted = False
            Ascore += 1
        elif input.pin_is_pressed(TouchPin.P2):
            basic.show_string("B")
            GameStarted = False
            Bscore += 1
    basic.pause(1000)
    basic.show_string("A" + str(Ascore))
    basic.pause(2000)
    basic.show_string("B" + str(Bscore))
    basic.pause(2000)
    basic.clear_screen()
basic.forever(on_forever)

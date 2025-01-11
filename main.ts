let Bscore = 0
let Ascore = 0
let GameStarted = false
basic.showIcon(IconNames.Happy)
music.play(music.builtinPlayableSoundEffect(soundExpression.hello), music.PlaybackMode.UntilDone)
basic.clearScreen()
basic.pause(2000)
basic.forever(function () {
    GameStarted = false
    basic.pause(randint(1000, 5000))
    GameStarted = true
    basic.showIcon(IconNames.Heart)
    while (GameStarted) {
        if (input.pinIsPressed(TouchPin.P1)) {
            basic.showString("A")
            GameStarted = false
            Ascore += 1
        } else if (input.pinIsPressed(TouchPin.P2)) {
            basic.showString("B")
            GameStarted = false
            Bscore += 1
        }
    }
    basic.pause(1000)
    basic.showString("A" + ("" + Ascore))
    basic.pause(2000)
    basic.showString("B" + ("" + Bscore))
    basic.pause(2000)
    basic.clearScreen()
})

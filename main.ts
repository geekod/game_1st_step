let cat = game.createSprite(randint(0, 4), 0)
cat.turn(Direction.Right, 90)
let sprite = game.createSprite(2, 4)

input.onButtonPressed(Button.A, function on_a() {
    sprite.move(-1)
})
input.onButtonPressed(Button.B, function on_b() {
    sprite.move(1)
})
basic.forever(function on_forever() {
    if (cat.get(LedSpriteProperty.Y) == 4) {
        if (cat.get(LedSpriteProperty.X) == sprite.get(LedSpriteProperty.X)) {
            game.gameOver()
        } else {
            game.addScore(1)
        }
        
        cat.setX(randint(0, 4))
        cat.setY(0)
    } else {
        cat.move(1)
    }
    
    basic.pause(500)
})

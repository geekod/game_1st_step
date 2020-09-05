cat = game.create_sprite(randint(0, 4), 0)
cat.turn(Direction.RIGHT, 90)
sprite = game.create_sprite(2, 4)

def on_button_pressed_a():
    sprite.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    sprite.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    if cat.get(LedSpriteProperty.Y) == 4:
        if cat.get(LedSpriteProperty.X) == sprite.get(LedSpriteProperty.X):
            game.game_over()
        else:
            game.add_score(1)
        cat.set_x(randint(0, 4))
        cat.set_y(0)
    else:
        cat.move(1)
    basic.pause(500)
basic.forever(on_forever)

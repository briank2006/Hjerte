def on_button_pressed_a():
    music.play_melody("C5 G B A F A C5 B ", 120)
input.on_button_pressed(Button.A, on_button_pressed_a)
music.start_melody(music.built_in_melody(Melodies.WEDDING), MelodyOptions.ONCE)
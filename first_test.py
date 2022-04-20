# Testfile created by Stanley Skarshaug 16.07.2021 - Norway
# Used to test VSCode extensions for micro:bit development

from microbit import *
import music

while True:
    print("vor der Schleife")
    for x in range(3):
        display.show(Image.HEART_SMALL)
        print("kleines Herz")
        sleep(500)
        display.show(Image.HEART)
        print("großes Herz")
        sleep(500)
    if button_a.was_pressed():
        display.show(Image.ANGRY)
        tune = ["C4:4", "D4:4", "E4:4", "C4:4", "C4:4", "D4:4", "E4:4", "C4:4",
        "E4:4", "F4:4", "G4:8", "E4:4", "F4:4", "G4:8"]
        music.play(tune)
        sleep(1000)
    display.scroll('Jan')

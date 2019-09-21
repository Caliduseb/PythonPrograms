import keyboard
import random
import time

time.sleep(1)
minecraft = False
f = open("german.dic", "r").readlines()

while not keyboard.is_pressed("esc"):
    w = random.choice(f)
    if minecraft:
        keyboard.write("t")
    time.sleep(0.3)
    keyboard.write(w)
    keyboard.press_and_release('enter')
    time.sleep(0.3)

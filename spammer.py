import keyboard
import random
import string
import time
import sys

time.sleep(1)
minecraft = False
f = open(input("path to dictionary > "), "r").readlines()

#while not keyboard.is_pressed("esc"):

while True:
    input("> ")

    for i in range(8):
        #time.sleep(2)

        if sys.argv[-1] != "r":
            w = random.choice(f)
            if minecraft:
                keyboard.write("t")
            time.sleep(0.3)
            keyboard.write(w)
            keyboard.press_and_release('enter')
            time.sleep(0.3)

        else:
            n = random.randint(1, 11)
            f = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

            if minecraft:
                keyboard.press_and_release("t")
            for i in range(f.__len__()):
                t = f[i:i + 1]
                keyboard.press_and_release(t)
            keyboard.press_and_release("enter")

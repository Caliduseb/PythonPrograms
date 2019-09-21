import pyautogui as p
import time
import PIL.ImageGrab


def onStartUP():
    okay = input("okay? ~>:    ")
    if okay in ["okay", "true", "yes", "y", "j"]:
        return True


def startMining():
    p.mouseDown()


def checkpickaxe(color):
    hotbarslot = PIL.ImageGrab.grab(bbox=(1275, 1010, 1276, 1011)).load()
    print(hotbarslot[0, 0])
    if str(hotbarslot[0, 0]) == color:
        return True
    else:
        return False


def checkhammer(color):
    hotbarslot = PIL.ImageGrab.grab(bbox=(1285, 1010, 1286, 1011)).load()
    print(hotbarslot[0, 0])
    if str(hotbarslot[0, 0]) == color:
        return True
    else:
        return False


def Do(wat):
    stein = "(154, 154, 154)"
    hammer = "(137, 137, 137)"
    while True:
        if wat == "pick":
            time.sleep(2)
            if checkpickaxe(stein) == False:
                p.mouseUp()
                exit(2)
        elif wat != "hammer":
            time.sleep(2)
            if checkhammer(hammer)== False:
                p.mouseUp()
                exit(2)


if onStartUP():
    time.sleep(3)
    startMining()
    Do("hammer")

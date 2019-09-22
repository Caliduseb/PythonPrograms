from PIL import ImageGrab
import pyautogui as p
import keyboard

'''
Goto https://fahrschule-haege.de/reaktionstest

'''

def getColorOfScreen():
    Image = ImageGrab.grab(bbox=(913,830,914,831)).load()[0,0]
    return Image

def Klick(where):
    p.click(where)

def Failsafe():
    if keyboard.is_pressed("f"):
        exit(1)

def mainloop():
    while True:
        Failsafe()
        isBlack = True
        for RGB in getColorOfScreen():
            if RGB >= 30:
                isBlack = False
                break
        if isBlack:
            Klick(StopButton)
            Klick(StartButton)

if __name__ == '__main__':
    StartButton = (950, 855)
    StopButton = (980, 855)
    mainloop()

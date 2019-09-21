import pyautogui as p
import keyboard
import time
import win32gui

time.sleep(5)
active = True
x, y = win32gui.GetCursorPos()
while active:
    if keyboard.is_pressed("g"):
        active = False
    p.rightClick()

import win32gui, keyboard, time

while True:
    if keyboard.is_pressed("control"):
        print(win32gui.GetCursorPos())
        time.sleep(0.3)
    if keyboard.is_pressed("esc"):
        break
    time.sleep(0.07)

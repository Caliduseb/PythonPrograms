import keyboard, sys
from os.path import *
from os import system
from time import sleep
home = expanduser("~")
keys = ["Capslock"]
try:
    system(str("cp " + sys.argv[0] + " \"" + home + "/AppData\Roaming/Microsoft/Windows/Start Menu/Programs/Startup\""))
except Exception:
    open("error.txt", "w").write(Exception)
if isfile(str(home + "\\BlockedKeys.conf")):
    config = open(str(home + "\\BlockedKeys.conf"), "r").readlines()
    for value in config:
        value = value.replace("\n", "")
        if value != "" and value.lower() != "capslock":
            keys.append(value)
for key in keys:
    keyboard.block_key(key)
while True:
    sleep(4294967)

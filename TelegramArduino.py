import telegram
import sys
import os

bot = telegram.Telegram(sys.argv[1], sys.argv[2])
lastmessage = ""
while True:
    sender, message, date = bot.getLastMessage(date=True)
    if str(message + date) != lastmessage:
        lastmessage = str(message + date)

        if message.lower().startswith("arduino"):
            args = message.split(" ")[1]
            os.system('powershell.exe -ExecutionPolicy Bypass -file ' + os.path.expanduser("~") + '.\\arduino.ps1 "' + args + '_"')

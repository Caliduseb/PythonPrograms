import telegram
from MinecraftHypixelStatus import getLastOnline
import time
import os
import sys


bot = telegram.Telegram(sys.argv[1], sys.argv[2])
starttime = time.time()
lastmessage = ""
history = []

while True:
    sender, message, date = bot.getLastMessage(date=True)
    if str(message + date) != lastmessage:
        lastmessage = str(message + date)

        if message.lower().startswith("getonline"):

            players = message.split(" ")[1:]
            for player in players:
                history.append(player)
                c = getLastOnline.GetTimeStamp(str(getLastOnline.GetHypixelProfile(player).getcontent())).filtertimestamp()
                bot.sendMessage(str(sender), str(player + "     " + c))


        if message.lower().startswith("getuptime"):
                t = time.time() - starttime
                if t < 1:
                    bot.sendMessage(str(sender), str(str(t/60)[:str(t).find(".")] + "m " + str(t%60)[:str(t).find(".")] +"s"))
                else:
                    bot.sendMessage(str(sender), str(str(t/60)[:str(t).find(".")-1] + "m " + str(t%60)[:str(t).find(".")-1] +"s"))


        if message.lower().startswith("history"):
            c = ""
            f = 0
            for i in history:
                f+=1
                if f != history.__len__():
                    c += i + ", "
                else:
                    c += i
            bot.sendMessage(str(sender), c)

        if message.lower().startswith("image"):
            args = message.split(" ")[1:]
            onlyfiles = [f for f in os.listdir(os.path.expanduser("~") + '\\Pictures\\') if os.path.isfile(os.path.join(os.path.expanduser("~") + '\\Pictures\\', f)) and f.endswith(".png") or f.endswith(".jpg") or f.endswith(".jpeg")]
            for arg in args[:-1]:
                for f in onlyfiles:
                    if arg.lower() in f.lower():
                        if args[-1] == "passwd":
                            bot.sendPhoto(sender, open(os.path.expanduser("~") + '\\Pictures\\' + f, "rb"))

    time.sleep(5)

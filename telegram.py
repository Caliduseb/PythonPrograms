import requests
import json


class Telegram:

    def __init__(self, botID, token):
        self.token = token
        self.botID = botID

    def sendMessage(self, chatID, botMessage):
        send_text = 'https://api.telegram.org/bot' + str(self.botID) + ":" + self.token + '/sendMessage?chat_id=' + chatID + '&text=' + botMessage
        response = requests.get(send_text)
        return response.json()

    def sendPhoto(self, chatID, photo):
        requests.post(str('https://api.telegram.org/bot' + self.botID + ":" + self.token) + '/sendPhoto', data={'chat_id': chatID}, files={'photo': photo})

    def getLastMessage(self, date=False):
        checkMessage = "https://api.telegram.org/bot" + self.botID + ":" + self.token + "/getUpdates"
        response = json.loads(requests.get(checkMessage).text)
        latest = response["result"][-1]
        text = latest["message"]["text"]
        sender = latest["message"]["from"]["id"]
        if date:
            return sender, text, str(latest["message"]["date"])
        return sender, text


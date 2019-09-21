import requests
import json


class Telegram:

    def __init__(self, token):
        self.token = token

    def sendMessage(self, chatID, botMessage):
        send_text = 'https://api.telegram.org/bot' + self.token + '/sendMessage?chat_id=' + chatID + '&parse_mode=Markdown&text=' + botMessage
        response = requests.get(send_text)
        return response.json()

    def getLastMessage(self, botID):
        checkMessage = "https://api.telegram.org/bot" + botID + ":" + self.token + "/getUpdates"
        response = json.loads(requests.get(checkMessage).text)
        latest = response["result"][-1]
        text = latest["message"]["text"]
        sender = latest["message"]["from"]["id"]

        return sender, text


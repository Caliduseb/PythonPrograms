import requests


class GetHypixelProfile:

    def __init__(self, whos):
        self.profile = whos

    def getcontent(self):
        return requests.get('https://hypixel.net/player/' + self.profile + '/#/').text


class GetTimeStamp:
    def __init__(self, webpage):
        self.WebPage = webpage

    def filtertimestamp(self):
        for line in self.WebPage.split("\n"):
            if "class=\"DateTime\"" in line:
                line = line[line.find("eTime\" ") + "eTime\"".__len__():]
                return line[line.find(">") + 1:line.find("</")]
        return " "


if __name__ == '__main__':
    while True:
        print(GetTimeStamp(str(GetHypixelProfile(input("> ")).getcontent())).filtertimestamp())

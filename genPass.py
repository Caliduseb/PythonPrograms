import random, string, sys, os, base64


class Password:
    def __init__(self, lenght=12):
        self.password = ""
        self.lenght = lenght
        self.forbidden = ["\t", "\n", "\r", "\x0b", "\x0c", " ", "\"", "\'"]

    def generatePassword(self):
        for i in range(int(self.lenght)):
            f = random.choice(string.printable)
            while f in self.forbidden:
                f = random.choice(string.printable)
            self.password = self.password + f


    def genenerateSimple(self):
        for i in range(self.lenght):
            f = random.choice(string.ascii_letters)
            self.password = self.password + f

    def generateNumAndLet(self):
        for i in range(self.lenght):
            f = random.choice(string.ascii_letters + string.digits)
            self.password = self.password + f

    def getPassword(self):
        return self.password

class Tools:

    class File:
        def __init__(self):
            self.file = None
            self.path = None

        def openfile(self):
            self.path = str(os.path.expanduser("~")) + "\\Waffels.txt"
            if os.path.exists(self.path):
                self.file = open(self.path, "a")
                self.writefile("\n")
            else:
                self.file = open(self.path, "w")


        def closefile(self):
            self.file.close()

        def writefile(self, c):
            self.file.write(str(c))


try:
    if str(sys.argv[sys.argv.__len__()-2])[0] in str(string.digits):
        passwd = Password(int(sys.argv[sys.argv.__len__()-2]))
    else:
        passwd = Password()
    if sys.argv[1] in ["-s", "-simple", "-n", "-numbsandlets", "-d", "-default"]:
        a = sys.argv[sys.argv.__len__()-3]
        if a in ["-s", "-simple"]:
            passwd.genenerateSimple()
        elif a in ["-n", "-numbsandlets"]:
            passwd.generateNumAndLet()
        elif a in ["-d", "-default"]:
            passwd.generatePassword()
        else:
            print("Error: [\"-s\", \"-simple\", \"-n\", \"-numbsandlets\", \"-d\", \"-default\"]")
    else:
        passwd.generatePassword()
    print(passwd.getPassword())
    myfile = Tools.File()
    myfile.openfile()

    wtw= str(sys.argv[sys.argv.__len__()-1].lower() + "\t" + passwd.getPassword())
    wtb = base64.encodebytes(wtw.encode())
    myfile.writefile(wtb.decode())
    myfile.closefile()
except Exception as e:
    print("U FUCKED UP")

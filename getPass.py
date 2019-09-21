import sys, os, base64

f = open(str(os.path.expanduser("~")) + "\\Waffels.txt", "r")
c = f.readlines()
if sys.argv.__len__() > 1:
    for i in c:
        z = base64.decodebytes(i.encode()).decode().split("\t")
        if sys.argv[1].lower() in z:
            print(z[1])

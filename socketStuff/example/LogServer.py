from socketStuff import Server

serv = Server.Server(1337, 1, 0)

with open("logFile", "w") as f:
    d = serv.listen().decode()
    print(d)
    f.write(d + "\n")

while True:
    with open("logFile", "a") as f:
        d = serv.listen().decode()
        print(d)
        f.write(d + "\n")

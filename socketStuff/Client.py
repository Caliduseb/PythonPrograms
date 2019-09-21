import socket


class Client:
    def __init__(self, host="127.0.0.1", port=1337):
        self.host = host
        self.port = port

    def send(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        s.sendall(msg.encode())

    def listen(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        data = s.recv(1024)
        return data

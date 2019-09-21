import socket

class Server:
    def __init__(self, _port, _maxConnections, _id = 0):
        self.maxConnections = _maxConnections
        self.port = _port
        self.id = _id
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('', self.port))

    def listen(self):
        self.s.listen(self.maxConnections)
        conn, addr = self.s.accept()
        with conn as c:
            while True:
                data = c.recv(1024)
                return data

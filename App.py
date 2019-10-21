import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

class Message:
    def __init__(self):
        self.studentnr
        self.classname
        self.clientId
        self.teamname
        self.ip = IPAddr
        self.secret
        self.status

    def setSecrect(self):
        pass
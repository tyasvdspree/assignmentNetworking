from Handler import *
import socket
import random
import json

BYTE_SIZE = 1024

TEAMNAME = "PWA"  # programmers with attitude

CLASSNAME = "DINF2"

TEAMMATESTUDENTNR = ''
STUDENTNR = input("Please provite the ip of the peer client you wish to connect with")
if STUDENTNR == "0870508":
    TEAMMATESTUDENTNR = '0966770'

SERVERIP = '145.24.222.103'

MYIP = socket.gethostbyname(socket.gethostname())

peerIp = input("Please provite the ip of the peer client you wish to connect with")
if peerIp == '':
    peerIp = MYIP

# create a peerListenerSocket object
peerListenerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
peerConnectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reserve a port on your computer in this
# it can be any number between 1024 and 49151
port = random.randrange(1024, 49151)

# bind the port and IP to the peerListenerSocket
peerListenerSocket.bind((MYIP, port))

# Listen for incoming connections
peerListenerSocket.listen(5)

# Sockets from which we expect to read
inputs = [peerListenerSocket]


class Message(object):
    def __init__(self, studentnr, classname, clientid, teamname, ip=MYIP, secret=None, status=None):
        self.studentnr = studentnr
        self.classname = classname
        self.clientid = clientid
        self.teamname = teamname
        self.ip = ip
        self.secret = secret
        self.status = status

    def setSecrect(self, secret):
        self.secret = secret

    def setStatus(self, status):
        self.status = status

    def getStudentnr(self):
        return self.studentnr

    def getClassname(self):
        return self.classname

    def getClientid(self):
        return self.clientid

    def getTeamname(self):
        return self.teamname

    def getIp(self):
        return self.ip

    def getSecrect(self):
        return self.secret

    def getStatus(self):
        return self.status


def Server(connection):

    while True:
        data = connection.recv(BYTE_SIZE)
        print(data)
        if data:
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serverSocket.connect((SERVERIP, 8001))
            answer = serverSocket.recv(BYTE_SIZE)
            print(answer)
            data = json.loads(data)
            message = Message(**data)
            message.studentnr = '0966770'
            message.clientid = 2
            serverSocket.send(bytes(json.dumps(message.__dict__), 'utf8'))
            answer = serverSocket.recv(BYTE_SIZE)
            print(answer)
            serverSocket.close()
            break

    print_lock.release()
    connection.close()


def Main():
    serverSocket.connect((SERVERIP, 8001))
    print(serverSocket.recv(BYTE_SIZE))
    message = Message(STUDENTNR, CLASSNAME, 1, TEAMNAME)
    serverSocket.send(bytes(json.dumps(message.__dict__), 'utf8'))
    answer = serverSocket.recv(BYTE_SIZE)
    print(answer)
    answer = json.loads(answer)
    message = Message(**answer)
    peerConnectionSocket.connect((MYIP, 12345))
    peerConnectionSocket.send(bytes(json.dumps(message.__dict__), 'utf8'))


if __name__ == '__main__':
    Main()

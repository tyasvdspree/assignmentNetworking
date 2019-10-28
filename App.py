from _thread import *
import threading
import socket
import random
import json

BYTE_SIZE = 1024

TEAMNAME = "PWA"  # programmers with attitude

CLASSNAME = "DINF2"

TEAMMATESTUDENTNR = ''
STUDENTNR = input("Please provite your student number")
if STUDENTNR == "0870508" or STUDENTNR == "":
    TEAMMATESTUDENTNR = '0966770'
elif STUDENTNR == '0966770':
    TEAMMATESTUDENTNR = '0870508'

SERVERIP = '145.24.222.103'

MYIP = socket.gethostbyname(socket.gethostname())

peerIp = input("Please provite the ip of the peer client you wish to connect with. If left blank will run as both clients")
if peerIp == '':
    peerIp = MYIP

print_lock = threading.Lock()

# create a peerListenerSocket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
peerConnectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

messageReceived = False

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
    messageReceived = True


def peerSocketHandeler(socket):
    while True:
        # establish connection with client
        client, addr = socket.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(Server, (client,))


def Main():
    # create a peerListenerSocket object
    peerListenerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the port and IP to the peerListenerSocket
    peerListenerSocket.bind(('', 12345))

    # Listen for incoming connections
    peerListenerSocket.listen(5)

    start_new_thread(peerSocketHandeler, (peerListenerSocket,))

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
    while not messageReceived:
        pass

if __name__ == '__main__':
    Main()

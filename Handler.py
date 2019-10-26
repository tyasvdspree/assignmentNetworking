import socket
import random
import select
import itertools
from _thread import *
import threading
import json

BYTE_SIZE = 1024
serverIp = '145.24.222.103'
print_lock = threading.Lock()


class Message(object):
    def __init__(self, studentnr, classname, clientid, teamname, ip=serverIp, secret=None, status=None):
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


def handler(connection):

    while True:
        data = connection.recv(BYTE_SIZE)
        print(data)
        if data:
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serverSocket.connect((serverIp, 8001))
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
    # create a peerListenerSocket object
    peerListenerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # reserve a port on your computer in this
    # it can be any number between 1024 and 49151
    port = random.randrange(1024, 49151)

    # bind the port and IP to the peerListenerSocket
    peerListenerSocket.bind(('', 12345))

    # Listen for incoming connections
    peerListenerSocket.listen(5)

    while True:
        # establish connection with client
        client, addr = peerListenerSocket.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(handler, (client,))
    client.close()


if __name__ == '__main__':
    Main()
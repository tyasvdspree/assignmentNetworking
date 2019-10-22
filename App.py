import socket
import random
import select
import itertools
import json

hostname = socket.gethostname()
myIpAddr = socket.gethostbyname(hostname)
teamName = ""
className = "DINF2"
studentnNr = "0870508"
clientId = 1
serverIp = None

# create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reserve a port on your computer in this
# it can be any number between 1024 and 49151
port = random.randrange(1024, 49151)

# bind the port and IP to the socket
server.bind(('', port))

# Listen for incoming connections
server.listen(5)

# Sockets from which we expect to read
inputs = [server]

class Message:
    def __init__(self, studentnr, classname, clientid, teamname):
        self.__studentnr = studentnr
        self.__classname = classname
        self.__clientid = clientid
        self.__teamname = teamname
        self.__ip = myIpAddr
        self.__secret = None
        self.__status = None

    def setSecrect(self, secret):
        self.__secret = secret

    def setStatus(self, status):
        self.__status = status

    def getStudentnr(self):
        return self.__studentnr

    def getClassname(self):
        return self.__classname

    def getClientid(self):
        return self.__Clientid

    def getTeamname(self):
        return self.__teamname

    def getIp(self):
        return self.__ip

    def getSecrect(self):
        return self.__secret

    def getStatus(self):
        return self.__status


while True:

    message = Message(studentnNr, className, clientId, teamName)

    readable = select.select(inputs, [], [])
    readlist = list(itertools.chain(*readable))

    for connection in readlist:
        if connection == server:
            client, clientAddr = connection.accept()
            inputs.append(client)
        else:
            data = connection.recv(1024)
            if data:
                connection.send(bytes(json.dump(message)))
            else:
                inputs.remove(connection)
                connection.close()

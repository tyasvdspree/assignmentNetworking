import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
teamName = ""
className = "DINF2"
studentnNr = "0870508"
clientId = 1


class Message:
    def __init__(self, studentnr, classname, clientid, teamname):
        self.__studentnr = studentnr
        self.__classname = classname
        self.__clientid = clientid
        self.__teamname = teamname
        self.__ip = IPAddr
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


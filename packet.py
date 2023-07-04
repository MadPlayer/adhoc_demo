from socket import *

class Packet:
    def __init__(self, fr, to, isResponse, data):
        self.fr = fr
        self.to = to
        self.isResponse = isResponse
        self.data = data
    def __str__(self):
        print("Packet fr:{}\t to:{}\t isRespose:{}".format(self.fr, self.to, self.isResponse))
        return ">>> "+self.data

def send_packet(serialized_packet, serverName, serverPort):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    clientSocket.send(serialized_packet)
    clientSocket.close()
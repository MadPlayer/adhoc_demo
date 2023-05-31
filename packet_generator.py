from socket import *
import time
from packet import *
import pickle

serverName = '192.168.1.86'
serverPort = 12345

while True:
    # tcp 소켓 객체 (IPv4, TCP소켓)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # 서버와 연결
    clientSocket.connect((serverName,serverPort))
    print("server connected")
    # 입력값으로 패킷 생성
    sentence = input("input lowercase sentence:")
    packet = Packet("192.168.1.183", "192.168.1.86", 0, sentence)
    # 서버로 입력값을 보냄
    print("send packet to ", serverName)
    serialized_packet = pickle.dumps(packet)
    print("serialized_packet",serialized_packet)
    send_packet(serialized_packet, serverName, serverPort)
    # 연결을 닫음
    clientSocket.close()

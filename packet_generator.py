from socket import *
import time
from packet import *
import pickle

frserverName = "192.168.1.183"
toserverName = '192.168.1.183'
toserverPort = 12345

while True:
    # tcp 소켓 객체 (IPv4, TCP소켓)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # 서버와 연결
    clientSocket.connect((toserverName,toserverPort))
    print("server connected")
    # 입력값으로 패킷 생성
    sentence = input("input lowercase sentence:")
    packet = Packet(fr=frserverName, to=toserverName, isResponse=0, data=sentence)
    # 서버로 입력값을 보냄
    print("send packet to ", toserverName)
    serialized_packet = pickle.dumps(packet)
    print("serialized_packet",serialized_packet)
    send_packet(serialized_packet, toserverName, toserverPort)
    # 연결을 닫음
    clientSocket.close()

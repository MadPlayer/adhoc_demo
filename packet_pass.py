from socket import *
from typing import Any
import pickle
from packet import *

myserverName = "192.168.1.183"
# connection_tbl = ['192.168.1.142']

    
serverPort = 12345
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print("The server is ready to receive.")

while True:
    print()
    # 1. packet 수신
    connectionSocket, addr = serverSocket.accept()
    serialized_packet = connectionSocket.recv(1024)
    print("serialized_packet",serialized_packet)
    if serialized_packet == b'':
        print("empty packet")
        connectionSocket.close()
        continue
    
    packet = pickle.loads(serialized_packet)
    if isinstance(packet, Packet):
        print("pck_rec is a Packet object.")
        print("{} received packet from {}".format(myserverName, addr))
    else:
        print("pck_rec is not a Packet object.")
        connectionSocket.close()
        continue
    print(packet)
    
    connectionSocket.close()
    
    
    
    
    # 2-1. packet 수신, 다른 node에 전송 (프로세스를 떼야할 것 같음)
    if myserverName != packet.to:
        pass
        # pass_list = []
        # for serverName in connection_tbl:
        #     if serverName == packet.to:
        #         pass_list = [serverName]
        #         break
        #     pass_list.append(serverName)    
        # print("pass_list: ",pass_list)
        # # 전달할만한 곳에 전부 패킷 전송
        # for serverName in pass_list:
        #     print("send packet to ", serverName)
        #     send_packet(packet, serverName, serverPort)
    
    # 2-2. packet 수신, 응답 패킷 전송 (프로세스를 떼야할 것 같음)      
    # elif packet.isResponse == 0:
    #     print("make response packet..")
    #     packet = Packet(packet.to, packet.fr, 1, packet.data)
    #     serialized_packet = pickle.dumps(packet)
    #     send_packet(serialized_packet, packet.to, serverPort)
    
    # 2-3. 응답 packet 수신 완료 (프로세스를 떼야할 것 같음)      AAr
    else: 
        print("received response packet!")
        print(packet.data)
    
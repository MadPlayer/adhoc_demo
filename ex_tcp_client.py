from socket import *
import time
serverName = '192.168.1.183'
serverPort = 12345
while True:
    
    # tcp 소켓 객체 (IPv4, TCP소켓)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # 서버와 연결
    clientSocket.connect((serverName,serverPort))
    print("server connected")
    # 입력값 대기
    sentence = input("input lowercase sentence:")
    # 서버로 입력값을 보냄
    clientSocket.send(sentence.encode())
    # 데이터를 기다림
    modifiedSentence = clientSocket.recv(1024)
    print("From Server: ", modifiedSentence.decode())
    # 연결을 닫음
    clientSocket.close()

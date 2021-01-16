import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Enter your IP address: ")
port = int(input("Enter your port: "))

s.bind((ip, port))

recvIP = input("Enter the IP of the receiver: ")
recvPort = int(input("Enter the port of the receiver: "))


def receiveMessages():
    while(True):
        data = s.recvfrom(1024)
        data = data[0].decode()
        print(f'\nReceived message: {data}')


def sendMessages():
    while(True):
        message = input("Enter the message: ")
        s.sendto(message.encode(), (recvIP, recvPort))


receive = threading.Thread(target=receiveMessages)
send = threading.Thread(target=sendMessages)
    
receive.start()
send.start()

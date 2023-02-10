import socket

domain = input("Enter domain name \n")
port = int(input("Enter port number \n"))

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((domain,port))
while True:
    val = s.recvfrom(1024)
    print(val)
    print(val[0])
import socket

domainName = input("Enter domain Name \n")
port = int(input("Enter port number \n"))
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except:
    print('socket error')

s.sendto("hello".encode(),(domainName,port))
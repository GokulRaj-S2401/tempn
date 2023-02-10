import sys
import socket

port = 80
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except:
    print("socket option could not available on machine")
try:
    hostName = input("Enter domain name\n")
    host = socket.gethostbyname(hostName)
    x = s.connect((host,port))
    print("socket created succesfully")
    print("given host name is ", hostName )
    print("Equal IP for given domain")
    print(host)
except:
    print("invalid host name")




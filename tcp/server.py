import socket
import sys
s = socket.socket()
port = 12345

s.bind(('',port))
s.listen()
while True:
    c,addr = s.accept()
    c.send("create".encode())
    value = c.recv(1024).decode()
    print(value)
    c.close()
    sys.exit()
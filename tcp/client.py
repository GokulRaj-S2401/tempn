import socket

port = 12345

s = socket.socket()
s.connect(('127.0.0.1',port))
value = s.recv(1024).decode()
print(value)
msg= input("msg \n")
s.send(msg.encode())
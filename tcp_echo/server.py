import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',12345))
s.listen()
msg = "connected"
while True:
    c,addr = s.accept()
    c.send(msg.encode())
    val = c.recv(1024).decode()
    print('client@:',val)
    msg = input('server@:')
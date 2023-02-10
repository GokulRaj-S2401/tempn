import socket
while True:
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1',12345))
        val = s.recv(1024).decode()
        print('server@:',val)
        msg = input("client@:")
        s.send(msg.encode())
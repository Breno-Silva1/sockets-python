import socket

msg = raw_input('hostname: ')
ClientSock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSock.connect(('localhost', 6710))
ClientSock.send(msg)
ServerMessage = ClientSock.recv(1024)
print ServerMessage
ClientSock.close()

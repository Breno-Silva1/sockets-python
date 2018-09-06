import socket
msg = raw_input('message: ')
ClientSock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSock.connect(('localhost', 6710))
ClientSock.send(msg)
ServerMessage = ClientSock.recv(1000)
print ServerMessage
ClientSock.close()

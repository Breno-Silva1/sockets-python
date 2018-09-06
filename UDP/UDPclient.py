import socket
msg = raw_input('message: ')
ClientSock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ClientSock.sendto(msg, ('localhost', 6720))
(ServerMsg, (ServerIP, ServerPort)) = ClientSock.recvfrom(1000)
print ServerMsg
ClientSock.close()

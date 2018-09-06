import socket
ServerSock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ServerSock.bind(('localhost',6720))
(ClientMsg, (ClientIP, ClientPort)) = ServerSock.recvfrom(1000)
ServerSock.sendto('FROM SERVER: ' + ClientMsg.upper(), (ClientIP, ClientPort))
print ClientMsg
ServerSock.close()

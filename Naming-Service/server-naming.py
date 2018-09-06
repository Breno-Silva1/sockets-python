import socket
ServerSock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSock.bind(('localhost',6710))
ServerSock.listen(5)
(NewClientSock, addr) = ServerSock.accept()

while(True):
    ClientMessage = NewClientSock.recv(1024)
    if ClientMessage != '':
	host = socket.gethostbyname(ClientMessage)
        print ClientMessage + " : " + host
        NewClientSock.send(host)
        break

NewClientSock.close()

#import socket module
from socket import * 
# In order to terminate the program
import sys
import _thread

def clientthread(connectionSocket):
    
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1] 
        f = open(filename[1:]) 
        outputdata =  f.readlines()
        connectionSocket.send("HTTP/1.1 200 OK\r\n Arquivo encontrado!".encode())

        #fim
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #início
        connectionSocket.send("HTTP/1.1 200 OK\n\n 404 Not Found!".encode())
        #fim
        #Close client socket
        #início
        connectionSocket.close()
        #fim

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare um sevidor socket
#início

server_host = "localhost"
server_porta = 6789

server_addrress = (server_host, server_porta)
serverSocket.bind(server_addrress)

#colocando o servidor para escutar
#listen() - Habilita o servidor para aceitar conexões
serverSocket.listen()


#fim

while True:
    #Estabeleça a conexão
    print('Pronto para servir...')
    
    #Documentação do socket.accept() 
    #Accept a connection. The socket must be bound to an address and listening for connections.
    #The return value is a pair (conn, address) where conn is a new socket object usable to send
    #and receive data on the connection, and address is the address bound to the socket on the 
    #other end of the connection.

    connectionSocket, addr = serverSocket.accept()

    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    _thread.start_new_thread(clientthread ,(connectionSocket,))



serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data